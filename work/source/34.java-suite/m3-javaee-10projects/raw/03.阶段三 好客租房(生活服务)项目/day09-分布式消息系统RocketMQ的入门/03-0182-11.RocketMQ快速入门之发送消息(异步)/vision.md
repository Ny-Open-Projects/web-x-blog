# 画面线理解：11.RocketMQ快速入门之发送消息（异步）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\11.RocketMQ快速入门之发送消息（异步）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:30, 00:53, 01:14, 01:31, 01:52, 02:20, 03:01, 03:29, 03:43, 04:18, 05:21, 05:37, 05:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:00:53

1) 这一组画面整体在讲如何使用 RocketMQ 的异步消息生产者（AsyncProducer）发送消息，并对比同步生产者，同时展示消息的结构和控制台操作。

2) 按时间顺序列出每张画面的要点：
画面1：展示同步生产者代码，包含设置 NameServer 地址、发送消息、打印发送结果和关闭生产者。
画面2：展示异步生产者类 AsyncProducer 的空框架。
画面3：在 AsyncProducer 类中，开始编写代码，准备使用 DefaultMQProducer。
画面4：展示 DefaultMQProducer 的方法列表，用于配置生产者。
画面5：导入必要的包，创建 DefaultMQProducer 实例并设置 NameServer 地址。
画面6：展示 RocketMQ 消息结构文档，包含 Topic、Body、Tags、Keys、Flag、DelayTimeLevel、WaitStoreMsgOK 等字段及其说明。
画面7：在 AsyncProducer 中，定义消息内容并创建 Message 对象。
画面8：为异步发送添加 SendCallback 回调，并开始编写 onSuccess 方法。
画面9：编写 onSuccess 方法的代码，用于处理发送成功的情况。
画面10：编写 onException 方法，用于处理发送失败的情况。
画面11：在 onException 方法中，打印异常信息，并显示发送失败。
画面12：在浏览器中打开 RocketMQ 控制台，显示消息发送失败的提示。
画面13：在 RocketMQ 控制台的“主题”页面，显示多个消费者组的状态。
画面14：展示文档中关于消费消息的部分，以及代码中 producer.shutdown() 的注释。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
producer.setNamesrvAddr("172.16.55.185:9876");
producer.start();
//发送消息
Message msg = new Message(topic: "my-topic", tags: "mytag", msg.getBytes(charsetName: "UTF-8"));
SendResult sendResult = producer.send(message);
System.out.println("消息ID：" + sendResult.getMessageId());
System.out.println("消息队列：" + sendResult.getMessageQueue());
System.out.println("消息offset值：" + sendResult.getQueueOffset());
System.out.println(sendResult);
producer.shutdown();
```

画面5：
```java
import org.apache.rocketmq.client.producer.DefaultMQProducer;
import sun.plugin2.message.Message;
public class AsyncProducer {
    public static void main(String[] args) throws Exception {
        DefaultMQProducer producer = new DefaultMQProducer(producerGroup: "haoke");
        producer.setNamesrvAddr("172.16.55.185:9876");
        producer.start();
    }
}
```

画面7：
```java
String msg = "我的第一个异步发送消息!";
Message message = new Message(topic: "my-topic", msg.getBytes(charsetName: "UTF-8"));
```

画面8：
```java
producer.send(message, new SendCallback() {
    public void onSuccess(SendResult sendResult) {
        System.out.println("发送成功了!" + sendResult);
    }
});
```

画面9：
```java
public void onSuccess(SendResult sendResult) {
    System.out.println("消息状态：" + sendResult.getSendStatus());
    System.out.println("消息ID：" + sendResult.getMessageId());
    System.out.println("消息队列：" + sendResult.getMessageQueue());
    System.out.println("消息offset值：" + sendResult.getQueueOffset());
}
```

画面10：
```java
public void onException(Throwable e) {
    System.out.println("消息发送失败!" + e);
}
```

画面11：
```java
System.out.println("消息发送失败!" + e);
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面6：PPT 标题为“2.2.1、Message数据结构”，表格包含字段名、默认值、说明三列，内容包括 Topic、Body、Tags、Keys、Flag、DelayTimeLevel、WaitStoreMsgOK。
画面13：表格包含列：组名、版本、类型、模式、TPS、延迟、操作，操作列包含“修改”、“查看详情”、“配置”、“删除”按钮。

5) 无。
