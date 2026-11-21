# 4.3 Flink介绍

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day4 Flink基础与流数据处理
- 源文件：06.阶段六 冷链监控平台项目\day4 Flink基础与流数据处理\4.3 Flink介绍_【海量资源尽在 666java.com】.mp4
- 时长 7分19秒（音频 440s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前面我们提到我们的数据流是源源不断无穷无尽的一个数据那么如果我们想要拿到数据流中的数据然后对数据进行处理的时候我们有什么方式呢那其实很容易就能想到我可以把应用端或者说设备端提交过来的数据流中的数据推送到我们的卡发卡队列里面去而我们可以开发我们的Java程序
[00:29] 作为消费端来消费卡法卡对链里面的数据那么在这个过程中呢其实就是我们对于实时数据的一个处理但是对于这种实时数据的处理它有一个问题它是一个无状态的换句话说假设我们如果开发某一个加码程序而这个加码程序消费卡法卡对链那么我如何来计算或者如何来得到过去五分钟之内的
[00:57] 所有数据的某一个指标的和呢那如果我要想解决这样的一个问题那我需要在我的程序里边把我数据给临时的存储一下对吧我要做数据的一个持久化那我要最终我的数据如何来做我的这个程序如何来写它的持久化方案应该是什么它的临时存储的方案是什么这些都需要我们自己来开发
[01:25] 还有一个非常重要的一个问题比如我们说过去五分钟内的数据过去十分钟内的数据那如何来定义五分钟呢当前时间是十点钟那十点零一分的时候那过去的五分钟就变了对吧我十点零一分零一秒我过去的五分钟还是变了在这个情况下我们可以想象一下这个加码程序是非常难以开发的或者说它需要考虑的因素会非常的多
[01:55] 那还有的是说我如果数据丢失了怎么办我如果数据来晚了怎么办我的服务器如果挂了怎么办就是我们加密程序如果挂掉了我们如何来处理这些都是需要我们对于整个程序需要考虑的一些因素而Flink它就做了这些工作它本身是一个开源的这种分布式的这种流逝处理框架刚才我提到的这些问题Flink它都有了相应的解决方案
[02:25] 比如我们数据它是可以进行扩展的我们的服务器如果它扩展的情况下其实就相当于我们数据的处理能力是增强的对吧那如果数据来晚了或者说是数据的不安顺序进入到我们的卡普卡处理器里边那么我们的Flink能够把它正确的进行放在正确的位置上
[02:49] 那我们如果把数据进行一个统计一个计算的时候Flink它提供的是有状态的数据处理等等的这一切其实就给我们大家相应的来讲的话描绘了我们Flink它能处理的一些特点处理的一些应用那在这种情况下我们看一看我们整个运行的一个过程那首先的话我们前端的这种各种各样的一些
[03:19] 设备设备是ROT指的是我们的物联网设备然后click指的是点击log呢指的是日志产生的文件transaction指的是我们的事务产生的一些过程那在这种情况下它会生成也就是说业务系统硬件设备它会生成相应的一些数据那有一种数据呢会存储到我们的数据库系统文件系统或者说是蒙古DB类似于这样的
[03:49] 数据库里边那还有一类的话是我们用卡普卡来接收这样的数据两类数据统一的就进入到我们的Flink程序里边了而Flink程序的话我们首先会有一部分叫做针对于我们事件驱动的一些应用那当某个事件过来的时候我们就能够及时的捕获到数据里边的一些状态数据里边的一些值
[04:16] 正过第二部分来讲的话是我们可以通过这种流处理的方式来接收到它那我们接收到它之后我就可以进行流或批处理的一些分析计算然后或者说是一些统计或者说是一些查询等等这样的功能大家注意的一点是刚才我提到了有一部分是属于实时数据那还有另外一部分的话比如存储到我们的数据库这一类系统它其实是一个
[04:44] P数据的一个处理换言之我们Flink是把流数据处理和P数据处理两者合而为一了而最终来讲这个整个Flink它是可以部署在我们的类似于KubernetesK8s就是KubernetesYi是一个资源管理的框架实际上是Hadoop体系里边的一个资源管理框架那MySource的话也是类似于K8s的一个东西
[05:12] 它最终的数据可以存储到HDFS里边存储到MySQL里边存储到NFS数据库里边等等各种各样的一个存储Flink可能直接的进行对接那最终来讲的话我们会通过Flink来应用来把我们的数据最终存储到应用系统相应的来用那么我们的事件的event或者说是它发对链里边我们可以放在这里边我们还可以放到我们数据库或者说最终的我们的一个
[05:41] 文件系统等等那简单的来讲的话是分成三个阶段第一个阶段就是数据的收集第二个阶段来讲的话是数据的一个处理第三个阶段是数据的一个存储那么Flink它统一的对这整个过程或者整个事件来做了处理那我们来看一看Flink的一个核心的一些流程而这个核心流程来讲的话包括我们的从存储端上我们刚才也提到了Flink可以
[06:10] 单独的集群进行部署也可以以一种集群方式来进行部署或者放到我们的其他的一些云服务厂商里面去那在这个部署之上呢是Flink的实时计算的核心的一个运行时的一个流处理的一个引擎那基于这个引擎的话它会开放出来我们一些这种API
[06:36] 这种API包括我们的流处理的,DataStream的API,还包括我们P处理的,DataSet的API,Streaming的一个Processing指的就是流处理,Batch的话就是P处理的一个过程,那在往上层的一些应用,或者说是在一些机器学习方面,它提供了一个BlinkML,那么针对于这种决策方面的话,它提供了一个CEP,
[07:00] 也就是说我根据数据我能够定义表达规则表达式来做我们的数据的一个决策然后还提供了我们的这种table也就是说我可以通过circuit去来查询我们的这种数据这是我们对大家给大家介绍了一个Flink的一个情况

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Apache Flink 的简介、核心组件架构和应用场景。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 内容：展示文档大纲，当前位于“1.2 Flink简介”章节。
- 画面中文字内容：
  - 1.2 Flink简介
  - Apache Flink 是一个开源的分布式流式处理框架，是新的流式计算引擎，用Java实现。Flink可以：
    - 提供准确的结果，甚至在出现无序或者延迟加的数据的情况下。
    - 它是状态化的容错的，同时在维护一次完整的应用状态时，能无缝修复错误。
    - 大规模运行，在上千个节点运行时有很好的吞吐量和低延迟。

