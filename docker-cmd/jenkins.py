#!/usr/bin/python
#coding:utf-8
import sys
import time
from Executor import *

#获取参数
cmd = sys.argv[1]

#初始化实例
executor = Executor('jenkins', {
    "ip": "3",
    "sshPort": "40001",
    "portMap": {
        "127.0.0.1:40001:22",
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd)
if cmd == 'restart':
    time.sleep(2)
    executor.app_restart("0")
