# 07-PB通讯工程-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对本章内容做一个回顾和总结

首先咱们看一下本章的学习目标

在这里咱们要掌握三点

第一要完成公用的PB通讯数据工程的搭建和配置

第二点咱们要了解工程通讯数据结构以及相应的规范

这个在PB结构定义的时候也做了一个讲解

最后一点咱们要掌握ProBuff的定义相关的语法

以及如何去编译生成交亚代码

并且对ProBuff脚本工具的使用做一层封装

编译咱们的后续使用

那咱们来回顾下本章所讲解的内容

首先咱们去创建了对应的工程

这个工程是专门用于定义ProBuff的数据结构

并且通过ProBuff生成的代码也是存储放置在该工程当中

接下来咱们就编写了ProBuff脚本

这脚本包含两部分

一部分是内部微幅物质间通讯

GRBC

的通讯方式

另外一部分是外部客户端

Neti的长连接方式进行的通讯

咱们在下面讲解了ProBuff语法的使用

如何去定义一个RPC接口

实现了下单接口

请求数据

以及响应数据的定义

接着的话咱们就编译生成交亚文件

通过ProBuff提供的编译工具

如果要生成GRBC接口代码

还要采用ProBuff提供的GRBC代码

为了便于大家的使用

以及后续的维护

咱们在这里对编译工具脚本做了一层封装

可以让它支持编译多个文件

简化了咱们的维护工作量

最后咱们对封装的编译脚本进行了一个测试验证

通过实际的测试结果都能够正常生成相应的加码代码

最后咱们再来总结一下

GRBC的内部通讯项目当中

数据结构定义以及相应的规范

咱们呢

不要将它们掌握清楚

要理解GRBC接口呢

是如何进行定义

新版本的ProBuff工具呢

它是不支持通配服的编译

多个文件的编译呢

咱们可以通过封装的脚本去做相应的实现

咱们要注意一下ProBuff的编译

以及呢

生成的路径

该怎么去配置

如果采用相对路径呢

要注意它的成绩顺序

还有ProBuff的路径呢

要注意它的成绩顺序

还有ProBuff相关的一些编译选项

这些呢

大家都可以多做一些了解

本章所讲解的ProBuff的数据结构定义呢

涉及到了基本的语法

这些语法呢

可以足够支撑咱们在项目当中

去实现不同的业务功能

更多的用法呢

大家可以去参阅相关的资料

拓展编译相关的命令

以及呢

更多ProBuff语法的使用

好

这一讲呢

咱们就先讲解到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是“交易平台 - Day 13”的一部分，主要讲解如何在 Java 项目中搭建和使用 Protocol Buffers (简称 PB 或 Protobuf) 作为服务间通信的数据格式。课程内容分为两大部分：

*   **第一部分 (第1章)**：聚焦于“公用PB通讯数据工程搭建”。核心任务是创建一个 Maven 项目，配置 Protobuf 依赖，并编写用于 gRPC 和 Netty 两种通信方式的 `.proto` 文件。课程重点在于掌握 Protobuf 的基本语法、定义数据结构，并通过自定义脚本解决新版本 Protobuf 不支持批量编译的问题。
*   **第二部分 (第2章)**：作为铺垫，简要介绍“简易下单功能实现”的目标和步骤，为后续的业务逻辑开发做准备。

课程采用“目标-步骤-实现”的结构，通过代码演示和目录结构展示，旨在让学习者掌握 Protobuf 的工程化配置和数据结构定义。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：课程开场，展示“第1章 公用PB通讯数据工程搭建”的标题页。
*   **00:05 - 00:15**：介绍本章学习目标：完成工程配置、理解数据结构与规范、掌握 Protobuf 定义与编译。
*   **00:15 - 00:30**：讲解“步骤”部分，包括创建工程、编写 `.proto` 脚本、编译生成 Java 文件、封装编译命令。
*   **00:30 - 00:45**：进入“实现”部分，首先讲解“3.1 创建工程”，展示 Maven 项目结构和 `pom.xml` 文件中的 Protobuf 依赖配置。
*   **00:45 - 01:00**：讲解“3.2 编写proto脚本”，展示项目目录结构，区分 `grpc` 和 `netty` 两个子目录，并介绍 `StockTradeDealService.proto` 文件。
*   **01:00 - 01:20**：展示 `StockTradeDealService.proto` 文件内容，定义了 `placeOrder` 服务接口及 `PlaceOrderRequest` 和 `PlaceOrderResponse` 两个消息体。
*   **01:20 - 01:35**：讲解“3.3 编译生成Java文件”，展示 gRPC 和 Netty 两种通信方式的编译命令。
*   **01:35 - 01:50**：讲解“3.4 封装编译脚本”，说明新版本 Protobuf 不支持通配符，需要自定义脚本。
*   **01:50 - 02:05**：展示 `protoc_grpc.bat` 和 `protoc_netty.bat` 两个脚本文件的内容，使用 `for` 循环遍历 `.proto` 文件并调用 `protoc` 或 `protoc.exe` 命令进行编译。
*   **02:05 - 02:20**：展示编译后的 Java 文件目录结构，突出显示了 `PlaceOrderResponse`、`PlaceOrderRequest` 等类。
*   **02:20 - 02:35**：切换到“第2章 简易下单功能实现”的标题页，为下一章内容做铺垫。
*   **02:35 - 02:45**：课程结束，回到“第1章”的总结页。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **第1章目标**：完成公用PB通讯数据工程搭建配置；了解工程通讯数据结构与规范；掌握protobuf定义与编译。
    *   **第1章步骤**：创建工程；编写proto脚本；编译生成java文件；封装protobuf编译命令，制作成脚本。
    *   **第2章目标**：实现简易下单功能。
    *   **总结页**：gRpc内部通讯，项目中数据结构定义与规范；新版本编译不支持通配符，多个文件的编译可通过脚本实现；注意protobuf编译与生成路径；自定义Protobuf数据结构，掌握Protobuf语法，拓展编译命令。

