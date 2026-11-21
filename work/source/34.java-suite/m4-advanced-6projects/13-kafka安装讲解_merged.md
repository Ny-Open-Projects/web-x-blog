# 13-kafka安装讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们来搭建我们的卡夫卡环境

我们直接在我们的服务器里面把卡夫卡给安装一下

然后去使用

那像卡夫卡的安装呢

它提供了多种安装方式

第一种是直接去使用它的软件

另外一个我们可以采用多颗容器的方式进行安装

好那咱这里呢就采用多颗容器的方式进行安装

不过它这里依赖咱们的主keeper

所以咱们得事先把主keeper给安装好

好我这里呢已经安装好了我们的一个主keeper

那主keeper的端口号是3181

并没有采用2181

这个安装这一块呢

这个命令就这么去拷贝一下执行一下就可以了

这里有一个目录挂载

这个主要是我们的一个时间同步

因为我们的容器里面的时间

不一定跟我们当前的一个宿主机

不一定跟我们当前的一个宿主机

时间同步

所以我们需要让他们的时间进行同步

好像主keeper这一块已经安装好了

所以我就不去安装了

我就直接去安装咱们的卡夫卡

那安装卡夫卡这一块呢

有这么一段命令

把它拷贝执行一下就可以了

首先我们说一下

它这一块相关的一些属性

像这个-P9092

这是咱们卡夫卡的一个端口号

这个呢

也是对外暴露的一个端口号

像这一块

这个其实就是咱们当前主keeper的一个IP以及端口号

还有一个是咱当前卡夫卡这一块

这块是咱当前卡夫卡对外暴露的一个IP以及端口号

那还有咱们卡夫卡各个服务之间协调怎么办呢

各个服务之间协调的话

它这个就是一个监听器的一个信息暴露

这一块各个服务之间进行一个协调通信

也是有这个IP和这个端口

那写上0.0.0的话

任何满足当前机器的IP都是可以的

好

后面这一块又是一个时间同步

我们就不说了

这个呢

就是咱们当前这一块的一个卡夫卡安装指令里面相关的属性介绍

接着我们就安装一次

看一下

来

拷贝一次

回车

回车

回车

回车

回车

那卡夫卡就安装成功

我们可以输入多克PS查看一下

这里就有咱们安装好的卡夫卡

好

卡夫卡安装好之后呢

我们要给他改一下相关的IP

那怎么改呢

先进入到我们卡夫卡

它里面有个configure

里面有个server.property

在这里面给他添加一个host.name

host.name呢

写当前宿主机的IP就可以了

多克

多克

多克

多克

多克

多克

多克

多克

多克

多克

多克

多克

多克

多克

多克

多克

多克

多克

这里呢有个opt目录在这一块

紧接着进入到它下面有一个卡夫卡目录

然后进入到configure里面去

去修改我们当前server.properties

修改怎么改呢

在最后面这里

我们添加一个属性host.name

这一块添加一个host.name

等于192.168.211.137

就可以了

紧接着我们保存

然后重启一下卡夫卡容器

那这个时候我们的卡夫卡安装就成功了

安装成功之后呢

紧接着我们就可以使用我们的卡夫卡了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于“热点数据实时收集”课程中“Kafka搭建”部分的教学内容。讲师通过演示在 Docker 环境中部署 Kafka 服务，详细讲解了其核心配置参数。主要内容包括：
- **环境准备**：首先安装 Zookeeper，作为 Kafka 的协调服务。
- **Kafka 安装**：使用 Docker 命令部署 Kafka 容器，并解释了关键环境变量（如 `KAFKA_BROKER_ID`、`KAFKA_ZOOKEEPER_CONNECT`、`KAFKA_LISTENERS`）的作用。
- **配置优化**：演示了如何修改 Kafka 的配置文件 `server.properties`，以设置主机名（`host.name`），便于外部程序连接。
- **操作演示**：进入 Kafka 容器内部，查看并编辑配置文件，以完成集群的初步搭建。

整个过程旨在为后续的实时数据处理和分析打下基础。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中的时间点，以下章节结构是根据画面内容和逻辑顺序推断的：

- **0:00 - 0:30**：课程导览与章节介绍。讲师展示 PPT，说明当前章节为“3.2.1 Kafka搭建”，并指出将采用 Docker 方式部署。
- **0:30 - 1:00**：Zookeeper 安装演示。讲师在终端中执行 `docker run` 命令，创建并启动 Zookeeper 容器，并解释了 `-v /etc/localtime:/etc/localtime` 参数的作用。
- **1:00 - 2:00**：Kafka 安装与配置讲解。讲师展示并解释了用于启动 Kafka 容器的完整 Docker 命令，详细说明了 `KAFKA_BROKER_ID`、`KAFKA_ZOOKEEPER_CONNECT`、`KAFKA_LISTENERS` 等环境变量的含义。
- **2:00 - 3:00**：IP地址配置与文件编辑。讲师演示如何进入 Kafka 容器，并在 `/opt/kafka_2.12-2.4.1/config/server.properties` 文件中添加 `host.name=192.168.211.137` 配置。
- **3:00 - 4:00**：配置文件内容展示。讲师在终端中查看并展示了 Kafka 配置文件 `server.properties` 的内容，包括 `listeners`、`num.network.threads`、`log.dirs`、`num.partitions`、`log.retention.hours` 等关键参数。
- **4:00 - 5:00**：章节小结与下一节预告。讲师总结了当前搭建的步骤，并预告了下一节将讲解“队列创建”。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 内容

