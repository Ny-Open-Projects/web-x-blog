# 03-客户端行情订阅-代理服务实现行情下发 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们来讲解客户端行情订阅功能的设计

以及代理服务去改造实现行情分发功能

之前代理服务已经实现了行情的订阅

接下来就由代理服务将行情数据分发给客户端

这个是之前所讲解过的功能设计流程图

整个流程图咱们再来回顾一下

从客户端到行情代理服务发起订阅

那么行情代理服务就从行情员服务集群当中

拉取到行情数据

行情服务的数据是从第三方行情员对接所获取而来

行情员服务在这里还会去实现行情的持续化处理

将行情数据加工存储至数据库当中

同时还会将行情数据存储至款存当中

行情代理服务作为无状态的设计

它可以去支持

水平节点的扩展

同时可以支撑海量用户的接入

这个就是客户端行情订阅功能设计处理流程

接下来咱们对行情代理服务做一个改造

去实现行情的分发处理功能

在用户登录成功之后

咱们将客户端的Channel做了记录

并且将Channel加入至Channel Group当中进行统一的管理

这里正是通过Channel

去实现行情数据的下发

接下来咱们就去修改代理服务行情数据的监听接口

增加行情数据下发处理功能

咱们回到代码当中

找到Proxy代理服务

在Proxy Code Consumer下面的6C5input的方法当中

做具体的实现

咱们先梳理一下整个代码的实现流程

第一步要生成消息的

虚拟ID

在实际的生产环境当中

消息虚拟ID有着重要的作用

它可以便于咱们去追踪

维护和排查对应的消息处理结果

那么消息虚拟ID需要保持它的唯一性

便于追踪

定位咱们的消息记录

能够更加方便的去维护和排查消息

接着第二步咱们要去构造

消息虚拟ID

我们先来做一个复制处理

复制接收的行情数据

这个是PB数据结构

用于下发给客户端

用到咱们约定的数据格式做解析处理

第三个步骤

将接收到的行情服务的行情数据

转换为咱们构造行情的数据包

这里咱们就要做一个复制处理

复制接收的行情数据

下发至客户端的数据结构

这个就是数据的一个转换处理

第四个步骤

消息组装完成之后

咱们要广播

也就是要群发行情的数据

下发至所有的登录在线的客户端

这就需要用到咱们之前所定义的

channel group

拿到用户的有效连接通道

在这里咱们就来做一个代码上的具体实现

首先咱们去定义一下service id

它是一个长整形

默认序号就从1开始

添加对应的注释

行情数据包

自身id

这个主要就是校验连续性

同时作为消息的唯一id标记

通过自身id

它的自身长序列

咱们就可以知道它的连续性

如果中间出现了中断或者是包的流失

那么咱们就知道行情接收会存在问题

这也起到了一个校验的作用

好咱们就来做具体实现

定一个消息序列id

从属性当中获取

接着咱们需要去构建行情数据包

store quota proto

下发

实时行情数据

咱们先来看一下

store quota proto脚本的一个定义

咱们要下发的行情是属于实时行情数据

这里有实时行情的盘口信息

比如产品的id

产品编号

然后买方的报价

下面的话是买方的数量

卖方的报价

这些都是盘口信息

这些属性定义都是行情下发所必要的一些数据信息

然后在这里

咱们一并将行情的k线数据也做了一个定义

后面章节的讲解当中会使用到

这个是行情k线的数据信息

和行情k线表里面的属性基本上都是一样的

这里面有组成k线的

必要的属性

比如说开盘价

最高价最低价收盘价等等

k线行情数据是一个响应包

它是一个集合的类型

那么集合是通过6P的关键字做一个实现

定义完成消息数据结构之后

咱们还去定义它的包头和包体的信息

这个是请求消息体的定义

获取k线数据是需要传递自定义的参数

所以在这里有一个消息体

但是实时行情下发是不需要去传递

接口参数

它是由服务端去主动推送的

所以是不需要请求的

消息体

下面是它的响应的消息结构

那么实时行情数据

