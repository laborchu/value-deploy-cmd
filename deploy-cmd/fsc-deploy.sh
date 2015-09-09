#!/bin/sh 
cp /new_home/deploy_file/fsc-server-1.0-SNAPSHOT.jar /new_home/res/eduos/fsc/app/fsc-server.jar
cd /new_home/res/eduos/fsc/app
~/software/jdk1.7.0_25/bin/jar xvf fsc-server.jar fastdfs.conf
cd  ~/ext_cmd
./fsc-deploy.sh
