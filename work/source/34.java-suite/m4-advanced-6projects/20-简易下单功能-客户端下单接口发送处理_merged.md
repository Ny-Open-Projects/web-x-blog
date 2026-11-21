# 20-简易下单功能-客户端下单接口发送处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来咱们接着去完善Neti模拟客户端

去实现接口数据交互处理逻辑

咱们先把客户端所接收到的服务消息打印出来

stockhead

plot

连stockhead

先获取他的头部

这个改成message

连stockhead

然后咱们将日志输出

提示接收到服务端的消息

打印消息虚拟号

stockhead.getServiceID

打印出请求消息类型

这个就知道是哪个接口所返回的消息

将响应状态打印出来

stockhead

getState

打印message

message.get

将message内容打印出来

然后咱们要做接口的判断

不同的接口

它的响应业务数据结构是不一样的

所以咱们在这里要做一层判断

根据它的请求类型判断

然后咱们去拿取对应的业务接口返回对象

这里咱们只实现了整理下单的功能

所以在这里咱们只需要判断

是否属于下单接口

下单接口咱们是将订单ID返回出来

所以在这里咱们去拿到订单ID

getDueID

咱们再完善其他方法

editInsert

将exceptionCode

重写一下

咱们需要将通脏关闭

再将对应的日志错误消息打印出来

接下来咱们还要去实现交互指令

通过指令咱们去控制接口数据的发送

比如说咱们可以定义序号为1

然后就是发送用户登录接口

序号为2就是发送用户下单接口

这样咱们测试操作起来

这样咱们测试操作交互起来

就会比较方便

那我们来做对应的实现

这个方法

这里面是显示咱们所有的交互菜单指令

显示

主菜单列出所有的交互指令

cissout

给他一个提示

cissout

这里比如序号为1

咱们就代表用户登录

给出他的提示

用户登录

cissout

序号为2呢

就代表下单

PaceOrder

这个是用户下单

咱们给出对应的提示

接下来咱们再给出一个指令

返回主菜单

这个就是退出当前的交互界面

最后呢

咱们要给他一个退出的指令

比如说0就代表退出

退出

客户端

有了菜单

那在启动模拟客户端的时候呢

就要将他打印出来

对不对

我们看一下这块该在哪里处理呢

ElectInsert

去重写

ChannelActive的方法

这个就代表通道已经激活

和服务端能够建立正常的连接

那咱们就在这里呢

将菜单打印出来

这里咱们就通过易步的方式

UseWrite

New Roundable

然后这里呢

就是使用menu

Ctrl-Alt-T

加上TryCatch

接着呢

就是启动现成

Start

这个就是显示

模拟客户端

这个就是显示

模拟客户端

这个就是显示

的功能菜单

有了菜单指定之后

咱们怎么去发送用户下单的接口数据呢

那么咱们再封装一个类

New Java Class

类的名称呢

咱们就叫BusinessHandler

加上日志书简

公共截图

进一个Channel

导入进来

给他一个各种方法

将Channel注入进去

List.Channel

然后咱们再定一个消息序号

Static

这个就采用静态类型

Sequence ID

默认为0

这个是消息的序列号ID

再封装一个消息发送的方法

Private Send Message

将消息传递进来

Message导入进来

这里呢

是Blobop的Message

通过连接通道发送指定的消息

首先咱们去判断一下

如果连接通道

它违控

或者Message也是违控

或者连接通道

它不能够写入

这些都属于异常的情况

咱们就不需要进行消息的发送

接着通道正常的话

咱们就将数据消息发送出去

接下来咱们再去实现下单接口的数据封装

Paste Order

加上注释

下单

数据

接口

咱们在这里要将下单的信息封装下

这个是下单方向

Intent

Revek

默认为0

然后是请求执行价格

也就是下单的委托价格

Long

Excuse

Price

比如说咱们执行一个价格

6.5

因为这个价格是用长整性表示

所以实际进度要做100的除数

也就是6.5的价格

然后是成交量

Intent Volume

成交量咱们给它100股

接着换的就是股票ID

Intent Stock ID

咱们就选取第一支股票

接着就是委托类型

Intent Type51

0是代表是下单

1呢是代表先加单

为了便于接口的调试和跟踪呢

咱们将参数信息打印出来

Sysout

Send

Paste

Order

Enemies

Sysout

输出呢它的方向