它要下发一个完整的消息

在这里就返回了Quotas BlueTime Response的

数据结构

消息体定义完成之后

还要在消息的头部定义对应的接口号

这里增加了两个接口

一个是实时行情数据下发的接口

另外是获取k线数据的接口

好

Plot脚本这一块

咱们就不做过多的追溯

这些属性这些定义的话

咱们都有对应的注释

大家如果是不清楚

可以再回过头来看一下

咱们回到刚才的业务逻辑的处理

在女C5的input的方法下面

咱们继续去构造行情的数据包

BlueTime Response

先创建好

接着

为了快速实现

咱们在这里做一个复制处理

采用binutils工具

copy

properties

这个是复制两个对象之间的属性

前提是两个对象的属性名称必须一致

属性类型也必须要求一致

这个是源头

第二个参数是要复制的目标对象

这个意思就是将

我们从行情服务当中接收的行情数据

复制给

下发客户端使用的行情数据信息

接着咱们还去组装下发的数据结构

定义stockhead

创建他的头部信息

设置接口的请求类型

这个是咱们服务端主动推送下发的

并非客户端

所发送过来的请求

但是咱们在这里仍然将请求类型下发给客户端

这样便于客户端的一个处理

接口类型是LiuTime

因为客户端会接收到各种各样的消息类型

因为客户端也会接收到各种消息

那么如何去识别呢

他就要根据咱们所下发的

消息的请求类型做对应的判断处理

然后设置序列ID

stock

circuit ID

设置他的状态

global consistence

stays ok

要用build的方法进行构建

最后咱们还定义完整的响应消息

response message

response message

new build

将头部信息设置进去

stock head

然后设置咱们的实时行情数据

进行build的构建

再将整个消息进行一个构建

最后消息组装完成

咱们要广播行情数据

通过channel groups

咱们去遍地channel通道

通过通道

去下发行情数据

response message

这样咱们就完成了行情数据下发给客户端的处理录

那咱们回到讲义当中

在这里咱们要注意一下

我们生成的消息序列

这个序列的主要作用

是要标识消息的唯一性

以及它的连续性

便于咱们在生产环境当中

如果是出现问题的时候

可以去追踪

维护和排查消息

行情数据的下发要遵循probov的规范

咱们在这里也进行了消息的包装转换处理

最后咱们是通过之前所做的

所记录的客户端圈楼

也就是在用户登录的时候

咱们会去记录用户的连接通道

在这里咱们就可以通过

圈楼通道

实现行情数据的广播推送

好

代理服务

改造实现行情分发功能

咱们就已经实现

那这一讲内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是“交易平台”系列课程的第14天，主要讲解如何实现客户端行情订阅功能。核心内容是改造代理服务，使其能够接收来自行情源的数据，并将行情数据分发给所有已登录的客户端。课程通过展示代码实现，重点讲解了在 `ProxyQuoteConsumer` 类中如何处理接收到的行情数据，包括生成唯一消息ID、构建Protobuf数据包、以及通过 `StockProxyServerHandler` 的 `channel` 集合向所有在线客户端广播数据。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开始，展示PPT大纲，当前章节为“3.2 代理服务改造实现行情分发功能”。
*   **00:05 - 00:15**: 展示系统架构图，说明行情数据从“行情源服务集群”流向“缓存服务”和“数据库”，再由代理服务分发给客户端。
*   **00:15 - 00:30**: 进入代码实现部分，打开 `ProxyQuoteConsumer.java` 文件，讲解 `@StreamListener` 注解用于监听行情数据。
*   **00:30 - 00:45**: 代码中，为消息生成唯一序列ID `seqId`，并构建 `StockQuoteProto.QuoteRealtimeResp.Builder`。
*   **00:45 - 01:00**: 使用 `BeanUtils.copyProperties` 方法将接收到的 `receiveMsg` 数据复制到 `realtimeResp` 中。
*   **01:00 - 01:15**: 设置 `StockHeadProto.StockHead` 的请求类型和状态，构建最终的 `ResponseMessage`。
*   **01:15 - 01:30**: 通过 `StockProxyServerHandler.channels` 集合，使用 `forEach` 方法向所有在线客户端的 `channel` 发送广播消息。
*   **01:30 - 01:45**: 展示最终的代码逻辑，完成行情数据的分发。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.2 代理服务改造实现行情分发功能”。
    *   **系统架构图**: 展示了行情源服务集群、缓存服务、数据库、代理服务和客户端之间的数据流向。
    *   **代码注释**: 在 `ProxyQuoteConsumer.java` 中，有详细的中文注释，说明了每一步操作的目的，例如：
        1.  生成消息序列ID，用于追踪和排错。
        2.  构造Protobuf行情数据包。
        3.  复制接收到的行情数据，转换为下发给客户端的数据结构。
        4.  消息组装完成后，广播给所有登录在线的客户端。

