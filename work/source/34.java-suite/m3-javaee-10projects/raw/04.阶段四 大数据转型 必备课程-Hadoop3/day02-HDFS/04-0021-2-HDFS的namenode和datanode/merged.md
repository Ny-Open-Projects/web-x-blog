# 2-HDFS的namenode和datanode

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\2-HDFS的namenode和datanode【海量资源尽在 ubkz.com】.mp4
- 时长 8分39秒（音频 519s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 我们来继续看这个HDFS那么HDFS是一个分布式文件存储系统那它的设计目标是什么呢我在这里给大家列了三点第一点它可以通过呢多个廉价的计算机集群来实现数据的一个存储看我刚才这张图那么我们要实现一个大数据的存储我们不需要买一台很牛的一个计算机我们只需要买多台廉价的计算机把它整合
[00:28] 就可以解决这个存储问题这是第一个第二个它可以呢维护多个数据的副本在发生故障的时候来保证数据的可靠性这个呢我可以先给大家提一下待会我们再详细讲解比如说呢我在这里把文件分成了三块每一块呢放在不同的主机上现在就有个问题假如说某一台机子突然挂掉了当机了那是不是这个数据就这个块是不是就丢失了
[00:56] 就不能保证这个数据的完整性不过大家不用担心我们的HDFS很强大的它就可以解决这个问题怎么解决呢它可以把每一个块存多个副本相当于拷贝多次即使你挂机了那么也不影响它的数据完整性这是第二个问题第三个问题它可以很好的解决大数据的数据扩展问题什么意思呢
[01:25] 比如说我这三台机子组成的一个集群呢这个分布式文件系统空间不够用了这个时候怎么去处理呢很简单我只需要呢再买一台计算机OK这个计算机呢比如说还是一个T的一个存储空间比如说我写的是Node04然后呢这里边呢我还是一个T然后呢我只需要呢把我这台计算机重新加在了这个集群里边
[02:01] 那么这个时候相当于我的整个HDFS系统是不是进行了扩容而且非常的方便代价也非常的小好那么咱们来看一下HDFS一个简单的历史这个HDFS最初是这个人在做这个爬虫的时候遇到一个数据的一个存储问题后来谷歌发表了三篇论文其中有一篇叫GFS也就是说谷歌的一个文件系统
[02:32] 那这个呢其实就是我们HDFS它的一个前身OK那么后来呢这个叫DunkChanting它呢就根据GFS来做出一个新的文件系统叫HDFS好 这才是一个历史也就是它来源于谷歌的一篇论文那么咱们再看一下HDFS的一个架构OK这个架构呢我也给大家画一张图我们来看一下来 我们来打开华东软件来 我们来看一下
[03:02] 这个HDFS首先它是有很多的主机组成的有计算机也就是主机组成的比如说这是一台计算机这是一台计算机这是一台计算机这些计算机它们最终要组成一个整体在我们HDFS里边有一个进程专门来管理每一个主机的磁盘这个叫DataNode
[03:37] 那么这里边呢还有两个Data NodeOK他们分别管管理每台主机的一个磁盘那么这些Data Node最后要进行一个整合整合成一个完整的一个文件系统那谁去管理这些Data Node呢我们有一个更牛的一个大哥这个大哥呢叫做Name Node那这个Name Node呢你认为他就是管理这些Data NodeOK那么他呢
[04:10] 管理它呢被它管理OK也被它管理OK那好了那我们接下来看我们认为NameNode就是我们所谓的主节点而这个DataNode呢就是我们所谓的从节点那NameNode具体干什么事情呢你可以这样理解NameNode它的作用呢第一个非常重要的作用就是管理我们的原数据
[04:42] 管理原数据什么意思呢什么叫原数据比如说呢我在整个HDFS系统里面呢存了一个文件这个文件呢还是A.TT那么这个A.TT呢它这个原数据比如说这个文件的名字呀这个文件的大小呀这个文件的权限呀还有这个文件在哪些DataNode里面存储啊那这些信息就是由NameNode来管理
[05:11] 这个原数据是非常重要的那么这些原数据呢如果一旦丢了就相当于你这个A.TT呢再也找不着了所以说原数据非常重要OK这是NameNode还有呢这个NameNode呢还会干一件事负责呢监控监控DataNode的状态这个什么意思呢你比如说这些DataNode很多
[05:42] 有可能有一些机械的原因或者说一些硬件的原因那么这些DataNode挂掉了 当机了那这个时候它NumNode需要去维护这些故障的节点然后实时的监控这些节点的一个存活状态这是一个NumNode干的第二件事情好 那么了解了这个之后咱们再说DataNode那每一个DataNode干什么事情呢它非常简单DataNode负责
[06:12] 存储具体的数据好具体的数据也就是说我去存一个文件呢那数据到底在哪里存就是在DataNode这个节点上存它呢负责提供磁盘OK那么还有呢DataNode还要干一件事情它呢DataNode和Nimnode之间有一个心跳机制什么意思呢就是说DataNode会隔一段时间呢向Nimnode报告自己的状态
[06:46] 还有报告自己呢它的这个里面的文件存储的状况如果隔一段时间呢DataNode没有向NameNode汇报那注意这个时候呢有一个机制就是NameNode会认为呢这个DataNode已经当机了OK这是它一个机制问题这里还有一个问题那么NameNode存数据的位置和这个DataNode存数据的位置是不一样的什么意思呢我们再加一条这个NameNode呢
[07:16] 它保存的是原数据也就是管理性的数据它的数据呢一般是存放在内存中数据存放在内存中也就是说呢它的数据呢存放在内存中万一呢这个机子挂掉了它的数据呢有可能就丢失了存在这边的问题那咱再看DataNodeDataNode呢它是存放具体数据的它的数据呢是存放在磁盘上的
[07:49] 好这是它两个的一个主要的一个特点记着Name node我们认为是主节点而Data node是从节点那再看一下我们之前搭的一个集群来看那么在搭集群的时候呢我们来GPS一下你会发现第一台呢它这个机子呢它有一个Name node那这个机子呢就是主节点那你看它还有一个Data node它又是一个从节点这里边我们并没有搭高可用的
[08:17] 所以说我们Name node和Data node这个第一个机子都有咱们看看第二台这个第二台它只有什么Data node没有Name node它就是一个重解点再看第三台第三台它也是一个Data node它也是一个重解点OK这是它们之间的关系我们先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面13：在 node03 节点的终端中，执行命令启动 ZooKeeper 服务，并显示服务启动日志，包括配置文件路径 /export/servers/ZooKeeper-3.4.9/bin/../conf/zoo.cfg。
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

[root@node03 ~]# /export/servers/ZooKeeper-3.4.9/bin/zkServer.sh start
ZooKeeper JMX enabled by default
Using config: /export/servers/ZooKeeper-3.4.9/bin/../conf/zoo.cfg
Starting ZooKeeper ... STARTED
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

