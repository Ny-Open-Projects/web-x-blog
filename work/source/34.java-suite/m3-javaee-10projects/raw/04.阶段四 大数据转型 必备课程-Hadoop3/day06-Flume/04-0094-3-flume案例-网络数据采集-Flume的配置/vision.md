# 画面线理解：3-flume案例-网络数据采集-Flume的配置

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\3-flume案例-网络数据采集-Flume的配置【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:27, 01:26, 02:48, 03:58, 04:06, 04:18, 05:46, 07:39, 07:57, 08:57, 09:54, 10:06, 10:15, 10:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 07:13:20

1) 这一组画面整体在讲什么（一句话）：
演示如何配置 Apache Flume 的 netcat logger 示例，包括编写配置文件、查看官方文档和理解 Flume 架构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Flume 配置文件 netcat-logger.conf 的开头部分，定义了 agent 中的 source、sink 和 channel 名称。
画面 2: 展示了配置文件中 source 组件的配置，包括类型为 netcat、绑定地址和端口。
画面 3: 展示了配置文件中 sink 组件的配置，类型为 logger。
画面 4: 跳转到 Apache Flume 官方 Confluence 页面，显示“Getting Started”部分。
画面 5: 在 Confluence 页面中滚动，显示了 Flume NG 的 Channel 类型列表，包括 memory、file、jdbc 等。
画面 6: 在 Confluence 页面中继续滚动，显示了 Flume NG 的 Source 类型列表，包括 exec、netcat、seq 等。
画面 7: 展示了配置文件中 channel 组件的配置，类型为 memory，容量和事务容量。
画面 8: 展示了配置文件中 source 和 sink 之间的连接关系，即 source.r1.channels = c1。
画面 9: 展示了 Flume 架构图，包含 Source、Channel、Sink 三个组件，以及它们的配置参数。
画面 10: 在架构图中添加了 sink 的配置参数。
画面 11: 展示了在终端中执行命令，准备启动 Flume。
画面 12: 展示了配置文件中 source、sink 和 channel 的配置部分。
画面 13: 展示了终端中执行的命令，用于启动 Flume。
画面 14: 展示了配置文件中 source、sink 和 channel 的配置部分。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
# 定义这个agent中各组件的名字
a1.sources = r1
a1.sinks = k1
a1.channels = c1

# 描述和配置source组件: r1
a1.sources.r1.type = netcat
a1.sources.r1.bind = 192.168.174.120
a1.sources.r1.port = 44444

# 描述和配置sink组件: k1
a1.sinks.k1.type = logger

# 描述和配置channel组件, 此处使用是内存存储的方式
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100

# 描述和配置source channel sink之间的连接关系
a1.sources.r1.channels = c1
a1.sinks.k1.channel = c1
```

画面 2:
```
export JAVA_HOME=/export/servers/jdk1.8.0_141
```

画面 3:
```
# 描述和配置sink组件: k1
a1.sinks.k1.type = logger
```

画面 7:
```
# 描述和配置channel组件, 此处使用是内存存储的方式
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100
```

画面 8:
```
# 描述和配置source channel sink之间的连接关系
a1.sources.r1.channels = c1
a1.sinks.k1.channel = c1
```

画面 9:
```
1: 从哪里采集 Source
2: 对采集的数据进行临时存储 Channel
3: 将采集的数据存入存储系统 Sink

Agent

a1.sources.r1.type = netcat
a1.sources.r1.bind = 192.168.174.120
a1.sources.r1.port = 44444

a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100
```

画面 10:
```
a1.sinks.k1.type = logger
```

画面 11:
```
# 描述和配置source channel sink之间的连接关系
a1.sources.r1.channels = c1
a1.sinks.k1.channel = c1
```

画面 13:
```
a1.sinks = k1
a1.channels = c1
# 描述和配置source组件: r1
a1.sources.r1.type = netcat
a1.sources.r1.bind = 192.168.174.120
a1.sources.r1.port = 44444
# 描述和配置sink组件: k1
a1.sinks.k1.type = logger
# 描述和配置channel组件, 此处使用是内存存储的方式
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100
# 描述和配置source channel sink之间的连接关系
a1.sources.r1.channels = c1
a1.sinks.k1.channel = c1
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 9: 架构图显示了 Source、Channel、Sink 三个组件，Source 指向 Channel，Channel 指向 Sink。
画面 5: 表格列出了 Channel 类型，包括 memory、file、jdbc 等。
画面 6: 表格列出了 Source 类型，包括 exec、netcat、seq 等。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
