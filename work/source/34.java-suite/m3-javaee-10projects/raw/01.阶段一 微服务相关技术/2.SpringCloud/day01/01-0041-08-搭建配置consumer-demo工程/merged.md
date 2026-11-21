# 08-搭建配置consumer-demo工程

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\08-搭建配置consumer-demo工程_【海量资源尽在 ubkz.com】.mp4
- 时长 12分29秒（音频 749s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 搭建配置consumer-demo工程在这一小节中我们的主要目标是编写测试类使用rest template访问user-Service的路径根据ID查询用户好那我们来分析这个目标的具体需求呢其实就是访问一个路径是我们的服务消费工程的一个路径然后这个路径对应的处理器呢要去使用我们的rest
[00:36] template获取刚刚服务提供工程中的一个路径数据OK要做这么一件事情那我们来分析一下应该如何去实现实现步骤我们是在服务的消费工程中去接收这样的一个请求然后利用这个rest template前面我们验证过它可以获取服务的数据获取到上面这一个工程我们的服务提供的工程中的一个数据
[01:16] OK那第一步呢我们现在是在服务的消费工程中也就是我们的consumer gun demo工程中去做了事情你要去编写处理器实现这么一个请求所以我们要去添加对应的web启动器添加启动器E-lineOK加完这个E-line以后呢接下来我们去创建启动引导内核配置文件OK然后接着呢再来我们是去编写
[01:47] 测试代码测试代码其实要编写一个处理器编写一个消费者就是consumercontroller在这一个处理器中使用我们的res template好访问服务获取数据那我们的第二个步骤里面的引导类就可以像我们在前面的施力工程中一样可以去注册一个res template
[02:29] OK 可以做这些事情然后编写好这些代码以后呢我们接着再去测试验证有没有问题那接下来我们打开IDA按照我们的分析去一步步实现第一个添加启动器依赖是在我们的consumer-demo工程中去添加好 所以我们打开找到我们的consumer-demo.sum文件好 在这边添加具体的依赖那依赖呢我们要加的是web启动器OK
[03:00] 我们去添加dependency-sprint-boe-starter-web好加好以后接下来我们再按照我们的分析去创建启动引导类和配置文件当然配置文件如果你没有什么参数的话可以暂时不加那我们是一个Sprintable工程后续呢总归有地方有组件需要使用到我们的配置文件的话那你加上也无所谓好所以我们来去
[03:30] 用插件的去生成创建一个启动引导类叫做consumer application要不要生成我们的配置文件要生成ok那按照分析我们的这个启动引导类里面呢我们可以再去注册一个rest template后面为我们的处理器注入提供便利我们在这边去注册一个public返回的是我们的rest templateok
[04:13] Rest TemplateReturn NewRest TemplateOK注册好后呢接下来我们再去编写处理器服务消费工程中你去编写一个Controller好这个Controller我们把它放到这个Controller包中好移进去移进了移进后呢接下来我们在这边标注它是一个处理器Add Rest Controller然后它的一个映射的路径Rest Mapping好我们指定
[05:03] consumer OK完了以后呢接下来在里边去编写处理的方法这个方法也是根据ID去查询用户信息好query by ID那这个user呢我们在消费工程中是不存在的我们去造一个出来创建一个packagepojo好然后我们把服务提供工程中的user给复制过来
[05:37] 这两个过程因为没有任何的依赖关系好所以我们去复制那复制的时候呢他说我们要用到一些呃这些注解那注解呢其实我们这边不是直接跟数据库进行交互所以我们的通用呃通用map中用到的jp注解呢是可以全部删除的我们不需要用到好所以把它删除删除这一个删除删除删除我们只是接收数据ok所以不进行一个数据库
[06:05] 字段跟属性的一个映射所以不需要这些JPG注解然后回来到我们的处理器中OK user引入引入的是我们刚才加入的是我们的consumer poll中的一个user然后呢我们去接收ID好然后映射的路径我们指定清楚get mapping好带一个ID接着呢我们在这边去注入刚才注册的rest template auto wire
[06:36] 注入private rest template注入rest template注入以后呢接下来我们再利用它去访问我们的一个地址这个地址呢我们是这么一个地址等于服务提供工程中的这个地址localhost9091user8ok然后我们再利用它去访问ok那就是get for object然后地址给过去返回的
[07:06] 数据类型我们是userok我们再得到它的一个返回结果这是一个user好得到以后呢接着我们再把它返回那直接返回也是可以的会更加简洁一些like returnok这就是我们的处理器里面的方法已经编写完成接下来我们进行测试那测试的话呢你要保证我们的服务提供工程userapplication这个启动引导类是启动的那么作为一个
[07:42] 服务消费工程也要启动然后呢去访问这么一个地址然后获取到数据好因为我们没有配置Tamcat的任何端口所以默认就是8080我们这边没有配置好所以打开我们的服务消费工程中的启动引导类你去启动它好启动好以后呢如果成功的话那就是我们访问我们笔记中记得这一个地址应该得到ID为8的这个数据也就是在服务提供工程中访问的结果是一致的
[08:12] OK接着呢我们打开浏览器去访问也就是跟这个结果是应该一致的OK我们打开来访问一下回车见到了没有问题这两个结果是一样的因为我们在消费工程中调用的就是这个地址好所以它的数据然后也可以这样输出出来OK这就是我们的一个消费工程中的一个案例测试从刚才的两个工程中分别实现了服务的提供和调用
[08:46] 现在来分析查看这种服务的调用关系是否存在一些问题我们现在打开讲义来了解问题在consumer.com demo中如果我们把这个地址呢以后都是这样硬编码方式写到代码中的话那后期不方便维护这是一个也就是这个意思在我们的这个处理中Controller中把这个地址写死了好第二个呢就是
[09:16] 我们的这一个工程如果不写死也要去记忆这个地址OK以后出现变更也得不到通知不太方便OK然后接着第三就是这个服务的消费工程呢不清楚这个9091服务器是启动还是没有启动的状态好所以也会引起问题当如果它是没有在启动状态中是得不到这个服务的OK好所以我们这个要去解决这些问题包括呢
[09:45] 9091这台服务器现在只有一台以后如果有多台的话那么你调用哪一台好就是我们的消费工程从哪一个地址中去调用这也是一个问题好而且现在只有一台的话呢这个9091也不高可用如果有一台挂了那就这个服务就得不到保障了再者就是我们的这个user干Service工程以后呢做了集群的话我们的消费工程还要从中去选择
[10:14] 多个地址中去选择一个来去进行也要去实现这个负载均衡OK那就会出现一系列的这些问题那其实上面的问题概括来说呢就是我们这种分布式服务必然会面临的一些问题刚才我们搭的两个项目呢做的是分布式服务的一个调用OK那这样的面临问题就是服务的管理问题如何实现自动注册和发现如何实现状态的监管跟
[10:41] 实现动态的路由就当如果有多个地址的时候如何精选精准的选择一个地址去访问另外就是服务如何实现负载均衡当多个地址的时候如何选择然后是服务如何解决容灾的问题当某一个服务挂了是不是有后备的一些服务来保障服务的稳定性然后接着呢就是如何实现统一的配置当如果多个这样的user跟Service工程做集群的时候呢一个
[11:10] 配置改了要改所有集群的配置那如果一个一个去改又太麻烦那这样的一些问题我们Spring Cloud都可以得到答案都可以解决刚刚的两个项目并不是Spring Cloud的一个应用而是给我们看到分布式服务中的一些问题我们慢慢的去用Spring Cloud去解决这样一些问题好所以我们回到笔记中把我们刚才见到的这一些问题呢给记录一下
[11:40] 也就是我们刚才那个两个工程中搭好以后测试验证倒也没问题只是有一些问题问题是哪些问题是这一些OK就是服务管理会有一些问题然后接下来再来是我们的服务如何实现负载均衡好是一个问题还有是统一的配置也是一个问题OK会出现这些问题那么这些问题呢上述的问题都可以通过Spring Cloud
[12:15] 的各种组件解决OK这就是我们刚才呢搭建配置consumer-demo工程的一个所有内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何搭建并实现一个使用 RestTemplate 调用远程服务的 Spring Cloud 消费者工程（consumer-demo），并引出后续将使用 Eureka 注册中心解决分布式服务面临的问题。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程目标与需求，说明要编写测试类使用 RestTemplate 调用 user-Service 的数据。
画面2: 展示 consumer-demo 工程的 Maven 依赖配置，其中包含父工程、Spring Cloud 版本、Spring Boot 版本及当前模块的 artifactId。
画面3: 在 IDEA 中右键点击 consumer 模块，准备添加依赖。
画面4: 在 ConsumerApplication.java 中添加 @Bean 注解，用于创建 RestTemplate 实例。
画面5: 在 IDEA 中右键点击 consumer 模块，选择“Add Framework Support...”并选择 Web。
画面6: 在 ConsumerController.java 中定义一个 @RestController 和 @RequestMapping("/consumer") 的类。
画面7: 在 ConsumerController.java 中定义一个 queryById 方法。
画面8: 在 ConsumerController.java 中为 queryById 方法添加 @GetMapping("/id") 注解。
画面9: 在 ConsumerController.java 中为 queryById 方法添加 @Autowired 注解，用于注入 RestTemplate。
画面10: 在 ConsumerController.java 中为 queryById 方法添加 RestTemplate 类型的私有成员变量。
画面11: 在 ConsumerApplication.java 中定义一个 @Bean 方法，用于创建并返回 RestTemplate 实例。
画面12: 在 ConsumerController.java 中为 queryById 方法设置 URL 为 http://localhost:9091/user/{id}。
画面13: 展示 PPT 内容，介绍 Eureka 注册中心的作用，以及服务管理、状态监控、动态路由、负载均衡和配置统一等问题。
画面14: 展示课程目标与需求，说明要编写测试类使用 RestTemplate 调用 user-Service 的数据，并列出后续要解决的服务管理、状态监控、动态路由、负载均衡、容灾问题和配置统一等问题。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <artifactId>heima-Spring Cloud</artifactId>
        <groupId>com.itheima</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>consumer-demo</artifactId>
