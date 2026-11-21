# 14-分布式锁实现方案（Zookeeper方式实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢我们是分析了一下

我们使用Zookeeper这种方式来实现分布式锁

它的原理其实还是比较简单的

就是大家都到我们Zookeeper的某个节点下边

去创建这种临时顺序节点

然后呢再来比较一下

看看哪一个节点,对吧

它的这个编号最小

那么所对应的那个客户端呢

就相当于获得了锁

那么这是咱们这个原理

那么实际上我们如果使用原生API

就是自己写代码,自己去实现

比如说我们要到这个MyLock节点下边来创建一个节点

并且呢创建完之后呢

再比较跟其他的客户端创建的节点

再来进行比较,对吧

最终呢来确定哪一个是最小的

其实整个这个代码实现起来呢

还是比较繁琐的

虽然原理简单

但是真正写起代码来还是比较繁琐的

所以说呢我们在这个地方呢

就给大家来介绍一个框架

是Apache的叫做Corridor

这个框架呢

它其实就是一个

比较完善的Zookeeper客户端的框架

而在这个框架当中呢

它已经提供好了分布式锁的实现

那么它对这个API呢

进行了封装,进行了简化

所以说呢我们就直接使用它

就可以大大简化这个过程

但是它的底层原理其实都是一样的

对吧,只不过它是做了一个封装

所以我们就不用自己再去写

怎么去创建节点,怎么比较

这些过程全都进行了封装

所以我们就直接使用它

来简化我们的开发就可以了

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

具体的这个操作过程啊

我们就按照下面这个过程来

实践一下就可以了

这个呢还是在咱们前面这个Logtest的

也就是我们这个工程的基础之上

来改造就可以

好

那么我们第一步呢

肯定还是需要来导入相关的

Main坐标

对吧

因为我们这块呢

要操作Zookeeper

所以说呢

需要导入Zookeeper这个客户端

以及还有什么呢

我们刚才提到的这个框架

对吧

那么这个框架呢

对应的有这么两个坐标

好

那接下来呢

我们就把这三个啊

一共这三个坐标

把它复制过来

放到我们这个POM文件里面来

好

这是加包

是不是导过来

然后接下来呢

我们第二步呢

就是来创建一个什么呢

配置类

这个配置类呢

主要就是来干什么呢

创建刚才我们看到的这个框架

Corridor

这个框架里边的一个核心类

这个核心类叫做Corridor Framework

你看是不是

Framework就是框架的

意思

这个呢

其实就是一个客户端对象

使用它呢

就可以连接上我们这个

Zookuber服务

对吧

方便操作它

好

那接下来呢

我们先把这个

先来创建一个包吧

在ID黑码下边

咱们来创建一个Config包

然后在这下边呢

来创建这么一个

叫做ZKConfig

好

具体这里面的代码呢

我就不再手敲了

直接复制过来

咱们来大概读一下

这个代码就可以了

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

,

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

咱们呢

把

上面这个方法

复制一份

这是原始的咱们这个方法

好

这个呢

是基于数据库这种方式实现

对吧

这个呢

我们就把它注视起来

好

然后呢

在下面粘贴一下

这呢

我们加一个注视

这是基于什么呢

基于我们的组keeper这种方式啊

组keeper方式来实现我们的分布式锁

好

然后这个synchronize的

这个就不要了

咱们把这个代码拿出来

把它覆盖掉

好

因为我们已经加了分布式锁了

所以那个synchronize的就不需要了

然后呢

我们在这呢

需要来创建一个对象啊

然后呢

把这个代码

把这个客户端对象给它放进去

这个对象呢

叫这个

叫做什么interprocess mutex

对吧

好

那这个是什么意思呢

这个呢

其实指的就是啊

到我们的组keeper下边

它的竖形结构里面

去创建这么一个

创建这么一个节点

注意这个节点呢

其实是一个什么呢

是一个持久节点

是一个持久节点

因为我们要增强锁的话呢

全都是在这个持久节点下边

去创建这种

临时的节点

就是顺序节点

刚才原理我们也已经多次介绍了

对吧

所以这个mylock呢

它其实对应的是谁呢

对应的就是我们刚才看到的这个图上

这个mylock

然后这些客户端A客户端B呢

都是在mylock这个节点下边

去创建子节点

对吧

创建子节点

然后呢

就是创建这种临时顺序节点

好

所以呢

我们就把它

先来这个创建出来

它是一个

持久的

好

如果已经存在了

它就不再创建了

如果不存在

就把它创建出来

好

创建出来之后啊

我们怎么去获取锁呢

注意

这个对象里边呢

有这么一个叫做

care

这么一个方法

这个表示什么呢

表示尝试获取锁

注意

我说的是尝试

对吧

因为它不一定就能获取成功啊

尝试来获取锁

或者叫做争抢都可以

然后呢

它这呢

要求我们传进去两个参数啊

第一个呢

就是这个等待的时间

第二个呢

是一个

等待的时间

time unit

咱们叫seconds

好

然后这个地方呢

