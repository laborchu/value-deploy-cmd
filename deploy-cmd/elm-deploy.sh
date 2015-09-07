#!/bin/sh
sudo rm -R /new_home/res/elm/webapp/elm/
tar -zxvf /new_home/deploy_file/elm.tar.gz -C /new_home/res/elm/webapp
cd  ~/ext_cmd
./elm-deploy.sh