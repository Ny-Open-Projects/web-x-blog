# 30-RocketMQ-安装与配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就来对LockitMQ进行一个安装配置

首先咱们去下载LockitMQ的安装包

还有它的控制台

下载地址在这里也已经提供出来

如果是以上地址不能连接

咱们可以采用其他的镜像

这个是腾讯云的一个镜像源

大家也可以从咱们所提供的资料当中

去获取LockitMQ的安装包

注意它的版本是4.4.0

接着咱们就来执行它的安装和配置

我们仍然采用10.10.20.251这台机器

在这里我们已经将LockitMQ

它的安装包上传到服务器当中

首先咱们去解压安装包-QO

并没有识别onjave命令

因为这个是一个新的虚拟机

咱们去安装对应的解压命令

onjave

安装完成之后

重新执行刚才的指令

执行完成

咱们进入LockitMQ的安装包

解压完成之后

它是可以直接运行的

在B目录下面

它提供了对应的脚本

咱们可以看一下

通过Long Server脚本

就能够运行LockitMQ服务

在运行之前

咱们要确保JDK环境是已经配置成功

咱们查看一下

当前虚拟机的JDK版本

这个并不能识别

咱们重新去读取它的环境变量

再次去查看一下

可以看到JDK版本是1.8.0-181的一个版本

建议大家要采用1.8以上的版本

接下来咱们要去修改它的配置

因为在虚拟机当中去运行

默认会占用4G的内存

这个比较浪费资源

作为学习和测试

我们可以修改并减少它的内存占用

怎么去修改呢

咱们只需要去修改它的启动脚本

首先咱们去修改Long Server的脚本

这个路径不对

因为咱们是在并目的下面返回上一层

重新执行

那咱们要去修改它的加瓦参数

将这一行copy

找到加瓦欧元

可以看到

这一行就是对加瓦运行内存的设置

那咱们将这一行先注释掉

然后将它copy进来

接着咱们保存wq小写的

接下来咱们还去修改Long Block的启动脚本配置

同样咱们也去修改加瓦的运行参数

咱们copy一下

将它内存指定为最大为1G的内存占用

因为咱们是做一个教学演示

实际的消息量并没有那么大

所以咱们可以将内存调小一点

粘贴进去

wq保存

最后还有一个脚本

这个是它的一个运行工具的脚本

咱们也将它修改一下

如果是咱们在本机上面

通过它的工具脚本去进行消息的生产和消费

那么我们就要去修改这个Tools.sh

ssh

的脚本配置

将这个加瓦的参数也做一个调整

先注释

然后粘贴上去

好保存

这样咱们就完成了启动参数的配置

接下来咱们还去修改它的服务端的配置

服务端配置咱们主要去修改Nameserver的地址

以及Block的地址

因为咱们是单个节点

所以集群信息这一块

暂时不用去做调整

下面是它的一些运行参数

比如说消息的删除策略

ACL的权限控制策略等等

咱们就来做相应的修改

大家要注意一下

LockitMQ的启动是包括两部分

一部分是Nameserver

另外一部分是Block

之前咱们讲解LockitMQ物理架构的时候

也做了介绍

在这里面有Nameserver

还有Producer

Block以及Consumer

我们从服务端要启动Nameserver以及Block

好

咱们回到刚才的配置

我们首先去编辑LockitMQ的服务端配置文件

注意一下它的路径

咱们的路径是LockitMQ-OR

跟讲义当中的路径是不一样的

这一点要注意一下

那么咱们就采用相对路径做一个修改

Configure

咱们就来添加一下它的配置

首先是Nameserver的地址

这个是采用咱们当前虚拟器的IP

10.10.20.251

然后是Block

它的IP因为现在是单个节点

所以只需要配置一个节点就可以了

251

最后咱们再配置一个ACL的控制

因为在这里咱们主要是学习LockitMQ的安装

所以权限控制这一块咱们是暂时不需要

好保存

