# Elastic-Job 入门案例：用配置类把 ZooKeeper 注册中心建起来

> 🔒 安全提示：文中示例的口令/密钥均为课程教学环境演示口径，生产环境的安全要求见《安全与合规须知》。

作业类已经就绪：`execute` 方法里拿着分片总数与分片项做分片查询，逻辑本身没有悬念。问题紧接着来了，这个方法由谁来触发？Elastic-Job 的答案是配置：注册中心的配置加调度器的配置，两块配齐，框架才有能力在既定时刻调起作业。这一课先解决第一块，把 ZooKeeper 注册中心通过一个配置类创建出来，交给 Spring 容器管理。

## 先给结论

- 作业类只负责执行，触发与协调靠配置，配置分两大块：ZooKeeper 注册中心配置、Elastic-Job 调度配置，本课先做前者。
- 注册中心在代码里的载体是 `ZookeeperRegistryCenter` 对象，它由 `ZookeeperConfiguration` 创建，构造参数只有两个：ZooKeeper 服务地址与作业命名空间。
- 两个参数不写死在代码里，落在 `application.properties` 中，经 `@Value` 注入配置类，键为 `zookeeper.connString` 与 `myjob.namespace`。
- `@Bean(initMethod = "init")` 是最容易漏也最致命的一处：`init` 方法负责真正建立与 ZooKeeper 的会话，漏掉它 Bean 照样能创建，但注册中心形同虚设。
- 分片总数是几，理论上就要启动几个微服务实例，实例启动后都向 ZooKeeper 注册，由 ZooKeeper 的选举机制选出 Leader 负责分片。

## 为什么第一块配置是注册中心

ZooKeeper 在这套体系里的角色，和微服务阶段接触过的 Eureka 类似，是一个微服务注册与管理中心。启动的每个作业实例都要注册到它那里，Elastic-Job 借助它完成三件事：实例的上线感知、Leader 选举、分片分配的协调。

入门案例的分片总数配置为 3，含义就是要把这个作业拆成三片，分给三个实例并行执行。三个实例启动后都往 ZooKeeper 注册，注册完成后框架利用 ZooKeeper 的选举机制选出一个 Leader，由 Leader 依据分片策略把三片分下去。注册中心此刻还不存在，所以第一步就是写一个配置类把它造出来。

配置类放在工程的 `config` 包下，类名沿用 `ZKRegistryCenterConfig`，类上标注 `@Configuration`，让 Spring 在启动时扫描并处理它。

## 配置项先落到 properties 文件

造一个注册中心，必须知道两件事：ZooKeeper 服务的 IP 地址与端口号、作业的命名空间。命名空间可以理解为 ZooKeeper 里的一层目录前缀，不同项目的作业各自隔离，互不干扰。这两个值都放进 `application.properties`：

```properties
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/mp?useUnicode=true&characterEncoding=utf8&autoReconnect=true
spring.datasource.username=root
spring.datasource.password=123456

# 数据访问层映射文件位置
mybatis-plus.mapper-locations = classpath*:dao/*.xml
mybatis-plus.type-aliases-package = com.study.finance.elasticjob.pojo

# zookeeper服务地址
zookeeper.connString = localhost:2181
# 定时任务命名空间
myjob.namespace = elastic-job-example
# 分片总数
myjob.count = 3
# cron表达式(定时策略)
myjob.cron = 0/5 * * * * ?
```

数据源与 MyBatis-Plus 的部分是作业查询数据用的常规配置，与调度无关；与注册中心直接相关的是 `zookeeper.connString` 与 `myjob.namespace` 两行，本课只用它们，分片总数与 cron 留给下一个配置类使用。

## 配置类的完整实现

配置类的骨架是「两个属性注入，一个 Bean 方法」，对照代码看：

```java
@Configuration
public class ZKRegistryCenterConfig {

    // zookeeper服务地址
    @Value("${zookeeper.connString}")
    private String ZOOKEEPER_CONNECTION_STRING;

    // 定时任务命名空间
    @Value("${myjob.namespace}")
    private String JOB_NAMESPACE;

    // zk的配置及创建注册中心
    @Bean(initMethod = "init")
    public ZookeeperRegistryCenter setupRegistryCenter() {
        // zk的配置 封装服务地址与命名空间
        ZookeeperConfiguration zookeeperConfiguration =
                new ZookeeperConfiguration(ZOOKEEPER_CONNECTION_STRING, JOB_NAMESPACE);
        // 创建注册中心
        ZookeeperRegistryCenter zookeeperRegistryCenter =
                new ZookeeperRegistryCenter(zookeeperConfiguration);
        return zookeeperRegistryCenter;
    }
}
```

**第一，属性注入取的是键而不是值。**`@Value` 里写的表达式是 `${zookeeper.connString}`，大括号里是 properties 文件中「等号前」的键，Spring 启动时按键取到等号后的值，再赋给字段。两个属性的名字保持全大写常量风格，与讲义一致，属性名本身可以自定，表达式里的键不能写错。

**第二，创建过程就是两个 new。**第一个 new 造 `ZookeeperConfiguration`，这是 ZooKeeper 的配置对象，把服务地址与命名空间封装进去；第二个 new 拿着配置对象造 `ZookeeperRegistryCenter`，注册中心就创建出来了，方法把它作为返回值交回 Spring。

