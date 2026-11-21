# 24-简易下单功能-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对本章内容做一个回顾和总结

首先咱们看一下本章的主要学习目标

在这里咱们要掌握三点

第一点咱们要完成交易服务的搭建和配置

第二点咱们要完成简易的下单功能

同时要熟悉外部和内部的数据处理交互流程

对外咱们是采用Netty加ProBub的通讯

对内部咱们是采用GRBC

再加上PB的一个数据通讯

整个的交互处理机制大家要熟悉

最后一点咱们要掌握SplitBoot 2.X

再加上GRBC、Netty、WebSocket

以及ProBub的基层通讯方案

这里面运用到的是长连接通讯

使整个传输效率有着更好的表现

掌握本套通讯方案

在整个微服务通讯领域当中

能有着较好的性能表现

好

这里通过一个简易下单的功能接口

让大家侧重理解GRBC的交互通讯流程

学会在内部微服务应用当中

如何去实现GRBC的通讯

为了便于GRBC组件的集成和使用

咱们将GRBC组件做了一个自动化的配置

这里大家要注意一下

GRBC和Cloud的阿里巴巴存在一些兼容性问题

那么咱们做了相应的修改和调整

让GRBC服务能够去支持Marcus的注册和发现

这里的调整也比较简单

主要就是将GRBC的服务信息注册到Marcus服务当中

再往下面就是在代理服务当中实现了接口的调用

为了便于今后的接口调用的扩展

咱们在这里做了一个工厂模式封装

通过工厂模式

可以便于咱们对今后业务接口调用的方式

扩展和维护

接着的话代理服务作为WebSocket的服务端

在这里实现了NetEase的集成配置

并且增加了对WebSocket的服务支持

咱们在这里也做了详细的讲解

WebSocket的连接

大家要注意一下它的消息包的具体格式

这个不同于咱们传统的Socket通讯

WebSocket有自定义的数据结构规范

在这里它发送过来的消息会存在多种类型

但是通过ProBuff进行传输

所以传递过来的数据是一个

Banner类的二进制封装的数据包

WebSocket是不能直接去发送ProBuff的二进制数据

所以咱们要做一层转换

往下面咱们就增加了ProBuff的解码器

将WebSocket的二进制数据包转换为ProBuff

自定义的数据结构对象

作为一个WebSocket的服务

客户端的连接需要做一个握手初始化的处理

自定义的集成配置以及WebSocket的支持

大家在这里要掌握好

接着的话咱们就对代理服务实现了GRPC的相关配置

代理服务是作为GRPC的调用方

在这里它要去配置所需要调用的远程服务信息

目前的话它是需要去调用交易服务

那么对应的就是交易服务的连接配置信息

再往下面咱们就实现了Netting模拟的客户端

通过Netting模拟客户端

可以帮助大家去调用

更好的去测试验证自己所编写的功能

可以提升自测处理效率

模拟客户端的编写

在这里也要去实现WebSocket的对接和支持

那么我们看一下Netting模拟客户端这一块

它是怎么去实现的

在这里面咱们去讲解了如何去启动配置

对它的数据包做了一个解码编码的一个配置

然后还对WebSocket的数据包做一个握手的处理

那么在握手之前

要将相应的信息配置好

比如说WebSocket的通讯连接地址

然后握手的消息格式

握手成功之后

WebSocket的这个长连接才算是有效建立

然后才能进行正常的业务数据通讯

再往下面咱们实现了交易服务的MyBatis双数据源方案的集成配置

交易服务也需要去操作交易数据和业务数据两个数据源

在这里咱们是采用MyBatis的双数据源方案

因为整个逻辑不再是

单纯的增上改查

同时还要求有较高的处理性能

所以就采用MyBatis作为双数据源的实现方案

最后咱们对整体功能进行了一个测试和验证

咱们启动了交易服务

代理服务

以及Netting模拟测试客户端

那么做了一个完整的测试验证

从各服务节点的控制台日志

咱们可以看到整体的输出交互结果

这些日志信息也是处理正常

咱们最后验证了数据库的数据信息

是能够成功生成订单的数据

也就完成了对简易下单功能的测试和验证

最后咱们再总结一下

通过简易的下单功能演示

咱们学习到了GRBC的运用

以及对外Netting

WebSocket加ProBuff的集成通讯配置

在这里咱们关键要掌握微服务高性能的通讯方案

学会了Spring Boot 2.X

加GRBC

加Netting

WebSocket

以及ProBuff的集成

生产机的实现方案

后面章节当中咱们还会基于这套技术解决方案

去实现更多的业务功能接口

好

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程为一个技术实战教程，主要讲解如何构建一个“交易服务”的代理系统。该系统通过 gRPC 服务与交易服务通信，并利用 Netty 框架实现高性能的客户端通信，最终将数据通过 MyBatis 持久化到数据库。课程内容覆盖了从项目工程创建、配置文件编写、gRPC 自动化配置、Netty 服务端与客户端开发，到最终的数据库验证和系统总结。核心目标是掌握 SpringBoot 2.X 与 gRPC、Netty、WebSocket、Protobuf 等技术的集成方案，用于构建高性能的微服务通信架构。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：课程总览与目标介绍，展示课程大纲。
*   **00:06 - 00:15**：**第2章 简易下单功能实现**。
    *   **00:06 - 00:10**：**3.1 交易服务工程创建**。演示创建名为 `stock-deal` 的 Spring Boot 项目，并展示其目录结构。
    *   **00:11 - 00:15**：**3.2 交易服务工程配置**。展示 `application.yml` 和 `bootstrap.yml` 等配置文件，以及如何配置多环境（dev, uat, prd）。
