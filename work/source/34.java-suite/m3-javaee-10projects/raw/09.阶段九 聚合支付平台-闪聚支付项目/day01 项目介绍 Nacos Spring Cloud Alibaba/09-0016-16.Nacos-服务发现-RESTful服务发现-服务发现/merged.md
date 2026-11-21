# 16.Nacos-服务发现-RESTful服务发现-服务发现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\16.Nacos-服务发现-RESTful服务发现-服务发现【海量资源尽在 666java.com】.mp4
- 时长 9分7秒（音频 547s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好接下来呢我们来实现RESTful服务发现这一块那么前面我们完成了服务注册下边我们做服务发现那么服务发现应该是在提供方还是消费方大家回答提供方是不是把自己注册到服务注册中心了然后呢服务发现是不是叫消费方从服务发现中心来获取服务列表所以我们现在要做的是服务消费方那服务消费方各位他是不是也需要一个服务发现的客户端
[00:31] 对你需要把原来我们加到服务提供方的这个Netflix的这个discovery这个客户端呢把它贴到消费方这个碰瓷文件中然后贴进来之后呢我们接下来要想那你服务发现怎么发现呀你是不是需要获取服务的信息呀对不对原来我们是不是通过硬编码通过配置文件的方式
[01:01] 然后呢在我们的程序当中你看到吗是不是就拼装这个对方提供方的URL然后进调用对吧而现在我们要做一件事对我们要做什么事啊我们要做一件智能发现服务的这么一个流程怎么智能啊首先你要指定什么呀服务名就是你要发现的服务名嘛你要发现哪个服务
[01:31] 行不行我们比如说我们指定一个叫Service id这个名字那么我们要发现哪个服务我们要发现刚才我们注册进去的这个服务叫necos-RESTful provider贴进去可以吧那你服务发现那你怎么发现我们说了你发现服务的话你需要做一件事
[01:57] 这个事呢就是我们说的要能够从服务列表当中干嘛去通过负载均衡获取一个地址理解吗所以这里边我们需要通过框架给我们提供的一个叫做loadabundanceclient这么一个对象
[02:20] 那这个到底是一个什么东西呢一会儿我会详细讲现在呢你只要知道我们要做的一件事是要通过什么通过负载均衡来找到来发现地址那么有人说老师这个到底是一个什么样的流程呢那负载均衡它怎么样把这个地址能够获取到一个可以调用的地址呢对不对那负载均衡是什么呢一会儿我会答
[02:51] 给大家讲一讲现在你要理解一件事它的流程是什么呢流程就是从服务发现中心拿到该服务哪个服务啊就是上面我指的那个服务啊拿到这个服务我把这个名字写过来拿到这个服务的列表然后呢通过负载负载均衡的算法能够获取一个地址这就是
[03:24] 整个它的一个作用那说老师那这个怎么获取很简单看好就是在loadabundance它的方法当中给我们提供了一个叫做什么叫做choose这个方法它也就是说它要找到一个对吧它要发现一个地址怎么发现choose你选择一个地址选择地址它的参数里边你要指定给我指定什么服务名就行了
[03:54] 其实你会发现他他只知道服务名就行了因为他拿着服务名啊从这个networks里面去找找什么找实力这个实力其实就是我们说的这个IP和端口懂我意思吗所以呢他就找到了这么一个什么具体的一个实力那么找到这个实力有时候老师这个实力它是IP和端口他咋获取到这个东西呢其实你会发现你看他可以获取house的
[04:18] 可以获取pro的你看这都可以获取并且它还可以获取URI这个URI就是带http链接的对带http冒号杠杠这个字母串的URI懂吧好那现在呢我们只要拿着这个URI怎么做那你直接相当于直接用这个URI然后呢再加上后边的杠Service就完事你Service其实你注意
[04:46] 它不是服务实例的地址因为你要知道这个属于具体某一个接口的地址是吧前边的URA其实就是什么就是获取一个http://开头的一个什么地址这个地址包括了一个什么IP和端口大家理解吗好那这时候呢我们是不是就可以拿到这个具体的的这个实例的地址然后呢
[05:15] 远程调用这就是我们说的服务发现那服务发现有时候老师那怎么测呀很简单启动那现在我们要启动起来之后呢我们现在怎么做我们在这打个断点然后呢我们去访问的时候你注意看啊看好啊我们现在呢需要去来看一下我们请求一下啊他这个是不是56020啊然后在这看好啊Local House的56020 Service
[05:51] 你看诶注意看我们把这个断点注意刚才我们访问的是不是上面这个Service呀我们刚才是不是新建了一个service1呀我们要访问这个service1呀看这个断点进去进去不去诶你看嗯大家看报啥错我们来看一下控制针啥意思哪个是控制针这里边报rest template呃这行是控制针是吧
[06:27] 这一行是控制针注意看啊嗯这一行是控制针那我们初次判断的话应该是哪个呀在这打一段点再刷进来了进来了进来了之后呢我们来看哎哦原来如此你看没发现吗就是他看这个load abundance这个client是不是不为空但是呢他获取到的这个Service instance是不是就为空了好那我们的问题找到了
[07:00] 那这个是什么原因导致的呢但我们发现他是不是没有拿到一个实例那我们现在来回顾一下当初对我们做服务提供方的时候服务注册是咋做的是不是需要把这个客户端依赖加进去对吧另外的话你要注册的话当初我们是不是要指定注册地址
[07:21] 对不对而现在你各位你说你去发现了你不光要加这个客户端的依赖你是不是也要指定你从哪个服务注册中心去发现大家理解吗所以这个配置也要配上去但这个配置我们这个位服务名就叫consumer了对所以其实它的流程这个服务发现的流程也是你需要指定它从哪一个注册中心就是Nexus来拿这个服务的地址所以你少了一个配置
[07:52] 好我们再来启动OK那现在呢我们各位刚才我们是不是在这打一段点啊嗯接下来我们还在这打一段点注意看啊刷新这时候呢我们发现他就不报错了这个URI的值是不是就是我们说的这个微服务的一个地址对我的IP是192.168.1.0103然后呢端口号是5600那我们是不是就拿到了拿到的时候来让他走完各位这是不是就OK了
[08:21] 对所以以上呢就是我们说的服务发现的整个流程服务发现和服务注册都需要添加服务发现的客户端依赖就把这个依赖添进去然后都需要在配置文件当中配服务发现中心的地址那以及他的这个服务名这个服务名一定不要配重复了这是consumer是吧下边是provider那么服务发现的时候我们使用到了一个叫做load balance client
[08:48] 这么一个对象那他呢就是用于从服务发现中心来获取服务地址并通过负载均衡算法拿到一个地址好那稍后我会讲负载均衡那到这儿为止我们这个服务发现的流程各位我们是就完成了吧好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Nacos 作为服务注册与发现中心，结合 Spring Cloud LoadBalancer 实现服务消费者通过服务名调用服务提供者，并演示了负载均衡的实现。

