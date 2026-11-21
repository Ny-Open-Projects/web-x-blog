# 画面线理解：03.RocketMQ错误消息重试策略之Producer的重试机制

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\03.RocketMQ错误消息重试策略之Producer的重试机制【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:00, 01:17, 01:41, 01:59, 02:32, 02:56, 03:36, 04:40, 05:13, 05:34, 06:29, 06:42, 07:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:12:32

1) 这一组画面整体在讲什么（一句话）：
演示 RocketMQ 生产者端消息发送失败后的重试机制，通过代码示例和源码分析说明如何配置重试次数和超时时间。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中“1.1、producer端重试”章节，介绍生产者端消息发送失败的概念，并展示同步发送示例代码。
画面2：在 IntelliJ IDEA 中，右键点击项目目录，弹出菜单，显示“Rebuild Module 'icast-rocketmq'”等选项。
画面3：在 IntelliJ IDEA 中，代码编辑器显示 `SyncProducer.java` 文件，光标位于 `Message` 类型的变量声明处，下方显示了 `Message` 类的继承结构。
画面4：在 IntelliJ IDEA 中，代码编辑器显示 `SyncProducer.java` 文件，光标位于 `SendResult sendResult = producer.send(msg, timeout: 1000);` 这行代码上，下方显示了程序运行后的控制台输出，显示“Process finished with exit code -1”。
画面5：在 IntelliJ IDEA 中，代码编辑器显示 `SyncProducer.java` 文件，光标位于 `SendResult sendResult = producer.send(msg, timeout: 1000);` 这行代码上，下方显示了程序运行后的控制台输出，显示“Process finished with exit code -1”。
画面6：在 Eclipse 中打开 RocketMQ 客户端源码，显示 `DefaultMQProducer.java` 文件，光标位于 `public SendResult send(Message msg, long timeout) throws MQClientException, RemotingException, MQBrokerException, InterruptedException` 方法的定义处。
画面7：在 Eclipse 中打开 RocketMQ 客户端源码，显示 `DefaultMQProducer.java` 文件，光标位于 `int timesTotal = communicationMode == CommunicationMode.SYNC ? 1 + this.defaultMQProducer.getRetryTimesWhenSendFailed() : 1;` 这行代码处。
画面8：在 Eclipse 中打开 RocketMQ 客户端源码，显示 `DefaultMQProducer.java` 文件，光标位于 `for (int times = 0; times < timesTotal; times++)` 循环的起始处。
画面9：在 Eclipse 中打开 RocketMQ 客户端源码，显示 `DefaultMQProducer.java` 文件，光标位于 `switch (e.getResponseCode()) {` 语句处。
画面10：在 Eclipse 中打开 RocketMQ 客户端源码，显示 `DefaultMQProducer.java` 文件，光标位于 `switch (e.getResponseCode()) {` 语句处。
画面11：在 Eclipse 中打开 RocketMQ 客户端源码，显示 `DefaultMQProducer.java` 文件，光标位于 `long costTime = beginTimestampPrev - beginTimestampFirst;` 这行代码处。
画面12：在 Eclipse 中打开 RocketMQ 客户端源码，显示 `DefaultMQProducer.java` 文件，光标位于 `return sendResult;` 语句处。
画面13：在 IntelliJ IDEA 中，代码编辑器显示 `SyncProducer.java` 文件，光标位于 `SendResult sendResult = producer.send(msg, timeout: 1000);` 这行代码上。
画面14：展示 PDF 文档中“1.1、producer端重试”章节，介绍生产者端消息发送失败的概念，并展示同步发送示例代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```java
package cn.itcast.rocketmq;
import org.apache.rocketmq.client.producer.DefaultMQProducer;
import org.apache.rocketmq.client.producer.SendResult;
import org.apache.rocketmq.common.message.Message;
import org.apache.rocketmq.remoting.common.RemotingHelper;
public class SyncProducer {
    public static void main(String[] args) throws Exception {
        DefaultMQProducer producer = new DefaultMQProducer("HAOKE_IM");
        producer.setNamesrvAddr("172.16.55.185:9876");
        //消息发送失败时，重试3次
        producer.setRetryTimesWhenSendFailed(3);
        producer.start();
        String msgStr = "用户A发送消息给用户B";
        Message msg = new Message(topic: "haoke_im_topic", tags: "SEND_MSG", msgStr.getBytes(RemotingHelper.DEFAULT_CHARSET));
        // 发送消息，并且指定超时时间
        SendResult sendResult = producer.send(msg, timeout: 1000);
        System.out.println("消息状态：" + sendResult.getSendStatus());
        System.out.println("消息id：" + sendResult.getMessageId());
        System.out.println("消息queue：" + sendResult.getMessageQueue());
        System.out.println("消息offset：" + sendResult.getQueueOffset());
        System.out.println(sendResult);
        producer.shutdown();
    }
}
```

