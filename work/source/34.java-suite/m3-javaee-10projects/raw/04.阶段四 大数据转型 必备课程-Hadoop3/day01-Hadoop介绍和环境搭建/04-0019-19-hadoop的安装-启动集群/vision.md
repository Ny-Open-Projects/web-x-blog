# 画面线理解：19-hadoop的安装-启动集群

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\19-hadoop的安装-启动集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:26, 01:22, 02:24, 03:03, 03:58, 04:49, 05:25, 06:16, 06:39, 08:20, 09:08, 10:06, 10:33, 11:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:47:14

1) 这一组画面整体在讲什么（一句话）：
在 Linux 环境下配置并启动 Hadoop 集群，包括环境变量设置、配置文件分发、服务启动及 Web 界面验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 SecureCRT 中，终端显示 Hadoop 集群的登录提示符，底部状态栏显示命令 `service iptables stop`。
画面 2: Typora 中的 PPT 页面，标题为“6. 格式化HDFS”，列出格式化 HDFS 的原因和命令 `hdfs namenode -format`。
画面 3: Typora 中的 PPT 页面，标题为“此时便可以通过如下三个URL访问Hadoop了”，列出 HDFS 和 Yarn 的访问 URL，并展示 `hadoop-env.sh` 文件中的环境变量设置。
画面 4: SecureCRT 终端中显示 `hadoop-env.sh` 文件内容，包含多个 `export` 命令，如 `export HDFS_NAMENODE_USER="root"`。
画面 5: SecureCRT 终端中，用户在 `hadoop-3.1.1` 目录下执行 `ls` 查看文件，然后执行 `scp hadoop-env.sh node02:$PWD` 将文件复制到 node02。
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
export HADOOP_HOME=/export/servers/hadoop-3.1.1/
export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH

6. 格式化HDFS
• 为什么要格式化HDFS
o HDFS需要一个格式化的过程来创建放元数据(image, editlog)的目录
hdfs namenode -format

7. 启动集群
• 会启动所有的worker但和相关运行，也可以手动运行，但是没必要
/export/servers/hadoop-3.1.1/sbin/start-dfs.sh
/export/servers/hadoop-3.1.1/sbin/start-yarn.sh
mapred --daemon start historyserver
```

画面 3:
```
报表：设置hadoop-env.sh
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
[root@node01 hadoop-3.1.1]# cd etc/hadoop
[root@node01 hadoop]# ls
capacity-scheduler.xml  httpfs-log4j.properties  mapred-site.xml
configuration.xsl       httpfs-site.xml         ssl-client.xml.example
container-executor.cfg  kms-env.sh              ssl-server.xml.example
core-site.xml           kms-site.xml            users_ec_policies.xml.template
hadoop-env.cmd          log4j.properties        workers
hadoop-metrics2.properties  mapred-env.cmd  yarn-env.sh
hadoop-policy.xml       log4j.properties        yarnservice-log4j.properties
hadoop-user-functions.sh.example  mapred-queues.xml.template  yarn-site.xml
httpfs-site.xml         mapred-env.sh           yarn-env.sh
hdfs-site.xml           mapred-site.xml         yarn-site.xml
[root@node01 hadoop]# scp hadoop-env.sh node02:$PWD
[root@node01 hadoop]# cd ../
```

画面 7:
```
Starting namenodes on [node01]
Starting secondary namenodes on [node01.hadoop.com]
2019-04-22 21:06:09,511 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform...
using builtin-java classes where applicable
24129 DataNode
24427 SecondaryNameNode
23980 NameNode
8206 QuorumPeerMain
[root@node01 hadoop-3.1.1]# sbin/start-yarn.sh
Starting resourcemanager
Starting nodemangers
```

画面 10:
```
"abc.txt" 1L, 12C written
[root@node01 hadoop-3.1.1]# ls
abc.txt  a.txt  bin  data  etc  include  lib  libexec  LICENSE.txt  logs  NOTICE.txt  README.txt  sbin  share
[root@node01 hadoop-3.1.1]# hdfs dfs -put abc.txt /
-bash: hdfs: command not found
[root@node01 hadoop-3.1.1]# jps
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
192.168.174.100  node01.hadoop.com
192.168.174.110  node02.hadoop.com
192.168.174.120  node03.hadoop.com
192.168.174.130  node04.hadoop.com
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
