# 08-elasticjob-监听器讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们接着来讲解它这一块的一个监听器

那么监听器就是在我们任务执行前

任务执行后进行一个监听

那这一块我们先创建一个监听器

写个Dynamic Listener

Dynamic Task Listener就行了

它需要继承一个抽象类

Obstract就这一个

里面有两个方法

Do Before Do After

这个大家一看就知道是什么意思了

执行前执行后的一个通知

行 这是这一块

这个是执行前通知

这个是执行后通知

好 我们来输出一段话就行了

就输出Before

这个就输出After

行了

它这里还有一个带参数的构造函数

这一块是我们的一个超时时间

那接着哪里要用的话

哪里使用它的实例就行了

好 我们来用一下

比如我们在这里要用

那我们在这里就要创建

就要创建这个对象的实例了

我们写到这上面去

这个是一个监听器

Public Dynamic Listener

Dynamic Listener

好 写个时间

这个我就随意写个时间就行了

那这里整一个bin

哪里要用到它

哪里注入就行了

那么这里很明显

一会儿就要用到它

所以我可以在这里直接注入进来

注入进来之后呢

注意在

好 我们这一块我们看一下

没有写add符号

对吧

接着我们需要把它丢给我们下面这里

那么这个时候

这个监听器在这里就会发挥作用

我们接着启动

测试一下

看监听器一会儿会不会执行

好 运行一下

看看效果

在这一块呢

我们等会儿就请求一次

好 扣掉

来刷新一下

大家看效果

5秒钟执行

诶 执行前

before 执行后

after

好 这个就是我们当前这一块的一个监听器的使用

监听器呢

它需要去继承这个抽象

对

并且里面有两个方法

分别是我们要执行的方法

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析：

---

### 1) 视频摘要

本视频片段演示了如何在 Spring Boot 项目中，利用 LiteJob-Lite（一个轻量级分布式任务调度框架）结合 ZooKeeper 实现动态定时任务的注册与执行。核心内容包括：
- **项目结构**：展示了一个包含 `controller`, `service`, `task` 等模块的 Spring Boot 项目。
- **核心类**：`DynamicListener`，一个继承自 `AbstractDistributeOnceElasticJobListener` 的监听器，用于在任务执行前后打印日志。
- **配置类**：`ElasticJobDynamicConfig`，负责初始化 ZooKeeper 注册中心、创建并注册监听器，并动态构建和初始化 LiteJob 任务。
- **技术栈**：Java, Spring Boot, LiteJob-Lite, ZooKeeper。
- **演示流程**：通过代码编写和调试，展示了如何动态添加一个任务，并在任务执行前后触发监听器方法。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中的时间点，以下章节是根据画面内容和逻辑顺序进行的划分：

- **章节 1：项目环境与任务监听器创建 (0:00 - 0:30)**
  - 展示项目结构，定位到 `DynamicListener` 类。
  - 通过 IDE 的“实现抽象方法”功能，为 `AbstractDistributeOnceElasticJobListener` 类实现 `doBeforeJobExecutedAtLastStarted` 和 `doAfterJobExecutedAtLastCompleted` 方法。

- **章节 2：动态任务配置与初始化 (0:30 - 1:00)**
  - 在 `ElasticJobDynamicConfig` 类中，定义 `ZookeeperRegistryCenter` 的初始化方法。
  - 定义 `DynamicListener` 的 Bean，并注入 `ZookeeperRegistryCenter`。

- **章节 3：动态添加任务的核心逻辑 (1:00 - 1:30)**
  - 编写 `addDynamicTask` 方法，使用 `LiteJobConfiguration.newBuilder()` 构建任务配置。
  - 设置任务参数（`jobName`, `cron`, `shardingTotalCount`）。
  - 使用 `.overwrite(true).build()` 方法构建任务。
  - 使用 `new SpringJobScheduler(...).init()` 将任务注册到 Spring 的任务调度器中。

- **章节 4：任务执行与监听器触发 (1:30 - 2:00)**
  - 通过浏览器访问任务接口（如 `/task/jobName=xxx`）触发任务。
  - 在 `DynamicListener` 中，`doBeforeJobExecutedAtLastStarted` 和 `doAfterJobExecutedAtLastCompleted` 方法被调用并打印日志。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### 代码关键内容：

