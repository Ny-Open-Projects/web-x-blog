# 24-Sentinel介绍-开源生态与工作原理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

咱们接着讲解下一个支持点

Sentinel的开源生态

以及它的工作原理

那我们看一下Sentinel开源生态

它支持哪些主线呢

在这里这张图形可以很直观的帮我们展示出来

从这里左侧GRPC的支持

还有Double Sentinel Double Adapt

专门为Double提供的试飞器

为Double提供了限流服务降级的能力

这个也是非常有帮助的

然后Service Mesh汲取了高可用的能力

在这里Service Mesh是一个服务网格治理

Istio是专业化的服务治理的整个的组件

在这里面它有一系列的工具

可以帮助我们去更好地治理的微服

如果说你的微服节点特别巨大

数量特别多

那么可以考虑采用Istio方案

但是如果只是十几个节点

或者说几十个节点

建议采用Sentinel Cloud

就足够了

那么在右侧的话

有Spring Cloud它整个的一些组件

比如像Web MVC

对不对

Cloud Netflix

在这里它也是提供了很多的一些工具和组件

去帮助我们更好地去开发

然后Spring Cloud KTV

再往下面是LockedMQ

消息推列

然后最下侧就是整个的动态规则

它在这里面所能够支持的一些开源组件

比如像Nakos Ladies JK Abloh等等

好

这个是Sentinel的整个生态圈

从中的话我们也可以知道

它的知识面是非常丰富

对不对

很多场景下面你都可以采用Sentinel

帮助我们去实现服务的垄断和降级

接下来我们再来看一下Sentinel的工作原理

Sentinel工作原理从中我们可以看到

在这里是它的一个框架设计

框架设计这一块它有怎样的特点呢

从中我们来看一下

在这里是它的slot chain

整个的一个链路槽

在这个链路槽这里

我们可以看到从Cut node build

然后再到Cast node集群节点的一个build

然后Static slot分析了一些统计分析的插槽

然后Blow slot

限流的一个插槽

Decreate降级认证系统管理等等

在这里面我们就可以很直观的看到了

在这里面我们就可以很直观的看到了

在这里面我们就可以很直观的看到了

它含有什么

JL式的一个设计

每个组件它都负责具体功能的处理

比如说统计的有统计的

限流有限流的

可以支持它的可插法

然后你不需要的就把它去除移除就可以了

不会影响整个系统原有的运行的稳定性

如果说你要去自己去根据所想要的规则

那么能不能去实现一个自定义的功能槽

这个也是可以的

比如说

在认证这一块你想加入自己的一些VIP权限

那么也可以自己去扩展实现对应的功能槽

这样就整体来讲

你不会有对原有的系统产生过多的冲击

因为你在这里只是加入了其中的一个功能槽

你的各个槽之间它都是独立的

只要把它交到链路里面调用就可以了

好

在下面的话

我们就来具体说明一下

在整个设计里面申请了它所有的资源

对应的一个资源名称以及一个ench

这个是它所有资源的一个处理方案

ench可以通过对主流框架的适配自动进行创建

也可以通过注解的方式或调用API显示进行创建

每一个ench它创建的时候

同时也会创建一系列的功能插槽

也就在这里面了

Smart Chain

这些插槽有不同的职责

比如说Node, Slack, Slack, etc.

这个是负责收集资源的路径

Smart的主要作用是将这些资源调用的路径

以数状结构存储起来

用于根据调用路径来做限流和降低

一般的话

我们用户有用户服务的一些限流保护策略

有交易的一些服务限流策略

Class, Build Slot

在这里它是用于存储资源的统计信息以及调用者信息

这个就是

Class, Build Slot

比如说该资源的RT,响应时间窗

QPS, SharedCorn,现成数量,等等

这些信息将用作多维度限流

也是降级的依据

Static Slot

这个是用于记录统计不同维度的Long Time指标监控信息

Flow Slot

