#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = 42035 + 3*int(index)-2
ip = str(35 + int(index))
sshPort = str(startPort )
serverPort = str(startPort + 1)
httpPort = str(startPort + 2)

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
        "~/authorized_keys": "/root/.ssh/authorized_keys",
	"/new_home/res/logs/metaq/"+index: "/home/software/metaq-server/logs"
    }
})
executor.execute(cmd, index)
