#!/bin/sh
sudo rm -R /home/res/eduos/webapp/eduos
sudo cp /home/ftp/dev/apps/elos-web.war /home/res/eduos/webapp/eduos.war
sudo unzip -oq /home/res/eduos/webapp/eduos.war -d /home/res/eduos/webapp/eduos
cd  ~/docker/python
./eduos_as.py restart 1
