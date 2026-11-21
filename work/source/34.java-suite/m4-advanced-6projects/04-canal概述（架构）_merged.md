# 04-canal概述（架构） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,刚才我们讲了一下Kandra的工作原理,接下来我们来看下一个小节,就是Kandra的架构。

通过下边这个图,大家能够看到Kandra的架构里边有这么几个概念,一个是server,还有什么instance,event passer,event think,还有event store,还有meta manager,这么多的概念。

接下来我们来看一下,首先第一个是server,server代表的是什么呢?是一个Kandra的服务。

那么Kandra它本身其实就是基于Java语言开发出来的这么一个服务框架。

那么我们可以把它跑起来,那么对应的就是一个服务的进程。

然后在这个服务里边有多个instance,也就是说这个服务可以管理多个instance,每一个instance对应的就是一个Kandra的实例。

那这个实例是干什么用的呢?这个实例它可以伪装成一个slave,然后从我们买circle,是不是来dump数据。

你看前面我们这个图,咱们这个左边是一个master,就是mycircle。

我们把这个mycircle它的主库,然后这个Kandra就可以把自己伪装成一个从户,对吧?

然后跟我们的主库来进行交互,主要就是获取主库这边产生的这个binary log,对吧?

然后Kandra就可以把这个日志把它获取过来,获取过来之后我们是不是就可以进行解析,对吧?

就可以有相应的方法,把这个日志解析,解析完之后我们就能知道主库那边发生了什么事情,对吧?

进行了什么样的操作,然后对应的我们也可以把那个相应的circle还有什么数据,

都解析出来,这样的话我们就可以去订阅这些数据,对吧?

好,那接下来我们来看,咱们这个instance它要做的就是把自己伪装成一个slave,然后来获取数据。

然后我们可以看到在instance里边又有这么几个模块,对吧?

而这个event passer,它做的事情就是什么呢?

数据源接入,说白了就是什么呢?

它是负责跟我们这个master进行交互的。

那么这个交互的过程,你看Kandra跟这个master,

我们之间交互过程来拉去这个binary log,对吧?

那么交互的过程就是交给我们这个event passer,由这个模块来完成的。

你看它是数据源接入,模拟slave协议和master进行交互,然后协议的解析等等。

那么是交给这个组件来完成。

然后接下来还有一个叫做event think,对吧?

这个其实是一个连接器,它连接谁呢?

它连接我们这个event passer跟这个event stop。

然后主要做的事情是什么呢?进行数据的过滤。

你看这个,这个是一个连接器,它连接我们这个event passer跟这个event stop。然后主要做的事情是什么呢?进行数据的过滤。

你看人家第一个组件event passer是不是把数据已经拉去过来了,对吧?

把日志拉去过来,然后它这边进行数据的处理,加工,分发等等这些。

那么做数据处理的工作。

然后数据处理完之后,是不是需要存储起来?存储的话就是交给这个event stop。

那么最后这个组件,第三个组件是不是来进行处理?这是数据的存储。

然后最后还有一个是meta manager,对吧?

这个主要是对外暴露的。

就是提供什么呢?增量的订阅呀,消费信息管理呀等等。

这是这个。

那么这是比如说我们通过这个kander,对吧?

我希望连接到kander上面,然后呢,把我们的日志信息读取过来,然后呢,订阅它的这个日志数据。

这个时候呢,我们直接跟meta manager,跟他交互就可以,是由他来负责的。

这是kander它的一个架构。

但是这个东西呢,不作为重点。

因为这个呢,其实都是它内部实现的。

对不对?

它的内部的这个架构原理。

那么我们呢,主要还是面向应用。

那么我们会安装,会使用它,能够解析它就可以了。

好,这个是关于我们kander它的一个架构。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对技术课程内容进行的结构化中文输出。

---

### 1) 视频摘要

本视频片段是关于“数据聚合服务开发”课程中“Canal”组件的介绍。讲师通过PPT演示，系统地讲解了Canal的核心架构、工作原理以及高可用（HA）机制设计。主要内容包括：Canal如何模拟MySQL Slave与Master进行交互，通过读取Binary Log来实现数据同步；其内部架构由Server、Instance、MetaManager等模块组成；以及HA机制如何确保服务的高可用性，通过限制同一服务器上只能有一个Instance处于运行状态来实现。

---

### 2) 按时间顺序的章节（带时间点）

