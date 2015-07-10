#!/bin/sh
cp /home/ftp/dev/apps/fsc-nodejs.tar.gz /home/res/nodejs/fsc-nodejs.tar.gz
cd /home/res/nodejs/
tar -zxvf fsc-nodejs.tar.gz
cd  ~/docker/python
./fsc-nodejs.py restart 1
