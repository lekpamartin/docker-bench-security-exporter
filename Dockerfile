FROM alpine:3.9
LABEL maintainer="LEKPA"

RUN \
	apk upgrade --no-cache && \
	apk add --no-cache \
		docker \
		git \
		python3 \
		dumb-init && \
	rm -rf /usr/bin/docker-* /usr/bin/dockerd && \
	mkdir /usr/local/bin/tests && \
	cd /tmp && \
	git clone https://github.com/docker/docker-bench-security.git

WORKDIR tmp/docker-bench-security

COPY files/exporter.py /exporter.py

CMD [ "python3", "/exporter.py" ]
