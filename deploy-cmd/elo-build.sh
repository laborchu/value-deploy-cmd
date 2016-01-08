#!/bin/sh 
rm -R /home/ftp/dev/apps/elo
unzip -oq /home/ftp/dev/apps/elo-web.war -d /home/ftp/dev/apps/elo
cp -R /home/ftp/dev/apps/elo_tmp/node_modules /home/ftp/dev/apps/elo/angular/
cp -R /home/ftp/dev/apps/elo_tmp/bower_components /home/ftp/dev/apps/elo/angular/
cd /home/ftp/dev/apps/elo/angular
#bower install
#npm install
grunt build
rm -R /home/ftp/dev/apps/elo/angular/node_modules
cd /home/ftp/dev/apps
tar -zcvf /home/ftp/dev/apps/elo.tar.gz elo/
