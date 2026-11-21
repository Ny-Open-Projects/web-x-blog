# 18-简易下单功能-WebSocket初始化配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着去实现NetEase的模拟调用客户端

之前咱们实现了NetEase模拟客户端的启动配置

接着咱们就去实现WebSocket的初始化以及连接调用配置

首先咱们创建一个对象

Channel Feature

接下来咱们去定一个UI

WebSocket

URI

这个用于WebSocket的连接

咱们要对它的UI做一个格式化

它的前缀是WS

%s是代表变量参数

后面再跟%d

然后再跟上后缀stock

收入IP

收入port传递进去

%s是代表一个实讯类型

%d代表是一个数值类型

外层还有加一个括号

咱们还给它加上一个外围的异常补货

我们还给它加上一个外围的异常补货

Ctrl Alt加T

选择Shared Cache

这里异常类型咱们改一下

改成最大的异常

然后通过日志打印一下

咱们加上日志的查件

Nobo Project 2

因为在这里是一个模拟客户端

咱们可以通过日志打印

也可以将它的异常站

直接输出在控制终端

接下来咱们就去对WebSocket的连接

进行一个初始化配置

首先创建HTTP

Headers

Evolved HTTP Headers

下面就进行初始化

连接握手

通过WebSocket

Client

Handshake

WebSocket Client Handshake

创建一个New Handshake

将UID地址传递进去

然后传递WebSocket的协议版本

我选

咱们采用V13

我们选择V13

此协议为空

是否允许拓展

在这里设备Q

可以用HTTP Headers

将头部信息传递进去

最大小

可以用HTTP Headers

大家注意WebSocket

它一定要进行握手

这样它才能建立一个有效的

长连接

然后将日志

盘一下

这样就Ready to connect Handshake

下面要连接至WebSocket的服务

建立真正的连接通道

要获取channel连接通道

进一个channel对象

通过hoststrap connect建立连接

这里要传递websocket的主题信息

gethost

还有websocket的关口信息getport

进行主设施调用

获取了连接通道

接下来咱们就要拿到客户端的连接通道

将这里配置的握手信息发送给服务端

让咱们做个实现

这里是获取连接通道

发送握手信息

client

counter handle

handler

要做一个转换

这个是咱们制定的业务数据处理器

channel.

pipeline

pipeline

get

counter

handler

这个大家之前应该还记得

就是咱们在上面所定义的counter handle

它放置在pipeline里面

那么就会通过pipeline

从这个属性当中获取

client

counter handle对象

接着咱们要将通道放到head check里面

它要拿取到一个有效通道

才能进行初始化握手信息的交互

然后咱们将

hand check

这个

放置在咱们的handle当中

咱们去制定业务数据处理器当中

去定义一个hand check

private

web socket

counter

hand check

让它导入进来

在neti包下面

这个是web

software

握手配置信息

给它一个set方法

edit

insert

这样子方法放置下面

接着回到刚才的处理逻辑

那咱们就可以将这个hand check呢

放在咱们的制定数据通道当中

点set

hand check

接着咱们就要去发送握手消息

咱们回到制定业务数据处理器当中

再去定义一个属性

定义channel promise

这个呢就用于web socket的握手处理

channel promise呢

无论成功或失败

都会有一个消息响应

这里呢是web

software的握手

消息的响应配置通道

咱们给它定一个方法

让它能够对外进行访问

public

channel

social

hand check

将这个对象呢

返回出去

这里是future

导入对应的包

neti下面

再回到咱们的主逻辑

接着咱们就可以发送对应的握手信息

future

handler

hand check future

目测是调用

咱们再打印一下

它的输出日志

hand check

complete

好在这里呢就是客户端

对web socket的数字化以及连接调用配置

那这一讲咱们就先讲到这里了

我们下期再见

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个 Java 项目中，如何使用 Netty 框架实现一个 WebSocket 客户端，用于连接一个基于 gRPC 的股票行情代理服务。核心内容是 `SimulateClient` 类的实现，它通过 Netty 的 `Bootstrap` 创建一个 `Channel`，并使用 `WebSocketClientHandshaker` 进行握手，最终将自定义的 `ClientBoundHandler` 添加到管道中以处理后续的业务消息。视频重点在于演示如何将 gRPC 的 `MessageLite` 序列化后的二进制数据，通过 WebSocket 协议发送给服务端，并在客户端接收和处理。

---

### 2) 按时间顺序的章节（带时间点）

