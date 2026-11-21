# 17-线程隔离&服务降级

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\17-线程隔离&服务降级_【海量资源尽在 ubkz.com】.mp4
- 时长 18分42秒（音频 1123s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 现成隔离与服务降级在这一小节中我们的主要目标是了解什么是现成隔离和服务降级在前面我们了解到用户的请求因为一直等待一个出现异常的服务致使请求的现成阻塞引起雪崩效应那如何去解决雪崩效应我们可以使用PiStream解决雪崩效应那它的解决手段有两个一个是现成隔离一个是
[00:34] 服务降级那现成隔离的意义就是用户请求不直接访问服务而是使用现成池中空闲的现成访问服务加速失败判断时间另外一个服务降级呢就是即使返回服务调用失败的
[01:08] 结果让现成不因为等待服务而阻塞具体我们打开讲义来了解highstreaks解决雪崩效应的一个两个手段现成隔离和服务降级我们具体来看现成隔离的一个示意图当有一个请求要用到几个服务的时候那么这时候呢不再直接去访问服务而是通过
[01:40] 一个小现成池里面有固定的现成数那么当如果要用到服务的时候通过现成池中可用的现成去发送请求去获得这个服务那如果这时候呢现成池中的现成数被耗尽了那么也就是说这个服务不可用了所以可以加速判断该服务是否能用可用好所以让我们的请求能够及时知道这个结果OK那如果知道这个结果以后呢他就可以去
[02:08] 要么去调用要么就是直接跳过这个服务不能使用那就直接离开而不是一直无限的等待下去好那如果是这一个服务可用的有现成池就是这个空闲的现成去请求这个服务的话那么请求的过程中如果我们的服务是有问题或是网络不通总之就是这个服务不可得的时候那这时候呢我们可以采用服务降级服务降级的意思就是加速告诉这个现成
[02:37] 这个服务是不可用的你不用再持续的等待下去导致呢请求进行阻塞引起资源耗尽服务器荡迹的问题好所以服务降级就是可以及时返回一个处理失败的结果当然如果你是正常的话那还是正常的返回如果是等待一定的时间都没有结果的话那么这个会返回一个失败结果而不会无限的等待下去OK这就是我们的一个关于现成隔离
[03:05] 还有服务降级那总的来说现成隔离通过判断现成池中的空前现成数是否可用如果不可用了那么就会加速判断一个失败判断的一个时间就不让我们的请求继续等待下去那另外一个是我们的服务降级服务降级呢就是直接会返回一个执行失败的结果因为它已经超过一定时间都没有响应那么就不会让我们的现成
[03:33] 持续的等待或是引起我们的一个阻塞OK这就是我们的两种手段那具体我们的项目中应该如何去应用我们现在来去配置一下在我们的消费者工程中去配置这么一个依赖然后再去开启熔断之后呢再去编写我们的降级逻辑就如果真的发生了服务不可用的时候应该返回怎么样的失败结果然后接着再次去编写对应的一个回调就是我们的处理方法
[04:02] 默认的forbent当如果服务不可用的时候应该返回什么信息这种全体性的一个方法我们可以去编写我们按照步骤来去实现第一个呢是添加依赖那依赖呢用的是这一个依赖在服务消费工程也就是我们的consumer-demo中去添加那么打开IDA去添加这个依赖启动器名称highstreaks好加好以后呢接下来打开我们的启动引导类
[04:42] 去添加一个开启熔断的一个注解at enable circuit breakerok 这是开启开启熔断那这三个注解呢可以通过一个组合的注解去使用叫做 at spring cloud application这个组合注解就包含这上面三个我们打开看一下就包含了这三个好所以
[05:17] 如果你用一个这个spring cloud application的话呢就可以代替这三个了三个就可以全部给注释掉好就可以不用用一个spring cloud application来代替他们三个ok这个启动引导类中注解加好以后接下来我们再去配置他的一个降级逻辑那我们为什么要去编写这么一个降级逻辑呢因为当如果这一个服务呢去访问这个地址
[05:42] 调用不到的时候应该是加速的返回一个失败的结果所以也就是服务的降级处理OK所以我们要去编写一个降级的逻辑那么我们可以通过一个注解叫做highstreak command这边指定它的一个方法就是当服务失败的时候我们返回的一个返回结果就失败的一个结果通过forbid math降级方法名称
[06:15] 你假设呢取一个叫做querybyidfallback那这个方法呢现在是没有的我们要去造一个那这个方法呢必须返回类型是字符串类型好所以我们要指定字符串类型然后这个方法的类型要跟我们的这一个处理的方法请求的方法呢类型是要保持一致的也就是说这边不能使用user而使用string
[06:43] 你要改造再说了如果是真的处理失败你返回user也是没有意义的所以我们要返回一个字符串那既然是字符串我们把这个改造成string就可以了它默认呢就是一个json格式字符串我们把它返回字符串也是没有任何影响之后呢在这个方法中我们再去处理它这个参数呢你要可以保持一致long id然后接呢在这里边我们输出一个日志代控制台我们把这个
[07:11] Lamborgue引进来一个CFOJ可以用一个Log变量记录消息失败的消息我们记录是查询用户信息失败ID是什么我们也记录下来这括号是一个站位符可以在后面的用后面的这个变量值代替它再返回一个字符串比如说对不起
[07:52] 网络太拥挤了好这是我们的一个降级的方法就编写好了我们来进行测试测试的点就是我们要去启动这个服务先正常的情况去测试它好先启动它启动后呢我们的消费的工程consumer工程也启动正常情况下那就还是正常的返回这个查询结果之后我们再把这个提供服务的user-Service工程给关闭了也就是说服务不通不通的情况下
[08:29] 再去访问那么他就会出现一个服务降级的一个呃结果返回7号以后我们先去访问一下打开consumer 8080 这个刷新这是第一次我们现在呢是第一次启动的时候他超时因为他有默认的超时时间不是我们的服务有问题而是我们的第一次访问超过了一秒钟好所以他现在是出现呃一个降级的结果
[09:01] 那如果我们第二次访问的时候呢这个服务是正常的因为我们的抓网呢第一次访问的时候确实慢一点第二次之后就会快所以它不在超时时间以外的话那么它会正常返回结果这时候我们来测试失败的结果也就是我们故意的把这个提供服务的工程给关闭也就是我们的这个user account Service把它关闭了以后接下来消费工程再怎么访问也是获取不了服务的
[09:29] 既然获取不了那肯定会超时就超过一秒钟因为他一会我们可以去改这个超时时间那这个获取不了以后他就会进行一个降级处理降级处理就会到我们的这个方法中返回一个结果也就是把这个失败的结果呢不会让我们的现成无限的等待而是会返回有一个结果让他知道这是请求是有问题的好服务调用失败所以我们来再刷新好超时以后他就会提示我们的这句话也就是一个服务降级处理
[09:59] OK那么再回到我们的开发工具中刚才呢都是在一个方法中去处理的那如果以后我们这个类有很多方法的话每一个方法都这样去写而且要写一个对应的降级方法来那么整个类就会很庞大也不方便所以我们可以针对一整个类呢去编写一个降级方法好所以我们来去改造一下这是一个方法的时候这个写法那么如果有多个的时候我们可以在类上面去编写
[10:29] 当然这个注解还是要加的at highstreak command加了以后我们在类上面加一个default properties这里边我们可以指定一个降级的方法我们给它起一个名称default fallback这个方法现在是没有的那它类型也是字符串所以要注意一下我们复制一分没有参数再标示一下这是默认的提示
[11:09] 也就是我们的默认降级方法中的一个输出跟这个有区别好就已经改造好了改造以后呢接着我们再去测试一下来重启服务消费工程consumer-demo起了以后现在我们的提供服务的工程user-Service呢还是没有起的也就是说会出现服务的降级也就是提示这句话刷新已经出现了这是我们的一个全局性的降级服务方法
[11:51] 提示的内容跟我们刚才某一个方法的不一样这个内容是不一样的我们是有区别的如果以后一个类里面有多个方法都要进行一个服务的降级的话那么可以使用这种方式来做那刚才说到一个降级超时就服务等待的超时时间的问题high streak默认的超时时间是一秒就刚才第一次为什么我们访问的时候就已经出现这个降级方法的返回结果了是因为你访问
[12:19] 超过了一秒钟所以他就认为是服务调用有问题直接是到降级方法这边来处理了那我们可以通过配置项去配置这一个超时时间打开我们的讲义来去配置这一个超时的时间在这边我们可以通过他这样复制会更方便我们再复制到我们的yaml配置软件中他会自动格式化我们再去改造因为大家如果直接复制这一个那到我们的配置软件中他会变动我们的格式不好
[12:51] OK所以大家看我的做法打开开发工具然后找到我们的配置文件就它里面我们去配置复制过来你看它就自动格式化了只是这个等号呢我们在yaml文件中是不可以用的所以要注意一下还有一个有值的配置项要有个空格后面没有这个冒号我们去掉配置完了配置后呢现在也就是说我们的highstreak超时的时间
[13:17] 是两秒刚才是一秒它是毫秒作为单位的配置好以后我们来去测试验证那为了验证这个效果呢我们可以在调用服务的这个工程中去改造一下它我们当时的这个方法把它改一下故意的延时来个休眠两秒这个休眠两秒快捷键有点问题好这个是一个异常我们catch一下
[14:12] 两秒钟我们再去启动服务的消费工程我们要去启动服务消费工程已经启动了但是我们刚才又去添加一个配置项这个我们去重启重启以后我们来看访问的时间打开F12浏览器F12按一下我们之后再去刷新查看启动情况起好了服务提供的消费的工程都起好我们来刷新这个请求地址刷新
[14:55] 好你看这就这一个请求这个请求呢我们看一下他的耗时时长2.47秒也就是已经超过两秒了超过两秒那么他就会提示这个网络太拥挤因为我们现在呢你如果要发送过来而且我们这边又是故意的让他沉睡两秒钟是一定会超过两秒的那如果这样我们会出现一个服务的降级那我们现在如果把这一个去掉的话再来去测那么他又不会出现
[15:27] 这个服务降级的情况我们再把它注视掉再来启动我们刚才不是第八个启动的我们现在要重启启了后再来去测成功的标准就是当如果你的请求网络的总共加起来时间不超过两秒的话那么它会正常的去返回我们的一个处理结果也就是我们的用户数据那如果是超时就会返回我们降级方法里面的一个返回结果就它而且我们用的是全局的一个降级方法再来刷一下
[16:04] 好已经返回了因为他现在耗时时间是一秒钟不到所以他现在没有超时正常返回一个数据现在我们再回到笔记中来进行小结那么刚才做的呢这些呃配置我们记录一下我们添加了一个依赖添加的依赖有哪些加了依赖后呢接着我们去开启开启熔断降级逻辑
[16:40] 还有就是我们修改一个超时配置的超时配置把它记录过来大家在自己用的时候会更加方便一点把对应的代码跟配置给拿过来第一个是我们的依赖那找到我们的配置这个碰文件依赖信息接着再次开启熔断我们做的事情是加了这么一个注解而且又发现一个组合注解呢
[17:36] 它可以代替这三个注解也就是这一块降级逻辑降级逻辑我们是在Controller中去编写的那也就是我们的这一个方法超时时间的修改这个配置文件因为大家从pdf中去复制不太好复制所以我们把配置文件中的这一个给拿到我们的笔记中记录下来这就是我们线程隔离与服务降级的一个演示包括我们了解到原来
[18:32] 隔离就是加速失败判断时间服务降级就是及时的返回服务调用失败的结果OK这就是我们这一个小节中的全部内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Cloud 项目中集成 Hystrix 熔断器，实现服务的线程隔离与降级处理。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程 PPT 页面，标题为“16. 熔断器Hystrix简介”和“17. 线程隔离&服务降级”，并列出目标和分析内容。
画面 2: 展示 PPT 页面，详细解释 Hystrix 的线程隔离和降级机制。
画面 3: 展示 PPT 页面，标题为“8.3.2. 手动实践”，内容包括引入依赖和开启熔断的步骤。
画面 4: 展示 IDEA 编辑器界面，显示 consumer-demo 项目的目录结构和 ConsumerApplication.java 文件内容，其中包含 @EnableDiscoveryClient 和 @EnableCircuitBreaker 注解。
画面 5: 展示 IDEA 编辑器界面，显示 ConsumerController.java 文件内容，其中包含 @HystrixCommand 注解和 queryById 方法。
画面 6: 展示 IDEA 编辑器界面，显示运行日志，显示服务已启动。
画面 7: 展示 IDEA 编辑器界面，显示 ConsumerController.java 文件内容，其中包含 queryById 和 defaultFallback 方法。
画面 8: 展示 IDEA 编辑器界面，显示 ConsumerController.java 文件内容，其中包含 @HystrixCommand 注解和 queryById 方法。
画面 9: 展示 IDEA 编辑器界面，显示 application.yml 文件内容，其中包含 Hystrix 的配置。
画面 10: 展示 IDEA 编辑器界面，显示 UserController.java 文件内容，其中包含 queryById 方法。
画面 11: 展示 IDEA 编辑器界面，显示 UserController.java 文件内容，其中包含 queryById 方法。
画面 12: 展示课程 PPT 页面，标题为“17. 线程隔离&服务降级”，并列出“添加依赖”、“开启熔断”、“降级逻辑”、“修改超时配置”等要点。
画面 13: 展示 IDEA 编辑器界面，显示 ConsumerController.java 文件内容，其中包含 @HystrixCommand 注解和 queryById 方法。
画面 14: 展示课程 PPT 页面，标题为“16. 熔断器Hystrix简介”和“17. 线程隔离&服务降级”，并列出目标和分析内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-hystrix</artifactId>
</dependency>
```
```java
@SpringBootApplication
@EnableDiscoveryClient
@EnableCircuitBreaker
public class ConsumerApplication {
    // ...
}
```
```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
```
画面 4:
```java
package com.itheima.consumer;

