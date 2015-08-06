#!/bin/sh
sudo rm -R /home/res/elm/webapp/elm/
tar -zxvf /home/ftp/dev/apps/elm.tar.gz -C /home/res/elm/webapp
cd  ~/docker/python
./elm_as.py restart 1
