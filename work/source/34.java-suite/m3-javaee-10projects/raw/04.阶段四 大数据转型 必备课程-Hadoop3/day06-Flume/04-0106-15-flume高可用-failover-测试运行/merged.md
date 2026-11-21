# 15-flume高可用-failover-测试运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\15-flume高可用-failover-测试运行【海量资源尽在 ubkz.com】.mp4
- 时长 5分9秒（音频 309s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在搭建好Flom的一个集群之后呢接下来我们来启动Flom来做一个测试来先回到我刚才画的图那么这里边呢三台主机上都有Flom那我问大家一个问题我们先启动哪一个主机上的Flom呢我们可不可以先启动Node01上的答案是不可以的为什么呢因为Node01呢你看它的sync写的是Evo表示它要将这个数据呢
[00:30] 传递给下一级的二进头那这个时候呢当启动node01的时候呢node02和node03它们的flume还不存在呢那所以说我们必须先启动node02或node03那这样咱就先启动node03吧来回到讲义咱们呢先在node03上启动flume把这句话呢给它复制一下好在这里这是node03来执行让它启动
[01:01] 好稍等而启动完之后呢接下来我们再启动node02把呢这句话呢也复制一下它的这个配置文件叫collector走也启动好启动完了之后呢接下来我们再启动谁呢我们再启动node01在这里node01上启动这个主节点的一个fulome好了来这里都启动完了
[01:37] 好启动完之后呢现在不要忘了一个问题我们是node01这个flow模式监控文件的变化把他的信息呢发送给node02或者node03好那接下来呢我们就向那个文件来发送数据打开我们这个还是这个100这个拷贝这个窗口来我们点开点开之后呢在tail logs下面有一个脚本叫tail file.sh还记笔的
[02:04] 当我运行这个脚本的时候呢它就会向这个文件呢添加数据那么我们的node01这个form就会监控这个文件的变化走一下好它正在向这个文件写数据那写数据的话呢我们依次来看一下看node01好这个地方呢还要再看看谁呢再看看这个node02好你看这个地方它说收到了一些数据你看它正在走那node03呢
[02:33] Node03好像没什么变化这是为什么呢大家看我刚才画了一个图我说Node01发数据的时候它或者发给Node02或者发给Node03这两个呢其实只有一个能收到Node01的数据那么为什么是Node02来收到呢是因为呢咱们在配置的时候有一个选值不知道大家还记不记得来我打开这个打开这个Node01的配置向上翻在我们配置Node01的时候呢你看
[03:02] 这个priority k也就是说我们的node02这个这个flom它的选址是10而node03呢它的选址是1所以说呢它就优先接收到这个数据好所以说呢我们再回来那么你看它一直在收数据而它呢文字不动那接下来我们来做一个尝试假如说我把node02这个机子上的flom干掉也就相当于当机了记着再来一遍啊
[03:32] 我如果把这个上面的这个机子当机了把这个当机了我们看node03能不能接收到数据来走把它挂掉挂了之后咱们来看看node03能不能做到替补node02的一个功能好稍等一下稍等你看到没有它已经收到了数据了OK也就是说node02挂掉之后node03立刻就上位了那么这个就叫高可用那这个是如何实现呢
[04:01] 实际上是因为我们在配置的时候呢我们有一个叫这个处理机制这个type呢是一个fillover这个表示故障转移当一台的flowm呢出现故障另外一台立刻起到一个替换的一个作用好了那这个问题那假如说现在还有个问题如果说呢我把node02再重新启动我重新启动
[04:26] 那你说我重新启动完之后你说是node02收数据还是node03呢我们可以观察一下稍等一下啊我们可以观察一下你看他俩都不动了稍等哎你看到没有node02又开始收到数据了也就是当node02恢复了之后呢他又立刻他又去收数据了这个时候呢大家注意这个时候是什么原因呢是因为呢他俩都在活跃的时候呢他的犬只大那么他又会收到这个新的数据
[04:58] OK这是它的一个高可用的一个特点好那么关于呢Floom一个高可用的集群的搭建呢和测试呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

