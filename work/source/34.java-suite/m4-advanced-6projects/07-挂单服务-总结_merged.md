# 07-挂单服务-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对本章内容做一个回顾和总结

首先咱们回顾下本章的学习目标

在这里咱们要创建挂单服务工程

挂单服务工程搭建完成之后

咱们就要引入各组件的功能配置

完成服务所需的组件

然后做相关的集成配置

这里咱们实现了LockitMQ消息堆叠的集成配置

缓存以及现任词的配置

那咱们来回顾下本章所讲解的具体内容

首先我们创建了挂单服务工程

这里加入了多环境的配置文件

日子文件以及Home的依赖信息

接着咱们实现了双数据源的集成配置

这里和交易服务里面的双数据源配置

基本上都是类似的

采用的是MyBetis的双数据源配置

然后我们在挂单服务当中

实现了LockitMQ

消息堆叠的集成配置

通过LockitMQ消息堆叠

挂单服务就能够监听

获取实时下发的行情数据信息

接着的话咱们实现了缓存的集成配置

在这里是采用Ladies作为缓存的实现

配置类当中要去实现LadiesTemplate

模板接口的配置

接着就是缓存的规则配置

我们在这里加入了一个超时时间配置

默认超时时间为24小时

因为交易平台一般每天要做一次结算

挂单堆叠里面未成交的订单信息

是要做清除处理

那么在这里就通过超时

去实现缓存的自动清除

最后咱们实现了挂单服务的现成池配置

加入现成池的目的是为了提升它的处理速度

避免任务执行时产生的阻塞

这里就是现成池的具体属性配置

咱们要理解这个现成池的执行策略

在这里如果是出现现成堆垫塞满的情况下

它会将任务放在调用者的主现成当中继续执行

并不会丢弃该任务

目的是为了保障客户的请求能够正常处理

这些是现成池的配置信息

如果应用的负荷并不是很大

通过以下现成配置就可以满足

如果并发压力比较大的话呢

在这里可以将

现成数适当扩大一点

同时也可以扩大任务堆垫的存储数量

但是要注意现成数量并非越大越好

这个要根据实际的硬件配置CPU的核心数来决定了

最后咱们再来总结一下

这里挂单服务的搭建配置与交易服务比较类似

可以从交易服务工程当中引用或者参考相关的配置文件信息

这些组件的集成配置

咱们在前面章节

也已经做了讲解

为了快速实现起见

可以从源码当中将相关的配置copy进来

最主要的一点是要学会融会贯通

能够在不同的工程当中去实现相关组件的集成配置

这样在大家的实际工作当中也会有所帮助

挂单服务集成的功能组件比较多一些

因为挂单逻辑

它是具有一定的业务复杂程度

我们要先把基础的功能组件集成配置好

这样咱们在下面的章节当中

才能够专注于核心业务逻辑的实现

好

在这里呢

就是对本章内容的回顾与总结

那这一讲的内容

咱们就先讲到这里

谢谢

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是“交易平台”系列课程的第15天，主题为“挂单服务工程搭建与配置”。课程内容聚焦于构建一个独立的“挂单服务”（`stock-pending`），并为其配置核心组件，包括：双数据源（用于连接不同环境的数据库）、消息队列（RocketMQ，用于接收行情数据）、缓存（Redis，用于存储和管理挂单状态）、以及线程池（用于异步处理高并发请求）。课程目标是让学习者掌握如何从零开始搭建并配置一个完整的、具备高可用和高性能的挂单服务工程，为后续的限价委托处理功能打下基础。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供具体时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:30**：课程开场与目标介绍。展示“第2章 限价委托挂单处理”的目标，包括实现限价委托、掌握交易处理逻辑和缓存队列、以及掌握全局锁。
*   **00:30 - 01:00**：**3.1 创建挂单服务工程**。演示如何创建名为 `stock-pending` 的新项目，并展示其标准的 Maven 项目结构。
*   **01:00 - 01:30**：**3.2 挂单服务双数据源配置**。讲解如何配置 Spring Boot 的多数据源，以支持开发、测试和生产环境。
*   **01:30 - 02:00**：**3.3 挂单服务队列配置**。展示如何使用 `@EnableBinding` 和 `@Input` 注解配置 RocketMQ 消费者，监听名为 `quote` 的队列。
*   **02:00 - 02:30**：**3.4 挂单服务缓存配置**。讲解如何使用 `@EnableCaching` 注解开启缓存，并配置 `RedisTemplate` 和 `CacheManager`，设置缓存的默认过期时间为 24 小时。
*   **02:30 - 03:00**：**3.5 挂单服务线程池配置**。演示如何配置 `ThreadPoolTaskExecutor`，设置核心线程数、最大线程数、队列容量和超时时间，并配置拒绝策略。
*   **03:00 - 03:30**：**4. 总结**。回顾本章内容，强调挂单服务集成的复杂性，并提示学习者需要准备好相应的组件配置。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **学习目标**：实现限价委托挂单处理功能；掌握交易处理逻辑和缓存队列；掌握全局锁。
    *   **章节结构**：清晰地列出了“3. 实现”下的五个子章节：创建工程、双数据源、队列、缓存、线程池。
    *   **配置文件示例**：
        *   **`application.yml`**：用于配置线程池参数，如 `corePoolSize: 5`, `maxPoolSize: 10`, `queueCapacity: 500`, `keepAliveSeconds: 60`。
        *   **`bootstrap.yml`**：用于配置多环境（如 `bootstrap-dev.yml`, `bootstrap-uat.yml`）的初始设置。