画面2：
- 内容：继续展示“1.2 Flink简介”内容，下方出现 Flink 架构图。
- 画面中文字内容：
  - Apache Flink 是一个开源的分布式流式处理框架，是新的流式计算引擎，用Java实现。Flink可以：
    - 提供准确的结果，甚至在出现无序或者延迟加的数据的情况下。
    - 它是状态化的容错的，同时在维护一次完整的应用状态时，能无缝修复错误。
    - 大规模运行，在上千个节点运行时有很好的吞吐量和低延迟。
  - 架构图标题：Flink的核心组件：
  - 架构图内容：
    - 上层：CEP Event Processing, Table Relational, FlinkML Machine Learning, Gelly Graph Processing, Table Relational
    - 中层：DataStream API Stream Processing, DataSet API Batch Processing
    - 下层：Runtime Distributed Streaming Dataflow
    - 底层：Deploy Local Single JVM, Cluster Standalone, YARN, Cloud GCE, EC2

画面3：
- 内容：展示 Flink 核心组件架构图，图中包含“所有流式场景”标题。
- 画面中文字内容：
  - Flink的核心组件：
    - 上层：CEP Event Processing, Table Relational, FlinkML Machine Learning, Gelly Graph Processing, Table Relational
    - 中层：DataStream API Stream Processing, DataSet API Batch Processing
    - 下层：Runtime Distributed Streaming Dataflow
    - 底层：Deploy Local Single JVM, Cluster Standalone, YARN, Cloud GCE, EC2
  - 标题：1.3 应用场景
  - 文字：Apache Flink 功能强大，支持开发和运行多种不同种类的应用程序。它的主要特性包括：
    - 所有流式场景

画面4：
- 内容：展示 Flink 核心组件架构图，图中包含“所有流式场景”标题。
- 画面中文字内容：
  - Flink的核心组件：
    - 上层：CEP Event Processing, Table Relational, FlinkML Machine Learning, Gelly Graph Processing, Table Relational
    - 中层：DataStream API Stream Processing, DataSet API Batch Processing
    - 下层：Runtime Distributed Streaming Dataflow
    - 底层：Deploy Local Single JVM, Cluster Standalone, YARN, Cloud GCE, EC2
  - 标题：1.3 应用场景
  - 文字：Apache Flink 功能强大，支持开发和运行多种不同种类的应用程序。它的主要特性包括：
    - 所有流式场景

画面5：
- 内容：展示 Flink 核心组件架构图，图中包含“所有流式场景”标题。
- 画面中文字内容：
  - Flink的核心组件：
    - 上层：CEP Event Processing, Table Relational, FlinkML Machine Learning, Gelly Graph Processing, Table Relational
    - 中层：DataStream API Stream Processing, DataSet API Batch Processing
    - 下层：Runtime Distributed Streaming Dataflow
    - 底层：Deploy Local Single JVM, Cluster Standalone, YARN, Cloud GCE, EC2
  - 标题：1.3 应用场景
  - 文字：Apache Flink 功能强大，支持开发和运行多种不同种类的应用程序。它的主要特性包括：
    - 所有流式场景

