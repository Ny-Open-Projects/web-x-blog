# 04-分布式锁（为什么要使用分布式锁_1） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是讲了一下什么是分布式锁

那接下来呢,我们来看下一个小节

就是为什么要使用分布式锁

那么我们这个地方呢

会通过一个电商项目当中

减库存的这个案例来演示啊

如果在没有分布式锁

这个时候呢,会出现什么问题

通过这个效果的演示呢

咱们就能够看到为什么要使用分布式锁,对吧

因为在我们这种分布式环境下边呢

如果没有分布式锁的话呢

很容易出现这种什么呢

这种数据不一致的这种情况

那接下来呢,我们就通过代码的方式呢

把这个效果呢,给展示出来

咱们呢,还是在我们刚才创建的这个

Maven工程的基础之上来开发就可以了

因为我们在这儿呢,要操作Redis啊

所以说呢,我们在这里边呢

需要导入一些这个坐标

因为我们这个地方呢,要减库存,对吧

这个库存这个数据啊

我们并没有存储在数据库当中

而是存到了我们的Redis当中

啊

好,先把这个Parent这块呢

因为我们当前呢,要使用Spring Boot,对吧

所以需要让它来继承一下

把这个关了

让我们当前这个Maven工程来继承

Spring Boot的Starter Parent,对吧

这个副工程

然后接下来呢,把我们这个坐标呢

给拷过来

直接拿过来

这里边呢,重点就是来看一下这个啊

就是我们这个Spring Boot的Starter

Starter,对吧

Data Redis

好,这相当于是对Redis的

进行了一个集成,对吧

Spring对Redis进行了一个集成

好

好,那么这个导完之后呢

接下来呢,我们就需要来

创建Spring Boot的一个配置文件,对吧

是不是叫做application.yml

好

然后在这呢,咱们来配置一下什么呢

一个是server.part,对吧

端口号呢,我们就使用8080

就可以了

然后接下来呢,是需要来配置我们

这个Spring跟Redis,对吧

Spring要整合Redis了

Spring.redis

.什么呢

一个是host

这个host的话呢,咱们没有使用本地的

使用的是我们远程的一个服务

当前呢,我们这个Redis呢

其实已经跑起来了

6379

68,应该是6879

6342

好

咱们直接从这边来抄一下也可以啊

你看,6879,6342

然后还有就是端口号

还有就是密码,对吧

好,这儿整理一下

OK

注意这个端口号呢,我们用的并不是默认的6379

而是用的这个端口号啊

咱们现在呢,可以来看一下

连上咱们这个Redis

通过我们这个客户端

连接一下,你看

6879,6342

好,这里边呢,我们准备了这么一个数据啊

它的key呢,是stock

对吧

这代表的就是我们库存数量

库存,对吧

然后呢,它的值呢,是50

当前呢,说明我们这个库存呢

还有50个

一会儿呢,我们就要操作这个数据

好

先把这个数据准备好

并且呢,我们这儿是不是也已经配置好了

配置好之后呢

我们就可以来创建一个controller,对吧

咱们通过controller呢

来接收客户端发过来的请求

然后在controller当中呢

我们需要来注入这么一个对象啊

叫做Redis template

为什么我们直接能注入这个对象呢

就是因为我们当前呢

已经导了相关的这个坐标,对吧

并且呢

在这个地方呢

也已经配置了Redis这个连接信息

那这样的话呢

我们可以来看一下

在我们导入的这个坐标里边

其中有这么一个架包啊

就是这个Spring Boot Auto Config,对吧

是不是完成自动配置的

然后在这里边呢

是不是有这么一个叫做Sprinter Factories

那么熟悉我们这个Spring Boot的

它的启动呢

大家应该都知道

在我们项目启动的时候呢

会加在我们架包里边

所有的这个什么呢

MetaInfo下边

这个的Sprinter Factories这个文件都会加载

然后在这个文件里边呢

它其实就会配置一些什么呢

