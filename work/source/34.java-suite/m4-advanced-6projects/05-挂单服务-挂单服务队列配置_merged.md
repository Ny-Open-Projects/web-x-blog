# 05-挂单服务-挂单服务队列配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们开始实现挂单服务的对列配置

挂单服务也要配置行情员监听对列

用于获取实时下发的行情数据

因为挂单服务需要根据实时的行情数据去处理下单信息

Lockit MQ消息对列的集成配置咱们之前也做过讲解

在这里咱们来实现一下

首先创建Lockit MQ消息对列的配置类

回到工程当中

在挂单服务Configure目标前面

右键New Java Class

咱们将名称拷贝进来

点击OK

配置类已经创建完成

回到讲解当中

将配置代码拷贝进去

那咱们来看一下

在这里是配置类的一个注解

下面就是Enable Bundy

这里是要绑定的消息对列配置

指向的是Q-Source的接口

Q-Source

它绑定的是Quart的消息对列的配置

这个名称不要弄错了

适合工程配置里面的Lockit MQ消息对列配置名称

要保持一致

这里是工程里面的Lockit MQ消费端的配置

注意它的配置名字是Quart

下面是作为消费端的具体配置信息

刚才的Lockit MQ配置类

它绑定的就是工程配置里面的Quart配置信息

好

咱们再回到讲义当中

实现完配置类之后

接着就要去实现对列消息监听处理类

咱们在这里先创建好

后面还会去实现它具体的业务逻辑

咱们在这里先copy一下

回到工程代码当中

在MQ包下面创建新的Java Class

Java Class名称叫Pending

Quart

Consumer

它是作为挂单服务

行情数据监听的处理类

咱们将讲义当中的代码copy进来

将这些错误信息做个修正

Value导入进来

Spring Blink Walk下面

这个的话暂时不做实现

在后面大家讲解的时候

咱们再做具体的实现

咱们先创建Service神的接口

在Service包下面

右键New

Java Class选择Innovate

添加对应的注释

这个是挂单服务

业务层接口

接下来咱们再创建一下它的实现类

New Package

Employment

New Java Class

实现类就叫Stock Trade

Pending

Service Employment

它去实现刚才所创建的接口

添加注释

挂单服务

业务层

实现类

添加注写Service

添加Log日志查件

咱们再回到消息消费的实现类当中

这里咱们添加相应的注释

这个LogKey是用于挂单对电不同订单的锁处理

保障整个挂单对电是能够有序处理

这个就是挂单对电的锁控制

避免进阀产生的数据维持问题

下面咱们会讲解它的具体的复制问题

这里是挂单服务的端口

每个挂单服务的端口不一样

它的作用是用于标识挂单服务的缓存对电

这样每个挂单服务的数据就互不干扰

每个挂单对电可以处理自己的消息

从而也可以提升挂单服务的吞吐能力

上面是现成词的推测

用于提升整体的处理速度

这个就是挂单服务的业务层接口

负责核心逻辑处理

上面是CacheManager

是缓存管理器

好,在这里就是挂单服务队列集成配置的实现

下面的章节会基于消息队列

再做具体的业务逻辑实现

那这里讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是“交易平台 - Day 15”课程的一部分，主要讲解如何在 Spring Cloud 微服务架构中，通过 Spring Cloud Stream 和 RocketMQ 消息中间件，配置并实现一个“挂单服务”的行情数据消费功能。核心内容包括：
- **配置类**：使用 `@Configuration` 和 `@EnableBinding` 注解定义消息队列的绑定关系。
- **消息接口**：定义一个 `QueueSource` 接口，通过 `@Input("quote")` 注解声明一个名为 `quote` 的输入通道。
- **消费者服务**：编写 `PendingQuoteConsumer` 类，使用 `@StreamListener` 注解监听 `quote` 通道，接收并处理行情数据。
- **业务服务**：定义 `IStockTradePendingService` 接口及其实现类 `StockTradePendingServiceImpl`，用于处理具体的挂单业务逻辑。
- **配置文件**：在 `bootstrap-dev.yml` 中配置 RocketMQ 的连接信息和数据源。

整个过程展示了如何将消息队列的消费能力与后端业务逻辑解耦，实现高内聚、低耦合的微服务架构。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面中未提供明确的时间戳，以下时间点是根据画面内容和课程逻辑推断的：

