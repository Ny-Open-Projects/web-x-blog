# 1-Azkaban介绍

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\1-Azkaban介绍【海量资源尽在 ubkz.com】.mp4
- 时长 6分20秒（音频 380s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 我们开始上课今天我们来学习大数据处理里面一个常用的框架阿兹卡班那么在讲阿兹卡班之前先说一下为什么需要学习阿兹卡班那么在我们日常的大数据分析里面一个完整的大数据分析系统可能需要很多个任务组成比如说这些任务分别是比如说shell脚本加尔程序MapReduce和Hive这些可能都是
[00:29] 我们大数据处理中一个一个的任务那只有呢把这些任务全部执行完毕我们的数据分析呢才能结束而且呢有时候呢这些任务与任务之间呢存在着先后的依赖关系比如说呢是要脚本执行完之后呢才能执行加尔程序而加尔程序执行完了才能执行MapReduce好那么这么多任务如何能够把它们组在一起能够完成我们指定的一个
[00:58] 任务需求呢这个时候我们需要一个工作流调度系统而我们今天学的阿兹卡巴呢就是来完成我们大数据中的任务流调度的能够保证我们这些任务在一定的时间在合适的位置去执行相应的动作OK那么接下来呢我们来通过一个图来看一下大数据处理里面都需要哪些步骤来打开我们那个画图
[01:27] 好 在这里有一张图这张图就很清晰的描述一下大数据中常用的一个处理的一个简单的一个任务调度来看一下比如说我们要去处理一个数据那首先从左到右看比如说我们在日常的业务系统中存在很多日志文件存在很多业务数据存在很多外部数据那我们需要对这些数据进行分析处理那么第一步我们可能比如说日志文件
[01:56] 我们可以采用flume采集比如说对于业务数据呢我们可以通过scope导入这个scope呢也是一个框架那么后面呢再给大家讲OK还有web数据呢我们可以通过爬虫获取不管怎么样我们获取的web数据之后呢我们可以把这个数据呢存储到HDFS了或者存储到HBase上都可以好当我把数据存储到HDFS之后呢这些数据呢可能格式不统一
[02:26] 或者说呢它并不能满足我的需求这个时候呢我需要对这个数据做一些预处理什么预处理呢比如说数据的清洗啊数据的解析啊或者数据的合并啊等等这些呢需要MapReduce来做好那么把这些数据经过预处理之后呢我再把清洗之后的数据呢存放到Hive仓库然后呢对Hive仓库中的数据呢做进一步的分析和处理
[02:56] 最后呢我再把这些数据呢经过处理后的分析后的数据呢通过报表系统来展示比如说我可以展示到页面上OK那么这是一系列的流程那如何保证这一系列的流程能够按照我们的需求从前到后依次执行呢这个时候我们就需要一个任务调度OK你比如说呢我只有把这个数据采集放在HDFS之后呢
[03:22] 我们的这个预处理才能进行而预处理之后呢我们的Hive才能进行那所以说这个时候呢我们的阿兹卡班就可以完成整个我们的任务调度所以说阿兹卡班就是为了任务调度而产生的那了解了这个阿兹卡班那个任务调度一个简单一个过程之后呢我们回到讲义我们来了解阿兹卡班这个其实呢除了阿兹卡班之外呢
[03:50] 也有很多常用的一些任务调度工具比如说最简单的比如说在Linux里面我们可以使用这个Crawl Table这个Crawl Table非常简单只需要一个meaning就也可以完成任务调度但是Crawl Table它不能解决多个任务之间的一个依赖关系而一些复杂的任务调度比如说在Hadoop领域有哪些比如说有Wooz还有今天我们学的阿兹卡班还有什么Kitskitting
[04:18] 还有什么HeyMaker等等这些是比较复杂的它的这个可以完成更复杂一些任务调度在这里有一个表格那么对这些常用的一些任务调度工具进行了一些对比我们简单看一下咱先看它的工作语言吧比如说HeyMaker和Woozly它用的都是XML而阿兹卡曼呢其实用的是类似于ProPractice的一些箭子队它的语言非常简单而KistKitting呢
[04:47] 用的是加味还有呢比如说这个是否需要web容器呃无贼和阿兹卡班是需要的他们有一个图形界面可以去观察他的任务整个执行流程还有那些进进程的跟踪啊比如说黑妹可能是通过控制台或者说日之的一些信息呃那无贼和阿兹卡班呢是通过web界面而这个kiss kidding呢是通过加味一篇等等ok好那么大家呢以后在工作中呢可以根据自己的需求呢去选择
[05:17] 对应的一些任务调度器好那接下来咱们再看看阿兹卡班的一些特点阿兹卡班呢是一个LinkedIn的它的一个开源开源的一个任务工作流调度器OK那么它呢是通过定一些建制队的方式来实现任务之间的一个依赖关系这个依赖关系呢也是通过配置文件而且配置文件写起来非常简单而且它提供了一些良好的用户界面
[05:45] 你看它的特点第一有web用户界面你的操作呢都是在界面上进行OK还可以呢实现一些定时任务它可以呢比如说我在某一个时间点去执行某个任务它都可以去实现而且呢我们在上传新的任务的时候呢非常的方便还可以设置任务与任务之间的一些依赖关系当任务执行的时候呢它可以呢去打一些日志信息等等OK那么这是阿兹卡班的一些特点
[06:15] OK关于阿维卡门的介绍呢我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
介绍Azkaban工作流调度系统，包括其必要性、常见调度工具对比以及Azkaban本身的功能和特性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 标题：Day 07，1. Azkaban介绍，1.1. 为什么需要Azkaban。
- 内容：一个完整的数据分系统通常是由大量任务单元组成，包括shell脚本程序、java程序、mapreduce程序、Hive脚本等。
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
- 内容：简单的任务调度：直接使用linux的crontab来定义；复杂的任务调度：在Hadoop领域，常见的工作流调度器有Oozie, Azkaban, Cascading等。

画面4：
- 标题：1.3. 各种调度工具特性对比。
- 内容：下面的表格对上述四种Hadoop工作流调度器的关键特性进行了比较，尽管这些工作流调度器能够解决的需求场景基本一致，但在设计理念、目标用户、应用场景等方面还是存在显著的区别，在做技术选型的时候，可以提供参考。

画面5：
- 标题：1.3. 各种调度工具特性对比。
- 内容：表格开始显示，特性包括：Hamake, Oozie, Azkaban, Cascading。
- 表格列：工作流描述语言、依赖机制、是否需要web容器、进度跟踪、Hadoop job调度支持、运行模式、Pig支持、事件通知、需要安装、支持的Hadoop版本、重试支持、运行任意命令、Amazon EMR支持。

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
- 内容：表格继续显示，支持的Hadoop版本：Hamake为0.18+，Oozie为0.20+，Azkaban为currently unknown，Cascading为0.18+。
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
  | 支持的Hadoop版本 | 0.18+ | 0.20+ | currently unknown | 0.18+ |
  | 重试支持 | no | workflownode | yes | yes |
  | 运行任意命令 | yes | yes | yes | yes |
  | Amazon EMR支持 | yes | no | currently unknown | yes |

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

