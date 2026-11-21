# 17-简易下单功能-Netty模拟客户端启动配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着咱们开始学习

Netty模拟客户端的编写实现

通过模拟客户端呢

能够便于咱们对功能进行测试和验证

那咱们就从代码层面做个实现

回到工程当中

在StockProxy工程下面的

Test目录下面咱们创建一个包

new package

comitcast

envast

stock proxy

创建完成之后

接着咱们创建模拟客户端

new class

给它一个名称

叫simulate client

编写它的启动方法

psvm

编写客户端的启动方法

start client

这里咱们给它一个参数

先设为now

这个参数呢是用于启动的时候

立即执行的请求方法

比如说登录

或者其他的一些请求

那么通过这些请求

通过这个参数呢

可以指定启动客户端的时候呢

就会自动进行相应的调用

接着咱们去定义服务端的请求IP

以及它的端口

static final stream server IP

27.0.0.1

这个指向本地的服务

这个是服务端的IP

下面咱们再配置服务的端口

vary的

datic final

in

接下来咱们去实现start client的方法

这个参数呢是指定的请求类型

是可以支持指定的请求方法

发送至服务端

这样初始化调用的时候呢

就不需要再去手动指定了

咱们要请求的方法

便于咱们的测试验证

咱们可以指定用户登录的方法

这样start client启动完成之后呢

就已经完成了用户的登录

咱们呢再去指定其他的业务接口

比如说下单

或者是查询计单信息等等

接着咱们继续实现

nety的客户端配置

首先定义英文的

group

这个是负责监听nio事件

接着咱们创建它的启动类

bootstrap

new bootstrap

然后做启动参数的配置

将group设置进去

接着定义channel

采用nio socket的channel

下面呢是通道的参数定义

opinion.dcp

no delay

这个为2

channel opinion

sale

tplive

这个呢也是设为chew

咱们加上对应的注释

这个呢是设置bcp连接配置信息

下面咱们去设置客户端的

打印日志级别

点handle

new login handle

在这里指定log的级别

咱们就打印了info级别日志

下面是初始化通道信息

new login handle

channel

initialize socket-channel

咱们要去重启它的方法

init-channel方法

首先咱们拿到channel的管道

从socket的channel参数当中去获取

接着咱们要去设置

addp

后端的调用配置

在管道当中咱们去添加

new addp

content

addp的一个编码包支持

然后咱们再去添加

adddp object

这个是设置它的一个

巨大buffer大小

咱们就采用index max value

然后是plot

buff的解码黑字

hyperline

点add last

plot buff

首先咱们将它的flame

decode的解码器加入进去

然后hyperline

add last

new total

将它的长度属性

推置性加入进去

接着咱们就要去指定客户端的

数据接收处理器

hyperline

add last

kind

handle

这个是要咱们去制定也实现的

咱们先把这个类写上

后面咱们再做具体的实现

我们先把这个类写上

后面咱们再做具体的实现

将方法传递进去

先创建这个类

new java class

给它一个空实现

下一讲咱们再去做详细的讲解

simple

channel

import handle object

重写channel3的方法

好

回到咱们刚才的

单码编写逻辑

然后再创建一个构造方法

plot add

将构造方法里面的参数

把我们设置进去

定义一个构造方法

将method传入进去

回到我们刚才

今天写的逻辑

接下来呢

还有配置websocket的

协议包的编码

为节省时间

我们从讲义当中

拷笔进来

拷笔到这里

添加进去

将这些包呢

导入进去

这个是net下面的包

导入完成之后

咱们把这些错误呢

涂一下

那我们回过头来

看一下导入的这些代码

这个呢

是针对于websocket的协议包

进行的一个解码

因为咱们知道websocket呢

它传过来是经过包装的数据结构

咱们拿到的是一个websocket的blame

拿到这个对象之后呢

咱们就要做一个判断

如果它是text的文本数据呢

咱们直接将它打印出来就可以

如果是二进制数据格式呢

咱们就要将它进行一个转换

通过bythebuff

将数据呢

转换成为protobuf的数据结构

这个呢是pong

下面呢是close的数据包

之前咱们对serve端的实现呢

也做了相应的讲解

然后下面呢是协议包的编码

咱们通讯定义的是protobuf的pb数据结构

客户端是不能直接拿到pb数据做一个解析

咱们通过websocket发送过去的

