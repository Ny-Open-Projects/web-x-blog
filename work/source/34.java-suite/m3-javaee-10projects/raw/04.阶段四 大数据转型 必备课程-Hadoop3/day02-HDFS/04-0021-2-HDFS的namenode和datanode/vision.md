# 画面线理解：2-HDFS的namenode和datanode

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\2-HDFS的namenode和datanode【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:18, 00:40, 01:18, 01:25, 02:14, 02:54, 07:06, 08:10, 08:13, 08:15, 08:26, 08:28, 08:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:52:08

1) 这一组画面整体在讲什么（一句话）：
讲解 HDFS（Hadoop Distributed File System）的设计目标、历史背景、系统架构及其核心组件（NameNode、DataNode）的工作机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 HDFS 的定义、设计目标和历史背景，包括 Doug Cutting 创建 HDFS 的背景故事。
画面2：空白画面，无内容。
画面3：展示 HDFS 的数据存储架构图，Client 访问 /a.txt 文件，该文件分布在 node01、node02、node03 三个节点上，每个节点存储 1T 数据，总容量 3T。
画面4：展示 HDFS 的架构图，包含 HDFS Client、NameNode、Secondary NameNode，以及 DataNode 节点，标注了心跳、负载均衡、复制等机制。
画面5：与画面3内容相同，为 HDFS 数据存储架构图。
画面6：与画面4内容相同，为 HDFS 架构图，展示 NameNode、DataNode、Secondary NameNode 之间的关系。
画面7：展示 HDFS 架构图的详细版本，包含 HDFS Client、NameNode、Secondary NameNode、DataNode，以及数据块（Block）和元数据（Metadata）的存储结构。
画面8：展示 NameNode 与 DataNode 之间的关系图，标注 NameNode 负责管理元数据和监控 DataNode 状态，DataNode 负责存储具体数据。
画面9：在 node01 节点的终端中，列出 Hadoop 集群中各服务的默认端口，包括 SecondaryNameNode (2673)、NameNode (2345)、NodeManager (3242)、JobHistoryServer (3675)、ResourceManager (3101)、DataNode (2494)、QuorumPeerMain (2030)。
画面10：与画面9内容相同，为 node01 节点的终端界面，显示 Hadoop 服务端口列表。
画面11：与画面9、10内容相同，为 node01 节点的终端界面，显示 Hadoop 服务端口列表。
画面12：在 node02 节点的终端中，显示登录信息和 Hadoop 服务端口列表，包括 QuorumPeerMain (2032)、DataNode (2471)、NodeManager (2332)。
画面13：在 node03 节点的终端中，执行命令启动 ZooKeeper 服务，并显示服务启动日志，包括配置文件路径 /export/servers/zookeeper-3.4.9/bin/../conf/zoo.cfg。
画面14：展示 NameNode 与 DataNode 之间的关系图，标注 NameNode 负责管理元数据和监控 DataNode 状态，DataNode 负责存储具体数据，且数据存储在磁盘上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面9、10、11、12、13 中的命令和输出：
```
[root@node01 ~]# jps
2673 SecondaryNameNode
2345 NameNode
3242 NodeManager
3675 JobHistoryServer
3101 ResourceManager
2494 DataNode
2030 QuorumPeerMain
[root@node01 ~]#

[root@node02 ~]# jps
2032 QuorumPeerMain
2332 NodeManager
2471 DataNode
2030 QuorumPeerMain
[root@node02 ~]#

[root@node03 ~]# /export/servers/zookeeper-3.4.9/bin/zkServer.sh start
ZooKeeper JMX enabled by default
Using config: /export/servers/zookeeper-3.4.9/bin/../conf/zoo.cfg
Starting zookeeper ... STARTED
[root@node03 ~]# jps
2030 QuorumPeerMain
2337 jps
2247 NodeManager
2124 DataNode
2030 QuorumPeerMain
[root@node03 ~]#
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：架构图结构：
- Client → /a.txt (HDFS系统)
- /a.txt (HDFS系统) → node01 (1T)
- /a.txt (HDFS系统) → node02 (1T)
- /a.txt (HDFS系统) → node03 (1T)

画面4：架构图结构：
- HDFS Client → NameNode
- NameNode → DataNode (多个)
- Secondary NameNode → NameNode
- DataNode → HDFS Client (通过心跳、负载均衡、复制等机制)

画面7：架构图结构：
- HDFS Client → NameNode
- NameNode → DataNode (多个)
- Secondary NameNode → NameNode
- DataNode → HDFS Client (通过心跳、负载均衡、复制等机制)
- NameNode → Metadata (Name, replicas, ...)
- DataNode → Block (data)
- Client → Read (Metadata) → DataNode (Block)
- Client → Write (Metadata) → NameNode → DataNode (Block)

画面8：架构图结构：
- namenode → datanode (多个)
- namenode → datanode (多个)
- namenode → datanode (多个)
- namenode → datanode (多个)

画面14：架构图结构：
- namenode → datanode (多个)
- namenode → datanode (多个)
- namenode → datanode (多个)
- namenode → datanode (多个)

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
