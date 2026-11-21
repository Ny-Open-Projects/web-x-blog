# 21-用户撤单-接口数据结构定义 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始去定义测单功能接口的数据结构

咱们要去定义两层数据结构

一层是Netty与客户端的交互数据结构

另外一层是内部的GRBC通讯层的数据层结构

好那咱们来做一个代码实现

回到工程当中

打开Stalker Message Browser文件

这里是定义Netty和客户端对外的传输数据结构

咱们在这里首先加上测单接口的请求数据包

测单接口的请求数据包

创建一个新的请求参数体

叫RecallAllData

序号为5

接下来咱们来创建这个消息结构

咱们在最下面去创建请求参数的数据结构

定义一个Message

RecallAllData

测单请求结构

接口传递的参数比较简单

主要是要传递订单ID

以及股票产品ID

因为挂单的数据是根据股票产品ID做了一个分组汇总

这里序号为1

然后定义股票产品ID

int64

startid

通过股票产品ID

这样咱们就能定位挂单的对列缓存信息

来自Pounce响应的包体可以不需要单独定义

通过Head头部消息去标示它的处理状态

咱们就知道测单是否成功就可以

接下来我们再定义GRBC接口的传输数据结构

这个接口是放在挂单服务里面实现的

所以我们去修改Stock Pending Service

在这里我们新增一个接口

用户测单接口

通过RBC进行调用

Recall Order

定义请求参数体

内部的传输咱们给它一个响应的参数体

响应参数体同样不需要传递对应的业务信息

咱们只需要标记这个接口处理成功或者失败就可以

接下来咱们去实现对应数据结构的定义

在最下面

咱们增加相应的数据定义

这个是测单请求的数据结构

Message

Recall Order Request

请求数据结构

定义一个股票账户ID

int64

序号为1

然后定义定单ID

int64我的ID

最后还有股票的产品ID

int64

stock ID

序号为3

接着咱们去定义测单的响应数据结构

定义一个Message

Recall

Order Response

返回处理的状态

返回响应消息

这个加上注释

它是处理状态

下面是响应消息

定义完成之后

咱们就要去生成对应的交往文件

在Protot目录下面右键Open in terminal

打开终端窗口

咱们执行P处理命令

Protot

需要PC

点Bet

好

可以看到

需要PC的交往文件就已经生成完成

接着咱们再去生成

Neti传输成的数据文件

好

这个也已经执行成功

咱们检查一下相关的代码

F5刷新一下

在Check目录下面

咱们检查一下有没有RecallOrder

好

可以看到有RecallOrderRequest

以及RecallOrderResponse

Neti的对外传输的数据结构

咱们也检查一下

在这里并没有发现RecallOrder的交往代码

咱们检查一下P处理命令

因为咱们刚才执行了相同的P处理脚本

这里我们要去执行Neti的Bet的处理脚本

好

我们再次刷新一下

这个时候可以看到RecallOrderData就已经生成成功

咱们回到讲义当中

这一讲咱们就定义了用户车单的接口数据结构

并且生成了对应的交往代码

好

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“用户撤单功能”的实现教程。讲师通过演示如何使用 Protocol Buffers (protobuf) 定义网络通信的数据结构，来构建一个支持“挂单”和“撤单”功能的系统。主要内容包括：

*   **定义接口数据结构**：首先修改 `StockMessage.proto` 文件，定义了用于客户端与服务端交互的通用消息结构 `StockMessage`，其中包含头部信息和不同类型的请求/响应数据包。
*   **定义 gRPC 服务接口**：接着修改 `StockPendingService.proto` 文件，定义了 `stockPendingService` 服务及其两个核心 RPC 方法：`limitPlaceOrder`（限价委托下单）和 `recallOrder`（撤单）。
*   **生成 Java 代码**：通过 IDE 的工具，将 `.proto` 文件编译生成对应的 Java 类（如 `LimitPlaceOrderRequest` 和 `RecallOrderResponse`），为后续的业务逻辑实现做准备。

整个过程展示了如何从协议设计到代码生成的完整流程，是构建高性能、强类型网络服务的基础。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面的绝对时间点，以下时间点是根据画面内容和逻辑顺序进行的相对估算：

