#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = 42075 + 3*int(index)-2
ip = str(75 + int(index))
sshPort = str(startPort )
rtmpPort = str(startPort + 1)
httpPort = str(startPort + 2)

#初始化实例
executor = Executor('value-sms', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        rtmpPort: "1935",
        httpPort: "80"
    },
    "volumeMap": {
        "/home/res/sms": "/home/sms",
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd, index)