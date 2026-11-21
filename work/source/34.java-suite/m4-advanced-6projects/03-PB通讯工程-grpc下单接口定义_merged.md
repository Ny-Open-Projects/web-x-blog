# 03-PB通讯工程-grpc下单接口定义 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们去实现

Netty外部通讯方式的PB数据结构定义

咱们回到代码当中

在Netty的包下面

创建一个新的文件

名称叫做stack-head.proto

首先咱们在头部定义ProBuff的配置信息

这个是标识采用Proto3的版本

然后是配置选项

这个是生成的包路径

指定包路径

这个是在Netty包下面

下面配置生成的加码内名

class name

这个是stock-head.proto

咱们就来定义头部消息体

message-stock-head

然后咱们先定义一个协议版本

接着的话定义接口请求类型

外部可能会传递很多的接口请求交互

所以咱们要通过

一个属性进行标识和区分

request-type

咱们加上对应的注释

这个是协议版本

这个是请求类

请求接口类型

下面咱们还定义消息编号

消息编号采用长整形

给掉消息要有一个消息编号

能够去定位和追踪

最后就是处理状态

处理状态就是标识整个接口的处理结果

接着咱们来实现这两个结果

我们先定义两个消息体

一个是的propto协议版本

协议版本在这里咱们就可以采用枚举方式

propto buff它是可以支持枚举的定义

咱们定义两个枚举值

一个是代表版本一

另外一个是代表版本二

下面是可以支持扩展

这个就根据咱们的业务需要做相应的定义

然后是请求类型

请求类型

我们同样也定义为枚举

request type

目前咱们只实现了用户下单

所以咱们只需要定义一个接口类型

这个就是用户的下单

定义完头部消息体之后

咱们接着就来定义数据消息体

重新创建一个脚本文件

名称就叫stock message.proto

首先定义头部信息

咱们可以先copy过来

做相应的调整修改

然后咱们要将刚才所定义的头部消息体导入进来

通过import指定

stock head

emprodo

咱们再加上一个配置项

这个配置项是允许生成多个加尔文件

PLA

那么接着的话咱们就来定义它的请求数据结构

message

stock message

有效一体就是一个完整的包

它要包含头部消息

stock message

message

message

stock message

然后是咱们的数据消息体

上面就是head

下面就类似于body

这里要注意一下

后续咱们功能实现当中会涉及到较多的接口

每个接口有自己的数据消息体

那么该如何去定义

这个不像attp的传送方式

可以传送实讯支付串

支付串里面可以存储各种各样的数据消息

然后将这些消息通过json可以转换为具体的数据对象

但是pp的话就不一样

pp它必须是一个明确的对象

也就是说所有传输数据必须要预先定义好

那咱们看一下该如何去实现

在这里通过一个one of关键字

然后定义一个stock data的消息体

下面定义了具体的消息结构

这个是用于下单传输的消息结构体

序号要保持它的有序性

那咱们看一下one of是什么作用呢

one of作用呢

咱们在这里再扩充一个

get user data

比如说还有一个获取用户资料的接口

那one of的意思呢

它就是说我要传递其中一个的消息数据类型

简单点说

如果我传递了下单的数据消息体

那么就不能设置获取用户的数据体

如果设置了获取用户的数据消息体

那么就不能设置下单的数据体

这样咱们就可以实现不同接口的数据消息的传递

好

那咱们呢

就来继续定义下单的数据消息体

定义下单的请求数据包体

关键字是message

快速实现起见

咱们呢

就从讲义当中

将这些信息呢

直接copy过来

这里都有对应的注释说明

语法的定义使用方法是什么呢

之前咱们也做了讲解

这样请求消息体就已经定义完成

定义完成之后呢

咱们是不是应该还需要去创建一个返回的消息体

对不对

好

那咱们创建一个返回的消息体

同样咱们在这里呢

要定义一个外层的完整的响应消息体

response

然后呢定义头部消息

这个头部消息呢

咱们是可以公用

咱们将它copy过来

所以返回消息呢

可以再直观一点

可以再扩展一下

给它一个返回提示消息

视讯的类型

然后同样咱们要定义了返回的

业务数据消息体

还用1off关键字

response

对

咱们定义一个trace order

下单接口的响应数据消息体

序号为3

咱们把下单响应消息体呢

做个定义

下单返回数据包

message

paste

order

response

这里咱们只需要返回呢

订单ID

加上对应的注释

好

咱们回到响应当中

在这里呢

咱们就完成了

project脚本的编写

定义了下单请求接口的两部分

projectbuff的脚本

一个是GRPC通讯所用到的

PB结构定义

另外一部分呢

是基于neti长连接实现的socket通讯

也是采用PB作为数据载体进行传输

好

