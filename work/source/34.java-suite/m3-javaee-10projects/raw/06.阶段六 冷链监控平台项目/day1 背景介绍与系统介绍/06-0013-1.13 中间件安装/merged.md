# 1.13 中间件安装

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day1 背景介绍与系统介绍
- 源文件：06.阶段六 冷链监控平台项目\day1 背景介绍与系统介绍\1.13 中间件安装_【海量资源尽在 666java.com】.mp4
- 时长 4分25秒（音频 266s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来看一看我们的基础组件基础组件里边包括我们的JDK的安装如果是在我们的开发环境比如说我们本地的一个电脑里边我们可能需要在Windows操作系统里边安装JDK 1.8以上的一个版本如果是Linux操作系统里边可以按照我们讲义里边提供的这个安装步骤来对它一步一步的安装先下载然后呢再使用RPM包来进行一个安装那么我们
[00:29] 注意的一点是需要设置一下Java HomeWindows操作系统里边也需要设置Java Home那么设置完了之后呢我们需要安装Jita Maven或者说IDEA Node.js这些是在Windows操作系统里边我们的开发环境里边需要用到的一些这个工具包那下面我们来看一看我们的Docker的一个安装因为我们的Redis也好还是Zookable Kafka都是在我们Docker容器里边运行的
[00:58] 而MySQL不是在容器里面运行的因为MySQL它涉及到数据的一个持久化而数据的持久化我们用的是直接在我们的Linux操作系统里面直接安装我们先看一看我们的Docker安装我们使用YAML来安装Docker我们输入yaml-y install Docker然后点回车它会下载Docker的安装镜像然后把安装镜像给安装上
[01:29] 那么稍等一下Docker的软件正在安装OK已经安装完了我们使用Docker PS查看一下Docker没有启动我们使用Service Docker start把Docker启动起来那我们再使用Docker PS但是呢我们已经证明Docker已经启动起来了用Docker安装我们的LOOKUP我们使用Docker Pro然后镜像的名字点回车
[02:01] 此时它会下载镜像的这个文件OKRooKeeper的镜像已经下载完了那么我们下一步下载卡普卡的镜像OK卡普卡镜像也下载下来了那我们从我们的Docker里面能够看到这两个镜像已经下载完毕那么下一步我们就把我们的RooKeeper给启动起来使用Docker run-d-nem-rooKeeper然后-p
[02:53] 2181冒号2181然后前面这个2181呢是我们的输入机的端口后边呢是我们的容器里边的2181端口那么杠T然后再加上我们Rocket Pro的镜像的名字然后点回车那此时我们使用这个Docker PS可以看到我们的Rocket Pro已经启动起来了那下一个的话我们就再把我们的卡布卡也给启动起来而这个卡布卡的启动端口是9092
[03:22] 我们点回车OK然后对我拷贝没拷贝全我们把重新拷贝一下然后大家需要注意的是在这里的Kafka连接的Zookip就是我们本地的Zookip 2181OK我们点击Docker PSKafka也启动起来了那下一步我们安装Redis安装Redis的过程也比较简单一些我们可以直接查询一下
[04:02] Docker search Redis然后呢我们可以看看Redis到底有哪些版本啊第一个版本就是官方的我们把Redis镜像给下载下来OK它下载下来之后呢我们直接Docker run

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 CentOS 系统上安装 Oracle JDK、Docker，并拉取并运行 Zookeeper、Kafka 和 Redis 的 Docker 镜像。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 内容：展示 PPT 页面，标题为“3.1.1 基础组件”，子标题“Oracle JDK 下载页面”，并给出下载链接。
- 代码：在终端中执行了 wget 下载 JDK RPM 文件、mv 移动文件、rpm -ivh 安装命令，以及 java -version 验证安装。
- 配置：提示设置 JAVA_HOME 环境变量。

画面 2：
- 内容：继续展示 PPT 页面，标题为“3.1.2 Docker”，并列出 Docker 要求的内核版本。
- 代码：在终端中执行了 yum -y install Docker 命令安装 Docker。
- 配置：提示设置 JAVA_HOME 环境变量。

画面 3：
- 内容：展示 PPT 页面，标题为“3.1.2 Docker”，并列出 Docker 要求的内核版本。
- 代码：在终端中执行了 yum -y install Docker 命令安装 Docker。
- 配置：提示设置 JAVA_HOME 环境变量。

画面 4：
- 内容：展示终端界面，显示 Docker 包的安装过程，包括下载、验证和安装。
- 代码：显示了安装的包列表和安装过程。

画面 5：
- 内容：展示终端界面，显示 Docker 安装完成后的信息，包括已安装的包和版本。
- 代码：显示了安装的包列表和安装过程。

画面 6：
- 内容：展示终端界面，显示 Docker 服务的启动命令。
- 代码：执行了 systemctl start Docker.Service 命令。

画面 7：
- 内容：展示终端界面，显示拉取 Zookeeper Docker 镜像的过程。
- 代码：执行了 Docker pull wurstmeister/ZooKeeper 命令。

画面 8：
- 内容：展示终端界面，显示拉取 Kafka Docker 镜像的过程。
- 代码：执行了 Docker pull wurstmeister/Kafka 命令。

画面 9：
- 内容：展示终端界面，显示拉取 Redis Docker 镜像的过程。
- 代码：执行了 Docker pull redis 命令。

画面 10：
- 内容：展示终端界面，显示运行 Zookeeper 容器的命令。
- 代码：执行了 Docker run -d --name ZooKeeper -p 2181:2181 wurstmeister/ZooKeeper 命令。

画面 11：
- 内容：展示终端界面，显示运行 Kafka 容器的命令。
- 代码：执行了 Docker run -d --name Kafka -p 9092:9092 -p 2181:2181 -e KAFKA_ZOOKEEPER_CONNECT=ZooKeeper:2181 -e KAFKA_ADVERTISED_PORT=9092 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://:9092 -e KAFKA_LISTENERS=PLAINTEXT://:9092 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_NUM_PARTITIONS=1 -e KAFKA_DEFAULT_REPLICATION_FACTOR=1 -e KAFKA_LOG_DIRS=/tmp/Kafka-logs -e KAFKA_BROKER_ID=0 -e KAFKA_AUTO_CREATE_TOPICS_ENABLE=true -e KAFKA_LOG_RETENTION_MS=604800000 -e KAFKA_LOG_RETENTION_BYTES=1073741824 -e KAFKA_LOG_RETENTION_CHECK_INTERVAL_MS=60000 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372036854775807 -e KAFKA_LOG_FLUSH_INTERVAL_MS=9223372

