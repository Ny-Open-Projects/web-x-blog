# 01-Feign应用

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\01-Feign应用_【海量资源尽在 ubkz.com】.mp4
- 时长 11分22秒（音频 683s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来开始学习Spring Cloud第二天内容今天主要的学习目标是使用Fame和Spring Cloud的各种组件首先学习应用的是Fame为什么要使用Fame呢因为在前面虽然使用了Ribbon的负载均衡功能大大简化了远程调用时的代码但是里面代码中服务地址还是需要拼接和利用REST Template去访问代码较多重复率高
[00:29] 如果使用Fame的话就能让代码更加简洁地实现服务的访问那么现在来了解FameFame也叫伪装Fame可以把REST的请求进行隐藏伪装成类似Spring MVC的Controller一样不用再自己拼接UIO拼接参数等等操作一切都交给Fame去做在讲解更多之前大家跟我读两遍这个组件的发音FameFame
[01:05] 它的项目主页是这个链接打开这个链接看到页面中说了FAN的主要作用就是让编写DRAWA HTTP客户端更加容易easier既然如此那就到我们的项目中将FAN应用起来打开笔记来分析它的使用步骤如果要使用FAN的话那么我们要去导入启动器依赖
[01:40] 导入以后接下来我们去开启Fain功能再去编写Fain客户端编写处理器这个处理器我们给它起个名字Consumer Fain Controller为了避免跟我们前面的处理器有冲突或是混淆所以我们编写一个新的处理器那这个处理器用来应用注入Fain
[02:23] 用的是openfame
[03:02] 一来加入以后接下来我们去开启Fain功能找到启动引导类加入一个注解at enable Fain Clients开启Fain功能开启以后接下来我们再去编写一个Fain客户端这是一个接口我们把它放到Client这个包项来一个
[03:36] 专门来处理用户的一个客户端来个user client标示它是一个fame的客户端加一个注解fame client那这个fame client它要去拼接的路径是要找哪一个Urica中的服务服务名称这个光标在省的地方你要指定是user-Service它的意思声明当前类是一个fame
[04:14] 客户端指定服务名为user-Service后续呢他就会去拼接我们其实主要在这个fan客户端中要做的事情就是拼接地址到时他会将我们的这个拼接到一会的路径中哪一些路径就是我们这边会去编写方法那这方法呢会有映射的路径get mapping我们指定一个user然后id
[04:44] 是一个路径变量返回类型是user query我们把它引入query by id路径变量at pass variablelong id好我们的fan code端就已经编好了编写好以后呢它会通过动态代理帮我们去生成一个实现类那这个呢就跟mybattist的Mapper接口是比较相似的那添加这个注解声明它是一个fan code端
[05:22] 指定服务名称其实我们主要拼接的按照我们现在这个方法编写的话呢它就可以替我们去拼接一个这样的路径user-serviceuser然后具体当以后你传什么具体的值那就是类似这些值OK那我们现在用的是一个路径变量所以要去获取到它到时候会把这个真值拼接到路径中假设传了113拼接的就是这个地址
[05:51] 接口中定义的方法呢我们可以使用Spring MVC的一些注解因为其实我们一会在处理器中调用的时候那么也就是按照处理器的就Controller的方式去调用的所以要可以使用Spring MVC的注解去帮我们生成这些URL那我们用了一个GetMapping指定一个访问的路径接下来这个路径当然也不能乱指定这个是要提供的服务要存在才行那我们现在是存在的
[06:23] 我们的服务提供工程中有这么一个路径你不能写的那么奇怪因为他最终是要拼接这个地址要能访问的才行好所以这个地址要注意完了以后接下来我们去编写一个处理器consumer fame Controller标注它是一个处理器add res Controller映射的路径request mappingc f consumer fame里面的方法要利用
[07:01] Fan客户端去访问一个服务好所以我们把这个Fan客户端给注入进来就刚才编写的user-client注入注入以后接下来我们去编写一个方法返回到类型query-by-id-user我们引入引入的是我们这个工程的路径变量也要去设置ID获取pass-variable-long
[07:42] ID然后我们再去调用fan code端user client.querybyidID传进去返回这么一个user就可以了这就我们的处理器编写也编写完成好那完了以后呢我们去测试来验证能否通过访问CF的这一个路径可以获取到我们的用户数据信息如果可以的话说明我们的fan code端是有意义的能够拼接一个正常可访问的地址
[08:14] 那么去启动这个服务的消费工程你启动的时候要保证我们提供服务的工程也是启动状态要注意这是我们提供服务的工程而Urica当然也要在因为它要根据我们的服务名称去Urica获取服务的地址列表所以这个Urica也要得启动不然你的服务也没法注册好启动好以后呢接下来我们去打开浏览器访问一个地址就是它那就访问Localhost
[08:50] 8080CF我们来一个1或是2都可以8当时我们访问的是就是前面我们的consumer工程访问过81也是一样的有数据存在就会显示我们回车好见到了没有问题如果你访问其他的也是一样没有问题可以看到数据好这就是我们Fan客户端的一个应用替我们去拼接一个可访问的地址然后去实现我们的服务访问现在回到笔记中我们来进行小结
[09:25] 那我们的Fend主要作用Fend主要作用就是自动根据参数拼接http请求地址好我们自己没有再去拼接了利用的是Fend客户端去替我们拼接的那我们刚才在编写的过程中要注意的就是启动器依赖还有是我们核心的一个Fend
[09:58] 客户端代码把它粘过来让大家更好的去参考打开开发工具去复制这两个东西启动器启动器依赖Fend客户端代码这个客户端代码用了一个注解就是FendClient标注它这个接口是一个Fend客户端Fend客户端里面可以去用Spring MVC一些常用的注解比如说我们用了一个App
[10:49] get mapping还有pass variable等这些mvcsprintmvccontroller中可以用的都可以在这边去使用意思就是替我们拼接一个地址那么地址呢是服务名结合这一个路径再得到一个完成的完整的一个服务名称再利用我们的ribbon负载均衡去从地址列表中选择一个地址再去访问具体服务ok它其实是传递依赖了ribbon过来后面我们也会说到它这个负载均衡部分这就是我们
[11:19] Fender 應用

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Cloud Feign 实现服务间的调用，并介绍其负载均衡与熔断机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前章节为“1. Feign”，并列出学习目标，包括使用 Feign 进行远程调用、配置 Gateway 网关服务、配置 Gateway 路由过滤器、编写 Gateway 全局过滤器、搭建 Config 配置中心服务、配置 Bus 实时更新配置。
画面2：展示课程大纲，包括“1. Feign应用”、“2. Feign负载均衡及熔断”、“3. Spring Cloud Gateway网关简介”、“4. Spring Cloud Gateway入门”等章节。
画面3：展示项目结构，包含 consumer-demo、Eureka-server、user-Service 等模块，以及 ConsumerApplication.java 文件，其中包含 @SpringBootApplication、@EnableDiscoveryClient、@EnableCircuitBreaker 等注解。
画面4：展示 UserClient.java 文件，导入了 org.springframework.cloud.openfeign.FeignClient、org.springframework.web.bind.annotation.RequestMapping 等包。
画面5：展示 UserClient.java 文件，定义了 @FeignClient 注解，指定服务名为 user-Service，并定义了 @GetMapping("/user/{id}") 方法。
画面6：展示 ConsumerFeignController.java 文件，导入了 org.springframework.cloud.openfeign.FeignClient、org.springframework.web.bind.annotation.RequestMapping 等包。
画面7：展示 ConsumerFeignController.java 文件，定义了 @RestController、@RequestMapping("/f") 注解。
画面8：展示 ConsumerFeignController.java 文件，定义了 @Autowired 注解的 UserClient 类型的私有属性。
画面9：展示 ConsumerFeignController.java 文件，定义了 @GetMapping("/id") 方法，调用 UserClient 的 queryById 方法。
画面10：展示运行结果，显示 UserApplication9091、EurekaServerApplication10086、UserApplication9092 等服务已启动。
画面11：展示浏览器访问 localhost:8080/consumer/8，返回结果为 "hello"。
画面12：展示 ConsumerFeignController.java 文件，定义了 @GetMapping("/id") 方法，调用 UserClient 的 queryById 方法。
画面13：展示 pom.xml 文件，定义了 Spring Cloud OpenFeign 的依赖。
画面14：展示 Feign 客户端的定义，使用 @FeignClient 注解指定服务名，并定义了 @GetMapping 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
package com.ithema.consumer;
import org.springframework.boot.SpringApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.client.loadbalancer.LoadBalancerClient;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@EnableDiscoveryClient
@EnableCircuitBreaker
public class ConsumerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ConsumerApplication.class, args);
    }
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}
```

画面4：
```java
package com.ithema.consumer.client;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RequestAttribute;
import org.springframework.web.bind.annotation.RequestTimeout;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestController

