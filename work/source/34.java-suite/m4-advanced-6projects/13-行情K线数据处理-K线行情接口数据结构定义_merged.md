# 13-行情K线数据处理-K线行情接口数据结构定义 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们开始学习K线行情接口

ProtoBuffer数据结构的生成实现

之前咱们已经将接口做了定义

在这里我们就来具体讲解下

回到StockStack的公用PB数据结构工程

找到StockKlineServiceProto

脚本定义文件

我们要提供获取股票K线数据的接口

这里定义了一个GetKline的方法

内部通过GRPC形式进行调用和实现

传递的参数是GetKlineRequest

返回的参数对象是GetKlineResponse

GetKline请求参数对象需要传递一些什么信息呢

他需要传递股票ID股票编号信息

我们可以根据这两个属性定义到是哪是股票的行情

然后还需要传递他的时间查询范围

这样就更为灵活

无论说你想查询当天的K线数据

还是想查询一年之内的K线数据

通过这个接口都可以实现

下面是他的返回对象

返回对象

它其实是一个K线数据的集合

这里是接口的处理状态

以及处理了返回消息

下面定义的是一个KlineData的数据集合

KlineData具体有哪些信息呢

我们可以看一下

KlineData定义了股票产品ID

产品编号产品名称

还有行情的相关信息

比如说开盘价最高价最低价收盘价

还有组成K线的必要数据

像成交量成交金额报价时间

昨日的收盘价

这个就是内部GRBC通讯

也就是代理服务节点请求行情服务

获取K线数据的接口定义

接下来再看一下外部的通讯

代理服务和客户端数据结构的定义

在内底下面

Stock Message

同样在这里定义了一个

获取K线的数据请求包

然后再往下面看

这个是K线请求包的具体属性信息

这里面的信息和GRBC借口里面的信息

基本上是一致的

有股票的ID股票编号

行情K线的时间范围

再往下面就是K线行情的返回数据包

这里面的信息和GRBC里面返回的K线数据信息都是一致的

数据结构定义完成之后

就可以通过Plot工具生成相关的代码

我们给大家演示一下

Open in terminal

Plot

GRBC

WordBet

GRBC的K线数据进行返回

我们可以看到

这里是一个K线数据的集合

这里定义的是K线数据的具体属性

这里面的信息和GRBC里面返回的K线数据信息都是一致的

接口代码就已经生成完成

接着来生成Neti的通讯代码

这个是Neti

可以看到Neti层的PB通讯代码也已经生成成功

好

那我们回到讲义当中

在这里就讲解了K线行情接口

PlotBuff数据结构的定义

包括内部GRBC的通讯数据结构

以及外部Neti传输的数据结构

好

这一讲内容就先讲到这里

谢谢大家

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票行情系统的开发教程，重点讲解如何使用 Protocol Buffers (protobuf) 定义 gRPC 服务的接口和数据结构。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何创建和编辑 `.proto` 文件，定义服务接口 `StockKlineService`、请求消息 `GetKlineRequest` 和响应消息 `KlineData`。视频内容旨在为开发者提供一个清晰的、基于 gRPC 的行情数据传输协议设计范例，为后续的后端服务实现和客户端调用打下基础。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 视频开头，讲师在 Typora 文档中展示课程大纲，定位到第 3.4 节“K线行情接口 protobuf 数据结构”。
*   **00:03 - 00:06**: 讲师切换到 IntelliJ IDEA，打开 `StockKlineService.proto` 文件，开始讲解如何定义 gRPC 服务。
*   **00:06 - 00:10**: 讲师在 `.proto` 文件中定义了服务接口 `StockKlineService` 及其唯一的 RPC 方法 `getKline`。
*   **00:10 - 00:15**: 讲师向下滚动，开始定义请求消息 `GetKlineRequest`，并逐行添加字段，如 `stockId`、`stockCode`、`timeStart` 和 `timeEnd`。
*   **00:15 - 00:20**: 讲师继续定义响应消息 `KlineData`，添加了 `stockId`、`stockCode`、`stockName` 等产品信息字段。
*   **00:20 - 00:25**: 讲师继续在 `KlineData` 中添加行情数据字段，包括开盘价 `priceOpen`、最高价 `priceHigh`、最低价 `priceLow`、收盘价 `priceClose`、成交量 `volume`、成交金额 `amount` 和报价时间 `time`。
*   **00:25 - 00:30**: 讲师切换到另一个 `.proto` 文件 `StockMessage.proto`，展示了一个更复杂的 `StockMessage` 消息结构，其中包含多个 `oneof` 选项，用于区分不同类型的请求或响应。
*   **00:30 - 00:35**: 讲师在 `StockMessage.proto` 中继续定义 `ResponseMessage`，并展示了其内部的 `oneof` 结构，用于返回不同类型的响应数据，如 `KlineDataRespLists`。
*   **00:35 - 00:40**: 讲师在 `StockMessage.proto` 中定义了 `PlaceOrderData` 消息结构，用于下单请求。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`3.4 K线行情接口 protobuf 数据结构`。
    *   服务定义：`service StockKlineService { rpc getKline(GetKlineRequest) returns (GetKlineResponse); }`。
    *   请求结构：`message GetKlineRequest { int64 stockId = 1; string stockCode = 2; int64 timeStart = 3; int64 timeEnd = 4; }`。
    *   响应结构：`message KlineData { int64 stockId = 1; string stockCode = 2; string stockName = 3; int64 priceOpen = 4; int64 priceHigh = 5; int64 priceLow = 6; int64 priceClose = 7; int64 volume = 8; int64 amount = 9; int64 time = 10; int64 lastClosePrice = 11; }`。
    *   复合消息结构：`message StockMessage { ... oneof ResponseData { ... KlineDataRespLists klineDataRespLists = 5; } }`。

