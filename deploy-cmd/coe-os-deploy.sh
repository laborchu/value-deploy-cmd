#!/bin/sh
sudo rm -R /new_home/res/coe/os/webapp/os-web
cp  /new_home/deploy_file/os-web.war /new_home/res/coe/os/webapp/os-web.war
cd  ~/ext_cmd
./coe-os-deploy.sh
