FROM alpine:3.9
LABEL maintainer="LEKPA"

RUN \
	apk upgrade --no-cache && \
	apk add --no-cache \
		docker \
		iproute2 \
		git \
		curl \
		python3 \
		dumb-init && \
	rm -rf /usr/bin/docker-* /usr/bin/dockerd && \
	git clone https://github.com/docker/docker-bench-security.git /opt/docker-bench-security && \
	echo "/opt/docker-bench-security/docker-bench-security.sh \$ARGS > /dev/null" >> /etc/periodic/daily/0-docker-bench-security

WORKDIR /opt/docker-bench-security

HEALTHCHECK --interval=5m --timeout=3s \
	CMD curl -f http://$DOCKERBENCHEXPORTER_SERVER_NAME:$DOCKERBENCHEXPORTER_SERVER_PORT/ || exit 1

COPY files/exporter.py /exporter.py

CMD [ "python3", "/exporter.py" ]
