#!/bin/sh 
rm /new_home/deploy_file/sop-web.war
lftp -u devftp,devftp 61.153.97.56 -e 'get apps/sop-web.war -o /new_home/deploy_file/sop-web.war; quit'
