# Elastic-Job 入门案例：三层包装装配出 LiteJobConfiguration 并交给调度器

注册中心配好了，作业类也写完了，入门案例只剩最后一块：Elastic-Job 自身的调度配置。这块配置要回答三个问题，执行哪个任务类、按什么 cron 触发、拆成几片。与注册中心那两个 new 不同，这块配置的 API 设计层层嵌套，一个配置对象套着另一个配置对象，课堂上的评价是「一环扣一环」，把它装配的层次理清楚，代码就只是照着层次填参数。

## 先给结论

- 整个配置类的最终产物是 `SpringJobScheduler` 对象，即任务调度器，由它负责按 cron 触发作业类的执行，创建后同样交给 Spring 管理。
- 构造 `SpringJobScheduler` 需要三样东西：作业对象、注册中心、`LiteJobConfiguration` 作业配置，前两个从容器注入，第三个在配置类里手工装配。
- `LiteJobConfiguration` 的装配链是三层包装：`JobCoreConfiguration` 装作业名、cron 与分片总数，包成 `SimpleJobConfiguration`，再包成 `LiteJobConfiguration`。
- 作业名取任务类的全类名，cron 与分片总数从 `application.properties` 经 `@Value` 注入，cron 是字符串类型，注入字段类型写错会直接编译报错。
- `overwrite(true)` 表示用当前配置覆盖注册中心里的旧配置，改过 cron 或分片数后不生效，多半是漏了它。

## 配置类需要注入什么

新建 `ElasticJobConfig` 配置类，类上标注 `@Configuration`，与注册中心配置类放在同一个 `config` 包里。往里写代码之前，先分析清楚 new 调度器时需要的数据，一共四样：

**第一是任务对象。**执行哪个任务必须告诉框架，入门案例的作业类此前已经编写完毕，`execute` 方法里封装了分片查询的逻辑，把它作为 Bean 注入进来，调度器才知道触发的是谁的 `execute`。

**第二是注册中心。**就是上一课配置类产出的 `ZookeeperRegistryCenter` Bean，调度器要通过它完成注册与协调。

**第三和第四是两个值：分片总数与 cron 表达式。**它们决定作业拆成几片、多久触发一次，值放在 `application.properties` 的 `myjob.count` 与 `myjob.cron` 里，用 `@Value` 注入：

```java
@Configuration
public class ElasticJobConfig {

    @Autowired
    private MyJob myJob;

    @Autowired
    private ZookeeperRegistryCenter registryCenter;

    @Value("${myjob.count}")
    private int shardingCount;

    @Value("${myjob.cron}")
    private String cron;
}
```

课堂实录里在这里踩过一个真实的坑：cron 属性声明成了 `int` 类型，方法里传参时编译器立刻报错。cron 是字符串，注入字段的类型要与最终用途一致，这是这类配置类最容易犯的低级错误。

## 三层包装：LiteJobConfiguration 的装配链

调度器的 `@Bean(initMethod = "init")` 方法最终就做一件事，new 一个 `SpringJobScheduler` 并返回。查看它的构造参数，前两个分别是作业对象与注册中心，第三个是一个 `LiteJobConfiguration` 类型的配置对象。这个对象的创建过程复杂，讲义单独抽取了一个 `createJobConfiguration` 方法负责装配：

