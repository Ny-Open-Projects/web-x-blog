# 03-资金额度调整-接口数据结构定义 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始去实现额度调整接口数据结构的定义

额度调整功能它和账户资金有关

通过资金服务去做对应的实现

提供额度调整的接口

用于内部服务之间的调用

这个是不对外暴露出去

一般对账户资金操作相关的接口

都是放在内部去调用处理

额度调整接口

它的使用场景包括下单

扣除账户资金

还有入金和出金等涉及到调整账户上资金的功能

入金就类似于充值的概念

出金就相当于是提现的概念

那咱们去修改原来的资金服务脚本文件

回到工程当中

打开公用的PB数据结构工程

这个是对内提供的服务接口

所以我们只需要修改

去RPC的传输数据结构

然后增加一个接口

接口名称

给它添加注释修改账户资金的接口

我们做个定义RPC update account balance

传递请求参数update balance request returns

返回响应的数据宝

balance response增加大括号

接下来去定义账户资金的请求数据结构

我们定义在最下面

message update balance request

增加故事

这个是更新资金请求的数据结构

还有传递账户ID

然后要调整的资金额度

最后还要定义一个XID

XID适用于CETA的分布式事务

这个咱们在后面章节会做具体的讲解

先把数据结构定义好

这个名称修正一下update

好

接着的话呢

去定义更新资金的返回数据结构

message

update

balance

response

定义states

message

接着的话呢

定义交易账户ID

account ID

区号为3

然后去定义更新的

使用资金

将剩余的可用资金返回给调用方

也要认识

好

GRBC的传输数据结构

我们就已经定义完成

接着的话呢

我们通过脚本去生成对应的交易代码

右键open in terminal

ploto

grbc.bat

执行下

好

这里提示update

balance request

没有定义

我们来看一下

这个名称我们要修正

接着咱们再重新执行一下

好

生成成功

咱们检查一下对应的代码

grbc目录下面

shed

update

balance

response

这些数据结构呢

都已经成功生成

好

那在这里呢

咱们就完成了资金额度调整接口的数据结构定义

这一讲的内容

咱们就先讲到这里

好

下期见

拜拜

拜拜

我想 ¡¨

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是“交易平台 - Day 17”课程的一部分，主要讲解如何在微服务架构中实现“额度调整”功能。该功能的核心是通过“资金服务”（Finance Service）提供一个内部 gRPC 接口，用于在下单、入金、出金等场景中调整用户账户的可用资金。视频内容聚焦于实现该功能的第一步：定义 gRPC 接口的数据结构。讲师通过在 `StockFinanceService.proto` 文件中添加 `UpdateBalanceRequest`（请求）和 `UpdateBalanceResponse`（响应）消息体，明确了接口的输入和输出参数，包括账户 ID、调整金额、事务 ID 以及更新后的可用余额。整个过程展示了如何在 Protobuf 文件中定义数据结构，并为后续的代码生成和接口实现做准备。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 视频开头，讲师在 Typora 文档中展示课程大纲，明确本节目标是“实现额度调整功能”，并列出子章节，包括“定义接口数据结构”、“资金服务额度调整接口实现”等。
*   **00:03 - 00:08**: 讲师切换到 IntelliJ IDEA，打开项目 `bulls-stock`，并导航至 `src/main/resources/proto/grpc/StockFinanceService.proto` 文件，准备进行代码修改。
*   **00:08 - 00:15**: 讲师在 `StockFinanceService.proto` 文件中定位到 `rpc updateAccountBalance(UpdateBalanceRequest) returns (UpdateBalanceResponse)` 的定义，并开始修改其内部的数据结构。
*   **00:15 - 00:25**: 讲师逐步在文件中添加 `UpdateBalanceRequest` 和 `UpdateBalanceResponse` 的消息体定义，详细说明了每个字段的含义，如 `accountId`、`adjustBalance`、`xid`、`balance` 等。
*   **00:25 - 00:30**: 讲师完成数据结构定义后，点击生成代码，终端显示成功生成了多个 `.java` 文件，包括 `UpdateBalanceResponse.java`，表明 Protobuf 文件已成功编译。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **目标**: 额度调整功能与账户资金有关，通过资金服务实现，提供额度调整接口，用于内部服务调用，不对外暴露。
    *   **实现步骤**: 3.1 定义接口数据结构；3.2 资金服务额度调整接口实现。
    *   **核心概念**: 额度调整仅用于内部服务调用，只需定义 gRPC 接口。

*   **代码关键内容**:
    *   **Protobuf 文件 (`StockFinanceService.proto`)**:
        ```protobuf
        // 更新资金请求的数据结构
        message UpdateBalanceRequest {
            int64 accountId = 1;
            int64 adjustBalance = 2;
            string xid = 3;
        }

        // 更新资金的返回数据结构
        message UpdateBalanceResponse {
            string status = 1;
            string message = 2;
            int64 accountId = 3;
            // 更新后的可用资金
            int64 balance = 4;
        }
        ```
    *   **生成的 Java 类 (`UpdateBalanceResponse.java`)**:
        ```java
        public final class UpdateBalanceResponse extends
            com.google.protobuf.GeneratedMessageV3 implements
            UpdateBalanceResponseOrBuilder {
            private static final long serialVersionUID = 0L;
            private UpdateBalanceResponse(com.google.protobuf.GeneratedMessageV3.Builder<?> builder) {
                super(builder);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境准备与目标定位 (00:00-00:08)**:
    *   讲师首先在 Typora 文档中展示课程目标，明确本节要实现“额度调整功能”。
    *   接着，讲师切换到 IntelliJ IDEA，打开项目 `bulls-stock`，并导航至 `StockFinanceService.proto` 文件，为后续的代码修改做准备。

*   **场景二：定义 gRPC 接口数据结构 (00:08-00:25)**:
    *   讲师在 `StockFinanceService.proto` 文件中，定位到 `rpc updateAccountBalance` 的定义。
    *   讲师在文件中添加了 `UpdateBalanceRequest` 消息体，定义了 `accountId`、`adjustBalance` 和 `xid` 三个字段。
    *   随后，讲师添加了 `UpdateBalanceResponse` 消息体，定义了 `status`、`message`、`accountId` 和 `balance` 四个字段，其中 `balance` 字段用于返回更新后的可用资金。
    *   讲师在代码中添加了注释，清晰地解释了每个字段的含义。

*   **场景三：代码生成与验证 (00:25-00:30)**:
    *   讲师完成数据结构定义后，执行了代码生成操作。
    *   终端窗口显示了成功生成多个 `.java` 文件的日志，包括 `UpdateBalanceResponse.java`，验证了 Protobuf 文件的修改已成功编译，为后续的 Java 代码实现打下了基础。
