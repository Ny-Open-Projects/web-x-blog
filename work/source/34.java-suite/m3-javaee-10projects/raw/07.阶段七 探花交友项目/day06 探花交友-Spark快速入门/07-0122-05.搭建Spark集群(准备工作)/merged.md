# 05.搭建Spark集群（准备工作）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\05.搭建Spark集群（准备工作）_【海量资源尽在 666java.com】.mp4
- 时长 5分50秒（音频 350s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 那么接下来呢我们就来动手搭建啊Spark集群呃 那么Spark集群呢它呢是可以在Windows上面去运行那么也可以是在Linux上面去做运行那么一般而言呢啊我们都是会选择在Linux上做运行啊因为我们最终我们的项目发布啊那么肯定会都会是在Linux上面的呃 那么我们的课程呢也是会
[00:27] 基于这个linux来做一个这个部署那么当然了我们在这呢所使用的这个linux的版本呢是centOS 6.5这样的一个版本好那么把这个交代清楚之后呢接下来呢我们就开始去做一个搭建了那么当然了搭建之前呢首先需要去做一个下载这个呢是他的下载地址那么我就不打开来看了啊那么大概呢会看到这样的一个页面
[00:54] 那么我们在这儿所使用的是Spark的目前的最新版那么就是2.4.3这样的一个版本那么它所对应的好多谱的版本是2.7以上的这样的一个版本好那么这个是我们就使用它来做一个部署那么接下来我们来看一下环境那么在这儿我们准备了三台Linux的虚拟机
[01:24] 那么分别是1916831.828384这三台机器然后它们的节点的名称是node1node2和node3然后所部署的路径都是根目录下面的itcast这样的一个目录好那么接下来我们来看一下就这三台机器分别是这一台和这一台和这一台三台机器那么接下来我们先把这个节点的映射我们先
[01:53] 添加进来那么我们先打开我们这个机器的host这样的一个文件然后呢可以看到呢是不是已经就添加好了对吧添加好了当然了我们还需要把自己的这个主机这个名呢也加上来那么我们就这样来写一下吧这个大家应该能够看懂吧
[02:12] 做这样的一个映射那么当然了在这个位置我们写了一个node1和node01那么也就是说我们通过node1去访问或者说通过node01访问也是可以的好嘞好那么我们就来保存退出一下那么这个是这个是第一台机器那我们接下来看第二台机器那么同样的是一样的那么我们到这去然后把它也拷贝过来
[02:41] 保障好保存退出那么到第三台机器呢我们也来去访问一下打开它然后呢我们去也是添加到这个位置来好保存退出一下好嘞那么这三台机器呢就已经OK了那我们可以来测试一下然后呢ITCast当然这个可能会有问题啊就是我们需要去改一下那么这个我们改成什么呢这个机器是84要指向到
[03:10] 本机啊好那么保存一下然后呢这个呢也是同样的道理那么这个改成83这个改成83好保存退出一下好那么我们可以来测试一下itcastok好那么是不是就拼到本机了对吧我们再来拼一下node1没有问题然后呢node3也没有问题好嘞好这个呢都是ok的
[03:38] 那么接下来我们还需要把防火墙给它关闭掉然后我们来防火墙关闭一下stop一下这个也是stop一下然后这个也是stop一下那么最好其实我们可以去不让它开机启动是吧叫cacconfig然后我们去找到ib tables然后off把它关闭掉这样的话它在下次启动的时候也就不会去
[04:07] 把我们防火墙启动起来了好然后我们就加到这然后这个是禁止禁止什么开机开机启动好嘞好那么这样的话我们的基础工作就ok了那么接下来我们还需要去把这个免密去配置一下如果之前大家已经配置过的话那么这个就不需要去做个配置了
[04:36] 那我们通过在这台机器吧sh 干什么呢这个去生成我们的一个这个key对吧一路回车啊一路回车好生成好之后呢我们要通过这个ssh这个copy id啊这样的一个啊这样的一个命令去做一个拷贝然后呢我们先拷贝到node1也就是说先把这个免密的这个密钥呢先拷贝到我们的这个本机啊yes
[05:05] 然后呢去输入密码就是这个是root用户的密码root123去做一个拷贝OK然后呢我再拷到node2上面然后呢yes然后呢输入密码没有问题对吧然后呢再去拷贝到这个node3这个机器yes好这样的话呢我们就绵密的工作呢就已经做好了
[05:34] 好那么接下来呢我们就可以来动手去做一个这个安装了那么这样我们先把这个视频呢停一下到这儿基本上我们的这个安装的前置的一些准备工作呢是不是都已经就搞定了哎OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在Linux集群上搭建Spark环境，包括下载Spark、配置hosts文件、关闭防火墙以及配置SSH免密登录。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：介绍Spark集群搭建，指出下载地址为 http://Spark.apache.org/downloads.html，选择版本为2.4.3，包类型为Pre-built for Apache Hadoop 2.7 and later，下载文件为 Spark-2.4.3-bin-hadoop2.7.tgz。
画面2：展示环境准备，列出三台Linux主机的IP地址、节点名称和部署路径，并给出在hosts文件中添加映射的命令：vim /etc/hosts。
画面3：展示三台Linux主机的桌面环境截图，用于说明环境准备。
画面4：在node2主机的终端中显示hosts文件内容，包含本机和三台节点的映射。
画面5：在node3主机的终端中显示hosts文件内容，包含本机和三台节点的映射。
画面6：在node1主机的终端中显示hosts文件内容，包含本机和三台节点的映射。
画面7：展示在hosts文件中添加节点映射的命令：vim /etc/hosts。
画面8：在node1主机的终端中执行ping命令测试节点连通性，结果为成功，然后执行Service iptables stop关闭防火墙。
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
3. Download Spark: Spark-2.4.3-bin-hadoop2.7.tgz
Link with Spark
Spark artifacts are hosted in Maven Central. You can add a Maven dependency with the following coordinates
groupId: org.apache.Spark
artifactId: Spark-core_2.11
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
8 Service iptables stop
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
[root@itcast ~]# Service iptables stop

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

#上传Spark-2.4.3-bin-hadoop2.7.tgz到该目录，进行解压
tar -xvf Spark-2.4.3-bin-hadoop2.7.tgz
mv Spark-2.4.3-bin-hadoop2.7 Spark

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

