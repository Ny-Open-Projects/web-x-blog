# 画面线理解：17_Spring整合RabbitMQ-生产者

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\17_Spring整合RabbitMQ-生产者_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:34, 02:00, 02:35, 03:21, 03:56, 05:05, 05:59, 07:02, 08:29, 09:30, 10:25, 12:01, 13:15, 14:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:40:28

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring 项目中整合 RabbitMQ，包括配置文件编写、交换机与队列的声明、以及生产者发送消息的测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 标题页“5. Spring 整合RabbitMQ”和子标题“5.1 Spring 整合 RabbitMQ”。
画面 2: 展示文件资源管理器，路径为“资料 (F:) > RabbitMQ 一天”，其中包含“代码”、“讲义”、“视频”、“资料”四个文件夹。
画面 3: 在 IntelliJ IDEA 中打开项目“spring-rabbitmq-producers”，展示 `pom.xml` 文件内容，包含 Spring Framework、Spring AMQP、JUnit 等依赖。
画面 4: 在 IDEA 中，将“RabbitMQ 一天”文件夹下的 `rabbitmq.properties` 文件复制到项目 `src/main/resources` 目录。
画面 5: 在 IDEA 中打开 `spring-rabbitmq-producer.xml` 文件，展示 RabbitMQ 连接工厂和队列的配置片段。
画面 6: 在 IDEA 中，继续编辑 `spring-rabbitmq-producer.xml`，添加了用于定义广播交换机和绑定队列的配置。
画面 7: 在 IDEA 中，继续编辑 `spring-rabbitmq-producer.xml`，添加了用于定义主题交换机和绑定队列的配置。
画面 8: 在 IDEA 中，打开 `ProducerTest.java` 文件，展示测试类的包名和导入的依赖。
画面 9: 在 IDEA 中，编辑 `ProducerTest.java`，添加了 `RabbitTemplate` 的注入和测试方法的框架。
画面 10: 在 IDEA 中，切换到桌面，展示多个打开的窗口，包括 RabbitMQ 管理界面、IDEA、讲义等。
画面 11: 在浏览器中打开 RabbitMQ 管理界面，显示主题交换机 `spring_topic_exchange` 及其绑定的队列。
画面 12: 在浏览器中打开 RabbitMQ 管理界面，显示所有队列列表，包括 `spring_queue`、`spring_fanout_queue_1` 等。
画面 13: 在 IDEA 中，运行测试，显示测试通过，日志中包含 RabbitMQ 的连接信息。
画面 14: 在 IDEA 中，编辑 `ProducerTest.java`，添加了测试方法 `testSendTopic`，用于发送主题消息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>5.1.7.RELEASE</version>
</dependency>

<dependency>
    <groupId>org.springframework.amqp</groupId>
    <artifactId>spring-rabbit</artifactId>
    <version>2.1.8.RELEASE</version>
</dependency>

<dependency>
    <groupId>org.junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
</dependency>

<dependency>
    <groupId>org.springframework.test</groupId>
    <artifactId>spring-test</artifactId>
    <version>5.1.7.RELEASE</version>
</dependency>

<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.8.0</version>
</plugin>
```

画面 5:
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
                               virtual-host="${rabbitmq.virtual-host}"/>
    <rabbit:admin connection-factory="connectionFactory"/>
    <rabbit:queue id="spring_queue" name="spring_queue" auto-declare="true"/>
```

画面 6:
```xml
    <rabbit:fanout-exchange id="spring_fanout_exchange" name="spring_fanout_exchange" auto-declare="true">
        <rabbit:bindings>
            <rabbit:binding queue="spring_fanout_queue_1" />
            <rabbit:binding queue="spring_fanout_queue_2" />
        </rabbit:bindings>
    </rabbit:fanout-exchange>
```

画面 7:
```xml
    <rabbit:topic-exchange id="spring_topic_exchange" name="spring_topic_exchange" auto-declare="true">
        <rabbit:bindings>
            <rabbit:binding queue="spring_topic_queue_star" pattern="heima.*" />
            <rabbit:binding queue="spring_topic_queue_well" pattern="itcast.#" />
        </rabbit:bindings>
    </rabbit:topic-exchange>
```

画面 8:
```java
package com.ithema;
import org.junit.runner.RunWith;
import org.springframework.context.annotation.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
```

画面 9:
```java
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired
