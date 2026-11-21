# 25-车辆轨迹服务（pd-netty开发_TCP接口方式_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那接下来呢咱们继续来看我们PD-NETI这个服务的开发

刚才呢我们是开发了HTTP这种接口方式对吧

那接下来呢我们来开发下一个呢就是TCP这种方式

而这种方式呢我们使用了一个框架

就是NETI这个网络编程的框架

那首先呢我们先来简单了解一下

NETI呢它是由JBOS提供的一个Java开源框架

那么它提供这种一步的事件驱动的这种网络应用程序框架

还有工具

从而呢可以使我们快速的来开发出高性能

高可靠性的这种网络服务器和这个客户端程序

当然我们这个地方呢使用NETI呢开发的是我们服务端的程序

咱们再回过头来来看一下这个图

你看我们PD-NETI这个地方呢

前面也介绍了准备提供这么两种方式的服务对吧

一种是HTTP的还有一种是TCP的

而TCP的这种呢底层呢我们就是使用NETI这个框架来进行编程

那这样的话呢

我们司机端APP呢

可以走这个HTTP协议也可以走TCP对吧

那么都可以来上报位置信息

好

那么这是关于我们这个NETI简单来介绍一下

当然其实如果这个NETI如果我们展开去讲的话呢

它其实包含的内容还是非常非常多的

但是因为我们这个项目我们是作为定位是项目课对吧

所以说我们这个NETI呢就把它当成一个工具

我们直接拿过来使用

那么如果大家对NETI呢有一些

想了解更加详细的一些细节的内容

那么大家可以自行上网上去搜一些资料啊

自行来学习一下

那么我们这个地方呢就直接拿过来使用了

其实使用这个NETI来进行编程的话呢

基本上也都是一些模板化的代码

所以对于这一类的代码呢

那么我们也不用自己一点一点手敲出来

那么网上呢相关的资料呢也是非常多的

那么这些代码呢基本上也是比较固定的

那么无非就是什么呢

有一些比较个性化的代码呢

有一些比较个性化的代码呢

有一些比较个性化的代码呢

有一些比较个性化的

比如说我们这个要读取完这个信息之后

对吧

那么读取完这个流之后

那么我们如何来处理

这块呢可能是不同的项目

有不同的处理方式

比如说我们这块

我们跟这个客户端

咱们看这个图

跟这个客户端连接上之后

对吧

把这个位置信息

把这个数据给他读取到

那么读取到之后

我们这块做的处理是什么呢

是不是把这个信息

把它

把它

发送到卡夫卡对链

那么其他的项目呢

可能读取到这个信息之后呢

有可能记录到日志

也有可能记录到数据库

也有可能做其他的业务操作

那么这一块的代码

是根据我们这个业务不同

那么

是有所不同的

而整体的我们如何去

创建一个Neti的服务

那么如何去指定它的channel

对吧

它的通道

等等这些代码呢

其实都属于模板化的

那么对于这些模板化的代码呢

我们其实没有必要去

去把它背下来

没有多大意义

好

所以说我们这块的话呢

咱们就直接啊

把我们讲一下这个代码

来考过来

因为都属于模板化的

然后呢

我们大概来读一下

就可以了

好

那么首先我们第一步呢

需要来编写一个Neti Server

刚才也提到了

我们要开发的

是不是我们服务器端的应用

对吧

所以说呢

需要开发这么一个Neti Server

并且呢

这个服务呢

它是可以启动的

对吧

就跟我们以前讲Tomcat的

对吧

我一启动的话

我可以绑定上

8080端口

那么它在这个端口呢

可以持续的来监听

我们客户们的请求

那么Neti Server呢

也是一样的

它随着我们的项目启动呢

这个Neti Server

也就起来了

好

那这块我们使用的端口号呢

大家可以看一下

在我们这个Nexus当中呢

你看我定义了一个Neti Part

对吧

是1001

但是这个端口号

我们随便指定啊

只要跟其他的服务端口

别冲突了就可以了

好

那么我们指定的是这个

好

然后呢

我们来看一下

我们需要创建这么一个

Neti Server这么一个类

好

然后在这个类里边呢

需要来创建一堆对象

一会儿呢

我们考进来

大概来读一下这个代码

好

咱们把这个呢

先都关上

然后呢

在我们这个Config下面呢

来创建咱们这个Neti Server

好

具体里边的代码呢

整体考过来之后

咱们来

大概来读一下这个代码

好

这是Neti Server

好

但是这个地方报错

是因为我们现在呢

还在这个

没有这个类

一会儿我们需要来创建这个类

而且重点呢