*   **代码关键内容**：
    *   **3.1 创建挂单服务工程**：
        *   项目包名：`com.itcast.trade.stock.pending`。
    *   **3.2 挂单服务双数据源配置**：
        *   代码未在画面中完整展示，但提到了需要配置多数据源。
    *   **3.3 挂单服务队列配置**：
        *   **配置类**：`com.itcast.trade.stock.pending.config.RocketMqConsumeConfiguration`。
        *   **核心代码**：
            ```java
            @Configuration
            @EnableBinding({RocketMqConsumeConfiguration.QueueSource.class})
            public class RocketMqConsumeConfiguration {
                public interface QueueSource {
                    @Input("quote")
                    SubscribableChannel quote();
                }
            }
            ```
    *   **3.4 挂单服务缓存配置**：
        *   **配置类**：`com.itcast.trade.stock.pending.config.RedisConfiguration`。
        *   **核心代码**：
            ```java
            @Configuration
            @EnableCaching
            public class RedisConfiguration extends CachingConfigurerSupport {
                @Bean(value = "redisTemplate")
                public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory redisConnectionFactory) {
                    RedisTemplate<String, Object> redisTemplate = new RedisTemplate<String, Object>();
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
    *   **3.5 挂单服务线程池配置**：
        *   **配置类**：`com.itcast.trade.stock.pending.config.ThreadPoolConfig`。
        *   **核心代码**：
            ```java
            @Configuration
            public class ThreadPoolConfig {
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
                    executor.setKeepAliveSeconds(keepAliveSeconds);
                    executor.setThreadNamePrefix("PendingAsyncTaskExec-");
                    executor.setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy());
                    return executor;
                }
            }
            ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与结构展示** (00:30-01:00)
    *   **描述**：讲师在 Typora 编辑器中展示了一个名为 `stock-pending` 的新项目。画面清晰地显示了项目的目录结构，包括 `src/main/java` 和 `src/main/resources` 文件夹，以及 `pom.xml` 文件，为后续的配置和开发奠定了基础。
*   **场景二：RocketMQ 队列配置演示** (01:30-02:00)
    *   **描述**：讲师展示了如何通过 `@EnableBinding` 注解将一个接口绑定到 RocketMQ 的队列上。代码中定义了一个 `QueueSource` 接口，其中包含一个 `@Input("quote")` 注解的方法 `quote()`，该方法返回一个 `SubscribableChannel`，用于监听名为 `quote` 的消息队列。
*   **场景三：Redis 缓存配置演示** (02:00-02:30)
    *   **描述**：讲师讲解了如何配置 Redis 缓存。首先，通过 `@EnableCaching` 注解开启缓存功能。然后，通过 `RedisTemplate` 配置了序列化器（`StringRedisSerializer`），并创建了 `CacheManager`。代码中设置了缓存的默认过期时间为 24 小时（`Duration.ofSeconds(3600 * 24)`），并使用 `RedisCacheManager` 进行管理。
*   **场景四：线程池配置演示** (02:30-03:00)
    *   **描述**：讲师演示了如何配置一个 `ThreadPoolTaskExecutor`。代码中设置了核心线程数、最大线程数、队列容量和超时时间。特别地，通过 `setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy())` 设置了拒绝策略，当线程池满时，任务会由调用者线程（主线程）执行，避免任务被丢弃。
*   **场景五：配置文件总结** (03:00-03:30)
    *   **描述**：讲师在 `application.yml` 文件中展示了线程池的配置参数，如 `corePoolSize: 5`, `maxPoolSize: 10`, `queueCapacity: 500`, `keepAliveSeconds: 60`。这为整个服务的线程池配置提供了明确的配置项，方便后续的调整和优化。
