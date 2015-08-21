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
startPort = (4080 + int(index)) * 10
ip = str(170 + int(index))
sshPort = str(startPort + 1)
tomcatPort = str(startPort + 2)

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
