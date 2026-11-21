# 04-elasticjob-动态定时任务案例实现步骤讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着我们来讲解我们EleticJob它的一个动态任务案例

动态任务案例这一块有一个参考地址

大家可以参考一下

然后我们这一块将去详细讲解一下这个动态任务案例

好这个参考地址我们可以打开

打开之后我们简单来讲解一下它这一块

它这一块我们来说一下

在这里首先这里有一个注册的一个信息

这个注册的信息呢

其实就是你把你当前我们主Keyboard的一个配置信息

以及你当前任务案例的一个命名空间的一个信息

把它给配置进来

这个是注册的一个配置信息

接着你要把这个注册的配置信息

把它注册到主Keyboard里面去

所以这一块有一个注Keyboard Registry Center这一块

这个其实就是注册数据到我们注Keyboard里面去了

注册之后呢

它这里还有一些别的操作哈

它把当前作业持久化到我们DB里面去了

其实可以不用持久化到DB里面去

因为我们这一块本身就不需要依赖我们的DB

所以等会儿我们将不实现这个操作

然后它这里还有一个就是我们任务调度的一个监听器

这个监听器呢

其实也是可有可无的

监听器其实是在任务执行前

任务执行后

这一块你可以做一个监听

它就类似我们的一个AOP的一个机制

好我们继续往后面看

像这一块就是上面它所用到的一个监听器

这一块监听器这一块呢

有一个before还有一个after

所以这两个其实就是类似我们AOP里面的一个执行机制

最后面这里呢

这里是添加我们的一个动态定时任务案例

添加动态定时任务案例呢

这一块写的比较复杂

其实这个非常简单

只是把我们之前的静态任务案例

这相关的一个参数给添加到我们程序中

用程序去执行而已

用程序去执行

所以这一块没有这么复杂

好我们基于它这一块的一个讲解了

我们来优化精简一下

我们这一个动态定时任务案例的一个实现步骤

这个实现步骤呢

第一个首先我们要知道我们主keep的一个地址

所以等会我们要配置主keep的地址

并且我们还要配置一个动态的一个定时任务案例的一个命名空间

这个命名空间呢

你是一定要配

但是我们不一定会用

就是有可能用不着

这个配置之后呢

紧接着我们就开始去注册初始化数据了

注册初始化数据了

注册初始化数据了

其实就是像主keep里面去注册我当前定时任务的一个命名空间信息

接着我们这里要有一个监听器

这个监听器的是可以不写的

那么我们一会儿先不写它

然后我们等会写完了之后

再把监听器给加进来就行了

接着是添加动态定时任务案例的一个实现

也就是写一个方法

然后把之前这些参数给加进来

加进去就可以了

最后的是制定这个任务处理的一个过程

也需要实现我们simple job这个接口就可以了

这个是我们这一块整体实现的一个流程

其实仔细一分的话

没有这么多个步骤仔细一分的话

这个只是一个数据配置

最终要在这儿来用到它

所以123可以看成一个步骤

而第五个步骤是这个数据配置的一个步骤

第五个是一个单独的步骤

第六个跟我们刚才写的静态任务案例是一样的

所以总体来说应该只有三个步骤就可以完成

第四个步骤是属于额外扩展的

你可以加

你可以不加

好

接着我们来实现一下这个动态定时任务案例

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程旨在教授如何在 Spring Boot 项目中使用 **Elastic-Job-Lite** 框架来实现分布式定时任务。课程内容从项目初始化、核心配置（如 Zookeeper 注册中心、数据源、Job 配置）开始，逐步深入到具体的任务实现、分片处理、以及如何动态添加任务。讲师通过代码演示和 PPT 讲解，系统地介绍了 Elastic-Job-Lite 的核心概念和使用方法，重点在于如何将一个简单的 Spring Boot 任务改造为一个可分布式、可动态管理的定时任务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程开场，展示 Elastic-Job 官方网站，介绍其作为分布式调度解决方案，由 Elastic-Job-Lite 和 Elastic-Job-Cloud 两个子项目组成。
*   **00:16 - 00:30**: 进入课程核心内容，讲解如何在 Spring Boot 项目中集成 Elastic-Job-Lite。首先展示 `pom.xml` 中需要添加的依赖项，包括 `elastic-job-lite-spring-boot-starter`。
*   **00:31 - 00:50**: 讲解 `application.yml` 中的配置，包括数据库连接（MySQL）和 Elastic-Job 相关的配置（如 `elastic.job` 前缀的属性）。
*   **00:51 - 01:10**: 详细演示 `ElasticJobConfig` 配置类的代码，用于初始化 Zookeeper 注册中心和 Job 配置。
*   **01:11 - 01:30**: 讲解如何实现一个具体的定时任务类 `MyElasticJob`，它需要实现 `SimpleJob` 接口并重写 `execute` 方法。
*   **01:31 - 01:50**: 讲解如何实现一个分布式任务监听器 `ElasticJobListener`，用于处理任务执行前后的状态变更。
*   **01:51 - 02:10**: 讲解如何使用 `ElasticJobHandler` 类来动态添加任务，通过 `LiteJobConfiguration` 构建器和 `SpringJobScheduler` 来完成。
*   **02:11 - 02:30**: 展示 `ElasticJobHandler` 的完整代码，包括如何注入依赖和调用 `addJob` 方法。
*   **02:31 - 02:50**: 讲解 `ElasticJobHandler` 中 `addJob` 方法的实现细节，包括如何构建 `LiteJobConfiguration` 并注册到 Spring 容器。
*   **02:51 - 03:10**: 展示 `StaticJob` 类的完整代码，用于演示一个简单的、非动态的定时任务。
*   **03:11 - 03:30**: 回顾并总结课程内容，强调动态任务添加的步骤和关键点。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 关键内容

