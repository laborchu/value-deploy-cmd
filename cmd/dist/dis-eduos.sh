#!/bin/sh 
lftp -u devftp,devftp 61.153.97.56 -e 'put /home/ftp/dev/apps/elos-web.tar.gz -o apps/eduos.tar.gz; quit'
lftp -u devftp,devftp 183.203.18.48 -e 'put /home/ftp/dev/apps/elos-web.tar.gz -o apps/eduos.tar.gz; quit'
