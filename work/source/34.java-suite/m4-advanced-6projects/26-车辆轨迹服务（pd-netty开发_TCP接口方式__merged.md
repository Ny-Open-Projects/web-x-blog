# 26-车辆轨迹服务（pd-netty开发_TCP接口方式_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那接下来呢

咱们继续来看我们TCP接口这种开发方式啊

那么刚才呢

咱们是把这个neti server呢

已经写好了对吧

我们是从讲义上直接复制过来的

因为也都是一些模板化的代码

那么现在呢

我们就需要来编写这个类

你看这个类叫做neti server handler

对吧

它是具体来处理我们这个网络IO事件的

比如说什么呢

比如说我这个服务端跟客户端连接上之后呢

我想从这个客户端来读取一些信息

一些数据

那么读取这其实就是一个事件

对吧

那么我读取到这个数据之后

应该做什么处理

这个时候呢

我们就需要在这个类里面去写

还有就是什么呢

当我这个数据读完之后

应该做什么处理

也需要在这里面来写

还有就是什么呢

如果读取过程当中出现了异常信息

对吧

那么应该怎么处理

也就是这些事

这些东西呢

都需要写到我们当前这个类里面来

好

那接下来呢

我们就把这个类呢

也把它考过来

大概来读一下

就是Netty Server Handler

把这个类呢来创建一下

咱们就放在service包里面就可以了

放在这service包里面

好

然后呢

我们这个类的话呢

按照Netty它的要求啊

就是什么呢

这种处理类必须要去干什么呢

继承Netty给我们提供的一个副类

这个副类呢

是什么呢

就是这个啊

叫做Channel Inbound Handler Adapter

需要去继承这么一个副类

然后呢

我们可以看到在副类里边啊

咱们进来看一下

其实有一些方法对吧

你看这是什么Channel Registered

这个就是什么通道注册之后

是不是会执行这个方法

对吧

然后呢

这是解除注册的时候

还有什么激活的时候

还有什么Channel Rate

这是不是就是读取到我们客户端的消息的时候

是不是会执行这个方法

然后呢

这个是读取完之后

是不是会执行这个方法

还有一些什么呢

什么Exception Cuts

对吧

这个就是什么呢

读取过程当中发生了异常

那么它就会执行这个方法

所以全都是这种事件驱动的

那也就是说

我们需要去覆盖这个副类的几个方法

因为呢

你直接使用副类这个方法呢

往往是满足不了要求的

因为我们读完之后

比如说我想把我们这个读取到的信息

把它发送到卡布卡

那副类不可能给我们去实现这样的效果

对吧

所以说呢

我们需要去覆盖它的这个方法

你看

这不是Channel Rate的吗

我这是不是加了Override

对吧

去覆盖副类的这个方法

这个呢

就是当我们读取到这个信息之后

那么NetEase框架呢

就会自动的帮我们去调这个方法

所以这些呢

其实都属于一些什么事件驱动

它的特点

对吧

那么不像我们以前编程

我们是Controller调Service

Service调DAO

那么都是我们自己去调这些代码

而现在呢

我们只需要把这些方法给它实现出来

具体什么时候该调呢

它是由事件来驱动的

当这个事件发生的时候

那么框架呢

就会主动给我们去调这个方法

所以并不需要我们自己去调这个方法

这是跟我们以前编程

可能不太一样的一些地方

那么这个方法呢

刚才提到了是什么呢

当我们通过这个通道

读取到这个客户端发送过来的数据的时候

这个方法将会被调用

将会被调用

好

那你看这个方法呢

给我们传过来两个参数

对吧

一个是这个CTX

这其实是一个上下文对象

对吧

还有一个就是Message

这就是我们读取过来的

这个信息

对吧

首先呢

把它这个向下强转一下

然后呢

我们调用这个方法

getRequestBody

这其实呢

就是把我们这个对象呢

给它转成String

具体怎么转的呢

这咱们下面是不是定义了这么一个方法吗

对吧

其实呢

就是new了一个by的数组

最后呢

把它newString

然后呢

通过UCF8编码

然后呢

相当于就是把这个对象

把这个类型的对象呢

给它转了一种格式

转成了String子符串

方便我们处理

好

然后呢

这就是body对吧

然后呢

我们通过这个log

然后再控制台输出一下日志

然后接下来呢

passMessage

因为我们需要把它转成JSON类型

对吧

所以说呢

这个passMessage呢

这个方法

就是把我们原始的这个字符串