**第三，`@Bean` 后面跟着的 `initMethod = "init"` 必须强调。**它指定 Bean 创建完成后自动执行 `ZookeeperRegistryCenter` 内部的 `init` 方法，真正去连接 ZooKeeper、建立会话。只 new 出对象而不调 `init`，Spring 启动不会报错，作业运行时才会发现注册中心根本没连上，这类问题排查起来相当隐蔽，写的时候就要盯住这个注解。

整条链路画出来是这样：

```mermaid
flowchart LR
    P[application.properties] -->|@Value 按键取值| C[ZKRegistryCenterConfig 配置类]
    C --> A[ZookeeperConfiguration 封装地址与命名空间]
    A --> R[ZookeeperRegistryCenter]
    R -->|initMethod init 建立会话| ZK[ZooKeeper 注册中心]
    ZK --> E[实例注册与 Leader 选举]
```

从图上可以看出数据流向单一：配置文件出值，配置类收值，配置对象封装值，注册中心消费值。右侧两步发生在多个服务实例同时启动时，属于框架在 ZooKeeper 之上自动完成的协调动作，不需要写任何代码。

到这里 ZooKeeper 相关的配置就绪了。剩下的一块是 Elastic-Job 自身的调度配置，它要回答的问题更具体：执行哪个任务类、按什么 cron 触发、分成几片，那是下一课的内容。

## 常见误区

- **漏写 `initMethod = "init"`。**错例：`@Bean` 上什么参数都不带，应用启动正常。正解：Bean 虽然创建成功，但没有与 ZooKeeper 建立会话，作业触发时拿不到注册中心能力，必须在 `@Bean` 注解上显式指定初始化方法。
- **`@Value` 的键与配置文件对不上。**错例：代码里写 `${zookeeper.connectString}`，文件里却是 `zookeeper.connString`，启动即抛占位符无法解析的异常。正解：键名以配置类 `@Value` 表达式与 properties 文件两侧一致为准，改动时两边同步。
- **命名空间随手乱起或中途更换。**错例：调试时把 `myjob.namespace` 改来改去，出现作业状态混乱、旧配置残留。正解：命名空间在 ZooKeeper 中是隔离单元，同一个作业集群必须共用一个固定命名空间，更换前清理 ZooKeeper 中对应节点。
- **把注册中心当成普通对象自己 new 了持有。**错例：在业务代码里直接 `new ZookeeperRegistryCenter(...)` 使用。正解：注册中心必须以 `@Bean` 方式交给 Spring 管理，后面的调度器配置要从容器里注入这个 Bean，脱离容器的实例无法参与框架生命周期。

## 面试可能被问到的问题

1. 面试官追问：「Elastic-Job 为什么需要一个 ZooKeeper 注册中心配置？」
   答：Elastic-Job 的分布式协调全部建立在 ZooKeeper 之上，实例注册、Leader 选举、分片分配都依赖它。配置类的作用是在 Spring 容器启动时创建并初始化 `ZookeeperRegistryCenter`，为后续的调度器提供协调服务，没有它作业就退化成单机定时逻辑。
2. 面试官追问：「`@Bean(initMethod = "init")` 里的 init 方法做了什么？不指定会怎样？」
   答：init 负责与 ZooKeeper 建立连接和会话，完成注册中心的内部初始化。不指定时 Bean 能正常创建，Spring 启动不报错，但注册中心未连接，作业触发时才会暴露问题，属于典型的延迟失效故障，排查成本高。
3. 面试官追问：「ZookeeperConfiguration 的构造参数有哪些？分别什么含义？」
   答：核心两个参数：连接串和命名空间。连接串是 ZooKeeper 服务地址加端口，集群场景写多台用逗号分隔；命名空间是本作业在 ZooKeeper 里的根节点前缀，用于多项目、多作业之间的数据隔离。
4. 面试官追问：「分片总数配置为 3，和要启动的实例数是什么关系？」
   答：分片总数是作业被拆成的片数，理论上启动相同数量的实例可以让每台领一片，并行度最高。实例数少于分片数时框架仍能运行，一个实例领多片；多于分片数时会有实例分不到片而空闲。它决定的是任务拆分粒度，不是必须的进程数。
5. 面试官追问：「@Value 注入的时机和取值规则是什么？」
   答：Spring 在创建 Bean、完成属性填充阶段解析 `@Value` 表达式，`${key}` 形式会到 Environment 中按键查找配置源，包括 properties 文件与配置中心下发的属性。键不存在且无默认值时启动直接失败，因此键名必须与配置文件严格一致。

## 配套资料

- 讲义：`materials/docs/10/万信金融-第5章-用户还款v1.0.md`，7.2 节功能实现中的「zookeeper 配置」部分（`ZKRegistryCenterConfig` 配置类源码、`@Bean(initMethod = "init")` 写法）；Elastic-Job 入门案例的独立示例工程未随资料包归档，示例中的 `application.properties` 为按课堂画面内容整理，包名按 `com.study.finance` 系改写。
- 代码：`materials/code/10/wanxinp2p/`，课程资料包内的工程源码归档目录（内含原始工程命名，与正文改写后的命名并非一一对应）；注册中心配置类未包含在资料包源码中，文中代码以讲义与课堂画面为准。
