# 10-仓位总览-接口数据结构定义 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始实现接口的数据结构的定义

首先咱们定义Netty的对外传输数据结构

在stock message的Proto文件下面

咱们增加一下数据结构的定义

在这里我们就直接copy进去

这里是磁场的请求参数体以及响应参数体

回到咱们工程当中

找到stock message Proto

咱们在最下面增加对应的定义

对于获取用户的所有磁场信息

在这里是可以不用定义请求消息对象

通过代理服务直接获取用户的交易账户ID

由代理服务传递用户的交易账户ID

这样就能获取用户下面的所有磁场数据

咱们要去修改一下返回消息

response message

在下面增加磁场数据的消息体

这里是获取

所有磁场的返回数据包

get all positions list

序号为期

这里修正一下

获取磁场的返回数据包

这里是一个list的集合对象

因为磁场信息是会存在多条记录

咱们来看一下磁场的返回数据

包含交易的订单号账户ID

磁场相关的信息

磁场相关的信息

以及盈亏相关的一些信息

好

接下来咱们再去定义GRBC内部的传输数据结构

咱们在这里将代码做个copy

回到工程当中

在GRBC的目录下面

我们创建一个新的PB的脚本文件

这个名称就叫stock

position service.proto

粘连进去

然后我们再去定义GRBC内部的传输数据结构

这里咱们定义了一个获取用户的所有磁场信息接口

请求参数体

咱们可以看到这里只定义了一个交易账户ID

交易账户ID是由代理服务从缓存当中获取

内部进行传输

不需要客户端去传递账户ID的参数

接口交互成功之后会返回磁场的数据信息

这个磁场记录也是一个集合

咱们可以看到

然后会有接口的处理状态

接口的处理返回消息

这里是磁场的详细数据信息

之前也做了讲解

这里就不再做过多的赘述

通讯数据传输结构定义完成之后

接着咱们就来生成相应的加码代码

open in Tomino

执行Proto的P处理脚本

先生成GRBC的代码

接下来咱们再生成Neti的传输数据结构代码

好

可以看到这里已经提示成功

我们检查一下

在加码目录下面

GRBC

CHAT

GET ALL POSITION

这个已经成功生成

咱们再检查一下Neti的

GET ALL POSITION DATA

这些通讯结构代码都已经成功生成

好

那这一讲就是实现了仓位容纳的

接口数据结构的定义

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段属于一个关于使用 gRPC 和 Protobuf 构建金融交易系统（特别是持仓数据总览功能）的技术课程。讲师正在演示如何定义和实现服务端与客户端之间的数据结构。主要内容包括：

*   **定义接口数据结构**：在 `StockMessage.proto` 文件中，定义了用于获取所有持仓数据的 `GetAllPositionData` 消息体，包含交易ID、账户ID、股票ID、成本价、持仓数量、市场、成交均价等字段。
*   **定义服务接口**：在 `StockPositionService.proto` 文件中，定义了 `getAllPositions` RPC 服务，该服务接收 `GetAllPositionRequest` 请求并返回 `GetAllPositionResponse` 响应。
*   **代码生成与实现**：讲师展示了如何通过 Protobuf 编译器生成 Java 代码，并查看了生成的 `GetAllPositionData` 类的结构，该类继承自 `GeneratedMessageV3`，用于序列化和反序列化数据。

整个过程旨在说明如何在微服务架构中，通过定义清晰、结构化的数据协议来实现服务间的通信。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节基于画面内容和逻辑顺序进行划分：

*   **00:00 - 00:05**: **章节 3.2 定义接口数据结构**。讲师在 Typora 文档中介绍本节目标，并在 IDE 中打开 `StockMessage.proto` 文件。
*   **00:05 - 00:15**: **定义 `GetAllPositionData` 消息体**。在 `StockMessage.proto` 文件中，讲师逐步添加并定义了 `GetAllPositionData` 消息的字段，包括 `id`, `tradeOrderId`, `accountId`, `stockId`, `costPrice`, `volume`, `stockMarket`, `avgPrice` 等。
*   **00:15 - 00:25**: **继续定义消息体字段**。讲师继续添加 `validSellVolume` (可卖数量)、`profit` (盈亏)、`execTime` (成交时间)、`status` (状态)、`interest` (持仓累计利息)、`lastPrice` (最新报价)、`profitRate` (盈亏比例) 等字段。
*   **00:25 - 00:35**: **定义服务接口**。讲师切换到 `StockPositionService.proto` 文件，定义了 `getAllPositions` RPC 服务，其请求和响应类型分别为 `GetAllPositionRequest` 和 `GetAllPositionResponse`。
*   **00:35 - 00:45**: **定义请求消息体**。在 `StockPositionService.proto` 文件中，讲师定义了 `GetAllPositionRequest` 消息体，其中包含 `accountId` 字段。
*   **00:45 - 00:55**: **查看生成的 Java 代码**。讲师在 IDE 中导航到生成的 Java 类 `GetAllPositionData`，并查看其继承结构和构造函数。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **文档标题**：`Day16.md - Typora`，表明这是课程的第16天内容。
*   **章节标题**：
    *   `3.2 定义接口数据结构`
    *   `2. gRpc对内数据结构`
