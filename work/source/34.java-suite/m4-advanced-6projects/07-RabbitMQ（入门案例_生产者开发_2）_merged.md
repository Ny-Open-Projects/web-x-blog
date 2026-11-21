# 07-RabbitMQ（入门案例_生产者开发_2） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 刚才呢

咱们这个入门案例当中的这个producer

也就是消息的生产者代码

我们是不是已经开发完了

整体呢

其实还是比较简单的

对吧

一个是导入相应的这个坐标

对吧

主要就看着这个

Springboard Starter AMQP

然后导入这个坐标之后呢

接下来就是我们这个配置文件

对吧

需要来进行配置

就是关于我们MQ的这些配置

配置好了之后呢

咱们是不是又提供了一个配置类

在配置类里边

主要就是创建三个对象

对吧

一个就是什么

交换机对象

还有一个是对链

还有一个呢

就是进行绑定的这个对象

就是将我们的对链

跟交换机进行绑定

然后呢

我们是不是就编写这个单元测试

对吧

在这个地方

我们直接注入了一个

template的对象

通过它呢

就可以将我们指定的这个消息

把它发送到我们相应的交换机里面去

好

接下来呢

我们来测试一下

直接来运行一下

刚才我们在运行的时候呢

是这个环境有点问题啊

但是这次在运行

你看就没有问题了

好

应该是这个idea工具呢

刚才出了点问题

其实我并没有去调整它

我们再次运行

你看它就是能够运行通过

好

那么运行成功之后呢

我们怎么确定

这个消息有没有发送成功呢

最简单的就是

我们可以到这来看

对吧

到这个页面上来看一下

刷新一下

你看

它这是不是就有一个

叫做myq2

对吧

这就是我们这个对链

就已经出来了

然后呢

我们点击它这个名字

好

然后呢

在这儿来看啊

这个对链里边的消息有没有呢

注意看

怎么看呢

在这儿是不是有个叫做get message

这就是获得消息

对吧

获得消息

点击它

它就展开了

从这儿能看到hello world

对吧

这就是我们这个对链里边的

具体的消息的内容

所以从这儿呢

能够看到啊

然后它跟哪个交换机绑定呢

从这儿也能看到myexchange2

对吧

好

这就是我们验证了一下

咱们执行完

好

这就是我们这个单元测试方法之后

没有报错

然后呢

我们想看看那个消息

到底有没有发送成功

对吧

可以通过它这个控制台

能够看到

好

现在呢

它其实还没有消费

因为什么呢

因为我们现在这个消费者

这一段还没有开发呢

那就相当于我们这个消息呢

现在是积压在了我这个对链里面

还没有去消费

那么一会儿呢

我们就可以来编写什么呢

编写一个消费段

然后呢

来消费这个消息

好

这是关于我们这个

生产者

生产消息

我们做这个单元测试

是没有问题的

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析：

---

### 1) 视频摘要

本视频演示了一个基于 Spring Boot 的 RabbitMQ 生产者（Producer）的完整开发与测试流程。讲师通过 IntelliJ IDEA 开发环境，逐步展示了如何配置项目、定义交换机（Exchange）、队列（Queue）及其绑定关系，然后编写并运行一个测试用例，最终通过 RabbitMQ 管理后台验证消息已成功发送并被消费。整个过程旨在教学如何使用 Spring AMQP 模块（特别是 `RabbitTemplate`）来实现消息的发送。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 展示项目结构，定位到 `pom.xml` 文件，确认项目依赖。
*   **00:05 - 00:10**: 展示 `application.yml` 文件，配置 RabbitMQ 服务器的连接信息（host, port, username, password, virtual-host）。
*   **00:10 - 00:15**: 展示 `RabbitmqConfig.java` 文件，定义交换机、队列和绑定关系的配置。
*   **00:15 - 00:20**: 展示 `RabbitmqTest.java` 文件，编写测试用例，使用 `RabbitTemplate` 发送消息。
*   **00:20 - 00:25**: 在 IntelliJ IDEA 的终端中运行测试用例。
*   **00:25 - 00:30**: 在 RabbitMQ 管理后台查看消息是否成功被接收。
*   **00:30 - 00:35**: 回到代码，对测试用例进行调试或修改。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**:
    *   无直接 PPT 或图表展示，主要通过 IDE 界面和浏览器窗口展示内容。
