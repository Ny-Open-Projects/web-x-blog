# 22-车辆轨迹服务（pd-netty开发_HTTP接口方式 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那接下来咱们继续来看我们PD-90的开发

刚才我们开发的是http接口这种方式

我们是写到了前四步对吧

那么前面这几步都是比较简单的

那接下来我们来看下一个

下一步就是来编写这么一个类

叫做Kafka Center

这个类就是用来操作我们Kafka的

那么把它放到这个service包下边

咱们在这个品达下边再来创建一个包

就叫做service

然后在这个包下边来创建这个类

就叫做Kafka Center

然后我们写一个注释

这是用于什么呢

操作我们的Kafka

然后给这个类加一个注解

Component

然后我们接下来就可以直接在这个类里边

来注入这么一个对象

注入这么一个对象

Private

它叫做什么呢

叫做Kafka

Template

然后这里边需要指定两个范型

咱们都指定String类行了

那么我们可以看到

我通过AutoValue的

就可以直接来注入这么一个对象了

叫做Kafka Template

是不是就是一个模板

通过这个模板对象

我们这个模板里边有相应的方法

比如说有什么呢

有这个

我给你找一下

这里边方法比较多

是不是有Send

Send Default

这是Send

其实都是什么

还有这个Send

这个Send

其实都是向我们的Kafka队列当中来发送消息

对吧

来发送消息

好

那么这个地方我们需要来分析一下

为什么我在这通过一个AutoValue的

就可以直接把这个对象注进来了

这是为什么呢

首先第一步是因为我们当前在这个项目里边

它的POM文件当中已经导入了这个这个坐标

你看就是Spring-Kafka

是吧

整合的这个坐标

Spring跟我们Kafka整合的这个坐标

这是第一步

同时呢

我们是不是还在它这个配置文件里面来配置了Kafka

这段配置

那么就是基于我们这两点啊

咱们一个是导入坐标

还有一个是做了这个配置

那这样的话呢

项目在启动的时候呢

它就会把这个Kafka

他们类的对象呢

给我们实力化了

对吧

并且呢

还能够通过这个对象呢

来操作我们指定的这个

这个地址的这个Kafka队列

好

因为我们在这儿

其实配置的就是我们Kafka服务它的地址

对吧

那这样的话呢

我们就能够用这个地址的这个Kafka队列

对吧

那这样的话呢

我们就可以啊

直接注入了

因为这个对象的实力化呢

它并不需要我们来做

我们只要提供相应的配置

那么框架呢

就会帮我们给实力化出来

那这样的话呢

我们就可以直接来注入了

那么注入之后呢

我们就可以在这个项目当中来使用了

那么其实呢

我是希望啊

我们当前这个类呢

把它做成一个工具类

也就是说我们直接通过这个类名

然后调用它的一个静态方法

就可以来发送消息了

像堆类当中来发送消息

但是呢

我们当前这个对象呢

它并不是一个静态的

所以说呢

我们在这儿呢

需要来提供一个静态的Kafka template

Kafka template的对象

因为只有静态的这种实力啊

这种属性

在静态方法当中

是不是才能够使用

那这样的话呢

我是不是就需要来解决一个问题

我需要干什么呢

为这个template来复制

因为当前这个对象呢

当前这个你看我没有加AutoValue的对吧

那么这个时候呢

我们就需要把上面这个

注进来的这个复制给它

对吧

那怎么复制呢

其实非常简单

咱们只要通过一个什么呢

通过一个生命周期函数就可以了

比方说就叫NIT

但这个方法名可以任意

关键是什么呢

我们需要给它来加这么一个注解

对吧

叫做Post Construct

大家还记得这个注解吧

这个是不是当我们这个

它是生命周期的一个方法

当我们这个实力

当我们这个实力

对吧

当前这个类创建完实力之后呢

它就会执行这个方法

Post Construct

然后在这个方法里边呢

我就可以为我们这个template来复制

复制给谁呢

是不是就是这个

卡夫卡template

那这样的话呢

我们这个template它就不是空了

对吧

然后呢

我们接下来就可以来封装一个静态方法

这个静态方法呢

就是干什么呢

就是向我们这个卡夫卡队列来发送什么呢

发送消息

发送消息

public

然后void

咱们这个就叫send吧