由于提供的截图未包含精确的时间戳，以下章节结构是根据画面内容推断的逻辑顺序：

*   **00:00 - 00:05**: **1.3 架构 (Architecture)**
    *   展示了Canal服务的顶层架构图，包含 `server`、`Instance`、`MetaManager` 等核心模块。
    *   介绍了 `Instance` 模块的三个子组件：`EventParser`、`EventSink`、`EventStore`。
*   **00:05 - 00:10**: **1.3 架构 (Architecture) → 1.4 HA机制设计 (HA Mechanism Design)**
    *   讲师将页面滚动至下一节“1.4 HA机制设计”。
    *   展示了HA机制的设计原则：`canal server` 和 `canal client` 分别有对应的HA实现。
    *   说明了HA机制的核心约束：同一服务器上的多个 `instance` 中，只能有一个处于 `running` 状态，其余必须处于 `standby` 状态，以减少对MySQL Master的dump请求压力。
*   **00:10 - 00:15**: **1.4 HA机制设计 (HA Mechanism Design)**
    *   讲师继续讲解HA机制，可能涉及具体实现细节或与后续章节（如安装、使用）的衔接。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 图表 1: Canal 工作原理**
    *   **内容**: 描述了Canal如何模拟MySQL Slave。
    *   **关键点**:
        *   Canal 伪装成一个 MySQL Slave。
        *   向 MySQL Master 发送 dump 请求。
        *   MySQL Master 收到请求后，开始推送 Binary Log 给 Canal。
        *   Canal 解析 Binary Log 对象（原始为 byte 流）。
    *   **图示**: 包含 `master` (MySQL)、`Canal`、`Binary log` 三个核心组件，并用箭头表示数据流向。

*   **PPT 图表 2: Canal 架构图**
    *   **内容**: 展示了Canal服务的内部结构。
    *   **关键点**:
        *   **server**: 代表一个Canal服务，管理多个 `instance`。
        *   **instance**: 伪装成一个Slave，从MySQL dump数据。
        *   **instance模块**:
            *   `EventParser`: 数据源接入，模拟slave协议和master进行交互，协议解析。
            *   `EventSink`: (Parser和Store链接器)，进行数据过滤、加工、分发的工作。
            *   `EventStore`: 数据存储。
            *   `MetaManager`: 增量订阅&消费信息管理器。
    *   **图示**: 一个大的 `server` 框，内部包含一个 `Instance` 框，`Instance` 框内包含 `EventParser`、`EventSink`、`EventStore` 三个模块，下方是 `MetaManager` 模块。

*   **PPT 文本内容**:
    *   **1.4 HA机制设计**:
        *   `canal` 的高可用（HA）可分为两部分：`canal server` 和 `canal client` 分别有对应的HA实现。
        *   `canal server`: 为了减少对MySQL dump的请求，不同服务器上的 `instance` 要求同一时间只能有一个处于 `running` 状态，其他处于 `standby` 状态。

---

### 4) 关键场景与演示描述

*   **场景 1: 展示Canal工作原理**
    *   **描述**: 讲师首先展示了一个包含 `master`、`Canal` 和 `Binary log` 的示意图。图中 `Canal` 通过“Read”箭头从 `master` 的 `Binary log` 中读取数据，并用一个红色的对话框标注“I'm slave”，形象地说明了Canal模拟Slave的角色。
    *   **技术点**: 强调了Canal通过模拟Slave协议与Master交互，从而获取并解析Binary Log。

*   **场景 2: 介绍Canal架构**
    *   **描述**: 讲师切换到Canal服务的架构图。图中清晰地展示了 `server`、`Instance`、`MetaManager` 的层级关系。讲师用鼠标依次指向 `EventParser`、`EventSink`、`EventStore` 等模块，进行逐个讲解。
    *   **技术点**: 详细解释了每个模块的功能，如 `EventParser` 负责协议解析和数据接入，`EventStore` 负责数据存储，`MetaManager` 负责管理订阅和消费信息。

*   **场景 3: 讲解HA机制设计**
    *   **描述**: 讲师将页面滚动至“1.4 HA机制设计”部分。屏幕上显示了关于HA机制的文字说明，讲师可能正在口头解释其重要性。
    *   **技术点**: 讲师重点说明了HA机制的核心思想：通过限制同一服务器上只能有一个 `instance` 处于 `running` 状态，来避免对MySQL Master的重复dump请求，从而保证系统的稳定性和性能。
