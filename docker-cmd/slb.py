#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

cmd = sys.argv[1]
index = sys.argv[2]
startPort = 41020 + 2*int(index)-1
ip = str(20 + int(index))
sshPort = str(startPort )
nginxPort = str(startPort + 1)

#初始化实例
executor = Executor('value-slb', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        "127.0.0.1:" + nginxPort: "80"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys",
	"/new_home/res/logs/slb/"+index: "/usr/local/nginx/logs"
    }
})
executor.execute(cmd, index)

