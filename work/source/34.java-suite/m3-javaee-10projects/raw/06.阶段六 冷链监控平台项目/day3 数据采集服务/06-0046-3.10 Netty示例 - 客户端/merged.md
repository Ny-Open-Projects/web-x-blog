# 3.10 Netty示例 - 客户端

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day3 数据采集服务
- 源文件：06.阶段六 冷链监控平台项目\day3 数据采集服务\3.10 Netty示例 - 客户端_【海量资源尽在 666java.com】.mp4
- 时长 16分23秒（音频 983s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来开发NetE实例程序的客户端程序那么我们从通过前面的介绍大家了解到了客户端的处理过程和我们服务器端的处理过程是类似的只不过两者之间有一点点差别而这种差别来讲的话比如我们的缓冲池也就是说我们的这种Event Loop Group
[00:24] 对于我们的客户端程序来讲的话它只有一个而服务器端的话它有两个这个也比较好理解那么上边的话是我们服务器端的程序一个是缓冲池是用来接收请求的另外一个缓冲池是用来处理我们接收到的请求那么但是对于客户端来讲的话它只是需要一个缓冲池来把我们的现成调用或者说调用我们服务器端的
[00:53] 端端口那么对于另外的差别在于我们的工厂类也就是说我们的启动的引导类对于客户端来讲的话它是一个NRO socket channel但是对于服务器端的话它是一个NRO server socket channel那对于启动类来讲的话我们的服务器端是属于我们一个叫做server的bootstrap那么对于
[01:22] 客户端的启动类是叫boostdrop那么他们的绑定方法也不一样而对于服务器端的绑定方法他一定要用了一个函数叫band而对于客户端来讲的话他是要连接服务器的端口所以他用了一个叫connect那么下面我们来开发我们的native客户端的一个程序那首先我们创建一个client类
[01:50] 这个client类的话我们首先需要定义我们的端口和我们的服务器的端口和我们的IP定义这两个变量我们private int我们的pot然后另外一个就是private string ip我们定义好了我们两个端口那么这两个一个端口一个ip我们在什么地方来给它初始化呢我们可以在我们的构造函数里边
[02:30] 比如说我们构造函数叫client那么client有两个参数一个叫pot或者一个叫ip一个叫ip一个叫pot那么我们在这构造函数里边可以设置我们的ip等于ip也传过来的参数ip我们的pot等于我们传输过来的pot那此时我们的ip呢也是一个是一个string类型的
[02:59] 那么我们的port呢是一个int类型的对吧这样的话我们构造函数就添加完了那下一步的话我们就需要开发我们的客户端的连接程序那么这个客户端的连接程序我们也可以直接使用一个啊构造一个函数public void然后这个函数的名字呢叫connect那么
[03:28] 在这里边我们开发native的客户端程序那么native客户端程序有几个步骤第一个步骤我们要定义我们的现成池这个现成池就是我们前面讲到的我的客户端向后台服务器来发送数据的这个现成池那第二个的话我们需要定义我们的启动程序或者启动类
[04:03] 那第三个的话我们需要配置我们的启动类或者启动的一些参数设置我们启动类的一些属性第四部分我们需要将我们的处理程序注册到我们的端口上或者注册到我们的这个channel上注册处理程序那第五步的话就是连接IP连接服务器
[04:46] 连接服务器的IP和端口那最后我们就可以把我们的服务器给启动起来了当然这个启动起来是在我们的我们的main函数里边启动客户端OK那我们来定义我们的现成池我们现成池是使用了eventevente loopgroup那么这个loopgroup我们可以理解为它就是一个worker或者说我们定义的名字叫worker等于我们new什么呢
[05:22] 我们有一个nroevent loop那么下一个的话我们要定义我们的启动类而这个启动类和我们的服务器端的其实是不一样的对吧服务器端的是一个叫做server bootstrap但是对于我们客户端呢我们使用的是bootstrap这个bootstrap我们需要对它来
[05:59] 创建一个实例想用一下我们使用的不是这个不是这个不是JDK的而我们要使用import class我们要使用我们的nativenative bootstrap比如我们看一下我们的native那么它在native类里边有个bootstrap实际上是这个这个bootstrap刚才它自动给我们引入了JDK的一个bootstrap
[06:35] 那下一步的话我们就要给这个boostdrop来设置我们的一些属性了比如说我们服务器端的属性第一个是要设置我们的group对吧那么对于客户端也是一样我们设置group这个group只有一个那第二个来讲的话我们可以设置我们的channel也就是说我们的通道这个通道的话和服务器端的也是不一样的服务器端是一个nro
[07:02] server socket channel那么在我们这里边我们就是一个nro的我们的socket socket channel那另外一个我们需要设置我们的连接是一个长连接也就是说我们用channeloption然后keepalive等于true那最后一个我们需要设置我们的handler而这个handler其实我们需要首先需要初始化一个channel
[07:37] Initialize而这个Initialize的参数或者是类型是属于一个Socket的一个Channel那么我们把这个类给它这个函数我们给它复写一下Generate的Override的一个Initial Channel那么在这里边我们是执行了第四步注册我们的处理程序那此时我们的处理程序可以使用Socket Channel的Pipeline
[08:11] 然后at last这个那么在这里边at last我们记得服务器端的话是我们自己开发了一个叫server handler对吧那么所以在这里边我们同样道理也需要开发一个client handler但是这个client handler我们现在还没有开发了那么我们可以先把这个client handler给它添加上client handler程序而client handler程序是需要extend我们的
[08:46] 一个类叫simple的channel inbound的handler然后它里面传递的参数是biter buffer那么我们再复写这个类的一些方法override有三个方法一个叫channel read一个叫我们的exception code那么还有一个方法我们需要对它进行一个复写
[09:27] 就是Channel的Active我们看一下ChannelActive对就这个这个方法那么我们的在这个方法里边我们需要填写一些我们的一些东西那首先的话我们需要在我们的我们的ChannelActive里边要添加我们的一些服务那么就此时我们需要往Channel里边发送数据
[09:56] 比如说我们可以发送数据是CTX那么这个CTX我们要write and flushwrite and flush是什么呢我们需要把我们缓冲区里边的数据拿过来也就是说要拷贝到缓冲区里边unpod.copy的buffer那此时我们就需要把我们的测试数据这个字符串然后发送过去了那此时我们需要把它转换成UTF-8格式
[10:32] charset util那么它的一个utf-8这种类型的OK这是一个最简单的一个那我们需要把我们的服务器客户端接着再往下写这个客户端来讲的话我们下一步需要绑定我们的一个端口和IP对吧我们要连接服务器我们就使用channel future这个future呢等于我们的bootstrap
[11:08] 他的一个connect那么connect什么呢就是连接连接我们的端口和我们的IP和端口那此时我们需要把我们的启动完了之后我们需要把我们的这个channel的这个future给它关闭掉ok那此时我们的客户端的start这个程序connection程序已经写好了那下一步的话我们就需要启动我们的程序而启动我们的程序我们
[11:43] 使用命方法我们在这里边启动我们的客户端又一个client那么client端口是127.0.0.1然后它的端口呢我们刚才在服务器端的端口是10010然后点击的一个connect此时我们的客户端程序就写完了那么写完了之后呢我们看一下它的一个核心它的核心和我们
[12:16] 整个的开发流程开发的步骤和我们的服务器端是一样的但是有差别在于第一我们服务客户端他的现成池只有一个只有一个worker这个现成池没有一个数据接收的他只有一个数据处理的那第二个来讲的话我们使用的启动引导类是一个boostdrop而server的端呢它是一个server的boostdrop那第三个点来讲的话我们用到的channel就是说端
[12:45] 通道这个通道呢是NRO socket channel而服务器端的开发程序里边它用到是NRO server的socket channel那另外的话就是我们把服务器启动之后呢我们需要注册我们处理程序这个处理程序我们需要扩展我们的一些方法或者继承我们的一些方法这个方法来讲的话是指我们simple channel的inbound handler这个类
[13:15] 我们要继承它继承它的时候要复写一个方法这个方法就是ChannelActive的一个方法我们在这个方法里边把我们的数据填写进来那下一步我们来看一看我们这个服务启动起来是一个什么样子那首先我们要启动我们的这个Server对吧我们要把我们的Server给启动起来Run那启动完了之后呢下一个我们就把我们的客户端给它启动起来再执行一下OK
[13:53] 那此时他报了一个错这个错大家需要注意一点我们看一看他报了个错然后报了错错的位置在哪呢在我们的server handler里边有一个channel rate我们点击进去看看到他那么这个方法是服务器的一个处理方法他会读取我们在channel里边就是通道里边的一缓冲池里边的数据而读取数据
[14:21] 它为什么会报这样的一个错误呢我们可以看到在这里边它有一个super的一个ray的channel ray的channel的一个ray的也就是说它的我们继承了是它负类里边的有一个叫channel inbound的handler的一个adapter那么负类里边也有一个channel ray的那么对于我们可以想象得到我们的数据缓冲池里边它的数据我们使用superchannel ray的时候已经读取了一遍了那么我们在
[14:51] 下面的时候又读取一遍这个时候数据就有问题了我们就读取不到了那么此时我们把它注视一下我们重新再启动一下看一看那么我们把客户端启动起来那么服务器端其实已经拿到了这个数据了对吧服务器端的数据就是我们在客户端里边我们发送的数据这个数据呢就是我们可以看一下我们在这儿我们用了一个CTX的
[15:21] read and flush的一个方法把我们的测试数据这个字符串然后拷贝到了我们的缓冲池里面那么服务器端它在对通道的缓冲池进行读取的时候就把数据拿到了然后把它打印出来然后我们就能看到了这就是我们整个的一个客户端的一个程序那么客户端程序来讲的话核心的逻辑刚才也提到了定义现成池定义引导类定义引导类启动类的一个属性然后连接服务器
[15:51] 同时我们要把服务器连接服务器同时我们把我们的客户端给它启动起来而在我们的启动类的属性里边有一个需要注册我们的处理程序这个处理程序我们需要扩展或者说继承我们的一个simple channel inbound handler这样的一个类而这个类的channel active方法我们需要在这个方法里边把我们的数据传递给我们服务器的一个端口这是我们整个的一个开发过程

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Netty 客户端的开发步骤，包括定义线程组、配置引导类、注册处理器和连接服务端。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Netty 客户端开发的步骤列表，包括定义线程组、定义启动类、初始化事件处理器、定义事件处理的处理逻辑、绑定端口、启动客户端。并对比了客户端与服务端的异同点，如 EventLoopGroup 个数、工具类、绑定方法等。

