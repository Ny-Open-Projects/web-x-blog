# 10-SpringBoot自动配置-自定义starter实现-2

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\10-SpringBoot自动配置-自定义starter实现-2_【海量资源尽在 ubkz.com】.mp4
- 时长 7分9秒（音频 429s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 自定义完这个Redis的Starter之后呢接下来我们先来这样我们把这个Redis获取到了之后我们来操作一下要想操作它呢我们首先呢得把这个Redis给它起起来我们就起本机的这个Redis Server然后同样呢我们把Client呢看一下它有没有数据啊case case7看一下没数据empty list outside空的对吧空的之后呢我们可以来去给它存点数据啊
[00:30] Jadis.比如说我们set一下比如说存一个nameitcast存完了之后呢我们也可以获取一下get通过name获取一下看一下能不能把itcast获取到sot一下name好重新运行一下可以来看一下这个itcast是不是就打印出来了那么也同样我们可以在客户端里面来看一下get比如说get name
[01:03] 好你看IDcast是不是也同样的存到了我们本地的这个Redis的机器里边去测完了之后呢接下来我们来做一些分析首先第一个事我们刚才说呀在这个里边呢它是不是会加载配置文件对吧而且呢加载哪个配置呢以Redis为开头的那些配置会和这个Redis的properties是不是相绑定啊我们可以来试一下啊好我们在我们的enable哪个地方要用Redis的地方我们来配它
[01:32] 在这里边呢我们给它定义配置当然properties和yaml都是可以的我们定义redis.dir比如说我们来定义一个port好port等于谁呢等于6666对吧将来这个端口肯定是不对的那么不对的话就会意味着我们这个jetis获取一定会失败那么不是获取会失败就是存储的时候这个地方会去存储发送一个连接请求那么连接会失败失败了呢它就会报错
[02:02] 如果报错就证明这个参数是不是识别了OK我们可以来尝试一下重新运行一下OK你看这个地方是报错了报什么错呢他说failed connecting连接失败从哪个连接失败的呢hosthost谁呢localhost冒号6666对不对就失败了所以呢证明我们这个配置是不是生效的没有问题那么将来用户要用你的redis的starter的时候呢他可以来指定
[02:36] 端口可以指定host的主机名当然其他的我们都没有去配好先删掉为了保证正常使用第一个事说完了之后接下来我们来说第二个事那么现在当我们的程序启动的时候这个bin就会被加载对吧我们可以给它加一些条件比如说at condition on比如说on class我们要保证这个Jadis在的时候我们才去加载这几个bin可以吧
[03:03] 当然这里边有很多将来其实我们就写了这么一个然后第二个呢如果用户他自己也定义了一个名字叫Jadis的病那你就用他自己定义的呗你就不要去加载了要不是两个会起冲突的对吧所以呢这个地方我们就写一个condition on missing bin也就是说如果没有一个名字叫JadisJadis的病的时候然后呢我们才提供
[03:32] 这么一个给他提供一个并如果他定义好了一个叫做Jadis的并我们就不提供了用他自己定义的那么我们可以来测试一下下边这个事为了测试方便啊我们在这个地方打印一句话我们打印一个我们这个名字打一个名字好打一个名字之后呢我们可以来看一下我们来看一下我们这个里边获取啊获取的时候呢注意现在呢我们来运行一下
[04:01] 那么刚才那个方法呢肯定是会被执行的对吧你看这个地方呢是不是就执行了这个打印了说明了我们这个地方的auto configuration的这个genesis这个方法是被执行了并且呢这个bin是被创建出来了OK那么接下来呢我们可以这样来做我们在我们自己的这个配置啊这个类里边就是我们自己定义的这个类里边这玩意里边呢是不是也相当于是一个configuration因为刚才我们看到了嘛
[04:29] 它里边是不是就是一个Spring Boot ConfigurationOK那么里边呢我们也可以来定义一个bin定义一个bin定义一个bin也叫一个同样的名叫做JadisJ-E-D-I-SJ-E-D-I-S也叫Jadis那么叫这个地方呢叫Jadis呢我们也同样return一个new一个Jadis里边呢我们就写loc localhost然后呢
[05:00] 6379好嘞那么接下来我们自己有一个Jadis的bin了那么我们看一下他给我们jar 包里边提供的这一句话还会不会打印如果没打印说明这个unmissingbin是生效的来看走来看一下日志信息没有打印吧OK说明这个unmissingbin是不是也是OK的
[05:30] 那么至此呢我们这个Redis对应的一个起步依赖整个流程其实我们都跑完了可以看到其实基本上呢Spring Boot它就是这样做的那么最后呢我们也可以来看一下整个的真正人家怎么定义的我们可以看一下它的一个过程打开一个这个地方的Spring Boot的Auto Configure这么一个包号这个名然后呢点开
[05:57] 它在里边呢提供了非常多的一些类非常多各种各样的然后Data里边呢有一个叫做RedisOK打开Redis的Auto Configuration这么一个自动配置的核心的配置类点开之后呢看首先呢配置类对吧好On Class当这个Class在的时候才会去加载这些币没有问题吧OK那么接下来呢它启动了一个Enable Configuration Properties
[06:28] 定义了一个叫做redis的properties跟我们起的名是不是一样的我们点进去看你看里边是不是有很多很多的信息它的前置叫做sprint.redis对吧跟我们写的不太一样好然后呢接下来你看它的host是不是默认值给了个logo host它已经写死了嘛对吧将来你配置文件里边改了那么就用改之后的没有配置就用这个默认的值并且呢port它给你指定成6379基本的逻辑呢其实跟我们做的都差不多
[06:57] 只不过人家弄得更加的严密严谨一些那么这个自定义的Starter我们就说到这个地方

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中通过自定义配置类和配置属性类，实现对 Redis 客户端（Jedis）的自动配置与注入。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 Spring Boot 应用的主类中，通过 context.getBean(Jedis.class) 获取 Jedis 实例并打印，演示了手动获取 Bean 的方式。
画面 2: 在主类中调用 jedis.set("name", "itcast");，向 Redis 写入数据。
画面 3: 展示了 application.properties 文件，用于配置 Spring Boot 应用。
画面 4: 在 application.properties 文件中，设置了 redis.port=6379。
画面 5: 展示了 RedisAutoConfiguration.java 文件，其中包含 @Configuration 和 @EnableConfigurationProperties(RedisProperties.class) 注解，用于自动配置 Redis。
画面 6: 在 RedisAutoConfiguration.java 中，定义了 @Bean 方法，用于创建 Jedis Bean。
画面 7: 在 RedisAutoConfiguration.java 中，为 Jedis Bean 添加了 @ConditionalOnMissingBean(name = "jedis") 注解，确保只有当没有同名 Bean 时才创建。
画面 8: 展示了 RedisProperties.java 文件，用于定义 Redis 的配置属性。
画面 9: 在 Spring Boot 应用的主类中，通过 context.getBean(Jedis.class) 获取 Jedis 实例并打印。
画面 10: 在 RedisAutoConfiguration.java 中，为 Jedis Bean 添加了 @ConditionalOnMissingBean(name = "jedis") 注解。
画面 11: 在 Spring Boot 应用的主类中，通过 context.getBean(Jedis.class) 获取 Jedis 实例并打印。
画面 12: 在 Spring Boot 应用的主类中，通过 context.getBean(Jedis.class) 获取 Jedis 实例并打印。
画面 13: 展示了 Spring Boot 自动配置的源码结构，其中包含 RedisAutoConfiguration 类。
画面 14: 展示了 RedisProperties.java 文件，其中定义了 Redis 的配置属性，如 host、port、password 等。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```java
Jedis jedis = context.getBean(Jedis.class);
System.out.println(jedis);
```