*   **代码关键内容**:
    *   **类**: `ProxyQuoteConsumer`。
    *   **方法**: `receiveInput`，这是一个 `@StreamListener` 注解的方法，用于处理接收到的行情数据。
    *   **关键代码片段**:
        ```java
        @StreamListener("quote")
        public void receiveInput(@Payload TradeStockQuoteLast receiveMsg) {
            // 1. 生成消息序列ID
            long stockSeqId = seqId ++;

            // 2. 构造行情数据包
            StockQuoteProto.QuoteRealtimeResp.Builder realtimeResp = StockQuoteProto.QuoteRealtimeResp.newBuilder();
            BeanUtils.copyProperties(receiveMsg, realtimeResp);

            // 3. 设置请求类型和状态
            StockHeadProto.StockHead stockHead = StockHeadProto.StockHead.newBuilder()
                .setRequestType(StockProto.RequestType.QUOTE_REALTIME)
                .setSeqId(stockSeqId)
                .setStatus(GlobalConstants.STATUS_OK)
                .build();

            // 4. 广播消息
            ResponseMessage responseMessage = ResponseMessage.newBuilder()
                .setStockHead(stockHead)
                .setQuoteRealtimeResp(realtimeResp.build())
                .build();

            StockProxyServerHandler.channels.forEach(channel -> {
                channel.writeAndFlush(responseMessage);
            });
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：系统架构介绍 (00:05-00:15)**:
    *   讲师通过PPT展示了一个三层架构图，从“行情源服务集群”获取数据，经过“缓存服务”和“数据库”处理，最终由“代理服务”分发给“客户端”。
    *   重点强调了代理服务在数据分发中的核心作用。

*   **场景二：代码实现演示 (00:15-01:45)**:
    *   讲师在IDEA中打开 `ProxyQuoteConsumer.java` 文件，逐行讲解代码。
    *   **第一步**: 展示 `@StreamListener("quote")` 注解，说明其用于监听名为“quote”的消息流。
    *   **第二步**: 展示 `receiveInput` 方法的参数 `@Payload TradeStockQuoteLast receiveMsg`，说明这是接收到的原始行情数据。
    *   **第三步**: 讲解 `long stockSeqId = seqId ++;` 语句，说明生成唯一序列ID的重要性。
    *   **第四步**: 展示 `StockQuoteProto.QuoteRealtimeResp.Builder realtimeResp = ...` 语句，说明构建Protobuf数据包。
    *   **第五步**: 讲解 `BeanUtils.copyProperties(receiveMsg, realtimeResp);` 语句，说明将原始数据复制到新的数据结构中。
    *   **第六步**: 展示 `StockHeadProto.StockHead stockHead = ...` 语句，说明设置请求类型和状态。
    *   **第七步**: 讲解 `ResponseMessage responseMessage = ...` 语句，说明构建最终的响应消息。
    *   **第八步**: 展示 `StockProxyServerHandler.channels.forEach(channel -> { channel.writeAndFlush(responseMessage); });` 语句，说明向所有在线客户端广播消息。
    *   讲师在代码中添加了中文注释，帮助理解每一步的逻辑。

---

以上是根据视频画面整理出的结构化技术课程分析。
