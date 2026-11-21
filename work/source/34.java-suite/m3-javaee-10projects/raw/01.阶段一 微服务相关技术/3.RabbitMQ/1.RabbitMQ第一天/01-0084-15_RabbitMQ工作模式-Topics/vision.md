# 画面线理解：15_RabbitMQ工作模式-Topics

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\15_RabbitMQ工作模式-Topics_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 02:18, 02:58, 04:01, 06:51, 07:02, 07:16, 07:37, 08:13, 08:23, 09:00, 09:24, 10:07, 10:25, 10:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:39:14

1) 这一组画面整体在讲 RabbitMQ 的 Topics 通配符模式，通过代码演示如何创建 Topic Exchange、绑定队列以及发送和接收带路由键的消息。

2) 按时间顺序列出每张画面的要点：
画面 1: PPT 标题为“4. RabbitMQ 的工作模式”下的“4.4 Topics 通配符模式”，展示了一个 Topic Exchange 的示意图，包含路由键模式：* .orange.*、*.rabbit.*、lazy.#。
画面 2: IDE 中展示 Producer_Routing.java 代码，定义了三个队列绑定到 Topic Exchange，路由键分别为 error、info、warning。
画面 3: IDE 中展示 Producer_Topics.java 代码，定义了 Topic Exchange 和三个队列的绑定关系，路由键分别为 * .error、*.order、*.*。
画面 4: RabbitMQ 管理界面显示了所有队列，包括 test_direct_queue1、test_direct_queue2、test_fanout_queue1、test_fanout_queue2、work_queue。
画面 5: RabbitMQ 管理界面显示了 Topic Exchange test_topic 的绑定关系，绑定到三个队列，路由键分别为 * .error、*.order、*.*。
画面 6: RabbitMQ 管理界面显示了所有交换机，包括 amq_direct、amq_fanout、amq_headers、amq_match、amq.rabbitmq.trace、test_direct、test_fanout、test_topic。
画面 7: RabbitMQ 管理界面显示了所有交换机，包括 amq_direct、amq_fanout、amq_headers、amq_match、amq.rabbitmq.trace、test_direct、test_fanout、test_topic。
画面 8: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 9: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 10: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 11: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 12: IDE 中展示 Producer_Topics.java 代码，定义了发送消息的方法，路由键为 goods.error。
画面 13: IDE 中展示 Producer_Topics.java 代码，定义了发送消息的方法，路由键为 goods.error。
画面 14: PPT 标题为“4. RabbitMQ 的工作模式”下的“4.4 Topics 通配符模式”，子标题为“2. 代码编写”。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 2:
```java
String exchangeName = "test_direct";
channel.queueDeclare(queueName, true, false, false, null);
channel.queueBind(queueName, exchangeName, "error");
channel.queueBind(queueName, exchangeName, "info");
channel.queueBind(queueName, exchangeName, "warning");
```

画面 3:
```java
String exchangeName = "test_fanout";
channel.exchangeDeclare(exchangeName, BuiltinExchangeType.FANOUT, true, false, null);
String queueName = "test_fanout_queue1";
channel.queueDeclare(queueName, true, false, false, null);
channel.queueBind(queueName, exchangeName, "");
```

画面 5:
```java
// 绑定关系
To Routing key Arguments
test_topic_queue1 * .error
test_topic_queue1 order
test_topic_queue1 *.*
```

画面 8:
```java
@Override
public void handleDelivery(String consumerTag, Delivery delivery) throws IOException {
    System.out.println("Exchange: " + delivery.getEnvelope().getExchange());
    System.out.println("RoutingKey: " + delivery.getEnvelope().getRoutingKey());
    System.out.println("Properties: " + delivery.getProperties());
    System.out.println("Body: " + new String(delivery.getBody()));
}
```

画面 12:
```java
String body = "日志消息：张三调用了findAll方法...日志级别：info...";
channel.basicPublish(exchangeName, "goods.error", null, body.getBytes());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: PPT 标题为“4. RabbitMQ 的工作模式”，子标题为“4.4 Topics 通配符模式”，架构图显示 P 指向 X，X 指向 Q1 和 Q2，Q1 指向 C1，Q2 指向 C2。
画面 4: RabbitMQ 管理界面表格数据包括 Virtual host、Name、Features、State、Ready、Unacked、Total、incoming deliver/get、ack。
画面 5: RabbitMQ 管理界面表格数据包括 To、Routing key、Arguments。
画面 6: RabbitMQ 管理界面表格数据包括 Virtual host、Name、Type、Features、Message rate in、Message rate out。
画面 7: RabbitMQ 管理界面表格数据包括 Virtual host、Name、Type、Features、Message rate in、Message rate out。
画面 8: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 9: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 10: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 11: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 12: IDE 中展示 Producer_Topics.java 代码，定义了发送消息的方法，路由键为 goods.error。
画面 13: IDE 中展示 Producer_Topics.java 代码，定义了发送消息的方法，路由键为 goods.error。
画面 14: PPT 标题为“4. RabbitMQ 的工作模式”，子标题为“4.4 Topics 通配符模式”，子标题为“2. 代码编写”。

5) 无
