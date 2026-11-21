# 06-Netty使用-演示与验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始对工程进行演示

做个启动和验证

那之前已经实现了服务端和客户端工程

对不对

那我们就来逐一启动一下

首先咱们去启动serve端

serve端的话

是在netbloodway的serve这个类里面进行了启动

通过这个论方法

它会去创建serve对象

然后调用它的long serve方法启动整个服务

那咱们就来启动一下

启动完服务之后

我们就可以启动客户端

然后注意观测他们的一个输出日志

这个是serve端的启动

在这里已经打印出日志

说明整个服务它是启动成功的

接下来咱们就来启动客户端

客户端的路口是在netclient的serve下面

同样我们也要做一个启动

在这里面的话

还没有实现论方法

对不对

论方法的话

我们来在这里补充一下

跟serve端的启动也是一样的

在这里它要注入IP以及port传输

指定服务的连接信息

好

那咱们启动一下

整个工程演示的话

我们是要做一个双向的通讯

这个双向通讯就是

互相去发送一个消息

然后看彼此能否正常接收成功

好

那么客户端也已经启动完成

对不对

咱们看一下它的日志输出情况

在这里它打印出来客户端所发送过来的连接信息

这个是客户端所发送的

大家可以在代码当中查看到

客户端连接成功之后

它会去发送一个消息

到客户端所发起的信息

来连接信息

那么客户端接收到之后

就将它直接打印出来

好

那么去发送一个消息

做个测试

比如说我是客户端

好

发送

那么看下服务端

服务端的话

这不是接收成功了

接收到了客户端所发送来的消息

那么服务端也可以发送一个消息

说我是服务端

点击回车

确认

客户端没有接收成功

对不对

我们要重新发送一下

服务端

好

这个时候咱们再看一下

客户端是不是接收成功了

对不对

因为客户端在这里

它要发送消息

发送消息的话

它是要从终端接收到消息

对不对

刚才的话

如果是你是直接敲击回车

没有任何数据

在这里它是无法去下发成功的

所以我们每条数据

要去下发的时候

就是直接输入完

然后再确定回车

再发现

服务端

对不对

重新发送

然后就确定回车

一定要有数据

不能直接按回车

好

我们看一下客户端

是不是

客户端能够正常接收到服务端的消息

那么我们再随便发送数据

服务端同样也是能够接收到

这样咱们就实现了一个

客户端跟服务端的简易通讯

彼此都能够正常收发消息

这样我们也是实现了整个

内体服务功能的基层了

好

我们现在就来看看

我们的测试验证

好

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是“交易平台 - Day 5”系列课程中关于“Netty 使用”的第 3.5 节“工程演示”。课程通过一个完整的、可运行的 Netty 服务端与客户端示例，演示了如何使用 Netty 构建一个简单的 TCP 通信程序。演示内容包括：服务端的启动、客户端的连接、双向消息发送与接收，以及在 `ChannelHandler` 中处理事件（如 `channelActive`、`channelRead`、`exceptionCaught`）的完整流程。整个过程在 IntelliJ IDEA 开发环境中进行，通过控制台日志和简单的文本界面验证了通信的正确性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，展示课程大纲，当前章节为“3.5 工程演示”。
*   **00:00:05 - 00:00:15**: 展示服务端 `NettyProviderServer` 的 `main` 方法，用于启动服务。
*   **00:00:15 - 00:00:30**: 展示服务端 `runServer` 方法的核心代码，包括创建 `NioEventLoopGroup`、绑定端口、处理客户端连接和优雅关闭。
*   **00:00:30 - 00:00:45**: 展示客户端 `NettyClientServer` 的 `main` 方法，用于启动客户端并连接服务端。
*   **00:00:45 - 00:01:00**: 展示客户端 `runServer` 方法，创建 `Bootstrap`、连接服务端、发送消息。
*   **00:01:00 - 00:01:15**: 展示 `NettyClientHandler` 类，用于处理客户端的 `channelActive` 和 `channelRead` 事件。
*   **00:01:15 - 00:01:30**: 展示 `NettyProviderServer` 中的 `NettyServerHandler` 类，用于处理服务端的 `channelRead` 事件。
*   **00:01:30 - 00:01:45**: 演示客户端连接服务端，发送消息“我是客户端client”。
*   **00:01:45 - 00:02:00**: 演示服务端接收消息并回复“我是服务端server”。
*   **00:02:00 - 00:02:15**: 展示客户端接收服务端回复的消息。
*   **00:02:15 - 00:02:30**: 总结，指出服务端和客户端能够正常收发消息，演示成功。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文本内容

