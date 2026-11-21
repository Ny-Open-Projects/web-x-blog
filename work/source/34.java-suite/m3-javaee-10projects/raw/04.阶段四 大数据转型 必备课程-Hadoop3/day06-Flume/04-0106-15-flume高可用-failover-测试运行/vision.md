# 画面线理解：15-flume高可用-failover-测试运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\15-flume高可用-failover-测试运行【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:59, 01:09, 01:25, 01:34, 02:29, 02:59, 03:20, 03:37, 03:51, 04:18, 04:28, 04:39, 05:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 08:14:08

1) 这一组画面整体在讲什么（一句话）：
演示如何在三台节点（node01、node02、node03）上配置和启动Flume Agent，实现从node01采集文件新增数据并通过failover机制将数据发送到node02或node03的HDFS。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 需求：node01采集文件新增数据，采集后发送给node02或node03的Flume Agent。
- 架构图：node01的Agent指向node02和node03的Agent，标注“failover”。
- node01 Agent配置：Source: exec, Channel: memory, Sink: avro。
- node02 Agent配置：Source: avro, Channel: memory, Sink: hdfs。
- node03 Agent配置：Source: avro, Channel: memory, Sink: hdfs。

画面2：
- 在node03上启动Flume Agent，命令为：bin/flume-ng agent -n a1 -c conf -f conf/collector.conf -Dflume.root.logger=DEBUG,console。

画面3：
- Typora中显示的PPT内容：Step 4: 顺序启动。
- 代码块：node03机器上面启动Flume的命令。
- 代码块：node02机器上面启动Flume的命令。
- 代码块：node01机器上面启动Flume的命令。

画面4：
- node01终端界面，显示已进入Flume目录，准备执行命令。

画面5：
- 在node01上执行启动Flume Agent的命令：bin/flume-ng agent -n agent1 -c conf -f conf/agent.conf -Dflume.root.logger=DEBUG,console。

画面6：
- node01终端显示Flume Agent启动日志，包括Avro source接收事件批次、HDFS sink创建临时文件、文件重命名等操作。

画面7：
- Typora中显示的PPT内容：Step 4: 顺序启动。
- 代码块：node03机器修改配置文件的内容。
- 代码块：a1.sources.r1.bind = node02。
- 代码块：a1.sinks.k1.hdfs.path = hdfs://node01:8020/flume/failover/。
- 代码块：a1.sinks.k1.hdfs.fileType = DataStream。
- 代码块：a1.sinks.k1.hdfs.writeFormat = TEXT。
- 代码块：a1.sinks.k1.hdfs.rollInterval = 10。
- 代码块：a1.sinks.k1.hdfs.filePrefix = NY-Sm-Xd。

画面8：
- node03终端显示Flume Agent启动日志，包括NettyServer AvroHandler绑定端口、配置文件轮询检查等。

画面9：
- node03终端显示Flume Agent启动日志，包括HDFS sink创建临时文件、文件重命名等操作。

画面10：
- node03终端显示Flume Agent启动日志，包括HDFS sink创建临时文件、文件重命名等操作。

画面11：
- node03终端显示Flume Agent启动日志，包括HDFS sink创建临时文件、文件重命名等操作。

画面12：
- node03终端显示Flume Agent启动日志，包括组件启动、监控计数器注册等。

画面13：
- node03终端显示Flume Agent启动日志，包括Avro source启动、接收事件批次等。

画面14：
- node03终端显示Flume Agent启动日志，包括HDFS sink创建临时文件、文件重命名等操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
- 需求：
  1. node01去采集一个文件的新增数据
  2. node01采集数据之后发送给node02
  或者node03的flume的Agent

画面2：
- 命令：
  bin/flume-ng agent -n a1 -c conf -f conf/collector.conf -Dflume.root.logger=DEBUG,console

画面3：
- 代码块：
  cd /export/servers/apache-flume-1.8.0-bin
  bin/flume-ng agent -n a1 -c conf -f conf/collector.conf -Dflume.root.logger=DEBUG,console

  cd /export/servers/apache-flume-1.8.0-bin
  bin/flume-ng agent -n a1 -c conf -f conf/collector.conf -Dflume.root.logger=DEBUG,console

  cd /export/servers/apache-flume-1.8.0-bin
  bin/flume-ng agent -n agent1 -c conf -f conf/agent.conf -Dflume.root.logger=DEBUG,console

画面5：
- 命令：
  bin/flume-ng agent -n agent1 -c conf -f conf/agent.conf -Dflume.root.logger=DEBUG,console

画面7：
- 代码块：
  a1.channels = c1
  a1.sinks = k1
  #set channel
  a1.channels.c1.type = memory
  a1.channels.c1.capacity = 1000
  a1.channels.c1.transactionCapacity = 100

  ## other node,nna to nns
  a1.sources.r1.type = avro
  a1.sources.r1.bind = node02
  a1.sources.r1.port = 52020
  a1.sources.r1.channels = c1

  ##set sink to hdfs
  a1.sinks.k1.type = hdfs
  a1.sinks.k1.hdfs.path = hdfs://node01:8020/flume/failover/
  a1.sinks.k1.hdfs.fileType = DataStream
  a1.sinks.k1.hdfs.writeFormat = TEXT
  a1.sinks.k1.hdfs.rollInterval = 10
  a1.sinks.k1.hdfs.filePrefix = NY-Sm-Xd

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：
- PPT标题：Step 4: 顺序启动。
- 代码块标题：node03机器上面启动Flume。
- 代码块标题：node02机器上面启动Flume。
- 代码块标题：node01机器上面启动Flume。

画面1：
- 架构图：node01的Agent指向node02和node03的Agent，标注“failover”。
- node01 Agent配置：Source: exec, Channel: memory, Sink: avro。
- node02 Agent配置：Source: avro, Channel: memory, Sink: hdfs。
- node03 Agent配置：Source: avro, Channel: memory, Sink: hdfs。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