画面 2: 在 IntelliJ IDEA 中，客户端代码文件 Client.java 的开头部分，定义了私有成员变量 ip 和 port。

画面 3: 客户端构造函数中，将传入的 ip 和 port 赋值给成员变量。

画面 4: 在 Client 类中，定义了 connect() 方法，并添加了注释说明这是客户端的连接程序。

画面 5: 在 connect() 方法中，添加了注释说明步骤：1. 定义线程组；2. 定义后引导类；3. 配置后引导类的属性；4. 注册处理器程序；5. 连接服务。

画面 6: 在 connect() 方法中，创建了 Bootstrap 对象，并开始配置。

画面 7: 在 connect() 方法中，配置了 Bootstrap 的 group、channel、handler 等属性。

画面 8: 在 connect() 方法中，注册了 ChannelInitializer，并调用其 initChannel 方法。

画面 9: 在 ClientHandler.java 文件中，右键选择“Copy Reference”等操作。

画面 10: 在 ClientHandler.java 文件中，显示了 ChannelHandler 的方法列表，如 channelRead、channelInactive 等。

画面 11: 在 ClientHandler.java 文件中，重写了 channelActive 方法，用于处理连接成功后的操作。

画面 12: 在 ClientHandler.java 文件中，调用 bootstrap 的 connect 方法连接服务端，并获取 ChannelFuture。

