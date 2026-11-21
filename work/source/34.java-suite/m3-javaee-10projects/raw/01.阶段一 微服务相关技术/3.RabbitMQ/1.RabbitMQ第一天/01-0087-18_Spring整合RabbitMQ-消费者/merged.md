# 18_Spring整合RabbitMQ-消费者

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\18_Spring整合RabbitMQ-消费者_【海量资源尽在 ubkz.com】.mp4
- 时长 5分33秒（音频 334s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 介绍完Spring整合RubtimeQ的生产者那么接下来我们来写消费者消费者其实更加的简单因为消费者这一块呢只需要定义一个监听就可以了它定义一个类当做监听器将来消息一来就会执行这个类的回调方法就完事了非常简单那么同样的呢我们刚才导入了坐标那么下来我们来下配置文件我们把这个配置文件加进来这两个复制一下
[00:29] 然后呢我们放到resources下边放下边之后呢注意还是一样这个地方呢我们给它删掉那么删掉之后呢我们来看一下这个配置首先呢还是一样声明一个连接的工厂然后注意这里边是不是声明了很多的bin而看这个bin的坐标或者说类是不是都是我们的自己定义的这些类啊其实这些类都是我们自己定义的监听器的对象当然这个类呢还没有写所以它爆红了那么再来rabbit的listener container就是它的监听器的容器
[00:59] 那么将来呢这里边都是被称为监听器其实就是这些bin那么现在是这样我们现在呢我们来写对应的监听器非常简单我们来写这些类就行了然后呢我的监听器要去有一定的规则必须实现一个message listener接口那么要写监听器我们为了方便我们还是把这个名字保持一致这样就不用来回改了我们在这里边直接来创建一个class把这个名字一复制过来OKOK完之后呢
[01:28] implements叫做messagemessage listener就可以了然后呢去复写它的一个方法有一个on message的回调方法复写一下然后呢这个on message方法呢直接我们打印一下message它有get方法get body就是对应的数据那么为了看到效果我们就把它转成字幕串当然我们要new一下
[01:55] 你有一个字幕串然后把这个body给它包起来这样呢我们就去打印了一个消息打印消息好嘞那么这个类有了监听器有了对吧然后呢配置也有了当然这些配置下边的我们先把它注视掉要么它报错我们还没写嘛对吧把这些都注视掉我们只留一个第一个呢就是SpringQListener它监听的Q呢是这个SpringQ就是刚才我们发的最简单的那个队列
[02:26] OK吧那么这样弄完了之后呢将来我这个配置文件一旦加载了之后这个监听就会找到这个类找到这个类了之后就会执行对应的这个onMessage毁掉方法会执行打印的这句代码那么这样我们为了简单其间我们直接通过测试的方式来加载配置文件就可以了我们写个测试类thecom.it黑码黑码.
[02:55] consumer test然后呢我们只需要在这个地方呢把它软位置一下把那个配置文件加载进来就可以了spring这unit4 test runner class然后呢同样的context configuration然后这里边是locations等于class pass
[03:22] 然后呢把这个配置文件的名字给它复制一下放到这个地方其实你什么都不用干但是为了能够执行这个测试类呢我们写一个测试方法VoidTest1随便起个名都可以前边呢我们加上一个test注解只要让这个类执行一下就可以了但是呢为了让它不提因为监听器嘛将来其实这是一个web项目我们通过
[03:49] web的一个Spring的核心的监听器启动了监听器就可以加载文件但是现在呢我们为了让它不停止我们定义这样写我们写一个Borling flagflag等于true然后我们vr true一下vr true呢让这个代码永远不停止那么这时候我们写完了写完了之后呢我们来运行一下运行一下之后呢我们看能不能把这个消息取出来打印刚才是不是叫Halloween了我记得稍等一下
[04:19] 看Hello World的Spring这个是不是就取出来了这样呢我们就写完了当然还剩下这么一些类每一个写法都是一模一样的你需要写一个类然后去实现对应的一个message listener复写这个on message方法就能够把对列里边的消息取出来所以呢消费者这个代码是非常非常的简单的
[04:46] 其他的几个我就不在这个地方写了留给大家课后当成作业来完成那么简单的去小结一下消费者的代码消费者呢只需要在这个SprintPage文件里边去配置对应的bin这个bin呢就是我们的监听器类这个监听器呢要实现message的接口messageListener接口复写onMessage方法然后呢你需要在配置文件里边定义一个ListenerContainer
[05:13] 把这些监听器都引入进来并且指定这个监听器类去监听哪个队列名称就可以了所以呢这个消费者也是非常的简单的那么至此呢我们Spring整合RubtimeQ的生产者消费者我们都讲解完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spring 框架整合 RabbitMQ，演示了消费者端的配置与监听器编写过程。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程 PPT，标题为“5. Spring 整合RabbitMQ”，子标题“5.1 Spring 整合 RabbitMQ”，列出生产者和消费者的步骤。
画面 2: 在 IntelliJ IDEA 中打开 `spring-RabbitMQ-consumer.xml` 文件，显示了 RabbitMQ 连接工厂和监听器的配置，以及测试通过的提示。
画面 3: 在 `spring-RabbitMQ-consumer.xml` 文件中，高亮显示了 `<rabbit:listener-container>` 配置块，用于定义多个监听器及其绑定的队列。
画面 4: 在 IDEA 项目结构中，右键点击 `src/main/java`，选择“New” -> “Java Class”，准备创建新的监听器类。
画面 5: 在 IDEA 中打开 `SpringQueueListener.java` 文件，准备编写监听器代码。
画面 6: 在 `SpringQueueListener.java` 文件中，导入 Spring AMQP 的 `Message` 类和 `MessageListener` 接口，并开始编写类定义。
画面 7: 在 `spring-RabbitMQ-consumer.xml` 文件中，高亮显示了 `<rabbit:listener-container>` 配置块，用于定义多个监听器及其绑定的队列。
画面 8: 在 `SpringQueueListener.java` 文件中，编写了 `onMessage` 方法，用于处理接收到的消息。
画面 9: 在 IDEA 中打开 `ConsumerTest.java` 文件，准备编写测试类。
画面 10: 在 `ConsumerTest.java` 文件中，导入 `@RunWith` 和 `@ContextConfiguration` 注解，并使用 `@RunWith(SpringJUnit4ClassRunner.class)` 注解。
画面 11: 在 `ConsumerTest.java` 文件中，编写了测试方法 `@Test public void test1()`，并设置断言 `assertTrue(true)`。
画面 12: 在 IDEA 中运行 `ConsumerTest` 测试，终端显示测试通过，输出“hello world spring...”。
画面 13: 在 IDEA 项目结构中，高亮显示 `spring-RabbitMQ-consumer.xml` 文件。
画面 14: 在 `spring-RabbitMQ-consumer.xml` 文件中，高亮显示了 `<rabbit:listener-container>` 配置块，用于定义多个监听器及其绑定的队列。

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

    <context:property-placeholder location="classpath:properties/RabbitMQ.properties"/>

    <rabbit:connection-factory id="connectionFactory"
        host="${RabbitMQ.host}"
        port="${RabbitMQ.port}"
        username="${RabbitMQ.username}"
        password="${RabbitMQ.password}"
        virtual-host="${RabbitMQ.virtual_host}"/>

    <bean id="springQueueListener" class="com.ithema.RabbitMQ.listener.SpringQueueListener"/>
    <bean id="fanoutListener" class="com.ithema.RabbitMQ.listener.FanoutListener"/>
    <bean id="topicListenerStar" class="com.ithema.RabbitMQ.listener.TopicListenerStar"/>
    <bean id="topicListenerWell" class="com.ithema.RabbitMQ.listener.TopicListenerWell"/>
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
package com.ithema.RabbitMQ.listener;

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
@ContextConfiguration(locations = "classpath:spring-RabbitMQ-consumer.xml")
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

