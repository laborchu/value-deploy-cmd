#!/bin/sh 
cp /home/ftp/dev/apps/paper-server-1.0-SNAPSHOT.jar /home/res/paper/server/paper-server.jar
cd /home/res/paper/server
~/software/jdk1.7.0_25/bin/jar xvf paper-server.jar fastdfs.conf
cd  ~/docker/python
./cw.py restart 1
