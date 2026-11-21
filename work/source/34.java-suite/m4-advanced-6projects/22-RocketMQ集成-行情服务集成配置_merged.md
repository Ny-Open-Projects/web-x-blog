# 22-RocketMQ集成-行情服务集成配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着讲解行情服务和LockitMQ的集成配置。

首先咱们来看一下行情服务和代理服务的交互处理流程。

行情服务将行情的报价数据从MQ的消息队列当中发布到所有的代理服务里面。

代理服务是怎么获取呢?

它是从MQ当中去订阅获取对应的行情消息。

每个代理服务采用的是统一的消息队列,同一个Copy格,通过不同的分组来区分,保障每个代理服务都能获取到相同的行情数据。

这个是什么意思呢?咱们来画一下。

这个比如说是行情服务,下面就有很多的代理服务节点,这个是2号代理服务节点,可以实现它的水平扩充。

以此类推。

那么行情和代理服务并非直接进行数据的交互。

在这里它是通过LockitMQ消息队列。

那么行情服务将它加工订阅的行情数据通过LockitMQ进行转发处理。

然后下面这些代理服务节点,它们就从LockitMQ当中订阅对应的行情数据。

它们订阅的都是同一个Topic。

但是,

每个代理服务它们都要拿到实时完整的行情数据。

对不对?

所以它们在这里会有不同的Group进行标识。

比如说代理服务1节点它是Group1,代理服务2节点它是Group2。

这里面一词一推,GroupN。

这样就能够保障这些代理服务都能够接收到完整的行情数据。

如果在这里它推送了一条股票行情报价。

这些代理服务订阅的都是同一个Topic,不同的分组。

它们都能够接收到这条行情报价数据。

好,这个就是行情和代理服务的交互处理流程。

那咱们就来做具体的配置。

先将依赖copy到工程当中。

将它放到行情服务里面。

找到咱们的行情服务。

放在POM文件下面。

让这个窗口最小化。

这个是放在Dependency上。

在Dependency标签里面。

保留生效。

这个组件咱们可以看到它通过start实现了自动化配置。

接下来咱们就来实现它的配置文件。

配置文件咱们来具体看一下它是如何去实现配置呢。

在这里它定义了一项名为Quart的配置。

它的对列名称是为stockQuart。

也在这里面定义了stockQuart。

这个呢也就是Topic。

数据内容呢,

是通过json方式进行了传递。

咱们可以看到这个是json格式。

name是我这个是LockitMQ的服务地址和端口。

之前咱们在搭建LockitMQ的时候呢也已经做了讲解。

然后大家要注意一下。

在这里面呢有一个sync的标识。

这个sync咱们是设为chew。

它的意思呢是采用同步方式进行发送。

行情报价呢对顺序是有要求的。

这个不能错乱。

所以呢必须要保持它的一个顺序。

一个同步有序的状态。

咱们可以看到这个层级会有点多。

对不对。

配置的时候呢要注意一下。

千万不要层级搞错了。

否则呢这个调用的时候会出现各种问题。

那如果担心编写配置出现错乱的情况。

那该怎么办呢。

咱们可以先将它写成properties配置格式。

再通过idea的一个插件。

可以呢将properties的文件呢转换为yaml的格式。

这个插件使用也比较简单。

将插件。

下载到idea的plugin目录下面。

进行解压。

然后重启运行。

右键选中文件。

点击covered properties to yaml。

就可以了实现它的转换。

在这里咱们就不做赘述。

大家有兴趣呢可以自行研究和实现。

咱们在这里呢要掌握好LockitMQ的无端的配置。

那回到代码当中。

咱们看一下配置文件。

在这里呢已经做了实现。

这个和讲义当中呢是一样的。

配置了它的内幕生活的。

LockitMQ无端的地址。

然后咱们订阅的消息对链。

以及呢消息的消费方式。

采用同步方式保持呢消息消费的有序性。

好那咱们再回到讲义当中。

这里消息发送方式呢是采用同步的方式。

保证呢消息发送的有序性。

好那咱们再回到讲义当中。

接着咱们就要实现MQ消息的发送功能。

咱们将消息发送呢做一个封装。

好。

咱们回到代码当中。

做个具体实现。

在MQ的包下面咱们创建一个内。

这个内呢就叫port。

专门用于行情服务消息的发送。

它是一个service。

咱们要将它的注解加上。

然后这里呢要注入消息对链。

这Qsource呢咱们还没实现。

咱们要先将它推置一下。

在这里面咱们新建一个内。

这是LockitMQ.

Aduce.

Configuration。

这里面是要定义LockitMQ的消息对链配置。

Configuration注解要加入进去。

然后这里呢我们要做一个绑定。

它要绑定一个消息通道。

咱们先做一个配置。

Interface.

Qsource。

然后再给它定义一个messageChannel。

专门用于行情消息对链的处理。

然后我们要通过注解做一个绑定。

好的port。

这个绑定配置上呢,

对应的就是咱们在工程配置文件当中。

在这里所定义的port的配置信息。

好。

