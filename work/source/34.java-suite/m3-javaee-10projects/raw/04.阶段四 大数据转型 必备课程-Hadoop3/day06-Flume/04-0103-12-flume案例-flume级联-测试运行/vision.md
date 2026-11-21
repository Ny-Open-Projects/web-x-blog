# 画面线理解：12-flume案例-flume级联-测试运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\12-flume案例-flume级联-测试运行【海量资源尽在 ubkz.com】.mp4
- 抽帧：13 帧 @ 00:14, 00:32, 00:54, 01:04, 01:22, 01:40, 02:20, 02:53, 03:21, 03:33, 03:50, 04:02, 04:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 08:03:08

1) 这一组画面整体在讲如何在两个节点（node02 和 node03）上配置并启动 Flume Agent，实现从 node02 的内存通道通过 Avro 协议传输数据到 node03 的 HDFS。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了 Flume 的架构图，包含两个节点：node02 和 node03。
- node02 节点：包含一个 memory 类型的 Channel 和一个 avro 类型的 Sink，Sink 指向 node03。
- node03 节点：包含一个 avro 类型的 Source，连接到一个 memory 类型的 Channel，Channel 再连接到一个 hdfs 类型的 Sink。
- 两个节点都标注了 "Agent"。

画面2：
- 展示了 SecureCRT 连接 node03 的终端界面，当前目录为 /root/node03/conf#，等待输入命令。

画面3：
- 展示了 Typora 编辑器中的 Flume 配置文档，内容包括：
  - Step 5: 顺序启动
  - node03机器启动flume进程：
    cd /export/servers/apache-flume-1.8.0-bin/
    bin/flume-ng agent -c conf -f conf/avro-hdfs.conf -n a1 -Dflume.root.logger=INFO,console
  - node02机器启动flume进程：
    cd /export/servers/apache-flume-1.8.0-bin/
    bin/flume-ng agent -c conf -f conf/tail-avro-avro-logger.conf -n a1 -Dflume.root.logger=INFO,console
  - node02机器启动Shell脚本不生成文件：
    cd /export/servers/shells
    sh tail-file.sh

画面4：
- 展示了 SecureCRT 终端中 Flume 启动后的日志输出，内容包括：
  2019-05-10 16:11:35,795 (lifecycleSupervisor-1-1) [INFO - org.apache.flume.instrumentation.MonitoredCounterGroup.p.register(MonitoredCounterGroup.java:119)] Monitored counter group for type: SINK, name: k1. Successfully registered new MBean.
  2019-05-10 16:11:35,796 (lifecycleSupervisor-1-1) [INFO - org.apache.flume.instrumentation.MonitoredCounterGroup.p.start(MonitoredCounterGroup.java:95)] Component type: SINK, name: k1 started
  2019-05-10 16:11:35,796 (lifecycleSupervisor-1-1) [INFO - org.apache.flume.sink.AbstractRpcSink.createConnection(AbstractRpcSink.java:205)] Rpc sink k1: Building RpcClient with hostname: 192.168.174.120, port: 4141
  2019-05-10 16:11:35,803 (lifecycleSupervisor-1-1) [INFO - org.apache.flume.instrumentation.MonitoredCounterGroup.p.register(MonitoredCounterGroup.java:119)] Monitored counter group for type: SOURCE, name: r1. Successfully registered new MBean.
  2019-05-10 16:11:35,805 (lifecycleSupervisor-1-2) [INFO - org.apache.flume.instrumentation.MonitoredCounterGroup.p.start(MonitoredCounterGroup.java:95)] Component type: SOURCE, name: r1 started
  2019-05-10 16:11:35,932 (lifecycleSupervisor-1-2) [WARN - org.apache.flume.api.NettyAvroRpcClient.configure(NettyAvroRpcClient.java:634)] Using default maxWorkers
  2019-05-10 16:11:36,535 (lifecycleSupervisor-1-1) [INFO - org.apache.flume.sink.AbstractRpcSink.start(AbstractRpcSink.java:301)] Rpc sink k1 started

画面5：
- 展示了 SecureCRT 终端中 Flume 启动后的日志输出，内容与画面4基本相同，但部分敏感信息（如主机名）被黑色方块遮挡。

画面6：
- 展示了 Typora 编辑器中的 Flume 配置文档，内容包括：
  - Step 3: 开发脚本向文件中写入数据
    直接将node03下面的脚本和数据传到node02即可，node03机器上执行以下命令
    cd /export/servers
    scp -r shells/ taillogs/ node02:$PWD
  - Step 4: Node03 Flume 配置文件
    在node03机器上升级flume的配置文件
  - 配置文件内容：
    #!#sink的avro是一个数据发送者
    a1.sinks.k1.type = avro
    a1.sinks.k1.channel = c1
    a1.sinks.k1.hostame = 192.168.174.120
    a1.sinks.k1.port = 4141
    a1.sinks.k1.batch-size = 10
    # use a channel which buffers events in memory
    a1.channels.c1.type = memory
    a1.channels.c1.capacity = 1000
    a1.channels.c1.transactionCapacity = 100
    # Bind the source and sink to the channel
    a1.sources.r1.channels = c1
    a1.sinks.k1.channel = c1
