# 14-简易下单功能-Netty WebSocket集成配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始学习代理服务和Netit的集成配置

以及对WebSocket的支持

为什么要增加WebSocket呢

因为咱们要为了支持H5终端的行情数据的呈现

H5它需要通过WS实现长连接

所以在这里咱们增加了WebSocket的支持

让H5终端能够拿到行情数据

那咱们来看一下

如何通过Netit去实现WebSocket

以及如何通过Netit去实现客户端和服务端数据的收发

首先咱们要在代理服务当中增加Netit的依赖组件

Blocks下面的POM文件咱们要检查一下

在这里要加入Netit的组件

让它导入生效

鼠标Ctrl

可以看到它已经找到对应组件

接着咱们去看看

我们去实现Netit的集成配置

在这里创建一个新的包

New Package

叫Netit

咱们先实现Netit服务端的配置

作为代理服务来讲

它就是客户端的服务端

那咱们去创建一个配置类

名称叫Stock

Blocks

Server

Initial

添加注解支持

Compander

加上日志注解

这里要继承Netit里面的Channel Initialize的接口

这里是Sockit的Channel对象

对于这个包是在Netit下面

然后咱们来做一个实现

首先给它一个控制标识

这个是用来控制是否需要开启Netit的调整日志

让它去读取

属性配置

属性配置名称叫Sockit.Netit.Channel

Netit.Channel

Netit.Channel

Debug

默认的话是False

将Value导入进来

这个是选第一个指定Flamework下面的包

接下来咱们要去定义一个服务端的数据处理器

Stock Proxy

这个处理器咱们稍后再做实现

先定义在这里

为了避免暴错

咱们先将这个类添加进去

让它注入进来

这个类主要是Netit数据的接收

以及发送处理

咱们给它添加对应的注释

接下来去初始化连接通道

Protect

Void

Init Channel

传递参数

Socket Channel

Exception

这个是重写

添加对应的注释

服务端

连接通道的初始化配置

咱们就来做一个具体实现

首先定义一个ChannelPile

这个是服务端的连接管道

接着咱们做一个判断

这里是判断

是否开启调试日子功能

如果开启了

咱们要将它的配置

放到管道当中

给它放进一个Login Handle

去记录Network日子

然后咱们要去增加

对ATDP

收我的支持

因为Network是一个

Socket的通信框架

对不对

要加上相应的配置

这里是初始化包的大小

ATDP要对包做编码处理

6ATDP

Servo Code

这个内

会将接收到的数据

封装为ATDP的传输包

下面是ATDP的

聚合解析

这里是设置聚合内容的长度

最大长度

这个呢也是添加进去

6ATDP Object

Add greater

给它一个最大值

下面呢

是要支持大数据流的写入

Add last

New

Chunked

Right Handle

下面是支持Web Socket的数据压缩功能

Hipeline

Add last

New

Web Socket

Servo Compilation Handle

然后呢是Web Socket的协议配置

这里面呢就是比较关键的Web Socket服务的配置

咱们要去设置它的访问路径

Hipeline

Add last

New

Web Socket

Servo Portal

第一个参数呢

是Web Socket的访问路径

这个就类似于咱们TalentCAD服务当中的服务

后转

对

第二个参数是指协议

这一块是不需要

第三个参数是否允许扩展

这个可以支持

最后一个参数是征战包的最大大小

这里呢

咱们就采用最大值了

咱们在这里Web Socket的通讯呢

采用的是PB作为数据载体

所以咱们需要配置Proton的解码器

ProtonBuff的解码器

Hipeline

Add last

New ProtonValue32

HipelineAdd last New ProtonValue32

这个呢

是它的解码器

HipelineAdd last New ProtonValue32

这个呢

是它的一个长度编码处理

再往下面呢

就要实现Web Socket的通讯包的编码和解码处理

因为Web Socket呢

它有自己的通讯规范

Web Socket主要有三种通讯数据包

一种是Text的文本格式

另一种是Binary二进制的通讯数据包

另外一种是Tax的文本格式

最后一种呢

就是PIN的报文

它是用于检测整个连接的健康状态

这里咱们就不再去逐一敲写

为了快速实现呢

节约点时间

咱们就从讲习当中呢

科比进来

从这里开始

好到这里结束

将错误信息呢

先处理一下

导入对应的包

Neti的包下面

这些都是Neti包下面了

将这些错误处理完成之后

咱们再做一个详细讲解

这个是服务端的数据处理器

是刚才咱们的数据处理器

是刚才咱们定义的一个空的实现类

它要去继承SIMPLE

CHANNEL INBUNDED HANDLE的抽象类

这个是翻形

传递Stock message

去实现它的方法

CHANNEL类的

具体实现了

咱们下面章节还会做

具体实现了

咱们在下面章节再做对应处理

好在这里就没有包缩

那咱们来看一下WebSocket的协议

它的包解码

以及呢

包编码是如何处理的

这个是WebSocket的

包解码的处理呢

是通过Message decode的

它传递的是WebSocket的通讯包

拿到WebSocket的通讯包

该怎么去处理呢

先不要采用ProBuf的解码器

