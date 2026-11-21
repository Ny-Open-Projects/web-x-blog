# 15-简易下单功能-Netty数据处理器与启动配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

咱们接着去实现自定义数据的配收处理器

再讲咱们完成了初始化的设置

实现了Netit的集成配置

以及WebSocket的支持

咱们来看一下数据处理器主要实现哪些功能

以及该如何去做对应的实现

咱们回到工程当中

打开Handler

添加对应的读解支持

作为一个Compound的主件

然后添加SharedBot的支持

SharedBot的意思是多个Channel能够安全的共享

不会产生现成安全性的问题

因为咱们知道代理服务作为服务端会揭露不同的终端

每个终端会产生一个Channel

这样即使多个Channel并发使用的话

也不会产生安全性的问题

所以这个是SharedBot读解的作用

接下来咱们将需要用到的属性注入进来

将Splint的现成功能

现成词加入进来

Task Discuter

Autowide读解

添加注释

这个是Splint的现成词

现成词组件

咱们还要添加之前所封装的处理器工厂

Stalker, Processor, Factory

加上Autowide读解

添加注释

业务处理器的工厂

然后咱们还要去添加一个Channel Group

这个Channel Group呢就是使用的主件

收集所有客户端和服务端所建立的Channel

就有点类似于咱们ATB传输的Session作用

服务器是要记录所有的Session

那么同样的

作为Socket的服务端

它要记录所有的Channel通道

这样才能实现消息的正常下发和交互

因为还有其他地方会使用到

在这里咱们就升为Public

静态的方式

Channel Group

采用Default Channel Group

Global

Event

Discute

通过NetEase

去创建一个

默认的Channel管理组

负责客户端的Channel

连接通道的管理

这个大家不用担心它的现成安全

NetEase已经帮咱们去实现了它的现成安全的控制

接下来咱们就去实现

接收客户端数据的处理逻辑

这里是接收处理

客户端

所发送的数据

为了提升处理性能

在这里咱们采用异图方式处理

Task

Discute

Discute方法

为了避免异常产生的中断

在这里

做一个ShareCache捕获

将错误信息反映出来

这里面的处理逻辑也比较简单

它是获取指定的

业务处理器

处理

业务请求数据

通过咱们的工厂

拿取对应的处理器

Generate Stock Processor

根据你传递过来的

使用类型

Get Stock Head

拿到

Request Type

然后调用

Processor

Request方法

传递参数是Channel Handle

Context

还有Stock Message

这个Stock Message

就是通过ProBuffer解码器

解码之后转换成的具体对象

下面是业务处理器的处理方法

我们先来看看

这个是处理业务异常的处理

那咱们就从讲义当中

将相关的代码拷贝进来

这里是处理业务异常

这个是处理系统异常

出现业务异常之后

先将错误日志打印出来

然后再去包装它的返回消息

在这里包装的就是对应的错误消息

可以看到

下面会将对应的错误异常码

返回给客户端

然后这个是系统异常

在这里面呢

我们就将这些消息

但由于它是系统异常

没有具体的错误码

所以呢我们就将异常

提示信息包装返回出去

消息包装完成之后呢

就通过channel通道进行

就通过channel通道

将数据发送给客户端

然后这里呢

还有一个general stockhead的方法

咱们也做一个实现

这个是生成返回的头部信息

传递的参数是stockhead

以及具体的处理状态

好

消息接受的处理逻辑呢

咱们就已经完成

接着咱们还加上

通道关闭的处理逻辑

在下面呢

alert insert

去重写

两个方法

一个是handle removed

咱们找一下

这个是handle removed

还有一个是exception code

将这两个方法呢

选中点击ok

handle removed

是通道

如果是被移除之后

那么在这里呢他会调用

相应的方法

我们加上对应的处理逻辑

将失效的通道呢

进行移除

然后将通道呢

关闭

可恶此方法

这里channel是咱们采用的是channel group

那么channel group呢

他会自动调用处理

可以不用写

当然如果你加上了也没有问题

然后呢是主动

关闭

释放资源

上面这个呢是出现

异常的时候

要做的处理逻辑

这里咱们呢

加上

异常日志

exception on socket

反映出现实站信息

然后呢要将通道进行关闭

这个可能会出现一些位置异常

那么只要出现异常呢

说明这个通道就已经失效

没法正常使用

所以咱们呢要将这个通道的上下文

进行关闭

好那咱们呢

再回到讲义当中

在这里咱们对整个逻辑呢

再做一个回顾

channel group的方法

它是接收

发送的数据

通过propert研码器呢

会自动转换成为

stock message对象

在这里咱们可以看到

这个stock message对象呢

就是通过propert的

研码器呢

将它进行了相应的转换

为了提升处理效率呢

咱们增加了异步现成词

task isq的进行处理

因为这些接口的调用呢

