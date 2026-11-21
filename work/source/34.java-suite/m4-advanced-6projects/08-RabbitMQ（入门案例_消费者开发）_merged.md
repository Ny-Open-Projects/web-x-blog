# 08-RabbitMQ（入门案例_消费者开发） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

咱们继续来看RabbitMQ的入门案例

刚才呢我们是已经完成了生产者的开发

并且呢我们是不是执行了这个单元测试啊

能够看到我们这个消息呢

是已经发送到我们这个堆列里面来了

对吧

好那接下来呢我们就来看啊

下一个呢就是关于我们这个消费者的开发

所谓消费者呢

他是不是就需要来监听我们这个堆列对吧

一旦呢堆列里边有消息

他就能够获取到啊

好那么消息消费者呢

我们也需要来创建一个什么呢

呃

美容工程对吧

好把这个关上

然后呢还是啊

咱们在这个demo这个工程下边来创建一个子模块

对吧

好

这个叫做MQ-consumer

好

完成

这样的话

他这个POM文件其实就不用配置了

为什么呢

因为他是不是继承了我们这个副工程

这里边这些坐标我们都已经导过了

所以这个就比较简单

简单了

然后呢

我们是不是也需要给他来提供一个配置文件

呃

这个配置文件的话呢

咱们其实从我们这个地方来考一下就可以了

复制一下

然后呢

复制到我们这个consumer里面来

因为这块呢

其实配置都是一样的

他们是不是都需要来连接我们这个MQ

所以说呢

也是啊

这段配置啊

这个是没有区别的

然后接下来呢

我们来看啊

咱们这是配置完这个application

对吧

点外描这个文件之后呢

我们就需要来编写一个什么呢

编写一个这个启动类

对吧

然后呢

编写完启动类之后呢

咱们是不是就可以来这个编写一个consumer

这个呢

就是我们的消消息处理类

其实就是一个监听器

对不对

用来监听我们堆叠消息的好

首先呢

我们先把这个启动类啊

把它创建出来

先把这个包来写一下

叫做看我们的ITK码

对吧

在这儿把这个包来写一下

对吧

在这儿把这个包来写一下

创建出来

然后呢

直接把这个类名呢

我们来考一下

具体这个类里边的内容呢

也是来复制一下

就是最普通的一个启动类啊

然后接下来下一个是不是比较关键

就是我们需要来编写一个什么呢

消息处理类

对吧

消息处理类

那么这里边呢

这个消息处理类呢

很明显也是交给Spring来管理

所以说需要加一个component注解

对吧

然后接下来呢

我们需要来提供一个方法

这个方法呢

其实叫什么名字无所谓啊

关键是什么呢

关键就是这个

RabbitListener这个注解

加了这个注解之后呢

这就表示我们当前这个方法呢

其实就是一个监听的方法

对吧

它会监听这么一个

它会监听我们这个队列

然后一旦队列里面有消息呢

它就会回调这个方法

对吧

然后具体这个消息呢

我们可以声明这么一个参数

它会通过这个参数给我们传进来

好

然后呢具体怎么用呢

好

我们用这个消息呢

我们是不是就

就是跟我们具体的这个业务逻辑相关了

咱们这个地方呢就比较简单了

直接输出一下就可以了

好

那接下来呢

我们把这个类呢来创建一下

咱们先在这来创建这么一个包啊

叫做consumer包

好

然后呢

我们在这创建这么一个myconsumer

对吧

在这呢

加一个component注解

这是我们的消息处理

哎

或者叫做消息处理类

监听什么呢

监听对列消息

好

然后咱们在这呢

是不是需要来创建一个方法

对吧

public void

这个不需要返回值

就叫receive吧

receive是不是就是接收的意思

好

然后呢

这里边来声明一个参数

message

然后呢

我们在这呢

可以来输出一句话

就说什么呢

从对列中

是不是读

读取消息

这个消息的内容呢

我们是不是可以在这来

写一下对吧

message

关键就是什么呢

需要给这个方法是不是来加一个注解

哎

加一个什么呢

叫做rabbit listener

rabbit listener

对吧

这是不是就是一个叫做监听器

对吧

哎

那么他会监听什么呢

他会监听我们对列里边的消息