import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.circuitbreaker.HystrixCommand;
import org.springframework.cloud.client.loadbalancer.LoadBalancerClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ConsumerController {
    @Autowired
    private RestTemplate restTemplate;
    @Autowired
    private DiscoveryClient discoveryClient;
    @RequestMapping("/consumer")
    public String queryById(Long id) {
        String url = "http://user-Service/user/" + id;
        return restTemplate.getForObject(url, String.class);
    }
}
```
画面 5:
```java
@HystrixCommand(fallbackMethod = "queryByIdFallback")
public String queryById(Long id) {
    String url = "http://user-Service/user/" + id;
    return restTemplate.getForObject(url, String.class);
}
```
画面 7:
```java
public String queryByIdFallback(Long id) {
    log.error("查询用户信息失败，id: {}", id);
    return "对不起，网络太拥挤了！";
}
```
画面 9:
```yaml
spring:
  application:
    name: consumer-demo
  cloud:
    Eureka:
      client:
        Service-url:
          defaultZone: http://127.0.0.1:10006/Eureka
        # 注册服务和拉取服务列表的时间间隔，默认30秒
        registry-fetch-interval-seconds: 10
    hystrix:
      command:
        default:
          execution:
            timeoutInMilliseconds: 2000
```
画面 10:
```java
package com.itheima.user.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/user")
public class UserController {
    @Autowired
    private UserService userService;
    @RequestMapping("/user")
    public User queryById(Long id) {
        return userService.queryById(id);
    }
}
```
画面 11:
```java
package com.itheima.user.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/user")
public class UserController {
    @Autowired
    private UserService userService;
    @RequestMapping("/user")
    public User queryById(Long id) {
        return userService.queryById(id);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题为“16. 熔断器Hystrix简介”和“17. 线程隔离&服务降级”，并列出目标和分析内容。
画面 2: 标题为“17. 线程隔离&服务降级”，并列出“线程隔离”和“服务降级”的分析内容。
画面 3: 标题为“8.3.2. 手动实践”，并列出“引入依赖”和“开启熔断”的步骤。
画面 12: 标题为“17. 线程隔离&服务降级”，并列出“添加依赖”、“开启熔断”、“降级逻辑”、“修改超时配置”等要点。
画面 14: 标题为“16. 熔断器Hystrix简介”和“17. 线程隔离&服务降级”，并列出目标和分析内容。

5) 不要评价画面美观，不要输出与课程无关的内容。

