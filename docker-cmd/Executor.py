#! /usr/bin/python
#coding:utf-8
import os

class Executor:
    # value镜像
    valueImg = {'value-cs': 'reg.docker:5000/ubuntu13.10:cs',  # 缓存镜像
                'value-cw': 'reg.docker:5000/ubuntu13.10:cw2.1',  #课件镜像
                'value-db': 'reg.docker:5000/ubuntu13.10:mysql',  #数据库镜像
                'value-dns': 'reg.docker:5000/ubuntu13.10:dns',  #dns镜像
                'value-fdfs': 'reg.docker:5000/ubuntu13.10:fdfs',  #文件系统镜像
                'value-solr': 'reg.docker:5000/ubuntu13.10:solr',  #全文搜索镜像
                'value-es': 'reg.docker:5000/ubuntu13.10:es',  #es全文搜索镜像
                'value-slb': 'reg.docker:5000/ubuntu13.10:slb',  #负载均衡镜像
                'value-sms': 'reg.docker:5000/ubuntu13.10:vss',  #流媒体服务器
                'value-etcd': 'reg.docker:5000/ubuntu13.10:etcd',  #etcd键值服务
        	'value-zoo': 'reg.docker:5000/ubuntu13.10:zoo',  #zookeeper服务
        	'value-metaq': 'reg.docker:5000/ubuntu13.10:metaq',  #metaq服务
        	'value-nodejs': 'reg.docker:5000/ubuntu13.10:nodejs',  #nodejs服务
        	'value-redis': 'reg.docker:5000/ubuntu13.10:redis',  #redis服务
        	'value-ftp': 'reg.docker:5000/ubuntu13.10:ftp',  #ftp服务
        	'value-atlas': 'reg.docker:5000/ubuntu13.10:atlas',  #atlas服务

                'eduos-as': 'reg.docker:5000/ubuntu13.10:eduos-as',  #eduos应用镜像
                'eduos-fsc': 'reg.docker:5000/ubuntu13.10:eduos-fsc',  #eduos-fsc应用镜像
                'elm-as': 'reg.docker:5000/ubuntu13.10:elm-as',  #elmos
                'elo-as': 'reg.docker:5000/ubuntu13.10:elo-as',  #elo
                'el-stat': 'reg.docker:5000/ubuntu13.10:el-stat', #el-stat
                'cas-as': 'reg.docker:5000/ubuntu13.10:elo-as', #cas-as

		'coe-fsc': 'reg.docker:5000/ubuntu13.10:eduos-fsc',  #eduos-fsc应用镜像
                'coe-os-as': 'reg.docker:5000/ubuntu13.10:coe-os-as',
                'coe-smp-as': 'reg.docker:5000/ubuntu13.10:coe-smp-as',
                'coe-sop-as': 'reg.docker:5000/ubuntu13.10:coe-sop-as'
    }
    #可执行命令
    cmdTuple = ('create', 'remove', 'restart','stop', 'ssh', 'app_restart')
    prop = {}

    def __init__(self, name, portDic):
        self.name = name
        for key, value in portDic.items():
            self[key] = value

    def __getitem__(self, key):
        return self.prop[key]

    def __setitem__(self, key, value):
        self.prop[key] = value

    #执行命令
    def execute(self, cmd, index="0"):
        if cmd not in Executor.cmdTuple:
            print("%s指令不包含在%s中" % (cmd, Executor.cmdTuple))
            return
        elif index.isdigit() == False:
            print("第二个参数必须为数字")
            return
        method = getattr(self, cmd)
        method(index)

    #创建容器
    def create(self, index):
        print("创建id为%s的容器" % (self.name + index))
        port_str = ""
        for key, value in self["portMap"].items():
            port_str += " -p " + key + ":" + value
        volume_str = ""
        for key, value in self["volumeMap"].items():
            volume_str += " -v " + key + ":" + value
        img_str = Executor.valueImg[self.name]
        ip = self.get_sn_ip()
        exe_str = "sudo weave run %s %s %s --dns 192.168.2.2 --name %s %s /usr/bin/supervisord" % (ip,port_str, volume_str, self.get_docker_id(index), img_str)
        # print(exe_str)
        os.system(exe_str)
        # self.set_ip(index)

    #删除容器
    def remove(self, index):
        print("删除id为%s的容器" % (self.name + index))
        exe_str = "sudo docker rm -f %s " % (self.get_docker_id(index),)
        os.system(exe_str)
        # print(exe_str)

    #重启容器
    def restart(self, index):
        print("重启id为%s的容器" % (self.name + index))
        exe_str = "sudo docker stop %s " % (self.get_docker_id(index),)
        os.system(exe_str)
        ip = self.get_sn_ip()
        exe_str = "sudo weave start %s %s " % (ip, self.get_docker_id(index),)
        os.system(exe_str)
        # print(exe_str)
        # self.set_ip(index)

    #关闭容器
    def stop(self, index):
        print("关闭id为%s的容器" % (self.name + index))
        exe_str = "sudo docker stop %s " % (self.get_docker_id(index),)
        os.system(exe_str)

    def get_docker_id(self, index):
        if index == "0":
            return self.name
        else:
            return self.name + index

    #重启应用
    def app_restart(self, index):
        print("重启id为%s的应用" % (self.name + index))
        ssh_port = self["sshPort"]
        exe_str = "ssh root@127.0.0.1 -p %s 'sh /root/restart.sh'" % (ssh_port,)
        os.system(exe_str)
        # print(exe_str)

    #设置ip
    # def set_ip(self, index):
    #     print("设置id为%s的ip %s" % ((self.name + index), self.get_ip()))
    #     ip = self["ip"]
    #     exe_str = "sudo ./pipework br1 %s 192.168.2.%s/24" % (self.get_docker_id(index), ip)
    #     os.system(exe_str)
    #     # print(exe_str)

    def get_sn_ip(self):
        ns = os.environ.get('DOCKER_NS')
        return ns % (self["ip"],)

    def get_ip(self):
        ns = os.environ.get('DOCKER_NS')
        ns = ns.replace('/16', '')
        return ns % (self["ip"],)

    #ssh 连接
    def ssh(self, index):
        exe_str = "ssh root@127.0.0.1 -p " + self["sshPort"]
        os.system(exe_str)
        # print(exe_str)
