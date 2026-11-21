# 19-hadoop的安装-启动集群

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\19-hadoop的安装-启动集群【海量资源尽在 ubkz.com】.mp4
- 时长 11分14秒（音频 674s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来验证刚才的配置是否有效接下来我们要启动我们的集群在启动之前我们先要对HDFS做一个格式化为什么要格式化呢是因为它在格式化的过程中它会给我们创建一些目录这些目录用来存放原数据信息所以必须要格式化OK 我把这个复制一下复制完之后我们要在第一台主机第一个节点
[00:29] 那么要进到哪里呢我必须保证呢我现在在我Hadoop的一个主目录你看我现在不在我应该回到我的Hadoop这个目录去来执行这个命令来我把这句话直接粘贴为什么要必须回到这个主目录呢我复制了两个是因为我这个地方是B代表这个目录下面的B目录里边有一个HDFS这个程序
[01:00] 然后呢NameNode-format然后回程稍等它让你输个Y如果有让你输个输个这个Y或N你就输个Y然后输个Y稍等好这个时候呢就格式化成功格式化的时候呢它会创你一些中间文件好我们不管好格式化完了之后呢接下来我们来继续我们来启动我们的机器群启动呢分两步第一步呢我们先启动我们的HDFS就是我们的分布式
[01:31] 文件存储我前边呢这个地方是一个绝对路径我呢直接这样子我用相对路径来启动在我当前的目录下面有一个Sbin有个Sbin那么我直接输个Sbin我要去用它下面的一个叫什么Start然后呢DFS有个SHOK咱们直接回车就可以了这就启动HDFS也就是分布式文件系统走稍等
[02:01] 好你发现启动的时候它出现了一些error也就是错误它说呢这个HDFS name node user没有定义这是环境面量没有定义这个出现这个问题呢大家不用担心这里边需要做一个额外的一个设置我在这里有个记录就是如果出错的时候呢我们需要配置hadoopenvsh把这几个呢添加到文件里边就可以了来我来复制一下
[02:30] 打开我们这个Hadoop env在哪里呢大家还记不记得在这个etc下面那我直接用相对路径etc下面有个Hadoop有一个叫Hadoop.env.sh好这个时候回到这个文件的末尾输个大写的G大写的GABCDEFG的G然后呢在最后这个位置把我刚才附着的粘贴一下来我再附着一份把这个呢粘贴一下
[03:00] 好站在这位置你可以把中间的空行去掉不去也可以OK好这些呢是配置它的一些环境面量比如说呢HDFS的Name node用的是什么用户呀我们都是Root用户Data node都是Root用户OK我保存退出好退出完之后呢我们还要做一件事情把这个文件呢分发给其他两台主机或者说你打开它们分别进行配置也可以那我进到这个ETC下面吧
[03:30] Hadoop下面好我现在呢就在这些文件的当前目录我SCP然后呢这个时候呢我干嘛呢我把Hadoopenv.sh分发分发到node02这个机子它的哪个目录呢PWD当前目录走好那么同样的分发给第三台主机它的当前目录好分发完之后呢我再回到我当前的主目录
[03:58] 我的这个Hadoop的主目录我们再一次启动再次启动就是SBIN下面呢有一个叫什么DFS稍等StartDFSSH稍等它开始启动我们的HDFS你看先启动NameNode再Node01这个主机然后再启动DataNodeOK这是DataNode4它呢会在各个主机里边呢从机里边启动DataNode
[04:28] 来启动SecondaryNameNode大家还记得SecondaryNameNode是不是来辅助这个NameNode好 稍等它启动完了启动完之后我们输个GPS来看一下NameNode启动成功DataNode启动成功SecondaryNameNode也有了咱们来看第二台机子GPS来 你看DataNode有了OK 这是重机再看第三台GPS好 DataNode也有了
[04:59] 好到此为止呢我们的HDFS启动成功那接下来呢我们就来启动我们的ERG群在这里ERG群呢就是Sbin下面一个startERG来我们来试一下这里边有Sbin下面一个startERG群SH走好稍等你看它先启动resource manager再启动node manager4
[05:29] 意思是在各个重机里面都会启动这个node manager稍等ok启动完毕我们来gps稍等你看多了很多这个node manager这个里边还有一个resource manager也就是说第一台主机它既是一个主节点又是一个重节点看第二台gpsnode managerdatanode都有了第三台node manager
[06:01] 对它都有了好有了之后呢我们可以通过浏览器来访问它的一些信息来我们打开浏览器在这里边呢我们可以输一个node01冒号50070这个50070呢是HDFS的一个访问端口回车你会发现看到这么一个页面它说node01 8020 active只要出现这么一个界面表示我们的HDFS
[06:31] 就启动成功你看这里它的一些描述信息还有呢它的NameNode的一些存储信息在这里那还有一个很重要的一个地方呢就是在U上角这个里边Unitly那么这个地方有一个叫BrowserFileSystem这个点开这就是我们的这个分布式一个文件系统这里边呢可以看到整个文件系统的所有的一些目录当然了现在我这里边是空的
[06:59] 没有给他添加数据你比如说我给大家上传一个数据你比如说我我给大家上传一个文件上来这个还没学过但是我给你用一下你看hdfsdfs里边有个命令叫put然后呢我可以上传一个文件我看我当前呢我踏起一个文件吧踏起一个abc.txtOK那这个时候我给他写点数据进去比如说vm abc.txt我随便来输点数据
[07:29] OK那接下来我要把这个文件这个ABC的帖体上传到我们的分布式文件系统怎么做呢HDFS DFS-PUT然后呢这个时候呢我可以把它ABC的帖体上传到我们分布式文件系统的根目录走它说呢它说命令没找到应该是HDFS DFS这个地方
[08:00] HDFS写反了稍等一下这个警告不用管来我们来看它是否把刚才这个ABCDAT上传到这里走你看到这里边是不是一个文件还有你可以选中你可以把这个文件的删掉这地方是删除按钮好那这是我们的这个HDFS那接下来呢我们再换一个端口换一个8088这个呢
[08:28] 可以访问的一二集群这就是我们的一二集群这里边呢有一些这个一些节点啦这个东西我们后边呢再给大家详细讲解好那么只要能访问这两个页面说明我们的Hadoop集群呢就搭建成功好那我们呢就先这样那这里面呢我还要强调一点大家注意一点在启动这个集群的时候呢首先有一点
[08:57] 你要保证你的zo kpart要先启动就这个进程要启动否则你的集群是启动不了的这是第一点第二点还要注意你在这里如果你输一个node01能够访问前提是你要做一个在windows里边要做一个域名声如果说你写node01你还可以这样写192.168.174.100
[09:26] 你这样写也是可以的这个都代表Node01如果说你想去写Node01你还要做一个映射这里跟大家说一下在哪里呢在这里呢我可以打开一个记事本好打开记事本稍等啊记事本稍等稍等记事本那么打开之后呢点右键然后呢这里边有一个叫一管理员权限运行那我们可以打开一个文件来看一下
[10:06] 在哪个文件呢在这里面文件里边打开打开之后呢找C盘C盘里边有一个叫WindowsWindows里边有一个Ctom32我们来找一下这里边呢有一个有一个有一个driversdrivers里边有一个etc好etc里边这里边选所有文件有一个文件叫hosts在这里边呢你需要对这个节点进行配置你看
[10:34] 这是三台机子的一些IP那么每个IP呢都有一个主机名这是Node01 Node02 Node03后面呢我又多写了一个你只有配了这个映射信息那么它才能够在浏览器里边呢使用Node01来访问好大家可以下去配一下注意我刚才之所以呢在这个地方给你打开记事本是因为呢很多Win10的系统呢它对这个文件呢
[11:01] 有全线的限制你是不能直接打开修改的如果说你通过这个位置来打开即时本的方式打开那它可以直接修改完之后保存好那我就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 Linux 环境下配置并启动 Hadoop 集群，包括环境变量设置、配置文件分发、服务启动及 Web 界面验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 SecureCRT 中，终端显示 Hadoop 集群的登录提示符，底部状态栏显示命令 `Service iptables stop`。
画面 2: Typora 中的 PPT 页面，标题为“6. 格式化HDFS”，列出格式化 HDFS 的原因和命令 `hdfs namenode -format`。
画面 3: Typora 中的 PPT 页面，标题为“此时便可以通过如下三个URL访问Hadoop了”，列出 HDFS 和 Yarn 的访问 URL，并展示 `Hadoop-env.sh` 文件中的环境变量设置。
画面 4: SecureCRT 终端中显示 `Hadoop-env.sh` 文件内容，包含多个 `export` 命令，如 `export HDFS_NAMENODE_USER="root"`。
画面 5: SecureCRT 终端中，用户在 `Hadoop-3.1.1` 目录下执行 `ls` 查看文件，然后执行 `scp Hadoop-env.sh node02:$PWD` 将文件复制到 node02。
画面 6: SecureCRT 终端中，用户在 node02 上登录，终端提示符为 `[root@node02 datanodeDatas]#`。
画面 7: SecureCRT 终端中，用户在 node01 上执行 `sbin/start-dfs.sh` 启动 HDFS，然后执行 `sbin/start-yarn.sh` 启动 Yarn，终端显示服务启动日志。
画面 8: 浏览器中访问 `node01:50070`，页面显示“无法访问此网站”，提示连接被拒绝。
画面 9: 浏览器中访问 `node01:50070/dshealth.html#overview`，显示 NameNode 存储信息，包括存储目录和 DFS 存储类型。
画面 10: SecureCRT 终端中，用户尝试执行 `hdfs dfs -put abc.txt /`，但提示 `command not found`，然后执行 `jps` 查看进程。
画面 11: 浏览器中访问 `node01:8088/cluster`，显示 Hadoop 集群的“About the Cluster”页面，包含集群指标和节点信息。
画面 12: 浏览器中访问 `node01:8088/cluster`，页面显示空白，无内容。
画面 13: Windows 记事本中打开 `hosts` 文件，内容包含 node01、node02、node03、node04 的 IP 地址映射。
画面 14: SecureCRT 终端中，用户执行 `jps` 查看进程，显示 DataNode、ResourceManager、NameNode、QuorumPeerMain 等进程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```
5. 在每个节点配置环境变量
vi /etc/profile
export HADOOP_HOME=/export/servers/Hadoop-3.1.1/
export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH

6. 格式化HDFS
• 为什么要格式化HDFS
o HDFS需要一个格式化的过程来创建放元数据(image, editlog)的目录
hdfs namenode -format

7. 启动集群
• 会启动所有的worker但和相关运行，也可以手动运行，但是没必要
/export/servers/Hadoop-3.1.1/sbin/start-dfs.sh
/export/servers/Hadoop-3.1.1/sbin/start-yarn.sh
mapred --daemon start historyserver
```

