# 画面线理解：11-flume案例-flume级联-配置文件编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\11-flume案例-flume级联-配置文件编写【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:38, 01:09, 01:56, 02:31, 04:16, 04:57, 05:43, 06:04, 06:34, 06:59, 07:30, 07:45, 08:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 07:56:50

1) 这一组画面整体在讲如何在两台节点（node02 和 node03）上配置 Flume，实现从 node02 采集日志并转发到 node03，最终将数据写入 HDFS。

2) 按时间顺序列出每张画面的要点：
   画面1：展示 Flume Agent 的架构图，node02 上的 Source（exec）通过 memory Channel 连接到 Sink（avro），并标注“收集文件的数据 tail -F access_log”。
   画面2：PPT 页面显示“Step 1: Node02 安装 Flume”和“Step 2: Node02 配置 Flume”，并给出在 node02 上执行的命令：cd /export/servers && scp -r apache-flume-1.8.0-bin node02:$PWD。
   画面3：PPT 页面显示“Step 2: Node02 配置 Flume”，并给出在 node02 上执行的命令：cd /export/servers/apache-flume-1.8.0-bin/conf && vim tail-avro-logger.conf。
   画面4：PPT 页面显示“Step 3: 开发脚本向文件中写入数据”和“Step 4: Node03 Flume 配置文件”，并给出在 node03 上执行的命令：cd /export/servers/apache-flume-1.8.0-bin/conf。
   画面5：在 SourceCRT 中编辑配置文件，内容为：
   # Name the components on this agent
   a1.sources = r1
   a1.sinks = k1
   a1.channels = c1
   # Describe/configure the source
   a1.sources.r1.type = exec
   a1.sources.r1.command = tail -F /export/servers/taillogs/access_log
   a1.sources.r1.channels = c1
   # Describe the sink
   ##sink露说腔vro胸一贴枚莘茎脣脣
   a1.sinks.k1 = k1
   a1.sinks.k1.type = avro
   a1.sinks.k1.channel = c1
   a1.sinks.k1.hostname = 192.168.174.120
   a1.sinks.k1.port = 4141
   a1.sinks.k1.batch-size = 10
   # Use a channel which buffers events in memory
   a1.channels.c1.type = memory
   a1.channels.c1.capacity = 1000
   a1.channels.c1.transactionCapacity = 100
   画面6：在 SourceCRT 中编辑配置文件，内容与画面5相同，但光标位于 a1.sinks.k1.type = avro 行。
   画面7：在 SourceCRT 中执行命令 mkdir /export/servers/taillogs/，并显示成功创建目录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
   画面2：
   cd /export/servers
   scp -r apache-flume-1.8.0-bin node02:$PWD
   画面3：
   cd /export/servers/apache-flume-1.8.0-bin/conf
   vim tail-avro-logger.conf
   画面4：
   cd /export/servers/apache-flume-1.8.0-bin/conf
   画面5：
   # Name the components on this agent
   a1.sources = r1
   a1.sinks = k1
   a1.channels = c1
   # Describe/configure the source
   a1.sources.r1.type = exec
   a1.sources.r1.command = tail -F /export/servers/taillogs/access_log
   a1.sources.r1.channels = c1
   # Describe the sink
   ##sink露说腔vro胸一贴枚莘茎脣脣
   a1.sinks.k1 = k1
   a1.sinks.k1.type = avro
   a1.sinks.k1.channel = c1
   a1.sinks.k1.hostname = 192.168.174.120
   a1.sinks.k1.port = 4141
   a1.sinks.k1.batch-size = 10
   # Use a channel which buffers events in memory
   a1.channels.c1.type = memory
   a1.channels.c1.capacity = 1000
   a1.channels.c1.transactionCapacity = 100
   画面7：
   mkdir /export/servers/taillogs/

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
   画面1：架构图中，Source（exec）指向 Channel（memory），Channel（memory）指向 Sink（avro）。
   画面2：PPT 标题为“分析”，内容为“第一个agent负责收集文件当中的数据，通过网络发送到第二个agent当中去，第二个agent负责接收第一个agent发送的数据，并将数据保存到hdfs上面去”。
   画面3：PPT 标题为“分析”，内容与画面2相同。
   画面4：PPT 标题为“Step 3: 开发脚本向文件中写入数据”和“Step 4: Node03 Flume 配置文件”。

5) 不要评价画面美观，不要输出与课程无关的内容。
