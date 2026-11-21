# 画面线理解：02_高级特性-消息可靠投递-confirm

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\02_高级特性-消息可靠投递-confirm_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 03:01, 03:32, 04:13, 05:06, 05:41, 06:28, 07:27, 07:46, 08:32, 08:45, 09:01, 10:59, 12:08, 13:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:45:19

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 RabbitMQ 的 confirm 确认模式来实现消息的可靠投递。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 标题“1.1 消息的可靠投递”，介绍 RabbitMQ 提供的 confirm 和 return 两种可靠性投递模式，并说明消息投递路径。
画面 2: 展示 IntelliJ IDEA 中的 `spring-rabbitmq-producer.xml` 配置文件，定义了 `rabbit.connection-factory` 和 `rabbit.template`。
画面 3: 展示 `spring-rabbitmq-producer.xml` 中定义了 `rabbit:queue` 元素。
画面 4: 展示 RabbitMQ 管理后台的 Exchanges 页面，列出多个交换机。
画面 5: 展示 `ProducerTest.java` 文件，定义了测试类 `ProducerTest`，并使用 `@RunWith(SpringJUnit4ClassRunner.class)` 和 `@ContextConfiguration` 注解。
画面 6: 展示 `spring-rabbitmq-producer.xml` 中定义了 `rabbit:direct-exchange` 和 `rabbit:binding`。
画面 7: 展示 `ProducerTest.java` 中的 `testConfirm` 方法，准备设置确认回调。
画面 8: 展示 `ProducerTest.java` 中为 `rabbitTemplate` 设置 `ConfirmCallback` 的代码。
画面 9: 展示 `ProducerTest.java` 中调用 `rabbitTemplate.convertAndSend` 发送消息的代码。
画面 10: 展示 RabbitMQ 管理后台的 Exchanges 页面，与画面 4 相同。
画面 11: 展示测试运行结果，显示测试通过，并在控制台输出“confirm方法被执行了...”。
画面 12: 展示 `ProducerTest.java` 中为 `ConfirmCallback` 方法添加了 `if (ack)` 判断逻辑。
画面 13: 展示 `ProducerTest.java` 中在 `else` 分支中添加了打印失败消息的代码，并准备发送一个失败的消息。
画面 14: 展示 `ProducerTest.java` 中修改了 `convertAndSend` 的参数，使消息发送失败，并在控制台输出“接收失败消息”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
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
    <context:property-placeholder location="classpath:rabbitmq.properties"/>
    <rabbit:connection-factory id="connectionFactory"
        host="172.16.98.133"
        port="5672"
        username="guest"
        password="guest"
        virtual-host="//"/>
    <!--定义RabbitMQ连接工厂，从别为-->
    <rabbit:admin connection-factory="connectionFactory"/>
    <rabbit:template id="rabbitTemplate" connection-factory="connectionFactory"/>
</beans>
```

画面 3:
```xml
<rabbit:queue id="test_queue" />
```

画面 6:
```xml
<rabbit:direct-exchange name="test_exchange_confirm">
    <rabbit:binding queue="test_queue_confirm" key="confirm"/>
</rabbit:direct-exchange>
```

画面 5:
```java
package com.ithema.test;

import org.junit.runner.RunWith;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = "classpath:spring-rabbitmq-producer.xml")
public class ProducerTest {

}
```

画面 7:
```java
public void testConfirm() {
    //1. 确认模式开启：ConnectionFactory中开启publisher-confirms="true"
    //2. 在RabbitTemplate中定义confirmCallback回调函数
}
```

画面 8:
```java
rabbitTemplate.setConfirmCallback(new RabbitTemplate.ConfirmCallback() {
    @Override
    public void confirm(CorrelationData correlationData, boolean ack, String cause) {
        System.out.println("confirm方法被执行了....");
    }
});
```

画面 9:
```java
rabbitTemplate.convertAndSend("test_exchange_confirm", "confirm", "message confirm.");
```

画面 12:
```java
if (ack) {
    //接收成功
} else {
    //接收失败
}
```

画面 13:
```java
rabbitTemplate.convertAndSend("test_exchange_confirm11", "confirm", "message confirm.");
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1. RabbitMQ 高级特性”，子标题“1.1 消息的可靠投递”，内容包括：
- 消息投递路径：producer ---> rabbitmq broker ---> exchange ---> queue ---> consumer
- 两种可靠性投递模式：confirm 确认模式、return 返回模式

画面 4: RabbitMQ 管理后台的 Exchanges 页面表格数据：
- Virtual host: (AMQP default)
- Name: amq.direct, amq.fanout, amq.headers, amq.match, amq.rabbitmq.log, amq.rabbitmq.trace, amq.topic
- Type: direct, fanout, headers, headers, topic, topic, topic
- Features: Q, Q, Q, Q, Q, Q, Q

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
