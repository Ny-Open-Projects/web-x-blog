# 画面线理解：05.通过非docker的方式进行RocketMQ的安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\05.通过非docker的方式进行RocketMQ的安装【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:45, 01:46, 02:47, 03:29, 05:07, 06:08, 07:31, 08:19, 08:56, 09:28, 10:10, 10:49, 11:09, 11:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:56:58

1) 这一组画面整体在讲什么（一句话）：
演示如何在非Docker环境下手动安装并运行RocketMQ 4.3.2，并解决因内存不足导致的启动失败问题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PDF文档中“1.4.2. 非Docker安装”章节，包含下载地址和初始安装命令（cd /home, unzip, cd），以及启动NameServer和Broker的命令。其中Broker启动失败，提示“Cannot allocate memory”。
画面2：在远程服务器终端中，解压RocketMQ压缩包，查看解压后的目录结构。
画面3：显示SSH连接到Ubuntu服务器的登录界面。
画面4：PDF文档中解释Broker启动失败的原因是内存不足，并说明RocketMQ默认配置内存过大，建议调整默认值。
画面5：在终端中编辑并设置JVM配置，包括设置JAVA_HOME、CLASSPATH，并定义JAVA_OPT变量。
画面6：终端中执行numactl命令，根据NUMA节点分配内存。
画面7：在终端中执行启动NameServer命令，成功启动并显示“Name Server boot success”。
画面8：PDF文档中展示发送消息的示例代码（tools.sh org.apache.rocketmq.example.quickstart.Consumer）。
画面9：PDF文档中展示发送消息的示例代码（tools.sh org.apache.rocketmq.example.quickstart.Producer）。
画面10：终端中执行发送消息命令，出现“MQLClientException: No route info of this topic, TopicTest”错误，表明Topic未创建或配置错误。
画面11：PDF文档中再次展示发送消息的示例代码（tools.sh org.apache.rocketmq.example.quickstart.Producer）。
画面12：PDF文档中展示消费消息的示例代码（tools.sh org.apache.rocketmq.example.quickstart.Consumer）。
画面13：终端中执行启动NameServer命令，成功启动并显示“Name Server boot success”。
画面14：PDF文档中展示“1.4.2. 非Docker安装”章节，包含下载地址和初始安装命令（cd /home, unzip, cd），以及启动NameServer和Broker的命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
cd /home
unzip rocketmq-all-4.3.2-bin-release.zip
cd rocketmq-all-4.3.2-bin-release
#启动nameserver
bin/mqnamesrv
#启动broker
bin/mqbroker -n 172.16.185.55:9876 #-n 指定nameserver地址和端口

画面2：
root@itcast:~# cd rocketmq-all-4.3.2-bin-release/
root@itcast:rocketmq-all-4.3.2-bin-release# ll
total 52
drwxr-xr-x 2 root root 4996 Nov 5 16:46 ./
drwxr-xr-x 2 root root 4996 Nov 5 16:46 ../
drwxr-xr-x 2 root root 4996 Nov 5 16:46 benchmark/
drwxr-xr-x 2 root root 4996 Nov 5 16:46 bin/
drwxr-xr-x 2 root root 4996 Nov 5 16:46 conf/
drwxr-xr-x 2 root root 4996 Nov 5 16:46 lib/
-rw-r--r-- 1 root root 17339 Nov 5 16:46 LICENSE
-rw-r--r-- 1 root root 1257 Nov 5 16:46 NOTICE
-rw-r--r-- 1 root root 7482 Nov 5 16:46 README.md
root@itcast:rocketmq-all-4.3.2-bin-release# cd bin/
root@itcast:bin#

画面5：
echo $ENVIRON: $! !!
exit 1
# JAVA Configuration
export JAVA_HOME=/usr/java
export JAVA_HOME=/usr/java
export BASE_DIR=$(dirname $0)/..
export CLASSPATH=:$CLASSPATH
# JVM Configuration
JAVA_OPT="$JAVA_OPT" -server -Xms8g -Xmx8g -Xmn4g
JAVA_OPT="$JAVA_OPT" -XX:UseCGroupMemorySize=16m -XX:GIReservePercent=25 -XX:InitiatingHeapOccupanc
yPercent=30 -XX:SoftMaxHeapSize=16m -XX:SurvivorRatio=8
JAVA_OPT="$JAVA_OPT" -verbose:gc -Xloggc:/dev/shm/mq_gc.log -XX:+PrintGCDetails -XX:+PrintDateStamps -XX
:PrintApplicationStoppedTime -XX:NumberOfGCLogFiles=5 -XX:GCLogFileSiz=30m
JAVA_OPT="$JAVA_OPT" -XX:OmitStackTraceInFastThrow
JAVA_OPT="$JAVA_OPT" -XX:AlwaysPreTouch
JAVA_OPT="$JAVA_OPT" -XX:MaxDirectMemorySize=1g
JAVA_OPT="$JAVA_OPT" -XX:UseLargePages -XX:UseBiasedLocking
JAVA_OPT="$JAVA_OPT" -Djava.ext.dirs=$JAVA_HOME/jre/lib/ext -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -
