# 画面线理解：10.RocketMQ快速入门之发送消息（同步）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\10.RocketMQ快速入门之发送消息（同步）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:42, 01:05, 01:29, 01:55, 02:17, 03:01, 04:00, 04:47, 05:03, 06:16, 06:50, 09:10, 09:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:00:26

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 RocketMQ Java 客户端创建 Topic、发送同步消息，并查看消息在控制台中的状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 TopicDemo.java 中创建 Topic 的代码，包括设置 broker 名称、topic 名称和 queue 数量，并打印“topic创建成功!”。
画面 2: 展示项目结构，当前选中文件为 SyncProducer.java。
画面 3: 展示 SyncProducer.java 中创建 DefaultMQProducer 的代码，设置 producerGroup。
画面 4: 展示在 main 方法中声明并初始化 DefaultMQProducer。
画面 5: 展示在 main 方法中调用 producer.send() 发送消息，并调用 producer.shutdown()。
画面 6: 展示 Message.java 类的源码，定义了 Message 的构造函数和属性。
画面 7: 展示 TopicDemo.java 中设置 NameServer 地址的代码。
画面 8: 展示在 SyncProducer.java 中调用 producer.send() 并获取 SendResult。
画面 9: 展示在 SyncProducer.java 中发送消息并打印消息 ID、队列、offset 等信息。
画面 10: 展示在 SyncProducer.java 中发送消息并打印消息 ID、队列、offset 等信息，代码与画面 9 相同。
画面 11: 展示 RocketMQ 控制台中 Topic “my-topic” 的队列状态，显示各队列的最小位点、最大位点和上次更新时间。
画面 12: 展示 PDF 文档中关于 RocketMQ 消息属性的说明，包括 Topic、Body、Tags、Keys、Flag、DelayTimeLevel、WaitStoreMsgOK 等字段的默认值和说明。
画面 13: 展示在终端中运行 SyncProducer 后的输出，显示 SendStatus 为 SEND_OK，消息 ID、offset 等信息。
画面 14: 展示 PDF 文档中关于 SyncProducer 类的代码，包括设置 NameServer 地址、发送消息并打印消息状态、消息 ID、队列、offset 等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
// 创建topic, 参数分别是: broker的名称, topic的名称, queue的数量
producer.createTopic(key: "broker_haoke_im", newTopic: "my-topic", queueNum: 8);
System.out.println("topic创建成功!");
producer.shutdown()
```

画面 3:
```java
package cn.itcast.rocketmq.sendmsg;
import org.apache.rocketmq.client.producer.DefaultMQProducer;
public class SyncProducer {
    public static void main(String[] args) {
        DefaultMQProducer producer = new DefaultMQProducer(producerGroup: "haoke");
```

画面 4:
```java
public static void main(String[] args) throws Exception {
```

画面 5:
```java
Message msg = new Message(topic: "my-topic", tags: "mytag", msg.getBytes(charsetName: "UTF-8"));
producer.send(msg);
```

画面 6:
```java
public Message(String topic, byte[] body) {
    this(topic, "", "", 0, body, true);
}
public Message(String topic, String tags, String keys, int flag, byte[] body, boolean waitStoreMsg) {
    this.topic = topic;
    this.tags = tags;
    this.keys = keys;
    this.flag = flag;
    this.body = body;
    this.waitStoreMsg = waitStoreMsg;
}
```

画面 7:
```java
producer.setNamesrvAddr("172.16.55.185:9876");
```

画面 8:
```java
SendResult sendResult = producer.send(message);
System.out.println("消息ID：" + sendResult.getMsgId());
System.out.println("消息队列：" + sendResult.getMessageQueue());
System.out.println("消息offset值：" + sendResult.getQueueOffset());
System.out.println(sendResult);
```

画面 9:
```java
String msg = "我的第一个消息!";
Message message = new Message(topic: "my-topic", tags: "mytag", msg.getBytes(charsetName: "UTF-8"));
SendResult sendResult = producer.send(message);
System.out.println("消息ID：" + sendResult.getMsgId());
System.out.println("消息队列：" + sendResult.getMessageQueue());
System.out.println("消息offset值：" + sendResult.getQueueOffset());
System.out.println(sendResult);
```

画面 10:
```java
String msg = "我的第一个消息!";
Message message = new Message(topic: "my-topic", tags: "mytag", msg.getBytes(charsetName: "UTF-8"));
SendResult sendResult = producer.send(message);
System.out.println("消息ID：" + sendResult.getMsgId());
System.out.println("消息队列：" + sendResult.getMessageQueue());
System.out.println("消息offset值：" + sendResult.getQueueOffset());
System.out.println(sendResult);
```

画面 13:
```
SendStatus: SEND_OK, msgId=AC1037B41C4418B4AAC260161DAE0000, offsetMsgId=AC1037B900002A9F0000
```

画面 14:
```java
package cn.itcast.rocketmq;
import org.apache.rocketmq.client.producer.DefaultMQProducer;
import org.apache.rocketmq.client.producer.SendResult;
import org.apache.rocketmq.common.message.Message;
import org.apache.rocketmq.remoting.common.RemotingHelper;
public class SyncProducer {
    public static void main(String[] args) throws Exception {
        DefaultMQProducer producer = new DefaultMQProducer(producerGroup: "HAOKE_IM");
        producer.setNamesrvAddr("172.16.55.185:9876");
        producer.start();
        String msg = "用户A发送消息给用户B";
        Message msg = new Message("haoke_in_topic", "SEND_MSG", msg.getBytes(RemotingHelper.DEFAULT_CHARSET));
        SendResult sendResult = producer.send(msg);
        System.out.println("消息状态：" + sendResult.getSendStatus());
        System.out.println("消息ID：" + sendResult.getMsgId());
        System.out.println("消息队列：" + sendResult.getMessageQueue());
        System.out.println("消息offset：" + sendResult.getQueueOffset());
        producer.shutdown();
    }
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 12: PDF 文档中表格数据：
| 字段名 | 默认值 | 说明 |
| :--- | :--- | :--- |
| Topic | null | 必填，线下环境不需要申请，线上环境需要申请后才能使用 |
| Body | null | 必填，二进制形式，序列化由应用决定，Producer 与 Consumer 要协商好序列化形式 |
| Tags | null | 速填，类似于 Gmail 为每封邮件设置的标签，方便服务器过滤使用。目前只支持每个消息设置一个 tag，也可以类似为 Notify 的 MessageType 概念 |
| Keys | null | 速填，代表这条消息的业务关键词，服务器会根据 keys 做哈希索引，设置后，可以在 Console 系统根据 Topic、Keys 查询消息，由于是哈希索引，请尽可能保证 key 唯一，例如订单号、商品 Id 等。 |
| Flag | 0 | 选填，完全由应用来设置，RocketMQ 不做干预 |
| DelayTimeLevel | 0 | 选填，消息延迟级别，0 表示不延时，大于 0 会延时特定的时间才会被消费 |
| WaitStoreMsgOK | TRUE | 选填，表示消息是否在服务器落盘后才返回响应。 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
