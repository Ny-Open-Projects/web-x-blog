# 3.9 Netty示例 - 服务端

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day3 数据采集服务
- 源文件：06.阶段六 冷链监控平台项目\day3 数据采集服务\3.9 Netty示例 - 服务端_【海量资源尽在 666java.com】.mp4
- 时长 17分17秒（音频 1038s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好前面我们介绍了NetEdit的网络编程的一个原理然后呢介绍了NetEdit它的主要的一些特点啊适用的一些场景然后紧接着给大家介绍了NetEdit的架构那么这种架构主要包括一个RO模型一个现成处理模型而RO模型呢决定如何来接收数据那么对于现成处理模型主要是决定我们如何来处理我们的一个逻辑
[00:30] 那对于NAT来讲的话它的一个RO模型适用了是多路的一个附用模型而对于现成处理模型呢NAT使用了一个主从的然后扩展的一个reactor模型那紧接着给大家介绍了我们的核心类和我们相关的一些开发步骤这个开发步骤包括我们服务器端的开发客户端的开发那么下面我们给大家来介绍一下如何开发一个我们的NAT服务
[00:58] 那首先我们创建了我们的这个Maven的工程这个Maven工程创建的步骤也比较简单一些我们直接打开创建工程的一个泡沫键添加native的一个坐标那首先我们要添加definitie然后添加native的坐标definitie它的group id叫ro.native那么它的artifact id实际上就是native-o然后我们
[01:33] 添加nety它的一个rosin版本4.1.10.final这样的话我们就把我们nety它的一个工程的POM文件里边给添加完了那紧接着我们可以看一看我们的POM文件里边引用的nety它的依赖的这个包其实就叫nety-o 4.1.0.10.final然后这个包里边有boostdrop
[02:05] 有我们的channel handler大家看的是不是比较熟悉这个是我们在核心类里边给大家介绍的我们一个native服务器或者一个native客户端它拥有的一些类这个类来讲的话比如说叫server的boostdrop一个叫做我们的boostdrop对吧客户端的和服务器端的还有我们的channelchannel里边会用到了一些channel的一个类还有我们的handler
[02:34] 这些都是我们在核心类里边给大家介绍的那下一步的话我们可以开发我们的server我们的服务器端com.it黑马.neti.demo.server这个类的名字就叫做server而这个server我们所要做的事情就是开启端口接收数据
[03:10] 这是我们native的服务器端要做的事情那首先我们要定义我们的端口private int pot这是我们的端口的类型变量变量名字我们构造函数里边我们可以直接把端口给传入进来然后我们在这里边写this.pot我们等于pot这个时候我们就设置了我们的端口了对吧
[03:41] 我们创建一个server的实例的时候我们可以把端口传入进来那下面的话我们就要开发我们的启动程序而这个启动程序就是我们native服务器端的一个核心程序我们定义一个public void run当然我们可以用run或者说用starter或者其他的你想要的一个任何一个名字都可以但是一般情况下我们建议是使用这个run或者用starter这两个它是指我们
[04:11] 服务器的启动时候那紧接着我们看一下我们的如何来开发我们服务器端这是核心的那第一部分来讲的话是我要定义我的定义我的现成组而这个现成组对于服务器端是有两个对吧对于客户端来讲的话是有一个现成组那第二第二步的话我们是需要定义启动的启动引导类第三步的话是我们要
[04:45] 设置我们启动类的属性我们要把我们的channel把我们的handler和它进行匹配上那第四步的话是我们要设置设置什么呢我们要设置我们的端口或者说叫绑定我们端口第五步我们要启动服务当然第四步的绑定端口
[05:29] 之前还有一个是启动设置属性的时候我们还需要设置绑定我们的处理程序或者处理逻辑OK那么我们来开发一下首先第一步第一个我们要定义我们的现成组或者现成池这现成池里面有两个那一个现成池是要定义定义我们的接收请求的
[06:02] 现成组叫event loop group我们把它设置成boss等于new nro event loop group这是我们的接收请求的而接收过来请求之后我们要怎么办呢我们要把它交给具体的处理也就是说我们在原来讲的这张图里边我第一个我在这一块servo我要accept的时候我用一个现成池这个现成池里边可以接收客户端的一些请求
[06:37] 那紧接着我要把请求扔给具体处理逻辑的一个现成词是吧那在这里边我们要定义具体处理工作的现成组也是event loop groupworker等于new nroevent loop groupOK我们定义好了我们的现成组了那下一步我们要定义我们的启动类
[07:11] 或者叫启动的辅助的引导类那么这个启动类有两个对吧我们刚才在我们的jar 包里边也看到了就是我们的boostdrop这个boostdrop一个叫做boostdrop一个叫serverboostdrop所以对于我们的服务器端它是一个server的一个boostdrop那么我们等于new server的boostdrop那下面的话我们就需要
[07:42] 来设置我们boostdrop它的一些属性绑定我们的处理程序了那么我们设置属性我们首先要设置它的一个group等于什么呢等于两个一个是我们的boost一个是我们的worker对吧我们把我们的group给它绑定上了就是处理程序给它绑定上了那紧接着我们要设置我们的channel这个channel是我们知道我们在原来的时候介绍channel它的类型就是它通道类型有很多个
[08:16] 那么有一个channel就是叫做我们的channel socket的一个channelnro的nro的一个对nro的一个nro server socket channel对这个类我们要也就是说我们channel的类型是nro server socket channel那下一个我们需要定义要初始化我们的channel
[08:52] child channelchild handler等于new channel initialize然后呢它的类型是socket的channel那么在这里边我们需要初始化一个或者说要复写一个方法就是我们的initial channel的这个方法在初始化的时候我们需要在这里边把我们的handler给注册上就是绑定我们的处理程序或者要注册处理
[09:30] 程序或者叫绑定处理程序我们使用socket的channel就是这个socket的channel它的一个fiblet然后再添加at last的方法执行一个我们的处理程序那这个处理程序它需要扩展我们的channel inboundhandler的一个adapter所以我们需要新开发一个server的一个类
[10:02] 或者新开发一个server的handler而这个server handler呢我们要extend我们的channel inbound handleradapterok就是这个类我们在这个类里边要扩展我们的一些或者说要复写我们的一些属性一些方法一个方法叫做channel read一个方法叫channel readcomplete然后还有第三个方法
[10:36] 我们只需要把这三个方法复写就OK了就是exception, caught当我的读取出现异常的时候我要怎么做那么这三个方法一个是我们要读取然后是读取完成时候要怎么做然后第三个就是出现异常时候怎么做那么回到我们的这个server的这个类里边那么我们看到刚才我们说要注册或者绑定我们处理程序里边我们需要在这个地方
[11:07] 添加一个new server看到了OK这个时候我们已经把我们的处理程序和我们的启动类的引导程序关联起来了那下一步我们再添加我们这个引导程序的其他的属性那一个属性就是我们channel它的对列的长度就是channel它对接的对列它的长度channel option的backlog
[11:38] 我们要设置成128可以设置成也可以设置成其他的256或者其他的都行那么我们在下一个属性是channel的一个child的一个option那么这个option呢我们使用channeloption的一个tplib也就是说保持一个长连接OK此时我们就把我们的启动类它的一个属性和我们的
[12:08] 处理程序给绑定起来了啊在这里边我就忘了一个C号啊那我们下一步的话实际上就是需要绑定我们的端口绑定端口的方法try然后我们在这里边用channelchannel的futurechannel future定义一个channel future类型那么它等于postdrop的band我们对于服务器端的开发它其实是用band来绑定端口对吧
[12:42] 我们也绑定了绑定我们的一个port然后再执行dechronize的一个方法那么第二个来讲的话我们要使用f.channel就是我们channel future把它进行一个关闭我们要把整个channel的对待进行关闭关闭完了之后呢我们要执行一个同步ok此时我们绑定了端口那么在我们在funnel里边我们实际上要把我们的
[13:14] Boss就是资源我们的线程池或者线程组要对它进行关闭Worker的一个线程池我们也要对它进行一个关闭OK此时我们已经把我们的这个绑定端口也添加完了这个时候我们的run函数已经填写好了那下一步的话我们就需要启动我们的程序了那么这个启动程序呢我们放在我们的命方法里边来做
[13:49] 在这里我们直接使用new server10010点runok此时我们就把我们的程序服务给启动起来了那但是在这里有一个问题啊哦抱错抱错我们是需要对于这个run我们要抛出一个异常这个地方我们的异常也需要提交上去ok此时没问题了那我们
[14:27] 来看一下我们的这个程序首先定义线程组对于server端的话是有两个线程组然后定义我们的引导类就server.boost.draft那么紧接着我们对于引导类的一些属性的一些设置然后绑定我们的server handler也就是说我们整个处理程序我们要把处理程序注册到我们的通道上那第四步的话就是绑定我们的端口
[14:53] 最后就是在我们的函数里面执行此时我们的server就可以启动起来了但是这中间有一个小问题就是我们的server handler并没有做任何的一个处理那么下面我们来做一些这个对于server handler的一个处理这个简单处理来讲也非常的一个简单那么首先我们要用batter buffer来读取我们的msg就是数据那这个时候我需要先把它做一个类型转化
[15:27] 把这buffer然后我们再把这个读取到的数据给它打印出来图物端接收到的数据加上buffer.toString而这个toString呢我需要把它转换成UTF-8格式的XsetUtil.UTF-8OK
[16:07] 那这个时候我们在执行我们的上下文的write好这个时候我们对于channel或者对于通道的读取程序就写完了简单的来讲的话我们就是要打印接收到的数据那第二步的话是我们在读取完了之后要怎么办我读取完了之后我们要对ctx就是上下文我对它要进行一个flash
[16:37] 这个上下文指的是我们通道处理程序的一个上下文而不是说我们这个比如说我们有obligation context或者说其他的context那么在现在的这个地方就是我们的这个程序里边就是我们的channel的一个except那紧接着我们在callexception的一个call就是出现异常的时候我们怎么办呢我们要把我们的channel上下文的处理程序给它close掉好
[17:09] 此时我们的服务器端啊就完全开发完了这是我们开发整个啊native服务器端的一个过程

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Netty 框架编写一个简单的 TCP 服务器，包括创建 EventLoopGroup、ServerBootstrap、设置 ChannelHandler 和绑定端口等核心步骤。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 内容，讲解 Netty 的 IO 模型和传统 HTTP 服务器的处理流程。
画面 2: 在 IntelliJ IDEA 中，展示 `pom.xml` 文件内容，添加 Netty 依赖。
画面 3: 编辑 `Server.java` 文件，定义类和构造函数。
画面 4: 在 `Server.java` 中添加注释，说明程序结构。
画面 5: 在 `Server.java` 中添加注释，说明程序结构。
画面 6: 在 `Server.java` 中导入 `io.netty.channel.nio.NioEventLoopGroup`。
画面 7: 在 `Server.java` 中创建 `NioEventLoopGroup` 实例。
画面 8: 在 `Server.java` 中创建 `ServerBootstrap` 实例。
画面 9: 在 `ServerHandler.java` 中定义 `ServerHandler` 类。
画面 10: 在 `ServerHandler.java` 中定义 `initChannel` 方法。
画面 11: 在 `ServerHandler.java` 中添加 `ChannelOption` 配置。
画面 12: 在 `ServerHandler.java` 中绑定端口并启动服务。
画面 13: 在 `ServerHandler.java` 中实现 `channelRead` 方法，打印接收到的数据。
画面 14: 在 `ServerHandler.java` 中实现 `channelReadComplete` 和 `exceptionCaught` 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2 的 `pom.xml` 内容：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.itheima</groupId>
    <artifactId>netty-demo</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <dependency>
            <groupId>io.netty</groupId>
            <artifactId>netty-all</artifactId>
            <version>4.1.10.Final</version>
        </dependency>
    </dependencies>
