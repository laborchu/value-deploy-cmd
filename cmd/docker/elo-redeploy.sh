#!/bin/sh 
rm -R /home/res/elo/webapp/elo
cp /home/ftp/dev/res/eduos/webapp/elo-web.war /home/res/elo/webapp/elo.war
unzip -oq /home/res/elo/webapp/elo.war -d /home/res/elo/webapp/elo
cp -R /home/value/cmd/elm/bower_components /home/res/elo/webapp/elo/angular
chmod -R 777 /home/res/elo/webapp/elo
python ~/value-deploy-cmd/cmd/docker/elo_as.py app_restart 1
