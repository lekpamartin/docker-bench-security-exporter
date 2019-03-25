FROM alpine:3.9
LABEL maintainer="LEKPA"

COPY files/exporter.py /exporter.py

RUN pip install --no-cache-dir --upgrade requests pip

CMD [ "python", "/exporter.py" ]
