# 14-仓位总览-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对本章内容做一个回顾和总结

首先咱们回顾下本章的学习目标

在这里咱们的重点是要去实现仓位总卵功能

同时掌握仓位总卵的核心处理流程

包括浮动盈亏

盈亏比例等方面的计算处理

那咱们再回顾下本章所讲解的具体内容

首先咱们从实现上做了一个讲解

仓位总卵是用户比较关注的一个核心功能

该接口需要提供用户的所有仓位信息

包含持仓价格持仓数量

还有盈亏等相关情况

核心的处理逻辑就是浮动盈亏的计算处理

接下来咱们就开始搭建了持仓服务

并且完成了必要组件的集成配置

接下来咱们就实现了接口数据结构的定义

包括NetEase的对付性能

地外传输数据结构

以及内部的GRPC传输数据结构

再往下面

咱们就在持仓服务里面实现了仓位总卵的接口

GRPC接口层的处理逻辑相对会比较简单一点

这里通过service的调用去完成了持仓数据的处理

然后拿到持仓数据做一个便利

将数据做了一个封装

然后返回给了调用方

也就是代理服务

下面呢

就在代理服务里面实现了它的转发和调用处理

这里我们就增加了一个仓位服务的处理器

然后在工厂方法里面做了相应的扩展

最后呢

就在工程配置里面增加了GRPC持仓服务的调用配置

再往下面就是在客户端里面做了接口的调用实现

以及对整体功能做了一个测试和验证

整体测试也给大家看到具体的结果能够呢

正常拿到持仓服务的结果

并且咱们也结合了行情推送服务

去验证了浮动盈亏盈亏比例的相关信息

最后咱们再来总结一下

仓位总览它是比较重要的功能

我们要理解浮动盈亏以及盈亏比例的计算处理规则

对于风控控制较高的系统

如果需要实现强频

就要监控所有账户的

所有仓位的实时盈亏变化数据

大家想想

一个平台如果是接入了300万用户

每个用户如果是买了10只股票

那么最少会产生1000万的数据

那每秒行情可能会产生多口报价

这个时候的数据量是非常巨大的

需要我们服务器有极大的负载能力

所以在实现思路上

咱们的仓位服务是采用无状态式的设计

可以支撑它的水平扩展

如果一个节点存在较大的压力瓶颈

那咱们可以再扩充几个节点

提升整体的吞吐能力

同时仓位服务也可以结合缓存功能

将仓位信息写入到缓存里面

做同步的处理

通过异步现成

这样浮动盈亏的计算

它就可以从缓存当中去做对应的加工

相比数据库的查询方式

会有极大的性能提升

这些就是应用在生产环境上的实现处理思路

好

做金融业务服务

不光要实现业务

咱们还需要考虑它的准确性

然后才是性能

不能本末倒置

一味的追求性能

而忽略了数据的准确性

数据的准确和安全

在金融行业尤为重要

如果这个层面不能保障

如果这个层面不能保障

再好的性能也是没有实际意义的

我们要注重IO资源的操作

能一次性查询的就不要多次查询

能不查询的咱们就尽量避免

去采用缓存做处理

好

这些层面希望大家在工作实际应用当中

要多加注意

这一讲就是对本章内容的回顾和总结

那咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程讲解了在金融交易系统中实现“账户资金总览”功能的技术方案。核心内容围绕“持仓总览”展开，旨在实现对用户所有持仓的实时监控，包括持仓价格、数量、最新价格、盈亏等关键信息。课程从服务架构设计（如无状态设计、水平扩展）到具体实现（如 gRPC 接口定义、服务调用、数据处理）进行了详细阐述，并强调了在金融业务中“先考虑准确性，再考虑性能”的核心原则。最后，通过客户端调用和验证，演示了如何获取并展示持仓总览数据。

---

### 2) 按时间顺序的章节（带时间点）

由于无法提供精确的时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **第 1 部分：目标与步骤 (约 0:00 - 0:30)**
    *   介绍“账户资金总览”功能的目标。
    *   概述实现该功能的步骤：服务搭建、接口定义、服务实现、客户端调用验证。

*   **第 2 部分：服务实现 (约 0:30 - 3:00)**
    *   **2.1 持仓服务的搭建与配置**
        *   展示了项目依赖，包括 Spring Boot、Nacos 服务发现和自定义的公共数据组件。
    *   **2.2 定义接口数据结构**
        *   使用 Protocol Buffers (protobuf) 定义 gRPC 服务接口 `StockPositionService`，包含 `getAllPositions` 方法。
    *   **2.3 持仓服务仓位总览接口实现**
        *   展示了服务端的 Java 实现代码，通过 `stockPositionService.getAllPositions` 获取持仓数据。
        *   对数据进行处理，将 `TradePosition` 对象转换为 `GetAllPositionData` 对象，并设置执行时间。
        *   处理异常并返回响应。
    *   **2.4 代理服务转发调用处理**
        *   展示了客户端如何通过 `@GrpcClient` 注解注入 gRPC 服务客户端 `stockPositionServiceStub`。
        *   展示了如何在 `processRequest` 方法中构造请求并调用远程服务。
    *   **2.5 客户端调用实现与验证**
        *   展示了如何在客户端配置中增加对 gRPC 服务的调用配置。
        *   通过 `NettyClientTest` 进行调用测试，成功获取到两条持仓数据的详细信息。

