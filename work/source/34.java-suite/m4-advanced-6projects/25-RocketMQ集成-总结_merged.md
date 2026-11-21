# 25-RocketMQ集成-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对本章内容做个回顾和总结

首先咱们看一下本章的学习目标

在这里咱们要完成行情服务和代理服务的配置

去集成和实现LockitMQ的整合

在这里通过LockitMQ

咱们就可以实现行情数据的订阅和分发处理功能

那咱们回顾一下本章所讲解的内容

首先的话咱们对实现方面做了一个讲解

行情服务的行情数据是如何流转到代理服务当中

咱们采用的是网货模式消费

确保每个代理服务节点都能够正常接收到行情消息

接下来咱们就实现了行情服务和LockitMQ的集成配置

首先要确保添加了LockitMQ消息组件依赖

然后在配置文件当中要注意LockitMQ服务端的具体配置

这里适应可维修

也就是说咱们消息的发送是采用同步方式

确保行情报价信息能够有序处理

接着咱们对MQ发送功能做了一个封装

咱们封装的两种发送方式

一种是附带Tag标记

另一种是不附带Tag标记直接方式进行发送

咱们在这里采用的是不带Tag的接口发送消息

因为咱们行情信息的业务处理功能

要单一

咱们暂时不需要通过Tag标记去处理不同的业务逻辑

方法的发送是采用配肉的方式

咱们是通过阶层方式去序列化处理传输数据

最后要实现消息的发送

还必须要绑定AutoPool对应的消息队列

注意这里面的AutoPool的注解

它的值为Quot

这个要和配置文件当中的配置项名称保持对应

接下来咱们就实现了

代理服务和MQ的集成配置

整个实现处理流程也是基本上一致的

但是不同的是要指定相关的消费配置

比如说最大的一个并发现成数量

最多的一个消息从事消费次数

这里要注意一下Group的配置

Group是分组名称

咱们代理服务可能会存在多个节点

所以分组名称要保持为一

出现相同的情况

这些数据有可能配备其他消费端

也就是其他代理服务节点的增强消费

不同的Group都可以消费到相同的topic消息

也就实现了类似于广播的消费处理

下面也提供了一个资料

就是集群消费和广播消费的区别

大家可以从相关的文档上再做一个具体了解

然后咱们要绑定监听处理接口

监听处理接口它的配置项是Quota

消息类型是Portable

配肉的这个呢

是以阶层格式进行数据的传输

那么这个Quota呢

要和下面的LockitMQ消息对列的绑定呢

是要保持一致

这里呢

他配置名称是Quota

上面的这个名称也要保持一致

最后呢

咱们就通过行情订阅发布功能做了一个测试和验证

整个测试流程呢

是从行情服务启动接收到行情数据

然后再将行情信息呢

下发给代理服务端

咱们通过控制台呢

可以查看到代理服务端呢

能够正常接收到消息

通过查看代理服务的控制后台

可以呢

正常接收到行情服务所发布的行情数据

然后咱们呢

也打开了控制台

查看了Topic的消费管理信息

消费管理信息当中

可以看到咱们所建立的分组订阅信息

并且呢

也可以成功去消费了所有的行情消息数据

最后咱们再来总结下

在这里咱们集成了LockitMQ

由行情服务进行推送

通过代理服务去订阅行情数据

并且呢

可以将这些数据再分发给客户端

客户端的消息订阅呢

咱们后面还会做讲解

在这里代理服务呢

是采用无状态的设计

支持水平扩展

当单个节点出现瓶颈了

咱们可以水平扩充的方式去扩展代理服务的分组能力

从而能够提升整个集群的分组能力

使用量

如果用户所属区域分布比较善练

咱们还可以通过代理服务呢

去部署在多个不同区域当中

类似于CDN的节点

从而能够提升咱们的行情数据传输交互速度

最后呢

咱们再对FQ实际操作实践过程当中

可能会出现的一些问题呢

做些讲解

如果是出现了NoRootInfoOfThisTopic的错误呢

