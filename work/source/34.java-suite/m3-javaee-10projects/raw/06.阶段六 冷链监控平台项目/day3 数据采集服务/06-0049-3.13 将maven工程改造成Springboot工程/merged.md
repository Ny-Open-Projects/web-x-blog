# 3.13 将maven工程改造成Springboot工程

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day3 数据采集服务
- 源文件：06.阶段六 冷链监控平台项目\day3 数据采集服务\3.13 将maven工程改造成Springboot工程_【海量资源尽在 666java.com】.mp4
- 时长 12分29秒（音频 749s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好前面我们给大家介绍了Neted网络编程然后包括我们的整个Neted它的架构设计开发过程那么我们还通过一个Neted的客户端和服务器端的一个示例程序来给大家演示了这个过程那么整个工程呢它其实是一个普通的一个Java的工程而整个项目呢也是一个普通的Maven项目那所以我们
[00:26] 但是我们希望我们整个工程是一个SpinBoot的工程为什么是一个SpinBoot的工程呢因为我们可以把一些注解把一些我们的一些实体bin在我们的SpinBoot容器启动的时候给它添加进来那么现在我们给大家演示一下如何把当前的这个工程就是Java的Maven工程给它改造成一个SpinBoot的一个工程那首先第一点的话我们需要引入一些
[00:56] Spring Boot的一个坐标那这种Spring Boot的坐标我不在这手中给大家敲了大家直接把我们的POM文件给它拷贝进去其实就OK了那紧接着的话我们需要添加一些Application的就是添加一个配置文件这个配置文件叫Application.yaml文件而这个yaml文件
[01:20] 它的起的作用就是我们Spring Boot容器在启动的时候的一些属性而这些属性包括我们Server的Port就是Server的端口8186或者是8186那么另外的话是我们当前这个工程的名字Spring.Application.Name这个Name我们可以叫做code-neti然后我们的活跃的或者说是生效的
[01:51] 配置文件是什么呢当然我可以把所有的配置文件全都在这一个文件里边来写但是我如何来区分我的我的测试环境或者是我的开发环境或者我们的生产环境呢那么我每次做的时候我只是我需要把里边的各个属性全部都更改一下但是我如果用我们的profile比如说active我们就可以直接更改这一个参数就OK了
[02:21] 那我下一步的话我需要添加一个叫applicationapplication-dv.yaml文件那同样道理如果我要是想更改其他的呢就是说我们的test的文件我们就可以把它更改成tst文件了对吧那此时的时候如果我要想切换到测试环境里面的配置我只需要在我的这个profile active改成tst了如果生产环境就是application-
[02:52] prod.yaml我在这儿的时候这个地方我就可以写成这prod那我们添加完了这个这个配置我们可以添加什么配置呢比如说我们添加Urica的一个配置中心呢Urica的配置或者我们可以添加我们的比如说像这个数据库数据库的配置对吧我现在需要第一个需要加的是什么
[03:24] 我们要加我们的Urica的一个配置而Urica的配置我们开始的时候已经把我们Urica配置Urica服务的中心已经启动起来了它就在我们的服务器端我们给大家看一下服务器端的一个Urica的服务的中心Urica这个Urica已经启动了那么我们在我们当前的这个工程里面我们就可以直接配置它了那么我的配置是Urica.client.
[04:11] Service-url.url然后有一个叫default run这个地方的话我们就要配置我们的Ureq服务注册中心了172.17.0.143然后呢它的端口是8001然后UreqOK这Ureq的服务注册中心的配置我们就给它加上了
[04:47] 下一步的话我们要把我们这个主程序就是我们这个server要把它改造成一个Spring Boot的一个应用我们需要添加第一步我们需要添加一个叫做注解而这个注解的话是Spring Boot的application然后我们还需要添加另外一个注解就是我们的Ulika客户端那我添加完了这个Spring Boot application的时候我当前的这个工程或者当前的这个构造函数
[05:20] 它就有问题了那这个是什么意思呢我们的Spring Boot的application的注册构造函数它不能是一个有参的构造函数那我们把它删掉删掉了之后我们端口怎么办呢那我当前的比如说我当前的这个端口是10010指的是我当前native服务器的一个端口那么我们可以固定下来当然了我也可以在配置文件里面写我直接把它在这个地方直接用那我
[05:50] 把我们的端口给它设置好之后那下一步的时候我们需要更改什么呢下一步它本身现在还是一个普通的加码工程那我下一步需要把我们的这个main函数给它改造一下比如我在这儿我给它填写springobligation.run而这个run的话需要有参数server.class还有再加一个参数args那此时它就是一个Spring Boot的工程了
[06:22] 但是我们希望在Spring Boot启动的时候把我们的native服务器就是10010这个端口给它启动起来但现在的情况下我们的run函数其实是没有用的它就是一个普通的函数它没有用那在这种情况我们需要做的一件事情就是把我们这个server实现了一个接口implement什么接口呢command run
[06:50] command run run的它的这个接口的主要的作用就在于我们sprint boot启动的时候如果我们想要启动编辑在启动的过程中执行其他的其他的一些方法或者其他的一些其他一些代码那么我们可以实现这个接口那实现这个接口的话需要我们复写一个run的一个方法我们generate override的一个message然后执行一个runOK
[07:19] 那么这个run的方法和我们可以看看我们这个run的方法那我可以把整个的我们的代码拷到里面去对不对或者我现在的话我直接就把我们的我们的方法的名字给去掉OK那此时就可以了对不对此时的时候我们的是一个sminboot的工程那么它启动的时候它要执行我们的native服务器的一些代码那我们来执行一下看一看我们执行一下OK好报错了
[08:04] failed to执行这个failed to执行这个的话是端口已经被端口被占用了那我们重新把端口给重新把服务给的停掉我们把另外一个服务的话它是把我们端口已经占用了那我现在在执行OK那此时我们的这个工程就启动起来了8186那么我们看一下我们的我们的这个
[08:37] 10010localhost10010也是启动起来的那我现在因为我们把我们的原来的工程是一个普通的普通的一个加密工程普通的一个native服务器那么我们的客户端呢我们可以再把它执行起来客户端原来的当时的一个作用或者当时的一个需求是我们
[09:09] 由客户端发送我们的数据到我们的服务器端那么现在我们看看能不能收到服务器端能不能收到我们客户端发来的数据OK我们已经收到了那么在这样的话我们其实就能把我们的整个工程给它由一个Java的Mainware工程改造成一个SpinBoot的工程那么这个过程呢第一步我们需要添加我们的Pump文件引入我们的SpinCloud的SpinBoot的一些坐标
[09:36] 那第二步我们需要添加我们的application的yaml文件还有是我们application的这个dv的文件那么这个yaml文件大家需要注意的一点是我们的比如说我们要想加一个什么呢我们要想加一个加一个注解注解我们要想添加注解的时候我们不能使用双斜杠我们要使用警号那接着的话我们在我们的这个主程序里边
[10:12] 要进行改造组成一类别改造的一是我们要添加spin boot的一个注解第二步我们要把main函数更改成我们的run函数就是spin application的run那第三步的话因为我们想在我们spin boot启动的时候执行我们的native程序那么所以我们当前这个工程要当前这个类要实现我们的command
[10:42] lan run的一个方法lan的一个接口而这个接口的话我们需要复写一个run的方法这个run的方法里边就是我们自己的这个额外想执行的程序这就是我们要把一个普通的工程普通的一个加挂工程改造成一个spin boot工程的一个过程那么我们再稍微多说一句
[11:06] 就是我们当前的工程一般情况下如果我们开发一个工程就是spin boot的工程那么开发的过程呢是正常的过程应该是什么呢应该是我们创建一个类而这个类呢我们开始的时候就需要把我们的at spin boot的application给添加上然后呢再添加main函数main函数里边添加我们的这个spin application的run这个方法然后再执行我们的其他的一些开发我们其他的代码比如说implement
[11:36] 但是我们在讲解的过程中是从先开发一个Java工程开发Java工程实现了NetE然后再把NetE把Java工程改造成我们的SpinBoot的一个工程我们通过这种方式来给大家讲解的那么这种方式讲解的主要的目的是希望大家能够明白我们的第一SpinBootSpin的这个NetENetE它的核心的东西是什么第二
[12:05] 我的spin boot的东西是什么需要我想把在这个过程中给大家分离出来这是我们现在这个讲解方式的一个原因好下一步的话我们给大家就会给大家讲解我们当前的server接收到了我们的数据之后我要如何来处理它

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Boot 和 Netty 构建一个支持服务发现（Eureka）的网络服务器，并配置不同环境的配置文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，选中 pom.xml，编辑器中显示 Server.java 的 Netty 服务端代码，注释说明“开启端口，接收数据”，定义了 boss 和 worker 线程组，创建 ServerBootstrap。
画面2：在项目中右键选择“New” -> “XML File”，创建 application.yml 文件，编辑器中显示 Spring Cloud 相关依赖配置，如 spring-cloud.version、mybatis-plus.version、fastjson.version。
画面3：编辑器中显示 application.yml 文件内容，配置 server.port 为 8188。
画面4：在 resources 目录下右键，选择“Copy File”，将 application.yml 复制为 application-dev.yml。
画面5：切换到终端，连接到远程服务器（IP 172.17.0.143），执行 Kafka 主题列表命令。
画面6：在 IDEA 中，选中 Server.java，查看导入的包，包括 Spring Boot 和 Netty 相关包。
画面7：在 Server.java 中，将类定义为 implements CommandLineRunner，准备在启动后执行自定义逻辑。
画面8：在 Server.java 中，将 main 方法改为 public static void main(String[] args) throws Exception，并添加 SpringApplication.run(Server.class, args)。
画面9：在 Server.java 中，将 main 方法改为 public static void main(String[] args) throws Exception，并添加 SpringApplication.run(Server.class, args)。
画面10：在 Server.java 中，选中并高亮显示 ServerBootstrap 的初始化代码，包括设置线程组、通道类型和 childHandler。
画面11：在 IDEA 的 Run 窗口中，显示服务启动日志，包括 Eureka 客户端注册成功，服务端启动成功，端口为 8188。
画面12：在 IDEA 中，选中 pom.xml，编辑器中显示 Spring Cloud 和 Netty 的依赖配置。
画面13：在 Server.java 中，选中并高亮显示 childHandler 的代码，包括添加 ServerHandler 和设置 ChannelOption。
画面14：在 IDEA 的 Run 窗口中，显示服务启动日志，包括 Eureka 客户端注册成功，服务端启动成功，端口为 8188。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public class Server {
    private int port;
    public Server(int port) {
        this.port = port;
    }
    public void run() throws Exception{
        //1. 定义线程组
        EventLoopGroup boss = new NioEventLoopGroup();
        //定义具体处理工作的线程组
        EventLoopGroup worker = new NioEventLoopGroup();
        //2. 定义启动引导类
        ServerBootstrap bootstrap = new ServerBootstrap();
        //3. 设置启动的属性，绑定处理程序
        bootstrap.group(boss, worker)
                .channel(NioServerSocketChannel.class)
                .childHandler(new ChannelInitializer<SocketChannel>() {
```

画面2：
```xml
<properties>
    <java.version>1.8</java.version>
    <spring-cloud.version>Greenwich.SR1</spring-cloud.version>
    <lombok.version>1.18.4</lombok.version>
    <mybatis-plus.version>3.0.7.1</mybatis-plus.version>
    <fastjson.version>1.2.47</fastjson.version>
</properties>

<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.Kafka</groupId>
    <artifactId>spring-Kafka</artifactId>
</dependency>

<dependency>
    <groupId>io.netty</groupId>
    <artifactId>netty-all</artifactId>
    <version>4.1.10.Final</version>
</dependency>
```

画面3：
```yaml
server:
  port: 8188
```

画面4：
（无代码或配置，仅显示复制文件对话框）

画面5：
```bash
bash-4.4# /opt/kafka_2.12-2.2.1/bin/Kafka-topics.sh --ZooKeeper 172.17.0.143:2101 --list
```

画面6：
（无代码或配置，仅显示导入包列表）

画面7：
```java
public class Server implements CommandLineRunner {
    public static void main(String[] args) throws Exception{
        SpringApplication.run(Server.class, args);
    }
    @Override
    public void run(String... args) throws Exception {
    }
    public void run() throws Exception{
```

画面8：
```java
public class Server implements CommandLineRunner {
    public static void main(String[] args) throws Exception{
        SpringApplication.run(Server.class, args);
    }
    @Override
    public void run(String... args) throws Exception {
    }
    public void run() throws Exception{
```

画面9：
```java
public class Server implements CommandLineRunner {
    public static void main(String[] args) throws Exception{
        SpringApplication.run(Server.class, args);
    }
    @Override
    public void run(String... args) throws Exception {
    }
    public void run() throws Exception{
```

画面10：
```java
//1. 定义线程组
EventLoopGroup boss = new NioEventLoopGroup();
//定义具体处理工作的线程组
EventLoopGroup worker = new NioEventLoopGroup();
//2. 定义启动引导类
ServerBootstrap bootstrap = new ServerBootstrap();
//3. 设置启动的属性，绑定处理程序
bootstrap.group(boss, worker)
        .channel(NioServerSocketChannel.class)
        .childHandler(new ChannelInitializer<SocketChannel>() {
```

画面11：
```text
DiscoveryClient: Getting all instance registry info from the Eureka server
: The response code is 200
DiscoveryClient: Starting heartbeat executor: renew interval is 30
DiscoveryClient: InstanceInfoReplicator onDemand update allowed rate per min is 4
DiscoveryClient: DiscoveryClient_COLD-NETTY/192.168.145.138:8188 registering Service...
DiscoveryClient: Saw local status change event StatusChangeEvent [timestamp=1576476899798, current=UP, previous=STARTING]
Server: Started Server in 5.773 seconds (JVM running for 5.773)
DiscoveryClient_COLD-NETTY/192.168.145.138:8188 - registration status: 204
```

画面12：
```xml
<properties>
    <java.version>1.8</java.version>
    <spring-cloud.version>Greenwich.SR1</spring-cloud.version>
    <lombok.version>1.18.4</lombok.version>
    <mybatis-plus.version>3.0.7.1</mybatis-plus.version>
    <fastjson.version>1.2.47</fastjson.version>
</properties>

<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.Kafka</groupId>
    <artifactId>spring-Kafka</artifactId>
</dependency>

<dependency>
    <groupId>io.netty</groupId>
    <artifactId>netty-all</artifactId>
    <version>4.1.10.Final</version>
</dependency>
```

画面13：
```java
@Override
protected void initChannel(SocketChannel socketChannel) throws Exception {
    //注册处理程序
    socketChannel.pipeline().addLast(new ServerHandler());
    //设置通道选项
    socketChannel.config().setOption(ChannelOption.SO_BACKLOG, 128);
    socketChannel.config().setOption(ChannelOption.SO_KEEPALIVE, true);
}
```

画面14：
```text
DiscoveryClient: Getting all instance registry info from the Eureka server
: The response code is 200
DiscoveryClient: Starting heartbeat executor: renew interval is 30
DiscoveryClient: InstanceInfoReplicator onDemand update allowed rate per min is 4
DiscoveryClient: DiscoveryClient_COLD-NETTY/192.168.145.138:8188 registering Service...
DiscoveryClient: Saw local status change event StatusChangeEvent [timestamp=1576476899798, current=UP, previous=STARTING]
Server: Started Server in 5.773 seconds (JVM running for 5.773)
DiscoveryClient_COLD-NETTY/192.168.145.138:8188 - registration status: 204
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
（

