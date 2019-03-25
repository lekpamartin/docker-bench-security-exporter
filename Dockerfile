FROM alpine:3.9
LABEL maintainer="LEKPA"

RUN \
	apk upgrade --no-cache && \
	apk add --no-cache \
		docker \
		dumb-init && \
	rm -rf /usr/bin/docker-* /usr/bin/dockerd && \
	mkdir /usr/local/bin/tests && \
	pip install --no-cache-dir --upgrade requests pip

COPY files/exporter.py /exporter.py

CMD [ "python", "/exporter.py" ]