2) 按时间顺序列出每张画面的要点：
画面1: 显示 IntelliJ IDEA 启动界面，项目名为 Nacos-RESTful-provider，当前打开的文件为 application.yml。
画面2: 显示项目结构，选中 Nacos-RESTful-provider 模块，编辑器中高亮显示了 pom.xml 文件中的依赖部分，包含 spring-boot-starter-web 和 spring-cloud-starter-alibaba-Nacos-discovery。
画面3: 编辑器中显示 RestConsumerController.java 文件内容，高亮部分为通过服务名拼接 URL 的代码。
画面4: 鼠标悬停在代码中 serviceId 变量上，弹出的提示框显示了该变量的类型和值。
画面5: 编辑器中显示 RestConsumerController.java 文件内容，高亮部分为使用 LoadBalancerClient 的 choose 方法选择服务实例的代码。
画面6: 显示 PPT 页面，标题为“2.3.4 负载均衡”，内容包括执行流程和负载均衡的定义。
画面7: 显示控制台输出，服务启动成功，端口为 5000。
画面8: 显示 RestConsumerController.java 文件内容，高亮部分为注释“通过服务名调用”。
画面9: 显示控制台输出，服务启动成功，端口为 5000。
画面10: 显示控制台输出，服务启动成功，端口为 5000。
画面11: 显示 application.yml 文件内容，配置了服务名、Nacos 服务发现中心地址。
画面12: 浏览器显示 Whitelabel Error Page，提示 Internal Server Error。
画面13: 显示 application.yml 文件内容，配置了服务提供方的地址。
画面14: 显示 PPT 页面，标题为“2.3.4 负载均衡”，内容包括执行流程和负载均衡的定义。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```xml
<modelVersion>4.0.0</modelVersion>
<groupId>com.alibaba.cloud</groupId>
<artifactId>Nacos-RESTful-provider</artifactId>
<packaging>jar</packaging>
<version>0.0.1-SNAPSHOT</version>
<name>Nacos-RESTful-provider</name>
<description>Demo project for Spring Boot</description>

<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.7.RELEASE</version>
    <relativePath/>
</parent>

<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <java.version>1.8</java.version>
</properties>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-alibaba-Nacos-discovery</artifactId>
    </dependency>
</dependencies>

<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>Hoxton.SR1</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```

画面3:
```java
@RestController
public class RestConsumerController {

    @Value("${server.port}")
    private String port;

    @Autowired
    private LoadBalancerClient loadBalancerClient;

    @GetMapping(value = "/Service")
    public String Service() {
        RestTemplate restTemplate = new RestTemplate();
        String result = restTemplate.getForObject("http://"+provider+"/Service", String.class);
        return "consumer invoke | "+result;
    }
}
```

画面5:
```java
@RestController
public class RestConsumerController {

    @Value("${server.port}")
    private String port;

    @Autowired
    private LoadBalancerClient loadBalancerClient;

    @GetMapping(value = "/Service")
    public String Service() {
        RestTemplate restTemplate = new RestTemplate();
        String result = restTemplate.getForObject("http://"+provider+"/Service", String.class);
        return "consumer invoke | "+result;
    }
}
```

画面11:
```yaml
server:
  port: 5000

spring:
  application:
    name: Nacos-RESTful-provider #服务名
  cloud:
    Nacos:
      discovery:
        server-addr: 127.0.0.1:8848 #服务发现中心地址
```

画面13:
```yaml
server:
  port: 5000

spring:
  application:
    name: Nacos-RESTful-provider #服务名
  cloud:
    Nacos:
      discovery:
        server-addr: 127.0.0.1:8848 #服务发现中心地址
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面6:
标题：2.3.4 负载均衡
内容：
执行流程：
1. 服务提供方将自己注册到服务注册中心
2. 服务消费者从注册中心获取服务地址
3. 进行远程调用

画面14:
标题：2.3.4 负载均衡
内容：
执行流程：
1. 服务提供方将自己注册到服务注册中心
2. 服务消费者从注册中心获取服务地址
3. 进行远程调用

5) 不要评价画面美观，不要输出与课程无关的内容。