并且咱们已经检查了启动命令

它可以加上自动创建的参数

也就是说在咱们消息发送或是消息接收的时候

指定的topic对链

即使这个topic对链没有创建呢

它会去自动创建对应的对链

也就是说这个对链呢

它会自动进行创建

那这种情况仍然出现的话呢

咱们就要去检查Locky的配置呢

是否正确

如果YAML的方式不便于配置

咱们可以通过PropBase配置进行检测

要检查Locky的配置

也就是咱们的发送端配置

还有消费端的配置

在这里呢

就是我们整个Locky的MQ

集成相关的一些配置信息

要去检查呢

所定义的对电信息

YAML这种格式呢

容易产生错乱

那么如果不便于去配置的话呢

咱们可以采用PropBase文件进行配置

这个也是一样的

或者呢

咱们可以采用PropBase

转换为YAML的一个插件

这个插件地址呢

咱们也已经提供出来

使用方法呢

是将插件下载到IDO的打解目录

并且进行解压

重启运行咱们的IDO工具

然后呢

右键选中需要转换的文件

点击Covered PropBase to YAML

这样呢

就可以实现它的自动转换

好

如果是咱们运行过程当中

出现以下错误提示

也就是PGCircle的数据源操作

存在问题的话呢

咱们就要去检查它的

Validation Query的配置属性

那咱们呢

可以看一下

在行情服务当中

也是确保在这里面的

验证查询Circle呢

要配置正确

因为不同的数据源

比如说买Circle

还有PGCircle

它们的验证查询语句的

一些语法上面呢

可能会存在一些差异

所以呢

咱们要针对于不同的数据源呢

做相应的Circle的调整

一般改成Slack1呢

这个就是通用的

但是呢

你不要写成Slack1 Plum6

这个语法呢

在PGCircle下面

是不能够支持的

所以呢

咱们也改为Slack1

好

在这里呢

就对本章内容的回顾和总结

并且对一些FAQ

常见的问题呢

做了讲解和说明

那这一讲呢

咱们就讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程讲解了如何在微服务架构中，使用 **Spring Cloud Stream** 框架集成 **RocketMQ** 消息中间件，实现行情数据的发布与订阅。核心内容包括：
- **目标**：构建一个高可用、可水平扩展的行情数据分发系统。
- **架构**：行情服务作为生产者，将数据发布到 RocketMQ 的 Topic；多个代理服务作为消费者，订阅并分发数据。
- **技术栈**：Spring Boot, Spring Cloud Stream, RocketMQ。
- **关键点**：通过配置文件定义 Topic、分组、序列化格式等；使用 `@StreamListener` 和 `@EnableBinding` 注解实现消息监听与绑定；利用 RocketMQ 的无状态设计和分组机制实现水平扩展。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取精确的时间戳，以下章节结构基于画面内容推断，按讲解顺序排列：

1.  **第3章：行情与代理服务MQ集成** (0:00)
    *   **4. 总结** (0:00) - 介绍本章目标与架构。
    *   **3. 实现** (0:00) - 详细讲解实现步骤。
        *   **3.1 行情服务与MQ集成配置** (0:00) - 讲解生产者配置。
        *   **3.2 代理服务与MQ集成配置** (0:00) - 讲解消费者配置。
        *   **3.3 行情订阅发布功能验证** (0:00) - 讲解功能验证。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **第3章：行情与代理服务MQ集成**
    *   **目标**：集成RocketMQ，由行情服务推送，通过代理服务订阅行情数据并分发至客户端。
    *   **实现**：代理服务无状态设计，支持水平扩展。
    *   **总结**：提升整体吞吐能力，部署多个代理服务在不同区域，类似CDN节点，提升数据传输速度。

#### 代码与配置