自动配置类,对吧

你看Enable Auto Config

Auto Configuration是不是来启用我们这个自动配置

其中呢

这里边是不是就有我们这个Redis的

Redis Auto Configuration

然后呢

我们直接点进来

你看也就是说在我们项目启动的时候呢

这个类呢

是不是也会被加载

当然了

它是有条件的对吧

它是有条件的

你看这是不是叫做Conditional On Class

也就是我们当前这个类路径下面呢

需要有这个类

对吧

需要有这个类

并且呢

什么呢

我们要创建的是不是就是这个Redis Template

而它的话呢

是不是要什么呢

当missing bin

就是没有它的时候是不是才去创建它

但是我们现在用的其实是下边这个Spring

这个String那个

你看我们注入的是这个叫String

Redis Template

也就是这个

这个是什么呢

是如果说我们Spring容器里面没有对吧

Conditional On Missing Bin

没有这个bin的时候呢

就会把它创建出来

因为在这呢

是不是已经加了bin这个注解对吧

就表示创建这个对象

然后下面这条件当没有它的时候才创建

然后呢

我们把它创建出来就可以了

所以说呢

我们这个地方通过自动配置类呢

已经将我们这个对象给创建好了

所以在我们这个项目里面呢

我们这个项目里面呢

我们这个项目里面呢

这个controller当中啊

直接注入就可以了

这是我们大概来看了一下

就是由于我们Spring Boot呢

支持这种什么的自动配置对吧

好

自动装配

然后呢

我们可以在这来创建一个controller包

在这呢

来创建一个controller

咱们就叫stock controller吧

好

在这呢

来加一个注解

rest controller

然后呢

我们把刚才看到的那个什么

String

Redis template

把它直接注入进来就可以了

注入进来之后干什么事呢

咱们是不是要进行这个简库存的操作对吧

进行简库存的操作

说白了就是我们使用这个redis template

是不是来操作我们刚才看到的这个redis数据对吧

把这个数据呢给它减个1

其实就这么回事啊

这个代码的话呢

我们直接拿过来啊

然后呢

我就不再手敲了

咱们大概来读一下这个代码

好

这就表示

库存减了个1

减完之后呢

重新给它set回去

注意set的时候呢

因为它是int类型啊

那么我们在这呢

要接收的是

你看这个set的方法

接收的是String方式的value对吧

String的这种类型

所以说呢

我们给它加一个空串

这样是不是就给它转成了这种什么呢

String类型

好

值的话呢

其实就是这个值

好

相当于给它减完1之后

是不是又重新设置回去

然后呢

我们在这控制台说出一句话

就是说

库存扣减1

减成功对吧

然后呢

剩余库存是多少

我们可以来输出一下

如果是else说明

是不是已经减到0了对吧

已经不大于0了

这个时候呢

我们就说库存不足

好

注意看啊

我们当前呢

并没有去使用什么锁机制对吧

甚至我们现在连这个synchronize的那个锁

是不是也都没有加

那也就是说

当前我们对这个方法

没有进行任何控制

那这个时候

如果我们要是并发来请求的话呢

大家可以想象一下

我们现在呢

这个数据呢

其实是有问题的

对吧

这是我们当前呢

是没有进行任何控制的情况下

咱们可以来看一下这个代码

对吧

它其实是有这个隐患的

好

那接下来呢

我们来编写这个什么呢

咱们这个启动类啊

注意这个是启动类

在这来改一下

把我们这个项目跑起来

就在我们这来创建这么一个

叫做myapplication

好

这个代码呢

我就不再写了

非常简单

好

这就是启动我们这个

Spring boot工程

对吧

然后呢

我们来看一下到这儿的话呢

咱们这个代码呢

其实就已经好了

对吧

设置redis

刚才我们已经设置过了

设置过了

这样的话

我们这个程序就已经提供好了

一会儿呢

我们可以来测试一下

刚才呢

我们也提出来了

