#!/usr/bin/python
#coding:utf-8
import sys
import time
from Executor import *
from Slb import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = 41070 + 2*int(index)-1
ip = str(80 + int(index))
sshPort = str(startPort )
tomcatPort = str(startPort + 1)

#初始化实例
executor = Executor('value-solr', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        "127.0.0.1:" + tomcatPort: "8080"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd, index)
#如果是新增或重启容器，则还要重启应用
if cmd == 'create' or cmd == 'restart':
    time.sleep(5)
    executor.app_restart(index)
