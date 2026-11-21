# 14-kafka常用操作讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们讲解卡夫卡的常用操作

那常用操作这里呢

我们会带大家去学习

用卡夫卡对应的脚本

来创建我们对应的一些对列信息

紧接着我们会利用脚本

去实现我们卡夫卡指定的

对列数据的一个消息发送

接着我们会利用卡夫卡的脚本

去实现指定对列的一个

数据消费与订阅

好我们来讲解一下

卡夫卡对列的一个创建

那我们要想去操作卡夫卡

我们先进入到卡夫卡容器里面去

找到对应脚本的一个位置

Docker exec-it

卡夫卡

在这一块进入到opt里面

这里有一个卡夫卡第二个

它下面有一个闭幕录

我们进入到闭幕录去

这里有很多相关的脚本

这些脚本呢

我来简单介绍一下

如果你是要创建对列

用kafka-topics.sh就可以了

如果你是要向我们指定的对列

去发送我们的数据

也就是消息生产者

我们可以用kafka-consult-produce

如果你是去消费指定的对列数据

你可以用kafka-consult-consumer

好我们现在来讲解

这个对列的创建

所以我们用的是

kafka-topics.sh

那么这个对列的创建呢

语法我已经给大家写到这来了

我们直接拷贝执行一下就可以了

我们看一下这个语法里面相关的属性

它代表的意思

第一个-credit表示执行创建一个新对列

Postchart-server表示当前我要操作的卡夫卡的IP和框口

这个是表示我们这一块卡夫卡创建

一个对列之后

它这里的一个副本数量

最后这个topic是表示当前这一块创建的对列名称

我们把这一段代码给拷贝一下

然后执行一次对列名称呢

我们就写个looks-items

回车一次

这个时候对列就已经创建好了

对列创建好之后呢

我们可以向对列去发消息了

那发消息了

在下面这一块有相关的一个页面

一个说明

我们可以直接把上面这一段脚本给拷贝一下

去执行就行了

那这段脚本我们也讲解一下

它的一个相关的属性信息

第一个-broker list

其实就是我们当前卡夫卡的一个服务的IP和框口信息

topic呢

就是我要向哪个对列去发消息

那个对列的名称

我们来实现一次发消息

发消息呢

也就是消息生产

因此是用这个脚本去执行

好

我们把脚本拷过来

对列是刚才创建的这一个对列

执行会进入到它的命令行模式

命令行模式呢

我们就可以向对列去发数据了

数据这一块

我已经准备好了一段数据

我们直接拷贝一下

看一下效果

这个是我要向卡夫卡发数据的一个信息

回车一下就发过去了

好了

发过去了之后

我们紧接着就要实现我们这个消息的消费

那么消费呢

我们会用这一个卡夫卡空手孔数码来进行消费

消费这一块

我们开一个窗口

进入到容器里面去

进入到opt

卡夫卡下面有一个并目录

这一块用这个空手空手孔数码来消费

消费的语法呢

在这一块也有

我们拷贝过来

直接进入到容器里面去

我们拷贝过来直行

一次就可以了

那这里相关的属性

我们也进行一次讲解

像这一块有一个bootstrap-server

其实就是你要去哪个卡夫卡里面去消费数据

因此要指定它的IP和端口

topic呢

我要消费的对列是哪一个

from beginning就是从头开始消费

每一条数据都不会放过

好

我们把这一段脚本拷贝执行一次

看一下能否消费

我们

对应的一个对列的数据

这个对列的名称呢

我们要换一下

换成刚才我们创建的对列的名称

好

执行一次看效果

那么这个时候就会进入到我们后台进行消费了

那现在消费的数据也已经显示了

那这一块就是我们卡夫卡的一些常用操作

好

我们接着还看一下下面有一些别的语法

大家可以去自己熟悉一下

比如查看已经存在的主题

删除指定的主题

查看主题相关的一个信息

这里的主题也就是我们刚才说的对列

topic

接着我们去看一下主keeper里面

我们卡夫卡的一个注册信息

我们打开我们的主keeper

进入主keeper里面

有一个脚本叫

dkclientsh

我们用这个脚本就可以去查看我们卡夫卡的一个注册信息

以及其他的服务注册信息

好

我们进入到这里了

进入到主keeper

dockerexec-it

主keeper

并bast

这里有一个闭目录

闭目录下了有一个叫dkclient

好

我们输入一下服务地址localhost

我们是3181

紧接着我们回车一下

看一下效果

输入一下ls-

大家看下面会显示我们的一个注册信息

好

回车一下

那么这一块就有我们的卡夫卡

还有我们的别的一些信息

OK

这个就是我们当前这一块卡夫卡的一些常用操作

像创建对链

发布消息

消息消费

