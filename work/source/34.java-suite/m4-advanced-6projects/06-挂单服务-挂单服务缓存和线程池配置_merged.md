# 06-挂单服务-挂单服务缓存和线程池配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始实现挂单服务缓存配置

以及挂单服务的现成时配置

那咱们就来做相应的实现

拖比对应的配置代码

回到工程当中

在Configure Package下面

咱们创建一个配置类

New Java Class

名称叫Ladies Configuration

咱们将讲义当中的原码copy进来

那咱们来看一下

这里是定义Ladies的template的模板操作接口

下面是设置CacheManage缓存的超时时间

默认的是以一天为单位24个小时

如果缓存数据存放超过此时间的话

会自动失效

比如说咱们挂单缓存对列当中的挂单数据

以一天为单位

会自动结算清空对列当中的缓存数据

通过这个默认超时时间设置

这样咱们就不用再进行手工的清除维护

好

这个呢就是Ladies的缓存配置

那咱们再回到讲义当中

接着咱们去实现挂单服务的现成词配置

为了提升挂单服务的处理速度

避免产生阻塞的问题

所以在这里咱们加入了现成词的处理方案

那咱们先copy讲义当中的代码

回到工程当中

在这里呢我们去创建一个配置类

右键New Java Class

名称叫Task

Execute

Configuration

将讲义中的代码copy进来

导入相应的包

Spring Framework下面

Execute

Java Util

Conclude下面的包

咱们来看一下这些属性的具体含义

在这里咱们添加对应的注释

这个是核心现成数量

下面这个是最大的现成数量

这里呢就是任务对列的吞吐数量

这个吞吐量是什么作用呢

它的作用是在于

现成数量如果是不够使用的时候

就会将任务先放在对列当中

这个对列会有一个大小限制

这个大小限制就是这里所配置的吞吐数量

这个根据实际情况来做配置

如果系统的压力

负荷量不是很大的话呢

这个吞吐量可以适当配小一点

如果并发量比较高

这个吞吐数量可以适当扩大一些

避免任务丢失或者执行失败的情况

下面呢是现成的有效存活时间

然后就是现成词的具体配置

将这里面的属性设置进去

大家注意一下

这里设置了现成词的执行策略

在现成对列塞满的情况下面

这个任务会在调用者的现成

或者主现成当中继续执行

这个任务并不会被抛弃

这个意思就是说

咱们在这里有个主现成在运行

另外呢会调用现成词

去处理一部现成任务

上面这个呢是主现成

那咱们知道现成词下面会有个任务对列

任务对列的话呢

如果是塞满了

这个时候该如何处理呢

这里面呢是一个主现成的任务

这里面的配置策略并不会将任务进行丢弃

而是将在这里面塞满的任务

把它挪到主现成当中去做处理

这个就是该策略的处理流程

咱们导入一下

好

在这里咱们就完成了挂单服务的现成词配置

以及Ladies缓存的集成配置

那这一讲内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于一个名为“挂单服务”的技术课程，主要讲解如何通过配置 Redis 缓存和线程池来优化服务性能。讲师通过 IntelliJ IDEA 开发环境，逐步演示了两个核心配置类的编写：`RedisConfiguration` 用于配置 Redis 缓存，以及 `TaskExecutorConfiguration` 用于配置线程池。视频内容聚焦于代码实现细节，包括 Spring Boot 的 `@Configuration`、`@EnableCaching`、`@EnableAsync` 注解，以及 `RedisTemplate` 和 `ThreadPoolTaskExecutor` 的具体配置。目标是提升挂单服务的处理速度，避免因高并发导致的阻塞。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 文档中浏览课程大纲，定位到“3.4 挂单服务缓存配置”章节。
*   **00:00:05 - 00:00:20**: 讲师切换到 IntelliJ IDEA，展示 `RedisConfiguration` 类的代码，重点讲解 `@Bean` 注解用于创建 `RedisTemplate` 实例，并设置其序列化器和连接工厂。
*   **00:00:20 - 00:00:40**: 讲师继续讲解 `RedisConfiguration`，展示如何配置 `CacheManager`，并设置默认的缓存过期时间为 24 小时（`Duration.ofSeconds(3600 * 24)`）。
*   **00:00:40 - 00:00:50**: 讲师在项目结构中导航到 `TaskExecutorConfiguration` 类，准备讲解线程池配置。
*   **00:00:50 - 00:01:10**: 讲师展示 `TaskExecutorConfiguration` 类，讲解其通过 `@Value` 注解注入配置参数，如核心线程数、最大线程数、队列容量和线程存活时间。
*   **00:01:10 - 00:01:30**: 讲师在代码中添加 `@Bean` 方法，创建并配置 `ThreadPoolTaskExecutor` 实例，设置其核心线程数、最大线程数、队列容量和线程名前缀。
*   **00:01:30 - 00:01:45**: 讲师在 Typora 文档中切换回大纲，定位到“3.5 挂单服务线程池配置”章节，总结本部分的讲解内容。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **章节标题**:
    *   `3.4 挂单服务缓存配置`
    *   `3.5 挂单服务线程池配置`
