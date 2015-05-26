#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

#获取参数
cmd = sys.argv[1]

#设置端口和ip
ip = 6
sshPort = "40016"
clientPort="40017"

#初始化实例
executor = Executor('value-zoo', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
	clientPort: "2181"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys",
        "/home/res/zookeeper": "/home/zookeeper"
    }
})
executor.execute(cmd)