*   **Elastic-Job 简介**：Elastic-Job 是一个分布式调度解决方案，由 Elastic-Job-Lite 和 Elastic-Job-Cloud 两个子项目组成。
*   **Elastic-Job-Lite**：定位为轻量级无中心化解决方案，使用 jar 包形式提供分布式任务的协调服务。
*   **Elastic-Job-Cloud**：采用自研 Mesos Framework 的解决方案，额外提供资源治理、应用分发以及进程隔离等功能。
*   **动态任务案例**：动态任务案例主要是讲解程序在运行时，动态添加定时任务，这种场景应用非常广泛。
*   **动态任务实现步骤**：
    1.  配置初始化 Zookeeper 地址
    2.  配置的定时任务命名空间（不一定使用）
    3.  注册初始化数据
    4.  监听器 -> 任务执行前后监听（可有可无）
    5.  动态添加定时任务
    6.  自定义任务处理过程 -> 实现 SimpleJob

#### 代码关键内容

*   **`pom.xml` 依赖**：
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    <dependency>
        <groupId>com.dangdang</groupId>
        <artifactId>elastic-job-lite-spring-boot-starter</artifactId>
        <version>2.1.5</version>
    </dependency>
    ```

*   **`application.yml` 配置**：
    ```yaml
    datasource:
      url: jdbc:mysql://localhost:3306/test?characterEncoding=utf-8&verifyServerCertificate=false&useSSL=false&requireSSL=false
      driver-class-name: com.mysql.jdbc.Driver
      username: root
      password: root
    type: com.zaxxer.hikari.HikariDataSource
    hibernate:
      ddl-auto: update
      show-sql: true
    database: mysql

    elastic.job:
      server-lists: localhost:2181
      namespace: elastic-job
    ```

*   **`ElasticJobConfig` 配置类**：
    ```java
    @Configuration
    @ConfigurationProperties(prefix = "elastic.job")
    public class ElasticJobConfig {
        private String serverLists;
        private String namespace;
        @Resource
        private HikariDataSource datasource;

        @Bean
        public ZookeeperConfiguration zkConfig() {
            return new ZookeeperConfiguration(serverLists, namespace);
        }

        @Bean(initMethod = "init")
        public JobEventConfiguration jobEventConfiguration() {
            return new JobEventConfiguration(datasource);
        }

        @Bean
        public ElasticJobListener elasticJobListener() {
            return new ElasticJobListener(100, 100);
        }
    }
    ```

*   **`MyElasticJob` 任务类**：
    ```java
    @Slf4j
    public class MyElasticJob implements SimpleJob {
        @Override
        public void execute(ShardingContext shardingContext) {
            log.info("任务名: {}, 分片: {}, 总分片: {}, 参数: {}", shardingContext.getJobName(), shardingContext.getShardingItem(), shardingContext.getShardingTotalCount(), shardingContext.getShardingParameter());
        }
    }
    ```

*   **`ElasticJobListener` 监听器类**：
    ```java
    public class ElasticJobListener extends AbstractDistributedElasticJobListener {
        @Resource
        private TaskRepository taskRepository;

        @Override
        public void doBeforeJobExecutedAtLastStarted(ShardingContexts shardingContexts) {
            super.doBeforeJobExecutedAtLastStarted(shardingContexts);
        }

        @Override
        public void doAfterJobExecutedAtLastCompleted(ShardingContexts shardingContexts) {
            // 任务执行完成，更新数据库状态
            JobTask jobTask = taskRepository.findJobTaskByJobNameAndShardingItem(shardingContexts.getJobName(), shardingContexts.getShardingItem());
            jobTask.setStatus(1);
            taskRepository.save(jobTask);
        }
    }
    ```

*   **`ElasticJobHandler` 动态任务处理器**：
    ```java
    @Component
    public class ElasticJobHandler {
        @Resource
        private ZookeeperRegistryCenter registryCenter;
        @Resource
        private JobEventConfiguration jobEventConfiguration;
        @Resource
        private ElasticJobListener elasticJobListener;

        private static LiteJobConfiguration.Builder simpleJobConfigBuilder(String jobName, Class<? extends SimpleJob> jobClass, int shardingTotalCount, String cron, String id) {
            return LiteJobConfiguration.newBuilder(new SimpleJobConfiguration(
                    new JobConfiguration(jobName, jobClass, shardingTotalCount, cron, id),
                    jobEventConfiguration,
                    elasticJobListener
            ));
        }

        public void addJob(String jobName, String cron, Integer shardingTotalCount, String id) {
            LiteJobConfiguration jobConfig = simpleJobConfigBuilder(jobName, MyElasticJob.class, shardingTotalCount, cron, id).build();
            new SpringJobScheduler(new MyElasticJob(), registryCenter, jobConfig, jobEventConfiguration, elasticJobListener).schedule();
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖配置**
    *   讲师首先在浏览器中打开 Elastic-Job 官网，介绍其背景。
    *   随后切换到 GitHub 仓库，展示 `README.md` 文件，讲解如何在 Spring Boot 项目中集成 Elastic-Job-Lite。
    *
