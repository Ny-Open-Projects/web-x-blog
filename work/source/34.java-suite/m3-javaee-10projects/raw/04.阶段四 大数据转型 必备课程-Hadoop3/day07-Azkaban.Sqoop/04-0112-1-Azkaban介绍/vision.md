# 画面线理解：1-Azkaban介绍

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\1-Azkaban介绍【海量资源尽在 ubkz.com】.mp4
- 抽帧：12 帧 @ 01:26, 03:45, 03:47, 04:26, 04:27, 05:12, 05:18, 05:19, 05:21, 05:31, 05:45, 06:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 08:46:35

1) 这一组画面整体在讲什么（一句话）：
介绍Azkaban工作流调度系统，包括其必要性、常见调度工具对比以及Azkaban本身的功能和特性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 标题：Day 07，1. Azkaban介绍，1.1. 为什么需要Azkaban。
- 内容：一个完整的数据分系统通常是由大量任务单元组成，包括shell脚本程序、java程序、mapreduce程序、hive脚本等。
- 举例：某个业务系统每天产生20G原始数据，需要通过Hadoop同步到HDFS，借助MapReduce转换，存储到Hive表，对多表进行JOIN处理，进行各种统计分析，最后将结果同步到业务系统。

画面2：
- 内容：处理步骤如下所示：
  1. 通过Hadoop先将原始数据同步到HDFS上；
  2. 借助MapReduce计算框架对原始数据进行转换，生成的数据以分表的形式存储到多张Hive表中；
  3. 需要对Hive中多个表的数据进行JOIN处理，得到一个明细数据Hive大表；
  4. 将明细数据进行各种统计分析，得到报表基本信息；
  5. 需要将统计分析得到的结果数据同步到业务系统中，供业务端使用。

画面3：
- 标题：1.2. 常见工作流调度系统。
- 内容：简单的任务调度：直接使用linux的crontab来定义；复杂的任务调度：在hadoop领域，常见的工作流调度器有Oozie, Azkaban, Cascading等。

画面4：
- 标题：1.3. 各种调度工具特性对比。
- 内容：下面的表格对上述四种hadoop工作流调度器的关键特性进行了比较，尽管这些工作流调度器能够解决的需求场景基本一致，但在设计理念、目标用户、应用场景等方面还是存在显著的区别，在做技术选型的时候，可以提供参考。

画面5：
- 标题：1.3. 各种调度工具特性对比。
- 内容：表格开始显示，特性包括：Hamake, Oozie, Azkaban, Cascading。
- 表格列：工作流描述语言、依赖机制、是否需要web容器、进度跟踪、Hadoop job调度支持、运行模式、Pig支持、事件通知、需要安装、支持的hadoop版本、重试支持、运行任意命令、Amazon EMR支持。

画面6：
- 标题：1.3. 各种调度工具特性对比。
- 内容：表格继续显示，工作流描述语言：Hamake为XML，Oozie为XML (xPDL based)，Azkaban为text file with key/value pairs，Cascading为Java API。
- 依赖机制：Hamake为data-driven，Oozie为explicit，Azkaban为explicit，Cascading为explicit。

画面7：
- 标题：1.3. 各种调度工具特性对比。
- 内容：表格继续显示，是否需要web容器：Hamake为No，Oozie为Yes，Azkaban为Yes，Cascading为No。
- 进度跟踪：Hamake为console/log messages，Oozie为web page，Azkaban为web page，Cascading为Java API。

画面8：
- 标题：1.3. 各种调度工具特性对比。
- 内容：表格继续显示，Hadoop job调度支持：Hamake为no，Oozie为yes，Azkaban为yes，Cascading为yes。
- 运行模式：Hamake为command line utility，Oozie为daemon，Azkaban为daemon，Cascading为API。

画面9：
- 标题：1.5. Azkaban 是什么。
- 内容：Azkaban是由LinkedIn开源的一个批量工作流任务调度器。用于在一个工作流内以一个特定的顺序运行一组工作和流程。Azkaban定义了一种KV文件(properties)格式来建立任务之间的依赖关系，并提供一个易于使用的web用户界面维护和跟踪你的工作流。
- 功能特点：Web用户界面、基于时间的执行任务、方便上传工作流、方便设置任务之间的关系、工作流和任务的日志记录和审计。

画面10：
- 标题：1.5. Azkaban 是什么。
- 内容：表格继续显示，Pig支持：Hamake为yes，Oozie为yes，Azkaban为yes，Cascading为yes。
- 事件通知：Hamake为no，Oozie为no，Azkaban为no，Cascading为yes。
- 需要安装：Hamake为no，Oozie为yes，Azkaban为yes，Cascading为no。

画面11：
- 标题：1.5. Azkaban 是什么。
- 内容：表格继续显示，支持的hadoop版本：Hamake为0.18+，Oozie为0.20+，Azkaban为currently unknown，Cascading为0.18+。
- 重试支持：Hamake为no，Oozie为workflownode，Azkaban为yes，Cascading为yes。
- 运行任意命令：Hamake为yes，Oozie为yes，Azkaban为yes，Cascading为yes。
- Amazon EMR支持：Hamake为yes，Oozie为no，Azkaban为currently unknown，Cascading为yes。

画面12：
- 标题：2. 安装。
- 内容：页面切换到“2. 安装”部分，但具体内容未显示。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- PPT标题：
  - Day 07
  - 1. Azkaban介绍
  - 1.1. 为什么需要Azkaban
  - 1.2. 常见工作流调度系统
  - 1.3. 各种调度工具特性对比
  - 1.5. Azkaban 是什么
  - 2. 安装

- 表格数据：
  1.3. 各种调度工具特性对比：
  | 特性 | Hamake | Oozie | Azkaban | Cascading |
  | :--- | :--- | :--- | :--- | :--- |
  | 工作流描述语言 | XML | XML (xPDL based) | text file with key/value pairs | Java API |
  | 依赖机制 | data-driven | explicit | explicit | explicit |
  | 是否需要web容器 | No | Yes | Yes | No |
  | 进度跟踪 | console/log messages | web page | web page | Java API |
  | Hadoop job调度支持 | no | yes | yes | yes |
  | 运行模式 | command line utility | daemon | daemon | API |
  | Pig支持 | yes | yes | yes | yes |
  | 事件通知 | no | no | no | yes |
  | 需要安装 | no | yes | yes | no |
  | 支持的hadoop版本 | 0.18+ | 0.20+ | currently unknown | 0.18+ |
  | 重试支持 | no | workflownode | yes | yes |
  | 运行任意命令 | yes | yes | yes | yes |
  | Amazon EMR支持 | yes | no | currently unknown | yes |

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