```java
/**
 * 配置任务详细信息
 * @param jobClass 任务执行类
 * @param cron 执行策略
 * @param shardingTotalCount 分片数量
 * @return LiteJobConfiguration 作业配置
 */
private LiteJobConfiguration createJobConfiguration(
        final Class<? extends SimpleJob> jobClass,
        final String cron,
        final int shardingTotalCount) {
    // 1.创建 JobCoreConfiguration 的 Builder 静态工厂方法传入作业名 cron 分片总数
    JobCoreConfiguration.Builder coreBuilder = JobCoreConfiguration
            .newBuilder(jobClass.getName(), cron, shardingTotalCount);
    JobCoreConfiguration jobCoreConfiguration = coreBuilder.build();
    // 2.基础配置连同任务类全名包装成 SimpleJobConfiguration
    SimpleJobConfiguration simpleJobConfiguration =
            new SimpleJobConfiguration(jobCoreConfiguration, jobClass.getCanonicalName());
    // 3.包装成 LiteJobConfiguration overwrite 为 true 允许覆盖注册中心中的旧配置
    LiteJobConfiguration liteJobConfiguration = LiteJobConfiguration
            .newBuilder(simpleJobConfiguration)
            .jobShardingStrategyClass("com.dangdang.ddframe.job.lite.api.strategy.impl.AverageAllocationJobShardingStrategy")
            .overwrite(true)
            .build();
    return liteJobConfiguration;
}
```

**第一层是 `JobCoreConfiguration`。**它不是 new 出来的，而是调用静态工厂方法 `newBuilder`，传入作业名、cron 表达式、分片总数三个值，拿到一个 `Builder` 内部类对象，再调 `build()` 造出基础配置。作业名用的是 `jobClass.getName()`，即任务类的全类名，它对应 ZooKeeper 里的作业节点，必须全局唯一。也可以用 `getSimpleName()` 取简单类名，两者多数场景等价，不必纠结。

**第二层是 `SimpleJobConfiguration`。**直接 new，两个参数：第一层造出的基础配置，加上任务类的全限定名（`getCanonicalName()`）。这一层声明了作业的类型是简单作业。

**第三层是 `LiteJobConfiguration`。**同样不走构造方法，调静态方法 `newBuilder` 把第二层对象传进去，链式追加配置后 `build()` 出最终对象。链上两个方法值得说明：`jobShardingStrategyClass` 显式指定分片策略类的全路径，写的是平均分配策略，与框架默认行为一致，属于可写可不写的一行；`overwrite(true)` 打开覆盖开关，让本地配置在启动时覆盖注册中心已存的作业配置。

装配好配置对象后，调度器方法顺势而为：

```java
// 创建 SpringJobScheduler 任务调度器 初始化后由框架调度执行
@Bean(initMethod = "init")
public SpringJobScheduler initSimpleElasticJob() {
    SpringJobScheduler springJobScheduler = new SpringJobScheduler(
            myJob,
            registryCenter,
            createJobConfiguration(myJob.getClass(), cron, shardingCount));
    return springJobScheduler;
}
```

三个参数各就各位：注入的作业对象、注入的注册中心、调用装配方法得到的配置对象。`@Bean(initMethod = "init")` 的初始化方法同样是必需的，调度器在 init 中启动调度引擎。

整个装配过程用一张图收拢：

```mermaid
flowchart LR
    P[properties 文件] -->|@Value| C[ElasticJobConfig]
    J[任务类对象] --> S[SpringJobScheduler]
    C -->|注入注册中心 Bean| S
    C -->|cron 与分片总数| B1[JobCoreConfiguration 作业名 cron 分片数]
    B1 --> B2[SimpleJobConfiguration]
    B2 --> B3[LiteJobConfiguration overwrite 为 true]
    B3 --> S
    S --> R[启动后按 cron 触发作业类 execute]
```

图中纵向是数据的来路，横向是包装的层次。三层配置对象一层包一层，最后在 `SpringJobScheduler` 处汇合并启动，这正是这套 API「一环扣一环」的含义：每一层各管各的信息，谁也不能省。

这套装配代码属于典型的一次性模板代码，课堂的建议是理解层次关系后直接取用，不必逐行手敲。

## 常见误区

