# 06-基础数据微服务开发准备（Id生成器） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么接下来呢

继续来看我们基础数据为服务开发准备

刚才呢我们是把这个服务启动类啊

还有配置类呢都已经提供好了

下面还有一个小的点呢

就是这个ID生成器

这个呢我们可以把它看成就是一个小的工具类

对吧

那么通过它呢

主要可以帮我们来生成什么呢

我们的主件值

保证它是唯一的

好 那么接下来呢我们来创建一下

咱们可以把它

把这个类呢放在我们这个common bar下边

咱们在这儿来创建一个包

叫做common

好

然后下边呢我们来创建一个类啊

这个类的名字呢

就叫做customer

自定义的对吧

customer ID generator

好 在这儿我们来写一下

自定义ID生成器

好

然后呢我们需要通过一个component的注解呢

把它这个管理起来对吧

那么最终呢我们可以把这个对象啊

注入给我们

某一个组件

比如说注给我们的service

或者注给controller

直接使用它就可以了

好 component

然后呢我们需要让它实现一个接口啊

这个接口呢

是我们这个mybattis plus给我们提供的

这么一个接口叫做ID identity file

对吧

generator

好 这是它

这个呢这个接口的话呢

需要我们去实现这么一个方法

对吧

就是这个叫做next ID

其实就是产生下一个ID对吧

好 那么我们把这个方法呢给它实现出来

叫做next ID

好

这个方法呢就是生成

生成为1 ID

好

但是要生成的话应该如何来生成呢

在这儿的话呢我们会借助啊

会借助我们导入的这个pdcommon里边

给我们提供的一个叫做ID worker的这么一个组件

好 大家来看一下

在我们这个youtube下面对吧

有一个叫做ID worker的组件

有一个叫做ID worker的组件

好

通过它呢可以帮我们来生成什么呢

唯一的这种

你看它描述是分布式资增ID

对吧

生成唯一的一个ID

所以说呢我们直接借助它就可以了

直接借助它就可以了

那就意味着我们在这里边呢

是不是需要来创建这么一个ID worker

并且呢我们希望让Spring给我们管理起来

所以说呢我们在这儿呢来创建ID worker

不要导错了

是我们自己的这个

好 ID worker

然后呢咱们直接return

new一个ID worker就可以

好

需要注意的是什么呢

注意看它这个地方呢

需要来加一个什么

加一个bin注解

对吧

这样的话呢

我们就会把这个对象创建出来

并且呢由Spring容器来是不是来管理

来管理我们这个对象ID worker

然后呢我们来看一下它这个构造方法

你看它有一个无参的构造方法对吧

然后呢你也可以指定有参

第一个呢是work ID

就是工作的机器ID

第二个呢是这个序列号对吧

序列号

比如说我们这个也可以给它传入一个1

然后1

第一个呢代表就是work ID对吧

第二个呢就是我们这个序列号

好

这样的话呢我们就把这个ID worker呢

是不是给创建出来

并且呢由Spring容器来管理

然后呢我们是不是希望在咱们这个

next ID这个地方呢

来使用我们这个ID worker

所以说呢我们需要把它呢

注给我们当前这个对象对吧

注给这个对象

那么要注入的话呢

我们是不是就可以使用这个什么呢

AutoVar的注解

ID worker先把它注入一下

通过AutoVar的注解

把它注进来

AutoVar的

这其实相当于就是上面我们通过一个并标签对吧

然后呢把它创建出来

并且呢放到Spring容器当中

然后AutoVar的呢就是从Spring容器当中来查找

把它注到我们当前这个对象当中

然后接下来呢我们这个地方呢

就可以直接调用ID worker对吧

它给我们提供的一个方法

就叫做什么呢

叫做next ID

那这样的话呢它就可以

直接给我们返回一个唯一的ID了

所以到时候我们真正使用的时候呢

咱们就直接把当前这个对象

是不是把它注给我们的controller

或者service

然后呢调用它的一个next ID这个方法对吧

最终呢就可以产生一个ID