画面6：
- 内容：展示 Flink 核心组件架构图，图中包含“所有流式场景”标题。
- 画面中文字内容：
  - Flink的核心组件：
    - 上层：CEP Event Processing, Table Relational, FlinkML Machine Learning, Gelly Graph Processing, Table Relational
    - 中层：DataStream API Stream Processing, DataSet API Batch Processing
    - 下层：Runtime Distributed Streaming Dataflow
    - 底层：Deploy Local Single JVM, Cluster Standalone, YARN, Cloud GCE, EC2
  - 标题：1.3 应用场景
  - 文字：Apache Flink 功能强大，支持开发和运行多种不同种类的应用程序。它的主要特性包括：
    - 所有流式场景

画面7：
- 内容：展示“1.2 Flink简介”内容，下方出现 Flink 架构图。
- 画面中文字内容：
  - Apache Flink 是一个开源的分布式流式处理框架，是新的流式计算引擎，用Java实现。Flink可以：
    - 提供准确的结果，甚至在出现无序或者延迟加的数据的情况下。
    - 它是状态化的容错的，同时在维护一次完整的应用状态时，能无缝修复错误。
    - 大规模运行，在上千个节点运行时有很好的吞吐量和低延迟。
  - 架构图标题：Flink的核心组件：
  - 架构图内容：
    - 上层：CEP Event Processing, Table Relational, FlinkML Machine Learning, Gelly Graph Processing, Table Relational
    - 中层：DataStream API Stream Processing, DataSet API Batch Processing
    - 下层：Runtime Distributed Streaming Dataflow
    - 底层：Deploy Local Single JVM, Cluster Standalone, YARN, Cloud GCE, EC2

画面8：
- 内容：展示“1.2 Flink简介”内容，下方出现 Flink 架构图。
- 画面中文字内容：
  - Apache Flink 是一个开源的分布式流式处理框架，是新的流式计算引擎，用Java实现。Flink可以：
    - 提供准确的结果，甚至在出现无序或者延迟加的数据的情况下。
    - 它是状态化的容错的，同时在维护一次完整的应用状态时，能无缝修复错误。
    - 大规模运行，在上千个节点运行时有很好的吞吐量和低延迟。
  - 架构图标题：Flink的核心组件：
  - 架构图内容：
    - 上层：CEP Event Processing, Table Relational, FlinkML Machine Learning, Gelly Graph Processing, Table Relational
    - 中层：DataStream API Stream Processing, DataSet API Batch Processing
    - 下层：Runtime Distributed Streaming Dataflow
    - 底层：Deploy Local Single JVM, Cluster Standalone, YARN, Cloud GCE, EC2

画面9：
- 内容：展示 Flink 核心组件架构图，图中包含“所有流式场景”标题。
- 画面中文字内容：
  - Flink的核心组件：
    - 上层：CEP Event Processing, Table Relational, FlinkML Machine Learning, Gelly Graph Processing, Table Relational
    - 中层：DataStream API Stream Processing, DataSet API Batch Processing
    - 下层：Runtime Distributed Streaming Dataflow
    - 底层：Deploy Local Single JVM, Cluster Standalone, YARN, Cloud GCE, EC2
  - 标题：1.3 应用场景
  - 文字：Apache Flink 功能强大，支持开发和运行多种不同种类的应用程序。它的主要特性包括：
    - 所有流式场景

画面10：
- 内容：展示 Flink 核心组件架构图，图中包含“所有流式场景”标题。
- 画面中文字内容：
  - Flink的核心组件：
    - 上层：CEP Event Processing, Table Relational, FlinkML Machine Learning, Gelly Graph Processing, Table Relational
    - 中层：DataStream API Stream Processing, DataSet API Batch Processing
    - 下层：Runtime Distributed Streaming Dataflow
    - 底层：Deploy Local Single JVM, Cluster Standalone, YARN, Cloud GCE, EC2
  - 标题：1.3 应用场景
  - 文字：Apache Flink 功能强大，支持开发和运行多种不同种类的应用程序。它的主要特性包括：
    - 所有流式场景

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- PPT 标题：
  - 1.2 Flink简介
  - 1.3 应用场景
  - Flink的核心组件：

- 架构图结构：
  - 顶部：Transactions, Logs, IOT, Clicks → (Event Log)

