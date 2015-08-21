#!/usr/bin/python
#coding:utf-8
import sys
from Executor import *

#获取参数
cmd = sys.argv[1]

#设置端口和ip
ip = 2
sshPort = "40011"

#初始化实例
executor = Executor('value-dnsmasq', {
    "ip": ip,
})
print(executor.get_ip())
