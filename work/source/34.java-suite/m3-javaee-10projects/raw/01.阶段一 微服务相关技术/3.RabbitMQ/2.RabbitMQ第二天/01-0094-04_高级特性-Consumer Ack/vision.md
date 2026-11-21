# 画面线理解：04_高级特性-Consumer Ack

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\04_高级特性-Consumer Ack_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 02:19, 04:08, 04:56, 05:55, 06:56, 08:00, 10:32, 11:34, 12:23, 13:25, 14:24, 15:10, 16:03, 17:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:46:40

1) 这一组画面整体在讲 RabbitMQ 消费者确认机制（Consumer Ack）的实现方式与代码示例。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 PPT 标题“1.2 Consumer Ack”，内容说明 RabbitMQ 消费者确认机制的三种方式：自动确认（acknowledge="none"）、手动确认（acknowledge="manual"）、根据异常情况确认（acknowledge="auto"），并解释了自动确认的语义。
画面 2: 展示 IDE 中的 Spring Boot 项目结构，包含 `rabbitmq-consumer-spring` 项目，以及 `spring-rabbitmq-consumer.xml` 配置文件，其中配置了 RabbitMQ 的连接工厂。
画面 3: 展示 `AckListener.java` 文件，开始编写消费者监听器代码。
画面 4: 展示 `AckListener.java` 文件，编写了 `@Component` 注解和 `MessageListener` 接口实现，并在 `onMessage` 方法中使用 `System.out.println` 打印消息体。
画面 5: 展示 `ConsumerTest.java` 文件，编写测试类，准备测试消费者监听器。
画面 6: 展示 `MessageListener.java` 的源码，说明其是 `@FunctionalInterface`，并列出其所有实现类。
画面 7: 展示 `AckListener.java` 文件，将监听器实现改为 `ChannelAwareMessageListener`，并添加了注释说明手动确认的步骤。
画面 8: 展示 `AckListener.java` 文件，使用 `message.getMessageProperties().getDeliveryTag()` 获取消息的交付标签。
画面 9: 展示 `AckListener.java` 文件，编写 `try-catch` 块，使用 `channel.basicAck(deliveryTag, multiple: true)` 进行手动确认。
画面 10: 展示 `ProducerTest.java` 文件，配置 `RabbitTemplate` 的 `setReturnCallback` 用于处理消息返回。
画面 11: 展示 `AckListener.java` 文件，完善 `try-catch` 块，添加了 `channel.basicAck(deliveryTag, multiple: true)` 和 `channel.basicNack(deliveryTag, multiple: true, requeue: true)` 用于处理异常和重新入队。
画面 12: 展示 `ConsumerTest.java` 文件，编写测试方法，调用 `ackListener.onMessage` 方法。
画面 13: 展示 `ConsumerTest.java` 文件，完善测试方法，添加了 `try-catch` 块和 `channel.basicNack` 用于模拟异常情况。
画面 14: 展示 PPT 标题“1.3 消息可靠性总结”，列出消息可靠性的四个要点：持久化（exchange、queue、message）、生产方确认 Confirm、消费方确认 Ack、Broker 高可用。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 2 的 XML 配置：
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
        host="172.16.0.88"
        port="5672"
        username="guest"
        password="guest"
        virtual-host="/"/>

    <context:component-scan base-package="com.ithema.listener" />
</beans>
```

画面 7 的 Java 代码：
```java
/**
 * Consumer_ACK说明：
 * 1. 设置手动确认，acknowledge="manual"
 * 2. 实现接口从ChannelAwareMessageListener接口
 * 3. 业务处理成功，调用channel.basicAck()确认
 * 4. 如果出现异常，则调用channel.basicNack()拒绝签收，broker重新发送给consumer
 */
@Component
public class AckListener implements ChannelAwareMessageListener {

    @Override
    public void onMessage(Message message, Channel channel) throws Exception {
        //1. 接收消息
        System.out.println(new String(message.getBody()));
        //2. 处理业务逻辑
        System.out.println("处理业务逻辑...");
        //3. 手动确认
        channel.basicAck(message.getMessageProperties().getDeliveryTag(), true);
    }
}
```

画面 10 的 Java 代码：
```java
public void testReturn() {
    //设置消息必须被确认的模式
    rabbitTemplate.setMandatory(true);
    //设置返回回调
    rabbitTemplate.setReturnCallback(new RabbitTemplate.ReturnCallback() {
        @Override
        public void returnedMessage(Message message, int replyCode, String replyText) {
            System.out.println("消息返回：" + message);
            System.out.println("回复码：" + replyCode);
            System.out.println("回复文本：" + replyText);
        }
    });
}
```

画面 11 的 Java 代码：
```java
try {
    //1. 接收消息
    System.out.println(new String(message.getBody()));
    //2. 处理业务逻辑
    System.out.println("处理业务逻辑...");
    //3. 手动确认
    channel.basicAck(deliveryTag, true);
} catch (Exception e) {
    //4. 拒绝签收
    channel.basicNack(deliveryTag, true, true);
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 1: PPT 标题“1. RabbitMQ 高级特性”，子标题“1.2 Consumer Ack”，内容为“ack指Acknowledge，确认。表示消费者收到消息后的确认方式。有三种确认方式：自动确认：acknowledge="none"；手动确认：acknowledge="manual"；根据异常情况确认：acknowledge="auto"（这种方式使用麻烦，不作讲解）”。
画面 14: PPT 标题“1. RabbitMQ 高级特性”，子标题“1.3 消息可靠性总结”，内容为“1. 持久化：exchange要持久化；queue要持久化；message要持久化。2. 生产方确认 Confirm。3. 消费方确认 Ack。4. Broker高可用”。

5) 无。
