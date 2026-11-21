# 04-分布式锁-Redisson配置讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

那通过刚才我们对Redis的一个介绍,我们可以了解到Redis它有两个核心流程,第一个核心流程是加锁这一块,第二个核心流程是释放锁,因此我们来学习它的时候,也要在我们接口代码里面去实现这两个操作。

好,我们开始学习一下我们Redis它的一个使用方式,首先第一个要先引入我们的依赖包,在这一块把这个依赖包给引入进来,这是Redis的依赖包,引入进来之后呢,我们给它新建一个接口,这个接口里面就要实现我们如何加锁,如何解锁。

在这一块,那么我们来先写一个加锁的方法。

这个加锁呢?

会一直循环加锁,直到拿到锁为止,会一直循环加锁,直到拿到锁。

好,我们写一下Rlock,这儿写个Rlock,把对应的加锁的key给我传过来。

好,这是这个,那么还有另外一种情况,加锁,但是并不是一直加锁,有一个超时时间。

跟上面这块其实差不多的哈,它只是多了个超时时间。

好,我们接着再往这写。

我们再写一个方法,也是加锁,也指定超时时间和超时单位。

这个呢,也是差不多的,Rlock,Rlock,String,Rlock,Key,Long,Timeout,给它一个超时时间就行了。

好,OK,接着再往这里看。

我们还可以做另外一个事情,也是加锁。

但这个加锁是做这么个事情哈,我加锁,我给你指定个超时时间。

一旦锁加成功之后,这个锁,如果说你多久没有释放,我会让它释放。

这是这个,防止失锁。

好,加锁,指定超时时间和锁的释放时间。

好,我们来写一下哈。

For,叫Try Lock,Lock Key,Timeout,List Time。

好,这个时间我们也给它哈。

OK,这上面这个加锁呢,我们基本上把人写的加锁都给写了哈。

那咱们紧接着就开始写解锁了。

因为它的核心就是加锁和解锁。

好,我们来写一下解锁。

Unlock,那你每次把这个Key给我传回来。

好,再写一个解锁。

那你每次把这个对象给我传回来。

行,那这一块我们这里,所有的加锁和解锁我们都写完了。

接着我们给它写一个实现内。

来看一下这一块该怎么实现哈。

Redicent,实现刚才这个接口。

这个要记得把它给容器管理。

好,这一块我们就开始去实现加锁和解锁。

在我们Redicent这里。

它有两个对象,一个是Redicent Client。

还有一个是谁呢?叫做Redicent Connection Factory哈。

我们现在要注入这个对象。

这个对象我们现在还没有配置。

我们等会再配置。

好,开始去编写相关的代码哈。

这个是我们的加锁。

那么这一块加锁呢怎么做呢?非常容易。

直接用Redicent Client点GetLock。

Lock Key给它。

这就是我们的加锁了。

它会一直去获取锁。

直到获取到为止。

这个就比较执着。

我们接着看这个。

这个跟上面是一样的。

它只是说在这里加了一个超时时间。

把这个超时时间给写过来就OK了。

行,这是这个。

超时时间呢,你要给它一个时间单位。

OK。

这个跟上面是一样的,只是有一个超时时间。

这个是在指定时间内拿不到锁,就会放弃。

好,这是这个。

那么下面这个呢,跟刚才这个是差不多的。

这个没有区别。

只是它多了一个时间单位。

这个呢,跟上面是差不多的。

只是它多了一个如果拿到锁。

锁。

最终。

有效时间。

为。

List Time。

好,这是这一块。

它又多了一个时间而已。

这个是我们的解锁。

解锁就非常简单了。

解锁。

那么两个解锁其实差不多的。

首先我们要获取这个Lock Key所对应的锁。

解锁就是Unlock就行了。

那么下面这块就是Unlock就OK了。

行,这一块我们就搞定了。

这是解锁。

好,那么加锁和解锁我们就都给写完了。

这也就是我们Redisn它的几个核心方法。

加锁、解锁就OK了。

紧接着我们开始去配置一下我们的Redisn。

它的这里呢,要有个核心的配置文件。

redisn.yml。

这里面配置什么呢?

主要要配置我们Redisn一些核心相关的一些参数。

这些参数比较多。

我们把它给拷过来。

然后有一些地方是需要我们去更改的。

那么我们需要更改的地方大家记得改就行了。

好,我们把它给拷过来。

在这一块。

拷过来之后呢,我们简单说一下要改的地方有哪些哈。

像这些地方,连接空闲超时时间这些我就不去带大家说了。

