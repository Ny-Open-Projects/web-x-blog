# 07-CAT链路监控-Google Dapper理论 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

咱们接着学习下一个知识点

Google Dapp的论文理论

我们看一下Google Dapp论文到底是什么呢

它其实呢提供的是一个大型伸缩的分布式系统的追踪设计的一个论文

那我们可以知道通过这个论文的话呢

奠定了我们分布式链路监控的一个基础

那么很多的一些分布式链路框架

Sluth, Zipkin, Skywalking

他们都是基于Google Dapp理论去衍生开发出来的

好那我们看一下Google的Dapp理论具体是怎样的

它整个的部署架构又是怎么去实现的呢

Google的Dapp的部署架构呢如图所示

我们可以看到在这里呢

是Production, Custom Machines

就是所有的主机

那么我们生产线上面的这些所有主机呢

可以看到有很多对不对

这些主机的话呢

我们不可能去每台主机上面去查看它的具体日志

所以呢

在这里Google这一块它怎么做的呢

它将这里面的数据会读取到哪里呢

读取到Dapp的Collector收集器里面

那收集器里面呢

它怎么去做的呢

它通过Extrament

Bunnelist也就是说一个二进制的Log文件

然后呢通过什么传输过去呢

通过Dapp的Demand后台线程

在这里呢

后台线程

它会将Log File的监控日志信息呢

传递给Dapp Collector

好Dapp Collector收集器拿到数据之后

它要做加工

对不对

那我们看一下它怎么去加工的

怎么去组织这些的监控信息

那我们可以看到它这个结构呢

是按照表格所示

在这里呢

CHESS ID是一个追踪ID

这追踪ID是什么意思呢

相当于就是每一次请求的ID标识

那么我们可以看到

在这里面的话呢

CHESS ID 123456对不对

它所对应的链路是怎样的呢

它是SPAN3和4

SPAN4和5

它的意思就是说

它是在SPAN第三和第四个节点当中的话呢

有做处理请求

看到没有

有带的数据对吧

然后的话呢

3和4流转到了什么

SPAN4和5

它们两个节点之间怎么去关联的呢

我链路当中一环扣一环的对不对

那么一环扣一环的这种追踪请求

我是不是应该要一个标识

或者是一个关联啊

这样的话呢

我就知道A服跟B服

它们呢是一个调用链的关系

大家想想是不是

如果说我们

这个请求之间没有任何关联

那么我B这边的请求呢

我根本就无法识别

到底是A发过来的

还是说外部的一个请求

所以呢

它是通过什么

有一个SPAN的ID做这样一个标识

好

那么我们有这么多节点对不对

123456这么多节点

那么这个请求它到底流转了哪些节点呢

它会在流转的节点下面做一个什么

Data的数据记录

这样呢

是不是就会比较直观一点啊

我就知道了

它流转了哪些节点

然后通过SPAN ID就能够追踪到它整个的链路监控

同样的这个缺失ID呢

它是流转了SPAN1和2

对不对

然后的话呢

它流转到哪里去了

流转到SPAN5跟6

同样的话呢

在这里面

如果说它没有链路的一个那个调用

它只调用了一个节点

那么呢

它在SPAN23里面直接写入数据就可以了

这个呢

就是整个的DAV的部署架构

以及呢

它怎么去做的实现

好

那这里呢

就是对谷歌DAV的理论的介绍

这一讲呢

我们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对技术课程内容进行的结构化中文输出：

---

### 1) 视频摘要

本视频片段是关于分布式系统监控工具 CAT（特别是其核心组件 Dapper）的讲解。讲师通过展示 Google 的 Dapper 论文（Google Technical Report dapper-2010-1, April 2010）来介绍其核心思想和架构。主要内容包括：
- **背景与动机**：现代互联网服务是复杂的分布式系统，理解其行为和性能至关重要。
- **Dapper 部署架构**：通过在生产主机上部署“instrumented binaries”（被植入代码的二进制文件），由 Dapper daemon 收集日志，再由 Dapper Collectors 读取并写入中央存储（Bigtable）。
- **链路监控工作机制**：通过 trace ID 和 span 来追踪一个请求在分布式系统中的完整调用链路，从而实现对系统行为的观察和性能分析。

---

### 2) 按时间顺序的章节（带时间点）

由于提供的截图未包含精确的时间戳，以下章节划分是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:05**: **3.5 Google Dapper论文** - 展示论文标题页，介绍论文来源和作者。
- **00:05 - 00:15**: **3.5 Google Dapper论文** - 展示论文摘要（Abstract），阐述分布式系统监控的必要性。
- **00:15 - 00:25**: **3.6 Dapper Deployment** - 展示 Dapper 的部署架构图，包括 instrumented binaries、Dapper daemon、Dapper Collectors 和中央存储。
- **00:25 - 00:35**: **3.7 链路监控工作机制** - 展示数据表，说明如何通过 trace ID 和 span 来追踪调用链路。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

- **PPT / 图表**:
  - **论文封面**: `Google Technical Report dapper-2010-1, April 2010`
  - **论文标题**: `Dapper, a Large-Scale Distributed Systems Tracing Infrastructure`
  - **作者列表**: Benjamin H. Sigelman, Luiz André Barroso, Mike Burrows, Pat Stephenson, Manoj Plakal, Donald Beaver, Saul Jaspan, Chandan Shanbag
  - **摘要 (Abstract)**: 强调现代互联网服务是复杂的分布式系统，需要工具来观察和理解其行为。
  - **部署架构图**:
    - **组件**: `<instrumented binaries>` (被植入代码的二进制文件)、`Dapper daemon`、`Dapper Collectors`、`(production host machines)` (生产主机)、`(Central Bigtable repository for trace data)` (中央 Bigtable 存储)。
    - **数据流**: 1. instrumented binaries 生成 log file；2. Dapper daemon 读取 log file 并发送给 Dapper Collectors；3. Dapper Collectors 将 trace 数据写入中央 Bigtable。
  - **数据表**:
    - **表头**: `trace id`, `span 12`, `span 23`, `span 34`, `span 45`, `span 56`, ...
    - **示例数据**:
      ```
      trace id | span 12 | span 23 | span 34 | span 45 | span 56 | ...
      123456    | nil     | nil     | <data>  | <data>  | nil     | ...
      246802    | <data> | nil     | nil     | nil     | <data> | ...
      357913    | nil     | <data> | nil     | nil     | nil     | ...
      ```

---

### 4) 关键场景与演示描述

- **场景一：论文介绍 (00:00-00:15)**
  - 讲师首先展示 Google Dapper 论文的封面和摘要。
  - 通过阅读摘要，强调了现代互联网服务的复杂性，以及监控和分析其行为的重要性。
  - 摘要中提到的“web-search example”（搜索引擎示例）被用来说明系统需要解决的挑战。

- **场景二：部署架构演示 (00:15-00:25)**
  - 讲师切换到“3.6 Dapper Deployment”章节。
  - 展示了 Dapper 的部署架构图，图中清晰地展示了 instrumented binaries、Dapper daemon、Dapper Collectors 和生产主机之间的数据流向。
  - 讲师可能通过鼠标指针指向图中的不同组件，解释其功能和作用。

- **场景三：链路监控机制演示 (00:25-00:35)**
  - 讲师切换到“3.7 链路监控工作机制”章节。
  - 展示了数据表，通过 trace ID 和 span 来说明如何追踪一个请求在分布式系统中的完整调用链路。
  - 表格中的 `<data>` 表示该 span 包含了实际的调用数据，而 `nil` 表示该 span 没有数据或尚未完成。

---

以上是根据视频画面截图对技术课程内容的结构化分析。
