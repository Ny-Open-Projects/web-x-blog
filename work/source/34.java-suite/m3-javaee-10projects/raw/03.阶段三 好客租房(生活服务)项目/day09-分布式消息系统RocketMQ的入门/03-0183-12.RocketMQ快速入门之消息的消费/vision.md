# 画面线理解：12.RocketMQ快速入门之消息的消费

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\12.RocketMQ快速入门之消息的消费【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:27, 01:09, 01:34, 02:37, 03:25, 04:02, 04:32, 05:56, 06:15, 06:45, 07:11, 07:28, 07:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:01:27

1) 这一组画面整体在讲如何使用 RocketMQ Java 客户端编写异步和同步消息的生产者与消费者程序。

2) 按时间顺序列出每张画面的要点：
画面 1:
要点：展示异步生产者代码的结尾部分，包含异常处理和关闭生产者的方法。终端显示消息发送成功，包含消息ID、队列信息等。
代码：
```java
public void onException(Throwable e) {
    System.out.println("消息发送失败!" + e);
}
producer.shutdown();
```

画面 2:
要点：展示消费者类的包声明和类定义，IDE提示“DefaultMQ”相关类。
代码：
```java
package cn.itcast.rocketmq.consumer;
public class ConsumerDemo {
```

画面 3:
要点：在消费者类的 main 方法中，IDE提示“DefaultMQ”类，但尚未选择。
代码：
```java
public static void main(String[] args) {
    Defaultmq
}
```

画面 4:
要点：在消费者类中导入 RocketMQ 消费者类，并创建 DefaultMQPushConsumer 实例。
代码：
```java
import org.apache.rocketmq.client.consumer.DefaultMQPushConsumer;
public class ConsumerDemo {
    public static void main(String[] args) {
        DefaultMQPushConsumer consumer = new DefaultMQPushConsumer(consumerGroup: "haoke-consumer");
    }
}
```

画面 5:
要点：在消费者类中，IDE提示 DefaultMQPushConsumer 的方法，选择 subscribe 方法。
代码：
```java
consumer.subscribe(topic, subExpression);
```

画面 6:
要点：在消费者类中，设置 NameServer 地址并订阅主题。
代码：
```java
consumer.setNamesrvAddr("172.16.55.185:9876");
consumer.subscribe(topic: "my-topic", subExpression: "*");
```

画面 7:
要点：在消费者类中，注册消息监听器并定义消费方法。
代码：
```java
consumer.registerMessageListener(new MessageListenerConcurrently() {
    public ConsumeConcurrentlyStatus consumeMessage(List<MessageExt> msgs, ConsumeConcurrentlyContext context) {
        return null;
    }
});
```

画面 8:
要点：在消费者类中，消费方法内使用 for 循环遍历消息并打印内容。
代码：
```java
for (MessageExt msg : msgs) {
    System.out.println("消息:" + new String(msg.getBody(), charsetName: "UTF-8"));
}
```

画面 9:
要点：在消费者类中，消费方法内添加 try-catch 块处理编码异常。
代码：
```java
try {
    for (MessageExt msg : msgs) {
        System.out.println("消息:" + new String(msg.getBody(), charsetName: "UTF-8"));
    }
} catch (UnsupportedEncodingException e) {
    e.printStackTrace();
}
```

画面 10:
要点：在消费者类中，消费方法内添加返回值，启动消费者。
代码：
```java
return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
consumer.start();
```

画面 11:
要点：终端显示消费者启动后，打印出队列信息。
代码：
```text
xt [queueId=6, storeSize=185, queueOffset=0, sysFlag=0, bornTimestamp=165205662011, bornHost=/172.16.55
xt [queueId=3, storeSize=194, queueOffset=0, sysFlag=0, bornTimestamp=1545205662128, bornHost=/172.16.55
```

画面 12:
要点：展示同步生产者代码，右键菜单中选择“Run 'SyncProducer.main()'”。
代码：
```java
public static void main(String[] args) throws Exception {
    DefaultMQProducer producer = new DefaultMQProducer(producerGroup: "haoke");
    producer.setNamesrvAddr("172.16.55.185:9876");
    producer.start();
    String msg = "我的第一个消息2!";
    Message message = new Message(topic: "my-topic", tags: "mytag", msg.getBytes(charsetName: "UTF-8"));
    SendResult sendResult = producer.send(message);
    System.out.println("消息id:" + sendResult.getMsgId());
    System.out.println("消息队列:" + sendResult.getMessageQueue());
    System.out.println("消息offset值:" + sendResult.getQueueOffset());
    System.out.println(sendResult);
}
```

画面 13:
要点：终端显示同步生产者发送消息成功，包含消息ID、队列信息等。
代码：
```text
SendResult [sendStatus=SEND_OK, msgId=AC1037B418F016B4AAC260327C6C0000, offsetMsgId=AC1037B900002A9F0000
Process finished with exit code 0
```

画面 14:
要点：展示 PDF 文档中关于消费消息的代码示例。
代码：
```java
import org.apache.rocketmq.client.consumer.DefaultMQPushConsumer;
import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyContext;
import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyStatus;
import org.apache.rocketmq.client.consumer.listener.MessageListenerConcurrently;
import org.apache.rocketmq.client.exception.MQClientException;
import org.apache.rocketmq.common.message.MessageExt;
import java.io.UnsupportedEncodingException;
import java.util.List;
public class ConsumerDemo {
```
