# 画面线理解：16-hadoop的架构

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\16-hadoop的架构【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:38, 03:21, 04:23, 04:49, 05:30, 05:54, 06:22, 08:32, 09:42, 10:45, 16:16, 18:14, 18:25, 18:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:38:44

1) 这一组画面整体在讲什么（一句话）：
讲解Hadoop的起源、生态体系以及1.x和2.x版本的架构模型。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 内容：Hadoop介绍，包含其起源（Nutch）、HDFS和MapReduce的提出，以及Hadoop成为Apache项目的时间点。
- 图表：Hadoop生态图，中心为“大数据hadoop生态圈”，向外辐射出Hadoop、HBase、Hive、Flume、Storm、Spark、Kafka、Elasticsearch、Flink、Druid、Pig、Phoenix、Impala等组件。

画面2：
- 内容：Hadoop生态图，与画面1相同，但鼠标指针指向“HBase”组件。

画面3：
- 内容：浏览器打开Google搜索主页，下方显示多个快捷方式，包括“Ooze Web Console”、“Namenode information”、“Browsing HDFS”等。

画面4：
- 内容：Apache Hadoop官网的文件列表页面，显示了多个Hadoop版本的下载链接，如hadoop-1.0.3、hadoop-1.1.2、hadoop-2.0.0等。

画面5：
- 内容：介绍免费开源版HortonWorks和软件收费版ClouderaManager，包含各自的官网链接。
- 文本：免费开源版hortonWorks: https://hortonworks.com/；软件收费版ClouderaManager: https://www.cloudera.com/。

画面6：
- 内容：Hadoop架构模型介绍，展示1.x版本架构图，包含NameNode、Secondary NameNode、DataNode、JobTracker、TaskTracker等组件。
- 文本：文件系统核心模块：NameNode、secondary NameNode、DataNode；数据计算核心模块：JobTracker、TaskTracker。

画面7：
- 内容：在图片编辑软件中查看Hadoop 1.x架构图，软件界面显示绘图工具栏。

画面8：
- 内容：Hadoop 1.x架构图，与画面6相同，但鼠标指针指向“JobTracker”组件。

画面9：
- 内容：Hadoop 2.x架构模型介绍，展示第一种架构模型：NameNode与ResourceManager单节点架构模型。
- 文本：文件系统核心模块：NameNode、secondary NameNode、DataNode；数据计算核心模块：JobTracker、TaskTracker。

画面10：
- 内容：电脑桌面，显示“黑马程序员”和“博学谷”的标志，以及多个未命名的文档预览。

画面11：
- 内容：Hadoop 2.x架构模型介绍，展示第二种架构模型：NameNode单节点与ResourceManager高可用架构模型。
- 文本：文件系统核心模块：NameNode、secondary NameNode、DataNode；数据计算核心模块：ResourceManager、NodeManager。

画面12：
- 内容：Hadoop 2.x架构模型介绍，展示第四种架构模型：NameNode与ResourceManager高可用架构模型。
- 文本：文件系统核心模块：NameNode、secondary NameNode、DataNode、JournalNode；数据计算核心模块：ResourceManager、NodeManager。

画面13：
- 内容：Hadoop 2.x架构模型介绍，展示第二种架构模型：NameNode单节点与ResourceManager高可用架构模型。
- 文本：文件系统核心模块：NameNode、secondary NameNode、DataNode、JournalNode；数据计算核心模块：ResourceManager、NodeManager。

画面14：
- 内容：Hadoop安装章节，标题为“8.2 Hadoop的安装”，并列出第一点“1. 下载并解压”。
- 文本：文件系统核心模块：NameNode、secondary NameNode、DataNode、JournalNode；数据计算核心模块：ResourceManager、NodeManager。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- 画面6架构图：NameNode指向DataNode，Secondary NameNode指向DataNode，JobTracker指向TaskTracker。
- 画面9架构图：NameNode指向DataNode，ResourceManager指向NodeManager。
- 画面11架构图：NameNode指向DataNode，ResourceManager指向NodeManager。
- 画面12架构图：NameNode指向DataNode，ResourceManager指向NodeManager，JournalNode指向NameNode。
- 画面13架构图：NameNode指向DataNode，ResourceManager指向NodeManager。
- 画面14无架构图。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