好

当然了我们刚才提到啊

这个地方呢

我提供的是工具方法

对吧

所以说呢

我们在这呢

给它加一个static

然后呢

我们这个消息到底发送成功没成功呢

我们可以通过一个boot类型

是不是来返回

如果返回出的话呢

我就认为消息发送成功了

那么如果返回false呢

我就认为这个发送失败了

所以我们返回一个boot类型的值

然后呢

这个方法呢

是需要两个参数的

一个是什么呢

一个是topic

这其实相当于就是我们的对列名称

对吧

还有一个呢

就是发送的消息具体内容

就是message

好

然后在这里边呢

我们是不是就可以来调用什么呢

咱们这个template

刚才也看到了template里边呢

它是不是应该有一个方法叫做send

对吧

叫做send

你看

第一个呢

就是topic

第二个呢

就是我们具体的消息内容

好

然后呢

我们在这儿呢

来加一个什么呢

try catch

对吧

来加一个try catch

好

catch一个exception

然后呢

如果它进了catch呢

是不是说明发送失败了

对吧

那这个时候呢

我们就直接先来输出一下这个信息

然后呢

直接return什么呢

return false

否则的话呢

我是不是就return true啊

好

OK

那么整体这个方法写起来

其实还是非常简单的

这个呢

是topic

那么具体这个对列呢

它叫什么名字呢

这个地方呢

我们其实前面已经

嗯

在咱们这个卡夫卡服务当中啊

已经创建好了这么一个对列

名字就叫这个叫做tmsorderlocation

好

所以呢

我们把它定义成一个常量

等后边呢

在咱们的controller当中

是不是就会调用我们这个sender

来具体发送请求

对吧

来发送这个消息

到时候呢

我们就直接使用这个常量来指定什么呢

来指定我们这个对列的名称

好

这是我们这个卡夫卡

这个对列名称

这是咱们提前呢

已经创建好了

具体在哪创建的呢

刚才我们也看到了

咱们这个卡夫卡服务是不是就在这个地址

是吧

现在我们这个服务其实已经跑起来了

并且呢

我们已经创建好了这个对列

所以这个前后一定要一致啊

也就是说你发送

向这个对列来发送消息

一定要保证这个对列它是存在的

对吧

啊

那个我们提前都已经做好了

所以在这呢

咱们直接把这个对列呢

把它定义成这么一个常量就可以了

好

那么到这儿的话呢

我们这个send的方法

也是整个啊

啊

咱们这个工具类呢

其实就已经搞定了

一会儿呢

在我们的controller当中呢

直接是不是来调用它就可以了

这是我们这个卡夫卡sender的开发

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于一个名为“品达物流TMS项目”的技术课程，具体讲解了如何在 Spring Boot 项目中集成 Apache Kafka 作为消息中间件。讲师通过 IntelliJ IDEA 开发环境，演示了如何创建一个名为 `KafkaSender` 的服务类，用于通过 HTTP 接口向 Kafka 队列发送消息。核心内容包括：使用 `@Component` 和 `@Autowired` 注解管理 Bean，使用 `@PostConstruct` 注解在 Bean 初始化后进行属性赋值，以及调用 Spring Kafka 提供的 `KafkaTemplate` 类发送消息。视频中还展示了如何在 Nacos 配置中心为 Kafka 设置相关参数，以确保服务能够正常运行。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 文档中展示课程大纲，指出当前讲解的是“第7章 车辆轨迹服务开发”下的“5.1.1 HTTP接口方式”。
*   **00:00:05 - 00:00:15**: 讲师切换到 IntelliJ IDEA，打开 `KafkaSender.java` 文件，开始编写用于操作 Kafka 的服务类。
*   **00:00:15 - 00:00:30**: 讲师在 `KafkaSender` 类中定义了 `@Component` 注解，并声明了一个 `@Autowired` 的 `KafkaTemplate<String, String>` 类型的私有属性 `kafkaTemplate`。
*   **00:00:30 - 00:00:45**: 讲师添加了一个静态的 `KafkaTemplate` 属性 `template`，并使用 `@PostConstruct` 注解的 `init()` 方法，将 `kafkaTemplate` 的引用赋值给静态属性 `template`，以便在其他地方复用。
*   **00:00:45 - 00:01:00**: 讲师编写了 `send(String topic, String message)` 方法，该方法内部调用 `template.send(topic, message)` 来发送消息，并在 `try-catch` 块中处理发送失败的情况。
*   **00:01:00 - 00:01:15**: 讲师切换到 Nacos 配置中心，展示为 Kafka 服务配置的参数，包括 `bootstrap-servers`、`producer` 和 `consumer` 相关的配置。
*   **00:01:15 - 00:01:30**: 讲师回到 IDEA，对 `KafkaSender` 类进行最终检查，确认代码逻辑无误。
*   **00:01:30 - 00:01:45**: 讲师在 Typora 文档中总结，指出本节内容是“第六步：编写NettyController，通过HTTP接口方式接收机端上报的车辆位置信息”，并强调了 `KafkaSender` 的作用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`第7章 车辆轨迹服务开发` -> `5.1.1 HTTP接口方式`。
    *   课程目标：`第六步：编写NettyController，通过HTTP接口方式接收机端上报的车辆位置信息`。
