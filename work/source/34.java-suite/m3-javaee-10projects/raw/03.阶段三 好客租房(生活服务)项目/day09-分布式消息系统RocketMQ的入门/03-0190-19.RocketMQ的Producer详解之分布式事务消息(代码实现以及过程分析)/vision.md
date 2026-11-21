# 画面线理解：19.RocketMQ的Producer详解之分布式事务消息（代码实现以及过程分析）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\19.RocketMQ的Producer详解之分布式事务消息（代码实现以及过程分析）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:46, 01:54, 03:18, 04:04, 05:36, 06:42, 07:19, 07:55, 09:00, 10:27, 11:38, 12:54, 15:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:05:52

1) 这一组画面整体在讲什么（一句话）：
演示 RocketMQ 事务消息的实现原理与代码示例，包括生产者、事务监听器和消费者三个核心组件的编写与测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 RocketMQ 事务消息的流程图，包含 Local Transaction、MQ Producer、MQ server、MQ Consumer 四个节点，以及 7 个步骤：1. 发送方向 MQ 服务端发送消息；2. MQ Server 将消息持久化成功后，向发方 ACK 确认消息已经发送成功，此时消息为半消息；3. 发送方根据本地事务执行结果向 MQ Server 提交二次确认（Commit 或是 Rollback）；4. 发送方根据本地事务执行结果向 MQ Server 提交二次确认（Commit 或是 Rollback），MQ Server 收到 Commit 状态则半消息可投递，MQ Server 收到 Rollback 状态则删除半消息；5. 在断网或者应用重启的特殊情况下，上述步骤4提交的二次确认最终未到 MQ Server，经过回调后 MQ Server 将对半消息进行操作；6. 发送方在收到消息回查后，需要检查对应消息的本地事务执行的最终结果；7. 发送方根据检查得到的本地事务的最终状态再次提交二次确认，MQ Server 仍按步骤4对半消息进行操作。

画面 2: 展示 OrderProducer.java 代码，用于发送普通消息，包含创建 DefaultMQProducer、设置 NameServer 地址、发送消息、关闭生产者等逻辑。

画面 3: 展示 TransactionProducer.java 代码，用于发送事务消息，包含创建 TransactionMQProducer、设置事务监听器、发送事务消息等逻辑。

画面 4: 展示 TransactionListenerImpl.java 代码中事务状态处理部分，包含根据业务逻辑返回 LocalTransactionState.COMMIT_MESSAGE 或 LocalTransactionState.ROLLBACK_MESSAGE。

画面 5: 展示 TransactionListenerImpl.java 代码，用于执行具体的业务逻辑，包含打印“用户A账户减500元”和“用户B账户加500元”的日志。

画面 6: 展示 TransactionListenerImpl.java 代码，用于执行具体的业务逻辑，包含打印“用户A账户减1000元”和“用户B账户加1000元”的日志。

画面 7: 展示 TransactionListenerImpl.java 代码，用于执行具体的业务逻辑，包含打印“用户A账户减1000元”和“用户B账户加1000元”的日志。

画面 8: 展示 TransactionConsumer.java 代码，用于订阅主题 "pay_topic" 并消费消息。

画面 9: 展示 TransactionConsumer.java 代码，用于消费消息并打印消息体。

画面 10: 展示 TransactionProducer.java 代码，用于发送事务消息，包含设置 NameServer 地址、设置事务监听器、发送事务消息、关闭生产者等逻辑。

画面 11: 展示 TransactionListenerImpl.java 代码中事务状态处理部分，包含根据业务逻辑返回 LocalTransactionState.COMMIT_MESSAGE 或 LocalTransactionState.ROLLBACK_MESSAGE。

画面 12: 展示 TransactionListenerImpl.java 代码，用于执行具体的业务逻辑，包含打印“用户A账户减500元”的日志。

画面 13: 展示 RocketMQ 事务消息的流程图，包含 Local Transaction、MQ Producer、MQ server、MQ Consumer 四个节点，以及 7 个步骤：1. 发送方向 MQ 服务端发送消息；2. MQ Server 将消息持久化成功后，向发方 ACK 确认消息已经发送成功，此时消息为半消息；3. 发送方根据本地事务执行结果向 MQ Server 提交二次确认（Commit 或是 Rollback）；4. 发送方根据本地事务执行结果向 MQ Server 提交二次确认（Commit 或是 Rollback），MQ Server 收到 Commit 状态则半消息可投递，MQ Server 收到 Rollback 状态则删除半消息；5. 在断网或者应用重启的特殊情况下，上述步骤4提交的二次确认最终未到 MQ Server，经过回调后 MQ Server 将对半消息进行操作；6. 发送方在收到消息回查后，需要检查对应消息的本地事务执行的最终结果；7. 发送方根据检查得到的本地事务的最终状态再次提交二次确认，MQ Server 仍按步骤4对半消息进行操作。