这里咱们快速实现Copy一下

然后是CusePrice

Volume

Stock ID

下面是Type

接着就是实现下单

消息的组装

接着就是实现消息的组装和发送

首先咱们要去构造头部消息

Stock

Add

Rotate

Stock Add

Stock

Add Rotate

New Builder

Set Seconds ID

将上面所进行的Seconds ID加入进去

注意这个采用一个支增长

Set

Paste

Type

Stock

Add Roto

Stock Add Roto

给它一个请求类型

标识它的请求类型

Stock Add Roto

Paste Order

Mute

进行构建

Paste Order

接着咱们要去构造

订单消息

Paste

Order Date

Paste Order Date

New Builder

要设置它的参数信息

一个是Detection

Set Excuse Price

Set它的

请求数量

Volume

还设置它的股票ID

Stock ID

下面的话设置它的Retail Type

最后

要用Build进行构建

接着咱们就要组装

请求

消息

数据包

Stock

Message

Stock Message

Build

要将头部信息设置进去

Stock Add

还有设置呢

构造的订单信息

Paste Order Date

Order Date

最后呢要用Build的方法

进行构建

消息组装完成之后

咱们就要将消息发送至服务端

再用咱们上面所封装的

消息发送接口

Stock Message

在这里呢咱们就完成了

客户端的

下单数据接口的组装

以及呢它的发送处理逻辑

好

那这一讲呢咱们就先讲到这里

我们下期再见

拜拜

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是一节关于使用 Netty 框架构建股票交易代理（Stock Proxy）系统的实战教学。课程主要围绕客户端（Client）和业务处理（Business）两个核心组件展开，演示了如何通过 Netty 的 `ChannelHandler` 机制来处理 WebSocket 连接、接收服务端发送的 Protobuf 业务消息，并构造和发送新的业务消息（如下单请求）。视频通过 IntelliJ IDEA 的代码编辑器进行实时演示，重点讲解了 `ClientBoundHandler` 和 `BusinessHandler` 两个类的实现细节，包括消息的接收、解析、构造和发送流程，以及如何使用 Protobuf 的 `Builder` 模式来构建消息体。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:10**：课程开场，展示项目结构和 `ClientBoundHandler` 类的代码，介绍其主要功能是处理服务端发送的消息。
*   **00:10 - 00:25**：讲解 `ClientBoundHandler` 中的 `recvProtocols` 方法，演示如何接收并打印服务端发送的 `BinaryWebSocketFrame`、`PongWebSocketFrame` 和 `CloseWebSocketFrame`。
*   **00:25 - 00:40**：聚焦于 `recvProtobufMsg` 方法，演示如何将接收到的字节流解析为 Protobuf 消息 `StockHeadProto.RequestType`，并打印其内容。
*   **00:40 - 00:55**：讲解 `channelRead0` 方法，演示如何处理 HTTP 协议握手，以及如何处理 `FullHttpResponse`。
*   **00:55 - 01:10**：展示 `ClientBoundHandler` 类中定义的 `ChannelPromise handshakeFuture` 变量，用于管理握手过程。
*   **01:10 - 01:25**：切换到 `BusinessHandler` 类，介绍其作用是处理业务消息的发送。
*   **01:25 - 01:40**：讲解 `BusinessHandler` 的构造函数和 `sendMsg` 方法，演示如何通过 `Channel` 发送消息。
*   **01:40 - 01:55**：演示如何使用 `StockHeadProto.RequestType` 枚举和 `StockHeadProto.StockHead.Builder` 来构造一个下单请求。
*   **01:55 - 02:10**：展示如何使用 `PlaceOrderData.Builder` 构造具体的下单数据，并最终构建 `StockMessage` 消息体。
*   **02:10 - 02:25**：演示如何调用 `sendMsg` 方法发送构造好的 `StockMessage`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**：
    *   **`ClientBoundHandler` 类**：
        ```java
        // 接收服务端发送的Protobuf业务消息，将业务消息打印出来
        @Override
        private void recvProtobufMsg(ResponseMessage parseFrom) {
            System.out.println("== status: " + head.status);
            System.out.println("== direct: " + direct);
            System.out.println("== execPrice: " + execPrice);
            System.out.println("== volume: " + volume);
            System.out.println("== stockId: " + stockId);
            System.out.println("== type: " + type);
        }
        ```
        ```java
        // 处理WebSocket帧
        if (frame instanceof BinaryWebSocketFrame) {
            System.out.println("receive BinaryWebSocketFrame");
        } else if (frame instanceof PongWebSocketFrame) {
            System.out.println("receive PongWebSocketFrame");
        } else if (frame instanceof CloseWebSocketFrame) {
            System.out.println("receive CloseWebSocketFrame");
            ch.close();
        }
        ```
        ```java
        // 处理HTTP握手
        if (this.handshaker.isHandshakeComplete()) {
            this.handshaker.finishHandshake(ch, response);
            this.handshakeFuture.setSuccess();
        } else if (msg instanceof FullHttpResponse) {
            throw new IllegalStateException(String.format("Unexpected FullHttpResponse, status: %s", ((FullHttpResponse) msg).status()));
        }
        ```
    *   **`BusinessHandler` 类**：
        ```java
        // 构造下单消息
        StockHeadProto.StockHead.Builder headBuilder = StockHeadProto.StockHead.newBuilder();
        headBuilder.setSeqId(seqId++).setRequestType(StockHeadProto.RequestType.PLACE_ORDER);
        PlaceOrderData.Builder orderDataBuilder = PlaceOrderData.newBuilder();
        orderDataBuilder.setDirection(direct).setExecPrice(execPrice).setExecVolume(volume).setStockId(stockId).setType(type);
        StockMessage stockMessage = StockMessage.newBuilder().setStockHead(headBuilder.build()).setPlaceOrderData(orderDataBuilder.build()).build();
        ```
        ```java
        // 发送消息
        private void sendMsg(Message msg) {
            if (null == ctx || null == msg || !ctx.isWritable()) {
                return;
            }
            ctx.writeAndFlush(msg);
        }
        ```

