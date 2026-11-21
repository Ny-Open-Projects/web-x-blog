# 11.RocketMQ快速入门之发送消息（异步）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\11.RocketMQ快速入门之发送消息（异步）【海量资源尽在 ubkz.com】.mp4
- 时长 6分1秒（音频 361s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续前面呢我们所看到的是同步的发送消息那么接下来我们来看一下异步的发送消息那么同样呢我们也在这个send message的这个包下面我们去创建啊我们的一个测试类那么下面呢我们这个名字就叫async然后呢来一个producer好那么我们来看一下这个里面怎么去写这个代码呢
[00:27] 那么我们首先呢先把这么几个内容我们先拷贝过来就是前面这几个他呢都是一样的哎OK有了他之后呢我们就可以去做这个操作了哎OK那么他呢同样的也让他去抛出exception啊exception好然后呢我们在下面的去发送消息发送消息那么发送消息呢我们去给他去通过什么呢通过一个producer.send的一个
[00:54] send message来看一下是不是send然后呢第一个参数是message第二个参数呢我们要给它设置一个什么呢叫做callback叫send callback我们用这个方法这个方法第一个呢是message第二个呢就是我们的一个callback回调好那么我们来调用它send然后呢send然后呢第一个参数我们就叫message那么我们就把那个跟我们刚刚写的一样来一个messagemessage
[01:24] 写权吧message等于等于你有一个message你有一个这个错了导包导错了不是他这个一定要注意那么我们把这个message拿过来message要用它
[01:40] 然后呢我们message可以给它设置设置什么呢第一个是不topic那么就是叫mygang topic然后呢第二个参数就是我们的消息体对吧前面我们说过这个消息的内容呢其实只有前面这两个啊这两个是必填项其他都是选填项我们可以不做一个填写第一个呢叫topic第二个就是我们的消息的内容那么比如说我们再来一个啊把这个刚刚这个拿过来就是我的第一个消息那么我们把它拷过来
[02:09] 然后我们这个叫什么我的第一个这个一步发送消息好嘞那么我们拿到message之后同样的去拿到它的一个直接宿主点盖到bytes然后来一个utf-8好嘞那么这样的话我们的这个视频就ok了messageok了第一个参数就搞定那么第二个参数我们需要给它去new一个叫做sendsend一个callback就是我们的一个
[02:38] 异步的一个发送一个回调函数然后呢在这个uncess是吧就是我们的一个成功啊那么在这个里面呢我们可以把我们的这个发送成功的一些这个内容呢就打印出来比如说在这个位置显示什么呢发送发送成功了发送成功了OK然后呢我们去把一个这个send result这个对象打印出来那么同样的我们是不是也可以去拿到
[03:06] 我们的这个流量的中的一些其他的内容当然这个都是一样的OK然后在这个位置如果是unexception就是我们的一个发现发生异常了对吧我们就把它打印出来叫做什么就是消息发送失败消息发送失败OK好那么发送失败咱们把这个异给打印出来
[03:30] 就是这个异常的一个对战信息那么接下来呢我们来看一下在这个位置呢我们先这么来写点什么呢OK那么看他会怎么样好那么接下来我们来去做一个发送消息走看一下消息是否能够发送成功呢测试一下等待他的一个发送可以看到在这个位置是不是显示消息的发送失败为什么失败呢来看一下他说这个不能获取到我们这个
[04:01] topic的这个信息我们前面写的应该是叫mytopic吧没有问题那是我们是不是这个也是ok的没有问题那么这个是什么问题呢这样我们先把它先注掉我们来看一下它是否能够发送成功呢然后呢我们走等待它的一个执行等待它的执行好那么我们可以看到我们这个消息已经发送成功了
[04:31] 为什么我们把最后这句话给它住掉之后就发动成功呢大家想一想其实是这样的那么由于我们这个发动的过程它是个异步的过程对不对那我们程序是不是一直往下面去执行那么当我们去调动这个声音之后相当于我们这个就结束了然后呢这个是它的一个异步的操作然后呢我们程序走到这儿是不是就掉入我们的一个sheddown那么是不是就把我们这个producer做一个sheddown就结束掉了
[04:57] 那么结束掉之后那么我们是不是就没有办法再去发动消息了对不对所以我们在这个位置不能紧接着去把它set down你要等到你的消息发送完成之后然后再去做一个set down可以等一段时间但是我们为了测试方便我们就直接把它住掉了我们就不做一个set down这样的话是不是我们就可以做一个发动就成功了对吧ok那我们来看一下消息ID做一个查找消息看能不能够查到我们刚刚的消息到这来看一下走
[05:24] 那么是不是拿到一个消息了你看我的第一个异步发送的消息OK那么我们可以看到这个消息它其实已经发送到我们的QID是什么呢等于6那么我们来看一下那我们的一个这个主题找到一个my topic可以看到一个这个ID等于6的这个上面是不是也有一个了OK好嘞那么这个呢就是我们的一个异步的一个发送的一个消息
[05:48] 这个是异步发动消息OK好那么关于异步消息这个发送我们就先讲到这最后大家要注意这个我们刚刚是不是已经设置测试了这个问题了OK好那么我们就到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.apache.RocketMQ.client.producer.DefaultMQProducer;
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

