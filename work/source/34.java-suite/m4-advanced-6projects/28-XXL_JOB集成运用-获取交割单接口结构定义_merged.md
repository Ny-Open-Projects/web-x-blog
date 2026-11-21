# 28-XXL_JOB集成运用-获取交割单接口结构定义 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来这一讲呢

咱们接着去实现

获取交个单的

接口数据结构的定义

首先要去定义

native对外的传输数据结构

这里呢

我们就不再去逐一编写代码

这里为节省时间

我们就直接做一个copy

回到工程当中

定位stock

message

plot

在最下面

咱们将第一的脚本

copy进来

可以看到返回的用户交个单

是一个数据集合

这里呢

就是交个单的具体属性信息

包括用户ID

成交记录

股票信息

交易相关的信息

上面是获取账户交个单的

请求数据结构

这里需要传递的是

开始时间和结束时间

咱们还要去修改

stock message的数据结构

这里增加一个定义

获取账户交个单

它的请求数据包

get account settlement debt

做copy

序号为7

然后我们还要去修改

response message的数据结构

在这里面增加获取账户交个单的

返回数据包

get account settlement response debt list

做一个copy

序号为9

外层nete的传输数据结构定义完整之后

接下来咱们还要去定义GRBC内部的传输数据结构

咱们同样做个copy

回到代码当中

修改stock finance service portal

在最下面

对一家脚本定义

这里面的返回信息和刚才在nete里面定义的返回信息

基本上是一致的

那传递的参数

这里是增加了交易账户的ID

response message呢

它返回的也是一个数据集合

上面是状态

这里呢是强硬处理消息

这个是账户的交个单

然后我们去定义RBC的接口

在最上面增加一个接口

RBC

get account settlement

传递对应的参数

account settlement request returns

get

返回响应包

返回交个单数据

account settlement response

添加注释

获取账户交个单数据

接口

好

GRBC的数据结构就已经定义完成

那我们去生成相应的代码

右键open intomino

通过必处理脚本

proto grbc

然后我们去输入我们的账户

这个生成成功

我们再去生成nety

生成完成

咱们检查一下

GRBC

确定下面

get account settlement

获取账户交个单的数据结构信息

是成功生成

咱们再去检查nety

这里get account settlement也是成功生成

好

那这一讲

咱们就完成了交个单的接口数据结构的定义

并且生成了对应的交换代码

好

这一讲的内容

咱们就先讲到这里

谢谢大家的观看

我们下期再见

拜拜

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统（`bulls-stock`）的开发教程，重点讲解如何定义和实现“获取交割单”这一核心业务功能的接口数据结构。讲师通过在 IntelliJ IDEA 中操作，演示了如何在两个不同的协议层（Netty 和 gRPC）中分别定义请求和响应的数据结构（`.proto` 文件），并展示了生成的 Java 代码。整个过程旨在说明如何在微服务架构中，通过定义清晰、一致的数据模型来支持业务功能的开发。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 开场，展示课程大纲，定位到第 3.8 节“定义获取交割单的接口数据结构”。
*   **00:03 - 00:08**: 讲解第一部分：**Netty 对外数据结构**。在 `StockMessage.proto` 文件中，定义了请求数据 `GetAccountSettlementData` 和响应数据 `GetAccountSettlementRespData`。
*   **00:08 - 00:15**: 讲解第二部分：**gRpc 接口内部数据结构**。在 `StockFinanceService.proto` 文件中，定义了 gRPC 服务接口 `getAccountSettlement` 及其对应的请求 `GetAccountSettlementRequest` 和响应 `GetAccountSettlementSingle`。
*   **00:15 - 00:20**: 展示 `StockFinanceService.proto` 文件的完整内容，包括服务定义和多个 RPC 方法。
*   **00:20 - 00:25**: 展示 `GetAccountSettlementRequest` 的 Java 生成类，说明其继承自 `GeneratedMessageV3`。
*   **00:25 - 00:30**: 结束本节，再次强调本节的核心是定义数据结构。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **PPT / 文档内容**