这个就是用于根据预设的限流规则

以及前面的Slot统计的状态来进行了限流状态

根据这个

然后结合Flow Slot实现了限流控制

Authorized Slot

它是根据配置的黑牌名单来调用来源信息

并且做到黑名单的控制

Decreased Slot

它是通过统计信息以及预设的规则来做熔断降级

System Slot

它是通过系统的状态比如说Node1

来控制总的入口流量

这个是它的一些主要功能槽的职责和作用

我们再看一下扩展机制这一块

这个就能够实现我们自定义的功能槽

Sentinel将Slot Chain Builder作为SPI接口进行扩展

遵循了SPI机制

使得Slot Chain具备了一个扩展的能力

这个是非常有作用的

您可以自己加入自定义的Slot

并且编排Slot时间的作用

从此可以申请添加自定义的功能

比如说在这里面的权限认证工具

我想根据VIP来设定不同的权限

那么它原有的这一块就不能做到这么灵活

怎么办呢

我们就可以自定义的My Custom Slot

自定义的一个认证权限机制去做对应的处理

这样扩展性就非常强

并且也不会对原有的系统造成很大的冲击

这个就是Sentinel的工作原理以及扩展性

它开源生态的介绍

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析：

---

### 1) 视频摘要

本视频片段是关于 **Sentinel**（一个流行的分布式系统流量控制组件）的深度技术讲解，主要聚焦于其 **开源生态** 和 **核心工作原理**。讲师通过 PPT 演示，系统性地介绍了 Sentinel 如何与主流微服务框架（如 Dubbo、Spring Cloud、gRPC）集成，以及其内部如何通过“插槽链”（Slot Chain）机制实现流量控制、熔断降级、系统保护等核心功能。视频内容技术性强，旨在帮助开发者理解 Sentinel 的架构设计和扩展能力。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:15**: **3.6 开源生态** - 展示 Sentinel 与 Dubbo、Spring Cloud、gRPC 等主流框架的集成关系图。
*   **00:15 - 00:30**: **3.7 工作原理** - 过渡到讲解 Sentinel 的内部工作机制。
*   **00:30 - 00:50**: **设计说明** - 详细解释 Entry 和 Slot Chain 的概念。
*   **00:50 - 01:10**: **Slot 插槽职责详解** - 逐一介绍各个插槽（NodeSelectorSlot, ClusterBuilderSlot, StatisticSlot, FlowSlot, AuthoritySlot, DegradeSlot, SystemSlot）的功能。
*   **01:10 - 01:25**: **扩展机制** - 讲解 Sentinel 如何通过 SlotChainBuilder SPI 接口允许用户自定义插槽。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 图表 1: Sentinel 开源生态图**
    *   **中心**: Sentinel。
    *   **上游集成**:
        *   **Dubbo**: 通过 `Sentinel Dubbo Adapter` 提供限流、降级能力。
        *   **Spring Cloud**: 通过 `Spring Cloud Sentinel Starter` 为 Spring Web MVC、Spring Cloud Netflix、Spring Cloud Gateway 等提供流量防护。
        *   **gRPC**: 通过 `Sentinel gRPC Adapter` 进行集成。
        *   **Service Mesh**: 与 Istio 集成，提供服务的可观测性和控制能力。
    *   **下游配置**:
        *   **动态规则配置**: 支持 `Nacos`、`Redis`、`Apache ZooKeeper`、`Apollo` 等多种配置中心。

