#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = (4171 + int(index)) * 10
ip = str(90 + int(index))
sshPort = str(startPort + 1)
dbPort = str(startPort + 2)
adminPort = str(startPort + 3)

#初始化实例
executor = Executor('value-atlas', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        dbPort: "1234",
        adminPort: "2345"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd, index)