*   **3.1 行情服务与MQ集成配置**
    *   **pom.xml 依赖**：
        ```xml
        <!-- RocketMQ 消息组件依赖 -->
        <dependency>
        ```
    *   **application.yml (或 bootstrap.yml) 配置**：
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
                bindings:
                  producer:
                    group: binder-group
                    sync: true
        ```

*   **3.2 代理服务与MQ集成配置**
    *   **bootstrap-dev.yml 配置**：
        ```yaml
        spring:
          cloud:
            stream:
              bindings:
                quote:
                  consumer:
                    concurrency: 10
                    maxAttempts: 1
                    content-type: application/json
                    destination: stock-quote
                    group: stock-quote-proxy-1
              rocketmq:
                binder:
                  name-server: 10.10.20.15:9876
        ```

*   **3.3 行情订阅发布功能验证**
    *   **代理服务消费者代码 (QuoteConsumer.java)**：
        ```java
        @Service
        public class QuoteConsumer {
            @StreamListener("quote")
            public void receiveInput1(@Payload TradeStockQuoteLast receiveMsg) {
                System.out.println("receive quote: " + receiveMsg);
            }
        }
        ```
    *   **生产者代码片段**：
        ```java
        public <T> void sendObject(T msg) throws Exception {
            Message message = MessageBuilder.withPayload(msg)
                .setHeader(MessageHeaders.CONTENT_TYPE,
                    MimeTypeUtils.APPLICATION_JSON)
                .build();
            source.quoteQueue().send(message);
        }
        ```

*   **FAQ (常见问题)**
    1.  **“No route info of this topic” 错误**：
        *   检查 `autoCreateTopicEnable=true` 是否正确。
        *   如果 `yml` 不方便，可使用 IDEA 插件 `properties-to-yaml-converter` 转换。
        *   插件地址：`https://plugins.jetbrains.com/plugin/8000-properties-to-yaml-converter`
    2.  **`org.postgresql.util.PSQLException: 错误: 关系 "dual" 不存在`**：
        *   将数据源配置属性 `validationQuery` 从 `SELECT 1 FROM DUAL` 改为 `SELECT 1`。

---

### 4) 关键场景与演示描述

1.  **架构总览与目标说明** (画面1)
    *   展示了课程的总览页面，明确本章目标是实现行情与代理服务的MQ集成。
    *   通过文字总结了架构优势：无状态、水平扩展、提升吞吐量和传输速度。

2.  **生产者配置演示** (画面2-3)
    *   展示了 `application.yml` 中的配置项，包括 `destination` (主题名)、`content-type` (数据格式)、`group` (生产者组) 和 `name-server` (Broker 地址)。
    *   强调了 `sync: true` 的含义：同步发送，保证数据顺序，不能错乱。

3.  **消费者配置演示** (画面4-5)
    *   展示了 `bootstrap-dev.yml` 中的消费者配置，包括 `concurrency` (并发数)、`maxAttempts` (最大重试次数)、`group` (消费者组) 和 `name-server`。
    *   说明了 `group` 的作用：用于区分不同的消费者组，实现负载均衡。

4.  **代码实现演示** (画面6-7)
    *   展示了消费者类 `QuoteConsumer` 的代码，使用 `@StreamListener` 注解监听名为 "quote" 的队列。
    *   使用 `@Payload` 注解指定数据以 JSON 格式传输，并与服务端的发送消息体类 `TradeStockQuoteLast` 匹配。

5.  **功能验证与结果展示** (画面8-9)
    *   展示了 RocketMQ 控制台的界面，显示了名为 `stock-quote-proxy-1` 的消费者组成功订阅了 `stock-quote` 主题。
    *   通过控制台数据和代码中的 `System.out.println` 输出，验证了数据成功被消费。
    *   画面中显示了多个代理服务实例（分组）成功消费了数据，体现了水平扩展能力。

6.  **FAQ 与问题解决** (画面10-11)
    *   展示了在开发过程中可能遇到的两个常见问题及其解决方案。
    *   对于 RocketMQ 主题不存在的问题，提供了检查配置和使用 IDEA 插件转换配置文件的方法。
    *   对于 PostgreSQL 数据源验证查询错误的问题，提供了修改 `validationQuery` 的具体方案。