以及查看它在主keeper里面的一个注册信息

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于 Apache Kafka 的入门实操教程，主要演示了如何在 Docker 环境中创建 Kafka 队列（Topic）、向队列中发送消息、以及如何从队列中消费消息。课程内容围绕一个名为 `itemaccess` 的测试主题展开，旨在帮助学习者掌握 Kafka 的核心操作流程。视频通过 PPT 讲解和终端实操相结合的方式，逐步引导观众完成每个步骤，并在最后介绍了如何通过 ZooKeeper 查看 Kafka 的注册信息。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: **章节 3.2.2 队列创建**。讲师在 PPT 上展示创建 Kafka 队列的命令，并解释了 `--bootstrap-server`、`--replication-factor` 和 `--topic` 等关键参数。
*   **00:03 - 00:05**: **章节 3.2.3 消息发布**。讲师在 PPT 上展示发送消息的命令，并解释了 `--broker-list` 和 `--topic` 参数。
*   **00:05 - 00:07**: **章节 3.2.4 消息订阅**。讲师在 PPT 上展示消费消息的命令，并解释了 `--from-beginning` 参数。
*   **00:07 - 00:09**: **章节 3.2.5 信息查看**。讲师在 PPT 上展示如何使用 `kafka-topics.sh` 脚本查看主题列表和详情。
*   **00:09 - 00:11**: **章节 3.2.6 Kafka 注册信息查看**。讲师在 PPT 上展示如何通过 ZooKeeper 查看 Kafka 的注册信息，并演示了 `zkCli.sh` 命令。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

**PPT 内容**:
*   **章节标题**: `3.2.2 队列创建`, `3.2.3 消息发布`, `3.2.4 消息订阅`, `3.2.5 信息查看`, `3.2.6 Kafka 注册信息查看`。
*   **命令行解释**:
    *   `./kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic itemaccess`
    *   `./kafka-console-producer.sh --broker-list localhost:9092 --topic itemaccess`
    *   `./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic itemaccess --from-beginning`
    *   `./kafka-topics.sh --zookeeper localhost:3181 --list`
    *   `./kafka-topics.sh --zookeeper localhost:3181 --delete --topic itemaccess`
    *   `./kafka-topics.sh --zookeeper localhost:3181 --describe --topic itemaccess`
    *   `docker exec -it zookeeper /bin/bash`
    *   `cd bin`
    *   `./zkCli.sh`
    *   `ls /`
*   **参数解释**:
    *   `--bootstrap-server`: 指定 Kafka 服务的连接地址。
    *   `--replication-factor`: 设置分区的副本数量。
    *   `--partitions`: 设置分区数量。
    *   `--topic`: 指定要操作的队列名称。
    *   `--broker-list`: 指定 Kafka 服务的连接列表。
    *   `--from-beginning`: 从队列的最开始位置消费消息。
*   **ZooKeeper 命令**:
    *   `./zkCli.sh`
    *   `ls /`

**代码/命令**:
*   **创建队列**:
    ```bash
    docker exec -it kafka /bin/sh
    cd /opt/kafka_2.12-2.4.1/bin
    ./kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic itemaccess
    ```
*   **发送消息**:
    ```bash
    ./kafka-console-producer.sh --broker-list localhost:9092 --topic itemaccess
    ```
*   **消费消息**:
    ```bash
    ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic itemaccess --from-beginning
    ```
*   **查看主题**:
    ```bash
    ./kafka-topics.sh --zookeeper localhost:3181 --list
    ```
*   **删除主题**:
    ```bash
    ./kafka-topics.sh --zookeeper localhost:3181 --delete --topic itemaccess
    ```
*   **查看主题详情**:
    ```bash
    ./kafka-topics.sh --zookeeper localhost:3181 --describe --topic itemaccess
    ```
*   **查看 ZooKeeper 注册信息**:
    ```bash
    docker exec -it zookeeper /bin/bash
    cd bin
    ./zkCli.sh
    ls /
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 进入 Kafka 容器并创建队列**。
    *   讲师在终端中执行 `docker exec -it kafka /bin/bash` 命令进入 Kafka 容器。
    *   然后执行 `cd /opt/kafka_2.12-2.4.1/bin` 命令进入 Kafka 的 bin 目录。
    *   最后执行 `./kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic itemaccess` 命令创建名为 `itemaccess` 的队列。
*   **场景 2: 发送消息到队列**。
    *   讲师在终端中执行 `./kafka-console-producer.sh --broker-list localhost:9092 --topic itemaccess` 命令启动消息生产者。
    *   然后输入一条 JSON 格式的消息：`{"actime":"2020-4-10 9:50:10","url":"http://www.seck11.itheima.net/items/333.html","IP":"119.123.33.231","Token":"Bearer itcast"}`，并按回车发送。
*   **场景 3: 消费队列中的消息**。
    *   讲师在终端中执行 `./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic itemaccess --from-beginning` 命令启动消息消费者。
    *   消费者成功接收到之前发送的消息。
*   **场景 4: 查看 Kafka 主题信息**。
    *   讲师在终端中执行 `./kafka-topics.sh --zookeeper localhost:3181 --list` 命令查看所有主题。
    *   然后执行 `./kafka-topics.sh --zookeeper localhost:3181 --describe --topic itemaccess` 命令查看 `itemaccess` 主题的详细信息。
*   **场景 5: 查看 ZooKeeper 注册信息**。
    *   讲师在终端中执行 `docker exec -it zookeeper /bin/bash` 命令进入 ZooKeeper 容器。
    *   然后执行 `cd bin` 命令进入 bin 目录。
    *   最后执行 `./zkCli.sh` 命令启动 ZooKeeper 客户端，并执行 `ls /` 命令查看 Kafka 在 ZooKeeper 中的注册信息。

---
