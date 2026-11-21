# 05-Netty使用-Client客户端实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来呢,咱们就开始实现NetEase的客户端工程。

上一讲呢,咱们去实现了NetEase的服务端,并且呢,对它的主要实现流程呢,做了详细讲解。

那么呢,我们再看一下NetEase Server Handle这一块,它怎么去实现呢?

它是通过继承Channel Import Handle这个适配器,实现了什么方法呢?

去重写了Channel Active,就是连接通道的激活,对不对?

连接通道激活的时候,它要怎么做呢?

它将通道呢,做一个记录,这样呢,它的作用呢,可以去监听所有的客户端连接通道。

那么如果服务端要下发消息呢,就可以从这个Channel List里面呢,将它的客户端的连接通道拿出来,然后呢,下发消息给客户端。

好,这个呢,是Channel Active所要做的事情。

那么,读取数据这一块是怎么做呢?

因为我们刚才讲了,读取数据呢,还有它的一个发送数据呢。

我们都是采用什么?

Stream作为这样一个编码,解码器。

那么呢,在这里,它就不需要对二进制数据呢,做额外的处理。

可以呢,直接将接收到的数据呢,打印出来。

然后呢,这个就是服务端的一个实现处理逻辑。

再往下面呢,是它的异常逻辑的处理。

异常逻辑的处理呢,咱们可以看到,在这里呢,如果是出现了连接通道,数据读取或者是传输方面的异常呢,

它就会进入这个方法。

然后呢,我们会将它连接通道。

我们会将异常信息,它的堆栈呢,打印出来。

最后呢,会关闭它所对应的连接通道。

好,这个呢,就是服务端的Server Handle的具体实现。

那回过头来,咱们来看一下客户端工程这一块是怎么实现呢?

客户端工程呢,整体的实现逻辑跟服务端呢,也基本类似。

它首先呢,要启动一个客户端服务,对不对?

客户端服务呢,主要就是要连接到我们的之前所编写的服务端当中。

然后呢,我们可以看到,它是一个客户端服务。

然后接着的话呢,它也要去实现了客户端的一个Handle。

那客户端Handle呢,跟服务端这个Handle呢,也比较类似,对吧?

都要将数据呢,做对应的处理。

那么Client端呢,将接收到的数据呢,也会打印出来。

好,那么咱们呢,就来具体实现一下。

在Net Demo下面呢,去Live一个Model。

然后点击Next。

好,给服务模块一个名称,叫Net Client。

这个Net Client的话呢,我们将名称调整一下。

点击Finalize。

Finalize。

导入生效。

那么我们先创建对应的包。

包的话呢,叫com.idcast.net.client。

好,创建完成之后呢,咱们就来做具体实现。

在这里呢,首先实现Net的启动服务。

Net Client的启动服务呢,怎么去做呢?

我们将这个Late创建一下。

创建完成之后呢,咱们定义两个属性。

第一个呢,是服务。

服务端的IP。

咱们加个注释。

服务端的IP。

然后呢,再定义一个端口。

LiveIt。

这个呢,是服务端的端口。

好,定义完成之后呢,同样通过构造参数呢,做初始化。

好,构造方法呢,创建两个参数。

一个呢,是IP。

另外呢,一个是Port。

然后呢,将它们注入进来。

this。

点Port。

这个Port的话呢,是Intelligent。

好。

那咱们来看一下,客户端,它怎么去启动,并且呢,和服务端建立连接呢?

我们呢,去定义一个方法。

LiveIt.

WaitLong.

SourceException。

第一个步骤呢,咱们要去定义Boss,先清楚。

对不对?

第二个步骤呢,咱们先把步骤,先捋清楚,对不对?

第二个步骤呢,要定义服务启动类。

好。

第三个步骤呢,跟我们之前服务端的实现一样,要去什么?

定义服务,就是服务的启动参数。

第四个步骤呢,咱们要去启动客户端。

好。

接着的话呢,咱们叫客户端呢,是不是叫发送个数据啊,对不对?

实现客户端数据的发送。

最后一个步骤呢,咱们叫监听呢。

你必须要有一个监听线程,对不对?

通过监听线程,然后呢,将输入的信息发送至服务端。

