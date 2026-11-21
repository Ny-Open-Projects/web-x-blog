# 05-PB通讯工程-编译生成JAVA文件 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始创建

公用的PB通讯数据工程

那咱们从代码当中做一个实现

在代码当中

去创建一个新的工程

new model

点击next

这个工程名称呢

咱们就要buzz

stock

stack

plot

就咱们的公用PB通讯工程

点击finish

好

工程的话呢

就已经创建完成

接着咱们要将它的依赖呢

添加进去

在讲义当中

咱们copy进来

那咱们来看一下

主要有哪些依赖呢

首先的话呢

是pro buff的插件

这版本呢

是3.8.0

下面的话呢

是GRBC的通讯层插件

咱们可以看到

它是基于neti做的实现

然后的话呢

是GRBC的

protobuff的插件

GRBC的通讯呢

是采用protobuff

作为它的数据载体

然后呢

在这里要注意一下

GRBC的protobuff插件呢

需要排除它自带的prot插件

这个目的是为了避免这个插件

产生对应的冲突

最后一个呢

也是GRBC的插件

这里面呢

主要是封装GRBC通讯

所涉及到的相关接口

回到讲义当中

接着的话呢

咱们就去编写protobuff的脚本

protobuff脚本主要分为两部分

一部分呢

是内部微幅的GRBC通讯

另一部分呢

是外部客户拨单的

nety长链接通讯

咱们就以简易的下单接口作为示例

来了解呢

protobuff的具体使用

以及呢

咱们内部微幅节点

是如何实现通讯

同时呢

了解通讯数据的结构

以及呢

它的规范

回到咱们的代码当中

咱们将protobuff文件呢

就全部存放在

resource支援目录下面

那咱们创建一个包

包名呢

就叫proto

先来实现

内部服务的通讯数据结构定义

也就是从代理服务

发起调用至交易服务

接下来咱们来创建两个目录

一个呢

是用于存放内部通讯的脚本

另外一个呢

是用于存放外部的通讯脚本

咱们就先实现

内部的GRBC

简易下单的通讯脚本

右键new

file

stock

fail deal

service

这个顺序名呢是proto

咱们来做具体的代码编写

send text

在这里呢是指定protobuff的编译版本

在这里呢咱们是采用proto3版本

咱们按照proto3的语法呢

去做相应的定义

这个参数选项呢

是标识该脚本呢

能否生成多个加尔文件

一般呢咱们设定为chew

接着话呢咱们再设置

它的生成的包路径

咱们指定下它具体的包路径

再buzz

stock

chark.grpc

点cheat的包下面

接下来咱们再去定义

它生成的内名称

内名呢咱们跟protobuff的名称呢

保持一致

将后缀名呢去除

这里呢修改下它的后缀

做一个标识

说明了它是proto生成的加尔代码

接下来呢咱们再去定义

它的grpc接口

这个呢是交易服务的

业务接口

定义一个service

stock

chared

deal service

然后就来定义咱们的简易下单接口

咱们来看一下rbc的接口该如何去定义呢

这里呢是它的方法名称

place order

下面呢是它的参数

然后呢是它的返回对象

这样呢咱们就完成了一个接口的定义

咱们也将它的参数和返回对象呢做一个定义

首先定义下单的请求参数

请求参数体以备备的参数体是什么呢

请求参数体以备备备的参数体是什么呢

以message关键字开头

定义place order request对象

注意这个呢不能定义在service内部

message参数体呢咱们要定义在外面

注意它的整个层次

接下来呢就来定义请求参数的具体属性

定义一个股票ID

这个呢是长者型

长者型呢采用int64

int32呢表示的是整形

64呢对应了就是long term

对应的就是浪形

接下来呢

是股票的买卖方向

0代表就是买入

1代表呢

就卖出

它是整形表示

咱们注意一下

普罗巴夫的定义

这个等号后面呢

并非表示它的具体值

而是呢

它的一个序号

在普罗巴夫属性定义的时候呢

要保持整个序号的有序连续性

不要出现相同的序号

