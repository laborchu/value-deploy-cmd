#!/bin/sh
rm -R /home/res/eduos/webapp/eduos
tar -zxvf /home/ftp/dev/apps/elos-web.tar.gz -C /home/res/eduos/webapp/eduos
cd  ~/docker/python
./eduos_as.py restart 1
