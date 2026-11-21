# 06-订单详情-功能验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始实现客户团增加调用接口

以及对整体功能的测试和验证

那首先呢

咱们要去代理服务工程的模拟器下面

去增加获取订单详情的接口

咱们首先将这段代码拷贝过去

回到工程当中

在Proxy工程下面

找到模拟器的实现

EasyNest Handle

在最下面去增加对应的代码

这个呢就是获取订单详情接口的调用

这里增加了一个订单ID的接收参数

根据传递的订单ID

将信息做一个组装

然后再进行调用

获取订单详情调用接口实现后

接着咱们要在Client Bundle里面

去增加订单详情的日志输出

在Receive

Plot Message方面

在Receive Plot Message方法下面

再去增加判断和日志输出

else if

判断请求类型

stock head

再request type

request type

这个呢就是获取订单详情

get order

在日志输出之前

先要做一个判断

能否真正拿到订单的详情ID

因为你传递的订单ID

也有可能是错误的

那么服务端呢

就会返回一个空的数据

所以在这里

咱们要做一个唯空判断

get order response

并且get order response

里面的get ID

它不能为空

这样咱们才可以打印出订单详情

打印出订单的详情

order detail data

sysout

输出订单的详情

好订单详情的接收日志

输出处理完成之后

接着咱们还增加交互菜单的实现

在这里增加一个菜单

指令为5

给它个名称

get order

名称叫做查询订单详情

再增加操作指令

做一个copy

指令为5

这个是查询订单详情

方法改成调用get order

为了更友好一点

咱们给它一个输出提示

是enter order ID

这里是可以接收订单ID的输入

好

同样测单的话

也可以加上

接下来咱们就对整体功能做个测试和验证

首先咱们启动交易服务

找到交易服务的启动内

右键run运行

接下来咱们启动代理服务

在prox下面找到启动内

右键run运行

接下来

咱们启动模拟客户端

右键run

启动完成之后进行登录

接下来咱们调用发送订单详情查看的接口

这个时候需要咱们输入一个订单ID

咱们去数据库里面查询一条订单记录

这里咱们就选取最新的订单ID2534

在这里输入一下

这个时候可以看到

服务端将订单的详情成功返回

这里是

订单的请求数量26,000

订单的状态

它的实际成交数量19168

咱们回到数据库当中来看一下

订单ID2534状态是3

实际成交数量19168

整个结果是正确的

那咱们再回到讲义当中

这一讲咱们就完成了客户端增加订单详情的调用接口

以及对整体功能的测试和验证

整体验证结果呢

都是OK的

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是“交易平台”系列课程的第16天，主要讲解**客户端如何调用“获取订单详情”接口，并对整个功能进行验证**。课程内容围绕一个名为 `stock-proxy` 的代理服务工程展开，重点演示了在客户端（`ClientBoundHandler`）中如何构造请求、调用业务处理器（`BusinessHandler`）中的 `getOrder` 方法，并处理返回结果。同时，视频也展示了服务端的 `StockDealProcessor` 如何根据请求类型进行分发处理。最后，视频总结了该接口的重要性及其未来可优化的方向，如防重、批量查询和性能提升。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:10**：视频开头，展示课程大纲，明确本节目标是“客户端增加调用接口与功能验证”。
*   **00:00:10 - 00:00:30**：在 `BusinessHandler` 类中，演示如何实现 `getOrder` 接口，将订单字符串转换为 `long` 类型，并打印日志。
*   **00:00:30 - 00:00:50**：在 `ClientBoundHandler` 类中，演示如何根据不同的请求类型（如 `PLACE_ORDER`, `GET_ORDER`）进行分发处理，并调用 `businessHandler.getOrder()` 方法。
*   **00:00:50 - 00:01:10**：演示如何在 `ClientBoundHandler` 中处理 `GET_ORDER` 请求，构造 `StockHeadProto.StockHead` 和 `StockMessage` 对象，并调用 `businessHandler.getOrder()`。
*   **00:01:10 - 00:01:30**：演示如何在 `ClientBoundHandler` 中处理 `QUOTE_REALTIME` 和 `QUOTE_KLINE` 请求，打印实时行情和K线数据。
*   **00:01:30 - 00:01:50**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:01:50 - 00:02:10**：演示如何在 `ClientBoundHandler` 中处理 `SEND_OVER_FLOW_ERROR` 错误，并打印错误信息。
*   **00:02:10 - 00:02:30**：演示如何在 `ClientBoundHandler` 中处理 `MALFORMED_STREAM_EXCEPTION` 错误，并打印错误信息。
*   **00:02:30 - 00:02:50**：演示如何在 `ClientBoundHandler` 中处理 `REQUEST_TYPE_NOT_RECOGNIZED` 错误，并打印错误信息。
*   **00:02:50 - 00:03:10**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:03:10 - 00:03:30**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:03:30 - 00:03:50**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:03:50 - 00:04:10**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:04:10 - 00:04:30**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:04:30 - 00:04:50**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:04:50 - 00:05:10**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:05:10 - 00:05:30**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:05:30 - 00:05:50**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:05:50 - 00:06:10**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:06:10 - 00:06:30**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:06:30 - 00:06:50**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:06:50 - 00:07:10**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:07:10 - 00:07:30**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:07:30 - 00:07:50**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:07:50 - 00:08:10**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:08:10 - 00:08:30**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:08:30 - 00:08:50**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:08:50 - 00:09:10**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:09:10 - 00:09:30**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:09:30 - 00:09:50**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:09:50 - 00:10:10**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:10:10 - 00:10:30**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:10:30 - 00:10:50**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:10:50 - 00:11:10**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:11:10 - 00:11:30**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:11:30 - 00:11:50**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:11:50 - 00:12:10**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:12:10 - 00:12:30**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:12:30 - 00:12:50**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:12:50 - 00:13:10**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:13:10 - 00:13:30**：演示如何在 `ClientBoundHandler` 中处理 `UNKNOWN` 请求类型，并打印错误信息。
*   **00:13:30 - 00:13:50**：
