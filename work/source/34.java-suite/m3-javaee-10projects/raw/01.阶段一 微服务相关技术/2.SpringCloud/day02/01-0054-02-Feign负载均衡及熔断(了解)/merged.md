# 02-Feign负载均衡及熔断（了解）

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\02-Feign负载均衡及熔断（了解）_【海量资源尽在 ubkz.com】.mp4
- 时长 17分25秒（音频 1045s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] Fan 负载均衡及熔断在这一小节中的主要目标是可以配置Fan内置Ribbon配置项和High-Stress熔断的Foreback配置前面学习了负载均衡Ribbon服务熔断High-Stress等组件在Fan中也都有自动去集成这些组件那么可以通过配置开启使用具体在Fan中可以去配置一些组件包括负载均衡服务熔断
[00:31] 压缩就是请求的一个压缩配置还是日志的记录级别都可以去配置那么这些配置呢都可以通过配置项在Fran中开启使用现在我们打开讲义来了解这些在Fran中的配置第一个是负载均衡在Fran本身已经集成了Ribbon依赖和自动配置
[01:08] 看这个图里面我们也看得出来就是我们添加这个all pin fan的时候就已经传递依赖了ribbon只是呢我们在Ureka中也有传递依赖ribbon所以在我们fan中依赖呢就会被忽略掉因为它其实也是已经存在了OK既然这个依赖是有的那么我们也就不用再额外引入也不需要去再注册rest template对象它已经自动整合那么只需要去添加了配置像有比如说
[01:37] 读取的超时时长读取的超时时长就是整个获取服务的时候这个时长包括你出连返回的时候connect turn out就是连接的时候连接时长那我们可以通过配置这些配置项来去应用ribbon还有其他的配置项包括有当失败的时候呢重视的次数你可以去配置然后是重视多少次服务因为你有多个服务列表那这个不行另外一个可以去尝试
[02:06] 是否对所有请求方式都进行从事等这些配置那现在呢我们就打开IDA在服务的消费工程中去配置这些配置项一定要注意这是针对Friend来做的也就是你一会要测试的时候呢肯定要是在用了Friend客户端的那些代码中或者是请求中去测试才可以才有效我们打开IDA这个配置软件中去添加刚才的那些依赖
[02:38] 好按住Alt键往下拉12两格好配置完以后接下来我们再去启动这一个工程启动启动好以后呢我们再去测试也就是你测试的时候一定需要访问这一个的我们当时写的这个处理器因为他采用了我们的Fain客户端我们打开浏览器去访问没有问题这个服务可以获取到
[03:14] 那是现在那么如果要测试刚才的一个超时的话我们现在可以在我们的服务提供工程中把这个睡眠两秒的给打开好当时被我们注视掉了现在把它打开来因为我们设置的control F9让他重新编译并加载我们就不用重启我们刚才配置超时时间是两秒钟那现在程序就要两秒还要
[03:42] 一个请求的时间所以一定是会超过两秒的那如果超过两秒呢就会一个进行报错因为它已经超时了我们现在又没有做一个服务的熔断或是一个降级所以呢它直接会提示一个错误信息那刚刚是好的现在被我们这样改了以后那么它就会实现达到一个超时时长那么打开来再去刷新一下就这个地址刷新好就报错了因为它已经超时这是我们的一个关于负载均衡的配置
[04:14] 配置后接下来继续回到讲义中往下走下一个是我们的highstrixhighstrix也是自动已经集成了的那么只要去配置一个开启就可以去使用我们来去配置在fam中的highstrix的开启开启后我们还要去编写一个客户在编写一个这个服务降级的类里面要去返回一个当服务是处理失败的时候
[04:47] 这样的一个服务降级返回结果那前面呢我们是写在类里边现在要单独写一个类那写了以后呢我们在find客户端中去指定当服务降级的时候调用哪一个类里面有一个方法你的方法跟你的请求方法名是要保持一致的好现在呢我们去按照这些步骤去实现首先要开启打开配准键开启好这就很明显是有问题的
[05:25] 这才没有问题这条线出来了这才是一个标准的书状层级结构EMO配置文件开启以后接下来我们要去造一个这样的服务降级类这个类的特征呢就是针对我们的这个处理器这个我们的FAN客户端它里面的各个方法当请求失败的时候应该是要用哪一个服务降级的方法所以这个方法名是跟它一致的既然是一致那我们就去
[05:53] 继承实现这个接口就可以了好所以我们编写一个这样的服务降级类放到一个包里面fallback.userclientfallback实现userclient标注它是一个组件component实现的方法ctrl o就可以了这里面我们再去
[06:37] 返回一个类型是user那我们既然已经失败的那么就返回一个失败的用户对象有了以后我们给他设置一下ID可以设置回去ID除此以外呢我们可以设置点set name来个用户异常返回这个user那我们的服务降级处理类也就编写好了编写好以后呢需要在我们的这个fame客户端中去指定
[07:15] 要去应用这个forbat也就是服务降级类所以我们这个就不再这样默认去写了要在这边去设置value要等于这个值还有可以设置它forbat那forbat呢我们刚刚已经写了一个叫userclientforbat我们指定它改了以后呢接下来我们再去测试我们来重启服务消费工程起了以后呢我们再去验证看一下
[07:45] 当现在如果是出现了一个请求失败的时候他是不是还提示这么一个信息理论上现在应该提示的就是我们返回的服务降级方法里面的返回结果也就是这个user好我们现在呢还是在服务的提供工程中这个程序两秒没有去掉的好现在也就是会引发超时那应该他要返回的是我们服务降级里面的一个返回结果这个user对象ID会有
[08:12] 但是它的名称是用户异常这么一个信息所以我们现在打开浏览器再去刷新这个地址再刷好就已经出现我们期待的结果已经被服务降级处理了它当出现异常的时候有问题的话那么它就会实现去我们的降级方法到降级方法中返回一个降级方法里面的对应结果我们配置是没有问题的应用也成功大家要跟我们前面的这个直接用
[08:44] high stress的一个区别前面呢我们直接在处理器里面去编写这些降级的方法那现在呢如果用了我们的fine客户端那是可以要需要去编写一个这样的服务降级的类然后再去实现这个fine客户端里面的各个方法每一个方法有错的那就对于哪一个方法去调用返回好这就是我们的一个high stress的支持配置开启好完了以后接着我们下一个我们回到讲义中
[09:13] 下一个呢我们可以去配置它的一个请求压缩请求压缩的意思就是当如果我们的请求或者是响应返回的数据呢可以使用这个ZZIP进行压缩也就是减少通信过程中的性能损耗它请求数据量就不会那么大可以去开启这个压缩的那我们也可以去开启只是这个开启以后呢我们不太好去测试因为你这个到底压缩了多少它也没有具体的显示
[09:42] 但是我们可以去配置好配置我们打开来在配置硬件中同样的我们去添加刚才说到这几个配置好又是一个范里面的所以我们把这个给去了那这一个我们把它删除这个好配置好还有是一个respon也可以改成是打开启动一个压缩好就响应的压缩这是请求的信息进行压缩
[10:40] 好这个配置配了以后呢我们验证标准就只能是重启这个服务看一下有没有报错如果没有报错那么就默认它是生效的正在启动中好没有报错没有报错我们就回到讲义中继续往下走来配置一个日志级别那日志级别呢我们可以通过一个lock.level然后指定哪一个哪一些包的日志记录级别那么的fan客户端也
[11:16] 会进行生效就是但是你要去配置一下在我们的Fend客户端类上面去指定一个配置类配置以后呢再去编写一个配置类刚才说了然后是可以去定义日志的级别那Fend呢支持四种的日志级别分别是不记录任何日志信息这是默认的还有一个Basic进记录请求的方法URL以及响应状态码和执行时间Headers
[11:44] 在这个basic的基础上额外记录了请求和响应的头信息-是记录所有请求和响应的明细那我们来记录一个详细的一个日志信息它就是-这个级别那我们去编写包括去开启配置这个的意思是针对哪一个包里面的你可以不一样OK现在呢我们来去按照步骤去配置它最后要在我们的Fancl端去引用这个配置类我们就可以去见到这个配置的日志信息在
[12:14] 后台会输出OK接下来我们去开启配置开启的日志记录级别是debug级别编写一个配置类那这个配置类呢我们配置的是所有详细的信息都记录下来的一个级别就是负所以我们来去编写一个配置类把它放到这个包里面来一个叫做fameconfig标注它是一个配置configuration这里面呢
[13:07] 写一个注册一个bin这个bin返回的是日志的级别那么其实直接返回log.level.fan里边的return log我们用的是log.level.for详细的日志信息好这个的意思就是记录所有请求
[13:59] 和响应的明细那就包括了投信息请求体原数据等这些信息都会被记录下来这样写了以后呢还不会生效那我们要去设置在我们的Fend客户端中去设置这个配置Configuration我们把刚才写的叫做Fend配置配置好以后我们接着再来重启我们的服务消费工程
[14:41] 你改了我们工程的配置包括添加了一些代码好所以去重启重启后呢接下来一会我们在控制台中去看它的一些请求的明细信息因为刚刚把我们的服务提供工程里面的这个方法呢设置了一个沉睡的时间我们可以把它再次给注视掉Ctrl F9接着我们再打开浏览器去访问刷新正常的信息输出
[15:28] 我们在控制台呢就应该要记录刚才的一些明晰信息这是我们的服务消费工程也就在这里边好你要去记录这些信息因为我们的这个Fan code端是这个包下面的所以他记得是debug级别日志信息包含了这些请求头还有响应的一些信息全部会记录下来这就是我们一个在Fan中的日志级别的配置好我们现在回到讲义中回到对
[15:57] 讲一种我们去继续了解就刚才这几个级别呢以后大家可以选择性的去配置尤其是这个debug不一定是要在所有项目中都要这样做的如果以后你的项目呢是要部署到用户那边了那这个debug级别就会比较大你应该调整info和won级别会比较合理一些所以要注意这是我们的fan中配置的几个组件已经配置完成回到笔记中去
[16:27] 小结在小结中我们就把配置文件中在服务消费工程consumer-demo中的配置文件我们把它给转过来刚刚加的一些配置项大家以后自己做的时候会更加好去复制把它拿过来服务的消费工程在这里边
[16:56] 添加了配置项我们刚才加了这一系列的其他的至于代码在我们的讲义中有详细的说明那只是这一个呢大家复制的时候可能不太好复制所以我把它拿过到笔记中来拿过到笔记里边让你去再跟进这一段代码的时候呢更加好复制这就是我们FAN负载均衡和及熔断的所有内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Cloud 中使用 Feign 客户端配置 Ribbon 负载均衡、Hystrix 熔断以及日志级别，并通过代码和配置文件进行演示。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 Feign 客户端接口定义，用于调用 user-Service 服务，并介绍目标是配置 Ribbon 和 Hystrix 的配置。
画面2: 展示 application.yml 中的 client、ribbon 和 hystrix 配置，包括服务发现地址、超时时间、熔断阈值等。
画面3: 展示 Feign 内置 Ribbon 的超时配置说明，并提示修改 application.yml 文件。
画面4: 展示 UserClient 接口定义，包含注解 @FeignClient 和 @GetMapping。
画面5: 展示 UserClientFallback 类的实现，用于处理服务调用失败时的降级逻辑。
画面6: 展示浏览器访问 localhost:8080/c/6，返回用户信息 JSON 数据。
画面7: 展示 application.yml 中 hystrix 配置项，包括 enabled、compression、request、response 等。
画面8: 展示如何通过修改 application.yml 设置日志级别，并创建 FeignConfig 类来定义日志级别。
画面9: 展示在 IntelliJ IDEA 中右键点击目录，选择新建文件或类。
画面10: 展示 FeignConfig 类的代码，用于配置 Feign 客户端的 fallback 类。
画面11: 展示 UserClient 接口定义，包含 @FeignClient 注解和 @GetMapping 注解。
画面12: 展示 UserClient 的调用日志，显示服务调用成功和失败的详细信息。
画面13: 展示 UserController 类的代码，包含 @RestController 注解和 queryById 方法。
画面14: 展示最终的配置文件内容，包括 ribbon、hystrix、feign、logging 等配置项。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2:
```yaml
spring:
  application:
    name: consumer-demo
  cloud:
    client:
      Service-url:
        defaultZone: http://127.0.0.1:10000/Eureka
    # 服务注册中心的刷新间隔，默认30秒
    registry-fetch-interval-seconds: 10
  hystrix:
    default:
      execution:
        isolation:
          Thread:
            timeoutInMilliseconds: 2000
    circuitBreaker:
      errorThresholdPercentage: 50 # 装载阈值，超过50%会触发熔断
      sleepWindowInMilliseconds: 10000 # 熔断后等待时间，单位毫秒
      requestVolumeThreshold: 10 # 熔断触发的请求数量，单位请求
    ribbon:
      ConnectTimeout: 1000 # 连接超时时间
      ReadTimeout: 2000 # 读取超时时间
      MaxAutoRetries: 0 # 最大重试次数
      MaxAutoRetriesNextServer: 0 # 重试多少次服务
      OkToRetryOnAllOperations: false # 是否对所有的请求方式重试
```

