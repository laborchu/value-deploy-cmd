#!/bin/sh 
lftp -u devftp,devftp 115.231.93.40 -e 'put /home/ftp/dev/apps/el-stat-1.0-SNAPSHOT.jar -o apps/el-stat-1.0-SNAPSHOT.jar; quit'
lftp -u devftp,devftp 183.203.18.61 -e 'put /home/ftp/dev/apps/el-stat-1.0-SNAPSHOT.jar -o apps/el-stat-1.0-SNAPSHOT.jar; quit'
