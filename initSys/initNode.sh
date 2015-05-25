#!/bin/bash
#安装nvm
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.25.1/install.sh | bash
source ~/.bashrc
#安装node
. ~/.nvm/nvm.sh
nvm install 0.10.36
echo "nvm use v0.10.36" >> ~/.bashrc
source ~/.bashrc
npm install -g bower
npm install -g grunt-cli
npm install -g spm@2.2.12
npm install spm-build@0.3.17 -g
