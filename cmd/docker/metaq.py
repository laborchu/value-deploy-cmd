#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = (4121 + int(index)) * 10
ip = str(180 + int(index))
sshPort = str(startPort + 1)
serverPort = str(startPort + 2)
httpPort = str(startPort + 3)

#初始化实例
executor = Executor('value-metaq', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        serverPort: serverPort,
        httpPort: "8120"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd, index)
