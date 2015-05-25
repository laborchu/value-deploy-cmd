#!/bin/sh 
cd /home/res/eduos/webapp/eduos/assets/script
sh b.sh
cd /home/res/eduos/webapp/eduos/ma/fsc
#cp -R /home/ftp/dev/bower_components /home/res/eduos/webapp/eduos/ma/fsc/
bower install
npm install
grunt build
