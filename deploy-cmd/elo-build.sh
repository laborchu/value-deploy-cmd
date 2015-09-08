#!/bin/sh 
rm -R /home/ftp/dev/apps/elo
unzip -oq /home/ftp/dev/apps/elo-web.war -d /home/ftp/dev/apps/elo
cd /home/ftp/dev/apps/elo/angular
bower install
cnpm install
grunt build
rm -R /home/ftp/dev/apps/elo/angular/node_modules
cd /home/ftp/dev/apps
tar -zcvf /home/ftp/dev/apps/elo.tar.gz elo/