#!/bin/sh 
cp /home/ftp/dev/res/eduos/webapp/paper-server-1.0-SNAPSHOT.jar /home/res/paper/server/paper-server.jar
cd /home/res/paper/server
/home/value/software/jdk1.7.0_25/bin/jar xvf paper-server.jar fastdfs.conf
#java -jar ma-server.jar
