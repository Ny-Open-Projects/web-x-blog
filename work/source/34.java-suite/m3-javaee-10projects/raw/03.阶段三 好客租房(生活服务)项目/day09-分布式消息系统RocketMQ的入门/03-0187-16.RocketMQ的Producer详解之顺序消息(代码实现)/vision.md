# 画面线理解：16.RocketMQ的Producer详解之顺序消息（代码实现）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\16.RocketMQ的Producer详解之顺序消息（代码实现）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:34, 04:16, 05:53, 07:20, 08:18, 09:13, 10:03, 10:31, 11:01, 11:54, 12:23, 13:33, 16:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:04:07

1) 这一组画面整体在讲如何使用 RocketMQ 的 Java 客户端实现消息的生产和消费，包括代码编写、项目结构配置和消息发送与接收的调试过程。

2) 按时间顺序列出每张画面的要点：
画面1：展示 RocketMQ 生产者代码，定义了 OrderProducer 类，设置 NameServer 地址并启动生产者，循环发送 100 条消息到主题 "haoke_order_topic"。
画面2：展示 IntelliJ IDEA 的 Project Structure 设置，将 src/main/java 设置为 Source Root，target 设置为 Excluded Folders。
画面3：展示 RocketMQ 客户端源码中 MessageQueueSelector 接口的定义，用于选择消息队列。
画面4：展示 OrderConsumer 类的代码，创建 DefaultMQPushConsumer，设置 NameServer 地址、订阅主题，注册消息监听器并启动消费者。
画面5：展示 OrderProducer.java 中的 send 方法，使用 RemotingHelper.DEFAULT_CHARSET 编码消息体，并根据消息队列数量进行轮询发送。
画面6：展示终端输出，显示发送的消息包含时间戳、出生主机、存储时间戳、存储主机等信息。
画面7：展示 EditPlus 中的消费日志，显示多个线程接收消息，包含队列 ID、存储大小、偏移量等信息。
画面8：展示 EditPlus 中的消费日志，显示消息的 commitLogOffset、bodyCRC、reconsumeTimes 等详细信息。
画面9：展示 EditPlus 中的消费日志，显示多个线程接收消息，包含队列 ID、存储大小、偏移量等信息。
画面10：展示 OrderConsumer.java 中的 consumeMessage 方法，用于处理接收到的消息。
画面11：展示 OrderConsumer.java 中的 consumeMessage 方法，显示消息体的字节码和字符集信息。
画面12：展示 OrderConsumer.java 中的 consumeMessage 方法，显示消息体的字符集为 UTF-8。
画面13：展示 OrderProducer.java 中的 send 方法，使用 RemotingHelper.DEFAULT_CHARSET 编码消息体，并根据消息队列数量进行轮询发送。
画面14：展示 PDF 文档中的架构图，显示 Producer 向两个 Broker（BrokerA 和 BrokerB）发送消息，BrokerA 和 BrokerB 分别向 Consumer 发送消息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
package cn.itcast.rocketmq.order;
import org.apache.rocketmq.client.producer.DefaultMQProducer;
import org.apache.rocketmq.client.producer.SendResult;
import org.apache.rocketmq.common.message.Message;
import org.apache.rocketmq.remoting.common.RemotingHelper;

