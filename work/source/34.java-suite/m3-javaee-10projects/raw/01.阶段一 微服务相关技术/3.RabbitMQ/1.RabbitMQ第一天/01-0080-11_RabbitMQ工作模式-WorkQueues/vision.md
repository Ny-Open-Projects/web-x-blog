# 画面线理解：11_RabbitMQ工作模式-WorkQueues

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\11_RabbitMQ工作模式-WorkQueues_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:56, 02:38, 02:50, 03:37, 04:13, 04:24, 04:43, 05:00, 05:29, 05:48, 05:59, 06:20, 07:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:36:35

1) 这一组画面整体在讲 RabbitMQ 的工作模式，重点演示了 Work queues（工作队列）模式的生产者与消费者代码实现及 RabbitMQ 管理界面的队列状态。

2) 按时间顺序列出每张画面的要点：
画面 1: RabbitMQ 管理界面，显示已存在一个名为 "hello_world" 的队列，状态为 Idle。
画面 2: PPT 目录页，当前章节为 "RabbitMQ 的工作模式"。
画面 3: IntelliJ IDEA 编辑器，显示生产者代码文件 Producer_WorkQueues.java，注释为 "//1.创建消息工厂"。
画面 4: PPT 页，标题为 "4.1 Work queues 工作队列模式"，图示 P -> 队列 -> C1, C2，并附有模式说明。
画面 5: IntelliJ IDEA 编辑器，显示生产者代码中 for 循环部分，用于发送 10 条消息。
画面 6: IntelliJ IDEA 编辑器，显示消费者代码文件 Consumer_WorkQueues.java，其中设置了连接工厂的主机、端口、虚拟主机、用户名和密码。
画面 7: IntelliJ IDEA 编辑器，显示消费者代码中调用 channel.queueDeclare 方法创建队列 "hello_world"。
画面 8: IntelliJ IDEA 编辑器，显示消费者代码中定义了 handleDelivery 方法用于处理消息，并调用 channel.basicConsume。
画面 9: IntelliJ IDEA 编辑器，显示消费者代码中创建了 DefaultConsumer 实例并传入 handleDelivery 方法。
画面 10: RabbitMQ 管理界面，显示了多个窗口的截图，包括管理界面、IDE、PPT 等。
画面 11: RabbitMQ 管理界面，显示已存在两个队列："hello_world" 和 "work_queues"，状态均为 Idle。
画面 12: IntelliJ IDEA 编辑器，显示生产者代码中发送消息的 body 为 "hello rabbitmq---"，并提示 SLF4J 日志绑定失败。
画面 13: IntelliJ IDEA 编辑器，显示终端输出了 10 条消息，内容为 "body: hello rabbitmq---"。
画面 14: PPT 页，标题为 "4.2 Pub/Sub 订阅模式"。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 3 代码：
```java
package com.ithema.producer;
import ...
public class Producer_WorkQueues {
    public static void main(String[] args) throws IOException, TimeoutException {
        //1.创建消息工厂
    }
}
```

画面 5 代码：
```java
for (int i = 1; i <= 10; i++) {
    String body = i + "hello rabbitmq---";
    channel.basicPublish("work_queues", null, body.getBytes());
}
```

画面 6 代码：
```java
ConnectionFactory factory = new ConnectionFactory();
factory.setHost("172.16.08.133"); //ip
factory.setPort(5672); //端口
factory.setVirtualHost("/"); //虚拟主机
factory.setUsername("itheima"); //用户名
factory.setPassword("itheima"); //密码
Connection connection = factory.newConnection();
Channel channel = connection.createChannel();
```

画面 7 代码：
```java
channel.queueDeclare("hello_world", true, false, false, null);
```

画面 8 代码：
```java
public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) {
    System.out.println("ConsumerTag: " + consumerTag);
    System.out.println("Exchange: " + envelope.getExchange());
    System.out.println("RoutingKey: " + envelope.getRoutingKey());
    System.out.println("Properties: " + properties);
    System.out.println("Body: " + new String(body));
}
```

画面 9 代码：
```java
Consumer consumer = new DefaultConsumer(channel) {
    @Override
    public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) {
        // 处理消息的逻辑
    }
};
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 2 PPT 标题：
- 目录
- MQ 的基本概念
- RabbitMQ 的安装和配置
- RabbitMQ 快速入门
- RabbitMQ 的工作模式（当前选中）
- Spring 整合 RabbitMQ

画面 4 PPT 标题：
- 4. RabbitMQ 的工作模式
- 4.1 Work queues 工作队列模式
- 模式说明：
  - Work Queues: 与入门程序的简单模式相比，多了一个或一些消费者，多个消费者共同消费同一个队列中的消息。
  - 应用场景: 对于任务过重或任务较多的情况，使用工作队列可以提高任务处理的速度。

画面 14 PPT 标题：
- 4. RabbitMQ 的工作模式
- 4.2 Pub/Sub 订阅模式

5) 无。
