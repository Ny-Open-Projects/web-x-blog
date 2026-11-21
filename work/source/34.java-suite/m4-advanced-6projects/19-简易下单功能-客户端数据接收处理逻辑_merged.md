# 19-简易下单功能-客户端数据接收处理逻辑 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着去实现NAT模拟客户端

自定义数据接收处理器

咱们回到代码当中

在test的测试目录下面找了Client Bundle Handle

之前咱们实现NAT模拟客户端的时候呢

也对Client Bundle Handle代码做了一些编写

接着咱们就对代码做一个完善

首先咱们在接收数据的处理方法当中

去实现对应的逻辑

这个是客户端数据接收的处理方法

之前咱们通过模拟客户端

发送了WebSocket的初始化握手信息

那么服务端就会将握手响应信息

发送给客户端

咱们在Channel Read方法当中

就能接收到服务端所下发的握手响应消息

看一下这一块该如何去处理实现

首先咱们去定一个通道

ch 将包导入进来

参数名称咱们改成ctx

这个对象呢

改成message cdx.panel

接下来定义一个HTTP响应对象

做一个判断

拿到Handshake对象

判断了握手是否已经结束

因为这个消息接收呢

是一个义不出力的

Socket连接建立过程当中呢

服务端也可能会发送各种类型消息

如果是服务端的握手响应消息呢

那么咱们在这里的Handshake

必须是先将封装的握手消息发送给服务端

接着response对象

咱们做一个转换

gooHTTP response

对message消息做一个强转

拿到握手消息之后

咱们就要做一个结束处理

结束握手的处理

通过

Handshake

要用finish Handshake方法

传递通道以及响应消息

然后要标记握手成功

list.Handshake

set success

这里要做一个challenge处理

ctrl t

选择第六项

生成了challenge代码

这个异常呢

就可能是握手处理的异常

Handshake exception

如果是出现错误

咱们要在这里标记为失败

gooHTTP response is

装错误消息

syn.format

websocket

client

build

connc

test

is.states

is.content

.tospin

这页码呢

采用UTF-8

然后这里呢要做一个标记

Handshake

Handshake future

set failure

放进一个异常

将admessage传递进去

握手消息处理完成之后

接着咱们再去判断其他消息类型

如果在未完成握手消息的发送之前

就已经接收到了HTTP消息

那么咱们在这里呢

就要抛出对应的异常

接收到HTTP响应消息

未完成握手时

response

will

adtp

response

将message做一个强转

直接抛出异常消息

exception

给它一个提示

同样返回状态

返回它的原因

response.getstates

外层加上syn.format

response.content

点图screen

键码呢

用getstates utf-8

点utf-8

接着就是接收二进制的数据

因为咱们是采用websocket的通讯

所以呢

这里接收到的数据就是就是一个

其实就是一个websocket的flame包

将包导入进来

websocket的flame

message

拿到websocket的包呢

咱们做一个判断

isTainsAll

如果它是一个

文本的数据呢

咱们在这里呢

就直接将它打印出来

因为咱们是通过pb数据作为传输

所以文本的话呢

一般是不会接收到的

除非是你传递了一些错误的数据

则是

让它打印出来

从mc5

text

标识呢

已经接收到了一个文本的数据

接着

再判断

如果

它是一个banderly

二进制数据

这个呢

就是咱们所预期要接收到的业务数据

那么我们就要将它进行一个转换

banderly

将它进行强转

通过bytebuffer

做对应处理

stream.content

再通过bytebuffer

将它转换为

字节数据

bytebuffer

util

getbiz

这里要传入bytebuffer

bytebuffer.zindex

bytebuffer

它的可读的数据大小

这里不将它进行copy

直接读取

那么读取完成之后呢

bytebuffer里面就不会再有二进制数据

这一点要注意一下

拿到二进制业务数据呢

咱们就要做相应的逻辑处理

在这里咱们通过一个方法去做对应的实现

response

message

pageform

page form

将字节数据呢

转换为

response message对象

距离实现呢

咱们在下个章节

再作处理

先给它添加对应的注释

这个呢是

接收

服务端

发送的

ProtoBuffer

业务消息

这个方法

咱们要将客户端所接收的服务消息

打印出来

将业务消息打印出来

咱们再回到刚才的主逻辑

这里我们给出一个提示信息

说已经接收到了二进制的数据消息

接着呢

还会有其他的消息类型

比如说发送过来的PIN消息

这里是PUN

WEB

Socket Flame

咱们直接将它打印出来就可以了

Resale

PUN Message

最后呢

还有一种消息类型

之前咱们也讲过

这个呢就是关闭的消息

Code

WebSocket Flame

咱们呢也将它打印出来

获取一下

最后将通道进行关闭

在这里呢

咱们就完成了客户端数据接收的处理逻辑

