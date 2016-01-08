#!/bin/sh
sudo rm -R /new_home/res/coe/sop/webapp/sop
cd /new_home/res/coe/sop/webapp/coe-sop-fe
git pull
cp  /new_home/deploy_file/sop-web.war /new_home/res/coe/sop/webapp/sop.war
cd  ~/ext_cmd
./coe-sop-deploy.sh