</project>
```

画面4:
```java
package com.itheima.consumer;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ConsumerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ConsumerApplication.class, args);
    }
}
```

画面5:
```java
@RestController
@RequestMapping("/consumer")
public class ConsumerController {
}
```

画面6:
```java
@GetMapping("/id")
public User queryById(Long id) {
}
```

画面7:
```java
@GetMapping("/id")
public User queryById(Long id) {
}
```

画面8:
```java
@GetMapping("/id")
public User queryById(Long id) {
}
```

画面9:
```java
@Autowired
private RestTemplate restTemplate;
```

画面10:
```java
@Autowired
private RestTemplate restTemplate;
```

画面11:
```java
@Bean
public RestTemplate restTemplate() {
    return new RestTemplate();
}
```

画面12:
```java
@GetMapping("/id")
public User queryById(Long id) {
    String url = "http://localhost:9091/user/" + id;
    return restTemplate.getForObject(url, User.class);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面13:
标题: 6. Eureka注册中心
子标题: 6.1. 认识Eureka
内容:
- user-Service只有1台服务，不具备高可用性
- 即使user-Service形成集群，consumer自己还不能实现负载均衡
- 其实上面的问题，概括一下就是分布式服务必然面临的问题：
  - 服务管理
    - 如何自动注册和发现
    - 如何实现状态监管
    - 如何实现动态路由
  - 服务如何实现负载均衡
  - 服务如何解决容灾问题
  - 服务如何实现统一配置
- 以上的问题，都将在Spring Cloud中得到答案。

5) 不要评价画面美观，不要输出与课程无关的内容。

