#!/usr/bin/python
#coding:utf-8
import sys
import time
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = 40035 + int(index)
ip = str(100 + int(index))
sshPort = str(startPort )

#初始化实例
executor = Executor('coe-os-as', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22"
    },
    "volumeMap": {
        "/new_home/res/coe/os": "/home/res/os",
        "/new_home/res/logs/coe-os/"+index: "/home/software/apache-tomcat-8.0.3/logs",
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd, index)
#如果是新增或重启容器，则还要重启应用
if cmd == 'create' or cmd == 'restart':
    time.sleep(5)
    executor.app_restart(index)
