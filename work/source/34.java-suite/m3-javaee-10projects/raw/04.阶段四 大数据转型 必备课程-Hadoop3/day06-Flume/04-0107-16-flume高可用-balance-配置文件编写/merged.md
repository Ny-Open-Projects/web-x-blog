# 16-flume高可用-balance-配置文件编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\16-flume高可用-balance-配置文件编写【海量资源尽在 ubkz.com】.mp4
- 时长 8分43秒（音频 523s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来学习Flum高可用的另外一种机制负载均衡什么是负载均衡呢回到我们刚才画的图里面好在这里我们刚才是node01来去收集文件的新增数据然后收集完之后呢发给node02或者node03在这里的话呢它是优先发给node02因为node02呢它的选值更高一点但是node03呢一直是观察着一个角色
[00:29] 它会看着Node02什么时候挂掉然后呢它再作为补充那这个时候有时候呢会造成一个问题就是Node02过多的承载了所有的数据那这个时候Node03呢它的一个作用呢只是一个备份的一个作用那接下来我们就有种想法能不能让Node02和Node03都能够接收数据呢或者说它俩平均去分配我们数据收集的一个压力呢那这个时候呢我们把这种思想呢其实就是
[00:59] 负载均衡比如说这里边Node01收集了100兆的数据好 100兆那么它收集100兆的数据的话我们可以把其中的50兆分给Node02而把剩余的50兆分给Node03让它俩平均去收集平均去转移那么Node01收集的数据这种思想就叫负载均衡
[01:31] 那如何实现负载均衡呢其实我们只需要呢对三个三个主机上的一个Flume进行配置就可以了那么它们最大的不同就是我们之前配置这个处理方式的时候呢我们选的是Failover不知道大家还记不记得那如果说你采用负载均衡我们只需要把Failover变成一个叫Load BalanceBalance就可以了那这个呢就是所谓的负载均衡
[02:02] 好基本上呢其他的配置都差不多那接下来我们就来看一下如何实现这么一个负载均衡回到我们的讲义我们来看首先呢我们要实现负载均衡还是三台机器呢Node01来收集数据然后呢Node02 Node03来接收Node01的数据那接下来我们来先对Node01呢做一个配置我们呢在这个康复这个目录下面呢我们来建这么一个文件
[02:31] 来在这个打开我们的基群我们找到node01进入export Service apache好conf这个目录下面我们来建一个文件然后呢把这个配置信息呢放进去好直接复制然后粘进去好粘完之后呢我们来一起来看一下这里边需要注意的一些点好那这里边呢把空行干掉好这里边呢前三个呢是
[03:09] 起了一个别名这个sync呢它有两个一个是k一个是kr好那接下来呢这个地方呢两个sync组成了一个组这个组呢叫g1好这里呢配置了一个channel这个channel呢是memory channel后面是它一个容量ok那这个地方呢还有一个sauce这个下面是一个是一个sauce这个sauce呢它的这个channel是ce然后呢这个sauce它的类型呢是encc
[03:39] 因为它要监控一个文件的变化要去监控这个命令的输出结果和以前是一样的OK这个都没变好了接下来我们再看sync这个sync呢它对应的channel也是ce也是ceOK那它这个type呢是ever为什么因为它要node01呢要把这个数据交给下一集的这个flom所以说呢是ever那么这个地方呢还要去指定
[04:07] 你要去发给哪一个主机我要发给node02它的端口是52020好那这是它一个信息那接下来呢还有这是一个sync1还有一个sync2那么sync2呢肯定是指定node03了那它的类型也是evr好那还有呢它的这个主机呢是node03端口也是52020OK那这个你就指定完了那接下来呢是指定这个组这个组的话呢
[04:35] 它的这个组呢里边有K1和K2好关键点来了在这里呢我们来看一下这几个配置把空行干掉这个地方呢有一个叫Processor Type那我们以前呢在写Node01Processor Type的时候我们写的是Failover叫故障转移这个故障转移那么另外一个立刻替补但是这里叫Load Balance这个叫负载均衡我只有配置了这个呢
[05:03] 它才能实现两台主机同时能够接收我们node01的数据好那这个地方呢还有个叫selector这个地方有个run的rubin这个表示轮循表示轮循什么意思呢就是说我两台机子两台机子都接收数据那么谁接收多少呢这个轮循机制看这个图轮循机制大概可以这样理解就说它收到一条接下来它再收然后呢再回来它继续然后一直轮流着
[05:33] 去接收Node01的数据这就所谓的负载均衡好这里还有一个超时时间来超时时间这个单位是秒好那么这个的话呢重点其实就在这Load Balance和这个Run Ruby好那么这个Node01呢我们就配置好了配置好之后呢接下来我们再配置Node02和Node03来打开我们的讲义在这里呢我们来配置Node02还是在这个目录下面有这么一个文件
[06:04] 好我们来看看node02 110用paw的service87然后呢conf这个目录好在这里走一下我们把这个信息呢给它粘进去好从上到下我们来看一下首先呢这个sourcesyncchannel这个没什么好说的接下来呢这个source呢是ever因为它要接受node01的一些数据ever好这个
[06:42] channel是C1这个地方呢就是绑定自己的IP和端口这个地方是node02这个端口52020好那接下来呢还有一个那还有一个呢这个sync这个sync的话呢这个sync呢它的类型呢是loggerok它类型logger好这个地方呢它把这个数据呢通过日志的方式输出好了那这个地方还有一个channel这个channel呢是memory channelok
[07:11] 好了这是memory channel稍等我看我改错了没有OK那接下来呢还有一个就是它这个channel呢这个source指定的channel是ce那最后呢还有sync指定的channel呢也是ce就这么简单通过这个呢把它们整合在一起好这是一个最基本的一个这个EverSource的一个配置好这是node02那接下来呢我们再看node03回到那个node03上
[07:40] 好进入export service87flomconf好在这里呢我们来建一个文件来下方建一个load balance server.conf好在这里的话呢我们把下面这个呢来直接来复制然后粘贴好粘贴完之后我们也看来看一下首先前三个没什么问题接下来这个source还是evr
[08:16] 这个地方要绑定自己的一个IPNode03主机名这个端口52020这个Sync是Logger把这个信息输到日志上OK那么还有这个Channel是Memory好接下来最后这个地方Channel CEOK就配置完了好配置完了之后我们先把这个视频暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置Flume的多节点数据采集与负载均衡架构，包含需求说明、架构图、配置文件编写及关键参数设置。