下面会做相应的判断

如果这个包呢

它属于文本格式

直接转换为TexWebSocketFrame

去做相应的处理

如果它属于二进制

Binary数据包

这个时候呢

就要去读取它的Content

Content是一个BitBuffer

其实就是二进制数据

那么BitBuffer收集完成数据之后

会通过ProBuf编码器

做相应的编码处理

封装成为具体的业务对象

然后下面是其他格式的包

这个Porn就是所发送的Pin包

一般都是健康检测

如果不需要特殊处理呢

在这里打印相应日志就可以了

这个Close呢

是一个关闭的提示数据包

如果接收到这个提示包呢

说明客户端这个连接呢

已经中断了

那咱们呢

就要进行通道的关闭

下面呢

就是WebSocket的协议包的编码

处理流程呢

基本上也是一致的

不同的是呢

一个是解码

一个呢

是编码

下面呢

是WebSocket的协议包的编码处理流程

那同样的

咱们的业务数据编码完成之后呢

要符合WebSocket的通讯数据包的格式

这里呢

拿到数据包之后

会将它转换为二进制数组

转换完成之后呢

再转成WebSocket的二进制流

因为客户端呢

他不能够直接去解析Provaful编码

所生成的数据

必须要包装成为WebSocket的通讯

所规范的数据格式

咱们可以看到这里呢

做了一层封装

好

那么前端呢

他就可以根据WebSocket的数据包呢

再做相应的转换

最后呢

按照Provaful的协议格式

就可以拿到对应的业务数据

下面呢

是Provaful解码器的一个配置

上面咱们定义的解码器呢

是说明通讯所获得的数据呢

是一个PB格式的数据信息

但是Provaful数据

最终会转换成为一个什么样的业务对象

咱们在这里呢

要声明一下

这个业务对象呢

必须是咱们能够识别的

那就在咱们PB当中

所定义的StockMessage

这个呢就是咱们定义的完整的交互数据包

配置完成之后

最后就是配置咱们自定义的数据处理器

在处理器当中

可以对接收的数据做相应的处理

好

在这里呢

就是对NetEase的集成配置

以及呢

通过NetEase去实现了WebSocket的配置

这些固端呢

就能够按照WebSocket的协议呢

泄露到咱们服务后台当中

好那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“bulls-stock-proxy”的Java项目，其核心目标是实现一个基于Netty框架的WebSocket代理服务。讲师通过IDE（IntelliJ IDEA）逐步演示了如何配置项目、编写初始化器（`StockProxyServerInitializer`）和处理器（`StockProxyServerHandler`）来处理WebSocket连接。整个过程聚焦于构建一个能够接收、解析并转发WebSocket消息的代理服务器，特别强调了使用`ChannelPipeline`来组装处理链，并处理不同类型的WebSocket帧（如文本、二进制、Ping、Pong、Close）。视频内容属于微服务架构中服务间通信或API网关的实现范畴。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:04**: 视频开头，讲师在Typora编辑器中展示课程大纲，定位到“3.6 代理服务Netty集成与Websocket支持”章节。
*   **00:05 - 00:10**: 讲师切换到IDE，展示项目结构，并开始编写 `StockProxyServerInitializer` 类。
*   **00:11 - 00:20**: 讲师在 `StockProxyServerInitializer` 类中添加 `@Component` 和 `@Log4j2` 注解，并声明一个 `debug` 配置属性。
*   **00:21 - 00:30**: 讲师开始编写 `initChannel` 方法，用于初始化ChannelPipeline。
*   **00:31 - 00:40**: 讲师添加 `LoggingHandler` 用于调试日志，并添加 `HttpObjectAggregator` 和 `ChunkedWriteHandler`。
*   **00:41 - 00:50**: 讲师添加 `WebSocketServerProtocolHandler`，配置WebSocket路径为 `/stock`。
*   **00:51 - 01:00**: 讲师添加 `ProtobufVarint32FrameDecoder` 和 `ProtobufVarint32LengthFieldPrepender` 用于处理Protobuf协议。
*   **01:01 - 01:10**: 讲师编写 `MessageToMessageDecoder<WebSocketFrame>`，用于解析不同类型的WebSocket帧。
*   **01:11 - 01:20**: 讲师编写 `MessageToMessageEncoder<MessageLite.Builder>`，用于将消息编码为字节流。
*   **01:21 - 01:30**: 讲师切换到 `StockProxyServerHandler` 类，开始编写 `channelRead0` 方法。
*   **01:31 - 01:40**: 讲师在 `StockProxyServerHandler` 中实现 `channelRead0` 方法，处理接收到的WebSocket帧。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: `3.6 代理服务Netty集成与Websocket支持`
    *   **POM依赖**: `io.netty:netty-all`
    *   **类注解**: `@Component`, `@Log4j2`
    *   **配置属性**: `@Value("${socket.netty.debug:false}") private boolean debug;`
    *   **处理器类**: `StockProxyServerInitializer extends ChannelInitializer<SocketChannel>`
    *   **处理器类**: `StockProxyServerHandler extends SimpleChannelInboundHandler<StockMessage>`

