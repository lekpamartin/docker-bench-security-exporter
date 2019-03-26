FROM alpine:3.9
LABEL maintainer="LEKPA"

RUN \
	apk upgrade --no-cache && \
	apk add --no-cache \
		docker \
		iproute2 \
		git \
		python3 \
		dumb-init && \
	rm -rf /usr/bin/docker-* /usr/bin/dockerd && \
	git clone https://github.com/docker/docker-bench-security.git /opt/docker-bench-security && \
	addgroup docker-bench && adduser -S -D -G docker-bench -h /opt/docker-bench-security docker-bench && \
	chown -R docker-bench:root /opt/docker-bench-security && \
	echo "0 11 * * 1-5 docker-bench /opt/docker-bench-security/docker-bench-security.sh \$ARGS > /dev/null" >> /etc/crontab

USER docker-bench

WORKDIR /opt/docker-bench-security

COPY files/exporter.py /exporter.py

CMD [ "python3", "/exporter.py" ]
