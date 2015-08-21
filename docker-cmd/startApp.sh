#!/bin/sh 
sudo weave launch
#sudo docker start redmine
sudo docker start boring_carson
./palette.py restart 1
./etcd.py restart
./zookeeper.py restart
./metaq.py restart 1
./dns.py restart
./db.py restart 1
./db.py restart 2
./atlas.py restart 1
./redis.py restart 1
./fsc.py restart 1
./jenkins.py restart 1
./slb.py restart 1
./fdfs.py restart 1
./cs.py restart 1
./cs.py restart 2
./cs.py restart 3
./cs.py restart 4
./cs.py restart 5
./cs.py restart 6
./fsc-nodejs.py restart 1
./el-stat.py restart 1
./elm_as.py restart 1
./eduos_as.py restart 1
./cw.py restart 1
