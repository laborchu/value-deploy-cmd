#!/bin/sh
sudo rm -R /home/res/eduos/webapp/eduos
tar -zxvf /home/ftp/dev/apps/eduos.tar.gz -C /home/res/eduos/webapp
cd  ~/docker/python
./eduos_as.py restart 1