- **cron 属性注入类型写错。**错例：把 `@Value("${myjob.cron}")` 的字段声明成 `int`，方法传参处编译报错。正解：cron 表达式是字符串，分片总数才是 `int`，声明字段前先确认它在装配方法里的用途。
- **混淆三层配置对象。**错例：把 cron 与分片数直接塞给 `LiteJobConfiguration`，或忘了 `SimpleJobConfiguration` 这一层。正解：记牢包装顺序，核心参数进 `JobCoreConfiguration`，作业类型进 `SimpleJobConfiguration`，覆盖开关与分片策略挂在 `LiteJobConfiguration` 的构建链上。
- **漏掉 `overwrite(true)`。**错例：修改 cron 或分片数后重启应用，运行行为仍是旧值。正解：作业配置已在 ZooKeeper 中持久化，默认不覆盖，开发调试阶段必须打开 overwrite，让本地最新配置生效。
- **作业名当作可随意改的普通字符串。**错例：改名后重新启动，ZooKeeper 里同时出现新旧两个作业节点。正解：作业名是 ZooKeeper 中作业实例的根标识，框架依据它做选举与分片，更换作业名前先清理旧节点。
- **以为 `newBuilder` 可以换成 new。**错例：`new JobCoreConfiguration(...)` 或 `new LiteJobConfiguration(...)`，编译不通过。正解：这两个类的构造逻辑封闭在静态工厂方法与 Builder 内部类里，只能按框架提供的链式方式构建。

## 面试可能被问到的问题

1. 面试官追问：「SpringJobScheduler 是什么？构造它需要哪些参数？」
   答：它是 Elastic-Job 提供的 Spring 集成调度器，负责按 cron 触发作业执行并协调分片。构造需要三个参数：实现了 SimpleJob 接口的作业对象、初始化完成的 ZooKeeper 注册中心、封装调度规则的 LiteJobConfiguration，创建后以 Bean 形式交由 Spring 管理，并指定 init 方法启动调度。
2. 面试官追问：「LiteJobConfiguration 为什么要三层包装？」
   答：分层各司其职。JobCoreConfiguration 承载作业名、cron、分片总数等核心调度参数；SimpleJobConfiguration 在其上声明作业类型与实现类全名；LiteJobConfiguration 是顶层配置，附加覆盖开关、分片策略等运行期选项。层层包装让每一层职责单一，也便于框架按层级读取配置。
3. 面试官追问：「overwrite 配置项的作用是什么？什么时候必须开？」
   答：作业配置在首次运行后会持久化到注册中心，默认每次启动不覆盖。开发调试阶段经常调整 cron、分片数等参数，必须设置 overwrite 为 true 才能让本地新配置生效；生产环境配置稳定后可以关闭，避免误操作改掉线上调度行为。
4. 面试官追问：「作业名是怎么确定的？它有什么约束？」
   答：示例用任务类的全类名作为作业名，传入 JobCoreConfiguration 的 newBuilder。作业名对应 ZooKeeper 中的作业节点路径，是选举、分片、状态存储的根标识，同一集群实例必须使用相同作业名，不同作业不能重名。
5. 面试官追问：「分片策略在配置类里怎么指定？不指定用哪个？」
   答：可以在 LiteJobConfiguration 构建链上通过 jobShardingStrategyClass 指定分片策略类的全路径，示例指定的是平均分配策略 AverageAllocationJobShardingStrategy。不指定时框架默认就是平均分配，因此这一行通常可省，仅在需要换用哈希升降序或轮转策略时才显式配置。

## 配套资料

- 讲义：`materials/docs/10/万信金融-第5章-用户还款v1.0.md`，7.2 节功能实现中的「elastic-job 配置」部分（`ElasticJobConfig` 配置类、`createJobConfiguration` 三层装配与 `SpringJobScheduler` 创建）；Elastic-Job 入门案例的独立示例工程未随资料包归档，入门示例的属性键名为按课堂画面整理的 `myjob.count` 与 `myjob.cron`，项目版对应 Apollo 中的 `p2p.job.count` 与 `p2p.job.cron`。
- 代码：`materials/code/10/wanxinp2p/`，课程资料包内的工程源码归档目录（内含原始工程命名，与正文改写后的命名并非一一对应）；调度器配置类不在资料包源码内，文中代码以讲义为准，包名按 `com.study.finance` 系改写。