*   **PPT 图表 2: Sentinel 工作原理图**
    *   **核心概念**:
        *   **Entry**: 每个资源（如一个接口）对应一个 Entry。Entry 可以通过框架适配、注解或 API 显式创建。
        *   **Slot Chain**: 每个 Entry 创建时，会生成一个由多个插槽（Slot）组成的链。
    *   **架构图**:
        *   **Tree Node Builder**: 构建以“Root”为根的树状结构，包含多个 `entry` 节点。
        *   **Cluster Node Builder**: 构建集群节点，用于统计。
        *   **StatisticSlot**: 用于记录和统计运行时指标（如 RT、QPS、线程数、成功率等）。
        *   **Slot Chain**: 插槽链包含 `SystemSlot`, `AuthorizeSlot`, `DegradeSlot`, `FlowSlot` 等。
        *   **Runtime statistics**: 运行时统计信息，由 StatisticSlot 收集。
        *   **rules**: 规则，由 FlowSlot、DegradeSlot 等根据规则进行控制。

*   **PPT 文本内容: 设计说明**
    *   **Entry 与 Slot Chain**: 所有资源对应一个资源名称和一个 Entry。Entry 创建时会创建一个 Slot Chain。
    *   **Slot 插槽职责**:
        *   `NodeSelectorSlot`: 收集调用路径，用于限流降级。
        *   `ClusterBuilderSlot`: 存储统计信息（RT, QPS, thread count），用于多维度限流、降级。
        *   `StatisticSlot`: 记录、统计 runtime 指标监控信息。
        *   `FlowSlot`: 根据限流规则和前面 slot 的统计状态，进行流量控制。
        *   `AuthoritySlot`: 根据黑白名单和调用来源，进行黑白名单控制。
        *   `DegradeSlot`: 根据统计信息和预设规则，进行熔断降级。
        *   `SystemSlot`: 根据系统状态（如 load1），控制总入口流量。
    *   **扩展机制**:
        *   Sentinel 通过 `SlotChainBuilder` SPI 接口允许用户自定义插槽。
        *   用户可以自行添加自定义插槽（如 `MyCustomSlot`）并编排其在 Slot Chain 中的顺序。

---

### 4) 关键场景与演示描述

*   **场景 1: 开源生态集成演示**
    *   **描述**: 讲师首先展示了一个中心为 Sentinel 的生态图。他用箭头指向各个框架，解释了 Sentinel 如何通过特定的适配器（如 `Sentinel Dubbo Adapter`）为 Dubbo 服务提供流量控制能力，以及如何通过 `Spring Cloud Sentinel Starter` 为 Spring Cloud 生态提供保护。他强调了 Sentinel 与 `Istio`、`Service Mesh` 的集成，以及支持多种配置中心（Nacos, Redis, ZooKeeper, Apollo）来实现动态规则管理。

*   **场景 2: 工作原理与 Slot Chain 演示**
    *   **描述**: 讲师切换到工作原理图，重点讲解了 Entry 和 Slot Chain 的概念。他通过一个树状结构图（Tree Node Builder）展示了资源如何被组织成树形结构，其中每个节点代表一个 Entry。接着，他解释了 `StatisticSlot` 如何收集运行时统计信息，并将这些信息传递给下游的插槽。他强调了 Slot Chain 是一个由多个插槽按顺序组成的链，每个插槽负责不同的功能。

*   **场景 3: Slot 插槽职责详解**
    *   **描述**: 讲师逐个介绍 Slot 插槽的功能。他通过 PPT 上的列表，详细说明了 `NodeSelectorSlot` 如何收集路径用于降级，`ClusterBuilderSlot` 如何存储统计信息用于限流，`StatisticSlot` 如何记录监控数据，`FlowSlot` 如何执行流量控制，`AuthoritySlot` 如何执行黑白名单控制，`DegradeSlot` 如何执行熔断降级，以及 `SystemSlot` 如何根据系统负载控制入口流量。

*   **场景 4: 扩展机制演示**
    *   **描述**: 讲师展示了 Sentinel 的扩展机制。他通过一个图示，说明了 `SlotChainBuilder` SPI 接口允许用户自定义插槽。图中显示了一个 `MyCustomSlot` 自定义插槽被添加到 Slot Chain 中，并且可以自由编排其顺序。他强调了这种机制使得 Sentinel 具备了强大的可扩展性，开发者可以根据需求添加自定义功能。
