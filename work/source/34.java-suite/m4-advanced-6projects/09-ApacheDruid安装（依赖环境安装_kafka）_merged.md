# 09-ApacheDruid安装（依赖环境安装_kafka） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才咱们这个Zookeeper容器已经跑起来了,对吧?

这个比较简单,我们就不再多说了

下一个就是卡夫卡的安装

这个卡夫卡它其实就是在大数据领域经常会用到的一个消息堆裂

可能大家以前没有使用过,但是大家应该用过其他的一些MQ产品

比如说什么ActiveMQ,或者RabbitMQ,或者是阿里的RocketMQ等等

那么它们其实都是比较类似的,就是同类的一些产品

只不过卡夫卡它是应用在大数据领域是比较多的

因为什么呢?因为它的吞吐量相对来说是非常非常大的

所以在大数据领域应用比较多

那么我们这个地方咱们就直接来安装一下就可以了

安装完之后我们可以来简单测试一下

比如说我们创建一个堆裂,对吧?

然后我们在向堆裂当中来发送一条消息

然后再通过我们的消费端来消费这条消息

其实跟我们以前学习的消息堆裂都是比较多的

类似的

那么首先我们可以先使用Docker这种方式先来拉取一下镜像

但是这个地方其实你不拉取镜像,直接启动容器也没有问题

那么如果没有镜像它是不是自己会去拉取,对吧?

你看我们前面这个组Keeper其实就是这样的

这儿的话我们也可以显示的先给它拉取一下

这个其实都无所谓

然后我们可以在这儿来执行一下

当然现在我们需要来退出一下

刚才咱们是在这个日志里边,对吧?

好,Ctrl C,退出来

来执行Docker Pro

这是不是拉取镜像,对吧?

好

因为我们在这个地方没有去指定版本号,对吧?

所以说它就会拉取目前来说最新的一个版本

你看这边Lusty的,对吧?

一般的这个镜像的话其实都是比较大的

基本上都是几百兆

甚至有可能会更大

所以你可以看到它这个拉取的时间也是比较长的

那么咱们先不管这边

然后我们来看一下

拉取完镜像之后

我们就需要来启动什么呢?

启动我们的这个卡布卡

它的这个容器,对吧?

那么也是使用Docker run命令

然后杠

但是这个i的话加不加都可以啊

杠ID

然后呢

杠杠Name,对吧?

来指定我们这个容器的名称就叫卡布卡

然后呢

做了一个什么呢

端口映射,对吧?

那么它提供服务呢

我们一般都访问这个9092

这是它默认端口号

然后来指定了这么一个参数,对吧?

Broker ID

那么这个地方就等于0就可以了

其实只要保证它是唯一的就可以

然后呢

这个地方呢

我们这个卡布卡的话呢

是需要干什么呢

连接我们的组keeper的

连接组keeper

使用组keeper作为我们这个服务协调,对吧?

服务协调的一个中心

所以需要连接上我们的组keeper

但是这个地方呢

大家需要注意啊

这是我们当时写讲义的时候用它一台服务器,对吧?

但是这个呢

它不是固定的

所以说呢

你需要把这个地方呢

改成我们当前这台服务器它的IP

你看我当前服务器的IP是什么呢?

是399934.207,对吧?

因为我们刚才这个组keeper就安装在这台服务器上了

所以说呢

这个地方是需要进行相应的修改的

也就是说这种IP的地方都需要来改

然后呢

这是设置什么呢

设置它的一个

你看监听器,对吧?

它的地址

所以这个IP也是需要来改的

包括这个listeners,对吧?

这都是一些监听

然后呢

做了一个目录映射local time

也是local time

然后呢

这个是指定我们这个镜像的名字,对吧?

那现在的话

我们这个镜像呢

其实已经拉取下来了

咱们可以来看一下我本地的镜像

你看现在呢

我们是不是除了刚才那个组keeper

对吧

它启动容器的时候会下来

然后呢

我们刚才又手动的把这个镜像给拉取下来了

400多兆,对吧?

好

那么接下来呢

我们就把这个命令啊

注意不要直接敲回车

咱们最好给它编辑一下

把那个IP的地址地址的地方了

给它改一下

然后呢

我们在这来给它修改一下

把这个IP对吧

给它整体来替换一下吧

整体来替换一下

查找

然后替换

替换成什么呢

我们刚才看到啊

应该是399934.207

3999

多少是34

34.207

然后呢

我们来替换一个

再来替换

应该是

已经替换完了

对吧

然后呢

我们把这个命令啊

给它复制过来

Ctrl C

复制过来

然后呢

在这来执行一下

好

先来检查一下啊

你看Docker Run

对吧

刚刚ID

然后呢

刚刚Name

这个容器的名字叫卡不卡

然后呢

做了一个端口映射

对吧

然后后边呢

是启动的时候指定了一些常量

