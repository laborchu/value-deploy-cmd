#!/bin/sh 
lftp -u devftp,devftp 115.231.93.40 -e 'put /home/ftp/dev/apps/fsc-nodejs.tar.gz -o apps/fsc-nodejs.tar.gz; quit'
lftp -u devftp,devftp 183.203.18.61 -e 'put /home/ftp/dev/apps/fsc-nodejs.tar.gz -o apps/fsc-nodejs.tar.gz; quit'