画面 13: 在 Server.java 文件中，定义了 EventLoopGroup、ServerBootstrap，并配置了 channel、childHandler、option 等属性。

画面 14: 在 ClientHandler.java 文件中，重写了 channelRead0 方法，用于处理接收到的数据，并在控制台打印。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
2.3.2. 客户端处理步骤
1. 定义线程组
2. 定义启动类
3. 初始化事件处理器
4. 定义事件处理的处理逻辑
5. 绑定端口、启动客户端

Netty 客户端和服务器的开发过程非常相似，但也有差异：
相同点：
1. 都是 EventLoopGroup 和 NioEventLoopGroup。
2. 都有 group, channel, handler (ChannelInitializer) 方法。

不同点：
| 区别点           | 客户端             | 服务端             |
|------------------|--------------------|--------------------|
| EventLoopGroup个数 | 1                  | 2                  |
| 工具类           | NioSocketChannel   | NioServerSocketChannel |
| 启动类           | Bootstrap         | ServerBootstrap    |
| 绑定方法         | connect           | bind               |
```

画面 2:
```
package com.ithaima.netty.demo;

public class Client {
    //ip
    private int ip;
    private String port;
}
```

画面 3:
```
package com.ithaima.netty.demo;

public class Client {
    //ip
    private int ip;
    private String port;

