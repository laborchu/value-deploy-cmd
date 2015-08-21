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
startPort = (4071 + int(index)) * 10
ip = str(50 + int(index))
sshPort = str(startPort + 1)

#初始化实例
circleExe = Executor('circle-as', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22"
    },
    "volumeMap": {
        "/home/res/circle": "/home/res/circle",
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
circleExe.execute(cmd, index)
circleIp = circleExe.get_ip()
#如果是新增或重启容器，则还要重启应用
if cmd == 'create' or cmd == 'restart':
    time.sleep(5)
    circleExe.app_restart(index)
if cmd == 'create':
    slb = Slb(1)
    slb.slb_add_ip(circleIp, "circle")
if cmd == 'remove':
    slb = Slb(1)
    slb.slb_del_ip(circleIp, "circle")
