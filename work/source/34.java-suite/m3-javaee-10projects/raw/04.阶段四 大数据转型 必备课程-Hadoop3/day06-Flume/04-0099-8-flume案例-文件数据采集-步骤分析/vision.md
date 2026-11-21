# 画面线理解：8-flume案例-文件数据采集-步骤分析

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\8-flume案例-文件数据采集-步骤分析【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:47, 02:04, 03:54, 04:15, 04:29, 05:17, 05:38, 06:41, 07:00, 07:21, 07:31, 09:11, 09:31, 10:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 07:40:39

1) 这一组画面整体在讲如何配置Flume Agent，通过Source、Channel和Sink三个组件实现日志文件到HDFS的采集与传输。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示Flume Agent架构图：Source → Channel → Sink。
- 实现步骤：
  1) 写一个配置文件: xxx.conf
  2) 配置Source
  3) 配置Channel
  4) 配置Sink
  5) 将Source, Channel和Sink组合在一起
  2) 启动Flume的Agent实例
  3) 运行测试

画面2：
- PPT标题：分析。
- 根据需求，首先定义以下3大要素：
  - 采集源，即Source——监控文件内容更新：exec tail -F file
  - 下沉目标，即Sink——HDFS文件系统：hdfs sink
  - Source和Sink之间的传递通道——channel，可用file channel 也可以用 内存channel
- Step 1: 定义 Flume 配置文件
  ```bash
  cd /export/servers/apache-flume-1.8.0-bin/conf
  vim tail-file.conf
  ```
  ```properties
  agent1.sources = sourcel
  agent1.sinks = sinkl
  agent1.channels = channell
  # Describe/configure tail -F sourcel
  agent1.sources.sourcel.type = exec
  agent1.sources.sourcel.command = tail -F /export/servers/taillogs/access_log
  agent1.sources.sourcel.channels = channell
  # Describe sinkl
  agent1.sinks.sinkl.type = hdfs
  ```

画面3：
- 继续展示Step 1: 定义 Flume 配置文件。
- 在画面2的基础上，补充了Sink的HDFS配置：
  ```properties
  agent1.sinks.sinkl.type = hdfs
  #a1.sinks.sinkl.channel = c1
  agent1.sinks.sinkl.hdfs.path = hdfs://node01:8020/weblog/flume-collection/Ky-Xm-SD/SH-AP
  agent1.sinks.sinkl.hdfs.filePrefix = access_log
  agent1.sinks.sinkl.hdfs.maxOpenFiles = 5000
  agent1.sinks.sinkl.hdfs.batchSize = 100
  ```

画面4：
- 展示了Flume Agent架构图：Source → Channel → Sink。
- 在画面1的基础上，增加了对“配置Source”部分的说明：
  ```properties
  agent1.sources.sourcel.type = exec
  agent1.sources.sourcel.command = tail -F /export/servers/taillogs/access_log
  ```

画面5：
- 展示了Flume Agent架构图：Source → Channel → Sink。
- 在画面4的基础上，画面下方显示了Windows任务栏，包含多个文件夹图标，如“Hadoop (空)”、“SecureCRT6”等。

画面6：
- 展示了Flume Agent架构图：Source → Channel → Sink。
- 在画面4的基础上，画面下方显示了Windows任务栏，仅显示“任务管理器”图标。

画面7：
- 展示了Flume Agent架构图：Source → Channel → Sink。
- 实现步骤：
  1) 写一个配置文件: xxx.conf
  2) 配置Source
  3) 配置Channel
  4) 配置Sink
  5) 将Source, Channel和Sink组合在一起
  2) 启动Flume的Agent实例
  3) 运行测试
- 在画面1的基础上，增加了对“配置Channel”的说明：
  ```properties
  agent1.channels.channell.type = memory
  agent1.channels.channell.keep-alive = 120
  agent1.channels.channell.capacity = 500000
  agent1.channels.channell.transactionCapacity = 600
  ```