咱们不需要保证它的严格顺序

所以可以加入现成词了

如果需要保证严格的顺序呢

在这里是不能够加入现成词了

这一点呢大家要理解清楚

在这里咱们先不做健全处理

在下面章节当中呢

还会做具体讲解

我们先去实现它的处理逻辑

通过工厂方法

获取指定的业务处理器

接收呢处理的数据

针对业务异常

或者是系统异常

要做不同的消息提示封装

刚才呢也做了讲解介绍

在这里咱们采用了channel group

它是负责客户端channel连接通道的管理

它是现成安全的

连接中断的时候呢

会自动进行释放

作为常连接

它是负责消息的推送和网播

所以咱们呢

将它声名为public

静态类型

如果要实现消息的推送呢

都可以通过channel group

做对应的实现

再往下面呢

咱们就要去实现

neti的启动配置

这里呢是通过stock proxy application

这个类进行的启动

这块代码呢

咱们就copy过来

再做详细讲解

在这里做一个替换

将这些包呢

导入进来

这个是neti包下面的

这些都是neti包下面的

不要导入成GRPC下面的包

这个启动类大家可以看到

在这里面呢

它是重写了乱方法

咱们将这个包呢

也导入进去

在Splitbook的服务启动完成之后呢

它会去调用application

当了接口的乱方法

大家要注意

Splitbook的应用服务

和socket的服务呢

它是分隔出来的

它们监听的是不同端口

这一段呢就是启动socket服务的代码

首先它创建了一个boss

还有它的一个work线程

然后通过soulboot进行启动

在这里呢

它将达门之前所定义的

neti服务配置呢

设置进去

然后进行启动

这样它就会读取

咱们在这里所定义的neti服务配置

以及websocket的配置

就实现了一个websocket的服务

最后finally当中呢

要实现优雅的关闭

一个是boss

另外一个呢

是work

好

服务启动配置完成之后呢

最后咱们还在配置文件当中加入相应的配置

在咱们的工程配置当中

去加入neti的服务配置

这里呢主要就是两个配置信息

一个是服务的端口

一个是否开启调试日志

在这里呢

咱们就完成了

neti的启动配置

以及呢

neti的自定义数据处理器的实现

那这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“bulls-stock-proxy”的Java项目，重点讲解了如何使用Netty框架构建一个股票行情代理服务的服务器端。核心内容是实现一个 `StockProxyServerHandler` 类，该类继承自 `SimpleChannelInboundHandler<StockMessage>`，用于处理客户端通过WebSocket发送的股票行情请求。视频详细演示了如何在Netty的ChannelHandler中，通过异步线程池（`@Autowired TaskExecutor`）来处理业务逻辑，将请求分发给不同的处理器（`StockProcessor`），并处理异常情况，最后将响应写回客户端。整个过程展示了如何将Netty的网络通信能力与Spring框架的业务逻辑解耦和集成。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：视频开始，展示项目结构和 `StockProxyServerHandler` 类的初始代码，介绍其作为Netty服务器处理器的角色。
*   **00:05 - 00:15**：讲解 `@Component`、`@Sharable`、`@Log4j2` 等Spring注解的作用，并引入 `@Autowired private TaskExecutor taskExecutor;` 用于异步处理。
*   **00:15 - 00:30**：演示 `channelRead0` 方法的实现，展示如何使用 `taskExecutor.execute(() -> { ... })` 将业务处理逻辑提交到异步线程池。
*   **00:30 - 00:45**：在异步线程中，通过 `stockProcessorFactory.generateStockProcessor(...)` 获取具体的业务处理器，并调用其 `.processRequest(...)` 方法。
*   **00:45 - 01:00**：演示异常处理逻辑，包括 `ComponentException`（业务异常）和 `Exception`（系统异常），并展示如何构建 `ResponseMessage` 返回给客户端。
*   **01:00 - 01:15**：讲解 `handlerRemoved` 方法，用于在客户端断开连接时清理资源。
*   **01:15 - 01:30**：展示 `StockProxyApplication` 的 `main` 方法，演示如何启动Netty服务，创建 `EventLoopGroup` 和 `ServerBootstrap`。
*   **01:30 - 01:45**：讲解 `StockProxyServerInitializer` 类，展示如何为Netty管道添加 `MessageToMessageEncoder` 用于WebSocket协议的编码。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **关键代码片段**

*   **`StockProxyServerHandler` 类定义**：
    ```java
    @Component
    @Sharable
    @Log4j2
    public class StockProxyServerHandler extends SimpleChannelInboundHandler<StockMessage> {
        @Autowired
        private TaskExecutor taskExecutor;
    }
    ```

