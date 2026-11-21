# 画面线理解：9-flume案例-文件数据采集-运行测试

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\9-flume案例-文件数据采集-运行测试【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:32, 00:40, 01:11, 01:32, 01:37, 02:01, 02:25, 03:04, 03:25, 03:45, 04:48, 05:00, 05:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 07:47:07

1) 这一组画面整体在讲如何配置Flume Agent，将本地日志文件通过tail-F方式采集并写入HDFS。

2) 按时间顺序列出每张画面的要点：
画面1：
要点：展示Flume架构图（Source → Channel → Sink → HDFS），并列出实现步骤：1) 写配置文件；2) 配置Source；3) 配置Channel；4) 配置Sink；5) 组合；6) 启动Agent；7) 运行测试。同时展示配置文件中各组件的命名配置：agent1.sources = source1；agent1.sinks = sink1；agent1.channels = channel1。

画面2：
要点：在SourceCRT终端中新建配置文件“tail-file.conf”。

画面3：
要点：在Typora中展示Flume配置文件的完整内容，包含Source、Channel、Sink的详细配置。其中Source配置为exec类型，命令为tail -F /export/servers/taillogs/access_log，绑定到channel1；Sink配置为hdfs类型，路径为hdfs://node01:8020/weblog/flume-collection/%y-%m-%d/%H-%M，文件前缀为access_log，batchSize为100，fileType为DataStream等。

画面4：
要点：在SourceCRT终端中显示配置文件内容，并执行命令创建HDFS目录和日志文件。

画面5：
要点：在SourceCRT终端中执行命令创建HDFS目录和日志文件，同时在Typora中展示配置文件内容。

画面6：
要点：在Typora中展示Flume配置文件的完整内容，包含Source、Channel、Sink的详细配置。其中Source配置为exec类型，命令为tail -F /export/servers/taillogs/access_log，绑定到channel1；Sink配置为hdfs类型，路径为hdfs://node01:8020/weblog/flume-collection/%y-%m-%d/%H-%M，文件前缀为access_log，batchSize为100，fileType为DataStream等。

画面7：
要点：在SourceCRT终端中执行命令创建HDFS目录和日志文件，同时在Typora中展示配置文件内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
agent1.sources = source1
agent1.sinks = sink1
agent1.channels = channel1

画面3：
# Describe/configure tail -F source1
agent1.sources.source1.type = exec
agent1.sources.source1.command = tail -F /export/servers/taillogs/access_log
agent1.sources.source1.channels = channel1

# Describe sink1
agent1.sinks.sink1.type = hdfs
agent1.sinks.sink1.channel = c1
agent1.sinks.sink1.hdfs.path = hdfs://node01:8020/weblog/flume-collection/%y-%m-%d/%H-%M
agent1.sinks.sink1.hdfs.filePrefix = access_log
agent1.sinks.sink1.hdfs.maxOpenFiles = 5000
agent1.sinks.sink1.hdfs.batchSize = 100
agent1.sinks.sink1.hdfs.fileType = DataStream
agent1.sinks.sink1.hdfs.writeFormat = Text
agent1.sinks.sink1.hdfs.rollSize = 102400
agent1.sinks.sink1.hdfs.rollInterval = 60
agent1.sinks.sink1.hdfs.round = true
agent1.sinks.sink1.hdfs.roundValue = 10
agent1.sinks.sink1.hdfs.roundUnit = minute
agent1.sinks.sink1.hdfs.useLocalTimeStamp = true

# Use a channel which buffers events in memory
agent1.channels.channel1.type = memory
agent1.channels.channel1.keepAlive = 120
agent1.channels.channel1.capacity = 500000
agent1.channels.channel1.transactionCapacity = 600

# Bind the source and sink to the channel
agent1.sources.source1.channels = channel1
agent1.sinks.sink1.channel = channel1

画面6：
Step 2: 启动 Flume
cd /export/servers/apache-flume-1.6.0-cdh5.14.0-bin
bin/flume-ng agent -c conf -f conf/tail-file.conf -n agent1 -Dflume.root.logger=INFO,console

Step 3: 开发 Shell 脚本时追加文件内容
mkdir -p /export/servers/shells/
cd /export/servers/shells/
vim tail-file.sh

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：
架构图：Source → Channel → Sink → HDFS
PPT标题：实现步骤
步骤列表：
1) 写一个配置文件：xxx.conf
2) 配置三个组件的名字
3) 配置Source
4) 配置Channel
5) 将Source, Channel和Sink组合在一起
6) 启动Flume的Agent实例
7) 运行测试

画面3：
PPT标题：2.2.1 Flume配置文件
步骤列表：
Step 1: 下载解压Flume安装包
Step 2: 开发配置文件
Step 3: 启动Flume
Step 4: 上传文件到HDFS
Step 5: Agent级联

画面6：
PPT标题：Step 2: 启动 Flume
Step 2: 启动 Flume
cd /export/servers/apache-flume-1.6.0-cdh5.14.0-bin
bin/flume-ng agent -c conf -f conf/tail-file.conf -n agent1 -Dflume.root.logger=INFO,console

Step 3: 开发 Shell 脚本时追加文件内容
mkdir -p /export/servers/shells/
cd /export/servers/shells/
vim tail-file.sh

5) 不要评价画面美观，不要输出与课程无关的内容。