给它转成什么呢

转成JSON来返回

好

转成JSON返回

那这样的话就到这了

对吧

到这

然后这块呢

就是我们最核心的

其实就是通过调用我们KafkaCinder

这是前面我们是不是已经实现了

对吧

就是这个类啊

KafkaCinder

那么调用我们这个静态的Send的方法

这样的话呢

就是把它发送到我们这个堆列里面去了

对吧

发送到Kafka堆列

然后把这个信息

这个信息呢

也是转完之后的JSON数据

好

然后最后呢

是不是把这个release

就是把相关的资源是不是去释放一下

就可以了

好

然后呢

这下边这块

这个呢

就是什么呢

当我们这个数据读完之后

那么就会

执行这个方法

就会执行这个方法

这个方法呢

其实就是写一个空的buff来刷新

并刷新写出区域

对吧

然后呢

让他这个并且关闭什么呢

关闭我们这个socket的连接

好

这就是读完之后就会执行这个方法

这个呢

是出一场之后

对吧

出一场之后呢

就把这个什么呢

上页文给它关闭

就可以了

好

所以重点呢

我们看的是这个方法

就是这个channel read对吧

当我们读取到客户端发送过来的数据的时候呢

其实这就相当于呢

相当于什么呢

我们这个司机app

他上报信息对吧

上报完成之后

那么这个时候呢

上报的时候呢

就会执行这个方法

上报完成之后

执行我们刚才看到那个complete的那个方法

然后这块呢

最核心的其实就是把这个消息呢

发到对列里面去

所以整体呢

这就是我们这个具体处理类

还是比较简单的

一会呢

我们可以简单来测试一下

所以你看

我们写完

这个时候呢

我们可以测什么呢

写完这个channel handler了

就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“品达物流TMS项目”的技术课程，主要讲解如何使用 **Netty** 框架开发一个 **TCP 服务器**，用于接收和处理来自车辆终端的报文。课程内容聚焦于 **5.1.2 TCP方式** 的实现，详细演示了如何编写一个 Netty 服务端处理器（`NettyServerHandler`），包括接收原始字节流、解析为字符串、校验数据、发送至 Kafka 队列以及关键的资源释放（`ReferenceCountUtil.release`）和内存管理（`ByteBuf` 的 `resetWriterIndex`）操作。视频最后简要提及了 `pd-druid` 开发，但指出其已在项目中完成，可直接使用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，展示课程大纲，定位到“5.1.2 TCP方式”章节。
*   **00:00:05 - 00:00:15**: 展示 `NettyServer` 服务端的初始化代码，包括 `EventLoopGroup`、`ServerBootstrap` 的配置和绑定端口。
*   **00:00:15 - 00:00:30**: 展示 `NettyServerHandler` 的 `channelRead` 方法，用于处理接收到的 `ByteBuf`。
*   **00:00:30 - 00:00:45**: 详细讲解 `getRequestBody` 方法，用于将 `ByteBuf` 转换为字符串。
*   **00:00:45 - 00:00:55**: 讲解 `parseMessage` 方法，用于解析报文内容，并处理空值情况。
*   **00:00:55 - 00:01:05**: 讲解 `KafkaSender.send` 方法，用于将解析后的消息发送至 Kafka。
*   **00:01:05 - 00:01:15**: 讲解 `try-catch-finally` 块，强调 `ReferenceCountUtil.release` 和 `in.resetWriterIndex()` 的重要性，以防止内存泄漏。
*   **00:01:15 - 00:01:25**: 展示 `parseMessage` 方法的实现细节，包括对 JSON 字符串的处理。
*   **00:01:25 - 00:01:35**: 展示 `channelReadComplete` 和 `exceptionCaught` 方法，用于完成写操作和处理异常。
*   **00:01:35 - 00:01:45**: 展示 `pd-druid` 开发的介绍，说明其已在项目中完成，可直接使用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   课程大纲：`品达物流TMS项目` -> `第7章 车辆轨迹服务开发(pd-netty, pd-druid)` -> `5. 车辆轨迹服务` -> `5.1.2 TCP方式`。
    *   `pd-druid` 开发的介绍：`在初始项目中已经编写完成，直接使用即可。`

