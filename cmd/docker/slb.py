#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

cmd = sys.argv[1]
index = sys.argv[2]
startPort = (4051 + int(index)) * 10
ip = str(10 + int(index))
sshPort = str(startPort + 1)
nginxPort = str(startPort + 2)

#初始化实例
executor = Executor('value-slb', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        "127.0.0.1:" + nginxPort: "80"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd, index)

