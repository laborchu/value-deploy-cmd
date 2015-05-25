#!/bin/sh
sudo mkdir -p home/mysql
sudo mkdir -p home/res/eduos/cloud
sudo mkdir -p home/res/eduos/webapp
sudo mkdir -p home/res/elm/webapp
sudo mkdir -p home/res/fdfs
sudo mkdir -p home/res/nodejs
sudo mkdir -p home/res/zookeeper
sudo mkdir -p home/res/paper/server
sudo mkdir -p home/res/sms/recorder/live
cd home/res/sms/recorder/live
sudo mkdir 240p  480p  720p  hls
cd -
sudo mkdir -p home/res/sms/recorder/vod
cd home/res/sms/recorder/vod
sudo mkdir 240p  480p  720p
cd -
sudo chmod -R 777 home