就是整体的实现步骤。

好,那我们来做个对应实现。

首先的话呢,创建Event.

Loop.

Loop。

在这里呢,是一个Boss.

Loop。

NIOEvent。

好,在这里呢,它并没找到我们的对应的依赖,对吧?

为什么呢?

咱们来看一下,肯定是依赖没加上去。

好,那我们可以看到,Client里面呢,并没有依赖,对不对?

那么,复聚工程呢?

哎,复聚工程也没有。

那什么原因呢?

因为我们之前呢,之前依赖放到服务端了,对不对?

所以呢,我们要把它呢,移出来。

放到哪里呢?

放到我们的复聚工程。

这样呢,我不用在每个模块上面,都去引用这个组件。

好,那它导入声效。

咱们再进去。

这个时候呢,是不是就可以找到了,对吧?

NIOEvent。

Loop,不Loop。

好,在这里面的话呢,创建Boss监定处。

接着的话呢,咱们还得去定义一个启动类。

WoodStrip。

这个呢,是Net下面的包。

BS要等于6。

WoodStrip。

这个下面的包的话呢,不要以路错误。

然后是配置它的参数,对不对?

我们来详细看一下。

这一块呢,是重点。

好。

在这里面呢,将BossGroove注入进来。

这是我们上面所写的。

BossGroove。

然后呢,要给它设置一个Channel。

Channel的话呢,是采用NIO socket的方式。

socketChannel.class。

好。

接着的话呢,咱们要去设置,就是它的参数。

比如说保持常连接,对吧?

这跟我们之前服务端设置呢,也是基本类似的。

Channel。

这里呢,参数是Keypline。

值呢,改为2。

然后点Header。

这个Header的话呢,跟我们之前服务端创建也是一样。

怎么创建呢?

去NIOchannel.initial。

socket的Channel。

然后呢,我们要去实现它的方法,对吧?

initial的Channel。

做一个重写。

这个Channel.initial呢,它是一个。

它是一个。

它是一个。

这个Channel.initial呢,它是一个。

它是一个。

它是一个。

它是一个。

它是一个。

它是一个。

它是一个。

它是一个。

它是一个。

它是一个。

它是一个。

这个Channel.initial呢,它是一个。

它是一个抽象。

抽象类。

在这里面,我们可以看到。

所以,我们要把这部分,沒有实现的方法,都做一个具体实现。

然后是让,我们可以直接 Copies 过来。

快速几天。

这个逻辑步骤呢,跟服务端一样。

首先的话呢是,广大的注册。

对不对?

然后编码和通道的处理。

转码的通道处理。

最后就是要处理来自呢。

这里呢。

这个是处理接收到的请求数据是来自无端的

好

慢慢还继续创建对应的一个类

这个类的话呢

就是下面

net client handle

这个handle呢

是专门处理接收数据的

好

我们先把这个类呢

先创建一下

避免它暴墜

这个呢

是net client

因为你现在是客户端吧

对吧

好

net client handle呢

它要去继承

client in bundle

思维器

将它拷贝过来

client handle

在这里呢

它暴墜了

对吧

那该怎么去处理呢

我们写一下

它用那个

socket channel

点

dit11

好

拍拍了

然后呢

点add last

new

net client

handle

这样呢

就完成客户端的一个

启动的配置参数

那接下来呢

就是启动客户端

在这一块呢

我们就加快一点

客户端的一个启动

对吧

我们在这里呢

拷贝过来

在这里是启动客户端

然后下面的话呢

是客户端的一个出去发送

连接的时候呢

它会发送一个消息

这个消息是什么

客户端发起的连接请求

然后呢

将这个通过圈的管道

输出给服务端

好

最后呢

就是它的一个监听线程

通过这个监听线程呢

它同样会监听了控制台的输入消息

然后呢

将输入的消息呢

发送给服务端

这样呢

就实现了一个简易的双向的通讯

那么client hand这一块呢

怎么去做呢

跟我们之前的服务端的实现

也是基本类似的

咱们将代码引入进来

这个channel呢

导入进来

注意它是net下面的包

导入进来之后呢

同样channel active呢

它在这里会记录什么

