# 画面线理解：6-flume案例-目录数据采集-配置文件编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\6-flume案例-目录数据采集-配置文件编写【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:39, 01:44, 03:05, 03:34, 05:12, 08:09, 08:47, 16:04, 18:50, 19:33, 20:10, 20:44, 21:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 07:30:45

1) 这一组画面整体在讲如何配置Flume Agent，将本地目录文件采集并写入HDFS。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了Flume Agent架构图，包含Source、Channel、Sink三个组件。
- 列出实现步骤：1.写配置文件；2.配置Source；3.配置Channel；4.配置Sink；5.组合组件；6.启动Agent；7.运行测试。

画面2：
- 展示了Flume架构图和配置文件的编写步骤。
- 列出Flume配置文件的编写步骤：cd /export/servers/apache-flume-1.8.0-bin/conf，mkdir -p /export/servers/dirfile，vim spooldir.conf。
- 展示了配置文件中定义组件名称的代码：
  # Name the components on this agent
  a1.sources = r1
  a1.sinks = k1
  a1.channels = c1

画面3：
- 继续展示配置文件，添加了Source的配置项。
- 代码：
  # Describe/configure the source
  #注意：不能往监控目录中重复写同名文件
  a1.sources.r1.type = spooldir
  a1.sources.r1.spoolDir = /export/servers/dirfile
  a1.sources.r1.fileHeader = true

画面4：
- 展示了Flume Agent架构图，Source指向Channel，Channel指向Sink。
- 展示了配置文件中Source的配置项：
  a1.sources.r1.type = spooldir
  a1.sources.r1.spoolDir = /export/servers/dirfile
  a1.sources.r1.fileHeader = true

画面5：
- 展示了配置文件中Sink和Channel的配置项。
- 代码：
  # Describe the sink
  a1.sinks.k1.type = hdfs
  a1.sinks.k1.channel = c1
  a1.sinks.k1.hdfs.path = hdfs://node01:8020/spooldir/files/%y-%m-%d/%H%M/
  a1.sinks.k1.hdfs.filePrefix = events
  a1.sinks.k1.hdfs.round = true
  a1.sinks.k1.hdfs.roundValue = 10
  a1.sinks.k1.hdfs.roundUnit = minute
  a1.sinks.k1.hdfs.rollSize = 20
  a1.sinks.k1.hdfs.rollCount = 5
  a1.sinks.k1.hdfs.batchSize = 1
  a1.sinks.k1.hdfs.useLocalTimeStamp = true
  #生成的文件类型，默认是SequenceFile，可用DataStream，则为普通文本
  a1.sinks.k1.hdfs.fileType = DataStream
  # Use a channel which buffers events in memory
  a1.channels.c1.type = memory
  a1.channels.c1.capacity = 1000
  a1.channels.c1.transactionCapacity = 100
  # Bind the source and sink to the channel
  a1.sources.r1.channels = c1

画面6：
- 展示了Flume Agent架构图，包含Source、Channel、Sink三个组件。
- 展示了配置文件中Source、Channel、Sink的配置项：
  a1.sources.r1.type = spooldir
  a1.sources.r1.spoolDir = /export/servers/dirfile
  a1.sources.r1.fileHeader = true
  a1.channels.c1.type = memory
  a1.channels.c1.capacity = 1000
  a1.channels.c1.transactionCapacity = 100
  a1.sinks.k1.type = hdfs
  a1.sinks.k1.channel = c1

画面7：
- 展示了配置文件中Sink的配置项，高亮显示了hdfs.path和filePrefix。
- 代码：
  a1.sinks.k1.type = hdfs
  a1.sinks.k1.channel = c1
  a1.sinks.k1.hdfs.path = hdfs://node01:8020/spooldir/files/%y-%m-%d/%H%M/
  a1.sinks.k1.hdfs.filePrefix = events
  a1.sinks.k1.hdfs.round = true
  a1.sinks.k1.hdfs.roundValue = 10
  a1.sinks.k1.hdfs.roundUnit = minute
  a1.sinks.k1.hdfs.rollSize = 20
  a1.sinks.k1.hdfs.rollCount = 5
  a1.sinks.k1.hdfs.batchSize = 1
  a1.sinks.k1.hdfs.useLocalTimeStamp = true
  #生成的文件类型，默认是SequenceFile，可用DataStream，则为普通文本
  a1.sinks.k1.hdfs.fileType = DataStream
  # Use a channel which buffers events in memory
  a1.channels.c1.type = memory
  a1.channels.c1.capacity = 1000
  a1.channels.c1.transactionCapacity = 100
  # Bind the source and sink to the channel
  a1.sources.r1.channels = c1

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
cd /export/servers/apache-flume-1.8.0-bin/conf
mkdir -p /export/servers/dirfile
vim spooldir.conf

# Name the components on this agent
a1.sources = r1
a1.sinks = k1
a1.channels = c1

画面3：
# Describe/configure the source
#注意：不能往监控目录中重复写同名文件
a1.sources.r1.type = spooldir
a1.sources.r1.spoolDir = /export/servers/dirfile
a1.sources.r1.fileHeader = true

画面5：
# Describe the sink
a1.sinks.k1.type = hdfs
a1.sinks.k1.channel = c1
a1.sinks.k1.hdfs.path = hdfs://node01:8020/spooldir/files/%y-%m-%d/%H%M/
a1.sinks.k1.hdfs.filePrefix = events
a1.sinks.k1.hdfs.round = true
a1.sinks.k1.hdfs.roundValue = 10
a1.sinks.k1.hdfs.roundUnit = minute
a1.sinks.k1.hdfs.rollSize = 20
a1.sinks.k1.hdfs.rollCount = 5
a1.sinks.k1.hdfs.batchSize = 1
a1.sinks.k1.hdfs.useLocalTimeStamp = true
#生成的文件类型，默认是SequenceFile，可用DataStream，则为普通文本
a1.sinks.k1.hdfs.fileType = DataStream
# Use a channel which buffers events in memory
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100
# Bind the source and sink to the channel
a1.sources.r1.channels = c1

画面6：
a1.sources.r1.type = spooldir
a1.sources.r1.spoolDir = /export/servers/dirfile
a1.sources.r1.fileHeader = true
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100
a1.sinks.k1.type = hdfs
a1.sinks.k1.channel = c1

画面7：
a1.sinks.k1.type = hdfs
a1.sinks.k1.channel = c1
a1.sinks.k1.hdfs.path = hdfs://node01:8020/spooldir/files/%y-%m-%d/%H%M/
a1.sinks.k1.hdfs.filePrefix = events
a1.sinks.k1.hdfs.round = true
a1.sinks.k1.hdfs.roundValue = 10
a1.sinks.k1.hdfs.roundUnit = minute
a1.sinks.k1.hdfs.rollSize = 20
a1.sinks.k1.hdfs.rollCount = 5
a1.sinks.k1.hdfs.batchSize = 1
a1.sinks.k1.hdfs.useLocalTimeStamp = true
#生成的文件类型，默认是SequenceFile，可用DataStream，则为普通文本
a1.sinks.k1.hdfs.fileType = DataStream
# Use a channel which buffers events in memory
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100
# Bind the source and sink to the channel
a1.sources.r1.channels = c1

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：
- 标题：Flume架构图
- 架构图：Source → Channel → Sink
- 标注：Agent

画面2：
- 标题：Flume架构图
- 标题：Flume 配置文件
- 标题：Step 1: Flume 配置文件
-
