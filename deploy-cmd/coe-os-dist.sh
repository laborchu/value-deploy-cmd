#!/bin/sh 
rm /new_home/deploy_file/os-web.war
lftp -u devftp,devftp 61.153.97.56 -e 'get apps/os-web.war -o /new_home/deploy_file/os-web.war; quit'