或者说从1直接跳到3

序号的主要作用呢

是处理数据的序列化

以及呢

它的反序列化

这里要注意一下

如果普罗巴夫里面

扩送了新的属性

咱们要将普罗巴夫的脚本呢

重新去编译生成新的代码

如果不重新生成代码呢

那么你新加的属性

就无法正常读取

如果你是调整了它的序号

那么这个PB代码呢

就必须要重新生成

接下来咱们来定义其他的属性

这个是

是委托类型

0是代表市价单

1是代表现价单

这里呢

用整形表示

序号设为3

保持整个序号的有序连续性

接下来咱们再定义

请求数量

这个也叫做挂单数量

采用整形表示

整形这个长度呢

是足够使用

接下来是它的请求价格

这个也叫挂单

或者是委托价格

这个呢

价格咱们都通过长整形表示

就是Qs price

序号为5

好

下单请求参数定义完成之后呢

咱们就掌握了PB的基本语法

在这里呢

是它的头部的一些配置标识

下面呢

是GRPC介面的一个定义

然后这个呢

就是请求参数体的一个定义

最后呢

还有一个返回参数体

那咱们从讲义当中做一个copy

这个呢

Place order response

就是下单请求参数体的一个定义

这是下单接口所返回的对象信息

在这里呢

它定义了状态

还有呢

消息提示

通过这两个属性呢

咱们可以知道

这个接口调用呢

是正常还是失败

下面呢

就是接口的业务属性

在这里呢

返回了订单ID

成交的数量

成交的价格

好

在这里咱们就实现了

内部的GRPC下单接口的定义

外部的PB的数据定义呢

咱们下一讲

再来做定义了

讲解和实现

那这讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面，对这段技术课程进行的结构化中文输出：

---

### 1) 视频摘要

本视频是“交易平台 - Day 13”课程的一部分，主要讲解如何搭建一个基于 **Protocol Buffers (protobuf)** 的通信数据工程。课程内容聚焦于 **第1章：公用PB通讯数据工程搭建**，具体步骤包括：创建一个名为 `stock-struct-proto` 的新工程，配置其 Maven 依赖（特别是 protobuf 和 gRPC 插件），并编写用于内部服务（gRPC）和外部客户端（Netty）通信的 `.proto` 文件。演示中以“简单下单功能”为例，定义了服务接口 `StockTradeDealService` 及其请求/响应消息结构 `PlaceOrderRequest` 和 `PlaceOrderResponse`。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，展示课程大纲，明确本节目标是“创建工程”。
*   **00:00:05 - 00:00:15**: 展示在 IntelliJ IDEA 中创建新模块 `stock-struct-proto` 的过程，设置其父模块和坐标。
*   **00:00:15 - 00:00:30**: 展示新创建工程的目录结构，包括 `src/main/java`、`src/main/resources` 和 `pom.xml`。
*   **00:00:30 - 00:00:45**: 展示 `pom.xml` 文件，重点添加了 protobuf 和 gRPC 的依赖。
*   **00:00:45 - 00:01:00**: 详细展示 `pom.xml` 中的依赖配置，包括 `protobuf-java`、`grpc-netty-shaded` 和 `grpc-stub`，并特别说明了 `grpc-stub` 的版本号 `1.22.1`。
*   **00:01:00 - 00:01:15**: 展示 `pom.xml` 中的 `exclusions` 配置，用于排除 `protobuf-java` 的冲突。
*   **00:01:15 - 00:01:30**: 切换到 `proto` 文件夹，展示其下包含 `grpc` 和 `netty` 两个子目录。
*   **00:01:30 - 00:01:45**: 在 `grpc` 目录下创建并打开 `StockTradeDealService.proto` 文件。
*   **00:01:45 - 00:02:00**: 编写 `StockTradeDealService.proto` 文件，定义服务接口 `StockTradeDealService` 和 `placeOrder` 方法。
*   **00:02:00 - 00:02:15**: 继续编写 `StockTradeDealService.proto` 文件，定义请求消息 `PlaceOrderRequest`。
*   **00:02:15 - 00:02:30**: 继续编写 `StockTradeDealService.proto` 文件，定义响应消息 `PlaceOrderResponse`，包含 `status`、`message`、`dealId`、`execVolume` 和 `execPrice` 等字段。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “第1章 公用PB通讯数据工程搭建”。
    *   **步骤列表**: “创建工程”、“编写proto脚本”、“编译生成java文件”、“封装protobuf编译命令，制作为脚本”。
    *   **子章节**: “3.1 创建工程”、“3.2 编写proto脚本”。
    *   **关键说明**: “proto脚本分为两部分，一部分是内部微服务gRpc通讯，另一部分是外部客户端Netty长连接通讯。”
    *   **文件结构图**: 展示了 `stock-struct-proto` 工程的目录结构，包括 `src/main/java`、`src/main/resources`、`target`、`pom.xml` 和 `ReadMe.md`。
    *   **依赖说明**: “增加Protobuf与grpc-protobuf相关依赖。”
    *   **文件结构图**: 展示了 `proto` 文件夹下的 `grpc` 和 `netty` 子目录。

