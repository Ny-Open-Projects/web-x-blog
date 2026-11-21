# 14-Ceph介绍-核心组件与概念 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们来学习Safe的核心组件以及它相应的概念

那我们来看一下主要包括哪些呢

在这里面也有很多对不对

我们就带着大家逐一来讲解

首先Monitor

Monitor是什么意思呢

它是Safe集群当中我们的一个监控组件

一个Safe集群它需要多个Monitor组成的一个小集群

也就是说Safe集群里面的话它有多个Monitor节点

然后呢这个多个Monitor的节点

它们组成了一个Monitor的小集群

它们通过PathSox进行了数据的同步

通过这个协议来进行数据的同步

保证了它的一个一致性

用来保存OSD的原数据

好这个呢是它的主要作用

因为你只有保障OSD数据的正常呢

才能保证整个服务集群的高可用

好再往下面呢

咱们来看一下OSD它是怎样的一个概念呢

OSD它全身就是Object Storage Device

也是一个OBJEC Storage Device

也就是负责响应客户端请求返回具体数据的进程

也就是说从客户端这边的一个请求

到数据的一个响应

都是交给我OBJEC Storage Device去进行处理

一个Safe集群呢

它一般都会有什么

很多个OSD节点呢去组成

那么MDS是怎样一个概念呢

MDS全身就是Safe Metadata Server

它是SafeFS服务依赖的原数据服务

其实呢就是一个原数据服务

好

咱们再往下面看OBJEC

OBJEC并非Java的OBJEC

在这里面的话呢

这个是Safe最底层的存储单元

它就是以OBJEC作为对象

每个OBJEC它怎样组成的呢

它包含原数据以及原始数据

好再往下面看PG

PG是什么意思呢

它全身是Placement Groups

好

它是一个什么逻辑的概念

并不是一个实实在在的一个对象

它是一个实实在在的一个对象

PG包含多个OSD

也就是说多个OSD我就组成了一个PG

引入PG这一层呢

它其实就是为了更好地去分配数据

并且呢去定位出我所要的数据

因为大家想想

分布式文件系统存储

面向大量的文件需要去处理

对不对

怎么去快速分配和定位

这个呢就是PG它所负责的

好

咱们再来看一下RedHouse

RedHouse的话呢

它的全身是Reliable Autonomic

就是去Build Object Store

好

这个呢在上面当前我们也做了一个讲解

它是Safe集群的核心

也是它的精华

对不对

用户实现数据分配

Fill Over等集群的一个操作

这个呢就是通过RedHouse去进行的实现

那么再往它关联的呢

就是LibRedHouse

LibRedHouse呢

它是RedHouse的一个提供库

也就是说是基于RedHouse呢

它实现了这样一个开发库

因为RedHouse呢

它是从协议上很难进行直接访问的

对不对

因为它是很底层的操作

那么因此呢

我们上一层的RBD

RGW和Safe S呢

都是通过什么

LibreDos进行的一个访问

也就是说

你在这里嘛

比较难访问

对不对

那没关系

我一给你包装一层

专门呢去实现了你的访问和操作

目前呢

它提供了像PHP啊

Ruby

Java

Python

C和C++的一个支持

好

咱们再往下面看

Crush

Crush呢

它是什么呢

它是一个数据分布式的算法

它帮助呢

Safe去实现了这种数据的均衡分配

类似一次性Hashi

咱们都知道

Hashi的话呢

可以保证的

你数据能够平均散落到每个节点当中

对不对

让数据的分配到预期的地方

这个呢

就是Crush它的一个概念和作用

RBD

RBD的是RedHouse Block Device

它是Safe对外提供的一个快设备服务

是对外提供的是快设备服务

RGW是RedHouse的Gateway

它是呢

Safe对外提供的对象存储服务

它的接口呢

是和S3和以及呢

Swift是进行了兼容匹配的

也就是说

如果是你之前的话呢

是操作S3或者Swift的话呢

可以无缝迁移到

就是我们的通过RGW

可以迁移到我们的Safe当中进行操作

SafeFS呢

它全称就是Safe File System

这个呢是什么意思呢

它是Safe对外提供的文件系统服务

也就上面我们所讲到的

比如说你想去共享一些文件啊

可以通过NFS实现了文件的一个共享

还有呢

文件的一些公用性的操作

好

这些呢

就是Safe的它的核心组件以及对应的概念

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面内容进行的结构化分析。

---

### 1) 视频摘要

本视频片段主要讲解了 Ceph 分布式存储系统的核心组件与整体架构。讲师通过在 Typora 编辑器中展示 Markdown 文档，系统性地介绍了 Ceph 的六大核心组件：Monitor、OSD、MDS、Object、PG 和 RADOS，并进一步阐述了 Librados、CRUSH、RBD、RGW 和 CephFS 等关键概念。视频中还通过一个架构图，清晰地展示了 Ceph 的分层设计，从应用层到数据层，说明了不同服务（如 RBD、RGW、CephFS）如何通过 Librados 库访问底层的 RADOS 对象存储系统。讲师在讲解过程中，对各组件的功能、相互关系以及在实际应用中的角色进行了详细说明。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下章节划分是根据画面内容变化和逻辑顺序进行的推断：

