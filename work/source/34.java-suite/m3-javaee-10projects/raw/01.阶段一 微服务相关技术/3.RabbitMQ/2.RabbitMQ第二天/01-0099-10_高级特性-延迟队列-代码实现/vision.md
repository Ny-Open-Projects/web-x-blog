# 画面线理解：10_高级特性-延迟队列-代码实现

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\10_高级特性-延迟队列-代码实现_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 03:02, 04:26, 05:15, 05:56, 06:33, 06:58, 07:37, 09:03, 10:24, 11:29, 12:30, 13:05, 13:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:49:57

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 RabbitMQ 的 TTL + 死信队列机制实现订单延迟处理功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- PPT 标题：1. RabbitMQ 高级特性，子标题：1.6 延迟队列。
- 文字内容：很可惜，在RabbitMQ中并未提供延迟队列功能。但是可以使用：TTL + 死信队列 组合实现延迟队列的效果。
- 图形：展示订单系统 → Exchange → Queue → 库存系统 的流程，Queue 指向“库存系统”并标注“设置队列过期时间为30分钟”，同时 Queue 指向“死信队列（DLX）”。
- 图形标注：死信队列（DLX）指向“库存系统”并标注“判断订单状态”，然后分叉为“支付”、“什么都不做”、“取消订单，回滚库存”。

画面 2:
- IDE 界面：显示项目结构和 `spring-rabbitmq-producer.xml` 文件。
- XML 配置代码：
```xml
<rabbit:queue name="queue_dlx" id="queue_dlx"><rabbit:queue>
<rabbit:topic-exchange name="exchange_dlx"><rabbit:exchange>
<rabbit:bindings>
    <rabbit:binding exchange="exchange_dlx" queue="queue_dlx" />
</rabbit:bindings>
</rabbit:exchange>
</rabbit:queue>
</rabbit:bindings>
```

画面 3:
- RabbitMQ Management 界面：显示队列列表，包含 `queue_dlx`、`test_queue_confirm`、`test_queue_dlx`、`test_queue_ttl`。
- 队列特性：`queue_dlx` 标记为 D（Durable）、DLX、Q（Queue）；`test_queue_dlx` 标记为 D、TTL、DLX、Q。

画面 4:
- RabbitMQ Management 界面：在“Add a new queue”区域，Arguments 部分显示：
  - x-dead-letter-exchange: String
  - x-dead-letter-routing-key: String
  - x-message-ttl: String

画面 5:
- IDE 界面：显示 `ProducerTest.java` 文件，`testDlx()` 方法中包含注释“测试过期时间，死信消息”和“测试长超时后，消息死信”。
- 代码片段：
```java
// 测试长超时后，消息死信
for (int i = 0; i < 20; i++) {
    rabbitTemplate.convertAndSend("test_exchange_dlx", "test.dlx.haha", "我是一条消息，我会死吗？");
}
```

画面 6:
- RabbitMQ Management 界面：空白页面，仅显示“HTTP API | Command Line”。

画面 7:
- RabbitMQ Management 界面：显示队列列表，包含 `order_queue`、`order_queue_dlx`、`queue_dlx`、`test_queue_confirm`、`test_queue_dlx`、`test_queue_ttl`。
- 队列特性：`order_queue_dlx` 标记为 D、TTL、DLX、Q；`test_queue_dlx` 标记为 D、TTL、DLX、Q。

画面 8:
- IDE 界面：显示 `ProducerTest.java` 文件，`testDelay()` 方法中包含注释“测试消息延迟”。
- 代码片段：
```java
// 测试消息延迟
rabbitTemplate.convertAndSend("test_exchange_dlx", "test.dlx.haha", "我是一条消息");
```

画面 9:
- IDE 界面：显示 `ProducerTest.java` 文件，`testDelay()` 方法中包含注释“测试消息延迟”。
- 代码片段：
```java
@Test
void testDelay() throws InterruptedException {
    // 发送订单消息，待业务处理中，下订单成功后，发送消息
    for (int i = 1; i <= 10; i++) {
        rabbitTemplate.convertAndSend("order_exchange", "order.msg", "订单信息：id=" + i + ",time=" + System.currentTimeMillis());
        Thread.sleep(1000);
    }
}
```

画面 10:
- IDE 界面：显示 `OrderListener.java` 文件，`onMessage` 方法中包含注释“处理业务逻辑”。
- 代码片段：
```java
@Override
public void onMessage(Message message, Channel channel) throws Exception {
    long deliveryTag = message.getMessageProperties().getDeliveryTag();
    System.out.println(new String(message.getBody()));
    // 处理业务逻辑
    System.out.println("处理订单业务逻辑...");
    System.out.println("根据订单状态更新库存...");
    System.out.println("判断状态是否为未支付成功");
    System.out.println("取消订单，回滚库存...");
    // 手动确认消息
    channel.basicAck(deliveryTag, true);
}
```

画面 11:
- IDE 界面：显示 `spring-rabbitmq-consumer.xml` 文件。
- XML 配置代码：
```xml
<rabbit:connection-factory id="connectionFactory" host="172.16.88.133" port="5672" username="guest" password="guest" virtual-host="/"/>
<context:component-scan base-package="com.itheima.listener" />
<rabbit:listener-container connection-factory="connectionFactory" acknowledge="manual" prefetch="1">
    <rabbit:listener ref="orderListener" queue-names="test_queue_confirm" />
    <rabbit:listener ref="divListener" queue-names="test_queue_dlx" />
</rabbit:listener-container>
```

画面 12:
- IDE 界面：显示 `ConsumerTest.java` 文件，`testDelay()` 方法中包含注释“测试消息延迟”。
- 代码片段：
```java
@Test
void testDelay() throws InterruptedException {
    // 发送订单消息，待业务处理中，下订单成功后，发送消息
    for (int i = 1; i <= 10; i++) {
        rabbitTemplate.convertAndSend("order_exchange", "order.msg", "订单信息：id=" + i + ",time=" + System.currentTimeMillis());
        Thread.sleep(1000);
    }
}
```

画面 13:
- IDE 界面：显示 `ConsumerTest.java` 文件，`testDelay()` 方法中包含注释“测试消息延迟”。
- 控制台输出：
```
订单信息：id=1, time=2019-09-17 16:41:47
处理订单业务逻辑...
根据订单状态更新库存...
判断状态是否为未支付成功
取消订单，回滚库存...
```

画面 14:
- PPT 标题：1. RabbitMQ 高级特性，子标题：1.6 延迟队列小结。