对吧

然后呢

这个也是非常重要的

就是需要连接我们的卡不卡

连接这个Zookeeper

然后后边的是一些常量定义

然后呢

又做了一个这个岗位

对吧

目录映射

好

最后呢

指定这个什么呢

镜像

然后呢

我们回车

好

那么现在呢

这个服务呢

已经跑起来了

那到底启动成功没成功呢

还是来查看一下什么呢

查看一下我们这个运行的日志

对吧

好

来看看啊

走

那么我们可以看到

它启动的这个日志呢

是没有报错

对吧

没有报错

好

然后呢

从这儿也能看到啊

它是不是这个

注册了一个broker

对吧

broker

然后呢

地址呢

就是这个地址啊

没有问题

好

那到这儿的话呢

咱们这个卡不卡呢

其实就已经安装完了

安装完之后呢

一会儿呢

我们可以来简单测试一下它

就是什么呢

创建队列

对吧

发送消息

监听消息

看看了这些能不能正常工作

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于“品达物流TMS项目”第7章“车辆轨迹服务开发”的技术课程，主要演示了如何使用 Docker 在 Linux 环境下部署 Apache Kafka 服务。课程内容以 PPT 文档为引导，详细讲解了 Kafka 安装的前置条件（即依赖服务 Zookeeper 的安装），并重点演示了 Kafka 容器的拉取、启动、参数配置及运行状态验证。视频通过终端命令行和 PPT 文档的结合，清晰地展示了整个部署流程，旨在帮助学习者掌握在实际项目中使用 Docker 部署 Kafka 的方法。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开始，展示 PPT 文档的目录结构，当前聚焦于“2.3 kafka安装”章节。
*   **00:00:05 - 00:00:15**: 展示 Kafka 安装的 PPT 内容，包括“下载安装”、“参数说明”和“验证”三个部分。
*   **00:00:15 - 00:00:25**: 切换到终端，演示执行 `docker pull wurstmeister/kafka` 命令，拉取 Kafka 镜像。
*   **00:00:25 - 00:00:35**: 展示拉取镜像后的终端输出，确认镜像已成功下载。
*   **00:00:35 - 00:00:45**: 回到 PPT，讲解 Kafka 启动命令中的关键参数，如 `KAFKA_ZOOKEEPER_CONNECT` 和 `KAFKA_LISTENERS`。
*   **00:00:45 - 00:00:55**: 在终端中执行 `docker run -d --name kafka -p 9092:9092 ...` 命令，启动 Kafka 容器。
*   **00:00:55 - 00:01:05**: 展示 Kafka 容器启动后的终端日志，确认服务已成功启动。
*   **00:01:05 - 00:01:15**: 回到 PPT，讲解如何通过 `docker logs -f kafka` 命令实时查看容器运行日志。
*   **00:01:15 - 00:01:25**: 展示 Kafka 启动后的完整日志，包括 Broker 注册、Zookeeper 交互等关键信息。
*   **00:01:25 - 00:01:35**: 视频结束，总结 Kafka 安装成功。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 文档内容**:
    *   **章节标题**: `2.3 kafka安装`
    *   **子标题**: `下载安装`, `参数说明`, `验证`
    *   **关键命令**:
        *   `docker pull wurstmeister/kafka`
        *   `docker run -d --name kafka -p 9092:9092 -e KAFKA_BROKER_ID=0 -e KAFKA_ZOOKEEPER_CONNECT=68.79.63.42:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://68.79.63.42:9092 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 -v /etc/localtime:/etc/localtime wurstmeister/kafka`
        *   `docker logs -f kafka`
    *   **参数说明**:
        *   `-e KAFKA_BROKER_ID=0`: 在 Kafka 集群中，每个 Kafka 都有一个 `BROKER_ID` 来区分自己。
        *   `-e KAFKA_ZOOKEEPER_CONNECT=68.79.63.42:2181`: 配置 Zookeeper 管理 Kafka 的路径。
        *   `-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://68.79.63.42:9092`: 把 Kafka 的地址端口注册给 Zookeeper。
        *   `-e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092`: 配置 Kafka 的监听端口。
        *   `-v /etc/localtime:/etc/localtime`: 容器时间同步宿主机的时间。

*   **终端命令与日志**:
    *   `docker pull wurstmeister/kafka`
    *   `docker run -d --name kafka -p 9092:9092 ...`
    *   `docker logs -f kafka`
    *   **Kafka 启动日志**:
        *   `Starting server`
        *   `Server environment: zookeeper.version=3.4.14`
        *   `Server environment: java.version=1.8.0_205`
        *   `Server environment: java.home=/usr/lib/jvm/java-8-oracle`
        *   `Server environment: java.library.path=/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib64:/usr/lib:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/jvm/java-8-oracle/jre/lib/amd64:/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server:/usr/lib/j
