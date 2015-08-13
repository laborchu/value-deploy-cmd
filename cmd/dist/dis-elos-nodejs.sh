#!/bin/sh 
lftp -u devftp,devftp 115.231.93.40 -e 'put /home/ftp/dev/apps/elos-nodejs.tar.gz -o apps/elos-nodejs.tar.gz; quit'
lftp -u devftp,devftp 183.203.18.61 -e 'put /home/ftp/dev/apps/elos-nodejs.tar.gz -o apps/elos-nodejs.tar.gz; quit'
