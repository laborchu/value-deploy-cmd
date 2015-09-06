#!/usr/bin/python
#coding:utf-8
import sys
import os
import time
import fileinput
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = 41080 +2*int(index)-1
ip = str(85 + int(index))
sshPort = str(startPort)
debugPort = str(startPort + 1)

executor = Executor('el-stat', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        debugPort: "9999"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys",
	"/home/res/eduos/stat" : "/home/stat"
    }
})
executor.execute(cmd, index)
