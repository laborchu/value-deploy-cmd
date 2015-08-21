#!/usr/bin/python
#coding:utf-8
import sys
import time
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = (4191 + int(index)) * 10
ip = str(150 + int(index))
sshPort = str(startPort + 1)
serverPort = str(startPort + 2)

#初始化实例
executor = Executor('value-nodejs', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        serverPort: "3000"
    },
    "volumeMap": {
        "/home/res/nodejs": "/home/nodejs",
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd, index)
