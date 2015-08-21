#!/bin/sh 
mv ~/cmd/eduos/eduos.conf ~/cmd/eduos/eduos.conf.tmp
mv ~/cmd/eduos/eduos-sub.conf ~/cmd/eduos/eduos.conf
mv ~/cmd/eduos/eduos.conf.tmp ~/cmd/eduos/eduos-sub.conf
sudo cp ~/cmd/eduos/eduos.conf /usr/local/nginx/conf/conf.d/eduos.conf
sudo /usr/local/nginx/sbin/nginx -s reload