画面 14: 展示 PPT 页面，标题为“3.3.8. 测试”，内容为“测试结果：返回commit状态时，消费者能够接收到消息，返回rollback状态时，消费者接受不到消息。”，并切换到“4. consumer详解”章节，其中“4.1. push和pull模式”部分介绍 RocketMQ 中消费者有两种模式：push 模式和 pull 模式。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
public static void main(String[] args) throws Exception {
    DefaultMQProducer producer = new DefaultMQProducer("HAC");
    producer.setNamesrvAddr("172.16.55.185:9876");
    producer.start();
    for (int orderId = 0; orderId < 100; ++orderId) {
        String msgStr = "order" + orderId + ",id=" + orderId;
        Message message = new Message("topic", "haoke_order_topic", tags, msgStr.getBytes(RemotingHelper.DEFAULT_CHARSET));
        SendResult sendResult = producer.send(message, (mqs, msg, arg) -> {
            Integer id = (Integer) arg;
            int index = id % mqs.size();
            return mqs.get(index);
        }, orderId);
        System.out.println(sendResult);
    }
    producer.shutdown();
}
```

画面 3:
```java
package cn.itcast.rocketmq.transaction;

import ...

public class TransactionProducer {
    public static void main(String[] args) throws Exception {
        TransactionMQProducer producer = new TransactionMQProducer("transaction_producer");
        producer.setNamesrvAddr("172.16.55.185:9876");
        // 设置事务监听器
        producer.setTransactionListener(new TransactionListenerImpl());
        producer.start();
        // 发送消息
        Message message = new Message("pay_topic", "用户A给用户B转账500元".getBytes(charsetName: "UTF-8"));
        producer.sendMessageInTransaction(message, arg: null);
        Thread.sleep(millis: 999999);
        producer.shutdown();
    }
}
```

画面 4:
```java
System.out.println("用户B账户加500元.");
STATE_MAP.put(msg.getTransactionId(),
LocalTransactionState.COMMIT_MESSAGE);
// 二次提交确认
return LocalTransactionState.COMMIT_MESSAGE;
} catch (Exception e) {
    e.printStackTrace();
}
STATE_MAP.put(msg.getTransactionId(),
LocalTransactionState.ROLLBACK_MESSAGE);
// 回滚
return LocalTransactionState.ROLLBACK_MESSAGE;
```

画面 5:
```java
package cn.itcast.rocketmq.transaction;

import ...

public class TransactionListenerImpl implements TransactionListener {

    private static Map<String, LocalTransactionState> STATE_MAP = new HashMap<>();

    /**
     * 执行具体的业务逻辑
     * @param msg 发送的消息对象
     * @param arg
     * @return
     */
    @Override
    public LocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        try {
            System.out.println("用户A账户减500元.");
            Thread.sleep(millis: 500); // 模拟调用服务
            System.out.println("用户B账户加500元.");
            Thread.sleep(millis: 800);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return LocalTransactionState.COMMIT_MESSAGE;
    }
}
```

画面 6:
```java
@Override
public LocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    try {
        System.out.println("用户A账户减1000元.");
        Thread.sleep(millis: 500); // 模拟调用服务
        // System.out.println("用户B账户加1000元.");
        System.out.println("用户B账户加1000元.");
        Thread.sleep(millis: 900);
        STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.COMMIT_MESSAGE);
        // 二次提交确认
        return LocalTransactionState.COMMIT_MESSAGE;
    } catch (Exception e) {
        e.printStackTrace();
    }
    STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.ROLLBACK_MESSAGE);
    // 回滚
    return LocalTransactionState.ROLLBACK_MESSAGE;
}
```

画面 8:
```java
package cn.itcast.rocketmq.transaction;

import java.util.List;
public class TransactionConsumer {
    public static void main(String[] args) throws Exception {
        DefaultMQPushConsumer consumer = new DefaultMQPushConsumer("HAC");
        consumer.setNamesrvAddr("172.16.55.185:9876");
        // 订阅topic，接收该主题下的所有消息
        consumer.subscribe