其实这儿其实是有问题的

因为我们当前的还没有加锁机制

我们就是给大家来看一下

在没有锁的情况下

那么有可能会出现什么问题

然后呢

我们再逐步去解决它

给它加锁

对吧

然后呢

前后对比

那么这样的话呢

就能说明我们这个锁机制

它到底能起到什么样的作用

好

咱们这是先把我们这个运行的

这个项目环境呢

来搭建了一下

一会儿呢

我们先基于这个

没有锁机制的这个代码

来进行一个测试

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是关于“分布式锁”技术的入门教程，旨在通过一个电商减库存的实战案例，演示在没有分布式锁的情况下，如何因并发问题导致数据不一致。视频主要讲解了如何使用 Redis 来实现一个简单的分布式锁方案。内容涵盖了项目初始化、配置文件编写、Redis客户端连接、Spring Boot 配置、以及核心的库存扣减控制器代码。视频最后提示了后续将介绍更完善的 Redisson 分布式锁方案。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，讲师在 Typora 文档中展示课程大纲，当前章节为“1.2 为什么要使用分布式锁”。
*   **00:00:05 - 00:00:15**：讲师解释了为什么需要分布式锁，指出在分布式环境下，即使使用 `synchronized` 或 `ReentrantLock` 这样的 JVM 级别锁，也无法控制跨 JVM 的并发问题，因此必须使用分布式锁。
*   **00:00:15 - 00:00:25**：讲师展示了一个简单的电商减库存的案例，用以说明没有分布式锁时会出现的问题。
*   **00:00:25 - 00:00:35**：讲师开始演示如何搭建项目，首先在 IntelliJ IDEA 中创建一个名为 `lock-test` 的 Spring Boot 项目，并导入 `pinda-tms-java` 项目作为依赖。
*   **00:00:35 - 00:00:45**：讲师在 `application.yml` 配置文件中设置 Spring Boot 的端口号为 `8080`。
*   **00:00:45 - 00:00:55**：讲师在配置文件中添加了 Redis 的连接信息，包括主机地址、端口和密码。
*   **00:00:55 - 00:01:05**：讲师在 Redis Desktop Manager 中连接到 Redis 服务器，并查看 `stock` 键的初始值为 `50`。
*   **00:01:05 - 00:01:15**：讲师在 `application.yml` 中配置了 Spring Boot 的自动配置类 `RedisAutoConfiguration`。
*   **00:01:15 - 00:01:25**：讲师编写了 `RedisAutoConfiguration` 配置类，用于创建 `RedisTemplate` 和 `StringRedisTemplate` 的 Bean。
*   **00:01:25 - 00:01:35**：讲师在 `StockController` 中编写了处理 `/stock` 路径的 REST 接口，用于模拟库存扣减操作。
*   **00:01:35 - 00:01:45**：讲师在控制器中编写了核心逻辑：先获取库存值，如果大于 0，则减 1 并更新；否则提示库存不足。
*   **00:01:45 - 00:01:55**：讲师展示了 `MyApplication` 启动类，并提示将使用 JMeter 进行压力测试。
*   **00:01:55 - 00:02:05**：讲师在控制器中添加了 `@Autowired` 注解，用于注入 `StringRedisTemplate`。
*   **00:02:05 - 00:02:15**：讲师在控制器中使用 `opsForValue().get("stock")` 获取 Redis 中的库存值，并使用 `opsForValue().set("stock", stock-1)` 更新库存。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   课程大纲：`1.1 什么是分布式锁`、`1.2 为什么要使用分布式锁`、`1.3 分布式锁应具有的特性`、`2. 分布式锁实现方案`、`3. Redisson`、`4. 导入功能代码`。
    *   项目结构：`lock-test` 项目，包含 `src/main/java`、`src/main/resources`、`pom.xml` 等标准目录。
    *   配置文件：`application.yml`，包含 `server.port`、`spring.redis.host`、`spring.redis.port`、`spring.redis.password` 等配置项。
    *   启动类：`MyApplication.java`，包含 `@SpringBootApplication` 和 `main` 方法。
    *   控制器：`StockController.java`，包含 `@RestController`、`@GetMapping`、`@Autowired` 等注解。

