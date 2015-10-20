#!/usr/bin/python
#coding:utf-8
import sys
import time
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = 41060 + 2*int(index)-1
ip = str(70 + int(index))
sshPort = str(startPort)
ftpPort = str(startPort + 1)

#初始化实例
executor = Executor('value-cw', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        ftpPort: "21"
    },
    "volumeMap": {
        "/new_home/res/eduos/cw": "/home/cw",
        "/new_home/res/paper": "/home/paper",
	"/new_home/res/logs/cw/"+index: "/home/logs",
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd, index)

if cmd == 'create':
    time.sleep(3)
    os.system("ssh root@127.0.0.1 -p %s 'sh /root/install.sh'" % (sshPort,))

if cmd == 'create' or cmd == 'restart':
    time.sleep(3)
    executor.app_restart(index)
