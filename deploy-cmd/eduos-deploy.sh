#!/bin/sh
sudo rm -R /new_home/res/eduos/eduos_tmp/
sudo cp -R /new_home/res/eduos/webapp/eduos /new_home/res/eduos/eduos_tmp
sudo rm -R /new_home/res/eduos/webapp/eduos/
tar -zxvf /new_home/deploy_file/eduos.tar.gz -C /new_home/res/eduos/webapp
cd  ~/ext_cmd
./eduos-deploy.sh
