# 画面线理解：17-flume高可用-balance-测试运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\17-flume高可用-balance-测试运行【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:33, 00:39, 00:47, 00:52, 00:59, 01:02, 01:15, 01:21, 01:28, 01:59, 02:21, 02:30, 02:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 08:26:31

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
