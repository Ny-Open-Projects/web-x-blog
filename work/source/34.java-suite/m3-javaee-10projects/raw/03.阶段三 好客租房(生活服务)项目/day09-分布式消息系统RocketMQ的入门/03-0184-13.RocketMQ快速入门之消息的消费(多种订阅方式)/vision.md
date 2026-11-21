# 画面线理解：13.RocketMQ快速入门之消息的消费（多种订阅方式）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\13.RocketMQ快速入门之消息的消费（多种订阅方式）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 00:41, 00:56, 01:02, 01:10, 01:28, 01:41, 02:00, 02:13, 02:36, 02:50, 03:28, 03:47, 03:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:02:17

1) 这一组画面整体在讲如何使用 RocketMQ 的 Java 客户端实现消息的生产和消费，重点演示了基于标签（tag）的消息过滤订阅机制。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 ConsumerDemo.java 中的 subscribe 方法，用于订阅主题和订阅表达式，支持通配符“*”和标签过滤。
画面2: 展示 ConsumerDemo.java 中的 main 方法，创建消费者实例并订阅主题“my-topic”，使用通配符“*”接收所有消息。
画面3: 展示 SyncProducer.java 中的 main 方法，创建生产者实例并发送消息，消息主题为“my-topic”，标签为“mytag”。
画面4: 展示 ConsumerDemo.java 中的 main 方法，修改订阅表达式为“add”，仅接收标签为“add”的消息。
画面5: 展示 SyncProducer.java 中的 main 方法，发送标签为“mytag”的消息。
画面6: 展示 SyncProducer.java 中的 main 方法，发送标签为“add”的消息，终端输出消息ID、消息队列和发送状态。
画面7: 展示 SyncProducer.java 中的 main 方法，发送标签为“add”的消息，终端输出消息ID、消息队列和发送状态。
画面8: 展示 SyncProducer.java 中的 main 方法，发送标签为“add”的消息，终端输出消息ID、消息队列和发送状态。
画面9: 展示 ConsumerDemo.java 中的 main 方法，订阅表达式为“add”，终端输出接收到的消息内容。
画面10: 展示 SyncProducer.java 中的 main 方法，右键菜单中选择“Run 'SyncProducer.main()'”运行程序。
画面11: 展示 SyncProducer.java 中的 main 方法，发送标签为“add”的消息，终端输出消息ID、消息队列和发送状态。
画面12: 展示 SyncProducer.java 中的 main 方法，发送标签为“Delete”的消息，终端输出消息ID、消息队列和发送状态。
画面13: 展示《讲义.pdf》第2.5节“消息过滤器”，说明 RocketMQ 支持基于自定义属性进行过滤，过滤表达式类似 SQL 的 WHERE 条件。
画面14: 展示《讲义.pdf》第2.5节“消息过滤器”，展示消息的完整属性结构，包括 topic、properties、UNIQUE_KEY、body、transactionId 等字段。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```java
@Override
public void subscribe(String topic, String subExpression) throws MQClientException {
    this.defaultMQPushConsumerImpl.subscribe(topic, subExpression);
}

/**
 * Subscribe a topic to consuming subscription.
 * @param topic topic to consume.
 * @param fullClassName full class name, must extend org.apache.rocketmq.common.filter.MessageFilter, source code, used UTF-8 file encoding, must be responsible for your own.
 * @param filterClassSource
 */
@Override
public void subscribe(String topic, String fullClassName, String filterClassSource) throws MQClientException {
    this.defaultMQPushConsumerImpl.subscribe(topic, fullClassName, filterClassSource);
}
```

画面2:
```java
public class ConsumerDemo {
    public static void main(String[] args) throws Exception {
        DefaultMQPushConsumer consumer = new DefaultMQPushConsumer(consumerGroup: "haoke-consumer");
        consumer.setNamesrvAddr("172.16.55.185:9876");
        // 订阅消息，接收的是所有消息
        consumer.subscribe("my-topic", "*");
        consumer.registerMessageListener(new MessageListenerConcurrently() {
            public ConsumeConcurrentlyStatus consumeMessage(List<MessageExt> msgs,
                    ConsumeConcurrentlyContext context) {
                try {
                    for (MessageExt msg : msgs) {
                        System.out.println("消息：" + new String(msg.getBody(), charsetName: "UTF-8"));
                    }
                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                }
                return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
            }
        });
    }
}
```