*   **关键代码片段**:

    **`StockProxyServerInitializer` 类 (初始化器)**

    ```java
    @Component
    @Log4j2
    public class StockProxyServerInitializer extends ChannelInitializer<SocketChannel> {

        @Autowired
        private StockProxyServerHandler stockProxyServerHandler;

        @Override
        protected void initChannel(SocketChannel ch) throws Exception {
            ChannelPipeline pipeline = ch.pipeline();

            // 调试日志
            if (debug) {
                pipeline.addLast(new LoggingHandler());
            }

            // HTTP SERVER支持
            pipeline.addLast(new HttpObjectAggregator(Integer.MAX_VALUE));
            pipeline.addLast(new ChunkedWriteHandler());

            // WebSocket协议支持
            pipeline.addLast(new WebSocketServerProtocolHandler("/stock", null, true));

            // Protobuf解码器
            pipeline.addLast(new ProtobufVarint32FrameDecoder());
            pipeline.addLast(new ProtobufVarint32LengthFieldPrepender());

            // 协议解码器
            pipeline.addLast(new MessageToMessageDecoder<WebSocketFrame>() {
                @Override
                protected void decode(ChannelHandlerContext ctx, WebSocketFrame frame, List<Object> out) {
                    if (frame instanceof TextWebSocketFrame) {
                        // 处理文本帧
                    } else if (frame instanceof BinaryWebSocketFrame) {
                        // 处理二进制帧
                    } else if (frame instanceof PingWebSocketFrame) {
                        // 处理Ping帧
                    } else if (frame instanceof PongWebSocketFrame) {
                        // 处理Pong帧
                    } else if (frame instanceof CloseWebSocketFrame) {
                        // 处理Close帧
                        ch.close();
                    }
                }
            });

            // 协议编码器
            pipeline.addLast(new MessageToMessageEncoder<MessageLite.Builder>() {
                @Override
                protected void encode(ChannelHandlerContext ctx, MessageLite.Builder msg, List<Object> out) {
                    // 编码逻辑
                }
            });
        }
    }
    ```

    **`StockProxyServerHandler` 类 (处理器)**

    ```java
    public class StockProxyServerHandler extends SimpleChannelInboundHandler<StockMessage> {

        @Override
        protected void channelRead0(ChannelHandlerContext ctx, StockMessage stockMessage) {
            // 处理接收到的StockMessage
        }

        @Override
        public void channelInactive(ChannelHandlerContext ctx) throws Exception {
            // 处理通道关闭
            super.channelInactive(ctx);
        }

        @Override
        public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
            // 处理异常
            super.exceptionCaught(ctx, cause);
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖管理 (00:00-00:10)**
    *   讲师首先在Typora中定位到课程大纲，明确本节目标是集成Netty并支持WebSocket。
    *   随后，讲师在IDE中打开项目，展示其模块结构（如 `bulls-stock-proxy`），并开始创建 `StockProxyServerInitializer` 类。

*   **场景二：初始化器配置 (00:11-01:10)**
    *   讲师在 `StockProxyServerInitializer` 中添加了Spring的 `@Component` 注解，使其能被Spring容器管理。
    *   讲师添加了 `@Log4j2` 注解用于日志记录。
    *   讲师定义了一个 `debug` 属性，用于控制是否启用调试日志。
    *   讲师编写了 `initChannel` 方法，这是Netty中初始化ChannelPipeline的核心方法。
    *   讲师依次添加了 `LoggingHandler`、`HttpObjectAggregator`、`ChunkedWriteHandler`、`WebSocketServerProtocolHandler`、`ProtobufVarint32FrameDecoder` 和 `ProtobufVarint32LengthFieldPrepender` 等处理器，构建了完整的处理链。

*   **场景三：WebSocket帧解码器 (01:11-01:30)**
    *   讲师编写了一个 `MessageToMessageDecoder<WebSocketFrame>`，用于将接收到的WebSocket帧解码为可处理的对象。
    *   通过 `instanceof` 判断帧的类型（`TextWebSocketFrame`, `BinaryWebSocketFrame`, `PingWebSocketFrame`, `PongWebSocketFrame`, `CloseWebSocketFrame`），并分别进行处理。
    *   对于 `CloseWebSocketFrame`，讲师调用 `ch.close()` 关闭通道。

*   **场景四：消息编码器 (01:31-01:40)**
    *   讲师编写了一个 `MessageToMessageEncoder<MessageLite.Builder>`，用于将业务消息编码为字节流。
    *   该编码器会将 `MessageLite.Builder` 对象转换为 `ByteBuf`，以便通过Netty的Channel发送出去。

*   **场景五：处理器实现 (01:41-01:50)**
    *   讲师切换到 `StockProxyServerHandler` 类，该类继承自 `SimpleChannelInboundHandler<StockMessage>`。
    *   讲师实现了 `channelRead0` 方法，用于处理接收到的 `StockMessage`。
    *   讲师还实现了 `channelInactive` 和 `exceptionCaught` 方法，用于处理通道关闭和异常情况。

---

以上是根据视频画面进行的详细技术分析。
