# 画面线理解：14-flume高可用-failover-配置文件编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\14-flume高可用-failover-配置文件编写【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:41, 01:34, 02:06, 02:26, 03:42, 04:05, 05:04, 06:27, 07:17, 07:36, 08:19, 08:36, 09:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 08:10:06

1) 这一组画面整体在讲什么（一句话）：
演示如何在多节点环境中配置Flume NG Agent，实现日志数据的采集、传输与故障转移。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1: 展示了Flume NG Agent配置文档，说明将node03的Flume安装包和日志目录复制到node01，并配置agent.conf。
画面2: 展示了SecureCRT中Flume的文件传输进度，显示多个HTML文件已传输完成。
画面3: 与画面1内容相同，展示Flume配置文档。
画面4: 展示了在Typora中编辑agent.conf文件，同时SecureCRT中显示了文件传输进度。
画面5: SecureCRT界面空白，准备输入命令。
画面6: SecureCRT中显示了agent.conf文件的配置内容，包括source、channel、sink的设置。
画面7: SecureCRT界面空白，准备输入命令。
画面8: SecureCRT中显示了agent.conf文件的配置内容，继续配置sink1和sink2。
画面9: SecureCRT中显示了agent.conf文件的配置内容，配置了failover机制。
画面10: SecureCRT中显示了在node02上执行命令，将taillogs目录复制到node01。
画面11: SecureCRT中显示了agent.conf文件的配置内容，配置了sink写入HDFS。
画面12: SecureCRT中显示了在node03上执行Flume服务的停止命令。
画面13: 展示了在Typora中编辑collector.conf文件，配置了source、channel、sink。
画面14: 展示了Flume架构图，说明node01采集数据并发送到node02或node03，实现failover。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```
cd /export/servers
scp -r apache-flume-1.8.0-bin/ node01:$PWD
scp -r shells/ taillogs/ node01:$PWD
```
画面4:
```
#agent1 name
agent1.channels = c1
agent1.sources = r1
agent1.sinks = k1 k2
```
画面6:
```
agent1.sources.r1.channels = c1
agent1.sources.r1.type = exec
agent1.sources.r1.command = tail -F /export/servers/taillogs/access_log
```
画面8:
```
agent1.sinks.k1.type = avro
agent1.sinks.k1.hostname = node02
agent1.sinks.k1.port = 52020
agent1.sinks.k2.type = avro
agent1.sinks.k2.hostname = node03
agent1.sinks.k2.port = 52020
```
画面9:
```
agent1.sinkgroups.g1.processor.type = failover
agent1.sinkgroups.g1.processor.priority.k1 = 10
agent1.sinkgroups.g1.processor.priority.k2 = 1
agent1.sinkgroups.g1.processor.maxpenalty = 10000
```
画面10:
```
[root@node02 servers]# cd taillogs
[root@node02 taillogs]# ls
access_log tail-file.sh
[root@node02 taillogs]# cd ..
[root@node02 servers]# scp -r taillogs/ node01:$PWD
```
画面11:
```
a1.sinks.k1.type=hdfs
a1.sinks.k1.hdfs.path = hdfs://node01:8020/flume/failover/
a1.sinks.k1.hdfs.fileType=DataStream
a1.sinks.k1.hdfs.writeFormat=TEXT
a1.sinks.k1.hdfs.rollInterval=10
a1.sinks.k1.channel=c1
```
画面13:
```
#set Agent name
a1.sources = r1
a1.channels = c1
a1.sinks = k1
```
画面14:
```
需求:
1:node01去采集一个文件的新增数据
2:node01采集数据之后发送给node02
或node03的flume的Agent
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14: 架构图显示了node01的Agent指向node02和node03的Agent，标注了failover。node01的Agent配置为Source: exec, Channel: memory, Sink: avro。node02和node03的Agent配置为Source: avro, Channel: memory, Sink: hdfs。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
