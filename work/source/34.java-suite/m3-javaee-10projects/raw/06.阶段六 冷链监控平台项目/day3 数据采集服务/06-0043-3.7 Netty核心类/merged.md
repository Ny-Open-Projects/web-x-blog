# 3.7 Netty核心类

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day3 数据采集服务
- 源文件：06.阶段六 冷链监控平台项目\day3 数据采集服务\3.7 Netty核心类_【海量资源尽在 666java.com】.mp4
- 时长 7分16秒（音频 436s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] NetE是一个网络编程框架那么它的整个框架有一些核心的类那么下面我们来看一看NetE这个框架它的一些核心类那第一个来讲的话叫boostdrop和server boostdropboostdrop的意思是一个引导一个NetE应用通常是由一个boostdrop开始的那么它的主要作用呢是配置整个NetE程序那么串联各个组件
[00:26] NetA中的boostdrop是客户端程序的一个启动引导类server bootstrap是服务端启动引导类那第二个类的话叫selectorNetA基于select对象实现了RO的多路复用通过select一个线程可以监听多个连接的channel事件当向一个select中注册channel之后
[00:52] Selector内部的机制就可以自动的不断查询这些注册的Channel是否有已就绪的RO事件比如说是否有可读的可写的网络连接完成的等等这样的一些RO事件这样程序就可以简单的使用一个现成高效的管理多个Channel了比如我们开始看到的这样的一个这个例子这个Selector其实就是一个多路附用的这样的一个
[01:21] 这个呢selector也是我们neti中的一个非常重要的一个类那下面的话我们说这个另外一个类叫channel类channel类我们通过前面的这种附用啊附用模型多路附用模型以及neti的这种现成模型可以理解neti网络编程中它是主要用来执行网络中的RO操作那么一个channel或者叫一个通道
[01:51] 用户提供了是当前这个网络连接的通道的状态是否比如说是否这个通道是打开的连接是否是已经连接上来的那第二点来讲的话它会呃网络配置一些网络连接的参数比如说我们接收缓冲区的一个大小我们可以在channel里边设置那第三点来讲的话它会提供一步的网络RO操作比如建立连接啊读写绑定端口
[02:21] 等等这样的一些操作那么一步调用意味着我们任何一个RO调用都将立即返回并且不保证在其调用结束时所请求的RO操作已完成在这种情况其实叫做一步对吧那第四点来讲的话是指调用立即返回一个Channel Future的一个实例那么通过注册监听器到Channel Future上就可以RO操作成功失败或者取消时回调通知
[02:50] 那第五点来讲的话它支持RO的操作并与对应的处理程序那不同的协议不同的组织类型的连接都有不同的channel与它对应那常见的channel包括ARO的socket channel那么它是用于一部的客户端的TCP的socket的一个连接ARO server socket的这种channel呢它是一部服务器端TCP的socket的连接
[03:20] diagrammer的这种channel它是一部的UDP连接ARO的SATP channel是指的一部客户端SATP这种连接ARO SATP server channel呢是一部的SATP服务器端的一个连接那么这些连接通道涵盖了我们如果开发UDP TCP协议或者这种服务器的时候网络RO及其文件的一些RO
[03:48] 那第四个比较常用或者比较重要的类叫做NRO Event Loop和NRO的Event Loop GroupNRO Event Loop中维护了一个现成和任务对立它支持一步的提交任务现成启动时会调用NRO Event Loop中的run方法那么执行RO任务和非RO任务包括我们的accept方法bind方法read方法connect方法read all task
[04:17] 方法等等这些方法都都是构成了我们这种ARO的event loop中的一些方法那这两种任务中它的执行时间呢是由一个RO RETO这个变量来控制的默认是50%就是说50%的是执行RO任务50%的执行的非RO任务那么这非RO任务指的是我们的逻辑处理任务那还有一个的话是指我们的AROevent loop group
[04:46] 它是主要管理我们的event loop的一个生命周期我们可以把它理解为就是一个现成池它是有一组的这种ARO group loop那么第五类的话是叫channel的一个handlerchannel handler相对来讲也比较好理解一些它是我们监听channel或者channel它调用的一个执行的这种RO事件或者说是RO的一个操作那么它要执行什么样的一个程序这个是我们的
[05:15] Channel的一个Handler大家注意Channel Handler是一个接口这个接口我们要具体的要实现它里边的一些方法那第六个的话是我们的Future和Channel Future这个Future和Channel Future大家可以理解为是一个回调监听函数也就是说我们的Net中的任务都是一个义务的对不对我把我的消息提交给那个比如说我们前面讲的一个例子
[05:43] 假设我要把我的材料提交给某一个部门这个部门来处理那么部门这个部门处理完了之后他要告诉我那么我提前就需要把我的电话号码或者说我的地址我要给这个处理部门留下来我的电话号码就是这个那么你们处理完了之后呢你给我打电话我就再来取这个future和channel future其实就是做这么一个作用它是处理的这种一步的回调函
[06:12] 或者说回调函数的监听的一个事件有事件的时候处理完了之后你就叫这个函数叫这个方法这是我们在NetEase框架里边常用的一些类它涵盖了我们在处理业务的时候或者说比如说我们这个Service Socket整个的这个Server它在无论是说我的程序的一个引导还是我们服务器的一个现成的处理
[06:41] 甚至于我们在处理完了之后一个一步的回调我监听哪一些这个通道我的通道如何选择比如说我们用select来进行选择那么这些类是构成了我们整个的native框架的一些比较核心的类由这些类能组成了我们整个native的高可用高并发的能力主要是高并发能力的这是我们native的一个核心类的给大家的一个讲解
[07:10] 那么下面一步我们会给大家讲解我们整个服务的一个开发过程

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Netty 的核心组件，包括 Bootstrap、Selector、Channel、NioEventLoop/NioEventLoopGroup、ChannelHandler 和 Future/ChannelFuture，以及事件驱动模型和 Reactor 线程模型。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 标题：2.3 核心类
- 内容：
  1. Bootstrap/ServerBootstrap
     Bootstrap 意思是引导，一个 Netty 应用通常由一个 Bootstrap 开始，主要作用是配置整个 Netty 程序，串联各个组件。Netty 中 Bootstrap 类是客户端程序的启动引导类，ServerBootstrap 是服务端启动引导类。
  2. Selector
     Netty 基于 Selector 对象实现 I/O 多路复用，通过 Selector 一个线程可以监听多个连接的 Channel 事件。
     当向一个 Selector 中注册 Channel 后，Selector 内部的机制就可以自动不断地查询(Select) 这些注册的 Channel 是否有自己线程的 I/O 事件（例如可读，可写，网络连接完成等），这样程序就可以很高效地使用一个线程高效地管理多个 Channel。
  3. Channel
     Netty 网络通信的组件，能够用于执行网络 I/O 操作。Channel 为用户提供：
     (1) 当前网络连接的通道的状态（例如是否打开？是否已连接？）
     (2) 网络连接的配置参数（例如接收缓冲区大小）
     (3) 提供异步的网络 I/O 操作(如建立连接，读写，绑定端口)，异步调用意味着任何 I/O 调用都将立即返回，并且不保证在调用返回时所需的所有 I/O 操作已完成。
     (4) 调用立即返回一个 ChannelFuture 实例，通过注册监听器到 ChannelFuture 上，可以 I/O 操作成功、失败或取消时回调通知调用方。
     不同协议、不同的阻塞类型的连接都有不同的 Channel 类型与之对应。
     常用的 Channel 类型：
     - NioSocketChannel，异步的客户端 TCP Socket 连接。
     - NioServerSocketChannel，异步的服务器端 TCP Socket 连接。
     - NioDatagramChannel，异步的 UDP 连接。
     - NioSctpChannel，异步的 Sctp 连接。
     - NioSctpServerChannel，异步的 Sctp 服务器端连接，这些通道涵盖了 UDP 和 TCP 网络 IO 以及文件 IO。
  4. NioEventLoop/NioEventLoopGroup
     NioEventLoop 中维护了一个线程任务队列，支持异步提交执行任务，线程启动时会调用 NioEventLoop 的 run 方法，执行 I/O 任务和非 I/O 任务：
     - I/O 任务，即 selectionKey 中 ready 的事件，如 accept, connect, read, write 等，由 processSelectedKeys 方法触发。
     - 非 I/O 任务，添加到 taskQueue 中的任务，如 register, bind 等任务，由 runAllTasks 方法触发。
     两种任务的执行时间比由变量 ioRatio 控制，默认为 50，则表示分配 I/O 任务的执行时间与非 I/O 任务的执行时间相等。
     NioEventLoopGroup，主要管理 eventLoop 的生命周期，可以理解为一个线程池，内部维护了一组线程，每个线程(NioEventLoop)负责处理多个 Channel 事件，而一个 Channel 只对应于一个线程。
  5. ChannelHandler
     ChannelHandler 是一个接口，处理 I/O 事件或拦截 I/O 操作，并将其转发到其 ChannelPipeline(业务处理链)中的下一个处理程序。
  6. Future, ChannelFuture
     Netty 中所有的 I/O 操作都是异步的，不能立刻得知消息是否被正确处理。
     但是可以监听一会等执行完成或者直接注册一个监听，具体的实现就是通过 Future 和 ChannelFutures，他们可以注册一个监听，当操作执行成功或失败时监听会自动触发注册的监听事件。

