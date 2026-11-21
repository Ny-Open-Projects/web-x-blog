# 03.RocketMQ错误消息重试策略之Producer的重试机制

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\03.RocketMQ错误消息重试策略之Producer的重试机制【海量资源尽在 ubkz.com】.mp4
- 时长 7分5秒（音频 426s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下producer的一个从事那么也就是我们的生产者的一个从事那么生产者在发送消息的时候呢从事之后怎么玩呢来看一下那么我们想要去使用RockMQ所提供的一个从事机制我们在生产者这一端只需要做两件事情就可以完成那么第一件事情呢就是在我们的producer这个位置给他设置一个从事的一个次数就如果我发送失败那里做一个retry
[00:26] 从事那么从事次数的设置为三那么就会从事三次ok这第一件事情那么第二件事情呢就需要在我们发送消息的时候那我们给他指定一个超时时间那么他会在这个指定的这个超时时间这个时间内如果发送失败就会做一个从事ok那么接下来呢我们来做一个测试好那么下面呢我们在我们这个代码这个位置啊我们给他创建一个包比方说我们就叫error这个包
[00:54] 然后呢我们把这个我们创建一个类吧我们这个类啊把这个类名拷过来然后呢我们把下面的这个代码我们拷过来去做一个测试OK那么其实这个代码跟我们前面写代码是基本上是一样的啊只是呢我们给他去啊给他去加了两个啊两个从事啊相关的一些这个参数那OK好那么我们来看一下第一个呢是不是给他设置了一个从事次数为三
[01:25] 那么下面呢我们是不是去发送这个消息那么发送消息啊发送消息呢我们给他设置的他的一个操作时间呢是1000啊是1000这个毫秒那么也就是我们的一秒钟啊一秒钟好那么下面呢我们来测试一下运行一下看会得到一个什么结果那么我们去直接运行然后呢我们会发现呢他会抛一个异常会抛一个超时的这个异常啊超这个异常
[01:55] 那么其实是这样的其实是我们这个去演示这个生产者这个从事这样的一个效果并不是很好演示所以呢我们选择什么呢选择这个给大家去通过圆满的方式去讲解一下他的这个生效或者说我们去看一下圆满吧然后呢去大概的去了解他这个机制就可以了因为这个效果不是特别好演示
[02:23] 那么我们就跟着这个代码我们进入它的一个send的这个方法来看一下那么进入这个send的方法之后呢我们继续进入它下面的一些这个方法的调用然后呢进入这个方法然后呢在这个里面呢我们就可以来看到它的一些核心的代码的逻辑那么首先我们来看一下这一行这个代码是在512行这个代码那么在这一行这个代码呢我们来看一下
[02:49] 他这个代码是在干嘛呢去计算出我们需要从事的一个次数我们来看一下那么在这个里面他用了一个三目运算符就是去做一个判断那么如果我们当前的这个模式是一个同步模式的话那么他的从事的次数就是一去加上什么呢我们的这个retry的这个次数这个是不是前面我们在代码中所设置的这个从事这个次数对不对OK那么从事这个次数加
[03:17] 加1就是它的总共要执行的个次数否则的话呢就是1那么也就是说通过我们这个圆码中我们可以得知那么如果你的生产者是一个同步的模式那么他会做一个从事那么如果你的生产者是一个异步的模式是不是就不会做从事啊OK所以说通过这个圆码是不是就会得到这样的一个信息那么接着我们继续往下面看那么在下面呢在这个位置可以看到啊在这个位置我们可以看到它是一个货循环对不对
[03:45] 那么for循环呢它的一个条件呢就是这个times小于我们的这个总的一个次数那么然后呢做一个time的一个加加其实在这个逻辑中呢就是在做一个重视或者说在这个逻辑啊这么一下面这个逻辑啊就这个for循环中的这个逻辑就是在做一个发送消息然后呢会发送多次对不对会发送多次有一个循环在这个位置啊那么循环的次数是不是由它来做一个决定然后呢我们来看一下
[04:14] 那么在下面的如果出现了异常那么出现什么异常呢比如说出现这个remoting这个异常然后mqclient这个异常mqblock异常等等都会有一个什么continue看到了吗continue也就是说我们这个循环会继续那么也就是说这个地方就是我们做一个从事的一个机制从事的一个关键点就在这然后你看他也会这个我们来看一下会不会从事往下面走
[04:42] 这个不会做从事这个会如果说在这如果是在这的话那么就会去做一个如果这么多这个异常的话那么就会做一个从事那么否则的话就会抛出这个异常那么这个地方抛出异常是不是就不继续做从事了OK那么包括下面的这个异常它也不会去
[05:06] 不会去从事也是去返回也是抛出异常那么也就是说什么意思就是说那么从事也就是说他会根据我们有几个或者说他只识别这么几个这个异常或者从事并不是所有的异常都会做一个从事这一点一定要注意一定要小心OK好那么为什么我们刚刚所说他这个效果不好掩饰呢原因是在这个位置他还有一个
[05:35] 还有一个时间那个对比我们来看一下它还有一个时间对比就在下面这个位置我们来看一下那么我们来找一下时间在这它会有一个这个时间那个对比就是说我们如果设置那个超时时间如果就是它所执行的一个时间超过了我们这个超时时间时间就会做一个break那么就会跳出我们这个复循环
[06:00] 跳出这个负循环那么就会导致直接是一个出错那么要注意你一旦跳出这个负循环对吧那么跳出这个负循环那么也就意味着你肯定后面就不会再去做一个从事了对吧所以说它这个效果不是很好掩饰那么它所识别的是不是就是一些它所看到的一些或者说所识别到的一些这种异常的情况才会做一个从事
[06:25] 所以不是特别好演示然后大家通过这个圆码解读我们是不是就已经知道OK那么在有些情况下面它是不是就可以去实现这个从事的这样的一个效果因为它有一个负循环在这个位置做一个循环的一个发送OK好那么关于这个生产者的一个从事的一个机制我们就讲这么多那么因为这个效果实在不好去做一个测试那我们就不做一个演示了OK那么但是我们知道
[06:53] 只要设置这两个点那么对于我们同步的一个消息是不是就可以实现一个从事这样的一个效果OK好那么关于我们生产者端的一个从事我们就讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 RocketMQ 生产者端消息发送失败后的重试机制，通过代码示例和源码分析说明如何配置重试次数和超时时间。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中“1.1、producer端重试”章节，介绍生产者端消息发送失败的概念，并展示同步发送示例代码。
画面2：在 IntelliJ IDEA 中，右键点击项目目录，弹出菜单，显示“Rebuild Module 'icast-RocketMQ'”等选项。
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
package cn.itcast.RocketMQ;
import org.apache.RocketMQ.client.producer.DefaultMQProducer;
import org.apache.RocketMQ.client.producer.SendResult;
import org.apache.RocketMQ.common.message.Message;
import org.apache.RocketMQ.remoting.common.RemotingHelper;
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
Message (org.apache.RocketMQ.common.message)
    Message (com.sun.xml.internal.ws.wsdl.writer.document)
    Message (com.sun.corba.se.impl.protocol.giopmsgheaders)
    MessageConst (org.apache.RocketMQ.common.message)
    MessageQueue (org.apache.RocketMQ.common.message)
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

