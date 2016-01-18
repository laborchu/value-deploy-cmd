#!/bin/sh 
cp /new_home/deploy_file/el-stat-1.0-SNAPSHOT.jar /new_home/res/eduos/stat/el-stat.jar
cd /new_home/res/eduos/stat
 ~/software/jdk1.7.0_25/bin/jar xvf el-stat.jar ssl/keystore.p12
cd  ~/ext_cmd
./elstat-deploy.sh
