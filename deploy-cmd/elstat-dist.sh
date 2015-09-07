#!/bin/sh 
rm /new_home/deploy_file/paper-server-1.0-SNAPSHOT.jar
lftp -u devftp,devftp 61.153.97.56 -e 'get apps/el-stat-1.0-SNAPSHOT.jar -o /new_home/deploy_file/el-stat-1.0-SNAPSHOT.jar; quit'
