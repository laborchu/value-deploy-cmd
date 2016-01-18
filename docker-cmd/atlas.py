#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

startPort = 40006 + 3*int(index)-2
ip = str(5 + int(index))
sshPort = str(startPort )

#初始化实例
executor = Executor('value-atlas', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:"+sshPort : "22"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd,index)
