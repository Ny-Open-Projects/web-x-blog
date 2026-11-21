# 04-Netty使用-Server服务端实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

现在咱们就实现了服务端的工程编码

首先我们看一下服务端它整体的一个实现步骤

在这里它主要是接收客户端的一个请求

并且打印客户端所发送的消息

那么消息这一块是怎么交互呢

采用内置的实讯作为编码和编码器

我们不采用二进制数据

就采用了比较直观的实讯

直接可以看到它所传输的内容

然后我们要开启一个信息输入的监听线程

这个监听线程它就可以发送消息给客户端

这个是服务端的一个整体实现的步骤

咱们首先实现了复集工程NetEase Demo

咱们先创建一个服务模块

我们右键然后New Model

这里面也用Model模板点击Next

名称的话我们叫做NetEase Demo

点击Next

点击Finish

那么NetEase Demo的这个NetEase的集成案例

它的复集工程就已经创建完成

咱们可以看到NetEase Demo

这个source目录可以不需要

我们可以把它删除

接下来的话我们再创建五端

New Model

点击Next

然后的话是NetEase

这个Serve

点击Next

点击Next

点击Finish

那么服务端就已经创建完成

这的话咱们可以看一下

NetEase Server主要有两个核心实现类

一个是NetEase Flowwide Server

这个是干嘛用的呢

这个是要启动NetEase的服务

然后还有一个是什么

还有一个是NetEase的Serve Handle

NetEase Server Handle要对NetEase

就是所接收的数据

做一个编码

还有读取的处理

那么我们可以看到在这里面

通过Channel 3的可以读取到客户端的消息

那我们因为是采用视讯作为这样一个编码解码

所以在这一块不需要做额外的处理

之间可以将内容做一个打印

好

这个就是服务端所要实现的两个核心类

那咱们就来具体实现一下

在这里先创建对应的包

Package

然后Com.IDCast.Net.Serve

这个呢

是它的一个包

那么我们再创建它对应的两个核心实现类

首先咱们先创建服务端的实现

NetEase Server

Provid

Serve

看一下怎么去实现一个NetEase服务端

那么首先必须要有一个端口

这个是服务端口

接着的话呢

我们就要给它一个注入

Public通过构造方法注入进来

NetEase Provider Server

然后呢

Int Port

将这个Port的话呢

赋予我们的

上面所定义的

成员变量Port

好

接着的话呢

咱们就可以启动服务端

怎么启动呢

我们通过一个方法

Public.Wide.Long.Serve

然后呢

将异常抛出去

Sluice.Exception

这个呢是

这个呢是

NetEase Server

通讯

服务端的启动实现

那咱们看一下具体该怎么去实现呢

首先呢

咱们呢要去定义一个Boss的监定组

Event

Loop

然后呢

是Gloop

这个呢是Event实现的监定组Boss.Gloop

好

在这里呢

它是一个包错了对不对

因为的话呢我们并没有集成对应的依赖包

好

好

好

Initially

因为它在这一块呢

是一个易步出点机制对吧

Event

然后呢

Loop

那这个Gloop呢

我们给它另外一个名称

叫WorkGloop

好

New

NIO

它们两个呢

实际都是

从同一个对象当中

创建出来的对不对

它们的一个作用是不一样的

接着的话呢

咱们就要做一个具体实现

然后呢是要

定义呢

NIO的

服务启动类

采用 server boot strip

然后 sbs 连接

new server boot strip

接着的话咱们要配置

NIO服务的启动相关参数

这个就比较重要了

那我们看一下怎么去配置呢

sbs.group

然后将它的 boss group

以及 workgroup 加入进来

加入完成之后咱们还去设置channel

channel 我们采用 nio

server socket channel.class

然后我们就要开始设置它的选项参数

选项参数咱们一般常用的

可以做一个设置像channel opinion

然后在这里面是点so backlog

这个参数是什么意思呢

这个参数的话

它是设置pcp最大缓存连接个数

如果是生产os6.5的版本

默认是128

这个咱们可以根据自己的实际需要

