#!/bin/sh 
cp /home/ftp/dev/res/eduos/webapp/fsc-server-1.0-SNAPSHOT.jar /home/res/eduos/fsc/app/fsc-server.jar
cd /home/res/eduos/fsc/app
/home/value/software/jdk1.7.0_25/bin/jar xvf fsc-server.jar fastdfs.conf
#java -jar ma-server.jar