跟服务端的一个连接通道

记录这个通道之后呢

呢

如果我客户端其他逻辑方面

要去发送消息的时候呢

就不需要在这里面去发送消息

对不对

它就可以直接拿到这个channel

进行一个消息发送

我们也可以看到

它是一个什么

public的方式

好

再往下面呢

是channel read

也就是在这里呢

是接收到服务端所下发过来的消息

那客户端呢

可以将消息呢

直接打印出来

同样如果是出现异常的时候呢

在这里会有一个异常的消息处理

好

这个呢

就是客户端的handle的

整体的一个实现逻辑

好

那在这里呢

在这一讲呢

咱们就讲解了客户端工程的一个

代码实现

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程是关于 **Netty 框架的客户端与服务端通信实战**。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何创建一个简单的 Netty 服务端（`NettyProviderServer`）和客户端（`NettyClientServer`），并实现双向通信。课程内容聚焦于 Netty 的核心组件，如 `EventLoopGroup`、`ServerBootstrap`、`Bootstrap`、`ChannelPipeline` 和 `ChannelHandler`。讲师通过代码演示，讲解了如何配置服务端监听器、客户端连接、数据编码解码以及消息处理，旨在帮助学习者理解 Netty 的基本工作原理和实际应用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程开场，展示项目结构，介绍本节将实现一个 Netty 服务端和客户端。
*   **00:16 - 00:40**: 讲解服务端代码 `NettyProviderServer`。重点是创建 `EventLoopGroup`（`bossGroup` 和 `workGroup`），并使用 `ServerBootstrap` 进行配置，包括设置 `NioServerSocketChannel`、`SO_BACKLOG` 和 `SO_KEEPALIVE` 等选项。
*   **00:41 - 01:00**: 讲解客户端代码 `NettyClientServer` 的初始化和 `runServer` 方法。创建 `EventLoopGroup` 和 `Bootstrap` 对象。
*   **01:01 - 01:20**: 讲解客户端 `Bootstrap` 的配置，包括设置 `ChannelOption`，如 `SO_BACKLOG` 和 `SO_KEEPALIVE`。
*   **01:21 - 01:40**: 讲解客户端 `ChannelInitializer` 的 `initChannel` 方法，用于向 `ChannelPipeline` 注册处理器，包括 `StringDecoder`、`StringEncoder` 和自定义的 `NettyClientHandler`。
*   **01:41 - 02:00**: 讲解客户端 `NettyClientHandler` 类，用于处理接收到的消息，并打印到控制台。
*   **02:01 - 02:20**: 讲解客户端如何发起连接、发送请求并启动线程进行异步通信。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   课程目标：实现 Netty 服务端和客户端通信。
    *   服务端功能：监听端口，接收并打印客户端消息。
    *   客户端功能：连接服务端，发送消息并接收服务端响应。
    *   代码结构：`NettyProviderServer`、`NettyClientServer`、`NettyServerHandler`、`NettyClientHandler`。

