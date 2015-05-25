#!/bin/bash

#安装
sudo apt-get install gcc make
wget https://www.python.org/ftp/python/3.4.1/Python-3.4.1.tgz
tar -xvf Python-3.4.1.tgz
cd Python-3.4.1/
./configure
make
sudo make install
echo "alias python=python3.4" >> ~/.bashrc
cd -
rm Python-3.4.1.tgz
rm -R Python-3.4.1/