public class OrderProducer {
    public static void main(String[] args) throws Exception{
        DefaultMQProducer producer = new DefaultMQProducer("HAOKE_ORDER_PRODUCER");
        producer.setNamesrvAddr("172.16.55.185:9876");
        producer.start();
        for (int i = 0; i < 100; i++) {
            String msgStr = "Order --> " + i; // 模拟生成订单id
            int orderId = i % 10; // 模拟生成订单id
            Message message = new Message("haoke_order_topic", "ORDER_MSG", msgStr.getBytes(RemotingHelper.DEFAULT_CHARSET));
            SendResult sendResult = producer.send(message, (mq, msg, arg) -> {
                Integer id = (Integer) arg;
                int index = id % mq.size();
                return mq.get(index);
            }, orderId);
            System.out.println(sendResult);
        }
    }
}
```

画面2：
```
Project Structure
Name: itcast-rocketmq
Language level: 8 (Lambdas, type annotations etc.)
Mark as: Sources
Sources
src
target
```

画面3：
```java
package org.apache.rocketmq.client.producer;
import ...
public interface MessageQueueSelector {
    MessageQueue select(final List<MessageQueue> mqs, final Message msg, final Object arg);
}
```

画面4：
```java
import ...
public class OrderConsumer {
    public static void main(String[] args) throws Exception {
        DefaultMQPushConsumer consumer = new DefaultMQPushConsumer("HAOKE_ORDER_CONSUMER");
        consumer.setNamesrvAddr("172.16.55.185:9876");
        consumer.subscribe("haoke_order_topic", subExpression: "*");
        consumer.registerMessageListener(new MessageListenerOrderly() {
            @Override
            public ConsumeOrderlyStatus consumeMessage(List<MessageExt> msgs, ConsumeOrderlyContext context) {
                System.out.println(Thread.currentThread().getName() + " Receive New Messages: " + msgs);
                return ConsumeOrderlyStatus.SUCCESS;
            }
        });
        consumer.start();
    }
}
```

画面5：
```java
producer.start();
for (int i = 0; i < 100; i++) {
    String msgStr = "Order --> " + i; // 模拟生成订单id
    int orderId = i % 10; // 模拟生成订单id
    Message message = new Message("haoke_order_topic", "ORDER_MSG", msgStr.getBytes(RemotingHelper.DEFAULT_CHARSET));
    SendResult sendResult = producer.send(message, (mq, msg, arg) -> {
        Integer id = (Integer) arg;
        int index = id % mq.size();
        return mq.get(index);
    }, orderId);
    System.out.println(sendResult);
}
```

画面6：
```
nTimestamp=154522043435, bornHost=/172.16.55.180:9899, storeTimestamp=154522043371, storeHost=/172.16.55.180:9899,
nTimestamp=154522043435, bornHost=/172.16.55.180:9899, storeTimestamp=154522043371, storeHost=/172.16.55.180:9899,
nTimestamp=154522043435, bornHost=/172.16.55.180:9899, storeTimestamp=154522043371, storeHost=/172.16.55.180:9899,
...
```

画面7：
```
ConsumeMessageThread_3 Receive New Messages: (MessageExt [queueId=0, storesize=187, queueOffset=23, sysFlag=1, ...
ConsumeMessageThread_3 Receive New Messages: (MessageExt [queueId=0, storesize=187, queueOffset=26, sysFlag=1, ...
ConsumeMessageThread_3 Receive New Messages: (MessageExt [queueId=0, storesize=187, queueOffset=29, sysFlag=1, ...
...
ConsumeMessageThread_1 Receive New Messages: (MessageExt [queueId=2, storesize=187, queueOffset=11, sysFlag=0, ...
ConsumeMessageThread_1 Receive New Messages: (MessageExt [queueId=2, storesize=187, queueOffset=15, sysFlag=0, ...
ConsumeMessageThread_1 Receive New Messages: (MessageExt [queueId=2, storesize=187, queueOffset=19, sysFlag=0, ...
```

画面8：
```
00347ED, commitLogOffset=214925, bodyCRC=2054501425, reconsumeTimes=0, preparedTransactionOffset=0, toString()
00347ED, commitLogOffset=216047, bodyCRC=1956407875, reconsumeTimes=0, preparedTransactionOffset=0, toString()
0035051, commitLogOffset=217595, bodyCRC=2099913214, reconsumeTimes=0, preparedTransactionOffset=0, toString()
...
0312E29, commitLogOffset=201465, bodyCRC=375818277, reconsumeTimes=0, preparedTransactionOffset=0, toString()
0312E29, commitLogOffset=201465, bodyCRC=375818277, reconsumeTimes=0, preparedTransactionOffset=0, toString()
0312E29, commitLogOffset=201465, bodyCRC=375818277, reconsumeTimes=0, preparedTransactionOffset=0, toString()
```

画面9：
```
ConsumeMessageThread_3 Receive New Messages: (MessageExt [queueId=0, storesize=187, queueOffset=23, sysFlag=1, ...
ConsumeMessageThread_3 Receive New Messages: (MessageExt [queueId=0, storesize=187, queueOffset=26, sysFlag=1, ...
ConsumeMessageThread_3 Receive New Messages: (Message
