# 16-简易下单功能-代理服务grpc配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始实现代理服务GRPC的相关配置

咱们回到工程

找到代理服务

修改它的配置文件

在最下面咱们添加GRPC

Client客户端的调用配置

GRPC

首先定义GRPC

下面一个层级是Client

作为调用方可能会调用不同的GRPC服务端

咱们就要配置GRPC服务节点的具体连接信息

这里咱们定义GRPCChad Server

定义它的连接地址

这里咱们采用名称的方式进行连接

通过服务注册发现主线去找到对应的服务端

所以这里咱们采用三个斜杠进行连接

这个就是服务的名称

咱们指向的是交易服务

下面咱们还要配置客户端的连接属性

Enable Keep Alive

这个设定为To

保持空闲连接的有效存活状态

下面呢

Keep Alive Without Cause

这个参数的意思是

不需要采用回调的方式去保持连接的有效状态

这样可以减少不必要的资源开销

如果是对于一些网络波动比较大的情况

这个可以将它关闭

这个可以将它关闭

下面是配置数据传输的协商类型

这里面不需要提

数据协商类型在这里采用的是Plain Text

纯文本的方式

这个并非数据的传输类型

而是以它的协商类型的数据格式

这样咱们就完成了客户端GRBC的调用配置

咱们回到讲义当中

如果说只有单个节点

这里呢Adjust

可以采用这种配置

用静态的方式指向固定的服务端的IP和端口

咱们在这里是通过配置注册中心的服务名称进行了连接

它可以支持负载方式对远程的GRBC服务进行调用

在这里就是对代理服务端GRBC调用方配置的实现

那这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个名为 `bulls-stock-proxy` 的 Java 项目的技术讲解，重点在于配置其作为代理服务的 gRPC 客户端。讲师通过 IntelliJ IDEA 编辑器展示 `bootstrap-dev.yml` 配置文件，详细说明了如何配置 gRPC 客户端以连接到名为 `stock-deal` 的交易服务。配置内容包括服务发现地址、是否启用长连接、以及协议类型等。同时，讲师也展示了项目结构和相关的 PPT 文档，以辅助理解。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 开场，展示项目结构和 `bootstrap-dev.yml` 文件。
*   **00:00:05 - 00:00:15**: 讲解 `bootstrap-dev.yml` 文件中的 `netty` 配置，包括端口 `19999` 和调试开关 `debug: true`。
*   **00:00:15 - 00:00:25**: 切换到 `grpc` 配置部分，开始配置 gRPC 客户端。
*   **00:00:25 - 00:00:35**: 配置 `grpc-trade-server` 的地址为服务发现地址 `discovery:///stock-deal`。
*   **00:00:35 - 00:00:45**: 设置 `enableKeepAlive: true` 和 `keepAliveWithoutCalls: true` 以启用长连接。
*   **00:00:45 - 00:00:55**: 设置 `negotiationType: plaintext` 为协议类型。
*   **00:00:55 - 00:01:05**: 展示 PPT 文档 `Day13.md`，介绍 `3.7 代理服务gRpc相关配置` 章节。
*   **00:01:05 - 00:01:15**: 回到代码编辑器，确认并展示最终的 gRPC 配置。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 文档 (`Day13.md`)**:
    *   **章节标题**: `3.7 代理服务gRpc相关配置`
    *   **关键内容**: 该章节的 PPT 内容与视频中展示的 `bootstrap-dev.yml` 文件中的 gRPC 配置完全一致，用于解释配置项的含义。

*   **代码 (`bootstrap-dev.yml`)**:
    *   **Redis 配置**:
        ```yaml
        redis:
          host: 127.0.0.1
          password: 6379
        ```
    *   **Spring 分布式 Session**:
        ```yaml
        session:
          store-type: redis
        ```
    *   **Netty 服务配置**:
        ```yaml
        socket:
          netty:
            port: 19999
            debug: true
        ```
    *   **gRPC 客户端配置**:
        ```yaml
        grpc:
          client:
            grpc-trade-server:
              # address: 'static://127.0.0.1:19998'
              address: 'discovery:///stock-deal'
              enableKeepAlive: true
              keepAliveWithoutCalls: true
              negotiationType: plaintext
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示 (00:00:00-00:00:05)**
    *   讲师在 IntelliJ IDEA 中展示了项目 `bulls-stock-proxy` 的目录结构，重点指向 `resources` 目录下的 `bootstrap-dev.yml` 文件，表明这是当前要编辑的配置文件。

*   **场景二：Netty 配置讲解 (00:00:05-00:00:15)**
    *   讲师将光标移动到 `netty` 配置块，高亮显示 `port: 19999` 和 `debug: true`，并口头解释这是代理服务监听的端口和调试开关。

*   **场景三：gRPC 配置讲解 (00:00:15-00:00:45)**
    *   讲师将光标移动到 `grpc` 配置块，逐行讲解：
        *   `address: 'discovery:///stock-deal'`：配置客户端通过服务发现机制连接到名为 `stock-deal` 的服务。
        *   `enableKeepAlive: true`：启用长连接，以维持与服务端的连接。
        *   `keepAliveWithoutCalls: true`：即使没有调用，也保持连接活跃。
        *   `negotiationType: plaintext`：设置通信协议为明文。

*   **场景四：PPT 与代码对照 (00:00:55-00:01:15)**
    *   讲师切换到 `Day13.md` 文档，展示 `3.7 代理服务gRpc相关配置` 章节的 PPT 内容，与代码编辑器中的配置进行对照，强调配置项的语义和作用。