如果说你的并发量特别大

可以将它相应的调高一点

一般情况下咱们就采用默认参数

就可以了

然后再去点channel

点chad opinion

在这里面的话

咱们再设置另外一个参数

channel opinion

在这里面是keep live

keep live我们让它设置为出

这个是什么意思

保持连接的正常状态

那么下面的话

还要有它对应的一个日志

对不对

通过日志的话

我们可以便于去跟踪和定位相关的一些问题

lock in handle

然后log in live

因为通过这个日志的话

跟我们log4j这里面日志的话有些不一样

它在这里呢

neti如果是开启了

它会将一些数据报的报文给打印出来

然后点chad

这里面我们还说一个配置handle

这个handle的话是用于管道的handle的配置

比如说我的编码器

还有我的解码器

channel initial

然后在这里面的话

给它一个翻新类型

翻新的话是一个sorti的channel

然后呢

在里面我们还去重写它的对应实行方法

我们去重写了它的

数字化方法

init channel

这个是重写channel的数字化方法

那这里面

在这里面呢

咱们主要是要配置它的一个管道

注册相关的信息

我们首先呢

来创建一个channel

pile

在这里面的话

pile

给一个sorti的channel

在这里面的话呢

去创建一个pile对象

好

这个呢是什么意思

管道的注册handle

接下来呢

咱们还要配置它的一个编码通道处理

编码通道处理呢

咱们来看一下pile

在这里面点add last

就是在它的最末端的这个档案里面呢

在这里面呢

我们可以在这里面呢

去添加对应的编码

编码器

这个呢是主要做一个解码的

也就是说

我接收到客户的所发过来的消息

但是呢

我并不知道你具体的内容

对吧

那这个时候怎么办呢

就要通过解码器

然后将它的内容的话呢

重新去解析

做一个转换

那么同样咱们呢

要发送消息呢

要想要一个转码对不对

转码的通道处理

pile

pile

然后呢再点add last

在这里面的话呢

就是encode

就做了一个编码

因为我们呢是采用string的这个编码器

就直接采用nete内置的string encode就可以了

最后呢

咱们呢

还要去添加一个什么事件处理器

就是比如说我们接收到客户端的数据

接收到数据之后呢

咱们该怎么处理

对吧

就交由我们的实现内去做对具体的逻辑实现

neti server handle

这个呢

咱们先写在这里

这个其实就是下面的咱们这个核心内

因为还没有实现

等下的话呢

咱们再做具体的一个实现

在这里面呢

它就是处理接收到的请求数据

好

这样呢

咱们就完成了nete服务端的一个启动

主要呢

就是

这样的一个实现流程

然后呢

具体的一些配置参数

好

下面呢

咱们来加快一下

在这里面的话呢

我们再把这一块代码拷贝过来

那下面的话呢

还要再拷贝一个翻轮

最后呢

就要开启无端的实现线程

这个呢

是放在最下面

这里work loop

好像是没找到

对不对

因为这是编写的话呢

抽

work loop

好

那么咱们先再实现了它的nete服务行动

先把收入解决

咱们再来讲解一下

就是刚才拷贝这一块的处理流程

好

nete服务行动

创建对应的实现内

new

加了class

然后呢

我们把这块实现拷贝一下

好

将相应的包呢

导进来

在nete下面

好

导了完成之后呢

有包做了

对吧

那我们来

重新恢复一下

在下面的话呢

咱们呢

是实现了它的一个

圈头的初始化处理

对不对

实现了圈头初始化处理之后呢

整个服务它就可以了正常启动

那就是15端的一个启动

那下面是干什么呢

下面是要监听输入消息

也就是说我服务端

我要下发消息给客户端

对不对

那么我是不是要去监听

我的控制台的输出消息

对吧

这个现场呢

就是做这个事情

那它怎么去监听呢

通过一个vr queue

不停的去监听你的输入

如果说你有输入新的字符

那么的话呢

按回车进行一个输入

然后进行对应的发送

在这里面的话呢

它就会呢

通过圈头将数据呢

发送给客户端

这个呢

