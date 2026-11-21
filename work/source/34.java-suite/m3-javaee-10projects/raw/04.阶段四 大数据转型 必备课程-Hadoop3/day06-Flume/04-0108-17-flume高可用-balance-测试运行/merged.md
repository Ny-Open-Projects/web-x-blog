# 17-flume高可用-balance-测试运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\17-flume高可用-balance-测试运行【海量资源尽在 ubkz.com】.mp4
- 时长 2分58秒（音频 179s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在配置好之后接下来我们来启动一下好 大概我们讲一我们先呢在三台主机上启动Floom服务启动的时候我们先启动哪一台呢我们肯定不能启动Node01对吧那么Node02或者Node03都可以启动来 我们先启动Node03在Node03上呢进到这个主进到这个我们要进到这个主模录下面这地方写错了应该是主模录好 这一都是主模录
[00:31] 好那我们来直接来启动在node03上进到上一集主目录下面来运行这个走一下好稍等它已经启动了那接下来呢我们再启动node02吧把这个呢也复制过来走好启动一下回到我们的主目录启动好启动完了好启动完了之后呢相当于呢我们的这个接收数据的节点
[01:09] 都已经启动了启动完之后我们再去启动发送数据的节点也就是node01我们来看在这里呢我们来启动node01好打开node01回到上一阶在这里走好node01也启动了好也启动了启动了之后呢咱们还是以前和以前一样你得向那个文件的写数据然后node01就可以监测到那在这里呢我们启动那个脚本吧
[01:43] 在export Service下面有个tail logs这里边有个叫share脚本sh tail share走来我们让它呢去向这个文件写数据那么node01呢就能监测到稍等一下看看它能不能收到来我们看那个node02和node03有没有变化走你看node02呢它已经收到了数据了你看event hide body这是它的一个
[02:14] 我们收到数据的一些字节的一些描述看看node03看看node03你看node03是不是也收到数据了你看node02和node03都同时收到数据了这个地方呢你稍等一下你看这地方变蓝色这个颜色变蓝色呀表示他正在收到数据这个也变蓝色了OK这个说明了他们俩同时收到数据不是同时啊是轮循的方式就是你收一包我收一包那这样子的话呢
[02:43] 我们就可以做到负载均衡保证了每一台主机呢它的压力是均等的OK那么这个就是我们Flume的一个高可用机制中的负载均衡那我们呢就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在多节点环境中配置并启动Flume服务，以实现数据从node02到node03的传输。

2) 按时间顺序列出每张画面的要点：
画面1：
- 标题：第四步：准备启动flume服务
- 内容：展示在Node03、Node02、Node01上启动Flume服务的命令，分别对应配置文件load_balancer_server.conf和load_balancer_client.conf。
- 命令：
  cd /export/servers/apache-flume-1.8.0-bin/conf
  bin/flume-ng agent -n a1 -c conf -f conf/load_balancer_server.conf -Dflume.root.logger=DEBUG,console
  cd /export/servers/apache-flume-1.8.0-bin/conf
  bin/flume-ng agent -n a1 -c conf -f conf/load_balancer_server.conf -Dflume.root.logger=DEBUG,console
  cd /export/servers/apache-flume-1.8.0-bin/conf
  bin/flume-ng agent -n a1 -c conf -f conf/load_balancer_client.conf -Dflume.root.logger=DEBUG,console

画面2：
- 与画面1内容相同，仅在Node02的命令行中添加了“shell”按钮，用于切换到终端。

画面3：
- 展示在Node03上执行命令后，Flume环境配置脚本加载成功，提示包含Hadoop库以支持HDFS访问。

画面4：
- 展示在Node02上配置文件的内容，包括源和目标的配置。
- 配置内容：
  a1.sources = r1
  a1.sinks = k1
  a1.channels = c1
  # Describe/configure the source
  a1.sources.r1.type = avro
  a1.sources.r1.channels = c1
  a1.sources.r1.bind = node02
  a1.sources.r1.port = 52020
  # Describe the sink
  a1.sinks.k1.type = logger
  # Use a channel which buffers events in memory
  "load_balancer_server.conf" [New] 25L, 521C written

画面5：
- 标题：第四步：准备启动flume服务
- 内容：展示在Node03、Node02、Node01上启动Flume服务的命令，分别对应配置文件load_balancer_server.conf和load_balancer_client.conf。
- 命令：
  cd /export/servers/apache-flume-1.8.0-bin/conf
  bin/flume-ng agent -n a1 -c conf -f conf/load_balancer_server.conf -Dflume.root.logger=DEBUG,console
  cd /export/servers/apache-flume-1.8.0-bin/conf
  bin/flume-ng agent -n a1 -c conf -f conf/load_balancer_server.conf -Dflume.root.logger=DEBUG,console
  cd /export/servers/apache-flume-1.8.0-bin/conf
  bin/flume-ng agent -n a1 -c conf -f conf/load_balancer_client.conf -Dflume.root.logger=DEBUG,console
- 标题：第五步：node01服务器运行脚本产生数据
- 命令：
  cd /export/servers/shells
  sh tail-file.sh

画面6：
- 展示在Node02上执行Flume命令时，提示“-bash: bin/flume-ng: No such file or directory”，表明Flume命令未找到。

画面7：
- 展示Flume服务启动后的日志，包括组件启动、源和目标成功启动等信息。
- 日志内容：
  registered new MBean.
  p.start(MonitoredCounterGroup.java:95) Component type: CHANNEL, name: c1 started
  (config-file-poller-0) [INFO - org.apache.flume.node.Application.startAllComponents(Application.java:182)] Starting Sink k1
  2019-05-11 10:43:00,804 (lifecycleSupervisor-1-3) [INFO - org.apache.flume.source.AvroSource.java:234] Starting Source r1: [bindAddress: node02, port: 52020]
  2019-05-11 10:43:00,816 (SinkRunner-PollingSinkProcessor.java:140) Polling sink runner starting
  2019-05-11 10:43:01,324 (lifecycleSupervisor-1-3) [INFO - org.apache.flume.source.AvroSource.java:260] Avro source r1 started.

