#!/bin/sh
cp /home/ftp/dev/apps/fsc-server-1.0-SNAPSHOT.jar /home/res/eduos/fsc/app/fsc-server.jar
cd /home/res/eduos/fsc/app
~/software/jdk1.7.0_25/bin/jar xvf fsc-server.jar fastdfs.conf
cd  ~/docker/python
./fsc.py restart 1