</project>
```

画面 3 的 `Server.java` 开头：
```java
package com.itheima.netty.demo;

import java.net.InetSocketAddress;

public class Server {
    public Server(int port) {
        this.port = port;
    }

    public void run() {
    }
}
```

画面 6 的 `Server.java` 代码：
```java
import io.netty.channel.nio.NioEventLoopGroup;
```

画面 7 的 `Server.java` 代码：
```java
public void run() {
    //1. 定义线程组
    //定义接收请求的线程组
    EventLoopGroup boss = new NioEventLoopGroup();
    //定义具体处理工作的线程组
    EventLoopGroup worker = new NioEventLoopGroup();
}
```

画面 8 的 `Server.java` 代码：
```java
public void run() {
    //1. 定义线程组
    //定义接收请求的线程组
    EventLoopGroup boss = new NioEventLoopGroup();
    //定义具体处理工作的线程组
    EventLoopGroup worker = new NioEventLoopGroup();
    //2. 定义启动引导类
    ServerBootstrap bootstrap = new ServerBootstrap();
}
```

画面 9 的 `ServerHandler.java` 代码：
```java
public class ServerHandler extends ChannelInboundHandlerAdapter {
    @Override
    protected void initChannel(SocketChannel socketChannel) throws Exception {
        socketChannel.pipeline().addLast(new ServerHandler());
    }
}
```

画面 10 的 `ServerHandler.java` 代码：
```java
@Override
protected void initChannel(SocketChannel socketChannel) throws Exception {
    //注册处理器
    socketChannel.pipeline().addLast(new ServerHandler());
}
```

画面 11 的 `ServerHandler.java` 代码：
```java
@Override
protected void initChannel(SocketChannel socketChannel) throws Exception {
    //注册处理器
    socketChannel.pipeline().addLast(new ServerHandler());
    //设置选项
    channel.option(ChannelOption.SO_BACKLOG, value: 128);
    channel.option(ChannelOption.SO_KEEPALIVE, value: true);
}
```

画面 12 的 `ServerHandler.java` 代码：
```java
@Override
protected void initChannel(SocketChannel socketChannel) throws Exception {
    //注册处理器
    socketChannel.pipeline().addLast(new ServerHandler());
    //设置选项
    channel.option(ChannelOption.SO_BACKLOG, value: 128);
    channel.option(ChannelOption.SO_KEEPALIVE, value: true);
}
//4. 绑定端口
try {
    ChannelFuture f = bootstrap.bind(port).sync();
    f.channel().closeFuture().sync()
} finally {
    boss.shutdownGracefully();
    worker.shutdownGracefully();
}
```

画面 13 的 `ServerHandler.java` 代码：
```java
import io.netty.channel.ChannelHandler;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;

public class ServerHandler extends ChannelInboundHandlerAdapter {
    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        super.channelRead(ctx, msg);
        ByteBuf buf = (ByteBuf) msg;
        System.out.println("服务端接收到的数据：" + buf.toString(Chinese));
    }

    @Override
    public void channelReadComplete(ChannelHandlerContext ctx) throws Exception {
        super.channelReadComplete(ctx);
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
        super.exceptionCaught(ctx, cause);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 的 PPT 内容：
- 标题：Netty 介绍
- 子标题：Netty 介绍
- 内容：
  1. 创建一个 ServerSocket，监听并绑定一个端口
  2. 一系列客户端来请求这个端口
  3. 服务器端使用 Accept，获得一个来自客户端的 Socket 连接对象
  4. 启动一个线程处理连接
  5. 读 Socket，得到字节流
  6. 解码协议，得到 HTTP 请求对象
  7. 处理 HTTP 请求，得到一个结果，封装成一个 HTTPResponse 对象
  8. 编码响应，将结果分类为字节流
  9. 写 Socket，将字节流发给客户端
  10. 继续循环步骤 3

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