**1. `DynamicListener` 类 (监听器)**

```java
public class DynamicListener extends AbstractDistributeOnceElasticJobListener {
    @Override
    public void doBeforeJobExecutedAtLastStarted(ShardingContexts shardingContexts) {
        System.out.println("doBeforeJobExecutedAtLastStarted");
    }

    @Override
    public void doAfterJobExecutedAtLastCompleted(ShardingContexts shardingContexts) {
        System.out.println("doAfterJobExecutedAtLastCompleted");
    }
}
```

**2. `ElasticJobDynamicConfig` 类 (配置类)**

```java
@Configuration
public class ElasticJobDynamicConfig {

    @Bean
    public ZookeeperConfiguration zkConfig() {
        // 1. Zookeeper地址
        // 2. 定时任务命名空间
        return new ZookeeperConfiguration(zkserver, zknamespace);
    }

    @Bean(initMethod = "init")
    public ZookeeperRegistryCenter registryCenter(ZookeeperConfiguration zkConfig) {
        return new ZookeeperRegistryCenter(zkConfig);
    }

    @Bean
    public DynamicListener dynamicListener() {
        return new DynamicListener(starterTimeoutMilliseconds: 10000L, completedTimeoutMilliseconds: 100000L);
    }

    @Autowired
    private ZookeeperRegistryCenter zookeeperRegistryCenter;

    public void addDynamicTask(String jobName, String cron, int shardingTotalCount, String id, SimpleJob instance) {
        // 1. 添加LiteJob-lite的任务作业器
        LiteJobConfiguration liteJobConfiguration = LiteJobConfiguration.newBuilder(
            new SimpleJobConfiguration(
                JobCoreConfiguration.newBuilder(jobName, cron, shardingTotalCount)
                    .jobParameter(id) // 额外的参数
                    .build()
            )
            .overwrite(true)
            .build()
        );

        // 2. 将Lite的任务作业器添加到Spring的任务启动器中，并初始化
        new SpringJobScheduler(instance, zookeeperRegistryCenter, liteJobConfiguration, dynamicListener).init();
    }
}
```

#### 公式与图表：

- **无公式**：视频中未出现数学公式。
- **无图表**：视频中未出现流程图、架构图等图表。

---

### 4) 关键场景与演示描述

- **场景 1：监听器方法实现**
  - 演示者在 IDE 中，通过右键选择“实现抽象方法”，自动为 `DynamicListener` 类生成 `doBeforeJobExecutedAtLastStarted` 和 `doAfterJobExecutedAtLastCompleted` 方法的骨架代码。
  - 在方法体内添加 `System.out.println(...)` 语句，用于在任务执行前后打印日志。

- **场景 2：动态任务构建与注册**
  - 演示者在 `ElasticJobDynamicConfig` 类中编写 `addDynamicTask` 方法。
  - 使用 `LiteJobConfiguration.newBuilder()` 构建任务配置，设置 `jobName`, `cron`, `shardingTotalCount` 等参数。
  - 使用 `.overwrite(true).build()` 方法构建任务配置。
  - 使用 `new SpringJobScheduler(...).init()` 方法将任务注册到 Spring 的任务调度器中，并传入监听器 `dynamicListener`。

- **场景 3：任务触发与监听器触发**
  - 演示者通过浏览器访问任务接口（如 `/task/jobName=xxx`）。
  - 在控制台中，看到 `doBeforeJobExecutedAtLastStarted` 和 `doAfterJobExecutedAtLastCompleted` 方法被调用并打印日志，证明任务成功执行并触发了监听器。

- **场景 4：配置类初始化**
  - 演示者在 `ElasticJobDynamicConfig` 类中，通过 `@Bean` 注解定义 `ZookeeperRegistryCenter` 和 `DynamicListener`。
  - 使用 `@Autowired` 注入 `ZookeeperRegistryCenter`，用于任务的注册和调度。

---

以上是根据视频画面进行的结构化技术分析。
