# 画面线理解：23.RocketMQ的Consumer详解之消息模式（补充）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\23.RocketMQ的Consumer详解之消息模式（补充）【海量资源尽在 ubkz.com】.mp4
- 抽帧：10 帧 @ 00:01, 00:04, 00:05, 00:07, 00:10, 00:16, 00:19, 00:23, 00:24, 00:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:08:16

1) 这一组画面整体在讲 RocketMQ 消息消费的两种模式（集群模式与广播模式）及其在代码中的实现方式。

2) 按时间顺序列出每张画面的要点：
画面 1:
- 展示 PDF 文档中“4.2. 消息模式”章节。
- 介绍 DefaultMQPushConsumer 实现了自动保存 offset 以及实现多个 consumer 的负载均衡。
- 代码示例：`DefaultMQPushConsumer consumer = new DefaultMQPushConsumer("HAOK_E_IN");`
- 说明通过 groupname 将多个 consumer 组在一起时，消息如何分配的问题，引出需要指定消息模式。
- 列出两种模式：集群模式（Cluster）和广播模式（Broadcast）。

画面 2:
- 画面内容与画面 1 基本相同，但光标聚焦在代码行 `DefaultMQPushConsumer consumer = new DefaultMQPushConsumer("HAOK_E_IN");` 上，强调实例化过程。

画面 3:
- 画面内容与画面 1、2 基本相同，但光标移动到代码行 `consumer.setMessagModel(MessageModel.CLUSTERING);` 上，准备讲解集群模式设置。

画面 4:
- 画面内容与画面 3 基本相同，但光标在 `consumer.setMessagModel(MessageModel.CLUSTERING);` 行上，同时下方出现“4.3. 重复消息的解决方案”章节标题，预示接下来的内容。

画面 5:
- 画面内容与画面 4 基本相同，但光标在 `consumer.setMessagModel(MessageModel.CLUSTERING);` 行上，画面底部显示“4.3. 重复消息的解决方案”章节标题。

画面 6:
- 切换到 IDE 界面，展示 RocketMQ 客户端源码 `DefaultMQPushConsumer.java`。
- 代码行：`public class DefaultMQPushConsumer extends ClientConfig implements MQPushConsumer {`
- 注释说明：消费者需要有相同的订阅和 consumerGroup 来实现负载均衡，且需要全局唯一。

画面 7:
- IDE 界面，光标在 `DefaultMQPushConsumer` 类定义上，显示搜索结果“14 matches”。

画面 8:
- IDE 界面，光标聚焦在代码行 `private MessageModel messageModel = MessageModel.CLUSTERING;` 上，高亮显示 `MessageModel` 和 `CLUSTERING`。

画面 9:
- IDE 界面，光标在 `private MessageModel messageModel = MessageModel.CLUSTERING;` 行上，下方显示注释“Consuming point on consumer booting.”。

画面 10:
- 切换到 `ConsumerDemo.java` 文件，展示消费端代码。
- 代码示例：
```java
import java.util.List;
public class ConsumerDemo {
    public static void main(String[] args) throws Exception {
        DefaultMQPushConsumer consumer = new DefaultMQPushConsumer(consumerGroup: "haoke-consumer");
        consumer.setNamesrvAddr("172.16.55.185:9876");
        consumer.subscribe("my-topic", "add || update");
        consumer.setMessageModel(MessageModel.CLUSTERING);
        consumer.registerMessageListener(new MessageListenerConcurrently() {
            public ConsumeConcurrentlyStatus consumeMessage(List<MessageExt> mags, ConsumeConcurrentlyContext context) {
                for (MessageExt mag : mags) {
                    System.out.println("消息：" + new String(mag.getBody(), charsetName: "UTF-8"));
                }
                return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
            }
        });
    }
}
```

3) 画面中出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 1:
```java
//设置姓名
DefaultMQPushConsumer consumer = new DefaultMQPushConsumer("HAOK_E_IN");
```
画面 3:
```java
// 集群模式
consumer.setMessagModel(MessageModel.CLUSTERING);
// 广播模式
consumer.setMessagModel(MessageModel.BROADCASTING);
```
画面 6:
```java
public class DefaultMQPushConsumer extends ClientConfig implements MQPushConsumer {
    ...
    protected final transient DefaultMQPushConsumerImpl defaultMQPushConsumerImpl;
    ...
    private String consumerGroup;
    ...
    private MessageModel messageModel = MessageModel.CLUSTERING;
```
画面 10:
```java
import java.util.List;
public class ConsumerDemo {
    public static void main(String[] args) throws Exception {
        DefaultMQPushConsumer consumer = new DefaultMQPushConsumer(consumerGroup: "haoke-consumer");
        consumer.setNamesrvAddr("172.16.55.185:9876");
        consumer.subscribe("my-topic", "add || update");
        consumer.setMessageModel(MessageModel.CLUSTERING);
        consumer.registerMessageListener(new MessageListenerConcurrently() {
            public ConsumeConcurrentlyStatus consumeMessage(List<MessageExt> mags, ConsumeConcurrentlyContext context) {
                for (MessageExt mag : mags) {
                    System.out.println("消息：" + new String(mag.getBody(), charsetName: "UTF-8"));
                }
                return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
            }
        });
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
- 画面 1、2、3、4、5: PPT 标题为“4.2. 消息模式”，内容包含“集群模式”和“广播模式”的定义。
- 画面 4、5: PPT 标题为“4.3. 重复消息的解决方案”，内容包含“造成消息重复的根本原因是：网络不达，只要通过网络发数据，就无法避免这个问题”。
- 无架构图或流程图。

5) 无其他内容。
