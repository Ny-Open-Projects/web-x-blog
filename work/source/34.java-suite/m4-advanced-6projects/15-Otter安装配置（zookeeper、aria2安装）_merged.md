# 15-Otter安装配置（zookeeper、aria2安装） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么前面关于alt安装配置当中这个3.2这个小节,也就是mycircle安装,我们都已经安装好了。

那么一共咱们是安装了三个数据库,分别是我们的原数据库,还有目标数据库,还有就是alt所使用到的一个配置数据库。

那么一共是这么三个库,并且我们通过远程也都已经连上来了。

大家能看到,咱们这三个库都已经创建好了。

那接下来我们再往下看就是我们的zookeeper安装。

因为咱们来看整个alt它的架构,这里边我们可以看到它需要使用到zookeeper来进行分布式协调。

所以说需要安装zookeeper。

这个zookeeper我们安装在哪台服务器上其实都可以。

你看我这这个zookeeper在讲义上我们分成了这么两个,一个是单机版的,还有一个是集群版的。

咱们现在就安装一个单机版的就可以。

集群版的话,

我们可以安装一个单机版的,

我们可以安装一个单机版的,

我们可以安装一个单机版的,

我们可以安装一个单机版的,

大家可以按照讲义自己来操作一下。

那么我们课上的话就直接安装这个单机版,相对来说会简单一点。

咱们就安装在我们第三台服务器,装在这就可以了。

实际上你安装在哪台机器上都可以。

那么我们直接通过docker这种方式来安装一下。

然后做了一个端口映射,叫做2181。

然后容器的名字叫做mygon.

然后容器的名字叫做mygon.

然后我们就把这个端口映射,叫做zoocouper。

好,咱们直接来执行这个docker run命令。

还是它需要去拉取一下这个zoocouper的镜像,对吧?

然后拉取完之后就会启动我们这个容器。

稍微等待一下。

好,那么咱们现在这个zoocouper已经跑起来了。

然后我们可以通过docker ps来看一下。

你看我们现在这个zoocouper已经跑起来了。好。

然后我们就把这个zoocouper给它们安装一下。好。

然后我们就把这个zoocouper给它们安装一下。好。

如果想看它的运行日志,可以通过这个docker logs,然后来看它这个日志。

如果想看它的运行日志,可以通过这个docker logs,然后来看它这个日志。

簡單看一下就行。

好,你看,这是它的启动日志。

它已经启动完了。没有问题。

好,这是关于我们这个docker的安装,关于这个zoocouper的安装。

好,这是关于我们这个docker的安装,关于这个zoocouper的安装。

然后下边还有一个,就是这个。

这个的话它是一个多线程下载工具。

咱们这个altr需要它的支持,

咱们这个altr需要它的支持,

所以我们也把这个来安装一下。

我们也把这个来安装一下

这个也是非常简单

直接通过YAML命令来安装它就可以

然后到这边来

那么我们退出一下它这个日志

然后直接来

那么这个是一个比较小的工具

因为我们后边Ultra会使用到它

所以我们把它安装上就可以了

这是关于咱们组Keeper

