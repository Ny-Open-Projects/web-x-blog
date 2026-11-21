# 12-flume案例-flume级联-测试运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\12-flume案例-flume级联-测试运行【海量资源尽在 ubkz.com】.mp4
- 时长 4分28秒（音频 268s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在写好这个配置文件之后呢接下来我们来做第五步来启动我们的Floom注意这个Floom有两个我们启动的时候呢我们先启动哪一台呢大家想一下看我刚才画了一个图那么Floom2的数据呢要发给Floom3我们应该先启动Floom3OK那么我把这个呢直接复制一下来先来到我们的Floom3有这个
[00:32] 在这里export Service apache flume我来运行这个稍等让它卡在这里等待我们的数据那接下来呢我再启动flume2把这个也复制一下走来启动flume2请注意这两个flume呢都启动起来了启动起来之后呢有个问题是我们的flume3是接收flume2的数据对不起这个应该是
[01:16] 我们的这个node03接收node02这个Floom的数据那么我们这个Floom也就是node02这台机子的Floom接收谁呢看这个图来我们这个node02的Floom它是不是接收我们文件的变化呀所以说我们需要向这个文件写数据那么向哪个文件呢我们这个配置文件中已经写死了回到我们刚才我需要向export Service这个文件写数据那这个文件怎么写数据呢
[01:46] 我们刚才在node03上是不是写了一个脚本我可以把这个脚本拷贝过来来看一下在哪里写了脚本呢在export Service下面有个tail有个tail logs在这里有个tail failed sh我把它拷过去然后我用sctail拷贝到哪里呢拷贝到node02这个主机$pwd
[02:16] 好拷贝在这里来回车好拷贝过去之后呢我们来看一下我把node02呢也复制一份来克隆一个绘画出来我们来看export Service在tail logs里边进来是不是有这么一个文件那我接下来呢我把这个放左边来OK我的数据来sh tail我来运行这个脚本好运行这个脚本呢它就会像
[02:45] 这个文件写数据一写数据呢我们的110这个主机它的这个Flume就能收到数据而这个Flume的数据呢就会输出给这个Node03这台主机那Node03这台主机呢拿到这个数据之后呢就会把这个数据呢把它存储在HDFS也就是说从左到右呢它是整个一条龙OK 那我们接下来看我们来运行 走这个时候呢
[03:14] 我们来看一看这个node02有没有收到数据OK我们来看一下node02这里再看node03node03呢它说有一个events正在收集数据好那接下来我们再去看看hdfs呢有没有我们想要的数据hdfs在哪里看呢我们再看这个配置文件在node03呢在这个hdfs有ever hdfs来我们来看一下打开hdfs
[03:44] 好在这个根目录下面有个ever稍等ever有进来hdfs进来ok进来再进来你会发现是不是拆分中很多小文件当然了我在设的时候我设的时候它这个滚动可能频率太大了你可以去加一些其他参数ok保证它不会产生这么多小文件好那这个说明了我们从左边开始向文件写数据
[04:14] 第一个Fulmer到第二个Fulmer一直呢到这个HDFS这个流程是没问题的OK那么这个呢就是两个urgent之间的一个集联好那么关于他们的集联呢我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