*   **课程大纲**:
    *   第二章：限价委托挂单处理
    *   3.1 定义接口数据结构
    *   3.2 挂单服务限价委托接口
    *   3.3 挂单服务队列配置
    *   3.4 挂单服务缓存配置
    *   3.5 挂单服务线程池配置
    *   4. 总结

#### 代码关键内容

*   **`RedisConfiguration` 类**:
    ```java
    @Configuration
    @EnableCaching
    public class RedisConfiguration extends CachingConfigurerSupport {
        @Bean(value = "redisTemplate")
        public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory redisConnectionFactory) {
            RedisTemplate<String, Object> redisTemplate = new RedisTemplate<>();
            redisTemplate.setKeySerializer(new StringRedisSerializer());
            redisTemplate.setConnectionFactory(redisConnectionFactory);
            return redisTemplate;
        }

        @Bean
        public CacheManager cacheManager(RedisConnectionFactory redisConnectionFactory) {
            Duration expiration = Duration.ofSeconds(3600 * 24);
            return RedisCacheManager.builder(redisConnectionFactory)
                    .cacheDefaults(RedisCacheConfiguration.defaultCacheConfig().entryTtl(expiration))
                    .build();
        }
    }
    ```

*   **`TaskExecutorConfiguration` 类**:
    ```java
    @Configuration
    @EnableAsync
    public class TaskExecutorConfiguration {
        @Value("${task.executor.corePoolSize:5}")
        private int corePoolSize;

        @Value("${task.executor.maxPoolSize:10}")
        private int maxPoolSize;

        @Value("${task.executor.queueCapacity:500}")
        private int queueCapacity;

        @Value("${task.executor.keepAliveSeconds:60}")
        private int keepAliveSeconds;

        @Bean
        public Executor taskExecutor() {
            ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
            executor.setCorePoolSize(corePoolSize);
            executor.setMaxPoolSize(maxPoolSize);
            executor.setQueueCapacity(queueCapacity);
            executor.setThreadNamePrefix("PendingAsyncTaskExec-");
            executor.setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy());
            return executor;
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：Redis 缓存配置演示 (00:00:05 - 00:00:40)**
    *   讲师在 IntelliJ IDEA 中打开 `RedisConfiguration.java` 文件。
    *   他首先展示了 `@Bean` 注解的 `redisTemplate` 方法，解释了如何创建 `RedisTemplate` 实例并设置其序列化器和连接工厂。
    *   接着，他展示了 `cacheManager` 方法，重点讲解了如何使用 `Duration.ofSeconds(3600 * 24)` 设置缓存的默认过期时间为 24 小时，并使用 `RedisCacheManager.builder()` 构建缓存管理器。

*   **场景二：线程池配置演示 (00:00:50 - 00:01:30)**
    *   讲师在项目结构中导航到 `TaskExecutorConfiguration.java` 文件。
    *   他展示了类中通过 `@Value` 注解注入的四个配置参数：核心线程数、最大线程数、队列容量和线程存活时间。
    *   他随后演示了 `@Bean` 方法 `taskExecutor()`，创建 `ThreadPoolTaskExecutor` 实例，并依次设置其核心线程数、最大线程数、队列容量、线程名前缀和拒绝策略（`CallerRunsPolicy`）。

*   **场景三：课程大纲导航 (00:01:30 - 00:01:45)**
    *   讲师在 Typora 文档中点击“3.5 挂单服务线程池配置”章节，切换到该部分的讲解内容，为后续内容做准备。

---
