# 画面线理解：22.RocketMQ的Consumer详解之消息模式（集群和广播模式）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\22.RocketMQ的Consumer详解之消息模式（集群和广播模式）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:29, 00:42, 00:52, 01:16, 01:57, 02:41, 02:54, 04:09, 04:53, 04:59, 05:17, 05:29, 05:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:07:45

1) 这一组画面整体在讲 RocketMQ 消息消费的两种模式：集群模式和广播模式，以及如何通过设置 messageModel 来切换。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中“4.2. 消息模式”章节，介绍 DefaultMQPushConsumer 实现自动保存 offset 以实现多个 consumer 的负载均衡，并引出需要指定消息模式的问题。
画面2：展示 IntelliJ IDEA 中 TransactionListenerImpl.java 文件，代码中包含事务状态的处理逻辑，如 STATE_MAP.put 和 return LocalTransactionState.COMMIT_MESSAGE。
画面3：展示绘图软件中“推送模式：push”和“拉取模式：轮询 pull”的概念图，左侧为发送端，右侧为消费者。
画面4：展示 RocketMQ 的架构图，包含 nameserver 集群、producer、broker 集群、consumer 和 topic 消息队列。
画面5：展示绘图软件中“推送模式：push”和“拉取模式：轮询 pull”的概念图，左侧为消费者，右侧为消息系统。
画面6：展示绘图软件中“消费者1”、“消费者2”、“消费者3”三个消费者框，表示同一组消费者。
画面7：展示 PDF 文档中“4.2. 消息模式”章节，介绍集群模式和广播模式，以及设置 messageModel 的代码。
画面8：展示 PDF 文档中“4.3. 重复消息的解决方案”章节，同时显示了“无标题 - 画图”窗口。
画面9：展示绘图软件中“1000条消息”从“消息系统”分发到“消费者1”、“消费者2”、“消费者3”的图示，标注“同一个组”。
画面10：展示 IntelliJ IDEA 中 ConsumerDemo.java 文件，代码中包含 consumer.setConsumerGroup 和 consumer.subscribe 的调用。
画面11：展示 IntelliJ IDEA 中 DefaultMQPushConsumer.java 文件，代码中包含 setMessageModel 方法的定义。
画面12：展示 IntelliJ IDEA 中 LocalTransactionState.java 文件，代码中包含 LocalTransactionState 枚举类的定义。
画面13：展示 IntelliJ IDEA 中 ConsumerDemo.java 文件，代码中包含 consumer.setMessageModel(MessageModel.CLUSTERING) 和 try-catch 块。
画面14：展示 PDF 文档中“4.2. 消息模式”章节，介绍集群模式和广播模式，以及设置 messageModel 的代码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
//设置组名
DefaultMQPushConsumer consumer = new DefaultMQPushConsumer("HAOKE_M_");
```
画面2：
```java
STATE_MAP.put(mag.getTransactionId(), LocalTransactionState.COMMIT_MESSAGE);
return LocalTransactionState.COMMIT_MESSAGE;
```
画面7：
```java
// 集群模式
consumer.setMessageModel(MessageModel.CLUSTERING);
// 广播模式
consumer.setMessageModel(MessageModel.BROADCASTING);
```
画面10：
```java
import java.util.List;

public class ConsumerDemo {
    public static void main(String[] args) throws Exception {
        DefaultMQPushConsumer consumer = new DefaultMQPushConsumer(consumerGroup: "haoke-consumer");
        consumer.setNamesrvAddr("172.16.55.185:9876");
        // 订阅消息，接收的是所有消息
        consumer.subscribe("my-topic", "*");
        consumer.subscribe(topic: "my-topic", subExpression: "add || update");
        consumer.start();
    }
}
```
画面11：
```java
public void setMessageModel(MessageModel messageModel) {
    this.messageModel = messageModel;
}
```
画面13：
```java
consumer.setMessageModel(MessageModel.CLUSTERING);
public ConsumeConcurrentlyStatus consumeMessage(List<MessageExt> mags, ConsumeConcurrentlyContext context) {
    try {
        for (MessageExt mag : mags) {
            System.out.println("消息：" + new String(mag.getBody(), charsetName: "UTF-8"));
        }
    } catch (UnsupportedEncodingException e) {
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面3：标题未显示，图示为“推送模式：push”和“拉取模式：轮询 pull”，“发送短信的系统”指向“消息系统”，“消息系统”指向“消费者”。
画面4：标题未显示，图示为 RocketMQ 架构图，包含“nameserver 集群”、“producer”、“broker 集群”、“consumer”、“broker”、“topic”和“Message queue”。
画面5：标题未显示，图示为“推送模式：push”和“拉取模式：轮询 pull”，“消费者”指向“消息系统”。
画面6：标题未显示，图示为“消费者1”、“消费者2”、“消费者3”三个消费者框。
画面9：标题未显示，图示为“1000条消息”从“消息系统”分发到“消费者1”、“消费者2”、“消费者3”，标注“同一个组”。
画面10：标题未显示，代码中包含 consumer.setConsumerGroup 和 consumer.subscribe 的调用。
画面11：标题未显示，代码中包含 setMessageModel 方法的定义。
画面12：标题未显示，代码中包含 LocalTransactionState 枚举类的定义。
画面13：标题未显示，代码中包含 consumer.setMessageModel(MessageModel.CLUSTERING) 和 try-catch 块。

5) 无其他内容。
