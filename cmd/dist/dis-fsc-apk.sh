#!/bin/sh 
lftp -u devftp,devftp 115.231.93.40 -e 'put /home/ftp/dev/apps/fsc-android-1.0-SNAPSHOT-prod.apk -o apps/fsc-app.apk; quit'
lftp -u devftp,devftp 183.203.18.61 -e 'put /home/ftp/dev/apps/fsc-android-1.0-SNAPSHOT-jz.apk -o apps/fsc-app.apk; quit'
