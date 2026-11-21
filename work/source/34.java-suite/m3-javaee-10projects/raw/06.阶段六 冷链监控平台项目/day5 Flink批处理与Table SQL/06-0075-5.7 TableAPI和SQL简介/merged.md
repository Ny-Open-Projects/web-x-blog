# 5.7 TableAPI和SQL简介

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.7 TableAPI和SQL简介_【海量资源尽在 666java.com】.mp4
- 时长 4分30秒（音频 271s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好,下面我们来给大家介绍一下Flink的Table API和Circle编程那么Flink针对标准的流处理和批处理提供了两种相关的API一个叫做Table API,一个叫做Circle那么Table API允许用户以一种很直观的方式进行Select, Filter, Join等各种操作那么Flink Circle支持它基于Apache Call Set实现的标准的Circle语句
[00:30] 那么也就是说无论是我们针对于流逝处理还是P处理的一些数据那么我们都可以通过标准的Circle语句来查询我们想要的得到的一个结果Flink Table API和Circle接口和Flink Data Stream的APIData Set API是紧密结合在一起的那么我们来先来看一看我们整个的Flink它的Table API和Circle API的一个架构或者说是在整个体系中的位置那么
[00:59] 最底层的话是具体的有状态的流处理的一个引擎那么这个流处理引擎呢在上边的话其实就是我们的datastream和dataset的一个API它是我们的整个Flink它的一个核心的API那么基于此之上的呢就是Flink的一个table APIapache callset的这么一个组件那么基于这个组件之上呢其实就是
[01:27] 先应用从的一个circle那么我们在我们的Flink程序里边可以直接使用circle语句来进行查询添加和删除等各种各样的一些操作那么我们来看一看我们整个的查询过程对于一个客户端来讲啊这这个架构图呢其实是偏向于mycircle的那么左侧部分是mycircle的一个查询过程其实我们的call set或者说我们的Flink它的整个原理和
[01:57] mycircle的这个原理大致类似那么比如一个客户端这个客户端来讲的话相当于我们的mycircle的一个客户端首先它连接到我们服务器端的时候它先连接一个连接器那么连接器连接完之后呢把相关的请求的circle语句扔到了分析器分析器对于circle语句进行分析结果之后呢它会做一些内部的优化所以就是优化去来
[02:27] 做的一些操作那么优化器执行完之后呢相关的是执行器具体执行那么这是在circle引擎部分相关的一些东西那么具体的mycircle存储的话它分成不同的一些存储方式比如说inodeb或者说myisam甚至于在它的一些缓存的索引等等这些属于它的存储层的那么和它相类似的或者相对应的其实是什么呢比如在我们的
[02:56] 上层,Flink上层它用到的是Apache的Cosette这个Circle执行引擎,那么再往下一层的话是DataStream API和DataSet的API,那么最底层的存储层的话是DataStream和DataSet相关的一些Process,那么这个过程呢我们大致的了解一下,在实际的开发过程中我们只需要知道我们对于
[03:23] Flink的table api和circle api的编程方式是什么样子后边我们会给出一个相关的一个例子然后给大家分析一下这个例子到底是它是如何运行的我们在操作时候如何来操作的那么如果是说我们的程序要引入table api或者circle的话那么需要添加一些依赖这些依赖包括两个部分一部分叫Flink-table-api-java的一个bridge
[03:51] 那么后边是它的一个版本号这个版本号的话目前的话是2.11另外一个依赖是Flink table planner这个planner类似于我们的一个执行器或者说优化器执行器在这个层面上的一个东西那我们的程序其实很多的时候需要依赖于call set的一些执行器这是我们给大家
[04:15] 大概的讲解了一下Flink table API和circle API它的一个运行的过程以及它的一个架构的一个大致的原理那么后面我们会给大家介绍Flink table API和circle API的一个示例

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Flink Table API 和 SQL 编程的架构原理与依赖配置。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 Flink Table API 和 SQL 编程的架构原理图，包含 SQL、Table API、DataStream/Dataset API 层级，以及客户端、Server、存储端的流程图。
画面2: 展示架构图中 Server 端的详细流程，包括连接器、分析器、优化器、执行器，以及与 Apache Calcite 和 DataStream/Dataset API 的连接。
画面3: 展示架构图中存储端的详细内容，包括 MyISAM、InnoDB、Memory 等存储引擎，以及与 DataStream/Dataset 的连接。
画面4: 展示使用 Table API 和 SQL 时需要添加的 Maven 依赖配置，包括 <properties> 和 <dependencies> 部分。
画面5: 展示架构原理图，包含 SQL、Table API、DataStream/Dataset API 层级，以及客户端、Server、存储端的流程图。
画面6: 展示架构图中 Server 端的详细流程，包括连接器、分析器、优化器、执行器，以及与 Apache Calcite 和 DataStream/Dataset API 的连接。
画面7: 展示架构图中存储端的详细内容，包括 MyISAM、InnoDB、Memory 等存储引擎，以及与 DataStream/Dataset 的连接。
画面8: 展示使用 Table API 和 SQL 时需要添加的 Maven 依赖配置，包括 <properties> 和 <dependencies> 部分。
画面9: 展示使用 Table API 和 SQL 时需要添加的 Maven 依赖配置，包括 <properties> 和 <dependencies> 部分。
画面10: 展示 Table API 和 SQL 的程序示例，包括 import 语句和 select 语言选择框。
画面11: 展示架构图中 Server 端的详细流程，包括连接器、分析器、优化器、执行器，以及与 Apache Calcite 和 DataStream/Dataset API 的连接。
画面12: 展示架构图中存储端的详细内容，包括 MyISAM、InnoDB、Memory 等存储引擎，以及与 DataStream/Dataset 的连接。
画面13: 展示架构原理图，包含 SQL、Table API、DataStream/Dataset API 层级，以及客户端、Server、存储端的流程图。
画面14: 展示 Flink Table API 和 SQL 编程的架构原理图，包含 SQL、Table API、DataStream/Dataset API 层级，以及客户端、Server、存储端的流程图。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面4:
<properties>
<scala.binary.version>2.11</scala.binary.version>
<!-- 其他依赖包的版本... -->
</properties>