*   **00:00 - 00:15**: 开场，展示文档大纲，定位到“3.5 核心组件与概念”章节。
*   **00:15 - 00:45**: 讲解 **Monitor** 组件，说明其通过 Paxos 协议同步数据，用于保存 OSD 元数据。
*   **00:45 - 01:15**: 讲解 **OSD** 组件，定义其为 Object Storage Device，负责响应客户端请求。
*   **01:15 - 01:30**: 讲解 **MDS** 组件，定义其为 Ceph Metadata Server，是 CephFS 服务依赖的元数据服务。
*   **01:30 - 01:50**: 讲解 **Object** 和 **PG** 组件，说明 Object 是最底层的存储单元，PG 是逻辑概念用于数据分布和定位。
*   **01:50 - 02:20**: 讲解 **RADOS** 组件，定义其为 Reliable Autonomic Distributed Object Store，是 Ceph 集群的核心。
*   **02:20 - 02:45**: 讲解 **Librados**，说明它是访问 RADOS 的客户端库，支持多种编程语言。
*   **02:45 - 03:00**: 讲解 **CRUSH** 算法，说明其是 Ceph 的数据分布算法，类似一致性哈希。
*   **03:00 - 03:25**: 讲解 **RBD**、**RGW** 和 **CephFS**，分别定义为块存储、对象存储和文件系统服务。
*   **03:25 - 03:45**: 展示并讲解 **Ceph 整体设计架构图**，说明各层之间的关系和数据流向。
*   **03:45 - 04:00**: 讲解应用层，对比 Librados 和 RADOS GW 的不同，以及 Swift 与 RADOS 的 API 差异。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **核心组件列表**：
    *   **Monitor**: 通过 Paxos 同步数据，保存 OSD 元数据。
    *   **OSD**: Object Storage Device，响应客户端请求。
    *   **MDS**: Ceph Metadata Server，CephFS 依赖的元数据服务。
    *   **Object**: 最底层的存储单元，包含元数据和原始数据。
    *   **PG**: Placement Groups，逻辑概念，用于数据分布和定位。
    *   **RADOS**: Reliable Autonomic Distributed Object Store，Ceph 集群的核心。
    *   **Librados**: RADOS 的客户端库，支持 PHP、Ruby、Java、Python、C 和 C++。
    *   **CRUSH**: Ceph 的数据分布算法，类似一致性哈希。
    *   **RBD**: RADOS block device，块存储服务。
    *   **RGW**: RADOS gateway，对象存储服务，兼容 S3 和 Swift。
    *   **CephFS**: Ceph File System，文件系统服务。

*   **架构图**：
    *   **图 1**: Ceph 整体设计架构图。
    *   **图 2**: 展示了应用层、对象存储接口、块存储接口和文件系统接口，以及它们如何通过 `librados` 库访问底层的 `RADOS`，并最终由 `MDS` 提供元数据服务。
    *   **图 3**: 展示了 `librados` 库支持的编程语言。

*   **关键概念**：
    *   **CRUSH 算法**: 类似一致性哈希，用于将数据分配到预期的位置。
    *   **RADOS GW**: 提供 RESTful API，与 Librados 的本地 API 区别。
    *   **Librados vs RADOS GW**: Librados 提供本地 API，RADOS GW 提供 RESTful API，目标应用场景不同。

---

### 4) 关键场景与演示描述

*   **场景 1: 核心组件讲解** (00:15 - 03:00)
    *   讲师在 Typora 编辑器中逐条展示并讲解 Ceph 的核心组件，包括 Monitor、OSD、MDS、Object、PG、RADOS、Librados、CRUSH、RBD、RGW 和 CephFS。
    *   讲师使用鼠标光标高亮和选择文本，以强调重点内容。
    *   讲师在讲解过程中，对每个组件的功能和作用进行了详细说明，例如，Monitor 用于数据同步，OSD 用于数据存储，MDS 用于元数据管理。

*   **场景 2: 架构图展示** (03:00 - 03:45)
    *   讲师切换到“3.4 Ceph 整体设计”章节，展示了一个清晰的架构图。
    *   图中展示了应用层、对象存储接口、块存储接口和文件系统接口，以及它们如何通过 `librados` 库访问底层的 `RADOS`。
    *   讲师用鼠标光标指向图中的不同部分，解释数据流向和各层之间的关系。
    *   讲师特别强调了 `librados` 库的作用，说明它如何支持多种编程语言访问 RADOS。

*   **场景 3: 应用层对比** (03:45 - 04:00)
    *   讲师在“应用层”部分，对比了 Librados 和 RADOS GW 的不同。
    *   讲师解释了 Librados 提供的是本地 API，而 RADOS GW 提供的是 RESTful API。
    *   讲师还提到了 Swift 与 RADOS 的 API 差异，说明 RADOS 提供的功能更为基础和底层。

*   **场景 4: 鼠标操作与截图** (00:45 - 01:50)
    *   讲师在讲解过程中，多次使用鼠标进行选择和截图操作，以突出显示关键内容。
    *   例如，在讲解 PG 时，讲师使用鼠标选择并截图了相关文本。
    *   在讲解 RADOS 时，讲师使用鼠标选择并截图了相关文本。

---

以上是根据视频画面内容进行的结构化分析。