    public Client(String ip, int port) {
        this.ip = ip;
        this.port = port;
    }
}
```

画面 4:
```
package com.ithaima.netty.demo;

public class Client {
    //ip
    private int ip;
    private String port;

    public Client(String ip, int port) {
        this.ip = ip;
        this.port = port;
    }

    /**
     * 客户端的连接程序
     */
    public void connect() {
        //1. 定义线程组
        //2. 定义后引导类
        //3. 配置后引导类的属性
        //4. 注册处理器程序
        //5. 连接服务
    }
}
```

画面 5:
```
package com.ithaima.netty.demo;

public class Client {
    //ip
    private int ip;
    private String port;

    public Client(String ip, int port) {
        this.ip = ip;
        this.port = port;
    }

    /**
     * 客户端的连接程序
     */
    public void connect() {
        //1. 定义线程组
        //2. 定义后引导类
        //3. 配置后引导类的属性
        //4. 注册处理器程序
        //5. 连接服务
    }
}
```

画面 6:
```
package com.ithaima.netty.demo;

public class Client {
    //ip
    private int ip;
    private String port;

    public Client(String ip, int port) {
        this.ip = ip;
        this.port = port;
    }

    /**
     * 客户端的连接程序
     */
    public void connect() {
        //1. 定义线程组
        //2. 定义后引导类
        //3. 配置后引导类的属性
        //4. 注册处理器程序
        //5. 连接服务
        EventLoopGroup worker = new NioEventLoopGroup();
        Bootstrap bootstrap = new Bootstrap();
    }
}
```

画面 7:
```
package com.ithaima.netty.demo;

public class Client {
    //ip
    private int ip;
    private String port;

    public Client(String ip, int port) {
        this.ip = ip;
        this.port = port;
    }

    /**
     * 客户端的连接程序
     */
    public void connect() {
        //1. 定义线程组
        //2. 定义后引导类
        //3. 配置后引导类的属性
        //4. 注册处理器程序
        //5. 连接服务
        EventLoopGroup worker = new NioEventLoopGroup();
        Bootstrap bootstrap = new Bootstrap();
        bootstrap.group(worker);
        bootstrap.channel(NioSocketChannel.class);
        bootstrap.handler(new ChannelInitializer<NioSocketChannel>() {
            @Override
            protected void initChannel(NioSocketChannel ch) throws Exception {
                ch.pipeline().addLast(new ClientHandler());
            }
        });
    }
}
```

画面 8:
```
package com.ithaima.netty.demo;

public class Client {
    //ip
    private int ip;
    private String port;

    public Client(String ip, int port) {
        this.ip = ip;
        this.port = port;
    }

    /**
     * 客户端的连接程序
     */
    public void connect() {
        //1. 定义线程组
        //2. 定义后引导类
        //3. 配置后引导类的属性
        //4. 注册处理器程序
        //5. 连接服务
        EventLoopGroup worker = new NioEventLoopGroup();
        Bootstrap bootstrap = new Bootstrap();
        bootstrap.group(worker);
        bootstrap.channel(NioSocketChannel.class);
        bootstrap.handler(new ChannelInitializer<NioSocketChannel>() {
            @Override
            protected void initChannel(NioSocketChannel ch) throws Exception {
                ch.pipeline().addLast(new ClientHandler());
            }
        });
    }
}
```

画面 9:
```
package com.ithaima.netty.demo;

import io.netty.channel.Channel;
import io.netty.channel.ChannelHandler;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.ChannelPromise;
import io.netty.channel.ChannelFuture;
import io.netty.channel.Channel;
import io.netty.channel.ChannelHandler;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.ChannelPromise;
import io.netty.channel.ChannelFuture;
import io.netty.channel.Channel;
import io.netty.channel.ChannelHandler;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.ChannelPromise;
import io.netty.channel.ChannelFuture;
import io.netty.channel.Channel;
import io.netty.channel.ChannelHandler;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.ChannelPromise;
import io.netty.channel.ChannelFuture;
import io.netty.channel.Channel;
import io.netty.channel.ChannelHandler;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.ChannelPromise;
import io.netty.channel.ChannelFuture;
import io.netty.channel.Channel;
import io.netty.channel.ChannelHandler;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.ChannelInitializer;
import