那这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是“交易平台 - Day 13”课程的一部分，主要讲解如何使用 Protocol Buffers (protobuf) 定义一个简单的股票下单接口的数据结构。课程内容聚焦于在 IntelliJ IDEA 开发环境中，为内部微服务 gRPC 和外部客户端 Netty 长连接通信分别创建和管理 `.proto` 文件。讲师通过演示如何定义请求和响应消息体，以及如何在项目中组织这些文件，来帮助学习者理解 protobuf 的基本语法和在实际项目中的应用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开始，展示课程大纲和当前学习目标。
*   **00:05 - 00:15**: 讲师介绍本节内容，即“编写 proto 脚本”，并展示项目结构，强调将 proto 文件分为 `grpc` 和 `netty` 两个目录。
*   **00:15 - 00:30**: 讲师在 IntelliJ IDEA 中演示如何创建新的 `.proto` 文件，例如 `StockMessage.proto`，并将其放置在 `netty` 目录下。
*   **00:30 - 00:45**: 讲师开始编写 `StockMessage.proto` 文件，首先定义了 `PlaceOrderRequest` 消息体，包含 `stockId`、`direction`、`type` 和 `execVolume` 等字段。
*   **00:45 - 01:00**: 讲师继续编写 `PlaceOrderResponse` 消息体，包含 `dealId` 字段。
*   **01:00 - 01:15**: 讲师在 `StockMessage.proto` 文件中定义了 `oneof` 结构 `ResponseData`，用于区分不同的响应类型，当前只定义了 `PlaceOrderResp`。
*   **01:15 - 01:30**: 讲师在 `StockHead.proto` 文件中定义了 `PlaceOrderResponse` 消息体，包含 `status`、`message`、`dealId`、`execVolume` 和 `execPrice` 字段。
*   **01:30 - 01:45**: 讲师在 `StockTradeDealService.proto` 文件中定义了 `StockTradeDealService` 服务接口，包含 `placeOrder` 方法，该方法接收 `PlaceOrderRequest` 并返回 `PlaceOrderResponse`。
*   **01:45 - 02:00**: 讲师总结了本节内容，强调了 proto 文件的组织方式和基本语法。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **学习目标**: 第1章 公用PB通讯数据工程搭建；第2章 简易下单功能实现。
    *   **关键概念**: proto 脚本分为两部分，一部分是内部微服务 gRpc 通讯，另一部分是外部客户端 Netty 长连接通讯。
    *   **项目结构图**: 展示了 `resources/proto` 目录下包含 `grpc` 和 `netty` 两个子目录，分别存放对应的 `.proto` 文件。

*   **代码关键内容**:
    *   **`StockHead.proto` 文件**:
        ```protobuf
        message PlaceOrderResponse {
            int32 status = 1;  // 状态，处理结果的状态
            string message = 2;  // 处理结果的提示消息
            int64 dealId = 3;  // 订单的ID
            int32 execVolume = 4;  // 成交的数量
            int64 execPrice = 5;  // 成交的价格
        }
        ```
    *   **`StockMessage.proto` 文件**:
        ```protobuf
        message PlaceOrderRequest {
            int64 stockId = 1;  // 股票产品ID
            int32 direction = 2;  // 买卖方向
            int32 type = 3;  // 挂单类型
            int32 execVolume = 4;  // 请求数量
            int64 execPrice = 5;  // 请求价格
        }

        oneof ResponseData {
            PlaceOrderResp placeOrderResp = 3;
        }
        ```
    *   **`StockTradeDealService.proto` 文件**:
        ```protobuf
        syntax = "proto3";

        option java_multiple_files = true;
        option java_package = "com.itcast.bulls.stock.struct.grpc.trade";
        option java_outer_classname = "StockTradeDealServiceProto";

        service StockTradeDealService {
            rpc placeOrder (PlaceOrderRequest) returns (PlaceOrderResponse) {
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建和组织 proto 文件** (00:15 - 00:30)
    *   讲师在 IntelliJ IDEA 的项目结构视图中，右键点击 `netty` 目录，选择“New” -> “File”，创建名为 `StockMessage.proto` 的新文件。
    *   讲师强调，为了区分内部服务和外部客户端，需要将 proto 文件分别放在 `grpc` 和 `netty` 目录下。

*   **场景二：编写请求和响应消息体** (00:30 - 01:15)
    *   讲师在 `StockMessage.proto` 文件中，首先定义了 `PlaceOrderRequest` 消息体，包含 `stockId`、`direction`、`type` 和 `execVolume` 字段。
    *   接着，讲师定义了 `PlaceOrderResponse` 消息体，包含 `dealId` 字段。
    *   为了支持多种响应类型，讲师在 `StockMessage.proto` 中定义了 `oneof ResponseData`，并添加了 `PlaceOrderResp`。

*   **场景三：定义服务接口** (01:15 - 01:30)
    *   讲师在 `StockHead.proto` 文件中，定义了 `PlaceOrderResponse` 消息体，包含 `status`、`message`、`dealId`、`execVolume` 和 `execPrice` 字段。
    *   讲师在 `StockTradeDealService.proto` 文件中，定义了 `StockTradeDealService` 服务接口，包含 `placeOrder` 方法，该方法接收 `PlaceOrderRequest` 并返回 `PlaceOrderResponse`。

*   **场景四：总结与回顾** (01:30 - 02:00)
    *   讲师总结了本节内容，强调了 proto 文件的组织方式和基本语法。
    *   讲师提醒学习者，proto 文件的定义是后续生成 Java 代码和进行网络通信的基础。