*   **关键概念**：
    *   **Netty `ChannelHandler`**：用于处理网络事件和数据。
    *   **Protobuf**：用于定义和序列化消息结构。
    *   **`Builder` 模式**：用于构建 Protobuf 消息。
    *   **`ChannelPromise`**：用于异步处理操作结果。
    *   **`StockHeadProto.RequestType`**：定义了业务消息的类型，如 `PLACE_ORDER`。
    *   **`StockMessage`**：包含 `StockHead` 和 `PlaceOrderData` 的完整消息体。

---

### 4) 关键场景与演示描述

*   **场景一：客户端消息接收与解析**
    *   **演示**：在 `ClientBoundHandler` 中，通过 `recvProtobufMsg` 方法接收服务端发送的 Protobuf 消息。演示了如何使用 `parseFrom` 方法将字节流解析为 `StockHeadProto.RequestType` 对象，并打印其字段值（如 `status`, `direct`, `execPrice` 等）。
*   **场景二：WebSocket 帧处理**
    *   **演示**：在 `ClientBoundHandler` 中，通过 `recvProtocols` 方法处理不同类型的 WebSocket 帧。演示了如何判断帧类型并打印日志，例如 `receive BinaryWebSocketFrame`、`receive PongWebSocketFrame`。
*   **场景三：HTTP 握手处理**
    *   **演示**：在 `ClientBoundHandler` 的 `channelRead0` 方法中，演示了如何处理 HTTP 握手。当握手完成时，调用 `finishHandshake` 方法并设置 `handshakeFuture` 为成功状态；当收到 `FullHttpResponse` 时，抛出异常。
*   **场景四：业务消息构造与发送**
    *   **演示**：在 `BusinessHandler` 中，演示了如何构造一个下单请求。首先使用 `StockHeadProto.StockHead.Builder` 设置消息头，然后使用 `PlaceOrderData.Builder` 设置具体的下单数据（如价格、数量、股票ID），最后使用 `StockMessage.newBuilder()` 将两者组合成一个完整的 `StockMessage`。
    *   **演示**：通过 `sendMsg` 方法将构造好的 `StockMessage` 发送到服务端，该方法会检查通道是否可写，然后调用 `ctx.writeAndFlush(msg)` 发送消息。
*   **场景五：项目结构与依赖管理**
    *   **演示**：展示了项目结构，包括 `ClientBoundHandler`、`BusinessHandler` 等核心类，以及 `pom.xml` 文件中的依赖项，如 `netty-all`、`protobuf-java` 等。演示了如何在 IntelliJ IDEA 中使用 Maven 管理项目依赖。
