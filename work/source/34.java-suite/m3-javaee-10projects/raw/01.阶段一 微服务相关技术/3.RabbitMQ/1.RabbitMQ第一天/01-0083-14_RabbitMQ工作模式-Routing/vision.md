# 画面线理解：14_RabbitMQ工作模式-Routing

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\14_RabbitMQ工作模式-Routing_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 01:11, 03:10, 04:13, 04:24, 05:45, 06:31, 06:58, 07:39, 08:09, 08:30, 09:28, 10:06, 10:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:38:37

1) 这一组画面整体在讲 RabbitMQ 的 Routing 路由模式，通过代码演示如何创建交换机、绑定队列和发送/接收消息。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Producer_Publish.java 文件中的代码，用于向名为 "test_direct" 的交换机发送消息，但未绑定队列，导致消息无法被消费。
画面2: 代码中注释了 "test_direct" 交换机的创建和绑定逻辑，但未实际执行。
画面3: 展示了 RabbitMQ 的 Routing 路由模式架构图，包含生产者 P、交换机 X、队列 C1 和 C2，以及路由键 error、info、warning。
画面4: 展示了 Producer_Routing.java 文件中的代码，创建了名为 "test_direct" 的 direct 交换机和队列，并绑定。
画面5: 代码中注释了 "test_direct" 交换机的创建和绑定逻辑，但未实际执行。
画面6: 代码中注释了 "test_direct" 交换机的创建和绑定逻辑，但未实际执行。
画面7: 展示了 RabbitMQ 管理界面的 Exchanges 页面，列出了包括 "test_direct" 和 "test_fanout" 在内的多个交换机。
画面8: 展示了 Consumer_Routing.java 文件中的代码，创建了连接工厂并设置连接参数。
画面9: 代码中注释了 "test_fanout" 交换机的创建和绑定逻辑，但未实际执行。
画面10: 代码中注释了 "test_fanout" 交换机的创建和绑定逻辑，但未实际执行。
画面11: 展示了 Consumer_Routing.java 文件中的代码，创建了消费者对象并设置回调方法。
画面12: 代码中注释了 "test_direct" 交换机的创建和绑定逻辑，但未实际执行。
画面13: 代码中注释了 "test_direct" 交换机的创建和绑定逻辑，但未实际执行。
画面14: 展示了 PPT 页面，标题为 "4. RabbitMQ 的工作模式"，子标题为 "4.3 Routing 路由模式" 和 "2. 代码编写"，并附有路由模式的架构图。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1:
```java
String body = "日志信息：张三调用了findAll方法...日志级别：info...";
channel.queueBind(queueName, exchangeName, "");
channel.basicPublish(exchangeName, "", basicProperties: null, body.getBytes());
channel.close();
connection.close();
```

画面4:
```java
String exchangeName = "test_direct";
channel.exchangeDeclare(exchangeName, BuiltinExchangeType.DIRECT, true, false, false, null);
String queueName = "test_direct_queue";
channel.queueDeclare(queueName, true, false, false, map);
channel.queueBind(queueName, exchangeName, "");
```

画面6:
```java
channel.queueBind(queueName, exchangeName, "error");
channel.queueBind(queueName, exchangeName, "info");
channel.queueBind(queueName, exchangeName, "warning");
```

画面8:
```java
factory.setHost("172.16.96.133"); // 默认 5672
factory.setPort(5672); // 默认 5672
factory.setUserName("heima"); // 用户名
factory.setPassword("heima"); // 密码
Connection connection = factory.newConnection();
Channel channel = connection.createChannel();
```

画面11:
```java
new DefaultConsumer(channel) {
    @Override
    public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) {
        System.out.println("Exchange: " + envelope.getExchange());
        System.out.println("RoutingKey: " + envelope.getRoutingKey());
        System.out.println("Properties: " + properties);
        System.out.println("Body: " + new String(body));
        System.out.println("消息主体已存储到数据库...");
    }
};
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14:
PPT 标题: "4. RabbitMQ 的工作模式"
子标题: "4.3 Routing 路由模式"
子标题: "2. 代码编写"
架构图: 生产者 P -> 交换机 X -> 队列 C1 (路由键: error, info)
架构图: 生产者 P -> 交换机 X -> 队列 C2 (路由键: error, warning)

5) 不要评价画面美观，不要输出与课程无关的内容。
