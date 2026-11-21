# 画面线理解：18_Spring整合RabbitMQ-消费者

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\18_Spring整合RabbitMQ-消费者_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:32, 01:01, 01:15, 01:26, 01:44, 02:14, 02:35, 03:02, 03:14, 04:01, 04:29, 04:56, 05:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:41:03

1) 这一组画面整体在讲如何使用 Spring 框架整合 RabbitMQ，演示了消费者端的配置与监听器编写过程。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程 PPT，标题为“5. Spring 整合RabbitMQ”，子标题“5.1 Spring 整合 RabbitMQ”，列出生产者和消费者的步骤。
画面 2: 在 IntelliJ IDEA 中打开 `spring-rabbitmq-consumer.xml` 文件，显示了 RabbitMQ 连接工厂和监听器的配置，以及测试通过的提示。
画面 3: 在 `spring-rabbitmq-consumer.xml` 文件中，高亮显示了 `<rabbit:listener-container>` 配置块，用于定义多个监听器及其绑定的队列。
画面 4: 在 IDEA 项目结构中，右键点击 `src/main/java`，选择“New” -> “Java Class”，准备创建新的监听器类。
画面 5: 在 IDEA 中打开 `SpringQueueListener.java` 文件，准备编写监听器代码。
画面 6: 在 `SpringQueueListener.java` 文件中，导入 Spring AMQP 的 `Message` 类和 `MessageListener` 接口，并开始编写类定义。
画面 7: 在 `spring-rabbitmq-consumer.xml` 文件中，高亮显示了 `<rabbit:listener-container>` 配置块，用于定义多个监听器及其绑定的队列。
画面 8: 在 `SpringQueueListener.java` 文件中，编写了 `onMessage` 方法，用于处理接收到的消息。
画面 9: 在 IDEA 中打开 `ConsumerTest.java` 文件，准备编写测试类。
画面 10: 在 `ConsumerTest.java` 文件中，导入 `@RunWith` 和 `@ContextConfiguration` 注解，并使用 `@RunWith(SpringJUnit4ClassRunner.class)` 注解。
画面 11: 在 `ConsumerTest.java` 文件中，编写了测试方法 `@Test public void test1()`，并设置断言 `assertTrue(true)`。
画面 12: 在 IDEA 中运行 `ConsumerTest` 测试，终端显示测试通过，输出“hello world spring...”。
画面 13: 在 IDEA 项目结构中，高亮显示 `spring-rabbitmq-consumer.xml` 文件。
画面 14: 在 `spring-rabbitmq-consumer.xml` 文件中，高亮显示了 `<rabbit:listener-container>` 配置块，用于定义多个监听器及其绑定的队列。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 2:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:rabbit="http://www.springframework.org/schema/rabbit"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context.xsd
        http://www.springframework.org/schema/rabbit
        http://www.springframework.org/schema/rabbit/spring-rabbit.xsd">

    <context:property-placeholder location="classpath:properties/rabbitmq.properties"/>

    <rabbit:connection-factory id="connectionFactory"
        host="${rabbitmq.host}"
        port="${rabbitmq.port}"
        username="${rabbitmq.username}"
        password="${rabbitmq.password}"
        virtual-host="${rabbitmq.virtual_host}"/>

    <bean id="springQueueListener" class="com.ithema.rabbitmq.listener.SpringQueueListener"/>
    <bean id="fanoutListener" class="com.ithema.rabbitmq.listener.FanoutListener"/>
    <bean id="topicListenerStar" class="com.ithema.rabbitmq.listener.TopicListenerStar"/>
    <bean id="topicListenerWell" class="com.ithema.rabbitmq.listener.TopicListenerWell"/>
</beans>
```

画面 3:
```xml
<rabbit:listener-container connection-factory="connectionFactory" auto-declare="true">
    <rabbit:listener ref="springQueueListener" queue-names="spring_queue"/>
    <rabbit:listener ref="fanoutListener" queue-names="spring_fanout_queue_1"/>
    <rabbit:listener ref="fanoutListener2" queue-names="spring_fanout_queue_2"/>
    <rabbit:listener ref="topicListenerStar" queue-names="spring_topic_queue_star"/>
    <rabbit:listener ref="topicListenerWell" queue-names="spring_topic_queue_well"/>
</rabbit:listener-container>
```

画面 6:
```java
package com.ithema.rabbitmq.listener;

import org.springframework.amqp.core.Message;
import org.springframework.amqp.core.MessageListener;

public class SpringQueueListener implements MessageListener {
    @Override
    public void onMessage(Message message) {
        System.out.println(new String(message.getBody()));
    }
}
```

画面 10:
```java
import org.junit.runner.RunWith;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = "classpath:spring-rabbitmq-consumer.xml")
public class ConsumerTest {
```

画面 11:
```java
@Test
public void test1(){
    boolean flag = true;
    assertTrue(flag);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: PPT 标题为“5. Spring 整合RabbitMQ”，子标题“5.1 Spring 整合 RabbitMQ”，列出生产者和消费者的步骤。

5) 不要评价画面美观，不要输出与课程无关的内容。
