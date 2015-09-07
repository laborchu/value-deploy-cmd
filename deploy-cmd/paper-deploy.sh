#!/bin/sh 
cp /new_home/deploy_file/paper-server-1.0-SNAPSHOT.jar /new_home/res/paper/server/paper-server.jar
cd /new_home/res/paper/server
~/software/jdk1.7.0_25/bin/jar xvf paper-server.jar fastdfs.conf
cd  ~/ext_cmd
./paper-deploy.sh
