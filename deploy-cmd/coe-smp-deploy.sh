#!/bin/sh
sudo rm -R /new_home/res/coe/smp/webapp/smp
cd /new_home/res/coe/smp/webapp/coe-smp-fe
git pull
cp  /new_home/deploy_file/smp-web.war /new_home/res/coe/smp/webapp/smp.war
cd  ~/ext_cmd
./coe-smp-deploy.sh
