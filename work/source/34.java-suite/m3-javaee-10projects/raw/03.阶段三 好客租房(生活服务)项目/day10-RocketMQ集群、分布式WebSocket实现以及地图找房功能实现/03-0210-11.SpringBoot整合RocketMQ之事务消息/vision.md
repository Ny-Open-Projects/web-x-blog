# 画面线理解：11.SpringBoot整合RocketMQ之事务消息

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\11.SpringBoot整合RocketMQ之事务消息【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:07, 02:35, 03:57, 05:22, 06:40, 09:15, 10:45, 11:56, 12:52, 14:02, 15:24, 16:44, 17:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:18:10

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 RocketMQ 实现事务消息，包括定义事务监听器、配置生产者和消费者，以及测试消息发送与事务提交。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“3.8.1. 定义TransactionListenerImpl”章节，介绍事务消息的定义。
画面 2: 在 IntelliJ IDEA 中，显示 `TransactionListenerImpl.java` 文件，其中 `implements RocketMQLocalTransactionListener`，并展示测试通过的日志。
画面 3: 在 PDF 文档中，展示 `TransactionListenerImpl` 类中 `executeLocalTransaction` 方法的 `try` 块，包含打印“执行操作1”和“执行操作2”的语句。
画面 4: 在 IntelliJ IDEA 中，显示 `TransactionListenerImpl.java` 文件，其中 `executeLocalTransaction` 方法的注释和部分代码，包括“执行具体的业务逻辑”和“用户A账户减500元”、“用户B账户加500元”等业务逻辑。
画面 5: 在 IntelliJ IDEA 中，显示 `TransactionListenerImpl.java` 文件，其中 `executeLocalTransaction` 方法的 `try` 块和 `catch` 块，包含返回 `COMMIT` 或 `ROLLBACK` 的语句。
画面 6: 在 IntelliJ IDEA 中，显示 `TransactionListenerImpl.java` 文件，其中 `executeLocalTransaction` 方法的注释和部分代码，包括“执行业务逻辑”和“@Override”等。
画面 7: 在 IntelliJ IDEA 中，显示 `SpringTransactionProducer.java` 文件，其中定义了 `@Autowired private RocketMQTemplate rocketMQTemplate;`，并展示发送消息的 `sendMsg` 方法。
画面 8: 在 IntelliJ IDEA 中，显示 `SpringConsumer.java` 文件，其中 `@RocketMQMessageListener` 注解配置了 `topic` 和 `consumerGroup`，并展示 `onMessage` 方法。
画面 9: 在 IntelliJ IDEA 中，显示 `SpringConsumer.java` 文件，其中 `@RocketMQMessageListener` 注解配置了 `topic` 和 `consumerGroup`，并展示 `onMessage` 方法。
画面 10: 在 IntelliJ IDEA 中，显示 `TestSpringRocketMQ.java` 文件，其中 `sendMsg` 方法发送了“我的第2个SpringRocketMQ消息！”，并展示终端日志显示“收到消息 -> 第1个Spring事务消息”。
画面 11: 在 IntelliJ IDEA 中，显示 `TestSpringRocketMQ.java` 文件，其中 `sendMsg` 方法发送了“第3个Spring事务消息”，并展示终端日志显示“执行操作1”、“执行操作2”、“发送消息成功”。
画面 12: 在 IntelliJ IDEA 中，显示 `TestSpringRocketMQ.java` 文件，其中定义了 `testSendMsg` 和 `testSendMsg2` 两个测试方法。
画面 13: 在 IntelliJ IDEA 中，显示 `TestSpringRocketMQ.java` 文件，其中 `testSendMsg2` 方法的 `catch` 块，包含打印异常栈信息的语句。
画面 14: 展示 PDF 文档中“3.8.1. 定义TransactionListenerImpl”章节，介绍事务消息的定义。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package cn.itcast.rocketmq.spring.transaction;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.core.RocketMQLocalTransactionState;
import org.apache.rocketmq.spring.support.RocketMQHeaders;
import org.springframework.messaging.Message;
import java.util.HashMap;
@RocketMQTransactionListener(txProducerGroup = "myTransactionGroup")
public class TransactionListenerImpl implements RocketMQLocalTransactionListener {
    private static Map<String, RocketMQLocalTransactionState> STATE_MAP = new HashMap<>();
    @Override
    public RocketMQLocalTransactionState executeLocalTransaction(Message message, Object o) {
```

画面 2:
```java
class TransactionListenerImpl implements RocketMQLocalTransactionListener {
```

画面 3:
```java
@Override
public RocketMQLocalTransactionState executeLocalTransaction(Message message, Object o) {
    String transId = (String)message.getHeaders().get(RocketMQHeaders.TRANSACTION_ID);
    try {
        System.out.println("执行操作1");
        Thread.sleep(500);
        System.out.println("执行操作2");
        Thread.sleep(800);
        STATE_MAP.put(transId, RocketMQLocalTransactionState.COMMIT);
        return RocketMQLocalTransactionState.COMMIT;
    } catch (Exception e) {
        e.printStackTrace();
        STATE_MAP.put(transId, RocketMQLocalTransactionState.ROLLBACK);
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面 4:
```java
/**
 * 执行具体的业务逻辑
 * @param msg 发送的消息对象
 * @param arg
 * @return
 */
@Override
public LocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    System.out.println("用户A账户减500元。");
    Thread.sleep(1000);
    System.out.println("用户B账户加500元。");
    Thread.sleep(800);
    STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.COMMIT);
    return LocalTransactionState.COMMIT;
}
```

画面 5:
```java
@Override
public RocketMQLocalTransactionState executeLocalTransaction(Message message, Object o) {
    String transId = (String)message.getHeaders().get(RocketMQHeaders.TRANSACTION_ID);
    try {
        System.out.println("执行操作1");
        Thread.sleep(500);
        System.out.println("执行操作2");
        Thread.sleep(800);
        STATE_MAP.put(transId, RocketMQLocalTransactionState.COMMIT);
        return RocketMQLocalTransactionState.COMMIT;
    } catch (Exception e) {
        e.printStackTrace();
        STATE_MAP.put(transId, RocketMQLocalTransactionState.ROLLBACK);
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面 6:
```java
import java.util.Map;
@RocketMQTransactionListener(txProducerGroup = "myTransactionGroup")
public class TransactionListenerImpl implements RocketMQLocalTransactionListener {
    private static Map<String, LocalTransactionState> STATE_MAP = new HashMap<>();
    /**
     * 执行业务逻辑
     * @param message
     * @param arg
     * @return
     */
    @Override
    public LocalTransactionState executeLocalTransaction(Message message, Object arg) {
        try {
            System.out.println("执行操作1");
            Thread.sleep(500);
            System.out.println("执行操作2");
            Thread.sleep(800);
            STATE_MAP.put(message.getTransactionId(), LocalTransactionState.COMMIT);
            return LocalTransactionState.COMMIT;
        } catch (Exception e) {
            e.printStackTrace();
            STATE_MAP.put(message.getTransactionId(), LocalTransactionState.ROLLBACK);
            return LocalTransactionState.ROLLBACK;
        }
    }
}
```

画面 7:
```java
package cn.itcast.rocketmq.spring.transaction;
import ...
@Component
public class SpringTransactionProducer {
    @Autowired
    private RocketMQTemplate rocketMQTemplate;
    /**
     * 发送消息
     * @param topic
     * @param msg
     */
    public void sendMsg(String topic, String msg) {
        Message message = MessageBuilder.withPayload(msg).build();
        //myTransactionGroup定义
        this.rocketMQTemplate.sendMessageInTransaction(txProducerGroup: "myTransactionGroup",
                topic,
                message,
                null);
    }
}
```

画面 8:
```java
package cn.itcast.rocketmq.spring.transaction;
import ...
@Component
@RocketMQMessageListener(topic = "my-topic",
        consumerGroup = "haoke-consumer",
        selectorExpression = "")
public class SpringConsumer implements RocketMQListener<String> {
    @Override
    public void onMessage(String msg) {
        System.out.println("接收到消息 -> " + msg);
    }
}
```

画面 9:
```java
package cn.itcast.rocketmq.spring.transaction;
import ...
@Component
@RocketMQMessageListener(topic = "spring-tx-my-topic",
        consumerGroup = "haoke-consumer",
        selectorExpression = "")
public class SpringConsumer implements RocketMQListener<String> {
    @Override
    public void onMessage(String msg) {
        System.out.println("接收到消息 -> " + msg);
    }
}
```

画面 10:
```java
// TestSpringRocketMQ.java
public class TestSpringRocketMQ {
    @Test
    public void testSendMsg() {
        String msg = "我的第2个SpringRocketMQ消息！";
        this.springProducer.sendMsg(topic: "spring-my-topic", msg);
        System.out.println("发送成功");
    }
}
```

画面 11:
```java
// TestSpringRocketMQ.java
public class TestSpringRocketMQ {
    @Test
    public void testSendMsg2() {
        this.springTransactionProducer.sendMsg(topic: "spring-tx-my-topic", msg);
    }
}
```

画面 12:
```java
// TestSpringRocketMQ.java
@Test
public void testSendMsg() {
    String msg = "我的第2个SpringRocketMQ消息！";
    this.springProducer.sendMsg(topic: "spring-my-topic", msg);
    System