*   **代码示例**：

    *   **Maven 依赖 (pom.xml)**：
        ```xml
        <dependency>
            <groupId>com.google.protobuf</groupId>
            <artifactId>protobuf-java</artifactId>
            <version>3.8.0</version>
        </dependency>
        ```

    *   **Protobuf 文件 (StockTradeDealService.proto)**：
        ```protobuf
        syntax = "proto3";

        option java_multiple_files = true;
        option java_package = "com.itcast.bulls.stock.struct.grpc.trade";
        option java_outer_classname = "StockTradeDealServiceProto";

        service StockTradeDealService {
            rpc placeOrder (PlaceOrderRequest) returns (PlaceOrderResponse) {}
        }

        message PlaceOrderRequest {
            int64 stockId = 1;
            int32 direction = 2; // 0:买入，1:卖出
            int32 type = 3;       // 0:市价单，1:限价单
            int32 execvolume = 4; // 请求数量/挂单数量
            int64 execprice = 5;  // 请求价格/委托价格
        }

        message PlaceOrderResponse {
            int32 status = 1;     // 状态，处理结果的状态
            string message = 2;   // 处理结果的提示消息
            int64 dealId = 3;     // 订单的ID
            int64 dealvolume = 4; // 成交的数量
        }
        ```

    *   **gRPC 编译命令**：
        ```bash
        protoc --proto_path=./grpc --plugin=protoc-gen-grpc-java=d:/TestCode/protoc-grpc.exe --grpc-java_out=../java --java_out=../java StockTradeDealService.proto
        ```

    *   **Netty 编译命令**：
        ```bash
        protoc.exe --proto_path=./netty --java_out=../java ./netty/StockHead.proto
        ```

    *   **自定义脚本 (protoc_grpc.bat)**：
        ```bat
        @echo off
        for %%i in (grpc/*.proto) do (
            d:/TestCode/protoc.exe --plugin=protoc-gen-grpc-java=d:/TestCode/protoc-grpc.exe --grpc-java_out=../java --java_out=../java %%i
            echo generate %%i to java file successfully!
        )
        ```

    *   **自定义脚本 (protoc_netty.bat)**：
        ```bat
        @echo off
        for %%i in (netty/*.proto) do (
            d:/TestCode/protoc.exe --proto_path=./netty --java_out=../java ./netty/%%i
            echo generate %%i to java file successfully!
        )
        ```

---

### 4) 关键场景与演示描述

*   **场景1：工程创建与依赖配置** (00:30-00:45)
    *   **描述**：讲师在 Typora 编辑器中展示了一个 Maven 项目结构，重点是 `pom.xml` 文件。他高亮显示了添加的 Protobuf 依赖，并解释了 `groupId`、`artifactId` 和 `version` 的含义，强调这是项目的基础配置。

*   **场景2：编写 `.proto` 文件** (00:45-01:00)
    *   **描述**：讲师切换到项目目录视图，展示了 `grpc` 和 `netty` 两个文件夹。他选中了 `StockTradeDealService.proto` 文件，说明这是用于 gRPC 通信的接口定义文件，用于定义下单服务。

*   **场景3：定义 Protobuf 数据结构** (01:00-01:20)
    *   **描述**：讲师在 Typora 中打开并高亮显示了 `StockTradeDealService.proto` 文件的内容。他逐行解释了 `syntax`、`option` 等语句，并重点讲解了 `service`、`rpc`、`message` 等核心结构，以及 `PlaceOrderRequest` 和 `PlaceOrderResponse` 中的字段定义（如 `stockId`、`direction`、`status` 等），并解释了字段的语义。

*   **场景4：编译命令演示** (01:20-01:35)
    *   **描述**：讲师在文档中展示了 gRPC 和 Netty 两种通信方式的编译命令。他解释了命令中 `--proto_path`、`--plugin`、`--java_out` 等参数的作用，说明了如何通过命令行将 `.proto` 文件编译成 Java 代码。

*   **场景5：自定义
