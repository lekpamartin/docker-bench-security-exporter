import argparse
import http.server
import os
import subprocess
import json
import time


## Monitors
def fetch_data():
  file = 'docker-bench-security.sh.log.json'
  if os.path.getmtime(file): 
    #if time.ctime(os.path.getmtime(file)) >= 360:
    #  subprocess.call(['./docker-bench-security.sh'])
    print('exist')
  else:
      subprocess.call(['./docker-bench-security.sh'])
  
  with open(file) as json_file:
    data = json.load(json_file)
    version = data["dockerbenchsecurity"]
    checks  = data["checks"]
    score = data["score"]
    start = data["start"]
    result = "# SCORE \nscore{version=\"%s\"} %s\n" %(version,score)
    for i in data["tests"]:
      ID = i["id"]
      DESC = i["desc"]
      result += "\n# %s %s\n" %(ID,DESC)
      for j in i["results"]:
        id = j["id"]
        desc = j["desc"]
        if j["result"] == "INFO":
          value = 0
        elif j["result"] == "WARN":
          value = 1
        else:
          value = 2
        result += "check{group_id=\"%s\",id=\"%s\",desc=\"%s\",version=\"%s\"} %s\n" %(ID,id,desc,version,value)

  return result



class ReqHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        answer = fetch_data()
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(
            #format_prometheus(answer.get('monitors')).encode('utf-8')
            fetch_data().encode('utf-8')
        )


if __name__ == '__main__':
  server_name = os.environ.get('DOCKERBENCHEXPORTER_SERVER_NAME', '0.0.0.0')
  server_port = int(os.environ.get('DOCKERBENCHEXPORTER_SERVER_PORT', '9700'))
  parser = argparse.ArgumentParser(
    description='Export all check results from uptimerobot.txt'
                        'for prometheus scraping.'
  )
  parser.add_argument(
    '--server_name', '-s',
    default='0.0.0.0',
    help='Server address to bind to.'
  )
  parser.add_argument(
    '--server_port', '-p',
    default=9700,
    type=int,
    help='Port to bind to.'
  )
  args = parser.parse_args()
  server_name = args.server_name
  server_port = args.server_port

  httpd = http.server.HTTPServer((server_name, server_port), ReqHandler)
  httpd.serve_forever()
