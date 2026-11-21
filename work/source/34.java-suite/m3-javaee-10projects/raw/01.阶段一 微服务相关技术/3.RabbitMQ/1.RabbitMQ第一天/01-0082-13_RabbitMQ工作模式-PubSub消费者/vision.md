# 画面线理解：13_RabbitMQ工作模式-PubSub消费者

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\13_RabbitMQ工作模式-PubSub消费者_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:33, 00:39, 00:51, 01:34, 01:46, 01:48, 01:58, 02:05, 02:24, 02:37, 02:46, 03:04, 03:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:38:05

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 RabbitMQ 的 Direct Exchange 模式，通过 Java 代码实现消息的发布与订阅，重点讲解了交换机、队列、绑定关系的创建与消费者监听的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 代码文件：`Producer_PubSub.java`
- 代码内容：
```java
channel.exchangeDeclare(exchangeName, BuiltinExchangeType.DIRECT, true, false, false, null);
String queueName = "test_fanout_queue";
String queue2Name = "test_fanout_queue2";
channel.queueDeclare(queueName, true, false, false, null);
channel.queueDeclare(queue2Name, true, false, false, null);
// 绑定队列到交换机
queueBind(String queue, String exchange, String routingKey)
参数：
1. queue：队列名称
2. exchange：交换机名称
3. routingKey：路由键，绑定规则
如果交换机类型为fanout，routingKey设置为""
channel.queueBind(queueName, exchangeName, "z2");
channel.queueBind(queue2Name, exchangeName, "z2");
String body = "日志信息：张三调用了findAll方法...日志级别：Info...";
// 我的发送
channel.basicPublish(exchangeName, "z2", basicProperties, null, body.getBytes());
connection.close();
```
- 画面中显示了 RabbitMQ 的架构图：P（生产者）→ X（交换机）→ C1、C2（消费者队列）。

画面2：
- 代码文件：`Consumer_PubSub1.java`
- 代码内容：
```java
// 建立连接
Connection connection = factory.newConnection();
// 创建通道
Channel channel = connection.createChannel();
// 声明队列
channel.queueDeclare(queue, durable, exclusive, autoDelete, arguments);
参数：
1. queue：队列名称
2. durable：是否持久化，当no设置为true，还在
3. exclusive：是否独占，只有一个消费者可以订阅队列
4. autoDelete：是否自动删除，当没有Consumer时，自动删除
5. arguments：参数
// 如果没有一个名字为hello_world的队列，会创建默认队列
channel.queueDeclare("work_queue", true, false, false, null);
```
- 画面中显示了 RabbitMQ 的架构图：P（生产者）→ X（交换机）→ C1、C2（消费者队列）。

画面3：
- 代码文件：`Consumer_PubSub1.java`
- 代码内容：
```java
// 建立连接
Connection connection = factory.newConnection();
// 创建通道
Channel channel = connection.createChannel();
// 声明队列
channel.queueDeclare(queue, durable, exclusive, autoDelete, arguments);
参数：
1. queue：队列名称
2. durable：是否持久化，当no设置为true，还在
3. exclusive：是否独占，只有一个消费者可以订阅队列
4. autoDelete：是否自动删除，当没有Consumer时，自动删除
5. arguments：参数
// 如果没有一个名字为hello_world的队列，会创建默认队列
channel.queueDeclare("work_queue", true, false, false, null);
```
- 画面中显示了 RabbitMQ 的架构图：P（生产者）→ X（交换机）→ C1、C2（消费者队列）。

画面4：
- 代码文件：`Consumer_PubSub1.java`
- 代码内容：
```java
// 建立连接
Connection connection = factory.newConnection();
// 创建通道
Channel channel = connection.createChannel();
// 声明队列
channel.queueDeclare(queue, durable, exclusive, autoDelete, arguments);
参数：
1. queue：队列名称
2. durable：是否持久化，当no设置为true，还在
3. exclusive：是否独占，只有一个消费者可以订阅队列
4. autoDelete：是否自动删除，当没有Consumer时，自动删除
5. arguments：参数
// 如果没有一个名字为hello_world的队列，会创建默认队列
channel.queueDeclare("work_queue", true, false, false, null);
```
- 画面中显示了 RabbitMQ 的架构图：P（生产者）→ X（交换机）→ C1、C2（消费者队列）。

