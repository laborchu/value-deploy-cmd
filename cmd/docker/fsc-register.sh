#!/bin/sh 
port=$(lsof -i:10081 -t)
if [ "$port"x = ""x ]; then
    /usr/bin/curl -L http://etcd.server:4001/v2/keys/edu/fsc/upstream/${ip} -XDELETE
else
    /usr/bin/curl -L http://etcd.server:4001/v2/keys/edu/fsc/upstream/${ip} -XPUT -d value=${ip}:${port} -d ttl=30
fi
