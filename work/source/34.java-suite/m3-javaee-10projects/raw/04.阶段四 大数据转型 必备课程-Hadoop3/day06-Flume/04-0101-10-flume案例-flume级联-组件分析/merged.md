# 10-flume案例-flume级联-组件分析

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\10-flume案例-flume级联-组件分析【海量资源尽在 ubkz.com】.mp4
- 时长 8分33秒（音频 513s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来继续学flom刚才给大家举的一些案例呢都是单个flom也就是只有一个flom agent在实际的应用中呢有时候呢是有多个flom组成的这个呢被称为flom agent的一个集连来我们来给大家举个例子来我们打开画图我们刚才呢给大家举的都是一个agent那么每个agent呢有source channel和sync那接下来我们把这个
[00:29] 图重新复制一下我们给大家重新画一张图假如说现在有这么一个需求我把这个呢先删掉那么其中呢有一台主机呢它有一个二进特那另外一台主机呢我再去放一个二进特好把这个呢再复制一份拷贝过来好这样子的话呢就实现了两个二进特的一个集联好这也是最简单的一种集联方式
[01:04] 那接下来我们举的这个案例要干什么事情呢我们来看看讲义好在这里呢我们需要实现这么一个功能说呀第一个agent呢负责收集文件中的数据通过网络呢发送给第二个agent注意这两个agent呢是放在不同的主机上那么第二呢agent负责收集第二个agent负责收集第一个agent的数据并把数据呢
[01:32] 保存在HDFS上OK那么问题来了那么左边这个agent呢他负责是收集数据把数据呢收集完之后呢发送给第二agent而第二个agent呢负责把数据呢最终存到HDFS好那我们先来搞清楚一件事情我们可以把第一个agent部署在一台机子上比如说我部署到node02这个机子上OK记住我们还需要在node02这个机子上呢
[02:02] 安装Flume别忘了这件事情好那下面这个是node03node03也就是我们这node03这台主机我们也部署一个agent那接下来我们问大家一个问题我要实现两个Flume的极点它的难点在哪里呢是不是还是对文件的一个配置呀不管是你多少个Flume你对于每一个Flume的agent总要去进行配置的好那么配置无非就是
[02:31] 配置这里的三个组件那咱现在先分析一下他们的三个组件分别写什么东西首先对于左边来讲呢我们要求呢左边这个二进堂他来收集文件的一个数据来看他说呢收集文件的数据那么收集文件的数据咱这个案例咱刚刚是不是做过了我把这个图呢再向右移一点来把这个呢向右移一点OK好了
[03:11] 那么接下来我们来看这个node02这机子呢它有个source它呢是是收集是收集文件的数据那么收集文件的数据我们的关注点是什么呢它用哪个source对不对那你收集文件的数据咱们刚才刚学过这个那我们的source写的是哪个呢我们的source需要去监控一个命令的变化命令的结果就是to-f
[03:45] 这个科标可以监控一个文件比如说access-log这么一个文件好那么要监控它的话我们的source用的是哪个来把这个拉一下我们的source用的是exec我们这个source exec这个source我把它标一下字体调大一点OK这是我们的一个source好那么有了这个source之后接下来我们
[04:20] 通过文件的一个变化来收集这个数据把这个数据放到哪里呢放这个签上中那这个签呢我们用的什么呢我们用的都是当前为止呢都是用的是memory存在内存里面那么关键是我收集完数据之后呢我这个sync怎么写因为咱们以往这个sync呢它要么把数据输出到控制台要么把这个数据输到hdfs但是这里又不一样了
[04:48] 这里是把这个收集的数据呢放到下一个agent这个怎么写呢大家注意这个地方的sync呢我们可以参考一下官方的文档我们来看一下在这个里边有一个文档这个文档呢咱们看左边左边呢给大家列出了很多的一些一些配置的一些信息你比如说这里边有flumosource还有向下翻还有呢这个flumosync
[05:16] 好这里边列出了一些常用的think在这里边有一个think呢我们要用叫everthink就这个这个everthink呢它可以实现多级浮轮母之间的一个关联那么也就是说你如果想把你的数据呢下沉到下一级的agent我们需要使用这个everthink这个everthink怎么配呢这里边呢注意这个里面有一个type这个type呢要写ever
[05:46] AVR那还要呢去绑定一个什么呢你看这里边还有一个叫hostnamehostname还有一个呢port这个hostname呢表示我要把数据发送到哪个主机它的一个urgentOK那么这个port呢是我要发送给哪个端口我们要指定这两个参数OK也就是说我们的think搞清楚了回到我们的图里边
[06:15] 好这个地方呢sync我们用的是avroavrook那么好了这边完成了那还有右边呢那第三台机子呢关键点是这个source我们的source以往呢要么从文件获取数据要么从目录获取数据还要呢从一些这个网络获取数据但是现在我获取的数据是来自上一机的sync那这个source怎么写呢
[06:46] 再回到刚才这个文档我们来看再看左侧回到这个最上面好在这里呢也有一些sauce的一些描述我们来看在这里呢找一下这里的sauceflum sauces看这这里边有一个ever sauce点一下这个ever sauce就是它可以去接收上一集urgent它的一个输出内容OK那么这里边呢这个type
[07:17] 也就是说这个source类型我们还是写ever而且呢需要去绑定一个IP绑定一个端口那么对方发给我的时候呢他要指定我的IP和端口而我呢需要绑定自己的IP和端口这三个是必须要设置的好那么有了这个之后呢我们再回到我们的图里边那也就是说我们这个source知道怎么写了我们还是写ever而这个channel呢
[07:48] 我们还是和以前一样我们写memory但是存储在内存里边好那还有最后这个sync怎么写这个sync呢决定了我们的数据发送到哪里对不对那这个sync呢我们说最终的数据我们要去到哪里呢是不是去到HDFS所以说呢我们这个地方呢我们的sync呢还是写HDFS好那么到这里的话呢我们相当于把这两台主机它们的三个组件
[08:18] 怎么配它的核心参数呢我们基本上就分析清楚了那接下来呢无非就是去分布去实施OK那么关于它的一个整个的一个流程呢我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