只不过呢这个ID呢是使用了一个

使用的ID worker来产生的

所以我们在这儿呢需要把它注入过来

那么之所以能够注入呢

是因为我们在这个地方是不是把它创建出来了

好

那么大概呢就是这么一个套路啊

那这样的话我们这个非常小的这么一个组件啊

就是自定义这个ID生成器

就已经搞定了

好那么到这儿的话呢

我们整个这个基础数据微服务啊

开发这些准备工作呢

咱们就都已经提供好了

然后后边的话呢

我们就可以直接来开发我们的业务代码了

好

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段为一个关于“品达物流TMS项目”中“基础数据服务开发”模块的技术课程。讲师正在使用 IntelliJ IDEA 开发环境，演示如何自定义一个分布式 ID 生成器。核心内容包括：
- **项目结构**：展示项目 `pd-base` 的目录结构，特别是 `common` 模块。
- **Swagger 配置**：在 `SwaggerConfig.java` 中配置 Swagger2 文档，用于 API 文档生成。
- **ID 生成器实现**：重点讲解并演示如何实现一个基于 `IdWorker` 的自定义 ID 生成器 `CustomIdGenerator`。
- **代码逻辑**：详细展示了 `IdWorker` 类的内部结构，包括时间戳、机器 ID、数据中心 ID 和序列号的位数划分，并解释了其工作原理。
- **Spring Boot 集成**：演示如何在 Spring Boot 中通过 `@Component` 和 `@Bean` 注解将自定义 ID 生成器注册为 Bean，并通过 `@Autowired` 注入使用。

整个过程旨在教授学生如何在项目中集成和使用一个高性能、高可用的分布式 ID 生成方案。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，展示项目结构，定位到 `pd-base` 模块下的 `common` 子模块。
*   **00:00:05 - 00:00:10**：切换到 `SwaggerConfig.java` 文件，展示如何开启 Swagger2 文档功能。
*   **00:00:10 - 00:00:15**：切换到 `CustomIdGenerator.java` 文件，准备编写自定义 ID 生成器。
*   **00:00:15 - 00:00:25**：在 `CustomIdGenerator.java` 中，导入 `IdentifierGenerator` 接口和 `IdWorker` 工具类，并声明类实现接口。
*   **00:00:25 - 00:00:35**：展示 `IdWorker` 类的源码，讲解其内部结构，包括 `workerIdBits`、`datacenterIdBits`、`sequenceBits` 等位数划分。
*   **00:00:35 - 00:00:45**：讲解 `IdWorker` 的构造函数，如何初始化 `datacenterId` 和 `workerId`。
*   **00:00:45 - 00:00:55**：讲解 `IdWorker` 的 `nextId()` 方法，其核心是通过 `sequence` 字段实现毫秒内递增。
*   **00:00:55 - 00:01:05**：在 `CustomIdGenerator` 中，使用 `@Bean` 注解创建 `IdWorker` 实例，并通过 `@Autowired` 注入。
*   **00:01:05 - 00:01:15**：在 `CustomIdGenerator` 的 `nextId()` 方法中，调用 `idWorker.nextId()` 来生成 ID。
*   **00:01:15 - 00:01:25**：展示最终的 `CustomIdGenerator` 类代码，完成自定义 ID 生成器的实现。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **标题**：`2.4 Id生成器`。
    *   **内容**：展示了 `CustomIdGenerator` 类的完整代码结构，包括 `@Component`、`@Bean`、`@Autowired` 注解，以及 `nextId()` 方法的实现。