- **章节标题**：`3.2.1 Kafka搭建`
- **核心说明**：单机版 Kafka 部署简单，但本课程采用 Docker 搭建 Kafka，且需先安装 Zookeeper。
- **Zookeeper 安装命令**：
  ```bash
  docker run -d --name zookeeper -p 3181:3181 -v /etc/localtime:/etc/localtime wurstmeister/zookeeper
  ```
- **Kafka 安装命令**：
  ```bash
  docker run -d --name kafka -p 9092:9092 -e KAFKA_BROKER_ID=0 -e KAFKA_ZOOKEEPER_CONNECT=192.168.211.137:3181/kafka -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.211.137:9092 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 -v /etc/localtime:/etc/localtime wurstmeister/kafka
  ```
- **配置说明**：
  - `KAFKA_BROKER_ID`：当前 Kafka 的唯一 ID。
  - `KAFKA_ZOOKEEPER_CONNECT`：当前 Kafka 使用的 Zookeeper 配置信息。
  - `KAFKA_ADVERTISED_LISTENERS`：对外发布（暴露）的监听器，对外发布监听端口、地址。
  - `KAFKA_LISTENERS`：监听器，告诉外部连接者要通过什么协议访问指定主机名和端口开放的 Kafka 服务。
- **IP地址配置**：
  - 在 `/opt/kafka_2.12-2.4.1/config/server.properties` 文件中添加：
    ```properties
    host.name=192.168.211.137
    ```

#### 代码与配置文件

- **Docker 命令**：
  ```bash
  docker run -d --name zookeeper -p 3181:3181 -v /etc/localtime:/etc/localtime wurstmeister/zookeeper
  ```
  ```bash
  docker run -d --name kafka -p 9092:9092 -e KAFKA_BROKER_ID=0 -e KAFKA_ZOOKEEPER_CONNECT=192.168.211.137:3181/kafka -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.211.137:9092 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 -v /etc/localtime:/etc/localtime wurstmeister/kafka
  ```

- **Kafka 配置文件 `server.properties`**：
  ```properties
  # Server Basics
  broker.id=0
  # Socket Settings
  listeners=PLAINTEXT://0.0.0.0:9092
  advertised.listeners=PLAINTEXT://192.168.211.137:9092
  # Log Basics
  log.dirs=/opt/kafka/kafka-logs
  num.partitions=1
  # Internal Topic Settings
  transaction.state.log.replication.factor=1
  transaction.state.log.min.isr=1
  # Log Flush Policy
  log.flush.interval.messages=10000
  log.flush.interval.ms=1000
  # Log Retention
  log.retention.hours=168
  log.retention.bytes=1073741824
  # Zookeeper connection string
  zookeeper.connect=192.168.211.137:3181
  ```

---

### 4) 关键场景与演示描述

- **场景一：Zookeeper 容器启动**
  - **描述**：讲师在终端中输入并执行了 `docker run` 命令，用于启动一个名为 `zookeeper` 的 Docker 容器。命令中包含了端口映射（`-p 3181:3181`）和卷挂载（`-v /etc/localtime:/etc/localtime`）。
  - **技术要点**：`-v /etc/localtime:/etc/localtime` 用于将宿主机的时区文件挂载到容器内，确保容器内部时间与宿主机同步，这对于分布式系统中的时间一致性至关重要。

- **场景二：Kafka 容器启动与参数解释**
  - **描述**：讲师展示了用于启动 Kafka 容器的完整 Docker 命令，并逐个解释了其中的关键环境变量。例如，`KAFKA_BROKER_ID=0` 表示这是集群中的第一个 Broker，`KAFKA_ZOOKEEPER_CONNECT=192.168.211.137:3181/kafka` 指定了 Zookeeper 的地址和端口。
  - **技术要点**：`KAFKA_ADVERTISED_LISTENERS` 是一个关键参数，它定义了 Kafka 服务对外暴露的地址和端口，是外部程序连接 Kafka 的依据。

- **场景三：配置文件编辑**
  - **描述**：讲师进入 Kafka 容器内部，通过 `docker exec -it kafka /bin/bash` 命令进入容器，并使用 `cd /opt/kafka_2.12-2.4.1/config/` 命令导航到配置目录。随后，讲师在 `server.properties` 文件中添加了 `host.name=192.168.211.137` 配置。
  - **技术要点**：`host.name` 配置用于指定 Kafka 服务的主机名，这在多节点集群或需要通过域名访问时非常重要。

- **场景四：配置文件内容展示**
  - **描述**：讲师在终端中使用 `cat server.properties` 命令查看了 Kafka 配置文件的内容，并逐行解释了关键
