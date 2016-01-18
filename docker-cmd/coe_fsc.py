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
startPort = (42110 + 3*int(index)-1) 
ip = str(110 + int(index))
sshPort = str(startPort )
serverPort = str(startPort + 1)
debugPort = str(startPort + 2)

if cmd == 'create':
  hostIp = os.environ.get('HOST_IP')
  os.system("mkdir -p /new_home/res/coe/fsc/"+index)
  os.system("echo "+hostIp+":"+serverPort+" > /new_home/res/coe/fsc/"+index+"/ip.txt")

executor = Executor('coe-fsc', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        serverPort: "10081",
        debugPort: "9999"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys",
	"/new_home/res/logs/fsc/"+index: "/home/logs",
	"/new_home/res/coe/fsc/app" : "/home/fsc",
	"/new_home/res/coe/fsc/"+index+"/ip.txt" : "/root/ip.txt",

    }
})
executor.execute(cmd, index)
