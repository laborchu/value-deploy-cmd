#!/usr/bin/python
#coding:utf-8
import sys
import time
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = (4031 + int(index)) * 10
ip = str(140 + int(index))
sshPort = str(startPort + 1)
trackerPort = str(startPort + 2)
storagePort = str(startPort + 3)

#初始化实例
executor = Executor('value-fdfs', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        trackerPort: "22122",
	storagePort: str(storagePort)
    },
    "volumeMap": {
        "/home/res/fdfs/fdfs"+index: "/home/fdfs",
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd, index)

#if cmd == 'create':
#    time.sleep(5)
#    os.system("ssh root@127.0.0.1 -p %s 'sh /root/init.sh'" % (sshPort,))
