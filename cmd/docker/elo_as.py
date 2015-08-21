#!/usr/bin/python
#coding:utf-8
import sys
import time
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = (4094 + int(index)) * 10
ip = str(43 + int(index))
sshPort = str(startPort + 1)

#初始化实例
elmExe = Executor('elo-as', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22"
    },
    "volumeMap": {
        "/home/res/elo": "/home/res/elo",
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
elmExe.execute(cmd, index)
#如果是新增或重启容器，则还要重启应用
if cmd == 'create' or cmd == 'restart':
    time.sleep(5)
    elmExe.app_restart(index)
