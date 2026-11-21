# 09-限价委托下单-数据结构定义 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们去实现接口数据结构的定义

首先咱们创建一个新的PB结构文件

回到咱们工程当中

在PB数据结构工程下面

Proto CRBC的目录下

咱们再创建一个文件

名称就叫Stock Appending Service Proto

首先要去定义PB的头部结构信息

先将头部信息copy进来

调整一下它的包路径结构

这里改成确的

调整一下它的名称

这个名称采用PB的文件名称

叫Stock Appending Service

接下来我们来定义GRBC的数据省结构

限价、委托、下单、无结构

定义Service

Stock Appending Service

定义限价、委托、下单、无结构

RBC

RBC

Limit

Pace Order

传递请求参数

返回

响应结果对象

咱们来定义请求参数体

在最下面定义

限价、委托、下单的请求数据结构

定义Message对象

请求参数对象

Limit

Pace

Order

Request

这里面定义要包括

下单的信息

首先是交易账户的ID

接下来定义股票产品ID

Int64长整形

Stock ID

序号为2

接着定义股票的买卖方向

Int32

Convection

序号为3

定义下单类型

Int32

Type等于4

然后是请求数量

Int32

Excused

Volume

然后是请求价格

Int64

Excused Files

最后要去定义限价委托的返回数据包

Message

Limit

Pace Order

Response

首先定义它的处理状态

String

States.1

接着的话定义返回消息

String

Message.2

接下来要返回所生成的定义ID

Int64

Odd ID

这里咱们只需要定义对内传输的GRBC数据结构

对外NAT与客户端的传输数据结构

仍然去采用下单的结构体

接下来我们就调用P处理脚本

去生成对应的Java代码

右键Open in Terminal

调用Plot

GRBC

Bet脚本

好

通过提示消息可以看到Pending Service

挂单的限价委托数据结构

就已经生成完成

咱们可以检查一下

在确认下面

这里就是LimitPlaceOrder的数据结构定义

代码呢

就已经生成完成

那这一讲就是对限价委托下单接口数据结构定义的实现

这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“挂单服务”的分布式系统开发教程的一部分，核心内容是使用 Protocol Buffers (protobuf) 定义 gRPC 服务的接口和数据结构。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何创建一个名为 `StockPendingService.proto` 的文件，定义了一个名为 `limitPlaceOrder` 的远程过程调用（RPC）接口，并详细构建了其请求（`LimitPlaceOrderRequest`）和响应（`LimitPlaceOrderResponse`）消息体。整个过程旨在为后续的 Java 服务端和客户端开发奠定数据契约基础。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: **课程引入与目标**。画面显示课程大纲，明确指出本节目标是“3.1 定义接口数据结构”，并强调这是“第2章 限价委托挂单处理”的一部分。
*   **00:05 - 00:15**: **创建 `.proto` 文件**。讲师在 IDE 中创建了 `StockPendingService.proto` 文件，并开始编写服务定义。
*   **00:15 - 00:30**: **定义服务接口**。在 `.proto` 文件中，定义了 `StockPendingService` 服务及其 `limitPlaceOrder` RPC 方法。
*   **00:30 - 00:45**: **定义请求消息体**。讲师逐步添加 `LimitPlaceOrderRequest` 消息的字段，包括 `accountId`、`stockId`、`direction`、`type` 等。
*   **00:45 - 00:55**: **继续定义请求消息体**。添加了 `execVolume` 和 `execPrice` 字段，完善请求结构。
*   **00:55 - 01:05**: **定义响应消息体**。讲师开始定义 `LimitPlaceOrderResponse` 消息，包含 `status` 和 `message` 字段。
*   **01:05 - 01:15**: **配置与生成代码**。讲师切换到 `proto_grpc.bat` 脚本文件，准备使用 `protoc` 编译器将 `.proto` 文件生成 Java 代码。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **课程大纲**: 显示了章节结构，包括“3.1 定义接口数据结构”、“3.2 挂单服务限价委托接口”等。
    *   **代码注释**: 代码中包含中文注释，如“// 限价委托下单服务类”、“// 限价委托下单接口”、“// 限价委托的请求数据结构”等，用于说明代码功能。

*   **关键代码片段**:

    **`StockPendingService.proto` 文件内容**:

    ```protobuf
    syntax = "proto3";

    option java_multiple_files = true;
    option java_package = "com.itcast.bulls.stock.struct.grpc.quote";
    option java_outer_classname = "StockPendingServiceProto";

    service StockPendingService {
      // 限价委托下单接口
      rpc limitPlaceOrder (LimitPlaceOrderRequest) returns (LimitPlaceOrderResponse) {
      }
    }

    // 限价委托的请求数据结构
    message LimitPlaceOrderRequest {
      // 交易账户ID
      int64 accountId = 1;
      // 股票产品ID
      int64 stockId = 2;
      // 买卖方向
      int32 direction = 3;
      // 下单类型
      int32 type = 4;
      // 请求数量
      int32 execVolume = 5;
      // 请求价格
      int64 execPrice = 6;
    }

    // 限价委托的返回数据结构
    message LimitPlaceOrderResponse {
      // 处理状态
      string status = 1;
      // 返回消息
      string message = 2;
    }
    ```

*   **脚本文件**:

    **`proto_grpc.bat` 文件内容**:

    ```bat
    @echo off
    for %%i in (grpc/*.proto) do (
      d:\TestCode\protoc.exe --plugin=protoc-gen-grpc=d:\TestCode\protoc-grpc.exe --java_out=../src/main/java %%i
      echo generate %%i to java file successfully!
    )
    ```

---

### 4) 关键场景与演示描述

*   **场景一：创建并编辑 `.proto` 文件**
    *   讲师在 IntelliJ IDEA 中，通过项目结构导航到 `src/main/resources/proto/grpc` 目录，右键点击并选择“New -> File”，创建了 `StockPendingService.proto` 文件。
    *   随后，讲师在文件中编写了服务定义，包括 `service` 块和 `rpc` 方法声明。

*   **场景二：定义请求与响应消息体**
    *   讲师在 `message LimitPlaceOrderRequest` 中，逐行添加了多个字段，如 `accountId`、`stockId`、`direction`、`type`、`execVolume` 和 `execPrice`，并为每个字段指定了类型和编号。
    *   接着，讲师定义了 `message LimitPlaceOrderResponse`，包含 `status` 和 `message` 字段。

*   **场景三：配置与生成代码**
    *   讲师切换到 `proto_grpc.bat` 脚本文件，该脚本使用 `protoc` 编译器，通过 `--plugin` 参数指定 gRPC 插件，将 `.proto` 文件编译为 Java 代码并输出到 `src/main/java` 目录。
    *   脚本中使用 `for` 循环遍历 `grpc` 目录下的所有 `.proto` 文件，自动执行编译操作。

*   **场景四：IDEA 项目结构展示**
    *   画面多次展示了 IntelliJ IDEA 的项目结构，清晰地显示了 `src/main/resources/proto/grpc` 目录下的多个 `.proto` 文件，如 `StockKlineService.proto`、`StockPendingService.proto` 等，表明这是一个包含多个服务的项目。

---

以上是根据视频画面内容进行的详细结构化分析。