*   **00:16 - 00:25**：**3.3 实现简易下单接口**。展示数据库表结构，以及如何通过 MyBatis 操作数据库。
*   **00:26 - 00:35**：**3.4 交易服务 gRpc 自动化配置**。讲解如何解决 gRPC 组件与最新 Cloud Alibaba 的兼容性问题，编写 `GrpcNacosConfiguration` 配置类。
*   **00:36 - 00:45**：**3.5 代理服务简易下单接口工厂模式封装**。展示如何使用工厂模式封装 gRPC 服务。
*   **00:46 - 00:55**：**3.6 代理服务 Netty 集成与 Websocket 支持**。讲解如何在 Netty 服务端集成 Websocket。
*   **00:56 - 01:05**：**3.7 代理服务 gRpc 相关配置**。展示 gRPC 服务的配置文件 `grpc-trade-server.yaml`。
*   **01:06 - 01:15**：**3.8 Netty 模拟客户端编写**。演示如何编写 Netty 客户端，配置 Protobuf 编解码器和自定义处理器。
*   **01:16 - 01:25**：**3.9 交易服务 MyBatis 双数据源方案实现**。讲解如何在服务中配置双数据源。
*   **01:26 - 01:35**：**3.10 测试验证**。演示如何通过日志查看代理服务处理 gRPC 请求并转发数据到 Netty 客户端的过程。
*   **01:36 - 01:45**：**第3章 代理服务登陆鉴权实现**。课程进入新章节，介绍代理服务的登录鉴权功能。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **课程大纲**：清晰列出了从“交易服务工程创建”到“测试验证”的各个章节。
    *   **总结页**：核心学习目标是“学习到gRpc运用，以及Netty+Protobuf的集成使用”，并掌握“SpringBoot2.X + gRpc+Netty+Websocket+Protobuf的集成生产实践方案”。
    *   **数据库表结构**：展示了 `id`, `accountid`, `stockid`, `status`, `type`, `direction`, `involume`, `execvolume`, `execprice`, `execetime` 等字段，用于存储交易数据。
*   **代码关键内容**：
    *   **工程配置**：`application.yml` 中的数据库连接配置，如 `minEvictableIdleTimeMillis: 300000`，`validationQuery: SELECT 1`。
    *   **gRPC 配置**：`GrpcNacosConfiguration` 类，用于解决 gRPC 与 Cloud Alibaba 的兼容性问题。
    *   **Netty 服务端**：`StockProxyServerInitializer` 类，用于初始化 Netty 服务端，配置 `ChannelInitializer` 和 `StockProxyServerHandler`。
    *   **Netty 客户端**：`SimulateClient` 类，配置 `ChannelPipeline`，添加 `HttpClientCodec`、`ProtobufVarint32FrameDecoder`、`ProtobufVarint32LengthFieldPrepender` 和自定义的 `ClientBoundHandler`。
    *   **MyBatis 配置**：`SqlSessionFactoryBean` 的配置，用于创建数据源和映射文件。
    *   **日志输出**：在 Netty 客户端中，通过 `handler.handshakeFuture().sync()` 等方法进行握手，并打印日志。

---

### 4) 关键场景与演示描述

*   **场景一：项目工程创建与配置**（00:06-00:15）
    *   **演示**：在 IDE 中创建名为 `stock-deal` 的 Spring Boot 项目，并展示其标准的 Maven 项目结构。
    *   **关键操作**：配置 `application.yml` 文件，设置数据库连接池参数和多环境配置（dev, uat, prd）。
*   **场景二：gRPC 服务集成**（00:26-00:35）
    *   **演示**：编写 `GrpcNacosConfiguration` 配置类，使用 `@EnableConfigurationProperties` 和 `@ConditionalOnClass` 注解，解决 gRPC 与 Cloud Alibaba 的兼容性问题。
    *   **关键操作**：在配置类中注入 `NacosRegistration`，用于服务注册。
*   **场景三：Netty 服务端开发**（00:36-00:45）
    *   **演示**：创建 `StockProxyServerInitializer` 类，继承 `ChannelInitializer<SocketChannel>`，并配置 `StockProxyServerHandler`。
    *   **关键操作**：在 `initChannel` 方法中，配置 `ChannelPipeline`，添加 `HttpClientCodec` 和自定义的 `StockProxyServerHandler`。
*   **场景四：Netty 客户端开发**（00:46-01:05）
    *   **演示**：创建 `SimulateClient` 类，配置 `ChannelPipeline`。
    *   **关键操作**：添加 `ProtobufVarint32FrameDecoder` 和 `ProtobufVarint32LengthFieldPrepender` 用于 Protobuf 编解码，添加自定义的 `ClientBoundHandler` 用于处理业务数据。
*   **场景五：测试验证**（01:16-01:25）
    *   **演示**：在 `SimulateClient` 中调用 `handler.handshakeFuture().sync()` 方法进行握手，并打印日志。
    *   **关键操作**：通过日志查看代理服务处理 gRPC 请求并转发数据到 Netty 客户端的过程。
*   **场景六：课程总结**（01:36-01:45）
    *   **演示**：展示课程总结页，强调学习目标和掌握的技术栈。
    *   **关键操作**：回顾整个课程内容，为下一章“代理服务登陆鉴权实现”做铺垫。

---
