#!/bin/sh 
rm /new_home/deploy_file/elo.tar.gz
lftp -u devftp,devftp 61.153.97.56 -e 'get apps/elo.tar.gz -o /new_home/deploy_file/elo.tar.gz; quit'