应该是有异常

你看有异常

呃

也就是说它在这个尝试获取的时候呢

有可能会抛异常

所以我们在这呢

来一个

出出

这个是争抢锁

争抢锁

这个异常

好

但是一般情况下是没有问题的

是什么时候可能会有问题啊

比如说连不上组keeper了

对吧

哎

那么连不上了

它有可能会

争抢锁异常

注意这个不是说争抢锁失败

不是说没有争抢到啊

那么它到底有没有争抢到呢

注意你看这个方法呢

它有一个布尔类型的返回值

对吧

哎

如果返回处的话呢

就表示什么呢

表示争抢到了

你看处表示什么呢

这个已经获取到了

所以说呢

我们根据这个返回值来判断啊

它有没有正确

争抢到啊

咱们叫lucked

所以我们在这来判断

if什么呢

它等于处

这就表示什么呢

这表示获取

获取到了这个分布失所

分布失所

那么else呢

那是不是就是没有获取到

哎

那就是没有获取到这个分布失所

那么我们来看一下

大概解释一下这两个参数啊

刚才没有说

这个参数呢

你看这是个时间

对吧

它这个时间

它表示的是什么

这个time代表的是

就是等待的时间

对吧

等待的时间

这是什么意思呢

就是说啊

我们如果有多个线程并发

对吧

那么很显然应该只有一个线程

是不是能够干什么呢

能够争抢到这把锁

哎

能够争抢到这把锁

那么如果其中

比如说第一个线程

它争抢到了

它开始执行下面的业务代码

然后其他没有争抢到的这些线程

它会怎么做呢

注意

它会有一定的等待时间

当然我这写的0就表示什么呢

它不等待

如果写1的话呢

就表示它会等待一秒钟

好

它会等待一秒钟

如果一秒钟之后之内呢

它还抢不到锁

哎

因为这边可能还没执行完了

对吧

还没有释放了

它肯定是抢不到

那这个时候呢

它就会直接返回了

好

所以说呢

这个是等待时间

我们这写0就表示什么呢

不等了

我就抢一下

抢不着直接返回

就是这个意思

好

所以这个呢

就是尝试

这句

就是尝试来获取锁

如果它等于处的话呢

表示获取到了

获取到之后干什么呢

那肯定显然

是不是就执行我们

减库存的操作就可以了

对吧

减库存的操作呢

咱们前面已经写过了

好

减库存的操作

就是这个

好

然后呢

注意

这个执行完之后啊

执行完之后

我们需要干什么

释放锁

执行完之后

需要释放锁

好

释放锁呢

就是还是调用这个对象

Mutex

这个对象

它有一个叫做release

这么一个方法

这就表示释放锁

好

你如果不释放的话呢

别的现场它就抢不到了

所以你用完之后

需要马上把它释放掉

好

如果else的话

表示没有

没有获取到锁

对吧

没有获取到

这个没有获取到的话呢

我们在这

来输出这句话

就可以了

所以你看啊

从代码层面来说呢

其实也是比较简单的

对吧

这是因为我们使用的

这个框架

corrider这个框架

然后呢

直接把这个对象

注进来

注进来之后呢

先连接上它

对吧

然后呢

尝试去创建这么一个

节点

对吧

这是持久节点

然后呢

我们在这个节点下面

去创建临时节点

但是它内部已经封装了

我们直接调这个方法

就可以

它底层呢

就会去创建这个临时节点

并且去比较

看谁的小

对吧

如果返回处的话呢

就说明它这个节点

创建成功

并且是最小的

那么它就获取锁了

那么这个时候呢

就会返回处

返回处的话呢

我们就直接执行

我们相应的这个业务操作

也就是减库存

减完库存之后呢

别忘了去释放锁

好

如果它等于false的话呢

它就会进入else

这个分支

对吧

这个时候呢

就是没有获取到锁

好

这是我们这个代码

是不是就已经写完了

一会儿呢

我们就可以

把咱们组keeper服务呢

跑起来

我们来测试一下

