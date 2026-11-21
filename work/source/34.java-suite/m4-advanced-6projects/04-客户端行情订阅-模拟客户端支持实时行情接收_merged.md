# 04-客户端行情订阅-模拟客户端支持实时行情接收 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着去实现Netting模拟客户端

改造支持实时行情数据的接收

前面章节咱们已经对代理服务做了改造

能够支持行情的分发

那在这里咱们就要去修改之前所实现的模拟客户端

增加对实时行情数据的接收处理

咱们回到代码当中

找到Client Bottom Header

修改Resale

Proto Message方法

咱们要增加实时行情数据的打印

stockhead.getRequestType

根据实时行情下发的请求类型做对应判断

拿到实时行情数据之后

咱们打印出相关信息

实时行情

打印出股票产品名称

getStockName

接下来再打印出完整的实时行情数据

Message.getQuarter.newTime

初始讯方法

好

只需要改造模拟客户端

增加对实时行情数据接收的打印处理就可以了

那这一讲内容呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“交易平台”的技术课程的第14天内容，主要聚焦于使用 Netty 框架改造客户端以支持接收实时行情数据。讲师通过 IntelliJ IDEA 开发环境，演示了如何修改 `ClientBoundHandler` 类中的 `recvProtoMsg` 方法。该方法负责解析从服务端接收到的 Protobuf 格式的消息，并根据消息的请求类型（`RequestType`）进行不同的处理：如果是下单请求（`PLACE_ORDER`），则打印订单ID；如果是实时行情请求（`QUOTE_REALTIME`），则打印股票名称和行情数据。整个过程展示了如何在 Netty 服务端与客户端之间进行消息的接收、解析和处理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，显示课程标题“交易平台 - Day 14”和学习目标大纲，当前章节为“3.3 Netty模拟客户端改造支持实时行情的接收”。
*   **00:00:05 - 00:00:15**：讲师在 IDE 中定位到 `ClientBoundHandler` 类，并展示其 `recvProtoMsg` 方法的初始代码结构，用于接收并打印服务端消息。
*   **00:00:15 - 00:00:30**：讲师开始修改代码，添加对 `StockHeadProto.RequestType` 枚举类型的判断逻辑，以区分不同类型的请求。
*   **00:00:30 - 00:00:45**：讲师为 `PLACE_ORDER` 类型的请求添加了处理逻辑，打印订单ID。
*   **00:00:45 - 00:01:00**：讲师为 `QUOTE_REALTIME` 类型的请求添加了处理逻辑，打印股票名称和行情数据。
*   **00:01:00 - 00:01:15**：讲师对代码进行最终调整，确保打印格式清晰，并完成演示。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   课程标题：`交易平台 - Day 14`。
    *   学习目标：`第1章 客户端行情订阅功能能实现`，`第2章 行情K线数据的处理`。
    *   当前章节标题：`3.3 Netty模拟客户端改造支持实时行情的接收`。
    *   代码修改目标：`修改com.icast.bulls.stock.proxy.test.ClientBoundHandler类`。

*   **关键代码片段**：
    ```java
    private void recvProtoMsg(ResponseMessage msg) throws Exception {
        StockHeadProto.StockHead stockHead = msg.getStockHead();
        System.out.println("******* Receive Server Message *******");
        System.out.println("== seqId: " + stockHead.getSeqId());
        System.out.println("== requestType: " + stockHead.getRequestType());
        System.out.println("== status: " + stockHead.getStatus());
        System.out.println("== message: " + msg.getMessage());

        if (stockHead.getRequestType() == StockHeadProto.RequestType.PLACE_ORDER) {
            System.out.println("== order id: " + msg.getPlaceOrderResp().getDealId());
        } else if (stockHead.getRequestType() == StockHeadProto.RequestType.QUOTE_REALTIME) {
            System.out.println("== 实时行情 [" + msg.getQuoteRealtimeResp().getStockName() + "]: ");
            System.out.println(msg.getQuoteRealtimeResp().toString());
        }
    }
    ```

*   **关键公式 / 枚举类型**：
    *   **枚举类型 `StockHeadProto.RequestType`**：
        ```java
        RequestType.PLACE_ORDER
        RequestType.QUOTE_REALTIME
        ```
    *   **消息结构 `ResponseMessage`**：
        *   包含 `StockHead` 对象。
        *   包含 `getPlaceOrderResp()` 方法用于获取下单响应。
        *   包含 `getQuoteRealtimeResp()` 方法用于获取实时行情响应。

---

### 4) 关键场景与演示描述

*   **场景一：环境与目标设定 (00:00:00 - 00:00:05)**
    *   讲师首先展示了课程的标题和学习目标，明确了本节内容是关于“Netty模拟客户端改造支持实时行情的接收”。
    *   画面显示了 IDE 中的 `ClientBoundHandler` 类，这是本次修改的核心文件。

*   **场景二：代码修改与逻辑分支 (00:00:15 - 00:01:15)**
    *   讲师在 `recvProtoMsg` 方法中添加了对 `StockHeadProto.RequestType` 枚举的判断。
    *   **分支一（`PLACE_ORDER`）**：当请求类型为下单时，代码调用 `msg.getPlaceOrderResp().getDealId()` 获取订单ID并打印。
    *   **分支二（`QUOTE_REALTIME`）**：当请求类型为实时行情时，代码调用 `msg.getQuoteRealtimeResp().getStockName()` 获取股票名称，并打印 `“== 实时行情 [股票名称]: ”`，然后打印完整的行情对象 `toString()`。
    *   讲师通过IDE的自动补全功能，展示了如何快速定位和使用 `StockHeadProto.RequestType` 枚举值。
    *   最终，代码成功实现了根据消息类型进行不同处理的功能。

---

以上是根据视频画面进行的详细结构化分析。