*   **课程大纲**：左侧导航栏清晰列出了课程结构，包括“目标”、“步骤”、“实现”、“工程设计”、“工程结构”、“服务端工程”、“客户端工程”、“工程演示”和“总结”。
*   **关键注释**：
    *   `// 服务端口`
    *   `// 定义时间的BOSS监听组`
    *   `// 定义Worker，用于处理已经接收的连接`
    *   `// 实现Netty的优雅关闭`
    *   `// 客户端发送连接请求`
    *   `// 客户端发送数据`
    *   `// 服务端接收消息`
    *   `// 服务端发送消息`
    *   `// 从结果可以看到，服务端和客户端均能正常收发相互之间消息。`

#### 代码关键内容

*   **服务端 `NettyProviderServer` 类**：
    *   **构造函数**：`public NettyProviderServer(int port) { this.port = port; }`
    *   **启动方法 `runServer()`**：
        ```java
        public void runServer() throws Exception {
            EventLoopGroup bossGroup = new NioEventLoopGroup();
            EventLoopGroup workGroup = new NioEventLoopGroup();
            try {
                ServerBootstrap b = new ServerBootstrap();
                b.group(bossGroup, workGroup)
                 .channel(NioServerSocketChannel.class)
                 .option(ChannelOption.SO_BACKLOG, 1024)
                 .childOption(ChannelOption.SO_KEEPALIVE, true)
                 .childHandler(new ChannelInitializer<SocketChannel>() {
                     @Override
                     public void initChannel(SocketChannel ch) throws Exception {
                         ch.pipeline().addLast(new NettyServerHandler());
                     }
                 });
                ChannelFuture cf = b.bind(port).sync();
                System.out.println("服务端启动，监听端口: " + port);
                cf.channel().closeFuture().sync();
            } finally {
                bossGroup.shutdownGracefully();
                workGroup.shutdownGracefully();
            }
        }
        ```
    *   **主方法 `main()`**：
        ```java
        public static void main(String[] args) throws Exception {
            new NettyProviderServer(9911).runServer();
        }
        ```

*   **客户端 `NettyClientServer` 类**：
    *   **构造函数**：`public NettyClientServer(String ip, int port) { this.ip = ip; this.port = port; }`
    *   **启动方法 `runServer()`**：
        ```java
        public void runServer() throws Exception {
            EventLoopGroup group = new NioEventLoopGroup();
            try {
                Bootstrap b = new Bootstrap();
                b.group(group)
                 .channel(NioSocketChannel.class)
                 .option(ChannelOption.SO_KEEPALIVE, true)
                 .handler(new ChannelInitializer<SocketChannel>() {
                     @Override
                     public void initChannel(SocketChannel ch) throws Exception {
                         ch.pipeline().addLast(new NettyClientHandler());
                     }
                 });
                ChannelFuture cf = b.connect(ip, port).sync();
                Channel channel = cf.channel();
                String reqStr = "客户端发起连接请求";
                channel.writeAndFlush(reqStr);
                channel.closeFuture().sync();
            } finally {
                group.shutdownGracefully();
            }
        }
        ```
    *   **主方法 `main()`**：
        ```java
        public static void main(String[] args) throws Exception {
            new NettyClientServer("127.0.0.1", 9911).runServer();
        }
        ```

*   **服务端处理器 `NettyServerHandler` 类**：
    *   **`channelRead` 方法**：
        ```java
        @Override
        public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
            String message = (String) msg;
            System.out.println("server--收到消息： " + message);
            ctx.writeAndFlush("我是服务端server");
        }
        ```

*   **客户端处理器 `NettyClientHandler` 类**：
    *   **`channelActive` 方法**：
        ```java
        @Override
        public void channelActive(ChannelHandlerContext ctx) throws Exception {
            super.channelActive(ctx);
            serverChannel = ctx.channel();
        }
        ```
    *   **`channelRead` 方法**：
        ```java
        @Override
        public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
            String message = (String) msg;
            System.out.println("client--收到消息： " + message);
        }
        ```
    *   **`exceptionCaught` 方法**：
        ```java
        @Override
        public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
            System.err.println("client 读取数据出现异常");
            cause.printStackTrace();
            ctx.close();
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：服务端启动**
    *   **描述**：讲师在 IntelliJ IDEA 中运行 `NettyProviderServer` 的 `main` 方法。控制台输出显示服务端已成功绑定到端口 `9911`，并进入等待客户端连接的状态。
    *   **关键日志**：
        ```
        Connected to the target VM, address: '127.0.0.1:5760', transport: 'socket'
        server 启动
        ```

*   **场景二：客户端连接与通信**
    *   **描述**：讲师运行 `NettyClientServer` 的 `main` 方法，客户端尝试连接服务端。控制台日志显示客户端成功连接并发送了消息“客户端发起连接请求”。
    *   **关键日志**：
        ```
        server--收到消息： 客户端发起连接请求
        server--收到消息： 我是客户端client
        ```

*   **场景三：双向消息收发**
    *   **描述**：服务端在收到客户端消息后，通过 `channelRead` 方法处理，并调用 `writeAndFlush` 发送回复消息“我是服务端server”。客户端在收到回复后，控制台输出“client--收到消息： 我是服务端server”。
    *   **
