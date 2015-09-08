#!/bin/sh
sudo rm -R /new_home/res/eduos/webapp/eduos/
tar -zxvf /new_home/deploy_file/eduos.tar.gz -C /new_home/res/eduos/webapp
cd  ~/ext_cmd
./eduos-deploy.sh