同样也要符合它的规范

这里面的编码呢

就是将数据包转换为websocket的blame的包结构

再将这个数据包呢输出给客户端

最后呢就是添加咱们protobuf的解码器

也就是一个数据包接收过来

首先呢要经过websocket的协议包的解码

将它存入至bythebuff

接着的话呢

再通过protobuf的解码器

将bythebuff里面的数据呢

转换为pb对象

这些呢就是客户端的启动配置

客户端启动配置完成之后呢

咱们逻辑还没有处理结束

下面还需要去实现呢

websocket的连接调用配置

websocket的连接触发调用该怎么去实现呢

这个在下一讲咱们再做具体的讲解

那这讲内容呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出：

---

### 1) 视频摘要

本视频课程聚焦于使用 **Netty** 框架模拟一个 **gRPC 客户端**，并集成 **WebSocket** 协议支持。讲师通过在 IntelliJ IDEA 中逐步编写 `SimulateClient` 类，演示了如何构建一个基于 Netty 的异步客户端，该客户端能够连接到服务端、处理 Protobuf 协议的编解码，并最终支持 WebSocket 协议的双向通信。整个过程是典型的 Java 后端服务开发实践，涉及 Netty 的核心组件如 `EventLoopGroup`、`Bootstrap`、`ChannelPipeline` 以及自定义的 `ChannelHandler`。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程引入，讲解本节目标是编写一个 Netty 模拟客户端。
*   **00:16 - 00:30**: 创建 `SimulateClient` 类，定义服务端口 `serverPort = 19999`。
*   **00:31 - 00:45**: 初始化 Netty 客户端，创建 `EventLoopGroup` 和 `Bootstrap` 实例。
*   **00:46 - 01:00**: 配置 TCP 连接选项，如 `TCP_NODELAY` 和 `SO_KEEPALIVE`。
*   **01:01 - 01:15**: 设置客户端的 Channel 类型为 `NioSocketChannel`。
*   **01:16 - 01:30**: 配置 ChannelPipeline，添加 `HttpClientCodec` 和 `HttpObjectAggregator` 用于 HTTP 协议。
*   **01:31 - 01:45**: 添加 Protobuf 解码器 `ProtobufVarint32FrameDecoder` 和 `ProtobufDecoder`。
*   **01:46 - 02:00**: 添加自定义的 `ClientBoundHandler` 作为业务处理处理器。
*   **02:01 - 02:15**: 在 `ClientBoundHandler` 中实现 WebSocket 协议的解码逻辑，区分 `TextWebSocketFrame` 和 `BinaryWebSocketFrame`。
*   **02:16 - 02:30**: 实现 WebSocket 协议的编码逻辑，将 `MessageLite` 对象转换为 `BinaryWebSocketFrame`。
*   **02:31 - 02:45**: 添加 Protobuf 编码器 `ProtobufEncoder`，用于将服务端响应编码为 WebSocket 协议帧。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲显示当前章节为 **3.8 Netty模拟客户端编写**。
    *   文档中提到 `grpc-trade-server` 为 gRPC 服务名称，支持负载均衡。