然后在绑定里面呢去指向刚才的消息通道。

Qsource.

Cast。

那咱们再回到刚才消息发送的封装处理。

在这里呢就可以使用刚才所定义的Qsource。

然后将它注入进来。

这个是用于消息发送的通道。

然后咱们去实现消息封装的方法。

这里呢,

采用一个func.

send.

object。

这个消息类型呢,

咱们并不清楚,

就采用func。

然后呢,

tag。

通过func呢,

它就能够支持更多消息类型的发送。

tag呢,

咱们之前讲LokiLMQ术语的时候呢,

也做了介绍。

这个是在topic的基础上面呢,

再做一层消息的标记和分类。

这样呢,

可以便于消息的处理。

那咱们看一下,

消息该如何去发送呢?

通过message build。

咱们在这里呢,

导入进来。

这个呢,

是sprint.flimwork下面的。

这个方法没有出来,

它是这个内容导入错误。

这个导入成myserve下面的。

这个有错误。

咱们重新导入一下。

这个是sprint.flimwork下面的包。

大家要注意一下。

然后要去设置呢,

它的头部信息。

头部里面呢,

就存放刚才所传递的tag信息。

constant。

property。

tag。

下面呢,

再设置一个头部信息。

就是咱们消息发送的类型。

咱们是采用json的格式。

这里呢,

大家可以采用不同的格式。

并非一定要采用json。

采用二进制序列化。

流逝方式等等都是可以的。

不管你是怎样的业务数据。

最后的话呢,

它都会包装为一个message。

然后呢,

进行发送。

source.wordq。

拿到消息堆叠。

然后进行发送。

这个方法呢,

就已经封装完成。

咱们加上对应的注射。

它是发送对象消息。

附带tag标记信息。

这里面是一个范型。

可以支持不同的对象。

有了tag标记的发送方法。

咱们还可以再封装一个,

没有附带tag标记的发送方法。

做一个方法的重展。

那么在这里呢,

就不需要tag的头部标记。

咱们加上注射。

这个意思呢,

是直接发送对象消息。

好,咱们回到讲义当中。

在这里呢,

咱们就实现了行情服务和mq的集成配置。

咱们注意一下,

这里的发送方法,

咱们做了两个封装。

一个呢,

是封装了带tag的发送方法。

另外呢,

是不带tag的发送接口。

如果咱们发送消息的时候呢,

是指定了tag。

那么对于指定了tag的消费端,

其他tag的消息呢,

它就不会再进行接收。

这点大家要理解清楚。

那针对于咱们的业务场景,

行情数据呢,

可以不需要带tag。

咱们呢,

就可以采用直接发送对象消息的接口,

进行消息的发送。

最后,

还有一项重要的配置,

就是要绑定它的autopull。

这个在刚才代码的实验过程当中呢,

也做了讲解。

就是咱们配置了LockitMQ,

比如ducer,configuration,

在这里面做的实现。

大家注意一下这个名称呢,

要和配置文件当中所定义的名称,

要保持一致。

否则的话呢,

它找不到对应的配置信息。

接着的话呢,

就是要开启EnableBinding这个珠线。

能够让它绑定Qsrc这个接口。

那整个LockitMQ消息发送的实现呢,

就比较简单。

底层的话呢,

我们的视频都帮咱们做了更进一步的封装。

咱们可以看到,

它在这里提供了很多的接口。

咱们就不用去关心了,

底层这块发送的处理逻辑。

在这里就是实现了对行情服务

和LockitMQ的集成配置。

那这一讲呢,