这样咱们就完成了LockitMQ服务端的配置

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于 **RocketMQ 4.4.0 版本的安装与配置教程**。讲师通过演示在 Linux 虚拟机环境中，从下载压缩包、解压、安装依赖工具、修改服务启动脚本的 JVM 参数、配置 Broker 服务文件，到最终启动 Name Server 服务的完整流程。视频内容聚焦于开发和测试环境的搭建，旨在帮助学习者掌握 RocketMQ 的基础部署方法。讲师特别强调了在虚拟机中调整内存配置的重要性，以避免资源浪费。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: **课程引言与目录概览**。讲师在 Typora 文档中展示了课程大纲，当前章节为“3. 实现”，并重点介绍了“3.3 安装配置”。
*   **00:15 - 00:30**: **下载与解压**。讲师在终端中演示了如何下载 RocketMQ 4.4.0 的压缩包，并在本地解压。
*   **00:30 - 00:45**: **安装依赖工具**。由于系统缺少 `unzip` 工具，讲师通过 `yum install unzip` 命令进行安装。
*   **00:45 - 01:00**: **修改服务启动脚本**。讲师在 Typora 文档中展示了需要修改的三个脚本文件：`runserver.sh`、`runbroker.sh` 和 `tools.sh`，并给出了修改后的 JVM 参数配置。
*   **01:00 - 01:15**: **配置 Broker 服务文件**。讲师在 Typora 文档中展示了 `broker.conf` 的配置示例，包括 `namesrvAddr`、`brokerIP1`、`brokerName`、`brokerId`、`brokerRole` 等关键参数。
*   **01:15 - 01:30**: **启动服务**。讲师在终端中演示了如何启动 Name Server 服务，命令为 `nohup /usr/local/rocketmq_4.4/bin/mqnamesrv > /dev/null 2>&1 &`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “3.3 安装配置”。
    *   **下载链接**: `https://mirrors.cloud.tencent.com/apache/rocketmq/4.4.0/rocketmq-all-4.4.0-bin-release.zip`。
    *   **配置文件路径**: `/usr/local/rocketmq_4.4/conf/broker.conf`。
    *   **服务启动命令**: `nohup /usr/local/rocketmq_4.4/bin/mqnamesrv > /dev/null 2>&1 &`。

*   **代码 / 配置文件内容**:
    *   **解压命令**: `unzip -qo rocketmq-all-4.4.0-bin-release.zip`。
    *   **安装 unzip 工具**: `yum install unzip`。
    *   **修改 `runserver.sh` 的 JVM 参数**:
        ```bash
        JAVA_OPT="$JAVA_OPT" -server -Xms256m -Xmx1024m -Xmn1024m -XX:MetaspaceSize=64m -XX:MaxMetaspaceSize=160m
        ```
    *   **修改 `runbroker.sh` 的 JVM 参数**:
        ```bash
        JAVA_OPT="$JAVA_OPT" -server -Xms256m -Xmx1024m -Xmn1024m
        ```
    *   **修改 `tools.sh` 的 JVM 参数**:
        ```bash
        JAVA_OPT="$JAVA_OPT" -server -Xms256m -Xmx512m -Xmn256m -XX:PermSize=128m -XX:MaxPermSize=128m
        ```
    *   **`broker.conf` 配置示例**:
        ```properties
        namesrvAddr=10.10.20.10:9876
        brokerIP1=10.10.20.10
        brokerClusterName = DefaultCluster
        brokerName = broker-a
        brokerId = 0
        deletewhen = 04
        fileReservedTime = 48
        brokerRole = ASYNC_MASTER
        flushDiskType = ASYNC_FLUSH
        aclEnable=false
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境准备与下载**。
    *   讲师在 Typora 文档中指出，RocketMQ 的 Broker 作为消息中转角色，负责存储和转发消息。
    *   他展示了下载链接，并在终端中执行 `rz` 命令进行文件传输，随后使用 `unzip` 命令解压文件。

*   **场景二：安装依赖与解压**。
    *   讲师在终端中发现 `unzip` 命令不存在，于是使用 `yum install unzip` 命令进行安装。
    *   安装完成后，他再次执行 `unzip -qo rocketmq-all-4.4.0-bin-release.zip` 命令进行解压。

*   **场景三：修改服务脚本**。
    *   讲师在 Typora 文档中详细讲解了需要修改的三个脚本文件，并给出了修改后的 JVM 参数配置。
    *   他特别强调了在虚拟机中修改内存参数的重要性，以避免资源浪费。

*   **场景四：配置 Broker 服务文件**。
    *   讲师在 Typora 文档中展示了 `broker.conf` 的配置示例，并解释了各个参数的含义。
    *   他特别指出了 `brokerRole` 和 `flushDiskType` 等关键参数。

*   **场景五：启动服务**。
    *   讲师在终端中执行 `nohup /usr/local/rocketmq_4.4/bin/mqnamesrv > /dev/null 2>&1 &` 命令，启动 Name Server 服务。
    *   他通过 `ps -ef | grep mqnamesrv` 命令验证服务是否成功启动。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解课程内容。