其实就类似咱们一个连接词的配置是差不多的。

往下面这里看。

这里是我们需要去关注的。

这个呢是当前Redisn的一个连接词。

这个要把它给改一下就OK了。

好,OK。

我们现在这个文件过来了。

紧接着我们还要去配置两个对象。

哪两个对象呢?

我们来说一下。

就是刚才我说的那两个对象。

第一个是我们的Redisn Client。

另外一个是我们Redisn Connect.

主要是这两个对象要配置哈。

好,我们先配置第一个Redisn Public Redisn Client。

这一块该怎么做呢?

我们简单说一下。

这个比较容易。

首先第一个,它要去加载这个配置文件。

加载配置文件。

第二个要解析配置文件。

第三个是要创建我们的Redisn Client对象。

大概就这样子就OK了。

好,我们来写一下哈。

加载它的话有个叫做classpath-resource.new classpath-resource。

我们把它给写过来。

redisn.yaml。

这是这个文件。

接着我们要解析这个文件。

那这里有个configure。

好,我们写一下configure哈。

from yaml。

OK,好,这是这一块。

接着我们就可以开始去创建我们的Redisn。

把当前这个配置给它就OK了。

这个好像还不是这样子哈。

redisn.client.create。

当前这个configure给它。

这一块就搞定了。

这个好像还是不行。

redisn.create。

行,这个就OK了。

这是我们Redisn Client的一个创建。

接着我们要创建它的工厂对象。

工厂对象呢也是一样的哈。

好,public.redisn.collectionfactory。

6.redisn.collectionfactory。

我们需要把上面这个对象给传过来就行了。

把它给传过来哈。

OK。

可以了。

那么这一块我们看一下。

我们缺的是。

缺的是它哈。

正确的。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面，对技术课程内容进行的结构化中文输出：

---

### 1) 视频摘要

本视频课程聚焦于 **分布式锁** 的实现，特别是使用 **Redisson** 库在 **Spring Boot** 项目中进行开发。讲师通过一个名为 `seckill-order` 的秒杀订单系统案例，详细讲解了如何定义分布式锁接口、实现基于 Redis 的锁机制、配置 Redisson 客户端以及处理锁的释放和超时问题。课程内容涵盖了分布式锁的核心概念、代码实现、配置文件编写以及潜在的 Redis 主从切换问题。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程开场，展示 PPT 大纲，介绍本节将讲解“分布式锁”。
*   **00:16 - 00:30**: 讲解分布式锁的必要性，引出 Redisson 作为实现工具。
*   **00:31 - 01:00**: 展示 `DistributedLocker` 接口定义，讲解 `lock` 方法的两种重载形式（无超时和带超时）。
*   **01:01 - 01:30**: 展示 `RedissonDistributedLocker` 类的实现，演示如何使用 `redissonClient.getLock(lockkey)` 获取锁，并调用 `lock.lock()` 方法。
*   **01:31 - 02:00**: 讲解 `lock` 方法的超时版本，使用 `lock.lock(timeout, TimeUnit.SECONDS)`。
*   **02:01 - 02:30**: 讲解 `unlock` 方法的实现，展示如何释放锁。
*   **02:31 - 03:00**: 讲解 `Redisson` 的配置，展示 `redisson.yml` 配置文件内容，包括连接超时、重试次数、密码等。
*   **03:01 - 03:30**: 展示 `RedisConfig` 配置类，讲解如何通过 `@Configuration` 注解和 `@Bean` 注解创建 `RedissonClient` 和 `RedisTemplate`。
*   **03:31 - 04:00**: 讲解 `RedissonClient` 的创建过程，展示如何通过 `Config` 对象配置并创建 `RedissonClient`。
*   **04:01 - 04:30**: 讲解 `RedisTemplate` 的配置，设置序列化器（`valueSerializer`、`keySerializer`、`hashKeySerializer`）。
*   **04:31 - 05:00**: 讲解 Redisson 的锁释放机制，展示 `tryLock` 方法的使用。
*   **05:01 - 05:30**: 讲解 Redis 主从切换的潜在问题，即在主节点宕机后，从节点晋升为主节点，导致锁状态不一致。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 大纲**:
    *   第4章：分布式锁
    *   4.1 问题分析
    *   4.2 Redisson介绍
    *   4.3 分布式事务
    *   4.4 WebSocket介绍