<dependencies>
<dependency>
<groupId>org.apache.Flink</groupId>
<artifactId>Flink-table-api-java-bridge_${scala.binary.version}</artifactId>
<version>${Flink.version}</version>
</dependency>
<dependency>
<groupId>org.apache.Flink</groupId>
<artifactId>Flink-table-planner_${scala.binary.version}</artifactId>
<version>${Flink.version}</version>
</dependency>
<!-- 其他依赖包 -->
</dependencies>

画面8:
<properties>
<scala.binary.version>2.11</scala.binary.version>
<!-- 其他依赖包的版本... -->
</properties>

<dependencies>
<dependency>
<groupId>org.apache.Flink</groupId>
<artifactId>Flink-table-api-java-bridge_${scala.binary.version}</artifactId>
<version>${Flink.version}</version>
</dependency>
<dependency>
<groupId>org.apache.Flink</groupId>
<artifactId>Flink-table-planner_${scala.binary.version}</artifactId>
<version>${Flink.version}</version>
</dependency>
<!-- 其他依赖包 -->
</dependencies>

画面10:
import org.apache.Flink.streaming.api.datastream.DataStream;
<!-- select a language -->
画面14:
<properties>
<scala.binary.version>2.11</scala.binary.version>
<!-- 其他依赖包的版本... -->
</properties>

<dependencies>
<dependency>
<groupId>org.apache.Flink</groupId>
<artifactId>Flink-table-api-java-bridge_${scala.binary.version}</artifactId>
<version>${Flink.version}</version>
</dependency>
<dependency>
<groupId>org.apache.Flink</groupId>
<artifactId>Flink-table-planner_${scala.binary.version}</artifactId>
<version>${Flink.version}</version>
</dependency>
<!-- 其他依赖包 -->
</dependencies>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1: 标题为“2 Flink Table API和SQL编程”，架构图中 SQL 指向 Table API，Table API 指向 DataStream/Dataset API，DataStream/Dataset API 指向 Stateful Stream Processing，Stateful Stream Processing 指向客户端，客户端指向 Server，Server 指向存储端。
画面2: 架构图中客户端指向 Server，Server 中的连接器指向分析器，分析器指向优化器，优化器指向执行器，执行器指向 Apache Calcite 和 DataStream/Dataset API。
画面3: 架构图中 Server 中的执行器指向存储端中的 MyISAM、InnoDB、Memory 等存储引擎，存储端中的 DB 指向 DataStream/Dataset。
画面4: 无表格数据。
画面5: 架构图中 SQL 指向 Table API，Table API 指向 DataStream/Dataset API，DataStream/Dataset API 指向 Stateful Stream Processing，Stateful Stream Processing 指向客户端，客户端指向 Server，Server 指向存储端。
画面6: 架构图中客户端指向 Server，Server 中的连接器指向分析器，分析器指向优化器，优化器指向执行器，执行器指向 Apache Calcite 和 DataStream/Dataset API。
画面7: 架构图中 Server 中的执行器指向存储端中的 MyISAM、InnoDB、Memory 等存储引擎，存储端中的 DB 指向 DataStream/Dataset。
画面8: 无表格数据。
画面9: 无表格数据。
画面10: 无表格数据。
画面11: 架构图中客户端指向 Server，Server 中的连接器指向分析器，分析器指向优化器，优化器指向执行器，执行器指向 Apache Calcite 和 DataStream/Dataset API。
画面12: 架构图中 Server 中的执行器指向存储端中的 MyISAM、InnoDB、Memory 等存储引擎，存储端中的 DB 指向 DataStream/Dataset。
画面13: 架构图中 SQL 指向 Table API，Table API 指向 DataStream/Dataset API，DataStream/Dataset API 指向 Stateful Stream Processing，Stateful Stream Processing 指向客户端，客户端指向 Server，Server 指向存储端。
画面14: 架构图中 SQL 指向 Table API，Table API 指向 DataStream/Dataset API，DataStream/Dataset API 指向 Stateful Stream Processing，Stateful Stream Processing 指向客户端，客户端指向 Server，Server 指向存储端。

5) 不要评价画面美观，不要输出与课程无关的内容。

