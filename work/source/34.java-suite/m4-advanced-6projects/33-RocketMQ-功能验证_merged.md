# 33-RocketMQ-功能验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就对Locky的MQ功能进行一个测试验证

首先咱们在虚拟机当中去指定好它的环境变量

也就是要配置好NIMS5的地址

因为咱们接下来要通过它提供的工具脚本进行测试

咱们在终端去执行一个Support命令

将NIMS5变量加入到系统环境变量当中

接着咱们就去执行生产者来做一个测试

咱们要到Locky的运行目录下面

然后再执行刚才的脚本

通过刚才这个测试脚本

它已经生产了一批消息

Topic的名称是叫做Topic Test

咱们可以在Console 公众台看一下

在这里有一个Topic Test的主题

咱们可以看一下它的状态

最大的消息是54

也就是说

刚才这个脚本已经发生了54条消息

接着咱们再去通过消费者进行消费测试

这个仍然是采用Tools工具脚本

在这里它的参数是Consume一个消费者

咱们来测试验证一下结果

可以看到消费者已经拿到了对应的消息

并且将这些记录打印出来

咱们可以通过控制终端

看一下这个Topic主题

它的一个消费情况

在这里面我们可以看到

Block Offset以及Consume Offset

都已经将消息消费完成

消费进度已经是指向了最后一条消息

咱们回到讲义当中

这个结果的话

刚才也做了一个验证

也是通过这个工具脚本

进行消息的发送

还有消息的消费都能够正常进行处理

接下来咱们再看一下

Bulkit MQ相关的其他命令

这里我们可以看到

这里列出了一些咱们会经常使用到的命令

比如说可以查看基讯的情况

通过MQ Admin这个脚本去查看

因为咱们在这里是单个节点

所以的话就不能查看多个节点的信息

在B目的下面可以看到

它默认了展示出了咱们当前运行的单个节点的情况

它的IP以及它的一个端口版本情况

这个通过这个工具就给你了

将它完整的展示出来

下面是查看Bulkit的状态

仍然是通过MQ Admin的这个脚本

那咱们再去控制中端演示一下

它能够的将Bulkit的信息全部列出来

比如说Bulkit的版本信息

还有这个提交的一些日子情况记录

下面的一些message消息等等

再往下面就是topic的列表

咱们要知道MQ对MQ的信息是什么样的

在这个列表当中到底存在多少个topic

可以通过这个工具去查询

回到中端咱们执行一下

它会将咱们MQ当中所有的主题都列出来

刚才咱们创建了topic test

在这里就可以将它展示出来

然后咱们也可以查看topic的状态

比如说咱们想查看刚才所创建的topic test

它的预警情况

咱们在这里也可以执行一下

它会将它的消费进度全部展示出来

最大的一个消息的数量

max of set

最后一次消息发送更新时间

在这里都会有一个记录

然后还可以去查看topic的路由信息

我们也可以看一下

路由里面会将Blockit的连接信息打印出来

如果是有多个节点或者是一个集群的话

在这里面会显示多个Blockit的地址信息

好

在这里咱们就对Lockit的MQ

其他相关命令做了一个大致的介绍

最后有个FAQ

如果咱们在配置和运行过程当中

出现这样的错误提示

该怎么去处理呢

这个错误提示是说

发送了从事了三次

仍然是失败

它所耗费了一个时间

topic出现问题的主题名称

然后Blockit的运行情况

那么出现了问题的主题名称

出现这种情况

咱们要在配置文件当中去修改Blockit的对外连接IP

也就之前在安装配置的时候

咱们所讲到的它的配置属性Blockit

这个一定要配置它的对外能够访问的IP

修改完成配置文件之后

在启动MQBlockit的时候

要指定好它的配置文件路径

否则它可能找不到咱们刚才所修改的配置文件

即便你修改了其中的属性

它也不能正常生效

这一点大家要理解清楚

如果碰到这样的情况

要知道如何去排错和处理解决

好

这一讲就是对Blockit的MQ

整个功能做了一个测试验证

介绍了它相关的一些命令

以及一些常见的错误

