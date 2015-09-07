#!/bin/sh
rm spm.tar.gz
rm thirdparty.tar.gz
rm docker.tar.gz
ftp -inv 183.203.18.61 << EOF
user devftp devftp
bin
get spm.tar.gz
get thirdparty.tar.gz
get docker.tar.gz
bye
EOF

tar -zxvf spm.tar.gz 
rm -R new_home/res/spm 
mv spm new_home/res/

tar -zxvf thirdparty.tar.gz 
rm -R new_home/res/thirdparty  
mv thirdparty new_home/res/

tar -zxvf docker.tar.gz
rm -R ~/docker
mv docker ~

rm spm.tar.gz thirdparty.tar.gz docker.tar.gz