画面 2:
```java
jedis.set("name", "itcast");
```

画面 3:
无代码，仅展示 application.properties 文件。

画面 4:
```properties
redis.port=6379
```

画面 5:
```java
package com.ltheima.redis.config;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Configuration;
import redis.clients.jedis.Jedis;
@Configuration
@EnableConfigurationProperties(RedisProperties.class)
public class RedisAutoConfiguration {
```

画面 6:
```java
@Bean
public Jedis jedis(RedisProperties redisProperties){
    return new Jedis(redisProperties.getHost(),redisProperties.getPort());
}
```

画面 7:
```java
@Bean
@ConditionalOnMissingBean(name = "jedis")
public Jedis jedis(RedisProperties redisProperties){
    return new Jedis(redisProperties.getHost(),redisProperties.getPort());
}
```

画面 8:
无代码，仅展示 RedisProperties.java 文件。

画面 9:
```java
Jedis jedis = context.getBean(Jedis.class);
System.out.println(jedis);
```

画面 10:
```java
@Bean
@ConditionalOnMissingBean(name = "jedis")
public Jedis jedis(RedisProperties redisProperties){
    return new Jedis(redisProperties.getHost(),redisProperties.getPort());
}
```

画面 11:
```java
Jedis jedis = context.getBean(Jedis.class);
System.out.println(jedis);
```

画面 12:
```java
Jedis jedis = context.getBean(Jedis.class);
System.out.println(jedis);
```

画面 13:
无代码，仅展示 Spring Boot 自动配置的源码结构。

画面 14:
```java
private String host = "localhost";
private int port = 6379;
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无 PPT 标题、架构图/流程图或表格数据。

5) 不评价画面美观，不输出与课程无关的内容。