那这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段为一个关于 Apache RocketMQ 消息中间件的实战教学课程。讲师通过演示如何在本地环境部署、配置并验证 RocketMQ 的基本功能，包括使用命令行工具进行消息的生产和消费，以及通过 Web 控制台查看消息的消费情况。视频内容主要集中在“验证”和“其他命令”两个部分，旨在帮助学习者掌握 RocketMQ 的核心操作和故障排查方法。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开始，讲师在 Typora 编辑器中展示课程大纲，当前页面为“3.7 验证”。
*   **00:00:05 - 00:00:15**: 讲师讲解如何通过命令行执行生产者和消费者测试，并在控制台中查看消息记录。
*   **00:00:15 - 00:00:25**: 讲师切换到终端窗口，执行 `sh bin/tools.sh org.apache.rocketmq.example.quickstart.Producer` 命令，成功发送消息。
*   **00:00:25 - 00:00:35**: 讲师执行 `sh bin/tools.sh org.apache.rocketmq.example.quickstart.Consumer` 命令，启动消费者。
*   **00:00:35 - 00:00:45**: 讲师切换到浏览器，打开 RocketMQ 控制台，展示 `TopicTest` 主题下消费组的消费记录，验证消息已成功消费。
*   **00:00:45 - 00:00:55**: 讲师切换回 Typora，进入“3.8 其他命令”章节，介绍如何使用 `mqadmin` 工具查看集群、Broker、Topic 等状态。
*   **00:00:55 - 00:01:05**: 讲师在终端执行 `./mqadmin clusterList -n 127.0.0.1:9876` 命令，查看集群信息。
*   **00:01:05 - 00:01:15**: 讲师执行 `./mqadmin brokerStatus -n 127.0.0.1:9876 -b 127.0.0.1:10911` 命令，查看 Broker 状态。
*   **00:01:15 - 00:01:25**: 讲师执行 `./mqadmin topicList -n 127.0.0.1:9876` 命令，查看 Topic 列表。
*   **00:01:25 - 00:01:35**: 讲师执行 `./mqadmin topicStatus -n 127.0.0.1:9876 -t TopicTest` 命令，查看特定 Topic 的状态。
*   **00:01:35 - 00:01:45**: 讲师执行 `./mqadmin topicRoute -n 127.0.0.1:9876 -t TopicTest` 命令，查看 Topic 的路由信息。
*   **00:01:45 - 00:01:55**: 讲师切换到“3.9 FAQ”章节，讲解如何解决消息发送失败的问题。
*   **00:01:55 - 00:02:05**: 讲师在 Typora 中展示错误信息 `Send [3] times, still failed, cost [575]ms, Topic: Name, BrokersSent: [broker-a, broker-a, broker-a]`，并解释其原因。
*   **00:02:05 - 00:02:15**: 讲师在 Typora 中展示解决方案：修改配置文件 `/usr/local/rocketmq_4.4/conf/broker.conf`，将 `brokerIP1` 设置为正确的对外 IP 地址。
*   **00:02:15 - 00:02:25**: 讲师展示如何通过命令行指定配置文件路径并启动 Broker 服务：`usr/local/rocketmq_4.4/bin/mqbroker -n 127.0.0.1:9876 -c /usr/local/rocketmq_4.4/conf/broker.conf`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **3.7 验证**: 包含设置 Name Server 地址的环境变量 `export NAMESRV_ADDR=localhost:9876`，以及执行生产者和消费者的命令。
    *   **3.8 其他命令**: 包含 `mqadmin` 工具的多个命令，如 `clusterList`, `brokerStatus`, `topicList`, `topicStatus`, `topicRoute`。
    *   **3.9 FAQ**: 包含一个常见的错误场景和解决方案，涉及修改 `broker.conf` 文件中的 `brokerIP1` 配置。

*   **代码/命令**:
    *   **环境变量设置**: `export NAMESRV_ADDR=localhost:9876`
    *   **生产者命令**: `sh bin/tools.sh org.apache.rocketmq.example.quickstart.Producer`
    *   **消费者命令**: `sh bin/tools.sh org.apache.rocketmq.example.quickstart.Consumer`
    *   **集群查看命令**: `./mqadmin clusterList -n 127.0.0.1:9876`
    *   **Broker 状态查看命令**: `./mqadmin brokerStatus -n 127.0.0.1:9876 -b 127.0.0.1:10911`
    *   **Topic 列表查看命令**: `./mqadmin topicList -n 127.0.0.1:9876`
    *   **Topic 状态查看命令**: `./mqadmin topicStatus -n 127.0.0.1:9876 -t TopicTest`
    *   **Topic 路由查看命令**: `./mqadmin topicRoute -n 127.0.0.1:9876 -t TopicTest`
    *   **启动 Broker 命令**: `usr/local/rocketmq_4.4/bin/mqbroker -n 127.0.0.1:9876 -c /usr/local/rocketmq_4.4/conf/broker.conf`

*   **图表/界面截图**:
    *   **RocketMQ 控制台界面**: 展示了 `TopicTest` 主题下消费组的详细信息，包括 Broker、Queue、消费客户端、消费偏移量等。
    *   **终端命令行界面**: 展示了执行 `mqadmin` 命令后的详细输出结果，包括集群信息、Broker 状态、Topic 列表等。

---

### 4) 关键场景与演示描述

*   **场景一：生产者与消费者测试** (00:00:15 - 00:00:35)
    *   讲师在终端中首先执行生产者命令，成功发送了多条消息。
    *   接着，讲师执行消费者命令，启动消费者程序。
    *   随后，讲师切换到浏览器中的 RocketMQ 控制台，成功在 `TopicTest` 主题下看到了消费记录，验证了消息的生产和消费流程。

*   **场景二：使用 mqadmin 工具进行集群管理** (00:00:45 - 00:01:35)
    *   讲师通过一系列 `mqadmin` 命令，演示了如何查看 RocketMQ 集群的详细信息。
    *   他首先使用 `clusterList` 查看集群状态，然后使用 `brokerStatus` 查看单个 Broker 的运行状态。
    *   接着，他使用 `topicList` 查看所有 Topic，使用 `topicStatus` 查看特定 Topic 的状态，最后使用 `topicRoute` 查看 Topic 的路由信息，全面展示了 RocketMQ 的管理能力。

*   **场景三：FAQ 故障排查** (00:01:45 - 00:02:15)
    *   讲师展示了当消息发送失败时，控制台会显示错误信息 `Send [3] times, still failed, cost [575]ms, Topic: Name, BrokersSent: [broker-a, broker-a, broker-a]`。
    *   讲师解释了错误原因：Broker 的对外 IP 地址配置不正确。
    *   他提供了解决方案：修改配置文件 `/usr/local/rocketmq_4.4/conf/broker.conf`，