*   **关键代码片段**:

    **服务端 `NettyProviderServer.java`**:
    ```java
    public void runServer() throws Exception {
        // 1. 定义NIO的事件循环组
        EventLoopGroup bossGroup = new NioEventLoopGroup();
        EventLoopGroup workGroup = new NioEventLoopGroup();

        try {
            // 2. 定义NIO的服务启动类
            ServerBootstrap sbs = new ServerBootstrap();
            // 3. 配置NIO服务的启动参数
            sbs.group(bossGroup, workGroup)
               .channel(NioServerSocketChannel.class)
               .option(ChannelOption.SO_BACKLOG, 128)
               .childOption(ChannelOption.SO_KEEPALIVE, true)
               .childHandler(new ChannelInitializer<SocketChannel>() {
                   @Override
                   protected void initChannel(SocketChannel socketChannel) throws Exception {
                       ChannelPipeline pipeline = socketChannel.pipeline();
                       pipeline.addLast(new NettyServerHandler());
                   }
               });
            // 4. 启动服务端
            ChannelFuture cf = sbs.bind(port).sync();
            System.out.println("服务端启动成功，端口：" + port);
            cf.channel().closeFuture().sync();
        } finally {
            bossGroup.shutdownGracefully();
            workGroup.shutdownGracefully();
        }
    }
    ```

    **客户端 `NettyClientServer.java`**:
    ```java
    public class NettyClientServer {
        private String ip;
        private int port;

        public NettyClientServer(String ip, int port) {
            this.ip = ip;
            this.port = port;
        }

        private void runServer() throws Exception {
            EventLoopGroup bossGroup = new NioEventLoopGroup();
            Bootstrap bs = new Bootstrap();
            bs.group(bossGroup)
              .channel(NioSocketChannel.class)
              .option(ChannelOption.SO_BACKLOG, 128)
              .childOption(ChannelOption.SO_KEEPALIVE, true)
              .handler(new ChannelInitializer<SocketChannel>() {
                  @Override
                  protected void initChannel(SocketChannel socketChannel) throws Exception {
                      ChannelPipeline pipeline = socketChannel.pipeline();
                      pipeline.addLast(new StringDecoder());
                      pipeline.addLast(new StringEncoder());
                      pipeline.addLast(new NettyClientHandler());
                  }
              });

            ChannelFuture cf = bs.connect(ip, port).sync();
            System.out.println("客户端启动成功，连接到：" + ip + ":" + port);
            Channel channel = cf.channel();
            channel.writeAndFlush("客户端发送的消息");

            new Thread(new Runnable() {
                @Override
                public void run() {
                    // 读取服务端响应
                    channel.read();
                }
            }).start();

            cf.channel().closeFuture().sync();
        }
    }
    ```

    **服务端处理器 `NettyServerHandler.java`**:
    ```java
    public class NettyServerHandler extends ChannelInboundHandlerAdapter {
        public static List<Channel> channelList = new ArrayList<Channel>();

        @Override
        public void channelActive(ChannelHandlerContext ctx) throws Exception {
            super.channelActive(ctx);
            channelList.add(ctx.channel());
        }

        @Override
        public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
            System.out.println("服务端收到消息：" + msg);
            // 可以选择向客户端发送响应
            ctx.writeAndFlush("服务端已收到消息");
        }
    }
    ```

    **客户端处理器 `NettyClientHandler.java`**:
    ```java
    public class NettyClientHandler extends ChannelInboundHandlerAdapter {
        public static Channel serverChannel = null;

        @Override
        public void channelActive(ChannelHandlerContext ctx) throws Exception {
            super.channelActive(ctx);
            serverChannel = ctx.channel();
        }

        @Override
        public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
            System.out.println("客户端--收到消息：" + msg);
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：服务端启动** (00:16-00:40)
    讲师在 IntelliJ IDEA 中打开 `NettyProviderServer.java` 文件，逐步讲解并演示了如何创建 `EventLoopGroup`、配置 `ServerBootstrap`、设置 `ChannelOption`，并最终调用 `bind` 方法启动服务端。演示中，讲师在代码中添加了 `System.out.println` 语句，用于在控制台打印服务端启动成功的信息。

*   **场景二：客户端启动与连接** (01:01-01:40)
    讲师切换到 `NettyClientServer.java` 文件，演示了如何创建 `Bootstrap` 对象，配置 `ChannelOption`，并使用 `connect` 方法连接到服务端。在 `initChannel` 方法中，讲师通过 `ChannelPipeline` 注册了 `StringDecoder`、`StringEncoder` 和 `NettyClientHandler`，用于处理数据的编码、解码和业务逻辑。

*   **场景三：消息处理与交互** (01:41-02:00)
    讲师演示了客户端 `NettyClientHandler` 如何处理接收到的消息，并在控制台打印。同时，讲师在服务端 `NettyServerHandler` 中添加了 `channelRead` 方法，用于接收并打印客户端发送的消息。通过在客户端发送消息，讲师展示了服务端如何接收并处理消息，从而实现了双向通信。

*   **场景四：代码调试与运行** (02:01-02:20)
    讲师在代码中添加了 `channel.writeAndFlush("客户端发送的消息")` 语句，用于向服务端发送消息。同时，讲师在客户端启动一个新线程，用于异步读取服务端的响应。通过运行程序，讲师展示了客户端和服务端之间的完整通信流程。