还有第二个Area这个安装

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于“数据聚合服务开发”课程的第6章，主要讲解如何安装和配置 **Otter** 数据库同步工具。课程内容从环境准备开始，依次介绍了 **MySQL** 数据库的创建、**ZooKeeper** 集群的 Docker 安装、**aria2** 多线程下载工具的安装，以及 **Otter Manager** 服务的部署和配置。视频通过屏幕录制的方式，展示了在 Linux 终端中执行命令、查看日志和配置文件的全过程，旨在为学员提供一个完整的、可操作的安装指南。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:15**: 课程引言，介绍本章将学习如何安装 Otter 数据库同步工具。
*   **00:00:15 - 00:00:30**: 展示 Otter 的数据库结构图，介绍其核心表（如 `USER`, `PIPELINE`, `LOG_RECORD`）。
*   **00:00:30 - 00:00:45**: 展示课程配套的 Markdown 文档，明确本章的安装步骤。
*   **00:00:45 - 00:01:00**: 开始安装 **ZooKeeper**，在终端中执行 `docker run` 命令启动单机版。
*   **00:01:00 - 00:01:15**: 查看 Docker 容器状态，确认 ZooKeeper 服务已成功启动。
*   **00:01:15 - 00:01:30**: 介绍并演示如何使用 `docker logs` 命令查看容器日志。
*   **00:01:30 - 00:01:45**: 介绍 **aria2** 工具，展示其安装命令 `yum -y install epel-release aria2`。
*   **00:01:45 - 00:02:00**: 展示 **Otter Manager** 的安装步骤，包括下载、解压和配置文件修改。
*   **00:02:00 - 00:02:15**: 课程结束，预告下一节内容。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：明确列出了本章的安装步骤，包括 MySQL、ZooKeeper、aria2 和 Otter Manager。
    *   Otter 数据库结构图：展示了 Otter 的核心表及其字段，如 `USER` 表包含 `USERNAME`, `PASSWORD` 等字段，`LOG_RECORD` 表包含 `LOG_ID`, `PIPELINE_ID` 等字段。
    *   **ZooKeeper 安装命令**:
        *   单机版启动命令：`docker run -d --name my_zookeeper -p 2181:2181 zookeeper:3.4.14`
        *   查看容器日志命令：`docker logs -f my_zookeeper`
        *   客户端连接命令：`docker run -it --rm --link my_zookeeper:zk zookeeper:3.4.14 zkCli.sh -server zk`
    *   **aria2 安装命令**: `yum -y install epel-release aria2`
    *   **Otter Manager 安装命令**:
        *   下载文件：`wget https://github.com/alibaba/otter/releases/download/otter-4.2.18/manager.deployer-4.2.18.tar.gz`
        *   解压文件：`tar -zxvf manager.deployer-4.2.18.tar.gz -C manager`
        *   配置文件路径：`/opt/otter/manager/conf/otter.properties`

*   **图表**:
    *   **Otter 数据库结构图**：一个清晰的图示，展示了 Otter 数据库中各个表之间的关系和字段结构。

---

### 4) 关键场景与演示描述

*   **场景 1: 数据库结构展示 (00:00:15)**
    *   **描述**: 视频首先展示了一个数据库设计图，图中包含了 Otter 的多个核心表，如 `USER`, `PIPELINE`, `LOG_RECORD`, `TABLE_STAT` 等。每个表都列出了其主要字段，如 `USER` 表包含 `USERNAME`, `PASSWORD`, `DEPARTMENT` 等字段，`LOG_RECORD` 表包含 `LOG_ID`, `PIPELINE_ID`, `START_TIME` 等字段。这为后续的安装和配置提供了数据层面的背景。

*   **场景 2: ZooKeeper 单机版安装 (00:00:45 - 00:01:15)**
    *   **描述**: 讲师在终端中执行 `docker run -d --name my_zookeeper -p 2181:2181 zookeeper:3.4.14` 命令，启动一个单机版的 ZooKeeper 服务。随后，通过 `docker ps` 命令查看容器状态，确认服务已成功启动并运行在 `0.0.0.0:2181` 端口上。

*   **场景 3: 查看 ZooKeeper 日志 (00:01:15)**
    *   **描述**: 讲师执行 `docker logs -f my_zookeeper` 命令，实时查看 ZooKeeper 容器的启动日志。日志中显示了服务器环境、Java 版本、配置文件路径等信息，确认服务已正常启动。

*   **场景 4: aria2 安装 (00:01:30)**
    *   **描述**: 讲师在终端中执行 `yum -y install epel-release aria2` 命令，安装 aria2 多线程下载工具。这是为了支持 Otter 在下载配置文件时的多线程加速。

*   **场景 5: Otter Manager 安装 (00:01:45)**
    *   **描述**: 讲师在终端中执行 `wget` 命令下载 Otter Manager 的部署包，然后使用 `tar -zxvf` 命令解压文件。接着，通过 `vim` 命令打开配置文件 `/opt/otter/manager/conf/otter.properties`，并修改其中的 MySQL 和 ZooKeeper 连接信息，为后续的配置做准备。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解课程内容。
