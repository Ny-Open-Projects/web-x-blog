# 画面线理解：7.3 Druid安装配置

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.3 Druid安装配置_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:41, 04:18, 06:33, 08:09, 10:34, 13:10, 14:47, 15:59, 17:24, 18:25, 19:28, 20:08, 20:55, 21:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:40:15

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 环境下安装并配置 Apache Druid，包括 JDK、MySQL 驱动、Zookeeper、Kafka 和 Druid 本身，并启动服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
要点：展示课程文档“1.2 环境”章节，说明环境配置为 2核、8G内存、CentOS 7、jdk 1.8、apache-druid 0.15.6，并给出 Oracle JDK 下载页面链接。

画面 2：
要点：展示设置 JAVA_HOME 环境变量的命令，以及编辑 /etc/hosts 文件添加节点映射。同时展示将 MySQL 驱动文件复制到 Druid 的 metadata-storage 目录。

画面 3：
要点：展示安装 Kafka 的步骤，包括下载、解压、配置 server.properties 文件（包含 zookeeper.connect 和 log.dirs 等配置），并启动 Kafka 服务。

画面 4：
要点：展示下载 Druid 的命令，解压后查看目录结构，包括 bin、conf、extensions 等目录。

画面 5：
要点：展示进入 Druid 的 conf 目录，准备进行配置。

画面 6：
要点：展示下载 Druid 的命令，解压后查看目录结构。

画面 7：
要点：展示 Druid 的配置文件说明，包括不同模式（cluster、single-server）下的组件配置。

画面 8：
要点：展示 Navicat Premium 的启动界面，版本为 12.0.18，用于后续数据库操作。

画面 9：
要点：展示进入 Druid 的 broker 目录，准备进行配置。

画面 10：
要点：展示进入 Druid 的 bin 目录，准备启动服务。

画面 11：
要点：展示 Druid 的配置文件目录结构，包括 cluster、common、historical、middleManager、master、query、broker、router、single-server 等子目录。

画面 12：
要点：展示进入 Druid 的 extensions 目录，复制 MySQL 驱动文件到 metadata-storage 目录。

画面 13：
要点：展示黑马程序员官网页面。

画面 14：
要点：展示启动 Druid 单节点服务的命令，以及 Navicat Premium 中显示的 Druid 数据库连接成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```text
2核，8G内存，CentOS 7，jdk 1.8，apache-druid 0.15.6
https://www.oracle.com/technetwork/java/java-archive-139210.html
在下载页面选择java SE 8 rpm文件，下载过程中需要登录oracle网站，安装jdk：
[root@node2-vmb6 ~]# cd /opt/software/
[root@node2-vmb6 software]# wget -c https://download.oracle.com/otn/java/jdk/8u202-nh8/156187064c90e26a475fa801551e/jdk-8u202-linux-x64.rpm
AuthParam=156187064c90e26a475fa801551e/jdk-8u202-linux-x64.rpm
[root@node2-vmb6 software]# mv jdk-8u202-linux-x64.rpm
[root@node2-vmb6 software]# rpm -ivh jdk-8u202-linux-x64.rpm
[root@node2-vmb6 software]# java -version
```

画面 2：
```text
设置JAVA_HOME环境变量：
[root@node2-vmb6 ~]# vim /etc/profile
export PATH USER LOGNAME MAIL HOSTNAME HISTSIZE HISTCONTROL
--此行之后插入以下设定
export JAVA_HOME=/usr/java/jdk1.8.0_202-amd64
export PATH=$JAVA_HOME/bin:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar
export CLASSPATH=.:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar
[root@node2-vmb6 ~]# source /etc/profile
设置hostname
[root@node2-vmb6 broker]# vim /etc/hosts
127.0.0.1 node2-vmb6.yyy
1.2.2 安装mysql驱动
将mysql驱动放置在extensions/mysql-metadata-storage目录下。
[root@node2-vmb6 ~]# cp /opt/software/jar/mysql-connector-java-5.1.44-bin.jar
/opt/druid/extensions/mysql-metadata-storage/
```

画面 3：
```text
# 下载kafka
[root@node2-vmb6 software]# wget -c https://archive.apache.org/dist/kafka/2.1.2-3.1.0.tgz
[root@node2-vmb6 software]# tar -zxvf kafka_2.12-2.3.8.tgz
[root@node2-vmb6 software]# cd /opt/software/kafka_2.12-2.3.8
# 配置kafka服务器，日志目录，端口等
[root@node2-vmb6 config]# vim /opt/software/kafka_2.12-2.3.8/config/server.properties
zookeeper.connect=172.17.0.143:2181
log.dirs=/tmp/kafka-logs
listeners=PLAINTEXT://172.17.0.143:9092
advertised.listeners=PLAINTEXT://172.17.0.143:9092
# 启动kafka
[root@node2-vmb6 kafka_2.12-2.3.8]# cd /opt/software/kafka_2.12-2.3.8
[root@node2-vmb6 kafka_2.12-2.3.8]# ./bin/kafka-server-start.sh config/server.properties &
# 关闭kafka
[root@node2-vmb6 kafka_2.12-2.3.8]# ./bin/kafka-server-stop.sh
```

画面 4：
```text
下载Druid，下载页面：https://druid.apache.org/downloads.html
[root@node2-vmb6 software]# wget -c http://mirrors.bjt.edu.cn/apache/incubator/druid/0.15.0-incubating/apache-druid-0.15.0-incubating-bin.tar.gz
[root@node2-vmb6 software]# tar -zxvf apache-druid-0.15.0-incubating-bin.tar.gz
[root@node2-vmb6 software]# mv apache-druid-0.15.0-incubating apache-druid
--执行文件
--配置文件
--扩展文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的H
