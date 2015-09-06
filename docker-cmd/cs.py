#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = 42065 + 3*int(index)-2
ip = str(45 + int(index))
sshPort = str(startPort )
memPort = str(startPort + 1)
twPort = str(startPort + 2)

#初始化实例
executor = Executor('value-cs', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        memPort: "11211",
        twPort: "22122"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd, index)