我们其实就是去写这个类

好

咱们来看一下

那这Import

他想报错

先不用管他

好

你看这是我们这个服务启动类

对吧

同时呢

这个类呢

我也希望

干什么呢

由我们的Spring容器来管理

你看我这是不是加了这么一个Component的注解

为什么要加它呢

哎

就是因为我们在这里边需要来动态的注入一个part

对吧

part

这是不是我们那个短口号

也就是说我们这个Neti

他这个Neti Server启动的时候呢

也是需要去绑定一个短口号的

而这个短口号呢

我不希望在我们的程序当中写死

对吧

那么从外部我们需要给他读取过来

你看这是不是Neti.part

通过这个Value注解

对吧

那么他就可以从我们这个地方

动态的把它读过去

好

所以最终呢

我们Neti Server启动的时候呢

使用的就是1001这个短口号

好

然后呢

在这儿加了这么一个注解

当我这个实例啊

创建好之后呢

他其实就会干什么呢

把我们当前Neti Server

这个短口号呢

Neti Server创建出来的实例

复制给这个对象

这个是一个静态的

对吧

目的是什么呢

他在下边呢

会使用到

你看

这不是Server.bond

是不是绑定啊

当然了

这块的话

我们来整体来读一下

这个代码结构啊

首先呢

我们来看

当前这个类呢

他实现了一个接口

叫做Command Line Render

那么大家来想

这个接口的话呢

我们前面其实已经学过了

对吧

就是什么呢

我实现这个接口的话

可以达到一个什么样的效果呢

就是当我们这个项目启动的时候

Spring Boot项目启动的时候呢

那么就会执行到我们当前这个类

因为你实现了这个接口

对吧

那这样的话呢

他就会去执行这个run方法

所以说你看我们这边的肯定要实现这个run方法

而在这个run方法当中啊

他就是this.start

调用start方法

而start方法是在上面的

那就意味着我们项目启动的时候呢

就会去执行这个方法

而这个方法是什么呢

是server.bound

是不是绑定绑定什么呢

绑定我们这个端口对吧

启动服务的时候

注意这是启动native服务啊

在这来

启动native服务的时候来绑定端口

具体那个端口号

咱们是不是通过native server.part

这样的话你看我一点是不是到这了

那么他动态解析出来的

刚才也看到了就是101对吧

所以说呢

我们项目启动的时候

他会执行run方法

run方法里面就一句话

那他就会调用start的方法

而start的方法这呢

他是不是就会去绑定端口呢

比如说那你这个server从哪来的呢

这个server呢

其实是在我们上面声明的

并且呢

咱们这个实例构建的时候呢

他是不是会调他的无参的构造方法

对吧

会调用无参的构造方法

而在这儿的话呢

我们是不是就已经把这个什么呢

把这个server给创建出来了

就是这个server

你看这儿是不是new出来了

所以说呢

这个地方呢

我们就通过server.bound

这就是启动服务

并且绑定端口

具体这儿这个端口刚才看了

是101对吧

然后控制这个端口

用这台输出这么一句话

就可以了

那么重点就是什么呢

这个server

它是怎么创建出来的呢

这块呢

其实都属于模板化的

那就是我们这个构造方法

对吧

所以说项目启动的时候呢

他要创建实例

要创建实例

他就会调用这个无参构造方法

来创建这个实例

这样的话

我们这个server对象就创建出来了

然后呢

这个地方我们可以看到

他是不是new了这么两个对象

你会发现这两个类是一样的

对吧

叫什么NIO event loop group

这其实是什么呢

是两个

线程组

而且是NIO的线程组

对吧

非组色的

NIO的线程组

那么主要是用于处理什么呢

网络相关的事件

因为我们是这个Netty

它的定位呢

就是开发这种网络应用程序

对吧

不管是你是网络的客户端

还是网络的服务端

那么他都要进行交互

对吧

客户端跟服务端

通过这个IO来进行交互

那这个时候呢

就需要来处理网络事件

那么这个地方呢

他就是来创建一些线程组

通过多线程的方式

那么来并行的处理这些网络事件

所以这个地方呢

需要两个线程组

那么处理不同的

也就是说他们之间

其实是有分工的

有分工的

你看一个是main group

一个是sub group

对吧

这两个线程组

然后呢

我们把这个对象创建出来

这个server呢

它叫server bootstrap

它其实是服务初始化的工具

用来封装什么

初始化服务的一些复杂的代码

你可以认为

这就是我们通过NIO这么一个server

这就是创建了

一个neti的什么呢

服务端

服务端

但是这个服务端呢

需要做一些配置