是它的一个主要的功能和作用

那在下面呢

就是要绑定端口

绑定端口的作用呢

它是要监听

就是客户端所发过来的连接请求

因为我们面向呢

不单单是一个客户端

对不对

是所有的就是面向呢

可以提供很多的客户端的连接

那在这里呢

它是通过什么sync

同步方式的一个传输

是

最后呢

咱们不要忘记了

要什么

让它优雅进行一个关闭

这样的话呢

就能够防止一些

一些强行中止呢

导致了程序的异常整

强化了一些信息

比如说你这个逻辑

还没处理完成

你呢

就强行中止了这个现成

那么的话呢

对你一些业务逻辑的稳定性呢

就会有些比较大的影响

好

这个呢

就是它的一个优雅的关闭方式

咱们呢

就建议放在Finder

Finder里下面

去做对应的实现

这是实现

好

NetEase的优雅关闭

好

再往下面呢

就是对NetEase服务端进行一个启动

那NetEase服务端启动的时候呢

咱们上面是给了它一个构造参数

对不对

要传递对应的端口

那么呢

传递端口之后呢

通过乱生活方法呢

就可以启动整个服务端

好

在这里呢

咱们就实现了NetEase服务端的整个的实现流程

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频是关于 **Netty 网络编程框架** 的实战教学课程，具体讲解了如何构建一个简单的 **Netty 服务端**。课程从项目工程结构入手，逐步演示了如何配置 Maven 依赖、编写服务端启动类 `NettyProviderServer`、配置 `ServerBootstrap`、设置 ChannelPipeline 以及实现 `ChannelInboundHandlerAdapter` 来处理客户端连接和消息。整个过程旨在帮助学习者理解 Netty 的核心组件和基本使用方法，为后续开发网络应用打下基础。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程开场，展示项目总览和学习目标。
*   **00:16 - 00:30**: 介绍项目结构，展示 `netty-demo` 父工程和 `netty-server` 子模块。
*   **00:31 - 00:45**: 查看父工程 `pom.xml`，确认项目版本和模块结构。
*   **00:46 - 01:00**: 查看 `netty-server` 子模块的 `pom.xml`，添加 Netty 核心依赖。
*   **01:01 - 01:20**: 编写 `NettyProviderServer` 类，定义服务端口和启动方法。
*   **01:21 - 01:40**: 在 `runServer()` 方法中，使用 `ServerBootstrap` 初始化服务。
*   **01:41 - 02:00**: 配置 `ServerBootstrap`，设置 `bossGroup`、`workerGroup`、`Channel` 类型、`ChannelOption` 和 `ChannelHandler`。
*   **02:01 - 02:20**: 实现 `ChannelInboundHandlerAdapter`，用于管理客户端连接。
*   **02:21 - 02:40**: 在 `channelActive` 方法中，将新连接的 `Channel` 添加到列表中。
*   **02:41 - 03:00**: 在主线程中，读取用户输入并广播给所有已连接的客户端。
*   **03:01 - 03:15**: 完成服务端代码，准备运行。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **工程结构**: `netty-demo` 作为父工程，包含 `netty-server` 和 `netty-client` 两个子模块。
*   **工程依赖**: 在父工程的 `pom.xml` 中，定义了 `<modules>`，包含 `netty-server` 和 `netty-client`。
*   **学习目标**: 第一章 Netty 使用，包括目标、步骤、实现、工程设计、工程结构、服务端工程、客户端工程、工程演示。

#### 代码关键内容

*   **父工程 `pom.xml`**:
    ```xml
    <modules>
        <module>netty-server</module>
        <module>netty-client</module>
    </modules>
    ```

*   **`netty-server` 子模块 `pom.xml`**:
    ```xml
    <dependencies>
        <dependency>
            <groupId>io.netty</groupId>
            <artifactId>netty-all</artifactId>
            <version>4.1.16.Final</version>
        </dependency>
    </dependencies>
    ```

