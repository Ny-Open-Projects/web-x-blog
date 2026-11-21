# 画面线理解：05.搭建Spark集群（准备工作）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\05.搭建Spark集群（准备工作）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:44, 01:49, 02:06, 02:34, 02:55, 03:15, 03:39, 03:49, 04:06, 04:25, 04:47, 05:11, 05:25, 05:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:20:32

1) 这一组画面整体在讲什么（一句话）：
在Linux集群上搭建Spark环境，包括下载Spark、配置hosts文件、关闭防火墙以及配置SSH免密登录。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：介绍Spark集群搭建，指出下载地址为 http://spark.apache.org/downloads.html，选择版本为2.4.3，包类型为Pre-built for Apache Hadoop 2.7 and later，下载文件为 spark-2.4.3-bin-hadoop2.7.tgz。
画面2：展示环境准备，列出三台Linux主机的IP地址、节点名称和部署路径，并给出在hosts文件中添加映射的命令：vim /etc/hosts。
画面3：展示三台Linux主机的桌面环境截图，用于说明环境准备。
画面4：在node2主机的终端中显示hosts文件内容，包含本机和三台节点的映射。
画面5：在node3主机的终端中显示hosts文件内容，包含本机和三台节点的映射。
画面6：在node1主机的终端中显示hosts文件内容，包含本机和三台节点的映射。
画面7：展示在hosts文件中添加节点映射的命令：vim /etc/hosts。
画面8：在node1主机的终端中执行ping命令测试节点连通性，结果为成功，然后执行service iptables stop关闭防火墙。
画面9：在node1主机的终端中执行iptables命令关闭防火墙，显示“确定”提示。
画面10：展示在hosts文件中添加节点映射的命令：vim /etc/hosts。
画面11：展示配置SSH免密登录的步骤：ssh-keygen、ssh-copy-id node1、ssh-copy-id node2、ssh-copy-id node3。
画面12：在node1主机的终端中执行ssh-copy-id node1命令，提示确认主机指纹，输入密码后继续。
画面13：在node1主机的终端中执行ssh-copy-id node2命令，提示确认主机指纹，输入密码后继续。
画面14：展示配置SSH免密登录的步骤：ssh-keygen、ssh-copy-id node1、ssh-copy-id node2、ssh-copy-id node3。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
Download Apache Spark™
1. Choose a Spark release: 2.4.3 (May 07 2019) 
2. Choose a package type: Pre-built for Apache Hadoop 2.7 and later 
3. Download Spark: spark-2.4.3-bin-hadoop2.7.tgz
Link with Spark
Spark artifacts are hosted in Maven Central. You can add a Maven dependency with the following coordinates
groupId: org.apache.spark
artifactId: spark-core_2.11
version: 2.4.3

画面2：
2.2. 环境准备
准备3台Linux虚拟机，分别如下：
| 机器地址 | 节点名称 | 部署路径 |
| --- | --- | --- |
| 192.168.31.82 | node1 | /itcast |
| 192.168.31.83 | node2 | /itcast |
| 192.168.31.84 | node3 | /itcast |
在hosts文件中添加节点的映射：
1 vim /etc/hosts
2 192.168.31.82 itcast
3 192.168.31.82 node1 node01
4 192.168.31.83 node2 node02
5 192.168.31.84 node3 node03
6
7 #关闭防火墙
8 service iptables stop
9 #禁止开机启动
10 chkconfig iptables off

画面3：
无代码或配置。

画面4：
/etc/hosts 5L, 239C
127.0.0.1 localhost localhost.localdomain localhost4 localhost4.localdomain4
::1 localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.31.82 itcast
192.168.31.83 node2 node02
192.168.31.84 node3 node03

画面5：
无代码或配置。

画面6：
无代码或配置。

画面7：
无代码或配置。

画面8：
PING itcast (192.168.31.82) 56(84) bytes of data.
64 bytes from itcast (192.168.31.82): icmp_seq=1 ttl=64 time=0.018 ms
64 bytes from itcast (192.168.31.82): icmp_seq=2 ttl=64 time=0.031 ms
--- itcast ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1936ms
rtt min/avg/max/mdev = 0.018/0.024/0.031/0.008 ms
PING node1 (192.168.31.82) 56(84) bytes of data.
64 bytes from node1 (192.168.31.82): icmp_seq=1 ttl=64 time=2.62 ms
64 bytes from node1 (192.168.31.82): icmp_seq=2 ttl=64 time=0.654 ms
--- node1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1049ms
rtt min/avg/max/mdev = 0.654/1.641/2.628/0.987 ms
PING node3 (192.168.31.84) 56(84) bytes of data.
64 bytes from node3 (192.168.31.84): icmp_seq=1 ttl=64 time=1.87 ms
--- node3 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 923ms
rtt min/avg/max/mdev = 1.876/1.876/1.876/0.000 ms
[root@itcast ~]# service iptables stop

画面9：
iptables: 将链设置为政策 ACCEPT
iptables: 清除防火墙规则：
iptables: 正在修改模块：
[root@itcast ~]# chkconfig iptables off

画面10：
无代码或配置。

画面11：
2.3. 配置免密登录
#生成秘钥，一路回车
ssh-keygen
ssh-copy-id node1
ssh-copy-id node2
ssh-copy-id node3

2.4. 开始安装
#创建安装目录，3台机器都要创建
mkdir /itcast

#上传spark-2.4.3-bin-hadoop2.7.tgz到该目录，进行解压
tar -xvf spark-2.4.3-bin-hadoop2.7.tgz
mv spark-2.4.3-bin-hadoop2.7 spark

画面12：
Enter file in which to save the key (/root/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key's randomart image is:
+--[ RSA 2048]----+
*o.
o .o
o .o
o .o
o .o
o .o
o .o
o .o
o .o
+----[ RSA 2048]----+
The key fingerprint is:
20:76:47:16:87:9d:71:bf:fc:ac:b6:86:da:c3:48 root@itcast
The key's randomart image is:
+--[ RSA 2048]----+
*o.
o .o
o .o
o .o
o .o
o .o
o .o
o .o
o .o
+----[ RSA 2048]----+
The key fingerprint is:
20:76:47:16:87:9d:71:bf:fc:ac:b6:86:da:c3:48 root@itcast
The key's randomart image is:
+--[ RSA 2048]----+
*o.
o .o
o .o
o .o
o .o
o .o
o .o
o .o
o .o
+----[ RSA 2048]----+
The key