这个效果

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于“品达物流TMS项目”第9章“后台管理端开发”的技术课程，具体讲解如何使用 Apache Curator 框架在 ZooKeeper 中实现分布式锁。讲师首先介绍了分布式锁的背景和 ZooKeeper 的作用，然后演示了如何在 Maven 项目中引入 Curator 相关依赖，接着编写 Spring 配置类来初始化 Curator 客户端，并最终在业务代码中使用 `InterProcessMutex` 类来实现一个基于 ZooKeeper 的分布式锁，用于解决库存扣减的并发问题。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 文档中展示课程大纲，当前章节为“2.2 ZooKeeper实现分布式锁”。
*   **00:00:05 - 00:00:15**: 讲师解释分布式锁的实现原理，通过在 ZooKeeper 的 `/my_lock` 节点下创建临时顺序节点来竞争锁，节点序号最小的客户端获得锁。
*   **00:00:15 - 00:00:30**: 讲师介绍 Apache Curator 框架，说明其通过封装高级 API 简化了 ZooKeeper 的操作。
*   **00:00:30 - 00:00:45**: 讲师开始演示具体操作，第一步是在 `pom.xml` 中导入 Curator 的 Maven 依赖。
*   **00:00:45 - 00:01:00**: 讲师切换到 IntelliJ IDEA，展示项目结构，并定位到 `StockController.java` 文件。
*   **00:01:00 - 00:01:15**: 讲师在 `StockController.java` 中添加 `@Autowired` 注解，用于注入 `CuratorFramework` 实例。
*   **00:01:15 - 00:01:30**: 讲师切换到 `ZkConfig.java` 文件，展示如何编写 Spring 配置类来初始化 Curator 客户端，并设置重试策略。
*   **00:01:30 - 00:01:45**: 讲师在 `StockController.java` 中编写业务逻辑，使用 `InterProcessMutex` 实例来获取和释放分布式锁。
*   **00:01:45 - 00:02:00**: 讲师完善代码，将锁的释放操作 `mutex.release()` 放在 `try` 块的 `finally` 块中，以确保锁的正确释放。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`品达物流TMS项目` -> `第9章 TMS后台管理端开发(pd-web-manager)` -> `2. 分布式锁实现方案` -> `2.2 ZooKeeper实现分布式锁`。
    *   分布式锁原理图：展示了客户端A和客户端B竞争锁的过程，锁节点为 `/my_lock`。
    *   依赖配置：`<dependency> <groupId>org.apache.curator</groupId> <artifactId>curator-recipes</artifactId> <version>2.12.0</version> </dependency>`。
    *   配置类代码：
        ```java
        @Configuration
        public class ZkConfig {
            @Bean
            public CuratorFramework curatorFramework() {
                RetryPolicy retryPolicy = new ExponentialBackoffRetry(1000, 3);
                CuratorFramework client = CuratorFrameworkFactory.builder()
                        .connectString("localhost:2181")
                        .sessionTimeoutMs(5000)
                        .connectionTimeoutMs(5000)
                        .retryPolicy(retryPolicy)
                        .build();
                client.start();
                return client;
            }
        }
        ```

*   **代码关键内容**:
    *   **Maven 依赖**:
        ```xml
        <dependency>
            <groupId>org.apache.zookeeper</groupId>
            <artifactId>zookeeper</artifactId>
            <version>3.4.10</version>
        </dependency>
        <dependency>
            <groupId>org.apache.curator</groupId>
            <artifactId>curator-framework</artifactId>
            <version>2.12.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.curator</groupId>
            <artifactId>curator-recipes</artifactId>
            <version>2.12.0</version>
        </dependency>
        ```
    *   **业务代码**:
        ```java
        @Autowired
        private CuratorFramework curatorFramework;

        @GetMapping("/stock")
        public String stock() {
            InterProcessMutex mutex = new InterProcessMutex(curatorFramework, path: "/mylock");
            try {
                boolean locked = mutex.acquire(time: 0, TimeUnit.SECONDS);
                if (locked) {
                    // 获得了分布式锁
                    int stock = Integer.parseInt(redisTemplate.opsForValue().get("stock"));
                    if (stock > 0) {
                        stock--;
                        redisTemplate.opsForValue().set("stock", stock + "");
                        System.out.println("库存扣减成功，剩余库存：" + stock);
                    } else {
                        System.out.println("库存不足！！！");
                    }
                } else {
                    // 没有获得到分布式锁
                    System.out.println("没有获得锁，不能执行减库存操作...");
                }
            } catch (Exception ex) {
                System.out.println("争抢异常...");
            } finally {
                mutex.release();
            }
            return "OK";
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：引入依赖** (00:00:30 - 00:00:45)
    *   讲师在 Typora 文档中展示 `pom.xml` 文件，演示如何添加 Curator 的 Maven 依赖。
    *   画面中显示了三个依赖项：`zookeeper`、`curator-framework` 和 `curator-recipes`。

*   **场景二：配置客户端** (00:01:15 - 00:01:30)
    *   讲师在 IntelliJ IDEA 中打开 `ZkConfig.java` 文件。
    *   画面展示了如何使用 `@Configuration` 注解和 `@Bean` 注解来创建一个 `CuratorFramework` 实例。
    *   代码中设置了连接地址 `localhost:2181`、会话超时和连接超时时间，并配置了指数退避重试策略。

*   **场景三：实现业务逻辑** (00:01:30 - 00:01:45)
    *   讲师在 `StockController.java` 中编写了获取库存的 HTTP 接口。
    *   代码中创建了一个 `InterProcessMutex` 实例，传入了 Curator 客户端和锁路径 `/mylock`。
    *   使用 `acquire` 方法尝试获取锁，成功后执行库存扣减逻辑，失败则打印错误信息。

*   **场景四：完善锁的释放** (00:01:45 - 00:02:00)
    *   讲师在代码中添加了 `finally` 块，并在其中调用 `mutex.release()` 方法。
    *   这样可以确保即使在执行过程中发生异常，锁也能被正确释放，避免死锁。
