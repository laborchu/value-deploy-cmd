#!/bin/sh 
sudo rm -R /home/res/elm/webapp/elm
sudo cp /home/ftp/dev/res/eduos/webapp/elm-web.war /home/res/elm/webapp/elm.war
sudo unzip -oq /home/res/elm/webapp/elm.war -d /home/res/elm/webapp/elm
python ~/docker/python/elm_as.py app_restart 1
