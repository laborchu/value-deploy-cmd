#!/bin/sh 
unzip -oq /home/ftp/dev/apps/eduos.war -d /home/ftp/dev/apps/eduos
cd /home/ftp/dev/apps/eduos/assets/script
sh b.sh
cd /home/ftp/dev/apps/eduos/ma/fsc
bower install
npm install
grunt build

#lftp -u devftp,devftp 61.153.97.56 -e 'put /home/ftp/dev/apps/elos-web.war -o apps/elos-web.war; quit'
#lftp -u devftp,devftp 183.203.18.61 -e 'put /home/ftp/dev/apps/elos-web.war -o apps/elos-web.war; quit'