所以下边这对代码呢

这就是什么呢

配置我们这个neti服务端

好

配置我们这个neti服务端

比如说来指定什么呢

你真正这个服务端

跟客户端交互的时候

有很多网络事件对吧

那么需要指定这两个线程组

通过多线程的方式去指定

对吧

去处理

所以说这儿

需要绑定这么两个线程组

然后呢

还要设置什么呢

缓存对吧

还要设置什么呢

keep alive

是否是持续

就是相当于它是一个长连接

对吧

一个长连接

keep alive

好

然后这个的channel

channel其实是通道对吧

这是我们neti当中

它提供的一个概念

我们简单理解了

你可以把它认为就是一个连接

但是它跟我们以前的connection

这种连接还不太一样

它指的是一个通道

那么在这儿呢

就是指定什么呢

指定我们使用这个

产生的一个连接

一个channel用来接收连接

其实是跟我们客户端来进行连接的

那么到时候产生的

就是这种类型的通道

因为它这种通道呢

有多种类型

这个是NIO server

什么socket的channel

对吧

是这种类型

然后呢

最重要的其实是后边这个

就是child handler

这就是具体来处理网络IO事件的

你看这个类是不是现在报错

因为我刚才也提到了

我们重点呢

就需要自己去写这个类

而对于其他的这些代码

这一堆代码

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

那么不同的项目

可能有不同的业务

对吧

那么处理方式不一样

所以说呢

我们重点一会儿就需要去编写这个类

这个才是具体每个项目不同的地方

而对于上面提到的这一堆

对吧

都属于模板化的

那么大家使用这个Netty

来编写我们的服务端

那么基本上全都是这个套路

好

这是关于咱们这个Netty server

一会儿呢

我们再来看一下这个类是如何编写的

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“TMS项目”的技术课程，具体讲解了如何使用 **Netty** 框架开发一个 **TCP服务端**。课程内容围绕一个名为 `pd-netty` 的服务展开，该服务用于接收车辆定位信息并发送到 Kafka。视频主要演示了如何在 IntelliJ IDEA 中创建并编写一个基于 Netty 的 Java 服务启动类 `NettyServer.java`，包括配置 NIO 线程组、创建 ServerBootstrap、设置 ChannelOption、绑定端口等核心步骤。同时，视频也展示了相关的配置文件（如 `bootstrap.yml`）和配置中心（Nacos）的设置。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频中的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: 课程介绍与项目导航。画面显示了项目结构，当前选中的是“5. 车辆轨迹服务”下的“5.1.2 TCP方式”。
*   **00:05 - 00:15**: 介绍 Netty 框架。画面展示了 Netty 的定义和用途，强调其异步、事件驱动的特性。
*   **00:15 - 00:30**: 编写服务启动类。画面聚焦在 `NettyServer.java` 文件，开始编写核心代码。
*   **00:30 - 00:45**: 配置 NIO 线程组。代码中创建了 `NioEventLoopGroup` 的实例 `mainGroup` 和 `subGroup`。
*   **00:45 - 00:55**: 初始化 ServerBootstrap。代码中创建了 `ServerBootstrap` 实例 `server`。
*   **00:55 - 01:05**: 配置 Netty 服务端。代码中调用 `server.group(...)`、`.option(...)`、`.childOption(...)`、`.channel(...)` 和 `.childHandler(...)` 方法进行配置。
*   **01:05 - 01:15**: 启动服务。代码中调用 `server.bind(...)` 方法绑定端口，并在 `start()` 方法中打印启动日志。
*   **01:15 - 01:25**: 展示配置文件。画面切换到 `bootstrap.yml` 文件，显示了服务的端口配置（`port: 8192`）和 Kafka 相关配置。
*   **01:25 - 01:35**: 展示 Nacos 配置中心。画面切换到 Nacos 界面，显示了 `pd-netty-dev.yml` 的配置内容，包括 `kafka` 和 `netty` 的相关参数。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **Netty 框架介绍**: “Netty是由JBoss提供的一个Java开源框架。Netty提供异步的、事件驱动的网络应用程序框架和工具，以快速开发高性能、高可靠的网络服务器和客户端程序。”
    *   **服务功能**: “pd-netty服务的作用是接收机端上报的车辆定位信息并将信息发送到kafka队列。”
    *   **通信方式**: “pd-netty共提供两种方式来接收机端上报的定位信息：基于netty实现的TCP方式、HTTP接口方式。”

