#!/bin/bash

#初始化docker域
domain="3"
if [ $DOCKER_NS ];then  
    echo "ORACLE_HOME = $DOCKER_NS"  
else  
    echo "export DOCKER_NS=192.168.${domain}.%s/16" >> ~/.bashrc
fi
