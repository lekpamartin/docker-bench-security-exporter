# docker-bench-security-exporter


## Running

Accepted parameters:

* server_name (optional): Name to bind the HTTP server to. Default: 0.0.0.0
* server_port (optional): Port to bind the HTTP server to. Default: 9700

You can either pass script arguments (run `python exporter.py -h` for an explanation)
or set the following environment variables:

* `DOCKERBENCHEXPORTER_SERVER_NAME`
* `DOCKERBENCHEXPORTER_SERVER_PORT`
<br><br>You can personnalise your check in the file :
```bash
check.env
```

## Docker run
You have to mount all used directory and files
```bash
docker run -d --name docker-bench-security-exporter \
	-p 9700:9700 \
	-v /var/run/docker.sock:/var/run/docker.sock \
	lekpamartin/docker-bench-security-exporter
```

## docker-compose
```bash
git clone https://github.com/lekpamartin/docker-bench-security-exporter.git
cd docker-bench-security-exporter 
docker-compose up -d
```

## docs
Use https://github.com/docker/docker-bench-security 
