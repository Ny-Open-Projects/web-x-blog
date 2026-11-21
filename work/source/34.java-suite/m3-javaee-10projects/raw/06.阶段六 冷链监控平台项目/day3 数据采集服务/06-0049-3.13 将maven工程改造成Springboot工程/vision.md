# 画面线理解：3.13 将maven工程改造成Springboot工程

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day3 数据采集服务
- 源文件：06.阶段六 冷链监控平台项目\day3 数据采集服务\3.13 将maven工程改造成Springboot工程_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 01:11, 01:39, 02:41, 03:50, 05:11, 06:09, 06:47, 07:26, 08:03, 08:47, 09:30, 10:08, 12:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:09:22

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
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.kafka</groupId>
    <artifactId>spring-kafka</artifactId>
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
bash-4.4# /opt/kafka_2.12-2.2.1/bin/kafka-topics.sh --zookeeper 172.17.0.143:2101 --list
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
DiscoveryClient: Getting all instance registry info from the eureka server
: The response code is 200
DiscoveryClient: Starting heartbeat executor: renew interval is 30
DiscoveryClient: InstanceInfoReplicator onDemand update allowed rate per min is 4
DiscoveryClient: DiscoveryClient_COLD-NETTY/192.168.145.138:8188 registering service...
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
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.kafka</groupId>
    <artifactId>spring-kafka</artifactId>
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
DiscoveryClient: Getting all instance registry info from the eureka server
: The response code is 200
DiscoveryClient: Starting heartbeat executor: renew interval is 30
DiscoveryClient: InstanceInfoReplicator onDemand update allowed rate per min is 4
DiscoveryClient: DiscoveryClient_COLD-NETTY/192.168.145.138:8188 registering service...
DiscoveryClient: Saw local status change event StatusChangeEvent [timestamp=1576476899798, current=UP, previous=STARTING]
Server: Started Server in 5.773 seconds (JVM running for 5.773)
DiscoveryClient_COLD-NETTY/192.168.145.138:8188 - registration status: 204
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
（
