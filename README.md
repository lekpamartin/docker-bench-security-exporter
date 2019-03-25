# docker-bench-security-exporter


## Requirements

* Python
* [requests](http://www.python-requests.org/en/master/)

## Running

Accepted parameters:

* server_name (optional): Name to bind the HTTP server to. Default: 0.0.0.0
* server_port (optional): Port to bind the HTTP server to. Default: 9700

You can either pass script arguments (run `python exporter.py -h` for an explanation)
or set the following environment variables:

* `DOCKERBENCHEXPORTER_SERVER_NAME`
* `DOCKERBENCHEXPORTER_SERVER_PORT`

## Docker

```bash
docker run -d --name docker-bench-security-exporter -p 9700:9700 lekpamartin/docker-bench-security-exporter
```

## docker-compose
```bash
git clone https://github.com/lekpamartin/docker-bench-security-exporter.git
cd docker-bench-security-exporter 
docker-compose ud -d
```
