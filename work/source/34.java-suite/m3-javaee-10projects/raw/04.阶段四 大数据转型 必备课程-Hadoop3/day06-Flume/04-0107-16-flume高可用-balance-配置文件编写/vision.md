# 画面线理解：16-flume高可用-balance-配置文件编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\16-flume高可用-balance-配置文件编写【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 02:34, 02:54, 03:10, 04:17, 04:36, 05:55, 06:12, 06:27, 07:27, 07:55, 08:07, 08:24, 08:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 08:20:19

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
