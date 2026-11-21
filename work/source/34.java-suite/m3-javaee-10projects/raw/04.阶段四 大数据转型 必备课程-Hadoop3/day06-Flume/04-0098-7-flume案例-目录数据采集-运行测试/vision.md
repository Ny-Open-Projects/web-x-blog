# 画面线理解：7-flume案例-目录数据采集-运行测试

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\7-flume案例-目录数据采集-运行测试【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:52, 01:06, 01:15, 02:00, 02:16, 02:49, 03:40, 03:55, 04:07, 04:29, 04:45, 05:05, 05:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 07:34:39

1) 这一组画面整体在讲如何配置并启动Flume Agent，将本地文件数据采集并写入HDFS。

2) 按时间顺序列出每张画面的要点：
画面1：
要点：展示Flume Agent架构图，包含Source、Channel、Sink三个组件，并列出实现步骤：1) 写配置文件；2) 配置Source；3) 配置Channel；4) 配置Sink；5) 启动Agent；6) 运行测试。同时展示配置文件中各组件的配置示例：
al.sources = r1
al.sources.r1.type = spooldir
al.sources.r1.spoolDir = /export/servers/dirfile
al.sources.r1.fileHeader = true
al.channels = c1
al.channels.c1.type = memory
al.channels.c1.capacity = 1000
al.channels.c1.transactionCapacity = 100
al.sinks = k1
al.sinks.k1.type = hdfs
al.sinks.k1.channel = c1
al.sinks.k1.hdfs.path = hdfs://node01:9000/spooldir/files/%y-%m-%d/%H/
al.sinks.k1.hdfs.filePrefix = events-
al.sinks.k1.hdfs.round = true
al.sinks.k1.hdfs.roundValue = 10
al.sinks.k1.hdfs.roundUnit = minute
al.sinks.k1.hdfs.rollInterval = 3
al.sinks.k1.hdfs.rollSize = 20
al.sinks.k1.hdfs.rollCount = 5
al.sinks.k1.hdfs.batchSize = 1
al.sinks.k1.hdfs.useLocalTimeStamp = true
al.sinks.k1.hdfs.fileType = DataStream

画面2：
要点：展示Flume配置文件的Channel部分配置及参数解释，以及启动Flume的命令：
bin/flume-ng agent -f ./conf/spooldir.conf -n al -Dflume.root.logger=INFO,console

画面3：
要点：展示Flume Agent启动后在SecureCRT终端的输出日志，显示Source和Sink组件已成功启动。

画面4：
要点：再次展示Flume Agent架构图，标注了Source、Channel、Sink三个组件及其容量参数（batchSize、transactionCapacity）。

画面5：
要点：展示SecureCRT终端中上传文件的命令提示，以及文件夹中包含的SecureCRT相关配置文件。

画面6：
要点：展示SecureCRT终端的空白界面，无任何操作。

画面7：
要点：展示Windows资源管理器中包含的文件，如zookeeper.out、install.log、anaconda-ks.cfg等。

画面8：
要点：展示SecureCRT终端中Flume启动后因找不到指定文件而报错的日志，错误信息为：
Could not find file: /export/servers/dirfile/a.txt (No such file or directory)

画面9：
要点：展示HDFS浏览器界面，路径为/spooldir，显示一个名为“files”的目录。

画面10：
要点：展示HDFS浏览器界面，路径为/spooldir/files，显示两个文件。

画面11：
要点：展示HDFS浏览器中对文件“events-1557455020423”的块信息弹窗，显示其Block ID、Block Pool、Generation Stamp及可用性（分布在node02.hadoop.com、node03.hadoop.com）。

画面12：
要点：展示EditPlus文本编辑器，内容为空。

画面13：
要点：展示Flume配置文件中Sink部分的配置，其中hdfs.path配置为：
hdfs://node01:9000/spooldir/files/%y-%m-%d/%H/

画面14：
要点：展示HDFS浏览器界面，路径为/spooldir/files/19-05-10/1020，显示两个文件。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
al.sources = r1
al.sources.r1.type = spooldir
al.sources.r1.spoolDir = /export/servers/dirfile
al.sources.r1.fileHeader = true
al.channels = c1
al.channels.c1.type = memory
al.channels.c1.capacity = 1000
al.channels.c1.transactionCapacity = 100
al.sinks = k1
al.sinks.k1.type = hdfs
al.sinks.k1.channel = c1
al.sinks.k1.hdfs.path = hdfs://node01:9000/spooldir/files/%y-%m-%d/%H/
al.sinks.k1.hdfs.filePrefix = events-
al.sinks.k1.hdfs.round = true
al.sinks.k1.hdfs.roundValue = 10
al.sinks.k1.hdfs.roundUnit = minute
al.sinks.k1.hdfs.rollInterval = 3
al.sinks.k1.hdfs.rollSize = 20
al.sinks.k1.hdfs.rollCount = 5
al.sinks.k1.hdfs.batchSize = 1
al.sinks.k1.hdfs.useLocalTimeStamp = true
al.sinks.k1.hdfs.fileType = DataStream

画面2：
bin/flume-ng agent -f ./conf/spooldir.conf -n al -Dflume.root.logger=INFO,console

画面8：
Could not find file: /export/servers/dirfile/a.txt (No such file or directory)

画面13：
hdfs://node01:9000/spooldir/files/%y-%m-%d/%H/

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：
架构图：Source → Channel → Sink
结构：Source指向Channel，Channel指向Sink。
表格数据：无。

画面4：
架构图：Source → Channel → Sink
结构：Source指向Channel，Channel指向Sink。
表格数据：无。

画面13：
无PPT标题或架构图。

5) 无。