那这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个基于 Netty 和 gRPC 的股票行情代理服务的开发教程。讲师正在讲解如何实现一个 `ClientBoundHandler` 类，该类负责处理客户端（模拟客户端）与代理服务器之间的 WebSocket 连接和消息交互。核心内容包括：
- **WebSocket 握手处理**：实现 `channelRead0` 方法，处理客户端的 HTTP 握手请求。
- **异常处理**：捕获 `WebSocketHandshakeException` 并返回错误响应。
- **消息解析**：定义 `recvProtoMsg` 方法用于接收并解析服务端发送的 Protobuf 格式业务消息。
- **代码结构**：代码基于 IntelliJ IDEA 编写，项目结构清晰，包含 `StockProxyServerHandler`、`StockProxyServerInitializer` 等核心组件。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下时间点是根据画面内容和逻辑顺序推断的：

- **0:00 - 0:15**: 课程介绍与项目背景。讲师提到这是第3章“代理服务登陆鉴权实现”的第8节“Netty模拟客户端编写”，并展示了项目结构和 `ClientBoundHandler` 类的初始代码。
- **0:15 - 0:30**: WebSocket 握手处理逻辑。讲师开始编写 `channelRead0` 方法，处理客户端的 HTTP 握手请求。
- **0:30 - 0:45**: 异常处理与错误响应。讲师添加了 `catch` 块，用于捕获 `WebSocketHandshakeException` 并构造错误响应。
- **0:45 - 1:00**: 消息解析与业务逻辑。讲师定义了 `recvProtoMsg` 方法，用于接收并解析服务端发送的 Protobuf 格式业务消息。
- **1:00 - 1:15**: 代码调试与优化。讲师对代码进行了调试，并添加了注释和日志记录。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### 关键代码片段

**`ClientBoundHandler` 类定义**

```java
@Log4j2
public class ClientBoundHandler extends SimpleChannelInboundHandler<Object> {
    // 定义请求类型，用来记录需要发送的预置消息（连接建立后即发送）
    private StockHeadProto.RequestType method;

    // WebSocket 握手消息的响应配置通道
    private WebSocketClientHandshaker handshaker;
    private ChannelPromise handshakeFuture;

    @Override
    protected void channelRead0(ChannelHandlerContext ctx, Object msg) throws Exception {
        Channel ch = ctx.channel();
        FullHttpResponse response;

        if (!this.handshaker.isHandshakeComplete()) {
            // 处理握手请求
            try {
                response = (FullHttpResponse) msg;
                this.handshaker.finishHandshake(ch, response);
                this.handshakeFuture.setSuccess();
            } catch (WebSocketHandshakeException e) {
                FullHttpResponse res = (FullHttpResponse) msg;
                String errorMsg = String.format("WebSocket Client failed to connect, status: %s", res.status());
                this.handshakeFuture.setFailure(new Exception(errorMsg));
            }
        } else if (msg instanceof FullHttpResponse) {
            // 接收到http响应消息（未完成握手）
            response = (FullHttpResponse) msg;
            throw new IllegalStateException(String.format("Unexpected FullHttpResponse, status: %s, reason: %s", response.status(), response.content().toString()));
        }
    }

    // 接收服务端发送的Protobuf业务消息，将业务消息打印出来
    @Override
    protected void channelRead0(ChannelHandlerContext ctx, Object msg) throws Exception {
        // 业务消息处理逻辑
        // ...
    }

    private void recvProtoMsg(ResponseMessage parseFrom) {
        // 业务消息解析逻辑
        // ...
    }
}
```

#### 关键注释

- `// 定义请求类型，用来记录需要发送的预置消息（连接建立后即发送）`
- `// WebSocket 握手消息的响应配置通道`
- `// 标记握手响应成功`
- `// 接收到http响应消息（未完成握手）`
- `// 接收服务端发送的Protobuf业务消息，将业务消息打印出来`

---

### 4) 关键场景与演示描述

#### 场景一：WebSocket 握手处理

讲师在 `channelRead0` 方法中处理客户端的 HTTP 握手请求。首先，检查握手是否完成，如果未完成，则调用 `handshaker.finishHandshake` 方法完成握手，并设置 `handshakeFuture` 为成功状态。如果握手失败，则捕获 `WebSocketHandshakeException` 并构造错误响应。

#### 场景二：异常处理

讲师添加了 `catch` 块，用于捕获 `WebSocketHandshakeException`。在 `catch` 块中，构造一个 `FullHttpResponse` 对象，并设置错误消息，然后将 `handshakeFuture` 设置为失败状态。

#### 场景三：消息解析

讲师定义了 `recvProtoMsg` 方法，用于接收并解析服务端发送的 Protobuf 格式业务消息。在该方法中，可以对消息进行解析和处理。

#### 场景四：代码调试与优化

讲师对代码进行了调试，并添加了注释和日志记录。在调试过程中，讲师对代码进行了优化，使其更加清晰和易于维护。

---

以上是根据视频画面进行的结构化技术分析。希望对您有所帮助。
