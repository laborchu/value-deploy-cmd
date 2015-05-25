#!/bin/sh 
rm -R /home/ftp/dev/apps/eduos
unzip -oq /home/ftp/dev/apps/elos-web.war -d /home/ftp/dev/apps/eduos
cd /home/ftp/dev/apps/eduos/assets/script
sh b.sh
cd /home/ftp/dev/apps/eduos/ma/fsc
bower install
cnpm install
grunt build

tar -zcvf /home/ftp/dev/apps/elos-web.tar.gz /home/ftp/dev/apps/eduos

#lftp -u devftp,devftp 61.153.97.56 -e 'put /home/ftp/dev/apps/elos-web.war -o apps/elos-web.war; quit'
#lftp -u devftp,devftp 183.203.18.61 -e 'put /home/ftp/dev/apps/elos-web.war -o apps/elos-web.war; quit'
