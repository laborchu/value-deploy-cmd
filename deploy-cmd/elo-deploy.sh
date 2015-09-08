#!/bin/sh
sudo rm -R /new_home/res/elo/webapp/elo/
tar -zxvf /new_home/deploy_file/elo.tar.gz -C /new_home/res/elo/webapp
cd  ~/ext_cmd
./elo-deploy.sh