那具体你监听的是哪个对列呢

注意看

我们在这里边是不是可以指定什么呢

具体的对列

你看这是不是qs

它是一个数组

那也就是说我可以同时监听什么呢

多个对列对吧

好

现在呢

咱们就监听一个对列就可以了啊

可以在这里边来指定qs等于什么呢

我们是不是在这来写一下

我想监听哪个对列呢

咱们刚才这个对列是不是叫做

呃

来看一下我这个对列名在哪呢

这个叫做myq

qs

对吧

监听这个对列

所以说呢

我们把这个对列名称

写到这

好

这样的话呢

他就会监听啊

这是监听对列消息

好

一旦这个对列里面有消息呢

他就会调用这个方法

对吧

然后呢

把消息读过来

我们在这呢

是直接输出一下就可以了

好

所以说我们作为

consumer

也就是消息的消费这一方

对吧

最主要的其实就是

就是这个类

就是这个类

好

那接下来呢

我们就来执行一下

咱们这个什么呢

来执行一下我们

这个方法对吧

启动

启动完之后呢

我们来看一下

这个方法能不能执行

能不能从对列里面来获取消息

好

我们来执行一下

其实现在对列里面是有消息的

对吧

刚才呢

我们是已经生产了一个消息

哎

你看他是不是从对列中读取消息

hello world

然后呢

我们可以来

执行一下什么呢

来执行一下我们这个producer

就是什么呢

我们再来这个呃产生一个消息

对吧

咱们再是再调用这个单元测试方法

我们再产生一个消息

啊

这样加几个碳号

对吧

哎

让他不太一样啊

然后呢

我们再来执行一下这个单元测试

再产生一个消息

产生完消息之后啊

回到我们这边来看

他能不能从对列里面再来获取消息

哎

你看他是不是又读取到了

哎

这就说明我们当前这个监听器呢

其实是已经生效了

对吧

哎

那么主要的就是

哎

在哪呢

这个my consumer

对吧

主要就是这道代码

好

那么到这儿的话呢

我们这个入门案例呢

其实就已经写完了

呃

整体来说呢

其实还是比较简单

对吧

哎

那么消息对链呢

咱们前面也都呃讲过了

应该接触了一些

只不过是以前可能接触的是rocket

或者卡不卡

对吧

这一类的啊

那么整体他的套路呢

都是类似的

都是像我们对列里面是不是来产生消息

然后呢

作为消费方呢

是不是来消费这些消息啊

整个套路其实都是一样的

只不过可能是从这个代码层面对吧

不太一样好

这是咱们这个入门案例

我们先说到这

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于 **RabbitMQ** 在 **Spring Boot** 项目中实现 **“简单模式”**（Simple Pattern）消息队列的入门教程。讲师通过 IntelliJ IDEA 开发环境，演示了如何创建消费者（Consumer）和生产者（Producer）两个模块，配置 RabbitMQ 连接，编写消息监听器和发送测试代码，并最终在控制台观察到消息被成功消费。整个过程旨在帮助初学者理解 RabbitMQ 的基本工作原理和在 Spring 生态中的集成方式。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：展示 RabbitMQ 管理后台界面，确认消息队列 `myqueue` 中存在消息，验证环境已准备就绪。
*   **00:00:05 - 00:00:15**：在 IntelliJ IDEA 中创建名为 `mq_consumer` 的新模块，选择 Maven 项目结构。
*   **00:00:15 - 00:00:25**：在 `mq_consumer` 模块中编辑 `pom.xml` 文件，配置父项目为 `rabbitmq`，并添加 `spring-boot-starter-amqp` 依赖。
*   **00:00:25 - 00:00:35**：在 `mq_consumer` 模块中创建 `application.yml` 配置文件，设置 RabbitMQ 的连接参数（`host`, `port`, `username`, `password`, `virtual-host`）。
*   **00:00:35 - 00:00:45**：编写启动类 `RabbitmqApplication`，使用 `@SpringBootApplication` 注解。
*   **00:00:45 - 00:00:55**：编写消息监听器类 `MyConsumer`，使用 `@Component` 和 `@RabbitListener` 注解监听队列 `myqueue`。
*   **00:00:55 - 00:01:05**：在 `mq_producer` 模块中编写测试类 `RabbitmqTest`，使用 `@Test` 注解的 `testSendMsg` 方法，通过 `RabbitTemplate` 发送消息。
*   **00:01:05 - 00:01:15**：运行 `RabbitmqApplication` 启动消费者服务。
*   **00:01:15 - 00:01:25**：运行 `RabbitmqTest` 测试类，发送消息 `hello world!!!`。
*   **00:01:25 - 00:01:35**：在控制台观察到消费者成功接收并打印消息，完成“简单模式”演示。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **标题**：`品达物流TMS项目`，`第10章 TMS客户端开发(pd-web-customer)`。
    *   **章节结构**：
        *   2.1 RabbitMQ介绍
        *   2.2 RabbitMQ工作原理
        *   2.3 RabbitMQ安装和启动
        *   2.4 RabbitMQ入门案例
            *   2.4.1 生产者开发
            *   2.4.2 消费者开发
            *   2.5 RabbitMQ工作模式
                *   2.5.1 简单模式 Hello World
    *   **关键文字**：`RabbitMQ提供了6种工作模式，分别为：`，并列出第一种模式 `1、简单模式 Hello World`。

