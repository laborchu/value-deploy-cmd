#!/bin/sh 
rm /new_home/deploy_file/smp-web.war
lftp -u devftp,devftp 61.153.97.56 -e 'get apps/smp-web.war -o /new_home/deploy_file/smp-web.war; quit'
