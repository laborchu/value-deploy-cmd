#!/usr/bin/python
#coding:utf-8
import time
import sys
import urllib.request
import socket

if len(sys.argv) > 1:
    INTERFACE = sys.argv[1]
else:
    INTERFACE = 'eth0'

# 监控网络流量 Start
pre_input = 0
pre_output = 0
ifstat = open('/proc/net/dev').readlines()
for interface in ifstat:
    if INTERFACE in interface:
        pre_input = float(interface.split()[1])
        pre_output = float(interface.split()[9])

time.sleep(1)

after_input = 0
after_output = 0
ifstat = open('/proc/net/dev').readlines()
for interface in ifstat:
    if INTERFACE in interface:
        after_input = float(interface.split()[1])
        after_output = float(interface.split()[9])

inputRate = round((after_input - pre_input) / 1024 / 1024, 3)
outputRate = round((after_output - pre_output) / 1024 / 1024, 3)
#print(str(input_rate) + 'MB              ' + str(output_rate) + 'MB')
# 监控网络流量 End

# 监控内存 Start
ifstat = open('/proc/meminfo').readlines()
memTotal = 0
memFree = 0
buffers = 0
cached = 0
for line in ifstat:
    if "MemTotal" in line:
        memTotal = float(line.split(":")[1].strip(' \r\nBk'))
    if "MemFree" in line:
        memFree = float(line.split(":")[1].strip(' \r\nBk'))
    if "Buffers" in line:
        buffers = float(line.split(":")[1].strip(' \r\nBk'))
    if "Cached" in line:
        cached = float(line.split(":")[1].strip(' \r\nBk'))
usedMem = memTotal - (memFree + buffers + cached)
# print(str(usedMem) + 'kB/' + str(memTotal) + 'kB')
# 监控内存 End

# 监控cpu负载 Start
con = open('/proc/loadavg').read().split()
lavg_1 = con[0]
lavg_5 = con[1]
lavg_15 = con[2]
# print(lavg_1 + ' ' + lavg_5 + ' '+lavg_15)
# 监控cpu负载 End

ip = socket.gethostbyname(socket.gethostname())
url = 'http://elm.test.cn/monitor.json?' \
    'ip=' + ip + '' \
    '&inputRate=' + str(inputRate) + '' \
    '&outputRate=' + str(outputRate) + '' \
    '&usedMem=' + str(usedMem) + '' \
    '&memTotal=' + str(memTotal) + '' \
    '&lavg1=' + str(lavg_1) + '' \
    '&lavg5=' + str(lavg_5) + '' \
    '&lavg15=' + str(lavg_15) + ''
print(url)
#resp = urllib.request.urlopen(url)
#html = resp.read()
#print(html)
