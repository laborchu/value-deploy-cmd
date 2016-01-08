#!/usr/bin/python
#coding:utf-8
import sys
import time
from Executor import *

#获取参数
cmd = sys.argv[1]
index = sys.argv[2]

#设置端口和ip
startPort = 40051 + 2*int(index)-1
ip = str(135 + int(index))
sshPort = str(startPort )
httpPort = str(startPort + 1)
tcpPort = str(startPort + 2)

if cmd == 'create':
  os.system("mkdir -p /new_home/res/es/"+index)


#初始化实例
executor = Executor('value-es', {
    "ip": ip,
    "sshPort": sshPort,
    "portMap": {
        "127.0.0.1:" + sshPort: "22",
        httpPort: "9200",
        tcpPort: "9300"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys",
	"/new_home/res/logs/es/"+index: "/home/software/elasticsearch-1.7.3/logs/",
        "/new_home/res/es/"+index+"/data/" : "/home/software/elasticsearch-1.7.3/data/",
    }
})
executor.execute(cmd, index)