画面3:
```yaml
ribbon:
  ConnectTimeout: 1000 # 连接超时时间
  ReadTimeout: 2000 # 读取超时时间
  MaxAutoRetries: 0 # 最大重试次数
  MaxAutoRetriesNextServer: 0 # 重试多少次服务
  OkToRetryOnAllOperations: false # 是否对所有的请求方式重试
```

画面7:
```yaml
hystrix:
  enabled: true # 开启hystrix熔断功能
  compression:
    request:
      enabled: true # 开启请求压缩
      mime-types: text/html,application/xml,application/json # 设置压缩的响应类型
      min-request-size: 2048 # 设置触发压缩的最小大小
    response:
      enabled: true # 开启响应压缩
```

画面8:
```java
package com.ithema.consumer.config;

import feign.Logger;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class FeignConfig {

    @Bean
    Logger.Level feignLoggerLevel() {
        // 记录所有请求和响应，包括头信息、请求体、元数据
        return Logger.Level.FULL;
    }
}
```

画面10:
```java
package com.ithema.consumer.client;

import com.ithema.consumer.client.fallback.UserClientFallback;
import com.ithema.consumer.pojo.User;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@FeignClient(value = "user-Service", fallback = UserClientFallback.class, configuration = FeignConfig.class)
public interface UserClient {

    @GetMapping("/user/{id}")
    User queryById(@PathVariable Long id);
}
```

画面13:
```java
package com.ithema.user.Controller;

import com.ithema.user.pojo.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/user/{id}")
    public User queryById(@PathVariable Long id) {
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return userService.queryById(id);
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1: PPT 标题为“2. Feign负载均衡及熔断”，目标是配置 Feign 内置 Ribbon 和 Hystrix 的配置。
画面3: PPT 标题为“1.4. Hystrix支持(了解)”，内容包括 Feign 内置 Ribbon 的超时配置说明。
画面8: PPT 标题为“2.2. 日志级别”，内容包括如何通过修改 application.yml 设置日志级别。
画面14: PPT 标题为“小结”，内容包括在消费者工程 consumer-demo 中的配置文件内容。

5) 无。