画面 2:
- 标题：2.2.2 Reactor 线程模型
- 内容：
  Reactor 是反应式的，Reactor 模型是通过一个或多个线程同时传递给多个处理器的事件驱动模式。
  服务器程序处理用户多路请求，并将它们同步分派给对应的处理线程。Reactor 模式也叫 Dispatcher 模式，即 I/O 多了复杂处理请求，服务器程序分派 Dispatch 给处理线程，是高性能网络服务器的必备技术之一。
  Reactor 模型中有 2 个关键组件：
  (1) Reactor: Reactor 在一个单独的线程中运行，负责监听和分发事件，分发适当的处理程序对 I/O 事件做出反应。它就像公司的电话接线员，它把来自客户的电话转接到适当的联系人。
  (2) Handlers: 处理程序是执行 I/O 事件要完成的实际事件，是以下客户要与之交谈的公司的中实际雇员。
  Reactor 通过分派合适的处理程序来响应 I/O 事件，处理程序执行非阻塞操作。
  图表：
  应用程序
  └─── 线程处理

画面 3:
- 标题：2.2.1.2 反应模型
- 内容：
  Netty 特点：
  Netty 的 IO 线程 NioEventLoop 由于整合了多路复用器 Selector，可以同时并发处理成百上千个客户端连接。当线程从客户端 Socket 通道进行读写数据时，若没有数据可读，则线程就阻塞在 Read 操作上，造成线程资源浪费。
  图表：
  Socket
  └─── SocketChannel
  └─── SocketChannel
  └─── SocketChannel
  └─── SocketChannel
  └─── Selector
  └─── Thread