*   **课程大纲**：显示了章节列表，当前聚焦于 **3.8 定义获取交割单的接口数据结构**。
*   **Netty 对外数据结构**：
    *   **请求结构**：`GetAccountSettlementData`
        *   `int64 timeStart = 1;` // 结束时间
        *   `int64 timeEnd = 2;` // 开始时间
    *   **响应结构**：`GetAccountSettlementRespData`
        *   `string status = 1;`
        *   `string message = 2;`
        *   `repeated GetAccountSettlementSingle getAccountSettlementSingle = 3;`

*   **gRpc 接口内部数据结构**：
    *   **请求结构**：`GetAccountSettlementRequest`
        *   `int64 accountId = 1;`
        *   `int64 timeStart = 2;`
        *   `int64 timeEnd = 3;`
    *   **响应结构**：`GetAccountSettlementSingle`
        *   `string status = 1;`
        *   `string message = 2;`
        *   `repeated GetAccountSettlementSingle getAccountSettlementSingle = 3;`

#### **代码内容**

*   **Netty `.proto` 文件 (`StockMessage.proto`)**：
    ```protobuf
    message GetAccountSettlementData {
        int64 timeStart = 1;
        int64 timeEnd = 2;
    }

    message GetAccountSettlementRespData {
        string status = 1;
        string message = 2;
        repeated GetAccountSettlementSingle getAccountSettlementSingle = 3;
    }
    ```

*   **gRPC `.proto` 文件 (`StockFinanceService.proto`)**：
    ```protobuf
    service StockFinanceService {
        rpc getAccountSettlement(GetAccountSettlementRequest) returns (GetAccountSettlementResponse) {
        }
    }
    ```

*   **Java 生成类 (`GetAccountSettlementRequest.java`)**：
    ```java
    public final class GetAccountSettlementRequest extends
        com.google.protobuf.GeneratedMessageV3 implements
        GetAccountSettlementRequestOrBuilder {
        private static final long serialVersionUID = 0L;
        private GetAccountSettlementRequest(com.google.protobuf.GeneratedMessageV3.Builder<?> builder) {
            super(builder);
        }
        private GetAccountSettlementRequest() {
        }
    }
    ```

---

### 4) 关键场景与演示描述

1.  **场景一：定义 Netty 外部接口**
    *   **描述**：讲师在 IntelliJ IDEA 中打开 `StockMessage.proto` 文件，定位到第 3.8 节。他首先定义了 `GetAccountSettlementData` 消息，包含 `timeStart` 和 `timeEnd` 两个字段，用于客户端向服务端发送请求。接着，他定义了 `GetAccountSettlementRespData` 消息，包含 `status`、`message` 和一个 `repeated` 的 `GetAccountSettlementSingle` 字段，用于服务端返回响应。

2.  **场景二：定义 gRPC 内部接口**
    *   **描述**：讲师切换到 `StockFinanceService.proto` 文件。他定义了 `StockFinanceService` 服务，并添加了 `getAccountSettlement` 方法，该方法接收 `GetAccountSettlementRequest` 并返回 `GetAccountSettlementResponse`。他同时定义了 `GetAccountSettlementRequest` 和 `GetAccountSettlementSingle` 的结构，与 Netty 层保持一致，确保数据模型的统一性。

3.  **场景三：展示生成的 Java 代码**
    *   **描述**：讲师通过 IDEA 的导航功能，跳转到 `GetAccountSettlementRequest` 的 Java 类。他展示了该类继承自 `GeneratedMessageV3`，并提供了构造函数和默认构造函数，说明了 gRPC 自动生成的代码结构，便于开发者在业务代码中使用。

4.  **场景四：强调数据结构的重要性**
    *   **描述**：讲师在 PPT 上强调，定义清晰的数据结构是实现“获取交割单”功能的基础，它确保了 Netty 和 gRPC 两个服务层之间的数据交互是标准化和可维护的。

---
