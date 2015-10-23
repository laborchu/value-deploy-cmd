#!/bin/sh 
rm -R /home/ftp/dev/apps/elm
unzip -oq /home/ftp/dev/apps/elm-web.war -d /home/ftp/dev/apps/elm
cp -R /home/ftp/dev/apps/elm_tmp/node_modules /home/ftp/dev/apps/elm/elm/
cp -R /home/ftp/dev/apps/elm_tmp/bower_components /home/ftp/dev/apps/elm/elm/
cd /home/ftp/dev/apps/elm/elm
#bower install
#npm install
grunt build
rm -R /home/ftp/dev/apps/elm/elm/node_modules
cd /home/ftp/dev/apps
tar -zcvf /home/ftp/dev/apps/elm.tar.gz elm/
