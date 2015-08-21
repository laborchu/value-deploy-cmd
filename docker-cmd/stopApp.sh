#!/bin/sh 
sudo docker stop boring_carson
./palette.py stop 1
./etcd.py stop
./dns.py stop
./db.py stop 1
./db.py stop 2
./atlas.py stop 2
./redis.py stop 1
./fsc.py stop 1
./jenkins.py stop 1
./slb.py stop 1
./fdfs.py stop 1
./cs.py stop 1
./cs.py stop 2
./cs.py stop 3
./cs.py stop 4
./cs.py stop 5
./cs.py stop 6
./elm_as.py stop 1
./eduos_as.py stop 11
./cw.py stop 1
