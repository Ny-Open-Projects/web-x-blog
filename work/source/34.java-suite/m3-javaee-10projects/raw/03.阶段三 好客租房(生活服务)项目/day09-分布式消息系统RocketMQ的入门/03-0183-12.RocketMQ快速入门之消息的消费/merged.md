# 12.RocketMQ快速入门之消息的消费

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\12.RocketMQ快速入门之消息的消费【海量资源尽在 ubkz.com】.mp4
- 时长 7分46秒（音频 466s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下消息的消费那么我们来看一下API怎么去用啊那么首先呢我们在这个下面呢创建一个包就叫consumer然后呢我们在下面呢去创建一个类这个类呢我们就把它称之为叫consumer demo吧就叫consumer demo去做一个消息的一个消费那么同样呢我们写一个man方法好,那么我们把前面这个给它先停掉
[00:31] 然后我们来看这个里面代码怎么样去编写首先我们要需要定义一个defaultdefault什么的defaultmq一个consumer要注意这consumer有两种一个是叫做pull一个叫做push那么前面我们其实在讲的时候也提到过这么在rockmq中有两种消费者一种是推一种是拉对吧pull就是拉曲这个就是推
[00:58] 那我们推送就是服务端向我们客户端做一个推送那我们接下来要用的就是这个推PUSHMQ来看一下叫PUSHPUSH CONSUMER好那么我们来看一下这个叫Consumer等于new一个default这个PUSH CONSUMER那么同样的我们给它一个这个group就分组比如说我们叫后客然后后客杠来一个Consumer
[01:29] 好那么接下来我们要给他设置一个set name server跟我们前面是一样的172.16.55.185 9876就是我们的name server的一个地址好那么接下来我们就需要给他去做一些设置设置什么我们要去做一个订阅订阅什么去订阅我们这个消息订阅这个消息
[01:55] 那么首先我们给他设置一个topictopic谁呢就是我们刚刚写的my topic然后呢我们去给他设置一个这个订阅的一个表达式那么我们设置一个新新代表什么意思呢就是只要是进入这个topic的这个消息那我全部都接收那就是所有消息的意思好那么我们给他去抛出一个抛出个一场那么exception好那么订阅这个订阅订阅这个消息
[02:24] 好 那么我们这里接收的是所有这个消息好 那么订阅完成之后那么接下来我们就需要去拿到他的消息了对吧那么我们需要去怎么拿我们要给他去注册一个message这个list就是一个register去注册注册一个消息的监听就是一旦有消息之后我们就可以去拿到里面的一些消息内容对吧
[02:50] 那么在我们这个消息监听里面就message的这个listener里面有两种实现一种是order一种是concurrator那么这两种有什么区别呢我们简单的说一下前面的这个第一个是order是表示它是一个顺序消息而下面这个是一个并发的一个消息那么现在呢我们先使用下面的这个后面我们会详细去讲这个顺序消息我们会使用它ok那我们就给它来一个register然后呢我们设置一个这个listener
[03:19] 然后去做一个new一个什么呢conqueror listenerOK好那么我们拿到这个消息之后呢实现之后呢就可以拿到这个消息了我们来看一下这个里面的一些这个内容好那么在这个位置他要求我们有一个return一会我们来给他去做一个return那么我们通过这个如果有消息的话那么我们就打印出一句话就是我们已经接收到这个消息是谁呢
[03:48] 加一个我们这个messagemessage是拿到他然后呢我们把这个每一个消息都给他去做一个打印出来打印出来那么messageok然后呢我们拿到他的一个消息的内容就是message点get什么get body然后呢我们需要去做一个打印怎么打印呢来一个他然后呢这个消息加一个什么呢
[04:17] 加一个new一个stream然后一个是他另外一个是不是UTF-8因为要做一个编码OK这个是有一个异常对吧那么有异常这样我们给他去做一个补货补货有异常OK好拿到了消息把每个消息都打印出来然后我们就去接收到这个消息那么我们接下来看一下这个返回值return那么返回什么呢
[04:48] 那么在这个实现内中这个实现内中他要求我们返回的是一个这个States状态那么也就是说我们现在是一个来我们画个图那么我们现在是一个这个假设这个是我们的一个消费者这个是我们的一个服务端对吧那么服务端是不是像我们的这个消费的这一端客户端是不是要去推送这个消息是不是推送OK
[05:15] 推送这个消息那么把消息拿过来了那么拿过来之后呢我们是不是进行做一个做一个这个消费那么消费完成之后呢我们是不是要给一个服务端一个响应对吧响应响应什么呢响应我们这个消息是你是处理成功了还是失败了因为
[05:32] 他是不是必须得知道这个消息是成功还是失败那么如果成功那这个消息那就OK了那么如果要是失败的话那么我是不是就需要做一些后续的一些处理比如说去做一些这个从事啊等等一些这个机制OK所以呢在这个位置要求我们返回一个状态那我们来看一下这个状态状态呢其实就是两种一种就是成功一种就是这个失败那么OK那我们给他去设置一个return一个成功吧那就是成功点success
[06:00] OK好那么最后呢我们需要在这个位置是不是将我们的这个consumer是不是启动起来启动我们这个消费消费者然后呢调用这个consumer点start做一个启动那么启动之后呢是不是就去做这样的一个监听监听之后呢我们就可以拿到我们的一个消息那么我们把它启动起来来看一下它是否能够拿到消息呢那么等待它的一个执行OK那么我们可以看到
[06:32] 当我们启动起来之后呢他已经就拿到了两个消息那么可以看到这两个消息是不是刚刚我们所测试的两条消息那么第一个就是异部的消息第二个就是我第一个发动的同步的消息对吧OK那么拿到的内容是不是一样OK
[06:47] 好那么比如说他的消息ID什么都可以拿到这个我们就不一一去打印他的内容了那么我们是不是消息的消息体是不是就已经拿到了哎OK那么这个呢就是我们的一个消息的一个消费那我们可以测试一下当我再次发送消息的时候他能不能够去拿到我的消息呢比如说这个我这是这个内容改一下我的第一个消息改成个二好那么我们去做一个发送走那么看一下我这个消费者一会能不能拿到消息呢
[07:16] 测试一下那么等待他的一个执行那么如果他发送成功在这个位置他肯定是不是就可以拿到这个消息你可以看到是不是我的第一个消息二OK那么这面就发送成功了那么这面是不是就拿到这个消息了OK好那么这个就是我们所讲的一个API就是什么呢消息的一个消费那么在这个里面是不是我们通过一个订阅就可以订阅到所有的这个消息OK好那么关于我们这个消息这个消费的API这个使用我们就讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package cn.itcast.RocketMQ.consumer;
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
import org.apache.RocketMQ.client.consumer.DefaultMQPushConsumer;
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
import org.apache.RocketMQ.client.consumer.DefaultMQPushConsumer;
import org.apache.RocketMQ.client.consumer.listener.ConsumeConcurrentlyContext;
import org.apache.RocketMQ.client.consumer.listener.ConsumeConcurrentlyStatus;
import org.apache.RocketMQ.client.consumer.listener.MessageListenerConcurrently;
import org.apache.RocketMQ.client.exception.MQClientException;
import org.apache.RocketMQ.common.message.MessageExt;
import java.io.UnsupportedEncodingException;
import java.util.List;
public class ConsumerDemo {
```

