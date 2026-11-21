# 画面线理解：12.RocketMQ研究-Rocket基础-延迟消息

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\12.RocketMQ研究-Rocket基础-延迟消息【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 02:08, 02:39, 02:59, 03:48, 05:05, 05:29, 05:55, 06:16, 06:54, 07:25, 07:49, 08:01, 08:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 03:11:08

1) 这一组画面整体在讲什么（一句话）：
演示如何在 RocketMQ 中使用同步延迟消息，包括代码实现和测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了课程文档的“2.7 延迟消息”章节，其中“2.7.1 延迟消息介绍”部分说明了延迟消息的用途和设置方法。
- 文档中提到延迟时间存在八个等级（1/5s/10s/30s/1m/2m/3m/4m/5m/6m/7m/8m/9m/10m/20m/30m/1h/2h），并指出使用 setDelayTimeLevel() 设置与时间对应的延迟级别即可。

画面 2：
- 展示了 IDE 中的代码，`ProducerSimple.java` 文件中定义了 `sendMsgByJson` 方法，用于发送消息。
- 代码中使用了 `rocketMQTemplate.convertAndSend(topic, orderExt)` 方法。

画面 3：
- 展示了 IDE 中的代码，`ProducerSimple.java` 文件中定义了 `sendMsgByJsonDelay` 方法，用于发送延迟消息。
- 代码中使用了 `rocketMQTemplate.syncSend` 方法。

画面 4：
- 展示了 IDE 中的代码，`ProducerSimple.java` 文件中定义了 `sendMsgByJsonDelay` 方法。
- 代码中使用了 `rocketMQTemplate.syncSend` 方法，参数包括 topic、message、timeout 和 delayLevel。

画面 5：
- 展示了 IDE 中的代码，`ProducerSimple.java` 文件中定义了 `sendMsgByJsonDelay` 方法。
- 代码中使用了 `MessageBuilder.withPayload(orderExt).build()` 方法构建消息。
- 代码中使用了 `rocketMQTemplate.syncSend` 方法。

画面 6：
- 展示了课程文档的“2.7.2 同步消息延迟”章节。
- 文档中展示了生产端的代码示例，包括使用 `MessageBuilder.withPayload(orderExt).build()` 构建消息，以及使用 `this.rocketMQTemplate.syncSend(topic, message, 1000, 3)` 发送消息。
- 文档中还提到了消费端需要“同自定义消息格式章节”。

画面 7：
- 展示了 IDE 中的项目结构，`test-rocketmq` 项目下包含 `src/main/java` 和 `src/test/java` 目录。
- 项目中包含 `application.yml` 配置文件。

画面 8：
- 展示了 IDE 中的测试类 `ProducerSimpleTest.java`。
- 代码中定义了 `testSendMsgByJsonDelay` 方法，用于测试发送延迟消息。
- 代码中使用了 `producerSimple.sendMsgByJsonDelay("my-topic-obj", orderExt)` 方法。

画面 9：
- 展示了 IDE 中的测试结果，测试通过。
- 控制台输出了 Spring Boot 的启动日志。

画面 10：
- 展示了 IDE 中的项目结构，`test-rocketmq` 项目下包含 `src/main/java` 和 `src/test/java` 目录。
- 项目中包含 `application.yml` 配置文件。

画面 11：
- 展示了 IDE 中的测试类 `ProducerSimpleTest.java`。
- 代码中定义了 `testSendMsgByJsonDelay` 方法，用于测试发送延迟消息。
- 代码中使用了 `producerSimple.sendMsgByJsonDelay("my-topic-obj", orderExt)` 方法。
- 控制台输出了测试日志。

画面 12：
- 展示了课程文档的“2.7.2 同步消息延迟”章节。
- 文档中展示了生产端的代码示例，包括使用 `MessageBuilder.withPayload(orderExt).build()` 构建消息，以及使用 `this.rocketMQTemplate.syncSend(topic, message, 1000, 3)` 发送消息。
- 文档中还提到了消费端需要“同自定义消息格式章节”。

画面 13：
- 展示了课程文档的“2.7.3 异步消息延迟（自学）”章节。
- 文档中展示了生产端的代码示例，包括使用 `this.rocketMQTemplate.getProducer().send(message, sendCallback)` 发送异步消息。
- 文档中还提到了消费端需要“同自定义消息格式章节”。