- **00:00 - 00:05**：课程标题页，显示“交易平台 - Day 15”和“第1章 挂单服务工程搭建”。
- **00:05 - 00:15**：讲解“3.3 挂单服务队列配置”章节，展示 `RocketMqConsumeConfiguration` 配置类的代码。
- **00:15 - 00:25**：展示 `QueueSource` 接口的定义，重点讲解 `@Input("quote")` 注解的作用。
- **00:25 - 00:35**：切换到 `PendingQuoteConsumer` 类，讲解其成员变量和 `@StreamListener` 注解。
- **00:35 - 00:45**：展示 `IStockTradePendingService` 接口，说明其作为业务层的抽象。
- **00:45 - 00:55**：展示 `StockTradePendingServiceImpl` 实现类，讲解其业务逻辑。
- **00:55 - 01:05**：展示 `bootstrap-dev.yml` 配置文件，讲解 RocketMQ 和数据库的配置。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **文档标题**：`Day15.md`，位于 Typora 编辑器中。
- **章节标题**：`3.3 挂单服务队列配置`。
- **学习目标**：配置行情源监听队列，获取实时下发的行情数据。

#### 代码关键内容

- **配置类 `RocketMqConsumeConfiguration`**：
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
  - `@Configuration`：声明这是一个 Spring 配置类。
  - `@EnableBinding`：启用绑定功能，将 `QueueSource` 接口与消息通道关联。
  - `@Input("quote")`：声明一个名为 `quote` 的输入通道，用于接收消息。

- **消费者类 `PendingQuoteConsumer`**：
  ```java
  @Service
  public class PendingQuoteConsumer {
      @Autowired
      private IStockTradePendingService stockTradeService;
      
      @Autowired
      private TaskExecutor taskExecutor;
      
      @Value("${server.port}")
      private String serverPort;
      
      public static Map<Long, Long> lockKeys = new ConcurrentHashMap<Long, Long>();
      
      @StreamListener("quote")
      public void receiveInput1(@Payload TradeStockQuoteLast quoteLastMsg) {
          // TODO 待实现
      }
  }
  ```
  - `@StreamListener("quote")`：监听名为 `quote` 的消息通道。
  - `@Payload`：标注方法参数，表示该参数是接收到的消息体。
  - `lockKeys`：一个静态的 `ConcurrentHashMap`，用于实现分布式锁，避免并发问题。

- **业务接口 `IStockTradePendingService`**：
  ```java
  public interface IStockTradePendingService {
      // 定义业务方法
  }
  ```

- **业务实现类 `StockTradePendingServiceImpl`**：
  ```java
  public class StockTradePendingServiceImpl implements IStockTradePendingService {
      // 实现具体的业务逻辑
  }
  ```

- **配置文件 `bootstrap-dev.yml`**：
  ```yaml
  rocketmq:
    name-server: 10.10.20.15:9876
    binder:
      name: stock-pending-1
      quote:
        consumer:
          orderly: true
  datasources:
    tradesystem:
      type: com.alibaba.druid.pool.DruidDataSource
      driver-class-name: org.postgresql.Driver
      username: office
      password: 654321
      url: jdbc:postgresql://192.168.19.150:5432/trade_stock
      druid:
        # Druid 数据源配置
  ```

---

### 4) 关键场景与演示描述

- **场景一：配置类定义**（00:05 - 00:15）
  - 讲师在 IDE 中打开 `RocketMqConsumeConfiguration.java` 文件。
  - 重点讲解 `@EnableBinding` 注解的作用，说明它将 `QueueSource` 接口与消息通道绑定。
  - 强调 `@Input("quote")` 注解定义了消息通道的名称，后续消费者将通过此名称监听消息。

- **场景二：消费者服务实现**（00:25 - 00:35）
  - 讲师切换到 `PendingQuoteConsumer.java` 文件。
  - 展示 `@StreamListener("quote")` 注解，说明它将方法绑定到 `quote` 通道。
  - 介绍 `@Payload` 注解，用于自动将消息体注入到方法参数中。
  - 讲解 `lockKeys` 静态变量的作用，用于实现分布式锁，确保数据一致性。

- **场景三：业务服务层**（00:35 - 00:45）
  - 讲师展示 `IStockTradePendingService` 接口，说明其作为业务层的抽象。
  - 通过 `StockTradePendingServiceImpl` 类，演示如何实现具体的业务逻辑。

- **场景四：配置文件**（00:55 - 01:05）
  - 讲师打开 `bootstrap-dev.yml` 文件。
  - 重点讲解 RocketMQ 的配置，包括 `name-server` 地址和 `binder` 的配置。
  - 展示数据库配置，说明如何连接 PostgreSQL 数据库。

- **场景五：整体架构**（00:45 - 00:55）
  - 讲师在 IDE 中展示项目结构，说明 `PendingQuoteConsumer`、`IStockTradePendingService` 和 `StockTradePendingServiceImpl` 之间的关系。
  - 强调消息队列作为中间件，将消费者与业务服务解耦，提高系统的可扩展性和可维护性。

---

以上是根据视频画面进行的结构化技术分析，希望能帮助您更好地理解课程内容。