*   **`NettyProviderServer` 类**:
    ```java
    public class NettyProviderServer {
        private int port;

        public NettyProviderServer(int port) {
            this.port = port;
        }

        public void runServer() throws Exception {
            // 1. 定义时间的boss监听组
            EventLoopGroup bossGroup = new NioEventLoopGroup();
            // 2. 定义Worker，用于处理已经被接收的连接
            EventLoopGroup workGroup = new NioEventLoopGroup();
            try {
                // 4. 定义NIO的服务启动类
                ServerBootstrap sbs = new ServerBootstrap();
                // 5. 配置NIO服务的启动相关参数
                sbs.group(bossGroup, workGroup)
                   .channel(NioServerSocketChannel.class)
                   .option(ChannelOption.SO_BACKLOG, value: 128)
                   .childOption(ChannelOption.SO_KEEPALIVE, value: true)
                   .childHandler(new ChannelInitializer<SocketChannel>() {
                       @Override
                       public void initChannel(SocketChannel ch) throws Exception {
                           ch.pipeline().addLast(new NettyServerHandler());
                       }
                   });
                // 6. 绑定端口，开始接受链接
                ChannelFuture cf = sbs.bind(port).sync();
                cf.channel().closeFuture().sync();
            } finally {
                bossGroup.shutdownGracefully();
                workGroup.shutdownGracefully();
            }
        }
    }
    ```

*   **`NettyServerHandler` 类**:
    ```java
    public class NettyServerHandler extends ChannelInboundHandlerAdapter {
        public static List<Channel> channelList = new ArrayList<Channel>();

        @Override
        public void channelActive(ChannelHandlerContext ctx) throws Exception {
            super.channelActive(ctx);
            channelList.add(ctx.channel());
        }
    }
    ```

*   **`main` 方法**:
    ```java
    public static void main(String[] args) throws Exception {
        new NettyProviderServer(9911).runServer();
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示 (00:16 - 00:30)**: 教师在 IntelliJ IDEA 中展示了 `netty-demo` 项目，强调其多模块结构，包括 `netty-server` 和 `netty-client`。通过鼠标点击，演示了如何在项目视图中展开和查看各个模块的文件结构。

*   **场景二：Maven 依赖配置 (00:46 - 01:00)**: 教师切换到 `netty-server` 模块的 `pom.xml` 文件，演示如何添加 Netty 的核心依赖。通过鼠标选中并高亮显示 `<dependency>` 标签，强调了 `groupId`、`artifactId` 和 `version` 的配置。

*   **场景三：Netty 服务端初始化 (01:21 - 01:40)**: 教师在 `NettyProviderServer` 类中编写 `runServer()` 方法。通过鼠标点击和高亮，演示了如何创建 `EventLoopGroup`、`ServerBootstrap` 对象，并调用 `group()`、`channel()`、`option()`、`childOption()` 和 `childHandler()` 方法进行配置。

*   **场景四：ChannelPipeline 配置 (01:41 - 02:00)**: 教师演示了如何在 `childHandler()` 中添加 `ChannelInitializer`，并使用 `ch.pipeline().addLast(new NettyServerHandler());` 将自定义的 `ChannelHandler` 添加到 ChannelPipeline 中。

*   **场景五：客户端连接管理 (02:01 - 02:20)**: 教师在 `NettyServerHandler` 类中实现 `channelActive()` 方法。通过鼠标点击和高亮，演示了如何将新连接的 `Channel` 添加到 `channelList` 静态列表中，以便后续广播消息。

*   **场景六：服务端运行与消息广播 (02:41 - 03:00)**: 教师在 `runServer()` 方法中添加了读取用户输入并广播的逻辑。通过鼠标点击和高亮，演示了如何使用 `BufferedReader` 读取标准输入，然后遍历 `channelList` 并调用 `channel.writeAndFlush(str);` 方法向所有客户端发送消息。

*   **场景七：代码调试与运行 (03:01 - 03:15)**: 教师在 `main` 方法中调用 `new NettyProviderServer(9911).runServer();`，并点击运行按钮。通过鼠标点击和高亮，演示了如何启动服务端，并在控制台中看到服务启动日志。