2) 按时间顺序列出每张画面的要点：
画面1：
- 需求：node01采集文件新增数据，采集后发送给node02或node03的Flume Agent。
- 架构图：node01 Agent（Source: exec, Channel: memory, Sink: avro）指向node02 Agent（Source: avro, Channel: memory, Sink: hdfs）和node03 Agent（Source: avro, Channel: memory, Sink: hdfs），中间标注“failover”。

画面2：
- 架构图更新：node01 Agent标注“100M”，node02 Agent标注“50M”，node03 Agent标注“50M”，中间标注“failover”和“load balance”。
- 底部显示三个远程桌面窗口：node02、node01、node03。

画面3：
- PPT标题：Node01.md - Typora。
- 内容：Step 5: 配置启动，包含角色分配、配置文件、负载均衡、测试等步骤。
- 代码片段：
  ```
  a1.sinks.k1.port = 52020
  # set sink2
  a1.sinks.k2.channel = c1
  a1.sinks.k2.type = avro
  a1.sinks.k2.hostame = node03
  a1.sinks.k2.port = 52020
  #set sink group
  a1.sinkgroups.g1.sinks = k1 k2
  #set failover
  a1.sinkgroups.g1.processor.type = load_balance
  a1.sinkgroups.g1.processor.backoff = true
  a1.sinkgroups.g1.processor.selector = round_robin
  a1.sinkgroups.g1.processor.selector.maxTimeOut=10000
  ```

画面4：
- 代码片段：
  ```
  #agent name
  a1.channels = c1
  a1.sources = r1
  a1.sinks = k1 k2
  #set grupo
  a1.sinkgroups = g1
  #set channel
  a1.channels.c1.type = memory
  a1.channels.c1.capacity = 1000
  ```

画面5：
- 代码片段：
  ```
  #set channel
  a1.channels.c1.type = memory
  a1.channels.c1.capacity = 1000
  a1.channels.c1.transactionCapacity = 100
  a1.sources.r1.channels = c1
  a1.sources.r1.type = exec
  a1.sources.r1.command = tail -F /export/servers/taillogs/access_log
  # set sink1
  a1.sinks.k1.channel = c1
  a1.sinks.k1.type = avro
  a1.sinks.k1.hostname = node02
  a1.sinks.k1.port = 52020
  # set sink2
  a1.sinks.k2.channel = c1
  ```

画面6：
- 代码片段：
  ```
  a1.sources.r1.channels = c1
  a1.sources.r1.type = exec
  a1.sources.r1.command = tail -F /export/servers/taillogs/access_log
  # set sink1
  a1.sinks.k1.channel = c1
  a1.sinks.k1.type = avro
  a1.sinks.k1.hostname = node02
  a1.sinks.k1.port = 52020
  # set sink2
  a1.sinks.k2.channel = c1
  a1.sinks.k2.type = avro
  a1.sinks.k2.hostname = node03
  a1.sinks.k2.port = 52020
  #set sink group
  a1.sinkgroups.g1.sinks = k1 k2
  #set failover
  ```

画面7：
- 代码片段：
  ```
  a1.sinks.k1.type = avro
  a1.sinks.k1.hostname = node02
  a1.sinks.k1.port = 52020
  # set sink2
  a1.sinks.k2.channel = c1
  a1.sinks.k2.type = avro
  a1.sinks.k2.hostname = node03
  a1.sinks.k2.port = 52020
  #set sink group
  a1.sinkgroups.g1.sinks = k1 k2
  #set failover
  a1.sinkgroups.g1.processor.type = load_balance
  a1.sinkgroups.g1.processor.backoff = true
  a1.sinkgroups.g1.processor.selector = round_robin
  a1.sinkgroups.g1.processor.selector.maxTimeOut=10000
  ```
- 底部提示："[load_balancer_client.conf] [New] 36L, 819C written"。
- 底部显示："[root@node01 conf]# "。
- 右下角弹出窗口：Node01.md - Typora，显示代码内容。