*   **代码关键内容**:
    *   **`KafkaSender.java` 类定义**:
        ```java
        @Component
        @Slf4j
        public class KafkaSender {
            @Autowired
            private KafkaTemplate<String, String> kafkaTemplate;
            private static KafkaTemplate<String, String> template;
        
            @PostConstruct
            public void init() {
                template = kafkaTemplate;
            }
        
            public static boolean send(String topic, String message) {
                try {
                    template.send(topic, message);
                    log.info("消息发送成功：{}, {}", topic, message);
                } catch (Exception e) {
                    log.error("消息发送失败：{}, {}", topic, message, e);
                    return false;
                }
                return true;
            }
        }
        ```
    *   **`KafkaTemplate` 类的结构**:
        ```java
        public class KafkaTemplate<K, V> implements KafkaOperations<K, V> {
            private final LogAccessor logger;
            private final ProducerFactory<K, V> producerFactory;
            private final boolean autoFlush;
            private final boolean transactional;
            private final ThreadLocal<Producer<K, V>> producers;
            private volatile String defaultTopic;
            private volatile ProducerListener<K, V> producerListener;
            private String transactionIdPrefix;
            private Duration closeTimeout;
        }
        ```
    *   **Nacos 配置内容**:
        ```yaml
        kafka:
          bootstrap-servers: 68.79.7.219:9092
          listener: # 指定listener 容器中并线程数，用于提高并发量
          producer:
            concurrency: 5
            retries: 3
            batch-size: 10000
            buffer-memory: 33554432
            key-serializer: org.apache.kafka.common.serialization.StringSerializer
            value-serializer: org.apache.kafka.common.serialization.StringSerializer
          consumer:
            group-id: pdtruck
            port: 1000
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建 Kafka 发送服务类**
    *   **描述**: 讲师在 IntelliJ IDEA 中创建并编辑 `KafkaSender.java` 文件。他首先添加了 `@Component` 注解，然后声明了一个 `@Autowired` 的 `KafkaTemplate<String, String>` 类型的私有属性 `kafkaTemplate`。接着，他添加了一个静态的 `KafkaTemplate` 属性 `template`，并使用 `@PostConstruct` 注解的 `init()` 方法，将 `kafkaTemplate` 的引用赋值给 `template`。
*   **场景二：编写消息发送方法**
    *   **描述**: 讲师编写了 `send(String topic, String message)` 方法。该方法内部调用 `template.send(topic, message)` 来发送消息。在 `try-catch` 块中，他添加了日志记录，用于记录消息发送的成功或失败情况。
*   **场景三：配置 Kafka 参数**
    *   **描述**: 讲师切换到 Nacos 配置中心，展示为 Kafka 服务配置的参数。他详细解释了 `bootstrap-servers`、`producer` 和 `consumer` 相关的配置项，如 `concurrency`、`batch-size`、`buffer-memory` 等，以确保 Kafka 服务能够正常运行。
*   **场景四：代码逻辑验证**
    *   **描述**: 讲师在 IDEA 中对 `KafkaSender` 类进行最终检查，确认代码逻辑无误。他强调了 `@PostConstruct` 注解的作用，即在 Bean 初始化后执行 `init()` 方法，从而确保 `template` 属性在使用前已被正确赋值。