*   **代码关键内容**：
    *   **`application.yml` 配置**：
        ```yaml
        server:
          port: 8080
        spring:
          redis:
            host: 68.79.63.42
            port: 26379
            password: itheima123
        ```
    *   **`RedisAutoConfiguration` 配置类**：
        ```java
        @Bean
        @ConditionalOnMissingBean
        public RedisTemplate<Object, Object> redisTemplate(RedisConnectionFactory redisConnectionFactory) throws UnknownHostException {
            RedisTemplate<Object, Object> template = new RedisTemplate<>();
            template.setConnectionFactory(redisConnectionFactory);
            return template;
        }

        @Bean
        @ConditionalOnMissingBean
        public StringRedisTemplate stringRedisTemplate(RedisConnectionFactory redisConnectionFactory) throws UnknownHostException {
            StringRedisTemplate template = new StringRedisTemplate();
            template.setConnectionFactory(redisConnectionFactory);
            return template;
        }
        ```
    *   **`StockController` 控制器代码**：
        ```java
        @RestController
        public class StockController {
            @Autowired
            private StringRedisTemplate redisTemplate;

            @GetMapping("/stock")
            public String stock() {
                int stock = Integer.parseInt(redisTemplate.opsForValue().get("stock"));
                if (stock > 0) {
                    stock--;
                    redisTemplate.opsForValue().set("stock", stock + "");
                    System.out.println("库存扣减成功，剩余库存：" + stock);
                } else {
                    System.out.println("库存不足！！！");
                }
                return "OK";
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖导入** (00:00:25 - 00:00:35)
    *   讲师在 IntelliJ IDEA 中创建了一个名为 `lock-test` 的 Spring Boot 项目。
    *   讲师通过 Maven 依赖管理，将 `pinda-tms-java` 项目作为依赖导入，为后续的业务逻辑提供支持。

*   **场景二：配置文件编写** (00:00:35 - 00:01:05)
    *   讲师在 `application.yml` 中配置了 Spring Boot 的端口号为 `8080`。
    *   讲师配置了 Redis 的连接信息，包括主机地址 `68.79.63.42`、端口 `26379` 和密码 `itheima123`。
    *   讲师在 Redis Desktop Manager 中连接到 Redis 服务器，并查看 `stock` 键的初始值为 `50`。

*   **场景三：Spring Boot 自动配置** (00:01:05 - 00:01:25)
    *   讲师在 `RedisAutoConfiguration` 类中，通过 `@Bean` 注解创建了 `RedisTemplate` 和 `StringRedisTemplate` 的 Bean。
    *   讲师通过 `@ConditionalOnMissingBean` 注解，确保只有在没有其他配置的情况下才会创建这些 Bean。

*   **场景四：控制器编写与核心逻辑** (00:01:25 - 00:01:45)
    *   讲师在 `StockController` 中编写了处理 `/stock` 路径的 REST 接口。
    *   讲师使用 `@Autowired` 注解注入 `StringRedisTemplate`。
    *   讲师使用 `opsForValue().get("stock")` 获取 Redis 中的库存值，并使用 `opsForValue().set("stock", stock-1)` 更新库存。

*   **场景五：压力测试准备** (00:01:45 - 00:02:05)
    *   讲师展示了 `MyApplication` 启动类，并提示将使用 JMeter 进行压力测试。
    *   讲师在控制器中添加了 `@Autowired` 注解，用于注入 `StringRedisTemplate`。
    *   讲师在控制器中使用 `opsForValue().get("stock")` 获取 Redis 中的库存值，并使用 `opsForValue().set("stock", stock-1)` 更新库存。

---

以上是根据视频