画面5：
- 代码文件：`Consumer_PubSub1.java`
- 代码内容：
```java
@Override
public void handleDelivery(String consumerTag, Delivery delivery) throws IOException {
    System.out.println("Exchange：" + delivery.envelope.getExchange());
    System.out.println("RoutingKey：" + delivery.envelope.getRoutingKey());
    System.out.println("Properties：" + delivery.properties());
    System.out.println("body：" + new String(delivery.body()));
    System.out.println("【打印日志信息保存数据库...】");
}
```
- 画面中显示了 RabbitMQ 的架构图：P（生产者）→ X（交换机）→ C1、C2（消费者队列）。

画面6：
- 代码文件：`Consumer_PubSub1.java`
- 代码内容：
```java
@Override
public void handleDelivery(String consumerTag, Delivery delivery) throws IOException {
    System.out.println("Exchange：" + delivery.envelope.getExchange());
    System.out.println("RoutingKey：" + delivery.envelope.getRoutingKey());
    System.out.println("Properties：" + delivery.properties());
    System.out.println("body：" + new String(delivery.body()));
    System.out.println("【打印日志信息保存数据库...】");
}
```
- 画面中显示了 RabbitMQ 的架构图：P（生产者）→ X（交换机）→ C1、C2（消费者队列）。

画面7：
- 代码文件：`Consumer_PubSub1.java`
- 代码内容：
```java
@Override
public void handleDelivery(String consumerTag, Delivery delivery) throws IOException {
    System.out.println("Exchange：" + delivery.envelope.getExchange());
    System.out.println("RoutingKey：" + delivery.envelope.getRoutingKey());
    System.out.println("Properties：" + delivery.properties());
    System.out.println("body：" + new String(delivery.body()));
    System.out.println("【打印日志信息保存数据库...】");
}
```
- 画面中显示了 RabbitMQ 的架构图：P（生产者）→ X（交换机）→ C1、C2（消费者队列）。

画面8：
- 代码文件：`Consumer_PubSub1.java`
- 代码内容：
```java
@Override
public void handleDelivery(String consumerTag, Delivery delivery) throws IOException {
    System.out.println("Exchange：" + delivery.envelope.getExchange());
    System.out.println("RoutingKey：" + delivery.envelope.getRoutingKey());
    System.out.println("Properties：" + delivery.properties());
    System.out.println("body：" + new String(delivery.body()));
    System.out.println("【打印日志信息保存数据库...】");
}
```
- 画面中显示了 RabbitMQ 的架构图：P（生产者）→ X（交换机）→ C1、C2（消费者队列）。

画面9：
- 代码文件：`Consumer_PubSub1.java`
- 代码内容：
```java
@Override
public void handleDelivery(String consumerTag, Delivery delivery) throws IOException {
    System.out.println("Exchange：" + delivery.envelope.getExchange());
    System.out.println("RoutingKey：" + delivery.envelope.getRoutingKey());
    System.out.println("Properties：" + delivery.properties());
    System.out.println("body：" + new String(delivery.body()));
    System.out.println("【打印日志信息保存数据库...】");
}
```
- 画面中显示了 RabbitMQ 的架构图：P（生产者）→ X（交换机）→ C1、C2（消费者队列）。

画面10：
- 代码文件：`Producer_PubSub.java`
- 代码内容：
```java
String exchangeName = "test_fanout";
channel.exchangeDeclare(exchangeName, BuiltinExchangeType.DIRECT, true, false, false, null);
String queueName = "test_fanout_queue";
String queue2Name = "test_fanout_queue2";
channel.queueDeclare(queueName, true, false, false, null);
channel.queueDeclare(queue2Name, true, false, false, null);
// 绑定队列到交换机
queueBind(String queue, String exchange, String routingKey)
参数：
1. queue：队列名称
2. exchange：交换机名称
3. routingKey：路由键，绑定规则
如果交换机类型为fanout，routingKey设置为""
channel.queueBind(queueName, exchangeName, "z2");
channel.queueBind(queue2Name, exchangeName, "z2");
String body = "日志信息：张三调用了findAll方法...日志级别：Info...";
// 我的发送
channel.basicPublish(exchangeName, "z2", basicProperties, null, body.getBytes());
connection.close();
```
- 画面中显示了 RabbitMQ 的架构图：P（生产者）→ X（交换机）→ C1、C2（消费者队列）。

画面11：
- 代码文件：`Producer_PubSub.java`
- 代码内容：
```java
String exchangeName = "test_fanout";
channel.exchangeDeclare(exchangeName, BuiltinExchangeType.DIRECT, true, false, false, null
