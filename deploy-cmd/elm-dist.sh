#!/bin/sh 
rm /new_home/deploy_file/elm.tar.gz
lftp -u devftp,devftp 61.153.97.56 -e 'get apps/elm.tar.gz -o /new_home/deploy_file/elm.tar.gz; quit'