*   **代码关键内容**:
    *   **`NettyServer.java` 启动类**:
        ```java
        package com.ithema.pinda.config;

        import com.ithema.pinda.service.NettyServerHandler;
        import io.netty.bootstrap.ServerBootstrap;
        import io.netty.channel.ChannelFuture;
        import io.netty.channel.ChannelOption;
        import io.netty.channel.EventLoopGroup;
        import io.netty.channel.nio.NioEventLoopGroup;
        import io.netty.channel.socket.nio.NioServerSocketChannel;
        import lombok.extern.slf4j.Slf4j;
        import org.springframework.beans.factory.annotation.Value;
        import org.springframework.boot.CommandLineRunner;
        import org.springframework.stereotype.Component;
        import javax.annotation.PostConstruct;

        @Slf4j
        @Component
        @Slf4j
        public class NettyServer implements CommandLineRunner {

            @PostConstruct
            public void init() {
                nettyServer = this;
            }

            @Value("${netty.port}")
            private int port;

            private EventLoopGroup mainGroup;
            private EventLoopGroup subGroup;
            private ServerBootstrap server;
            private ChannelFuture future;

            public NettyServer() {
                // NIO线程组，用于处理网络事件
                mainGroup = new NioEventLoopGroup();
                subGroup = new NioEventLoopGroup();
                // 服务初始化工具，封装初始化服务的复杂代码
                server = new ServerBootstrap();
                // 配置netty服务端
                server.group(mainGroup, subGroup)
                    .option(ChannelOption.SO_BACKLOG, 128) // 设置缓冲区
                    .childOption(ChannelOption.SO_KEEPALIVE, true) // 指定使用NioServerSocketChannel产生一个Channel用来接收连接
                    .channel(NioServerSocketChannel.class) // 指定使用NioServerSocketChannel产生一个Channel用来接收连接
                    .childHandler(new NettyServerHandler()); // 具体处理网络IO事件
            }

            public void start() {
                // 启动netty服务端，绑定端口
                this.future = server.bind(nettyServer.port);
                log.info("Netty Server 启动完毕！！！ 端口：{} ", nettyServer.port);
            }

            @Override
            public void run(String... args) {
                this.start();
            }
        }
        ```
    *   **`bootstrap.yml` 配置文件**:
        ```yaml
        server:
          tomcat:
            uri-encoding: UTF-8
            max-threads: 1000
            min-spare-threads: 30
            port: 8192
            connection-timeout: 50000ms

        spring:
          application:
            name: pd-netty
            profiles:
              active: dev
            main:
              allow-bean-definition-overriding: true
        ```
    *   **Nacos 配置内容**:
        ```yaml
        kafka:
          bootstrap-servers: 68.79.7.219:9092
          # 指定kafka的生产者
          producer:
            concurrency: 5
            retries: 3
            batch-size: 10000
            buffer-memory: 33554432
            key-serializer: org.apache.kafka.common.serialization.StringSerializer
            value-serializer: org.apache.kafka.common.serialization.StringSerializer
        netty:
          port: 1000
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与课程定位**
    *   **描述**: 视频开头展示了项目的整体结构，通过左侧的导航栏，清晰地定位到“第7章 车辆轨迹服务开发”下的“5.1.2 TCP方式”这一小节，为观众明确了本节的学习目标。

*   **场景二：Netty 服务启动类编写**
    *   **描述**: 视频的核心部分。讲师在 IntelliJ IDEA 中逐步编写 `NettyServer.java` 文件。首先，通过 `@Component` 注解将其注册为 Spring Bean，并使用 `@PostConstruct` 注解在初始化时将自身实例赋值给静态变量 `nettyServer`，以便在 `CommandLineRunner` 中调用。接着，讲师定义了 `port` 属性并使用 `@Value("${netty.port}")` 注解从配置文件中注入端口号。然后，讲师创建了 `mainGroup` 和 `subGroup` 两个 `NioEventLoopGroup` 实例，用于处理网络事件。随后，创建了 `ServerBootstrap` 实例 `server`，并调用其 `group(...)`、`option(...)`、`childOption(...)`、`channel(...)` 和 `childHandler(...)` 方法进行配置，最终调用 `bind(...)` 方法启动服务。

*   **场景三：配置文件与 Nacos 配置**
    *   **描述**: 讲师切换到 `bootstrap.yml` 文件，展示了服务的端口配置（`port: 8192`）和 Spring Boot 的其他配置。随后，讲师切换到 Nacos 配置中心，展示了 `pd-netty-dev.yml` 的详细配置，包括 Kafka 的 `bootstrap-servers`、`producer` 和 `consumer` 参数，以及 Netty 的 `port` 参数，说明了如何通过配置中心统一管理服务配置。
