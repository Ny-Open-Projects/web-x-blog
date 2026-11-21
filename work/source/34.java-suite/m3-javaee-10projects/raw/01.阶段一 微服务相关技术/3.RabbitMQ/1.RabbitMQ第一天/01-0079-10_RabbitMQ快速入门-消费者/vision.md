# 画面线理解：10_RabbitMQ快速入门-消费者

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\10_RabbitMQ快速入门-消费者_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:38, 00:52, 01:11, 01:45, 02:22, 02:36, 04:21, 04:47, 07:12, 08:07, 08:35, 09:26, 10:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:36:03

1) 这一组画面整体在讲 RabbitMQ 的基础使用，通过 Java 代码演示生产者和消费者如何通过 Exchange 和 Queue 发送和接收消息。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了生产者代码文件 Producer_HelloWorld.java。
- 代码内容：String body = "hello rabbitmq"; channel.basicPublish("hello_world", "hello_world", null, body.getBytes()); channel.close();
- 画面右上角有 RabbitMQ 的工作模式图：P（生产者）→ Exchange → Queue → C（消费者）。

画面2：
- 展示了消费者代码文件 Consumer_HelloWorld.java。
- 代码内容：public class Consumer_HelloWorld { ... }，光标位于类定义处。

画面3：
- 展示了多个文件和 PPT 页面的缩略图，包括 RabbitMQ 的安装与配置相关材料。
- 画面右上角有 RabbitMQ 的工作模式图。

画面4：
- 展示了消费者代码中创建 ConnectionFactory 的部分。
- 代码内容：ConnectionFactory factory = new ConnectionFactory(); factory.setHost("172.16.98.133"); factory.setVirtualHost("/"); factory.setUsername("heima"); factory.setPassword("heima"); Connection connection = factory.newConnection();

画面5：
- 展示了创建 Channel 的代码。
- 代码内容：Channel channel = connection.createChannel();
- 画面右侧有 channel.queueDeclare() 方法的注释说明。

画面6：
- 展示了声明队列的代码。
- 代码内容：channel.queueDeclare("hello_world", true, false, false, null);
- 画面右侧有方法参数的注释说明。

画面7：
- 展示了 RabbitMQ 客户端库的类文件结构。
- 代码内容：Decompiled class file, bytecode version 52.0 (Java 8)。
- 画面右侧有 Channel 类的多个方法。

画面8：
- 展示了 RabbitMQ 客户端库的类文件结构。
- 代码内容：Choose Implementation of Consumer (10 found)。
- 画面右侧有多个 Consumer 类的实现。

画面9：
- 展示了消费者代码中创建消费者对象的代码。
- 代码内容：Consumer consumer = new DefaultConsumer(channel); channel.basicConsume("hello_world", true, consumer);

画面10：
- 展示了消费者代码中重写 handleDelivery 方法的代码。
- 代码内容：public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) { ... }
- 画面右侧有 Envelope 类的属性方法提示。

画面11：
- 展示了消费者代码中重写 handleDelivery 方法的代码。
- 代码内容：System.out.println("consumerTag: " + consumerTag); System.out.println("Exchange: " + envelope.getExchange()); System.out.println("RoutingKey: " + envelope.getRoutingKey()); System.out.println("properties: " + properties); System.out.println("body: " + new String(body));

画面12：
- 展示了消费者代码中重写 handleDelivery 方法的代码。
- 代码内容：System.out.println("body: " + new String(body));
- 画面下方有控制台输出：properties: ... body: hello rabbitmq

画面13：
- 展示了 PPT 页面，标题为“1.6 RabbitMQ 简介”。
- 内容：Exchange: message 到达 broker 的第一站，根据分发规则，匹配查找表中的 routing key，分发消息到 queue 中去。Queue: 消息最终被送到这里等待 consumer 取走。Binding: exchange 和 queue 之间的连接，binding 中可以包含 routing key，Binding 信息被保存到 exchange 中的查询表中，用于 message 的分发依据。

画面14：
- 展示了 PPT 目录页。
- 内容：目录包括：MQ 的基本概念、RabbitMQ 的安装和配置、RabbitMQ 快速入门、RabbitMQ 的工作模式、Spring 整合 RabbitMQ。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
String body = "hello rabbitmq";
channel.basicPublish("hello_world", "hello_world", null, body.getBytes());
channel.close();
```

画面4：
```java
ConnectionFactory factory = new ConnectionFactory();
factory.setHost("172.16.98.133");
factory.setVirtualHost("/");
factory.setUsername("heima");
factory.setPassword("heima");
Connection connection = factory.newConnection();
```

画面5：
```java
Channel channel = connection.createChannel();
```

画面6：
```java
channel.queueDeclare("hello_world", true, false, false, null);
```

画面9：
```java
Consumer consumer = new DefaultConsumer(channel);
channel.basicConsume("hello_world", true, consumer);
```

画面10：
```java
public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) {
    System.out.println("consumerTag: " + consumerTag);
    System.out.println("Exchange: " + envelope.getExchange());
    System.out.println("RoutingKey: " + envelope.getRoutingKey());
    System.out.println("properties: " + properties);
    System.out.println("body: " + new String(body));
}
```

画面11：
```java
System.out.println("Exchange: " + envelope.getExchange());
System.out.println("RoutingKey: " + envelope.getRoutingKey());
System.out.println("properties: " + properties);
System.out.println("body: " + new String(body));
```

画面12：
```java
System.out.println("body: " + new String(body));
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面13：
- 标题：1.6 RabbitMQ 简介
- 内容：
  - Exchange: message 到达 broker 的第一站，根据分发规则，匹配查找表中的 routing key，分发消息到 queue 中去。常见的类型有：direct (point-to-point), topic (publish-subscribe) and fanout (multicast)。
  - Queue: 消息最终被送到这里等待 consumer 取走。
  - Binding: exchange 和 queue 之间的连接，binding 中可以包含 routing key，Binding 信息被保存到 exchange 中的查询表中，用于 message 的分发依据。

画面14：
- 标题：目录
- 内容：
  - MQ 的基本概念
  - RabbitMQ 的安装和配置
  - RabbitMQ 快速入门
  - RabbitMQ 的工作模式
  - Spring 整合 RabbitMQ

5) 不要评价画面美观，不要输出与课程无关的内容。
