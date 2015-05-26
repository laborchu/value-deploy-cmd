#!/usr/bin/python
#coding:utf-8
import sys
import os
import time
import fileinput
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = (4141 + int(index)) * 10
ip = str(60 + int(index))
sshPort = str(startPort + 1)
serverPort = str(startPort + 2)

if cmd == 'create':
  hostIp = os.environ.get('HOST_IP')
  os.system("mkdir -p /home/res/eduos/fsc/"+index)
  os.system("echo "+hostIp+":"+serverPort+" > /home/res/eduos/fsc/"+index+"/ip.txt")

executor = Executor('eduos-fsc', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        serverPort: "10081"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys",
	"/home/res/eduos/fsc/app" : "/home/fsc",
	"/home/res/eduos/fsc/"+index+"/ip.txt" : "/root/ip.txt",

    }
})
executor.execute(cmd, index)