咱们就先讲到这里。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个基于 Spring Cloud Stream 的微服务架构项目，重点讲解如何将行情服务（Quote Service）与 RocketMQ 消息队列集成。核心目标是让行情服务能够将行情报价数据发布到消息队列中，然后由多个代理服务（Proxy Services）订阅并消费这些数据。视频主要演示了行情服务端的配置步骤，包括在 `pom.xml` 中添加依赖、在 `bootstrap-dev.yml` 配置文件中定义 RocketMQ 的连接参数和消息队列（Topic）配置，以及在 Java 代码中如何使用 `@EnableBinding` 注解和 `QueueSource` 接口来发送带标签的消息。视频还提及了配置文件的层级结构和潜在的配置错误风险。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开始，展示课程大纲，定位到“3. 实现”章节下的“3.1 行情服务与MQ集成配置”。
*   **00:00:05 - 00:00:15**: 展示 `pom.xml` 文件，讲解需要添加的 Spring Cloud Stream RocketMQ 依赖。
*   **00:00:15 - 00:00:30**: 展示 `bootstrap-dev.yml` 配置文件，讲解如何配置 RocketMQ 的 `name-server` 地址、消息队列名称（`destination`）和生产者分组（`group`）。
*   **00:00:30 - 00:00:45**: 讲解配置文件中 `sync: true` 的含义，即同步发送，保证消息顺序。
*   **00:00:45 - 00:01:00**: 讲解配置文件的层级结构，并提示配置错误可能导致的问题，推荐使用 IDEA 插件将 `properties` 格式转换为 `yaml` 格式。
*   **00:01:00 - 00:01:15**: 切换到 IntelliJ IDEA，展示 `QuoteSender.java` 文件，准备编写发送消息的代码。
*   **00:01:15 - 00:01:30**: 展示 `RocketMqProduceConfiguration.java` 文件，讲解如何使用 `@EnableBinding` 注解和 `@Configuration` 注解来定义消息生产者。
*   **00:01:30 - 00:01:45**: 在 `QuoteSender.java` 中，使用 `@Service` 注解，并引入 `QueueSource` 接口。
*   **00:01:45 - 00:02:00**: 在 `QuoteSender.java` 中，使用 `@Autowired` 注解注入 `QueueSource`。
*   **00:02:00 - 00:02:15**: 在 `QuoteSender.java` 中，编写 `sendObject` 方法，使用 `MessageBuilder` 构建消息，并设置消息头（`PROPERTY_TAGS` 和 `CONTENT_TYPE`）。
*   **00:02:15 - 00:02:30**: 在 `QuoteSender.java` 中，调用 `source.quoteQueue().send(message)` 发送消息。
*   **00:02:30 - 00:02:45**: 展示 `bootstrap-dev.yml` 配置文件，讲解 `Output` 注解的含义，即绑定 `QueueSource` 接口。
*   **00:02:45 - 00:03:00**: 切换到“3.2 代理服务与MQ集成配置”章节，准备讲解代理服务的配置。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3. 实现”、“3.1 行情服务与MQ集成配置”、“3.2 代理服务与MQ集成配置”。
    *   **核心概念**: “行情服务将行情报价数据从MQ消息队列中发布至所有代理服务，代理服务从MQ订阅获取消息。”、“每个代理服务采用统一的消息队列（同一个TOPIC），不同的分组，保障每个代理服务都能获取到相同的行情数据。”、“这里通过Spring cloud stream 方式来集成使用RocketMQ。”
    *   **配置说明**: “定义了一名为quote的配置，队列名称为stock-quote，数据内容通过json传递，name-server为服务器地址和端口。sync采用同步方式发送，行情报价对顺序是有要求，不能错乱。”

*   **代码关键内容**:
    *   **Maven 依赖 (pom.xml)**:
        ```xml
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-stream-rocketmq</artifactId>
        </dependency>
        ```
    *   **配置文件 (bootstrap-dev.yml)**:
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
                  quote:
                    producer:
                      group: binder-group
                      sync: true
        ```
    *   **Java 代码 (RocketMqProduceConfiguration.java)**:
        ```java
        @Configuration
        @EnableBinding
        public class RocketMqProduceConfiguration {
        }
        ```
    *   **Java 代码 (QuoteSender.java)**:
        ```java
        @Service
        public class QuoteSender {
            @Autowired
            private QueueSource source;
            
            public void sendObject(Object msg, String tag) throws Exception {
                Message message = MessageBuilder.withPayload(msg)
                    .setHeader(MessageConst.PROPERTY_TAGS, tag)
                    .setHeader(MessageConst.CONTENT_TYPE, "application/json");
                source.quoteQueue().send(message);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：配置文件讲解 (00:00:05 - 00:00:30)**:
    *   讲师在 PPT 上展示 `bootstrap-dev.yml` 文件的配置内容。
    *   重点讲解 `spring.cloud.stream.bindings.quote.destination: stock-quote`，说明这是消息队列的名称。
    *   讲解 `spring.cloud.stream.rocketmq.binder.name-server`，说明这是 RocketMQ 服务的地址。
    *   讲解 `spring.cloud.stream.rocketmq.bindings.quote.producer.group`，说明这是生产者分组，用于区分不同的代理服务。
    *   讲解 `spring.cloud.stream.rocketmq.bindings.quote.producer.sync: true`，说明这是同步发送，保证消息顺序。

*   **场景二：代码编写与注解 (00:01:15 - 00:02:30)**:
    *   讲师在 IntelliJ IDEA 中打开 `QuoteSender.java` 文件。
    *   在 `@Service` 注解下，使用 `@Autowired` 注解注入 `QueueSource` 接口。
    *   在 `sendObject` 方法中，使用 `MessageBuilder` 构建消息，并设置 `PROPERTY_TAGS` 和 `CONTENT_TYPE` 消息头。
    *   最后，调用 `source.quoteQueue().send(message)` 发送消息。

*   **场景三：配置绑定 (00:02:30 - 00:02:45)**:
    *   讲师在 PPT 上展示 `bootstrap-dev.yml` 文件的 `Output` 配置。
    *   解释 `Output` 注解的含义，即绑定 `QueueSource` 接口。
    *   说明 `Output` 的值 `quote` 必须与配置文件中的 `destination` 值一致。

*   **场景四：章节过渡 (00:02:45 - 00:03:00)**:
    *   讲师在 PPT 上切换到“3.2 代理服务与MQ集成配置”章节。
    *   预告接下来将讲解代理服务如何订阅消息队列。

---
