# 画面线理解：10-flume案例-flume级联-组件分析

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\10-flume案例-flume级联-组件分析【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 00:57, 01:43, 02:59, 05:01, 05:06, 05:13, 05:24, 06:48, 06:51, 06:57, 07:00, 07:33, 08:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 07:50:35

1) 这一组画面整体在讲 Apache Flume 的架构、组件配置方法及多节点数据传输流程。

2) 按时间顺序列出每张画面的要点：
画面1:
要点：展示 Flume Agent 的核心组件（Source、Channel、Sink）及其数据流向（Source → Channel → Sink → HDFS），并列出配置步骤：1) 写配置文件；2) 配置 Source；3) 配置 Channel；4) 配置 Sink；5) 组合组件；6) 启动 Agent；7) 运行测试。
代码：
agent1.sources = sourcel
agent1.sinks = sinkl
agent1.channels = channel1
agent1.sources.sourcel.type = exec
agent1.sources.sourcel.command = tail -F /export/servers
agent1.channels.channel1.type = memory
agent1.channels.channel1.keep-alive = 120
agent1.channels.channel1.capacity = 500000
agent1.channels.channel1.transactionCapacity = 600
agent1.sinks.sink1.hdfs.path = /%Y/%m/%d
agent1.sinks.sink1.hdfs.filePrefix = logs
agent1.sinks.sink1.hdfs.maxOpenFiles = 4
agent1.sinks.sink1.hdfs.batchSize = 100
agent1.sinks.sink1.hdfs.fileType = DataStream

画面2:
要点：展示一个 Flume Agent 的基本数据流结构图（Source → Channel → Sink）。

画面3:
要点：展示一个 Flume Agent 的基本数据流结构图（Source → Channel → Sink）。

画面4:
要点：在画面2的基础上，右侧新增一个 Agent，形成两个 Agent 的数据流连接，左侧 Agent 的 Sink 指向右侧 Agent 的 Source。

画面5:
要点：展示 Apache Flume 1.8.0 用户指南的首页，介绍 Flume 是一个用于高效收集、聚合和移动大量日志数据的分布式、可靠、可用系统。

画面6:
要点：展示 Flume 架构的“Data flow model”图，图中“Web Server”指向“Source”，“Source”指向“Channel”，“Channel”指向“Sink”，“Sink”指向“HDFS”。同时，左侧导航栏显示“Configuring individual components”和“Wiring the pieces together”等配置章节。

画面7:
要点：展示如何启动 Flume Agent，命令为：`$ bin/flume-ng agent --name a1 --conf conf --conf-file conf/flume-conf.properties.template`。

画面8:
要点：展示 Avro Sink 的配置属性表，包括 channel、type、hostname、port、batch-size、connect.timeout、request.timeout、reset.connection.interval、compression-type、compression.level 等属性及其默认值和描述。

画面9:
要点：展示 Avro Sink 的配置属性表，内容与画面8相同。

画面10:
要点：展示 Legacy Source 的配置属性表，包括 channels、type、host、port、selector.*、interceptors.* 等属性及其默认值和描述。

画面11:
要点：展示 Flume 的“Complex flows”和“Reliability”部分，说明 Flume 支持多跳数据流、故障转移等特性。

画面12:
要点：展示 Flume 架构的“Data flow model”图，图中“Web Server”指向“Source”，“Source”指向“Channel”，“Channel”指向“Sink”，“Sink”指向“HDFS”。同时，左侧导航栏显示“Configuring individual components”和“Wiring the pieces together”等配置章节。

画面13:
要点：展示 Avro Source 的配置属性表，包括 channels、type、bind、port、threads、selector.*、interceptors.*、compression-type、compression.level、keystore、keystore.password 等属性及其默认值和描述。

画面14:
要点：展示两个节点（node02 和 node03）之间的 Flume 数据传输架构图，node02 的 Agent 包含 memory Channel 和 avro Sink，node03 的 Agent 包含 avro Source、memory Channel 和 hdfs Sink，数据从 node02 的 Sink 流向 node03 的 Source。