*   **0:00 - 0:10**: 展示 `SimulateClient` 类的代码，重点是 `pipeline.addLast(new ProtobufDecoder(...))`，用于解码服务端返回的 Protobuf 消息。
*   **0:10 - 0:20**: 代码跳转到 `WebSocket` 连接配置部分，定义了 `serverIp` 和 `serverPort`，并创建 `URI websocketURI`。
*   **0:20 - 0:30**: 初始化 `HttpHeaders`，并创建 `WebSocketClientHandshaker`，配置 `subprotocol` 和 `allowExtensions`。
*   **0:30 - 0:40**: 使用 `bootstrap.connect(...)` 建立连接，并创建 `ChannelFuture`。
*   **0:40 - 0:50**: 将 `ClientBoundHandler` 添加到管道中，并设置 `handshaker`。
*   **0:50 - 1:00**: 调用 `handshakeFuture().sync()` 等待握手完成，并打印日志。
*   **1:00 - 1:10**: 切换到 `ClientBoundHandler` 类，展示其继承自 `SimpleChannelInboundHandler`，并持有 `WebSocketClientHandshaker` 实例。
*   **1:10 - 1:20**: 在 `ClientBoundHandler` 中，`channelRead0` 方法被调用，用于处理接收到的业务数据。
*   **1:20 - 1:30**: 代码回到 `SimulateClient`，展示 `handshakeFuture().sync()` 的调用，等待握手完成。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **WebSocket 连接配置**:
        ```java
        URI websocketURI = new URI(String.format("ws://%s:%d/stock", serverIp, serverPort));
        HttpHeaders httpHeaders = new DefaultHttpHeaders();
        WebSocketClientHandshaker handshaker = WebSocketClientHandshakerFactory.newHandshaker(
            websocketURI, WebSocketVersion.V13, null, true, httpHeaders, Integer.MAX_VALUE);
        Channel channel = bootstrap.connect(websocketURI.getHost(), websocketURI.getPort()).sync().channel();
        ClientBoundHandler handler = new ClientBoundHandler(method);
        handler.setHandshaker(handshaker);
        handler.handshakeFuture().sync();
        ```
    *   **Protobuf 解码器**:
        ```java
        pipeline.addLast(new ProtobufDecoder(ResponseMessage.getDefaultInstance()));
        ```
    *   **消息发送**:
        ```java
        if (msg instanceof MessageLite) {
            result = wrappedBuffer((MessageLite) msg).toByteArray();
        } else if (msg instanceof MessageLite.Builder) {
            result = wrappedBuffer((MessageLite.Builder) msg).build().toByteArray();
        }
        // 下面再转成websocket二进制流，因为客户端不能直接解析protobuf编码生成的WebSocketFrame frame = new BinaryWebSocketFrame(result);
        out.add(frame);
        ```
    *   **ClientBoundHandler**:
        ```java
        public class ClientBoundHandler extends SimpleChannelInboundHandler<Object> {
            private WebSocketClientHandshaker handshaker;
            public ClientBoundHandler(StockHeadProto.RequestType method) {
                this.method = method;
            }
            @Override
            protected void channelRead0(ChannelHandlerContext ctx, Object msg) throws Exception {
                // 处理接收到的消息
            }
        }
        ```

*   **关键注释**:
    *   `// 下面再转成websocket二进制流，因为客户端不能直接解析protobuf编码生成的`
    *   `// WebSocket的连接调用配置`
    *   `// 初始化，配置握手`
    *   `// 连接WebSocket服务，获取channel连接通道`
    *   `// 获取连接通道，发送消息`

---

### 4) 关键场景与演示描述

*   **场景一：WebSocket 客户端初始化与连接** (0:10 - 0:40)
    *   **演示**: 视频展示了如何在 `SimulateClient` 中初始化一个 `URI`，并创建一个 `WebSocketClientHandshaker`。它配置了 WebSocket 版本（`V13`）、允许扩展（`true`）和最大帧大小（`Integer.MAX_VALUE`）。然后，它使用 `Bootstrap` 连接到指定的服务器地址和端口，创建一个 `Channel`。
    *   **技术点**: 展示了 Netty 中 `WebSocketClientHandshaker` 的使用，以及如何通过 `Bootstrap.connect()` 建立网络连接。

*   **场景二：添加业务处理器与握手** (0:40 - 1:00)
    *   **演示**: 代码将一个自定义的 `ClientBoundHandler` 实例添加到 `Channel` 的管道中。然后，通过调用 `handshaker.handshake(channel)` 方法，触发 WebSocket 握手流程。`handshakeFuture().sync()` 用于阻塞当前线程，直到握手完成。
    *   **技术点**: 展示了如何将自定义的 `ChannelHandler` 添加到 Netty 管道中，以及如何使用 `WebSocketClientHandshaker` 进行握手。

*   **场景三：处理接收到的业务消息** (1:10 - 1:30)
    *   **演示**: 视频切换到 `ClientBoundHandler` 类，展示了其继承自 `SimpleChannelInboundHandler`。当 `channelRead0` 方法被调用时，它会处理从服务端接收到的 `Object` 类型的消息。虽然视频没有展示具体的业务处理逻辑，但通过 `@Override` 标注，表明该方法是处理业务数据的核心。
    *   **技术点**: 展示了 Netty 中 `ChannelHandler` 的设计模式，以及如何在 `channelRead0` 中处理接收到的数据。

*   **场景四：Protobuf 消息的发送与解码** (0:00 - 0:10)
    *   **演示**: 视频展示了如何将 `MessageLite` 或其 `Builder` 类型的对象序列化为字节数组。然后，它将字节数组包装成 `BinaryWebSocketFrame`，并添加到 `Channel` 的输出队列中，以便通过 WebSocket 发送出去。在接收端，`ProtobufDecoder` 被添加到管道中，用于将接收到的字节流解码为 `ResponseMessage` 对象。
    *   **技术点**: 展示了如何将 Protobuf 消息通过 WebSocket 发送，并在客户端使用 `ProtobufDecoder` 进行解码。

---

以上是根据视频画面进行的结构化分析，旨在提供清晰的技术要点和场景描述。
