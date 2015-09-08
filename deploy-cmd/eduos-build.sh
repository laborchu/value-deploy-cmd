#!/bin/sh 
rm -R /home/ftp/dev/apps/eduos
unzip -oq /home/ftp/dev/apps/elos-web.war -d /home/ftp/dev/apps/eduos
cd /home/ftp/dev/apps/eduos/assets/script
sh b.sh
cd /home/ftp/dev/apps/eduos/ma/fsc
bower install
cnpm install
grunt build
rm -R /home/ftp/dev/apps/eduos/ma/fsc/node_modules
cd /home/ftp/dev/apps
tar -zcvf /home/ftp/dev/apps/eduos.tar.gz eduos/