画面 3:
```
报表：设置Hadoop-env.sh
export HDFS_NAMENODE_USER="root"
export HDFS_DATANODE_USER="root"
export HDFS_SECONDARYNAMENODE_USER="root"
export YARN_RESOURCEMANAGER_USER="root"
export YARN_NODEMANAGER_USER="root"
```

画面 4:
```
# export HADOOP ENABLE BUILD PATHS="true"
# To prevent accidents, shell commands be (superficially) locked
# to only allow certain users to execute certain subcommands.
# It uses the format of (command)_(subcommand).USER.
# For example, to limit who can execute the namenode command,
# export HDFS NAMENODE USER=hdfs
export HDFS_NAMENODE_USER="root"
export HDFS_DATANODE_USER="root"
export HDFS_SECONDARYNAMENODE_USER="root"
export YARN_RESOURCEMANAGER_USER="root"
export YARN_NODEMANAGER_USER="root"
```

画面 5:
```
[root@node01 Hadoop-3.1.1]# cd etc/Hadoop
[root@node01 Hadoop]# ls
capacity-scheduler.xml  httpfs-log4j.properties  mapred-site.xml
configuration.xsl       httpfs-site.xml         ssl-client.xml.example
container-executor.cfg  kms-env.sh              ssl-server.xml.example
core-site.xml           kms-site.xml            users_ec_policies.xml.template
Hadoop-env.cmd          log4j.properties        workers
Hadoop-metrics2.properties  mapred-env.cmd  yarn-env.sh
Hadoop-policy.xml       log4j.properties        yarnservice-log4j.properties
Hadoop-user-functions.sh.example  mapred-queues.xml.template  yarn-site.xml
httpfs-site.xml         mapred-env.sh           yarn-env.sh
hdfs-site.xml           mapred-site.xml         yarn-site.xml
[root@node01 Hadoop]# scp Hadoop-env.sh node02:$PWD
[root@node01 Hadoop]# cd ../
```