*   **0:00 - 0:05**：视频开头，展示课程大纲，明确本节主题为“第3章 用户撤单功能实现”，并列出“3.1 定义接口数据结构”、“3.2 挂单服务撤单功能实现”等子章节。
*   **0:05 - 0:15**：讲师讲解并演示如何修改 `StockMessage.proto` 文件，定义 `StockMessage` 消息结构，包含 `StockHead` 头部和 `StockData` 体。
*   **0:15 - 0:30**：继续在 `StockMessage.proto` 中定义 `StockData` 的具体类型，包括 `LoginData`、`PlaceOrderData` 和 `KlineData`。
*   **0:30 - 0:45**：定义 `StockHead` 的结构，包含 `ProtoVer`（协议版本）和 `RequestType`（请求类型）等字段。
*   **0:45 - 1:00**：切换到 `StockPendingService.proto` 文件，定义 `stockPendingService` 服务，并添加 `limitPlaceOrder` 方法。
*   **1:00 - 1:15**：继续在 `StockPendingService.proto` 中定义 `recallOrder` 方法，用于撤单。
*   **1:15 - 1:30**：在终端中执行 `protoc` 命令，生成 Java 代码。
*   **1:30 - 1:45**：展示生成的 Java 类文件，如 `LimitPlaceOrderRequest.java` 和 `RecallOrderResponse.java`，并讲解其继承关系和构造方式。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **课程大纲**：显示了“第3章 用户撤单功能实现”的章节结构，包括“3.1 定义接口数据结构”、“3.2 挂单服务撤单功能实现”、“3.3 代理服务撤单调用实现”和“3.4 功能验证”。
*   **关键注释**：
    *   在 `StockMessage.proto` 中，注释说明了 `StockMessage` 是“请求消息”。
    *   在 `StockPendingService.proto` 中，注释说明了 `stockPendingService` 是“限价委托下单接口”和“撤单接口”。

#### 代码关键内容

*   **`StockMessage.proto` 文件内容**：
    ```protobuf
    option java_package = "com.itcast.bulls.stock.struct.netty.trade";
    option java_outer_classname = "StockMessageProto";

    message StockMessage {
      // 头部消息
      StockHead stockHead = 1;

      // 消息体
      oneof StockData {
        LoginData loginData = 2;
        PlaceOrderData placeOrderData = 3;
        KlineData klineData = 4;
      }
    }

    message StockHead {
      ProtoVer protoVer = 1;
      RequestType requestType = 2;
      int64 seqid = 3;
      string status = 4;
    }

    enum ProtoVer {
      VER_1 = 0;
      VER_2 = 1;
    }

    enum RequestType {
      // 请求类型定义
    }
    ```

*   **`StockPendingService.proto` 文件内容**：
    ```protobuf
    syntax = "proto3";
    option java_multiple_files = true;
    option java_package = "com.itcast.bulls.stock.struct.grpc.trade";
    option java_outer_classname = "StockPendingServiceProto";

    service stockPendingService {
      // 限价委托下单接口
      rpc limitPlaceOrder (LimitPlaceOrderRequest) returns (LimitPlaceOrderResponse) {
      }

      // 撤单接口
      rpc recallOrder (RecallOrderRequest) returns (RecallOrderResponse) {
      }
    }
    ```

*   **`RecallOrderData` 结构定义**：
    ```protobuf
    message RecallOrderData {
      // 订单ID
      int64 orderId = 1;
      // 股票产品ID
      int64 stockId = 2;
    }
    ```

*   **生成的 Java 类（示例）**：
    ```java
    public final class LimitPlaceOrderRequest extends
        com.google.protobuf.GeneratedMessageV3 implements
        LimitPlaceOrderRequestOrBuilder {
      private static final long serialVersionUID = 0L;
      private LimitPlaceOrderRequest(com.google.protobuf.GeneratedMessageV3.Builder<?> builder) {
        super(builder);
      }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：定义通用消息结构**
    *   **描述**：讲师在 IDE 中打开 `StockMessage.proto` 文件，通过鼠标滚动和光标移动，逐步展示如何定义 `StockMessage` 消息。他首先定义了头部 `StockHead`，然后定义了消息体 `StockData`，并用 `oneof` 关键字来表示消息体只能包含其中一种类型的数据。
    *   **技术点**：演示了 `oneof` 的使用，以及如何定义嵌套消息和枚举类型。

*   **场景二：定义 gRPC 服务接口**
    *   **描述**：讲师切换到 `StockPendingService.proto` 文件，通过光标移动和高亮显示，演示如何定义 `stockPendingService` 服务。他依次添加了 `limitPlaceOrder` 和 `recallOrder` 两个 RPC 方法，并在方法中指定了请求和响应的数据结构。
    *   **技术点**：演示了 gRPC 服务的定义方式，以及如何将请求和响应类型与 `.proto` 文件中的消息结构关联。

*   **场景三：生成 Java 代码**
    *   **描述**：讲师在终端中执行 `protoc` 命令，将 `.proto` 文件编译成 Java 代码。他展示了终端输出的“generate ... proto to java file successfully!”信息，表明代码生成成功。
    *   **技术点**：演示了 protobuf 编译器的使用，以及如何通过 IDE 自动完成代码生成。

*   **场景四：查看生成的 Java 类**
    *   **描述**：讲师在 IDE 中打开生成的 `LimitPlaceOrderRequest.java` 和 `RecallOrderResponse.java` 文件，通过光标移动和高亮显示，讲解这些类的继承关系和构造方式。他特别强调了这些类是 `GeneratedMessageV3` 的子类，并提供了 `newBuilder()` 方法来构建实例。
    *   **技术点**：演示了生成的 Java 类的结构，以及如何使用 `Builder` 模式来创建对象。

---

以上是对视频内容的完整结构化分析。