*   **代码关键内容**：

    *   **`application.yml` 配置文件**：
        ```yaml
        port: 8080
        username: admin
        password: admin2020
        virtual-host: /
        ```

    *   **消费者启动类 `RabbitmqApplication.java`**：
        ```java
        @SpringBootApplication
        public class RabbitmqApplication {
            public static void main(String[] args) {
                SpringApplication.run(RabbitmqApplication.class, args);
            }
        }
        ```

    *   **消费者消息监听类 `MyConsumer.java`**：
        ```java
        @Component
        public class MyConsumer {
            @RabbitListener(queues = "myqueue")
            public void receive(String msg) {
                System.out.println("消费者接收到消息：" + msg);
            }
        }
        ```

    *   **生产者测试类 `RabbitmqTest.java`**：
        ```java
        @Test
        public void testSendMsg() {
            rabbitTemplate.convertAndSend(RabbitmqConfig.EXCHANGE,
                    RabbitmqConfig.ROUTING_KEY,
                    "hello world!!!");
        }
        ```

    *   **`pom.xml` 依赖配置**：
        ```xml
        <parent>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-parent</artifactId>
            <version>2.3.0.RELEASE</version>
        </parent>

        <artifactId>rabbitmq_consumer</artifactId>
        <groupId>com.itheima</groupId>
        <version>1.0-SNAPSHOT</version>

        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-amqp</artifactId>
            </dependency>
        </dependencies>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境验证**
    *   **描述**：讲师首先打开 RabbitMQ 管理后台（`http://66.79.7.219:15672/#/queues/%2F/myqueue`），确认 `myqueue` 队列中存在消息，证明 RabbitMQ 服务已成功安装并运行。

*   **场景二：项目结构搭建**
    *   **描述**：在 IntelliJ IDEA 中，讲师创建了 `mq_consumer` 模块，并在 `pom.xml` 中添加了 `spring-boot-starter-amqp` 依赖，为后续开发做好准备。

*   **场景三：配置文件编写**
    *   **描述**：讲师在 `application.yml` 中配置了 RabbitMQ 的连接信息，包括端口、用户名、密码和虚拟主机，这是消费者连接 RabbitMQ 的关键配置。

*   **场景四：消费者代码开发**
    *   **描述**：讲师编写了 `MyConsumer` 类，使用 `@Component` 注解将其注册为 Spring Bean，并使用 `@RabbitListener` 注解指定监听队列 `myqueue`。在 `receive` 方法中，通过 `System.out.println` 打印接收到的消息。

*   **场景五：生产者代码开发**
    *   **描述**：讲师在 `mq_producer` 模块中编写了 `RabbitmqTest` 测试类，使用 `@Test` 注解的 `testSendMsg` 方法，通过 `RabbitTemplate` 将消息 `hello world!!!` 发送到指定的交换机和路由键。

*   **场景六：运行与结果演示**
    *   **描述**：讲师先后运行消费者和生产者程序。在控制台中，可以看到消费者成功接收到消息并打印输出，验证了“简单模式”消息队列的完整工作流程。

---
