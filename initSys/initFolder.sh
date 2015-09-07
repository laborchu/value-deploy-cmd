#!/bin/sh
#sudo mkdir -p new_home/mysql
sudo mkdir -p new_home/res/eduos/cloud
sudo mkdir -p new_home/res/eduos/webapp
sudo mkdir -p new_home/res/elm/webapp
sudo mkdir -p new_home/res/fdfs
sudo mkdir -p new_home/res/nodejs
sudo mkdir -p new_home/res/zookeeper
sudo mkdir -p new_home/res/paper/server
sudo mkdir -p new_home/res/sms/recorder/live
cd new_home/res/sms/recorder/live
sudo mkdir 240p  480p  720p  hls
cd -
sudo mkdir -p new_home/res/sms/recorder/vod
cd new_home/res/sms/recorder/vod
sudo mkdir 240p  480p  720p
cd -
sudo chmod -R 777 new_home
