#!/bin/sh 
sudo rm -R /home/res/eduos/webapp/eduos
sudo cp /home/ftp/dev/res/eduos/webapp/elos-web.war /home/res/eduos/webapp/eduos.war
sudo unzip -oq /home/res/eduos/webapp/eduos.war -d /home/res/eduos/webapp/eduos
python ~/docker/python/eduos_as.py app_restart 1
#mv ~/cmd/eduos/restart.sh ~/cmd/eduos/restart.sh.tmp
#mv ~/cmd/eduos/sub-restart.sh ~/cmd/eduos/restart.sh
#mv ~/cmd/eduos/restart.sh.tmp ~/cmd/eduos/sub-restart.sh
#sh ~/cmd/eduos/restart.sh
