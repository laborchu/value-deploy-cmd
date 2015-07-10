#!/bin/sh
cp /home/ftp/dev/apps/el-stat-1.0-SNAPSHOT.jar /home/res/eduos/stat/el-stat.jar
cd  ~/docker/python
./el-stat.py restart 1