画面 14：
- 展示了课程文档的“2.7.3 异步消息延迟（自学）”章节。
- 文档中展示了生产端的代码示例，包括使用 `this.rocketMQTemplate.getProducer().send(message, sendCallback)` 发送异步消息。
- 文档中还提到了消费端需要“同自定义消息格式章节”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```
延迟消息也叫定时消息，比如在电商项目的交易系统中，当用户下单之后超过一段时间之后仍然没有支付，此时就需要将订单关闭。要实现该功能的话，可以在用户创建订单时就发送一条包含订单内容的延迟消息，该消息在一段时间之后投递给消息消费者，当消息消费者接收到该消息后，判断该订单的支付状态，如果处于未支付状态，则将该订单关闭。
RocketMQ的延迟消息实现非常简单，只需要发送消息前设置延迟的时间，延迟时间存在八个等级（1/5s/10s/30s/1m/2m/3m/4m/5m/6m/7m/8m/9m/10m/20m/30m/1h/2h），调用setDelayTimeLevel()设置与时间对应的延迟级别即可。
```

画面 2：
```
/**
 * 发送延迟消息
 * 消息内容为json格式
 */
public void sendMsgByJsonDelay(String topic, OrderExt orderExt) throws
JsonProcessingException, InterruptedException, RemotingException, MQClientException,
MQBrokerException {
    //发送同步消息，消息内容将orderExt转为json
    Message<OrderExt> message = MessageBuilder.withPayload(orderExt).build();
    //指定发送超时时间（毫秒）和延迟等级
    this.rocketMQTemplate.syncSend(topic, message, 1000, 3);
    System.out.println("send msg : " + orderExt);
}
```

画面 3：
```
/**
 * 发送延迟消息
 * 消息内容为json格式
 */
public void sendMsgByJsonDelay(String topic, OrderExt orderExt) throws
JsonProcessingException, InterruptedException, RemotingException, MQClientException,
MQBrokerException {
    //发送同步消息，消息内容将orderExt转为json
    Message<OrderExt> message = MessageBuilder.withPayload(orderExt).build();
    //指定发送超时时间（毫秒）和延迟等级
    this.rocketMQTemplate.syncSend(topic, message, 1000, 3);
    System.out.println("send msg : " + orderExt);
}
```

画面 4：
```
/**
 * 发送延迟消息
 * 消息内容为json格式
 */
public void sendMsgByJsonDelay(String topic, OrderExt orderExt) throws
JsonProcessingException, InterruptedException, RemotingException, MQClientException,
MQBrokerException {
    //发送同步消息，消息内容将orderExt转为json
    Message<OrderExt> message = MessageBuilder.withPayload(orderExt).build();
    //指定发送超时时间（毫秒）和延迟等级
    this.rocketMQTemplate.syncSend(topic, message, 1000, 3);
    System.out.println("send msg : " + orderExt);
}
```

画面 5：
```
/**
 * 发送延迟消息
 * 消息内容为json格式
 */
public void sendMsgByJsonDelay(String topic, OrderExt orderExt) throws
JsonProcessingException, InterruptedException, RemotingException, MQClientException,
MQBrokerException {
    //发送同步消息，消息内容将orderExt转为json
    Message<OrderExt> message = MessageBuilder.withPayload(orderExt).build();
    //指定发送超时时间（毫秒）和延迟等级
    this.rocketMQTemplate.syncSend(topic, message, 1000, 3);
    System.out.println("send msg : " + orderExt);
}
```

画面 6：
```
生产端：
/**
 * 发送延迟消息
 * 消息内容为json格式
 */
public void sendMsgByJsonDelay(String topic, OrderExt orderExt) throws
JsonProcessingException, InterruptedException, RemotingException, MQClientException,
MQBrokerException {
    //发送同步消息，消息内容将orderExt转为json
    Message<OrderExt> message = MessageBuilder.withPayload(orderExt).build();
    //指定发送超时时间（毫秒）和延迟等级
    this.rocketMQTemplate.syncSend(topic, message, 1000, 3);
    System.out.println("send msg : " + orderExt);
}

消费端：
同自定义消息格式章节。

测试：
//测试发送同步消息
@Test
```

画面 7：
```
application.yml
