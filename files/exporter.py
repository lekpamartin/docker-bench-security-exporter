import argparse
import http.server
import os
import subprocess
import shutil


## Monitors
def fetch_data():
  os.chdir("/tmp/docker-bench-security")
  subprocess.call(['./docker-bench-security.sh'])
  
  with open('docker-bench-security.sh.log.json') as json_file:
    data = json.load(json_file)
    result = ''
    for i in data["tests"]:
      for j in i["results"]:
        if j["result"] == "WARN":
          result += "test %s %s" %(i,j)

  return result



class ReqHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        answer = fetch_data()
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(
            format_prometheus(answer.get('monitors')).encode('utf-8')
        )
        self.wfile.write(
            format_prometheus_accountdetails(accountdetails.get('account')).encode('utf-8')
        )
        self.wfile.write(
            format_prometheus_psp(psp.get('psps')).encode('utf-8')
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
