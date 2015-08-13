#!/bin/sh 
#lftp -u devftp,devftp 61.153.97.56 -e 'put /home/ftp/dev/apps/elm.tar.gz -o apps/elm.tar.gz; quit'
lftp -u devftp,devftp 183.203.18.61 -e 'put /home/ftp/dev/apps/elm.tar.gz -o apps/elm.tar.gz; quit'