*   **关键代码**:
    *   **`DistributedLocker` 接口**:
        ```java
        public interface DistributedLocker {
            /**
             * 加锁，会一直循环加锁，直到拿到锁
             */
            RLock lock(String lockkey);

            /**
             * 加锁，指定超时时间
             */
            RLock lock(String lockkey, long timeout, TimeUnit unit);
        }
        ```
    *   **`RedissonDistributedLocker` 实现类**:
        ```java
        @Component
        public class RedissonDistributedLocker implements DistributedLocker {
            @Autowired
            private RedissonClient redissonClient;

            @Override
            public RLock lock(String lockkey) {
                RLock lock = redissonClient.getLock(lockkey);
                lock.lock();
                return lock;
            }

            @Override
            public RLock lock(String lockkey, long timeout, TimeUnit unit) {
                RLock lock = redissonClient.getLock(lockkey);
                lock.lock(timeout, unit);
                return lock;
            }

            @Override
            public RLock lock(String lockkey, long timeout) {
                RLock lock = redissonClient.getLock(lockkey);
                lock.lock(timeout, TimeUnit.SECONDS);
                return lock;
            }

            @Override
            public void unlock(RLock lock) {
                lock.unlock();
            }
        }
        ```
    *   **`redisson.yml` 配置文件**:
        ```yaml
        clusterServersConfig:
          # 连接空闲超时，单位：毫秒 默认10000
          idleConnectionTimeout: 10000
          # pingTimeout: 1000
          # connectTimeout: 10000
          # timeout: 3000
          # 命令失败重试次数
          retryAttempts: 3
          # 命令重试发送时间间隔，单位：毫秒
          retryInterval: 1500
          # 重新连接时间间隔，单位：毫秒
          reconnectionTimeout: 3000
          # 执行失败最大次数
          failedAttempts: 3
          # 密码
          password: test1234
          # 单个连接最大订阅数量
          subscriptionsPerConnection: 5
          # 负载均衡策略的选择
          loadBalancer: 'org.redisson.connection.balancer.RoundRobinLoadBalancer'
        ```
    *   **`RedisConfig` 配置类**:
        ```java
        @Configuration
        public class RedisConfig {
            @Bean("redisTemplate")
            public RedisTemplate<Object, Object> getRedisTemplate(RedissonConnectionFactory redissonConnectionFactory) {
                RedisTemplate<Object, Object> redisTemplate = new RedisTemplate<>();
                redisTemplate.setConnectionFactory(redissonConnectionFactory);
                redisTemplate.setValueSerializer(new StringRedisSerializer());
                redisTemplate.setKeySerializer(new StringRedisSerializer());
                redisTemplate.setHashKeySerializer(new StringRedisSerializer());
                return redisTemplate;
            }

            @Bean
            public RedissonClient redissonClient() {
                Config config = Config.fromYAML(new ClassPathResource("redisson.yml").getInputStream());
                return Redisson.create(config);
            }

            @Bean
            public RedissonConnectionFactory redissonConnectionFactory(RedissonClient redissonClient) {
                return new RedissonConnectionFactory(redissonClient);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：定义分布式锁接口** (00:30)
    *   讲师在 IDE 中打开 `DistributedLocker.java` 文件，展示了接口定义。
    *   通过注释解释了 `lock` 方法的两种形式：无超时和带超时。

*   **场景二：实现锁的获取** (01:00)
    *   讲师在 `RedissonDistributedLocker.java` 文件中，演示了如何使用 `redissonClient.getLock(lockkey)` 获取锁对象。
    *   通过 `lock.lock()` 方法实现加锁，代码简洁明了。

*   **场景三：配置 Redisson 客户端** (02:30)
    *   讲师展示了 `redisson.yml` 配置文件，详细解释了各个配置项的含义，如连接超时、重试次数、密码等。
    *   讲师强调了配置文件的重要性，它是连接 Redis 服务器的关键。

*   **场景四：配置 RedisTemplate** (03:30)
    *   讲师在 `RedisConfig.java` 文件中，演示了如何通过 `@Bean` 注解创建 `RedisTemplate`。
    *   通过 `setConnectionFactory` 设置连接工厂，并配置了序列化器，以便于后续的数据操作。

*   **场景五：讲解 Redis 主从切换问题** (05:00)
    *   讲师在 PPT 上展示了关于 Redis 主从切换的潜在问题。
    *   解释了当主节点宕机后，从节点晋升为主节点，可能导致锁状态不一致，从而引发业务问题。
    *   强调了在生产环境中需要考虑此问题，并可能需要引入更复杂的解决方案。

--- 

以上是根据视频画面整理出的结构化内容，希望能帮助您更好地理解课程内容。