画面3:
```java
import org.apache.rocketmq.common.message.Message;
import org.apache.rocketmq.client.consumer.DefaultMQPushConsumer;
import org.apache.rocketmq.client.producer.DefaultMQProducer;
import org.apache.rocketmq.client.exception.MQClientException;
import org.apache.rocketmq.common.message.MessageExt;

public class SyncProducer {
    public static void main(String[] args) throws Exception {
        DefaultMQProducer producer = new DefaultMQProducer(producerGroup: "haoke");
        producer.setNamesrvAddr("172.16.55.185:9876");
        producer.start();
        //发送消息
        String msg = "我的第一个消息2!";
        Message message = new Message(topic: "my-topic", tags: "mytag", msg.getBytes(charsetName: "UTF-8"));
        SendResult sendResult = producer.send(message);
        System.out.println("消息id：" + sendResult.getMsgId());
        System.out.println("消息队列：" + sendResult.getMessageQueue());
        System.out.println("消息offset值：" + sendResult.getMessageQueue());
    }
}
```

画面4:
```java
import java.io.UnsupportedEncodingException;
import java.util.List;

public class ConsumerDemo {
    public static void main(String[] args) throws Exception {
        DefaultMQPushConsumer consumer = new DefaultMQPushConsumer(consumerGroup: "haoke-consumer");
        consumer.setNamesrvAddr("172.16.55.185:9876");
        // 订阅消息，接收的是所有消息
        consumer.subscribe("my-topic", "*");
        consumer.subscribe("my-topic", "add");
        consumer.registerMessageListener(new MessageListenerConcurrently() {
            public ConsumeConcurrentlyStatus consumeMessage(List<MessageExt> msgs,
                    ConsumeConcurrentlyContext context) {
                try {
                    for (MessageExt msg : msgs) {
                        System.out.println("消息：" + new String(msg.getBody(), charsetName: "UTF-8"));
                    }
                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                }
                return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
            }
        });
    }
}
```

画面5:
```java
import org.apache.rocketmq.common.message.Message;
import org.apache.rocketmq.client.consumer.DefaultMQPushConsumer;
import org.apache.rocketmq.client.producer.DefaultMQProducer;
import org.apache.rocketmq.client.exception.MQClientException;
import org.apache.rocketmq.common.message.MessageExt;

public class SyncProducer {
    public static void main(String[] args) throws Exception {
        DefaultMQProducer producer = new DefaultMQProducer(producerGroup: "haoke");
        producer.setNamesrvAddr("172.16.55.185:9876");
        producer.start();
        //发送消息
        String msg = "我的第一个消息2!";
        Message message = new Message(topic: "my-topic", tags: "mytag", msg.getBytes(charsetName: "UTF-8"));
        SendResult sendResult = producer.send(message);
        System.out.println("消息id：" + sendResult.getMsgId());
        System.out.println("消息队列：" + sendResult.getMessageQueue());
        System.out.println("消息offset值：" + sendResult.getMessageQueue());
    }
}
```

画面6:
```java
import org.apache.rocketmq.common.message.Message;
import org.apache.rocketmq.client.consumer.DefaultMQPushConsumer;
import org.apache.rocketmq.client.producer.DefaultMQProducer;
import org.apache.rocketmq.client.exception.MQClientException;
import org.apache.rocketmq.common.message.MessageExt;

public class SyncProducer {
    public static void main(String[] args) throws Exception {
        DefaultMQProducer producer = new DefaultMQProducer(producerGroup: "haoke");
        producer.setNamesrvAddr("172.16.55.185:9876");
        producer.start();
        //发送消息
        String msg = "我的第一个消息3!";
        Message message = new Message(topic: "my-topic", tags: "mytag", msg.getBytes(charsetName: "UTF-8"));
        SendResult sendResult = producer.send(message);
        System.out.println("消息id：" + sendResult.getMsgId());
        System.out.println("消息队列：" + sendResult.getMessageQueue());
        System.out.println("消息offset值：" + sendResult.getMessageQueue());
    }
}
```

画面7:
```java
import org.apache.rocketmq.common.message.Message;
import org.apache.rocketmq.client.consumer.DefaultMQPushConsumer;
import org.apache.rocketmq.client.producer.DefaultMQProducer;
import org.apache.rocketmq.client.exception.MQClientException;
import org.apache.rocketmq.common.message.MessageExt;

public class SyncProducer {
    public static void main(String[] args) throws Exception {
        DefaultMQProducer producer = new DefaultMQProducer(producerGroup: "haoke");
        producer.setNamesrvAddr("172.16.55.185:9876");
        producer.start();
        //发送消息
        String msg = "我的第一个消息4!";
        Message message = new Message(topic: "my-topic", tags: "add", msg.getBytes(charsetName: "UTF-8"));
        SendResult sendResult = producer.send(message);
        System.out.println("消息id：" + sendResult.getMsgId());
        System.out.println("消息队列：" + sendResult.getMessageQueue());
        System.out.println("消息offset值："