*   **代码内容**:
    *   **Maven 依赖配置**:
        ```xml
        <!-- Protobuf 插件 -->
        <dependency>
            <groupId>com.google.protobuf</groupId>
            <artifactId>protobuf-java</artifactId>
            <version>3.8.0</version>
        </dependency>

        <!-- gRPC proto 插件，排除自带的protobuf插件，避免冲突 -->
        <dependency>
            <groupId>io.grpc</groupId>
            <artifactId>grpc-netty-shaded</artifactId>
            <version>1.22.1</version>
        </dependency>

        <dependency>
            <groupId>io.grpc</groupId>
            <artifactId>grpc-stub</artifactId>
            <version>1.22.1</version>
        </dependency>
        ```
    *   **Protobuf 文件内容**:
        ```protobuf
        option java_multiple_files = true;
        option java_package = "com.itcast.bulls.stock.struct.grpc.trade";
        option java_outer_classname = "StockTradeDealServiceProto";

        // 交易服务的业务接口
        service StockTradeDealService {
            rpc placeOrder (PlaceOrderRequest) returns (PlaceOrderResponse) {
            }
        }

        // 下单的请求对象
        message PlaceOrderRequest {
            // 请求价格/挂单/委托价格
            int64 execprice = 5;
        }

        // 下单的返回对象
        message PlaceOrderResponse {
            // 状态，处理结果的状态
            int32 status = 1;
            // 处理结果的提示消息
            string message = 2;
            // 订单的ID
            int64 dealId = 3;
            // 成交的数量
            int32 execvolume = 4;
            // 成交的价格
            int64 execprice = 5;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建工程** (00:00:05 - 00:00:15)
    *   演示者在 IntelliJ IDEA 中通过 `File -> New -> Module` 创建一个名为 `stock-struct-proto` 的新模块。
    *   设置其父模块为 `com.itcast.trade.bulls-stock`，并配置了 `GroupId` 和 `Version`。

*   **场景二：配置 Maven 依赖** (00:00:30 - 00:01:30)
    *   演示者打开 `pom.xml` 文件，添加了 protobuf 和 gRPC 的依赖。
    *   重点演示了 `grpc-stub` 依赖的版本号 `1.22.1`。
    *   为避免依赖冲突，配置了 `exclusions`，排除了 `protobuf-java`。

*   **场景三：编写 proto 文件** (00:01:30 - 00:02:30)
    *   演示者在 `grpc` 目录下创建并打开 `StockTradeDealService.proto` 文件。
    *   逐步编写了服务接口 `StockTradeDealService` 和 `placeOrder` 方法。
    *   定义了请求消息 `PlaceOrderRequest` 和响应消息 `PlaceOrderResponse`。
    *   在 `PlaceOrderResponse` 中定义了多个字段，如 `status`、`message`、`dealId`、`execVolume` 和 `execPrice`，并为每个字段指定了标签（tag）和注释。

---