*   **公式**:
    *   无数学公式。
*   **代码**:
    *   **`pom.xml`** (Maven 依赖配置):
        ```xml
        <parent>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-parent</artifactId>
            <version>2.2.5.RELEASE</version>
        </parent>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-amqp</artifactId>
            </dependency>
        </dependencies>
        ```
    *   **`application.yml`** (RabbitMQ 配置):
        ```yaml
        spring:
          rabbitmq:
            host: 68.79.7.219
            port: 5672
            username: admin
            password: admin@2020
            virtual-host: /
        ```
    *   **`RabbitmqConfig.java`** (Spring 配置类):
        ```java
        @Configuration
        public class RabbitmqConfig {

            // 交换机
            @Bean
            public DirectExchange exchange() {
                return ExchangeBuilder.directExchange(EXCHANGE).durable(true).build();
            }

            // 队列
            @Bean
            public Queue queue() {
                return new Queue(QUEUE);
            }

            // 将队列和交换机绑定
            @Bean
            public Binding binding(@Qualifier(QUEUE) Queue queue, @Qualifier(EXCHANGE) DirectExchange exchange) {
                return BindingBuilder.bind(queue).to(exchange).with(ROUTING_KEY);
            }
        }
        ```
    *   **`RabbitmqTest.java`** (测试类):
        ```java
        @RunWith(SpringRunner.class)
        @SpringBootTest
        public class RabbitmqTest {

            @Autowired
            RabbitTemplate rabbitTemplate;

            @Test
            public void testSendMsg() {
                rabbitTemplate.convertAndSend(RabbitmqConfig.EXCHANGE,
                        RabbitmqConfig.ROUTING_KEY,
                        "hello world");
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖配置**
    *   讲师在 IntelliJ IDEA 中打开项目 `rabbitmq_demo`，首先查看 `pom.xml` 文件，确认项目已引入 `spring-boot-starter-amqp` 依赖，这是实现 RabbitMQ 功能的基础。
*   **场景二：RabbitMQ 服务器配置**
    *   讲师切换到 `application.yml` 文件，配置了连接到本地 RabbitMQ 服务器的详细信息，包括 IP 地址、端口、用户名和密码。
*   **场景三：Spring 配置类编写**
    *   讲师在 `RabbitmqConfig.java` 中定义了三个核心 Bean：
        1.  一个名为 `EXCHANGE` 的 `DirectExchange`。
        2.  一个名为 `QUEUE` 的 `Queue`。
        3.  一个将上述队列和交换机绑定的 `Binding`。
    *   这部分代码定义了消息的路由规则。
*   **场景四：编写并运行测试用例**
    *   讲师在 `RabbitmqTest.java` 中编写了一个 `@Test` 方法 `testSendMsg`。
    *   该方法通过 `@Autowired` 注入 `RabbitTemplate`，并调用其 `convertAndSend` 方法，将字符串 `"hello world"` 发送到之前配置的交换机和路由键。
    *   讲师点击运行按钮，IDE 的终端输出显示测试成功通过。
*   **场景五：验证消息发送**
    *   讲师切换到浏览器，打开 RabbitMQ 管理后台（`http://68.79.7.219:15672`）。
    *   在 `Queues` 标签页中，找到名为 `myqueue2` 的队列。
    *   点击 `Get message(s)` 按钮，成功获取到消息，消息内容为 `"hello world"`，并显示其路由键和属性。
    *   这证明了消息已成功从生产者发送到 RabbitMQ 服务器，并被正确路由到目标队列。

---