*   **代码关键内容**:

    **Netty 服务端初始化 (`NettyServer.java`)**:
    ```java
    public NettyServer() {
        mainGroup = new NioEventLoopGroup();
        subgroup = new NioEventLoopGroup();
        server = new ServerBootstrap();
        server.group(mainGroup, subgroup)
            .option(ChannelOption.SO_BACKLOG, 128)
            .childOption(ChannelOption.SO_KEEPALIVE, true)
            .childHandler(new NettyServerHandler());
    }

    public void start() {
        this.future = server.bind(nettyServer.port);
        log.info("Netty Server 启动完毕!!! 端口：{} ", nettyServer.port);
    }
    ```

    **Netty 服务端处理器 (`NettyServerHandler.java`)**:
    ```java
    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) {
        log.info("ServerHandler.channelRead()");
        ByteBuf in = (ByteBuf) msg;
        try {
            // 接收报文
            String body = getRequestBody(in);
            log.info("报文内容: {}", body);

            // 解析报文
            String message = parseMessage(body);
            if (StringUtils.isBlank(message)) {
                log.info("报文解析失败");
                return;
            }

            // 发送至Kafka队列
            KafkaSender.send(KafkaSender.MSG_TOPIC, message);
        } catch (Exception e) {
            log.error(e.getMessage());
        } finally {
            // 使用完ByteBuf之后，需要主动去释放资源，否则，资源一直在内存中加载，容易造成内存泄漏
            ReferenceCountUtil.release(msg);
            // 把当前的写指针 writerIndex 恢复到之前保存的 markedWriterIndex值
            if (null != in) {
                in.resetWriterIndex();
            }
        }
    }
    ```

    **辅助方法 `getRequestBody`**:
    ```java
    private String getRequestBody(ByteBuf in) throws UnsupportedEncodingException {
        if (in.readableBytes() <= 0) {
            return null;
        }
        byte[] req = new byte[in.readableBytes()];
        in.readBytes(req);
        return new String(req, "UTF-8");
    }
    ```

    **辅助方法 `parseMessage`**:
    ```java
    private String parseMessage(String body) {
        if (StringUtils.isBlank(body)) {
            log.warn("报文内容异常");
            return null;
        }
        String result = JSON.toJSONString(body);
        return result;
    }
    ```

    **异常处理方法**:
    ```java
    @Override
    public void channelReadComplete(ChannelHandlerContext ctx) {
        ctx.writeAndFlush(Unpooled.EMPTY_BUFFER).addListener(ChannelFutureListener.CLOSE);
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {
        ctx.close();
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：服务端初始化与启动**
    *   **描述**: 讲师在 IDE 中展示 `NettyServer` 类的构造函数和 `start` 方法。通过 `ServerBootstrap` 配置 NIO 线程组，并绑定端口。演示了如何将 `NettyServerHandler` 作为 `childHandler` 注册，用于处理每个新连接的 I/O 事件。
    *   **技术点**: `EventLoopGroup`, `ServerBootstrap`, `ChannelFutureListener`, `bind` 方法。

*   **场景二：处理接收到的报文**
    *   **描述**: 讲师聚焦于 `NettyServerHandler` 的 `channelRead` 方法。演示了如何从 `ChannelHandlerContext` 中获取 `ByteBuf` 对象，并通过 `getRequestBody` 方法将其转换为字符串。在控制台日志中打印出接收到的报文内容。
    *   **技术点**: `ByteBuf`, `channelRead`, `getRequestBody`, 日志记录。

*   **场景三：解析与发送**
    *   **描述**: 讲师演示了 `parseMessage` 方法，用于将字符串报文转换为 JSON 格式。如果报文为空，则记录日志并返回。解析成功后，调用 `KafkaSender.send` 方法将消息发送至 Kafka 队列。
    *   **技术点**: `parseMessage`, `JSON.toJSONString`, `KafkaSender.send`, `MSG_TOPIC`。

*   **场景四：资源释放与内存管理**
    *   **描述**: 讲师重点讲解了 `finally` 块中的代码。强调在使用完 `ByteBuf` 后，必须调用 `ReferenceCountUtil.release(msg)` 来释放资源，否则会导致内存泄漏。同时，调用 `in.resetWriterIndex()` 来恢复写指针，确保后续操作的正确性。
    *   **技术点**: `ReferenceCountUtil.release`, `resetWriterIndex`, 内存泄漏预防。

*   **场景五：项目结构与 pd-druid**
    *   **描述**: 视频最后，讲师切换到 PPT 页面，简要介绍了 `pd-druid` 开发。指出该部分已在项目中完成，开发者可以直接使用，无需重复编写代码。
    *   **技术点**: `pd-druid`, 项目结构, 代码复用。
