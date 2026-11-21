# 23-RocketMQ集成-代理服务集成配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始讲解和实现代理服务与LockitMQ的机身配置

首先咱们要添加对应的POM依赖

咱们回到代码当中

找到代理服务POM依赖文件

这里咱们看到已经加上了LockitMQ消息主线的依赖

这样咱们就不需要重复去添加

注意一下它的Group ID在这里做了调整

从之前的Spring Framework下面独立迁移出来

咱们将Group ID做一个修正

接着就是配置文件的修改

在这里要增加LockitMQ消费端相关的配置

之前的行情服务和MQ的机身

在这里是服务端也就是发送端的一个配置

在代理服务当中

它是属于订阅消息的消费者

咱们来看一下消费端这一块是如何去配置实现的

咱们回到代码当中

对配置做一个详细讲解

咱们来看一下

在这里开始是LockitMQ消费端的配置

在这里它绑定的是Quart的对立

下面是消费端的一个配置策略

这里是并发数的设置

也就是消费端最多有多少个线程

能够去同时从对立当中消费消息

下面是它的最大尝试次数

这些根据业务需要

去做对应的设置

在这里咱们设定为一次

避免重复消费处理

下面这个是ContentType

这个是ContentType

标识消息的类型

下面这个是消息的订阅堆叠

咱们是消费端

要订阅的目标堆叠

然后是Group

这个是消费分组

当咱们Blockit服务存在多个节点的时候

我们要标识不同的分组

可以订阅的分组是Blockit服务存在多个节点的时候

可以订阅的分组是Blockit服务存在多个节点的时候

可以订阅的分组是Blockit服务存在多个节点的时候

同一个消息队列

这样配置能够确保每个代理服务节点

都能够收到行情服务所下发过来的数据

这个是BlockitMQ服务的连接地址

下面我们有个配置项

这个配置项是Oddly

在这里它的值是为2

这个配置项的主要作用

是为了保证接收的消息能够有序处理

咱们再回到讲义当中

下面对整个配置项

也做了说明

和介绍

大家注意一下

在这里的Group设置

每个代理服务的分组名称要保持为一

如果是出现相同的情况

数据会被其他消费端增强消费

不同的Group都可以消费到相同的topic消息

咱们在这里采用的是网播消费

而非集群消费

至于这两者的区别

大家可以参考相关的资料文档

接下来咱们再去实现代码相关的配置

我们可以看到

回到咱们的代码当中

在Proxy工程下面

咱们先创建相应的包

Open in Terminal

创建三个包

一个是Configure

接下来是MQ

然后是Startup启动的包

咱们首先实现MQ的代码配置

在这里咱们创建一个类

这个是专门用于Proxy代理服务的

是一个消费的代码

我们先把这个配置的内容

给它加上了对应的注写

Service

Log日志的注写

咱们定一个消息接收的处理方法

Public

Void

CEI

Input

它的参数是传递Chadstock

Botlast

最新行情数据对象

咱们要给这个参数对象加上一个注写

Payload

标识图

Payload

标识它的数据传输序调化处理方式

Payload的注写

它是标识

参数传输对象是采用节省的方式进行序调化处理

接下来咱们打印一个日志

将接收到的消息打印出来

通过咱们的CEIInput的方法进行处理

直接进行打印

接着咱们还做一个注写配置

要绑定咱们的消费端的配置信息

这过程

咱们在配置文件当中

这里面所定义的quota的消费项配置

它会绑定对应的消费对链

以及采用相应的分组配置

下面咱们再回到讲义当中

在这里面的实现

咱们加入了StreamListener的注写

它的作用是指定坚定的配置对链

然后Payload注写

这个也需要加上

它是标识数据

采用阶层的格式进行传递

同时它也和服务端的发送消息

它的类型要保持一致

咱们可以回过头来看一下行情服务

之前咱们实现了它的消息发送

在这里它也采用了Payload的方式

进行消息的包装和传递

接着咱们再去实现LockitMQ

它的消息堆叠的绑定配置

咱们回到代码当中做相应的实现

在Config包下面咱们去创建一个配置类

这个叫LockitMQ

Consume Configuration

首先加上它对应的注写

接下来咱们首先定义一个接口

用于消息堆叠的绑定

这个是消费端需要坚定的堆叠

它采用定阅的方式

咱们要加上一个注写

Impute绑定Quart的消息堆叠配置

然后呢?

咱们再去开启它的绑定注写

让它能够去绑定咱们所定义的接口

Qsrc

这个配置类的作用

是让消费端能够绑定到它的监听队列

注意这个名称要和这里面所定义的名称导致一致

这个是队列的监听绑定

这个是队列的监听绑定

在这里就从队列当中去读取和消费消息

这是它们的一个作用

接着的话呢?咱们再去实现启动类

stock proxy application

定义它的启动方法

bsvm spring application.run

指定当前的类

接着咱们加上对应的注写

spring boot application

然后Enable discovery client

company screen 包的扫描

指向了咱们的基础包

base package

com.idcast

logo4j2的日子

这个可以不需要

最后一个就是要开启对应的缓存

Enable cache

咱们先将缓存功能开启

后面业务功能的时候可能会需要使用到

好

咱们再回到讲义当中

