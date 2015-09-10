#!/bin/sh 
rm /new_home/deploy_file/fsc-app-wan-release.apk
rm /new_home/deploy_file/fsc-app-prod-release.apk
lftp -u devftp,devftp 61.153.97.56 -e 'get apps/fsc-app-wan-release.apk -o /new_home/deploy_file/fsc-app-wan-release.apk; quit'
lftp -u devftp,devftp 61.153.97.56 -e 'get apps/fsc-app-prod-release.apk -o /new_home/deploy_file/fsc-app-prod-release.apk; quit'