画面 4:
- 标题：2.2.1 事件驱动模型
- 内容：
  通常，我们设计一个事件处理模型的思路有两种：
  (1) 轮询方式：线程不断轮询相关事件发生没有发生事件，有发生事件时就调用事件处理逻辑；
  (2) 事件驱动方式：发生事件，主线程把事件放入事件队列，在另外线程中不断轮询消费事件列表中的事件，调用事件对应的处理逻辑处理事件。事件驱动方式也被称为消息通知方式，其实是设计模式中观察者模式的思路。
  图表：
  Event
  └─── Event Queue
  └─── Event Mediator
  └─── Event Handler
  └─── Event Handler
  └─── Event Handler

画面 5:
- 标题：2.3 核心类
- 内容：
  1. Bootstrap/ServerBootstrap
     Bootstrap 意思是引导，一个 Netty 应用通常由一个 Bootstrap 开始，主要作用是配置整个 Netty 程序，串联各个组件。Netty 中 Bootstrap 类是客户端程序的启动引导类，ServerBootstrap 是服务端启动引导类。
  2. Selector
     Netty 基于 Selector 对象实现 I/O 多路复用，通过 Selector 一个线程可以监听多个连接的 Channel 事件。
     当向一个 Selector 中注册 Channel 后，Selector 内部的机制就可以自动不断地查询(Select) 这些注册的 Channel 是否有自己线程的 I/O 事件（例如可读，可写，网络连接完成等），这样程序就可以很高效地使用一个线程高效地管理多个 Channel。
  3. Channel
     Netty 网络通信的组件，能够用于执行网络 I/O 操作。Channel 为用户提供：
     (1) 当前网络连接的通道的状态（例如是否打开？是否已连接？）
     (2) 网络连接的配置参数（例如接收缓冲区大小）
     (3) 提供异步的网络 I/O 操作(如建立连接，读写，绑定端口)，异步调用意味着任何 I/O 调用都将立即返回，并且不保证在调用返回时所需的所有 I/O 操作已完成。
     (4) 调用立即返回一个 ChannelFuture 实例，通过注册监听器到 ChannelFuture 上，可以 I/O 操作成功、失败或取消时回调通知调用方。
     不同协议、不同的阻塞类型的连接都有不同的 Channel 类型与之对应。
     常用的 Channel 类型：
     - NioSocketChannel，异步的客户端 TCP Socket 连接。
     - NioServerSocketChannel，异步的服务器端 TCP Socket 连接。
     - NioDatagramChannel，异步的 UDP 连接。
     - NioSctpChannel，异步的 Sctp 连接。
     - NioSctpServerChannel，异步的 Sctp 服务器端连接，这些通道涵盖了 UDP 和 TCP 网络 IO 以及文件 IO。
  4.

