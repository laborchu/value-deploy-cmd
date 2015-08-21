#!/bin/sh 
for k in $( seq 1 1 )
do
  if [ $k -eq 1 ];then
    ssh root@127.0.0.1 -p 40721 "rm -R /home/res/circle/webapp/circle"
    cp /home/ftp/dev/res/eduos/webapp/circle.war /home/res/circle/webapp/circle.war
    unzip -oq /home/res/circle/webapp/circle.war -d /home/res/circle/webapp/circle
    ssh root@127.0.0.1 -p 40721 "chmod -R 777 /home/res/circle/webapp/circle"
  fi
  python /home/value/docker/python/circle_as.py app_restart $k
done
