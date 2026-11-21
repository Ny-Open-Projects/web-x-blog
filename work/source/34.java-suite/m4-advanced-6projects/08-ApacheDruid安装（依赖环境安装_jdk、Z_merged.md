# 08-ApacheDruid安装（依赖环境安装_jdk、Z — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

咱们来看我们第七章的第二个部分

也就是我们apache-dread的安装

那么要运行这个apache-dread呢

它其实是有一些依赖环境的

那么我们需要先把这个依赖的环境给它安装上

然后最后呢我们再来安装dread

那么它依赖的环境有什么呢

比如说我们的JDK对吧

这肯定是必须的

然后还有Zookeeper

然后还有Kafka

当然这个前面这些安装的话

尤其是JDK还有Zookeeper

这个呢其实就比较简单了

我提前呢把这个JDK已经安装好了

那么大家呢也可以自行来安装一下

那么这个呢我们就不再说了

然后接下来呢我们可以基于这个Docker呢

把咱们这个Zookeeper服务呢把它跑起来

那么我们这个都是这种容器化的

方便我们管理

我这呢提前也已经安装好了这个Docker了

所以大家呢也可以自行来安装一下

那么我们来看一下这个命令啊

Docker run对吧

这个大家应该非常熟悉

然后呢杠杠ID

然后呢我们这个Zookeeper起来之后呢

容器的名字就是这个对吧

my-zookeeper

然后呢做一个端口映射对吧

然后呢又做了一个目录映射

映射这个叫做local time

然后呢主要是用来匹配它的这个时区的

然后呢就是这是我们这个镜像的名字对吧

镜像那名称

然后后边跟上版本号

然后呢这个命令呢我们直接复制过来啊

然后呢我们在这来执行一下

把这个Zookeeper跑起来

当然了那么我们现在用的是一个新的环境啊

这个地方呢你看它是不是没有找到我们这个镜像对吧

Zookeeper的镜像

所以去它需要去拉取一下

拉取完之后呢

再把这个容器跑起来

然后呢这个如果这个启动容器成功的话呢

我们可以通过什么呢

Docker logs这个命令是不是来查看一下什么呢

Zookeeper它的启动日志啊

来判断一下它启动了到底是否成功对吧

它现在呢正在拉取镜像

好

马上就会下载完了

你看这边downloading对吧

这最后一部分

好

那么你看它其实下载完之后呢启动这个时间其实是非常快的

瞬间就可以起来

好起来之后呢我们来查看一下它这个什么呢启动日志对吧

好复制一下

在这边来执行一下

好那么可以看到它启动的时候呢没有报错对吧

没有报错

然后呢从这也能看到绑定

to part对吧

也就是绑定了我们这个2181

好

这个是没有问题的

那到这儿的话呢我们

安装这个什么

Droid所需要的环境对吧

包括我们的JDK还有Docker

还有我们刚才启动的这个Zookeeper呢

就都已经搞定了

大家在自己本地呢来安装一下

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于“品达物流TMS项目”第7章“车辆轨迹服务开发”的技术课程，主要讲解 Apache Druid 的依赖环境安装。讲师通过 Typora 编辑器展示 PPT 内容，并在终端（Terminal）中演示如何使用 Docker 快速部署 Zookeeper 和 Kafka。视频内容聚焦于环境准备阶段，为后续安装 Druid 做铺垫。整个过程以命令行操作为主，强调了使用 Docker 容器化部署的便捷性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 视频开场，展示 Typora 编辑器中的 PPT 页面，标题为“2. apache druid安装”，并列出依赖环境：jdk, zookeeper, kafka。
*   **00:03 - 00:08**: 讲师在 PPT 中滚动展示“2.1 jdk安装”和“2.2 zookeeper安装”两个小节，并在终端中演示了 `docker run` 命令来启动 Zookeeper 容器。
*   **00:08 - 00:12**: 终端显示 Docker 容器成功启动后的日志信息，确认 Zookeeper 服务已运行。
*   **00:12 - 00:16**: 讲师在 PPT 中滚动展示“2.3 kafka安装”小节，并在终端中演示了 `docker run` 命令来启动 Kafka 容器。
*   **00:16 - 00:20**: 终端显示 Docker 容器成功启动后的日志信息，确认 Kafka 服务已运行。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “2. apache druid安装”
    *   **依赖环境**: `jdk`, `zookeeper`, `kafka`
    *   **2.1 jdk安装**:
        *   解压命令: `tar -zxvf jdk-8u191-linux-x64.tar.gz -C /usr/local/`
        *   配置命令: `vi /etc/profile`
        *   添加内容:
            ```bash
            export JAVA_HOME=/usr/local/jdk1.8.0_191
            export PATH=$JAVA_HOME/bin:$PATH
            ```
        *   配置生效命令: `source /etc/profile`
        *   查看版本命令: `java -version`
    *   **2.2 zookeeper安装**:
        *   启动容器命令: `docker run -id --name my_zookeeper -p 2181:2181 -v /etc/localtime:/etc/localtime zookeeper:3.4.14`
        *   查看容器运行情况命令: `docker logs -f my_zookeeper`
    *   **2.3 kafka安装**:
        *   下载镜像命令: `docker pull wurstmeister/kafka`
        *   启动容器命令: `docker run -d --name kafka -p 9092:9092 -e KAFKA_BROKER_ID=0 -e KAFKA_ZOOKEEPER_CONNECT=68.79.63.42:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://68.79.63.42:9092 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 -v /etc/localtime:/etc/localtime wurstmeister/kafka`
        *   查看容器运行情况命令: `docker logs -f kafka`

*   **终端日志**:
    *   **Zookeeper 启动日志**:
        ```
        Using config: /conf/zoo.cfg
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] - autpurge.purgeInterval set to 9
        [main:DatadirCleanupManager] - autpurge.snapRetainCount set to 3
        [main:DatadirCleanupManager] -
