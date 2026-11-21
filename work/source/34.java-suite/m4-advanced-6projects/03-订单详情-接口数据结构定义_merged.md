# 03-订单详情-接口数据结构定义 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们就去实现订单详情的接口数据结构的定义

首先咱们来定义Netty对外的传输数据结构

这里的属性代码咱们就不再逐一敲选

从讲义当中copy

找到咱们的数据结构工程

Proto, Netty,在stock message, proto文件下面

咱们去增加对应的请求参数以及响应参数的消息体

这个是获取订单详情结构的请求参数体

这个是订单详情结构的返回数据结构

咱们可以看到它返回的是订单的详情

包括订单ID,交易账户

还有挂单相关的信息,买卖方向

实际的成交数量,请求价格

还有股票相关的信息等等

接下来我们还要去修改stock message的

传输报告

增加获取订单详情的请求数据结构消息体

get,order,save,序号为6

下面还要增加响应的消息体

获取详情的返回数据包

这里是get,order,response,getorder,response对象

下面我们还去head头部里面增加接口请求类型

获取

订单详情接口

名称就叫get,order,序号为5

对外传输结构定义完成之后

接着咱们来定义GRBC的对内传输数据结构

首先我们在交易服务里面去增加获取订单详情的

接口

这里已经提前将定义的代码移植过来

咱们来看一下

这个是RBC的获取订单详情接口

传输的消息体是get,order,request的

响应消息体是get,order,response

咱们来看一下这两个数据结构

get,order,request它会传递两个参数

一个是交易账户的ID

另外一个是订单的ID

下面就是订单返回详情的数据结构

这里就是订单的详情信息

这里就不再赘述

接下来咱们通过PB脚本去生成对应的加码代码

在Proto下面右键Open in Tomino

Proto

编译生成GRBC的加码代码

接着画的是Neti的传输数据结构代码

好就已经生成完成

咱们来检查一下

这个是GRBC

Shared里面

可以看到get,order,response这些代码就已经生成完成

接着咱们再检查一下Neti的传输结构

在这里可以看到get,order,date

get,order,response

整个代码都已经成功生成

好咱们回到讲习当中

这一讲就是对订单详情

然后再来讲一下这个数据结构的定义

咱们已经将对应的加码代码生成好

下面我们就可以对它的逻辑做具体的实现

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是“交易平台”系列课程的第16天，主要讲解**订单详情接口**的实现。课程内容聚焦于定义接口的数据结构，包括客户端请求和服务器返回的数据格式。讲师通过演示如何在 `.proto` 文件中定义 `GetOrderData` 和 `GetOrderResp` 消息体，并展示了如何使用 gRPC 服务定义文件（如 `StockTradeDealService.proto`）来声明服务接口。整个过程旨在为后续的代理服务转发和客户端调用打下数据结构基础。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开场，展示课程大纲，明确本节主题为“第1章 订单详情接口”。
*   **00:05 - 00:15**: 讲师介绍本章目标，即定义接口数据结构，为后续实现做准备。
*   **00:15 - 00:30**: 展示 `StockMessage.proto` 文件，讲解如何在其中定义 `GetOrderData` 和 `GetOrderResp` 消息体。
*   **00:30 - 00:45**: 展示 `StockTradeDealService.proto` 文件，讲解如何定义 gRPC 服务接口，包括 `getOrder` 和 `getAllOrders` 方法。
*   **00:45 - 01:00**: 讲师在 IDE 中演示如何生成 Java 代码，展示 `GetAllOrdersResponse` 类的生成过程。
*   **01:00 - 01:15**: 回顾并总结本节内容，强调数据结构定义的重要性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **课程大纲**：包含“第1章 订单详情接口”和“第2章 仓位总览功能”。
*   **章节目标**：定义接口数据结构、实现 gRPC 接口、代理服务转发、客户端调用验证。

#### 代码内容

*   **`StockMessage.proto` 文件**：
    *   定义了 `StockMessage` 消息体，包含 `StockHead` 头部和 `StockData` 消息体。
    *   `StockData` 中定义了 `LoginData`、`PlaceOrderData` 等消息。
    *   定义了 `GetOrderData` 请求消息：
        ```protobuf
        message GetOrderData {
            int64 orderId = 2;
        }
        ```
    *   定义了 `GetOrderResp` 返回消息：
        ```protobuf
        message GetOrderResp {
            int64 id = 1;
            int64 accountId = 2;
            int64 stockId = 3;
            int32 status = 4;  // 订单状态: 0:待成交, 1:部分成交, 2:完全成交, 3:手工撤单, 4:系统撤单
            int32 type = 5;    // 挂单类型: 0:市价单, 1:限价单
            int32 direction = 6; // 买卖方向: 0:买入, 1:卖出
            int32 initVolume = 7;
            int32 execVolume = 8;
            double execPrice = 9;
            int64 requestPrice = 10;
            int64 execTime = 11;
            string stockCode = 12;
            string stockName = 13;
        }
        ```

*   **`StockTradeDealService.proto` 文件**：
    *   定义了 `StockTradeDealService` 服务。
    *   定义了 `getOrder` 方法：
        ```protobuf
        rpc getOrder (GetOrderRequest) returns (GetOrderResponse) {}
        ```
    *   定义了 `getAllOrders` 方法：
        ```protobuf
        rpc getAllOrders (GetAllOrdersRequest) returns (GetAllOrdersResponse) {}
        ```

*   **Java 生成代码**：
    *   `GetAllOrdersResponse` 类继承自 `GeneratedMessageV3`，并实现了 `GetAllOrdersResponse` 接口。
    *   代码中包含 `serialVersionUID` 和 `GetAllOrdersResponse.Builder` 的构造方法。

---

### 4) 关键场景与演示描述

*   **场景一：定义数据结构**
    *   讲师首先在 `StockMessage.proto` 文件中定义了 `GetOrderData` 和 `GetOrderResp` 消息体。
    *   详细演示了每个字段的含义，如 `orderId`、`accountId`、`stockId`、`status`、`type`、`direction` 等。
    *   特别强调了 `status` 和 `type` 字段的枚举含义。

*   **场景二：定义 gRPC 服务接口**
    *   讲师切换到 `StockTradeDealService.proto` 文件。
    *   演示了如何定义 `getOrder` 和 `getAllOrders` 两个 gRPC 方法。
    *   展示了方法的输入参数和返回值类型。

*   **场景三：生成 Java 代码**
    *   讲师在 IDE 中执行了 `protoc` 命令，将 `.proto` 文件编译为 Java 代码。
    *   展示了终端输出，确认 `GetAllOrdersResponse`、`StockMessage` 等类已成功生成。
    *   展示了生成的 `GetAllOrdersResponse` 类的结构，包括 `serialVersionUID` 和 `Builder`。

*   **场景四：总结与回顾**
    *   讲师总结了本节内容，强调了数据结构定义的重要性。
    *   提醒观众，这些数据结构是后续实现 gRPC 服务和客户端调用的基础。

---

以上是根据视频画面整理的技术课程结构化分析。