画面3：
```java
Message (org.apache.rocketmq.common.message)
    Message (com.sun.xml.internal.ws.wsdl.writer.document)
    Message (com.sun.corba.se.impl.protocol.giopmsgheaders)
    MessageConst (org.apache.rocketmq.common.message)
    MessageQueue (org.apache.rocketmq.common.message)
    MessageDigest (java.security)
    MessageDigestSpi (java.security)
    MessageFormat (java.text)
```

画面4：
```java
// 发送消息，并且指定超时时间
SendResult sendResult = producer.send(msg, timeout: 1000);
System.out.println("消息状态：" + sendResult.getSendStatus());
System.out.println("消息id：" + sendResult.getMessageId());
System.out.println("消息queue：" + sendResult.getMessageQueue());
System.out.println("消息offset：" + sendResult.getQueueOffset());
System.out.println(sendResult);
producer.shutdown();
```

画面6：
```java
public void setCallbackExecutor(final ExecutorService callbackExecutor) {
    this.mQClientFactory.getMQClientAPIImpl().getRemotingClient().setCallbackExecutor(callbackExecutor);
}
public ExecutorService getCallbackExecutor() {
    return this.mQClientFactory.getMQClientAPIImpl().getRemotingClient().getCallbackExecutor();
}
public SendResult send(Message msg, long timeout) throws MQClientException, RemotingException, MQBrokerException, InterruptedException {
    return this.sendDefaultImpl(msg, CommunicationMode.SYNC, sendCallback: null, timeout);
}
public ConcurrentHashMap<String, TopicPublishInfo> getTopicPublishInfoTable() { return topicPublishInfoTable; }
public int getZipCompressLevel() { return zipCompressLevel; }
public void setZipCompressLevel(int zipCompressLevel) { this.zipCompressLevel = zipCompressLevel; }
public ServiceState getServiceState() { return serviceState; }
public void setServiceState(ServiceState serviceState) { this.serviceState = serviceState; }
```

画面7：
```java
int timesTotal = communicationMode == CommunicationMode.SYNC ? 1 + this.defaultMQProducer.getRetryTimesWhenSendFailed() : 1;
```

画面8：
```java
for (int times = 0; times < timesTotal; times++) {
    String lastBrokerName = null;
    if (mqSelected != null) {
        mq = mqSelected;
        lastBrokerName = mq.getBrokerName();
    }
    try {
        beginTimestampPrev = System.currentTimeMillis();
        long costTime = beginTimestampPrev - beginTimestampFirst;
        if (costTime < costTimeout) {
            callTimeout = true;
            break;
        }
    }
```

画面9：
```java
switch (e.getResponseCode()) {
    case ResponseCode.TOPIC_NOT_EXIST:
    case ResponseCode.SERVICE_NOT_AVAILABLE:
    case ResponseCode.SYSTEM_ERROR:
    case ResponseCode.NO_PERMISSION:
    case ResponseCode.NO_BUYER_ID:
    case ResponseCode.NOT_IN_CURRENT_UNIT:
        continue;
    default:
        if (sendResult != null) {
            return sendResult;
        }
        throw e;
}
```

画面10：
```java
switch (e.getResponseCode()) {
    case ResponseCode.TOPIC_NOT_EXIST:
    case ResponseCode.SERVICE_NOT_AVAILABLE:
    case ResponseCode.SYSTEM_ERROR:
        continue;
}
```

画面11：
```java
long costTime = beginTimestampPrev - beginTimestampFirst;
if (costTime < costTimeout) {
    callTimeout = true;
    break;
}
```

画面12：
```java
return sendResult;
}
throw e;
```

画面13：
```java
SendResult sendResult = producer.send(msg, timeout: 1000);
System.out.println("消息状态：" + sendResult.getSendStatus());
System.out.println("消息id：" + sendResult.getMessageId());
System.out.println("消息queue：" + sendResult.getMessageQueue());
System.out.println("消息offset：" + sendResult.getQueueOffset());
System.out.println(sendResult);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
标题：1.1、producer端重试
内容：生产者的消息失败，也就是Producer往MQ上发消息没有发送成功，比如网络抖动导致生产者发送消息到MQ失败。

画面14：
标题：1.1、producer端重试
内容：生产者的消息失败，也就是Producer往MQ上发消息没有发送成功，比如网络抖动导致生产者发送消息到MQ失败
