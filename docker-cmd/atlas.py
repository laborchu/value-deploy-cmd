#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

#获取参数
cmd = sys.argv[1]

#初始化实例
executor = Executor('value-atlas', {
    "ip": "6",
    "sshPort": "40007",
    "portMap": {
        "127.0.0.1:40007" : "22"
    },
    "volumeMap": {
        "~/authorized_keys": "/root/.ssh/authorized_keys"
    }
})
executor.execute(cmd, index)
