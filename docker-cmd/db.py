#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = 40020+int(index)
ip = str(25 + int(index))
sshPort = str(startPort)

#初始化实例
executor = Executor('value-db', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22"
    },
    "volumeMap": {
        "/home/mysql/mysql"+str(index): "/home/mysql",
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd, index)
