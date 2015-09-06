#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = 41050 + 2*int(index)-1
ip = str(65 + int(index))
sshPort = str(startPort )
redisPort = str(startPort + 1)

#初始化实例
executor = Executor('value-redis', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        redisPort: "6379"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd, index)
