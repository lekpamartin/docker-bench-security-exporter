#!/usr/bin/python

import os
import json
import subprocess
import shutil

myhost = os.uname()[1]

os.chdir("/tmp")
os.system("git clone https://github.com/docker/docker-bench-security.git")
os.chdir("/tmp/docker-bench-security")
subprocess.call(['./docker-bench-security.sh'])

file = open("test.log","w")

with open('docker-bench-security.sh.log.json') as json_file:
  data = json.load(json_file)
  for i in data["tests"]:
    for j in i["results"]:
      if j["result"] == "WARN":
        file.write("dockerbenchsecurity{version=\"" + data["dockerbenchsecurity"] + "\",instance=\"" + myhost + "\",cat=\"" + i["desc"] + "\",id=\"" + j["id"] + "\",name=\"" + j["desc"] + "\",details=\"" + j.get('details', 'N/A')+ "\"} 1\n")

file.close()
os.system("cat /tmp/docker-bench-security/test.log | curl --data-binary @- http://admin:4gc5oTm6WT@10.155.52.18:9091/metrics/job/dockerbench")
os.chdir("..")
shutil.rmtree("docker-bench-security")