*   **第 3 部分：总结 (约 3:00 - 结束)**
    *   强调了“仓位总览”功能的重要性。
    *   重申了实现该功能的关键技术点：无状态设计、水平扩展、缓存同步。
    *   重申了金融业务开发的核心原则：先考虑准确性，再考虑性能，避免不必要的多次查询。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容：**
    *   **章节标题：** “第2章 仓位总览功能”、“第3章 账户资金总览功能”。
    *   **核心要点：**
        *   仓位总览是重要功能，用于监控浮动盈亏与盈亏比例。
        *   实现思路：持仓服务为无状态设计，支持水平扩展；仓位写入缓存，做同步处理；所有浮动盈亏的计算条件数据都从缓存中获取处理。
        *   金融业务开发原则：先考虑准确性，再考虑性能，注重要素 I/O 操作，能一次性查询的就不要多次查询，不能查询就采用缓存处理。

*   **代码关键内容：**

    *   **Maven 依赖 (POM.xml):**
        ```xml
        <!-- Spring Boot 依赖 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <!-- Nacos 服务发现依赖 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-nacos-discovery</artifactId>
        </dependency>

        <!-- 公用数据组件 -->
        <dependency>
            <groupId>com.itcast.trade</groupId>
            <artifactId>bulls-stock-common-dao</artifactId>
            <version>${project.stock.version}</version>
        </dependency>
        ```

    *   **gRPC 接口定义 (StockPositionService.proto):**
        ```protobuf
        syntax = "proto3";

        option java_multiple_files = true;
        option java_package = "com.itcast.bulls.stock.struct.grpc.trade";
        option java_outer_classname = "StockPositionServiceProto";

        service StockPositionService {
            // 获取所有持仓信息接口
            rpc getAllPositions (GetAllPositionRequest) returns (GetAllPositionResponse) {}
        }
        ```

    *   **服务端 Java 实现 (StockPositionServiceImpl.java):**
        ```java
        // 1. 根据账户ID获取所有持仓数据
        List<TradePosition> positionList = stockPositionService.getAllPositions(request.getAccountId());
        GetAllPositionResponse.Builder responseBuilder = GetAllPositionResponse.newBuilder();

        // 2. 对持仓数据做非空判断处理
        if (null != positionList) {
            // 3. 遍历持仓数据，将持仓对象转换成PB对象进行输出
            for (TradePosition pos : positionList) {
                GetAllPositionData.Builder positionData = GetAllPositionData.newBuilder();
                BeanAssistant.copyNotNullProps(pos, positionData, new String[]{"execTime"});
                positionData.setExecTime(pos.getExecTime().getTime());
                // ... 其他字段设置
            }
        }

        // 处理异常
        catch (Exception e) {
            log.error(e.getMessage(), e);
            response = GetAllPositionResponse.newBuilder().setStatus(GlobalConstants.STATUS_ERROR).setMessage(e.getMessage()).build();
        }

        // 发送响应
        responseObserver.onNext(response);
        responseObserver.onCompleted();
        ```

    *   **客户端 Java 实现 (NettyClientTest.java):**
        ```java
        @GrpcClient("grpc-position-server")
        private StockPositionServiceGrpc.StockPositionServiceBlockingStub stockPositionServiceStub;

        @Override
        public void processRequest(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage) {
            // 构造请求信息
            GetAllPositionRequest request = GetAllPositionRequest.newBuilder()
                .setAccountId(stockMessage.getAccountId())
                .build();

            // 调用远程服务
            GetAllPositionResponse response = stockPositionServiceStub.getAllPositions(request);
            // ... 处理响应
        }
        ```

    *   **客户端配置 (application.yml):**
        ```yaml
        grpc:
          client:
            grpc-position-server:
              address: 'discovery://stock-position'
              enableKeepAlive: true
              keepAliveWithoutCalls: true
              negotiationType: plaintext
        ```

---

### 4) 关键场景与演示描述

*   **场景一：服务架构与接口设计**
    *   **描述：** 讲师首先介绍了“仓位总览”功能的目标，并展示了项目依赖，说明了使用 Spring Boot、Nacos 和自定义组件构建服务。接着，通过 PPT 展示了 gRPC 接口定义文件 `StockPositionService.proto`，明确了服务接口 `getAllPositions` 的功能。

*   **场景二：服务端实现与数据处理**
    *   **描述：** 讲师展示了服务端 Java 代码，演示了如何通过 `stockPositionService.getAllPositions` 方法获取持仓数据。代码逻辑包括：根据账户ID查询数据、对数据进行非空判断、遍历数据并将其转换为 gRPC 响应对象、设置执行时间等字段、处理异常并构建响应。最后，通过 `responseObserver` 发送响应。

*   **场景三：客户端调用与验证**
    *   **描述：** 讲师展示了客户端如何通过 `@GrpcClient` 注解注入 gRPC 服务客户端。接着，通过 `NettyClientTest` 的测试代码，演示了如何构造请求并调用远程服务。最终，成功获取到两条持仓数据的详细信息，包括 `accountId`、`stockId`、`costPrice`、`volume`、`avgPrice`、`profit`、`execTime`、`lastPrice` 和 `profitRate` 等字段。

*   **场景四：总结与核心原则**
    *   **描述：** 在课程结尾，讲师通过 PPT 总结了本章的核心内容。强调了“仓位总览”功能的重要性，并重申了实现该功能的关键技术点：无状态设计、水平扩展、缓存同步。最后，再次强调了金融业务开发的核心原则：先考虑准确性，再考虑性能，避免不必要的多次查询，能一次性查询的就不要多次查询，不能查询就采用缓存处理。