画面 7:
```
Starting namenodes on [node01]
Starting secondary namenodes on [node01.Hadoop.com]
2019-04-22 21:06:09,511 WARN util.NativeCodeLoader: Unable to load native-Hadoop library for your platform...
using builtin-java classes where applicable
24129 DataNode
24427 SecondaryNameNode
23980 NameNode
8206 QuorumPeerMain
[root@node01 Hadoop-3.1.1]# sbin/start-yarn.sh
Starting resourcemanager
Starting nodemangers
```

画面 10:
```
"abc.txt" 1L, 12C written
[root@node01 Hadoop-3.1.1]# ls
abc.txt  a.txt  bin  data  etc  include  lib  libexec  LICENSE.txt  logs  NOTICE.txt  README.txt  sbin  share
[root@node01 Hadoop-3.1.1]# hdfs dfs -put abc.txt /
-bash: hdfs: command not found
[root@node01 Hadoop-3.1.1]# jps
24129 DataNode
24427 SecondaryNameNode
23980 NameNode
8206 QuorumPeerMain
```

画面 13:
```
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one space.
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a # symbol.
# For example:
# 102.54.94.97  rhino.acme.com  # source server
# 38.25.63.10  x.acme.com  # x client
# localhost name resolution is handled within DNS itself.
#127.0.0.1  www.itheima01.com
#127.0.0.1  api.itheima01.com
192.168.174.100  node01.Hadoop.com
192.168.174.110  node02.Hadoop.com
192.168.174.120  node03.Hadoop.com
192.168.174.130  node04.Hadoop.com
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2:
标题：6. 格式化HDFS
内容：
• 为什么要格式化HDFS
o HDFS需要一个格式化的过程来创建放元数据(image, editlog)的目录
命令：hdfs namenode -format

画面 3:
标题：此时便可以通过如下三个URL访问Hadoop了
内容：
• HDFS: http://192.1