*   **代码关键内容**:
    *   **`SimulateClient` 类**:
        ```java
        @Log4j2
        public class SimulateClient {
            private static final int serverPort = 19999;
            public static void main(String[] args) {
                startClient(null);
            }
            private static void startClient(StockHeadProto.RequestType method) {
                // Netty客户端启动配置
                EventLoopGroup group = new NioEventLoopGroup();
                Bootstrap bootstrap = new Bootstrap();
                bootstrap.group(group)
                         .channel(NioSocketChannel.class)
                         .option(ChannelOption.TCP_NODELAY, true)
                         .option(ChannelOption.SO_KEEPALIVE, true)
                         .handler(new LoggingHandler(LogLevel.INFO))
                         .handler(new ChannelInitializer<SocketChannel>() {
                             @Override
                             protected void initChannel(SocketChannel socketChannel) throws Exception {
                                 ChannelPipeline pipeline = socketChannel.pipeline();
                                 // 设置http客户端的调用配置
                                 pipeline.addLast(new HttpClientCodec());
                                 pipeline.addLast(new HttpObjectAggregator(Integer.MAX_VALUE));
                                 // protobuf的解码配置
                                 pipeline.addLast(new ProtobufVarint32FrameDecoder());
                                 pipeline.addLast(new ProtobufDecoder(StockHeadProto.getDefaultInstance()));
                                 // 指定客户端的数据接收处理器
                                 pipeline.addLast("client_handler", new ClientBoundHandler(method));
                             }
                         });
                // 配置websocket协议的解码
                pipeline.addLast(new MessageToMessageDecoder<WebSocketFrame, Object>() {
                    @Override
                    protected void decode(ChannelHandlerContext ctx, WebSocketFrame frame, List<Object> out) throws Exception {
                        if (frame instanceof TextWebSocketFrame) {
                            TextWebSocketFrame textFrame = (TextWebSocketFrame) frame;
                            System.out.println("TextWebSocketFrame received: " + textFrame.text());
                        } else if (frame instanceof BinaryWebSocketFrame) {
                            System.out.println("BinaryWebSocketFrame received");
                        } else if (frame instanceof PingWebSocketFrame) {
                            System.out.println("PingWebSocketFrame received");
                        } else if (frame instanceof CloseWebSocketFrame) {
                            System.out.println("CloseWebSocketFrame received");
                        }
                    }
                });
                // 配置websocket协议的编码
                pipeline.addLast(new MessageToMessageEncoder<MessageLiteOrBuilder>() {
                    @Override
                    protected void encode(ChannelHandlerContext ctx, MessageLiteOrBuilder msg, List<Object> out) throws Exception {
                        if (msg instanceof MessageLite) {
                            byte[] bytes = ((MessageLite) msg).toByteArray();
                            BinaryWebSocketFrame frame = new BinaryWebSocketFrame(bytes);
                            out.add(frame);
                        } else if (msg instanceof MessageLite.Builder) {
                            byte[] bytes = ((MessageLite.Builder) msg).build().toByteArray();
                            BinaryWebSocketFrame frame = new BinaryWebSocketFrame(bytes);
                            out.add(frame);
                        }
                    }
                });
                // 添加Protobuf编码器
                pipeline.addLast(new ProtobufEncoder(ResponseMessage.getDefaultInstance()));
            }
        }
        ```

*   **公式 / 图表**:
    *   无公式或图表。

---

### 4) 关键场景与演示描述

*   **场景一：创建客户端类** (00:16-00:30)
    *   讲师在 `test` 包下创建 `SimulateClient` 类，并定义了服务端口 `serverPort = 19999`。这是客户端的基础配置。

*   **场景二：Netty 客户端初始化** (00:31-01:00)
    *   讲师创建 `EventLoopGroup` 和 `Bootstrap` 实例，这是 Netty 客户端的核心组件。`Bootstrap` 用于配置和启动客户端连接。

*   **场景三：TCP 选项配置** (00:46-01:00)
    *   讲师设置 `ChannelOption.TCP_NODELAY` 和 `ChannelOption.SO_KEEPALIVE`，以优化 TCP 连接性能。

*   **场景四：ChannelPipeline 配置** (01:16-02:45)
    *   讲师在 `initChannel` 方法中配置 `ChannelPipeline`，依次添加：
        1.  `HttpClientCodec` 和 `HttpObjectAggregator` 用于 HTTP 协议。
        2.  `ProtobufVarint32FrameDecoder` 和 `ProtobufDecoder` 用于 Protobuf 协议的解码。
        3.  `ClientBoundHandler` 用于处理业务逻辑。
        4.  `MessageToMessageDecoder` 用于 WebSocket 协议的解码。
        5.  `MessageToMessageEncoder` 用于 WebSocket 协议的编码。
        6.  `ProtobufEncoder` 用于 Protobuf 协议的编码。

*   **场景五：自定义处理器 `ClientBoundHandler`** (02:01-02:30)
    *   讲师展示了 `ClientBoundHandler` 的 `decode` 方法，用于处理 WebSocket 协议的帧，区分文本帧和二进制帧，并打印日志。

*   **场景六：WebSocket 协议编码** (02:16-02:30)
    *   讲师展示了 `MessageToMessageEncoder` 的 `encode` 方法，将 Protobuf 消息转换为 `BinaryWebSocketFrame`，以便通过 WebSocket 发送。

*   **场景七：Protobuf 编码器** (02:31-02:45)
    *   讲师添加了 `ProtobufEncoder`，用于将服务端的 Protobuf 响应编码为二进制数据，以便通过 WebSocket 发送。

---