*   **代码关键内容**：
    *   **Swagger 配置**：
        ```java
        @Configuration
        @EnableSwagger2
        public class SwaggerConfig extends WebMvcConfigurationSupport {
            @Bean
            public Docket createRestApi() {
                return new Docket(DocumentationType.SWAGGER_2)
                        .apiInfo(apiInfo())
                        .select()
                        .apis(RequestHandlerSelectors.basePackage("com.ithema.pinda.controller"))
                        .paths(PathSelectors.any())
                        .build();
            }
        }
        ```
    *   **自定义 ID 生成器 `CustomIdGenerator`**：
        ```java
        @Component
        public class CustomIdGenerator implements IdentifierGenerator {
            @Bean
            public IdWorker idWorker() {
                return new IdWorker(workerId: 1, datacenterId: 1);
            }

            @Autowired
            private IdWorker idWorker;

            @Override
            public Long nextId(Object entity) {
                return idWorker.nextId();
            }
        }
        ```
    *   **ID 生成器核心类 `IdWorker`**：
        ```java
        public class IdWorker {
            private final static long twepoch = System.currentTimeMillis();
            private final static long workerIdBits = 5L;
            private final static long datacenterIdBits = 5L;
            private final static long maxWorkerId = -1L << workerIdBits;
            private final static long maxDatacenterId = -1L << datacenterIdBits;
            private final static long sequenceBits = 12L;
            private final long workerId;
            private final long datacenterId;
            private long sequence = 0L;
            private long lastTimestamp = -1L;

            public IdWorker() {
                this.datacenterId = getDatacenterId(maxDatacenterId);
                this.workerId = getMaxWorkerId(maxWorkerId, datacenterId);
            }

            public IdWorker(long workerId, long datacenterId) {
                if (workerId > maxWorkerId || datacenterId > maxDatacenterId) {
                    throw new IllegalArgumentException("worker Id can't be greater than " + maxWorkerId);
                }
                this.workerId = workerId;
                this.datacenterId = datacenterId;
            }

            public synchronized long nextId() {
                long timestamp = System.currentTimeMillis();
                if (timestamp < lastTimestamp) {
                    throw new RuntimeException("Clock moved backwards. Refusing to generate id.");
                }
                if (timestamp == lastTimestamp) {
                    sequence = (sequence + 1) & sequenceMask;
                    if (sequence == 0) {
                        timestamp = tilNextMillis(lastTimestamp);
                    }
                } else {
                    sequence = 0;
                }
                lastTimestamp = timestamp;
                return ((timestamp - twepoch) << timestampBits) |
                        (datacenterId << datacenterIdBits) |
                        (workerId << workerIdBits) |
                        sequence;
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示** (00:00:00-00:00:05)
    *   讲师在 IntelliJ IDEA 中打开项目 `pd-base`，并导航到 `common` 模块，为后续的 ID 生成器开发做准备。

*   **场景二：Swagger 配置演示** (00:00:05-00:00:10)
    *   讲师切换到 `SwaggerConfig.java` 文件，展示如何通过 `@EnableSwagger2` 注解开启 Swagger2 文档功能，并通过 `Docket` 对象配置扫描的包路径，以便生成 API 文档。

*   **场景三：自定义 ID 生成器创建** (00:00:10-00:00:25)
    *   讲师在 `common` 模块下创建新文件 `CustomIdGenerator.java`，并导入 `IdentifierGenerator` 接口和 `IdWorker` 工具类，声明类实现接口。

*   **场景四：`IdWorker` 类结构讲解** (00:00:25-00:00:45)
    *   讲师在 `IdWorker` 类中，详细讲解了其内部的位数划分，包括时间戳、机器 ID、数据中心 ID 和序列号的位数，以及它们的取值范围。并解释了 `workerId` 和 `datacenterId` 的初始化逻辑。

*   **场景五：`CustomIdGenerator` 实现** (00:00:45-00:01:15)
    *   讲师在 `CustomIdGenerator` 类中，使用 `@Bean` 注解创建一个 `IdWorker` 实例，并通过 `@Autowired` 注入该实例。
    *   在 `nextId()` 方法中，调用 `idWorker.nextId()` 来生成 ID，从而实现了自定义 ID 生成器的功能。

*   **场景六：最终代码展示** (00:01:15-00:01:25)
    *   讲师展示了最终完成的 `CustomIdGenerator` 类代码，强调其通过 Spring Boot 的依赖注入机制，可以方便地在项目中使用。