*   **`channelRead0` 方法核心逻辑**：
    ```java
    @Override
    protected void channelRead0(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage) throws Exception {
        taskExecutor.execute(() -> {
            try {
                // 获取指定的业务处理器，处理业务请求数据
                stockProcessorFactory.generateStockProcessor(stockMessage.getStockHead().getRequestType())
                    .processRequest(channelHandlerContext, stockMessage);
            } catch (ComponentException e) {
                // 业务异常
                log.error(e.getMessage(), e);
                StockHeadProto.StockHead stockHead = generateStockHead(stockMessage.getStockHead(), GlobalConstants.STATUS_ERROR);
                ResponseMessage responseMessage = ResponseMessage.newBuilder()
                    .setStockHead(stockHead)
                    .setMessage(e.getErrorCodeEnum().getMessage())
                    .build();
                channelHandlerContext.writeAndFlush(responseMessage);
            } catch (Exception e) {
                // 系统异常
                log.error(e.getMessage(), e);
                StockHeadProto.StockHead stockHead = generateStockHead(stockMessage.getStockHead(), GlobalConstants.STATUS_ERROR);
                ResponseMessage responseMessage = ResponseMessage.newBuilder()
                    .setStockHead(stockHead)
                    .setMessage(e.getErrorCodeEnum().getMessage())
                    .build();
                channelHandlerContext.writeAndFlush(responseMessage);
            }
        });
    }
    ```

*   **`handlerRemoved` 方法**：
    ```java
    @Override
    public void handlerRemoved(ChannelHandlerContext ctx) throws Exception {
        channels.remove(ctx.channel());
    }
    ```

*   **`StockProxyApplication` 启动类**：
    ```java
    public class StockProxyApplication {
        public static void main(String[] args) {
            SpringApplication.run(StockProxyApplication.class, args);
        }

        @Override
        public void run(ApplicationArguments args) throws Exception {
            // 启动网络服务器
            EventLoopGroup boss = new NioEventLoopGroup();
            ServerBootstrap boot = new ServerBootstrap();
            boot.group(boss, worker).channel(NioServerSocketChannel.class).childHandler(new StockProxyServerInitializer());
            ChannelFuture f = boot.bind(nettyPort).sync();
            log.info("Stock Quote Proxy Netty Server Start!");
        }
    }
    ```

#### **关键概念与结构**

*   **架构模式**：采用“代理服务 + Netty + WebSocket + Spring” 的架构。
*   **设计模式**：使用工厂模式（`StockProcessorFactory`）来创建不同的业务处理器。
*   **异步处理**：通过 `TaskExecutor` 将耗时的业务处理逻辑从网络I/O线程中分离，提高服务器吞吐量。
*   **异常处理**：区分业务异常和系统异常，并统一返回 `ResponseMessage` 给客户端。
*   **Netty管道**：通过 `StockProxyServerInitializer` 为管道添加编码器（`MessageToMessageEncoder`）。

---

### 4) 关键场景与演示描述

*   **场景一：初始化与注解配置**
    *   **描述**：视频首先展示了 `StockProxyServerHandler` 类的代码，强调其使用了 `@Component` 注解使其成为Spring Bean，并使用 `@Sharable` 注解表明该处理器可以被多个Channel共享，使用 `@Log4j2` 注解引入日志功能。同时，通过 `@Autowired` 注解注入了一个 `TaskExecutor`，用于后续的异步处理。

*   **场景二：异步处理业务逻辑**
    *   **描述**：在 `channelRead0` 方法中，演示了如何将网络事件（客户端发送消息）的处理委托给异步线程池。通过 `taskExecutor.execute(() -> { ... })`，将业务处理代码放入一个独立的线程中执行，避免阻塞网络线程。

*   **场景三：业务处理器分发与异常处理**
    *   **描述**：在异步线程中，通过 `stockProcessorFactory.generateStockProcessor(...)` 获取具体的处理器实例，并调用其 `processRequest` 方法。视频详细演示了如何捕获 `ComponentException`（业务异常）和 `Exception`（系统异常），并根据异常类型构建不同的响应消息，最终通过 `channelHandlerContext.writeAndFlush(responseMessage)` 将响应写回客户端。

*   **场景四：Netty服务启动**
    *   **描述**：视频展示了 `StockProxyApplication` 的 `main` 方法，演示了如何通过 `SpringApplication.run(...)` 启动Spring应用，并在 `run` 方法中创建 `EventLoopGroup` 和 `ServerBootstrap`，绑定端口并启动Netty服务。

*   **场景五：WebSocket协议编码**
    *   **描述**：在 `StockProxyServerInitializer` 类中，演示了如何为Netty管道添加 `MessageToMessageEncoder`，用于将 `StockMessage` 对象编码为字节流，以便通过WebSocket协议传输给客户端。代码中展示了如何根据消息类型（如 `MessageLite` 或 `MessageLite.Builder`）进行不同的编码处理。

---

以上是根据视频画面进行的结构化技术分析，旨在清晰地呈现视频中的核心知识点和实现细节。