*   **关键说明**：
    *   “一个账户会有多个持仓数据，这里采用集合类型定义。”
    *   “请求参数可以不用传递，这里只需识别账号ID即可，服务内部可以获取。”

#### 代码关键内容

*   **`StockMessage.proto` 文件内容**：
    ```protobuf
    message GetAllPositionData {
        // 主键，唯一标识
        int64 id = 1;
        // 交易订单号
        int64 tradeOrderId = 2;
        // 交易账号ID
        int64 accountId = 3;
        // 股票ID
        int64 stockId = 4;
        // 成本价
        int64 costPrice = 5;
        // 持仓数量
        int32 volume = 6;
        // 股票市场(0: 上交所， 1: 深交所， 2: 港股， 3: 美股)
        int32 stockMarket = 7;
        // 成交均价
        int64 avgPrice = 8;
        // 可卖数量(T-1制度使用，T-0不限制)
        int32 validSellVolume = 9;
        // 盈亏
        int64 profit = 10;
        // 成交时间
        int64 execTime = 11;
        // 状态(0:有效，1:无效)
        int32 status = 12;
        // 持仓累计利息
        int64 interest = 13;
        // 最新报价
        int64 lastPrice = 14;
        // 盈亏比例
        int64 profitRate = 15;
        // 股票代码
        string stockCode = 16;
        // 股票名称
        string stockName = 17;
    }
    ```

*   **`StockPositionService.proto` 文件内容**：
    ```protobuf
    syntax = "proto3";
    option java_multiple_files = true;
    option java_package = "com.itcast.bulls.stock.struct.grpc.trade";
    option java_outer_classname = "StockPositionServiceProto";

    service StockPositionService {
        // 获取所有持仓信息接口
        rpc getAllPositions (GetAllPositionRequest) returns (GetAllPositionResponse) {
        }
    }
    ```

*   **`GetAllPositionRequest` 消息体**：
    ```protobuf
    message GetAllPositionRequest {
        // 账户ID
        int64 accountId = 1;
    }
    ```

*   **生成的 Java 类 `GetAllPositionData`**：
    ```java
    public final class GetAllPositionData extends com.google.protobuf.GeneratedMessageV3 implements GetAllPositionDataOrBuilder {
        private static final long serialVersionUID = 0L;
        private GetAllPositionData(com.google.protobuf.GeneratedMessageV3.Builder builder) {
            super(builder);
        }
        private GetAllPositionData() {
            stockCode = "";
            stockName = "";
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：定义接口数据结构**
    *   **描述**：讲师在 Typora 文档中讲解 `3.2 定义接口数据结构` 章节，随后在 IntelliJ IDEA 中打开 `StockMessage.proto` 文件。
    *   **演示**：讲师在 `.proto` 文件中逐行添加 `GetAllPositionData` 消息体的字段，如 `id`, `tradeOrderId`, `accountId` 等，并为每个字段添加了中文注释和编号。演示了如何定义股票市场、成交均价、盈亏等金融交易相关的字段。

*   **场景二：定义服务接口**
    *   **描述**：讲师在 IDE 中切换到 `StockPositionService.proto` 文件，开始定义服务接口。
    *   **演示**：讲师定义了 `StockPositionService` 服务，并添加了 `getAllPositions` RPC 方法，该方法接收 `GetAllPositionRequest` 并返回 `GetAllPositionResponse`。演示了如何在 `.proto` 文件中定义服务和方法。

*   **场景三：查看生成的 Java 代码**
    *   **描述**：讲师在 IDE 中导航到 `com.itcast.bulls.stock.struct.grpc.trade` 包下的 `GetAllPositionData` 类。
    *   **演示**：讲师展示了生成的 Java 类 `GetAllPositionData`，该类继承自 `GeneratedMessageV3`，并包含一个无参构造函数和一个带参数的构造函数。演示了 Protobuf 如何将 `.proto` 文件自动生成 Java 代码，以便在服务端和客户端中使用。

*   **场景四：字段定义与注释**
    *   **描述**：讲师在定义 `GetAllPositionData` 消息体时，为每个字段添加了详细的中文注释，如“主键，唯一标识”、“交易订单号”、“股票市场(0: 上交所， 1: 深交所， 2: 港股， 3: 美股)”等。
    *   **演示**：通过注释，讲师清晰地解释了每个字段的业务含义和数据类型，帮助观众理解数据结构的设计意图。

---

以上是根据视频画面进行的结构化技术分析报告。
