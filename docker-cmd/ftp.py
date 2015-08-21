#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = (4161 + int(index)) * 10
ip = str(80 + int(index))
sshPort = str(startPort + 1)
ftpPort = str(startPort + 2)

#初始化实例
executor = Executor('value-ftp', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        ftpPort: "21"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys",
        "/home/ftp/pureftp"+str(index): "/home/ftp"
    }
})
executor.execute(cmd, index)