*   **代码关键内容**:
    *   **文件路径**: `bulls-stock-struct-proto/src/main/resources/proto/grpc/StockKlineService.proto`。
    *   **语法和选项**:
        ```protobuf
        syntax = "proto3";
        option java_multiple_files = true;
        option java_package = "com.itcast.bulls.stock.struct.grpc.quote";
        option java_outer_classname = "StockKlineServiceProto";
        ```
    *   **服务定义**:
        ```protobuf
        service StockKlineService {
          rpc getKline(GetKlineRequest) returns (GetKlineResponse) {}
        }
        ```
    *   **请求消息 `GetKlineRequest`**:
        ```protobuf
        message GetKlineRequest {
          int64 stockId = 1;
          string stockCode = 2;
          int64 timeStart = 3;
          int64 timeEnd = 4;
        }
        ```
    *   **响应消息 `KlineData`**:
        ```protobuf
        message KlineData {
          int64 stockId = 1;
          string stockCode = 2;
          string stockName = 3;
          int64 priceOpen = 4;
          int64 priceHigh = 5;
          int64 priceLow = 6;
          int64 priceClose = 7;
          int64 volume = 8;
          int64 amount = 9;
          int64 time = 10;
          int64 lastClosePrice = 11;
        }
        ```
    *   **复合消息 `StockMessage`**:
        ```protobuf
        message StockMessage {
          // 头部消息
          StockHead stockHead = 1;

          // 消息体
          oneof ResponseData {
            LoginData loginData = 2;
            PlaceOrderData placeOrderData = 3;
            QuoteRealtimeResp quoteRealtimeResp = 4;
            KlineDataRespLists klineDataRespLists = 5;
          }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：服务接口定义** (00:03-00:10)
    *   讲师在 IntelliJ IDEA 中打开 `StockKlineService.proto` 文件。
    *   他首先定义了服务的 `syntax` 和 `option`，指定了生成的 Java 包名和类名。
    *   接着，他定义了服务 `StockKlineService`，并声明了一个名为 `getKline` 的 RPC 方法，该方法接收 `GetKlineRequest` 类型的请求并返回 `GetKlineResponse` 类型的响应。

*   **场景二：请求与响应数据结构定义** (00:10-00:25)
    *   讲师向下滚动，开始定义请求消息 `GetKlineRequest`。
    *   他逐个添加字段，包括股票ID、股票代码、开始时间和结束时间。
    *   之后，他定义了响应消息 `KlineData`，并添加了产品信息（ID、代码、名称）和行情数据（开盘价、最高价、最低价、收盘价、成交量、成交金额、报价时间、昨收盘价）。

*   **场景三：复合消息结构演示** (00:25-00:35)
    *   讲师切换到 `StockMessage.proto` 文件。
    *   他展示了如何使用 `oneof` 关键字来定义一个消息体，该消息体可以包含多种不同类型的响应数据。
    *   他定义了 `ResponseData` 的 `oneof`，并包含了 `LoginData`、`PlaceOrderData`、`QuoteRealtimeResp` 和 `KlineDataRespLists` 等多种响应类型，这体现了系统支持多种业务场景的能力。

*   **场景四：代码编辑与导航** (00:35-00:40)
    *   讲师在 `StockMessage.proto` 中继续定义 `PlaceOrderData` 消息结构，用于下单请求，展示了如何为不同的业务功能定义独立的消息类型。