在这里咱们就实现了代理服务和Lockit MQ的集成配置

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于使用 Spring Cloud Stream 与 RocketMQ 进行消息集成的实战教程。讲师通过演示一个名为 `bulls-stock-proxy` 的代理服务项目，详细讲解了如何配置消费者（Consumer）和生产者（Producer）以实现行情数据的订阅与发布。核心内容包括：添加必要的 Maven 依赖、配置 `bootstrap-dev.yml` 文件以定义 RocketMQ 的连接信息和消息队列绑定、编写 `@StreamListener` 消费者代码、以及通过 `@EnableBinding` 启用消息绑定功能。最后，通过启动服务并观察控制台日志，验证了消息订阅功能的正确性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 中展示课程大纲，当前章节为“3.2 代理服务与MQ集成配置”。
*   **00:00:05 - 00:00:15**: 讲师在 Typora 中展示 `pom.xml` 的依赖配置，重点是引入 `spring-cloud-starter-stream-rocketmq`。
*   **00:00:15 - 00:00:30**: 讲师在 Typora 中展示 `bootstrap-dev.yml` 文件的配置内容，包括 `spring.cloud.stream.bindings.quote.destination` 和 `rocketmq.binder.name-server`。
*   **00:00:30 - 00:00:45**: 讲师切换到 IntelliJ IDEA，展示 `bulls-stock-proxy` 项目结构，并在 `bootstrap-dev.yml` 中高亮显示 `name-server` 配置。
*   **00:00:45 - 00:01:00**: 讲师在 IDEA 中展示 `ProxyQuoteConsumer` 类的代码，其中包含 `@StreamListener` 注解和 `receiveInput` 方法。
*   **00:01:00 - 00:01:15**: 讲师在 IDEA 中展示 `RocketMqConsumerConfiguration` 类，高亮显示 `@EnableBinding` 注解。
*   **00:01:15 - 00:01:30**: 讲师在 IDEA 中展示 `StockProxyApplication` 的主类，高亮显示 `@ComponentScan` 注解。
*   **00:01:30 - 00:01:45**: 讲师在 Typora 中展示“3.3 行情订阅发布功能验证”章节，并演示如何通过控制台日志观察消息接收情况。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “3.2 代理服务与MQ集成配置” 和 “3.3 行情订阅发布功能验证”。
    *   **关键注释**: “@StreamListener 注解，指定监听的配置队列。”、“@Payload 注解加上，它是标识数据以 JSON 格式进行传输，要与服务端的发送消息体类保持一致。”、“@EnableBinding 绑定 Queue 接口。”
    *   **配置文件说明**: “bootstrap-dev.yml” 文件用于配置 RocketMQ 的服务端地址和消息队列绑定。

*   **代码关键内容**:
    *   **Maven 依赖**:
        ```xml
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-stream-rocketmq</artifactId>
        </dependency>
        ```
    *   **配置文件 `bootstrap-dev.yml`**:
        ```yaml
        spring:
          cloud:
            stream:
              bindings:
                quote:
                  content-type: application/json
                  destination: stock-quote
              rocketmq:
                binder:
                  name-server: 10.10.20.15:9876
        ```
    *   **消费者代码 `ProxyQuoteConsumer.java`**:
        ```java
        @Service
        public class ProxyQuoteConsumer {
            @StreamListener("quote")
            public void receiveInput(@Payload TradeStockQuoteLast receiveMsg) {
                System.out.println("receive quote: " + receiveMsg);
            }
        }
        ```
    *   **配置类 `RocketMqConsumerConfiguration.java`**:
        ```java
        @Configuration
        @EnableBinding(RocketMqMessageSource.class)
        public class RocketMqConsumerConfiguration {
        }
        ```
    *   **主类 `StockProxyApplication.java`**:
        ```java
        @SpringBootApplication
        @ComponentScan(basePackages = "com.ictast.bulls.stock.proxy")
        public class StockProxyApplication {
            public static void main(String[] args) {
                SpringApplication.run(StockProxyApplication.class, args);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：依赖配置** (00:00:05)
    *   **描述**: 讲师在 Typora 中展示 `pom.xml` 文件，高亮显示 `spring-cloud-starter-stream-rocketmq` 依赖项，强调这是实现消息集成的基础。

*   **场景二：配置文件编写** (00:00:15)
    *   **描述**: 讲师在 Typora 中展示 `bootstrap-dev.yml` 文件的配置内容，详细解释了 `destination` 和 `name-server` 的作用，确保消费者能正确连接到 RocketMQ 服务并监听指定队列。

*   **场景三：IDEA 项目结构与代码编写** (00:00:30)
    *   **描述**: 讲师切换到 IntelliJ IDEA，展示 `bulls-stock-proxy` 项目的目录结构。随后，他高亮显示 `bootstrap-dev.yml` 中的 `name-server` 配置，并在 `ProxyQuoteConsumer` 类中编写 `@StreamListener` 注解和接收消息的方法，演示了如何定义消息监听器。

*   **场景四：启用绑定功能** (00:01:00)
    *   **描述**: 讲师在 IDEA 中展示 `RocketMqConsumerConfiguration` 类，高亮显示 `@EnableBinding` 注解，并说明其作用是将 `RocketMqMessageSource` 接口绑定到消息通道，使 Spring Cloud Stream 能够识别和处理消息。

*   **场景五：主类配置与启动** (00:01:15)
    *   **描述**: 讲师在 IDEA 中展示 `StockProxyApplication` 的主类，高亮显示 `@ComponentScan` 注解，并说明其用于扫描包路径，确保所有配置类和组件都能被 Spring 容器加载。

*   **场景六：功能验证** (00:01:30)
    *   **描述**: 讲师在 Typora 中展示“3.3 行情订阅发布功能验证”章节，并演示如何通过控制台日志观察消息接收情况，验证了代理服务成功订阅了行情数据。
