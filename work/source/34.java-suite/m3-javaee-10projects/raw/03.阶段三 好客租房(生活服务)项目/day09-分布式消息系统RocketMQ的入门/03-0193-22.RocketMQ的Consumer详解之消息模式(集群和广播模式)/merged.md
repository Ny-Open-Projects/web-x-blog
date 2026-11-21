# 22.RocketMQ的Consumer详解之消息模式（集群和广播模式）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\22.RocketMQ的Consumer详解之消息模式（集群和广播模式）【海量资源尽在 ubkz.com】.mp4
- 时长 5分44秒（音频 345s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们来看一下consumer中的消息的模式啊那么在我们前面所使用的这个default mqpulse consumer中呢它其实实现了一些这个自动保存offset值那么offset值前面我们也提到了对吧它就是它的一个偏移量对吧消息的一个偏移量那么以及实现多consumer的一个负载均衡那么它是怎么实现的呢其实我们来看一下那么我们在前面去写我们的consumer的时候啊
[00:28] 那么我们来看一下啊随便我们来找consumer就他吧那么在consumer的时候呢我们其实去设置了一个consumer的一个group那么这个group到底有什么用我们来看一下那么我们简单的去画一个图吧简单的画一个图那么我们来说一下这个啊说一下这个它的一个用处啊好那么把这个图呢我们拉大一点然后呢来看一下
[00:54] 那么在后面呢我们简单的画一个图啊简单画一个图来去做一个简单的一个分析呃然后呢我们来看一下假设呢这个就是我们的一个啊这个就是我们的一个呃服务器啊我们的一个服务器啊这个是我们的一个消呃消息的一个服务器也就是我们的消息系统呃消息系统呃然后呢我们这个消息系统呢我们会有一些这个消费者啊会有个消费者那么我在这个位置呢我来
[01:23] 看一下啊我是有一个消费者的组那么这个是我的consumer1啊那么我就写一个叫做消费者消费者1啊消费者1然后呢我们把它call一下那么假设呢我现在呢有多个这个消费者这个消费者2然后呢有消费者3哎大概呢就有这么三个吧那么这个是这个是2啊这个是3来看一下那么
[01:53] 这个消费者啊消费者二然后呢这个是消费者三好嘞那么我有三个消费者他们呢是同属于一个组啊同属于一个组就是呃同一个组啊是同一个这个消费者这个组那么我们来看一下他的一个消息的发送那么这个时候啊这个时候
[02:16] 当我的消费系统它有一个消息的时候是不是需要去发送到我们这个消费者那么这个时候就会有个问题了那么你这个消息是发送给这个消费者一还是发送给消费者二还是发送给消费者三还是呢这三个全部都能够接收到这个消息对吧这个时候就会有一个问题了哎呀OK那么所以接下来我们要讲这个内容的就是它的一个消息的一个模式那么就是说
[02:46] 那么这个consumer的这个消息模式呢它其实有两种那么第一种叫做集群第二种叫做广播什么意思呢如果我们去设置我们去设置它的这个模式是集群的话那么这个时候呢当我们的这个服务器有一个消息来的时候呢这个消息它只能进入到其中的某一个这个consumer
[03:11] 某一个这个消费者那么为什么要去这样设计呢大家想一下那么假设啊假设我在我的这个消息系统有100条或者1000条啊1000条这个条这个消息那么有1000条这个消息那么我采用集群这种模式的话那么是不是就可以把我的1000条消息
[03:34] 分别向我不同的这种消费者当然他们是同属于一种一个组不同的消费者上面去做一个平均做一个分发这样的话我这个消费者是不是就很就能够快速的去消费我这个消息对不对但是他们三个他们三个消费消息的总和是不是都是我这个1000条OK这个就是叫集群的模式集群的模式
[04:01] 那么如果我们把它设置为是一个广播的模式那么从这个名字上面我们就能够看出啊它是什么意思呢如果是广播的模式那么我们任意啊任意一个消费者虽然也是同属于一个组啊那么任意一个消费者都会接收到我们这个消息那么如果这个消息统有一千条消息那么消费者也他也会接收到一千条消息那么这个也是一千条
[04:30] 同理那么消费者三也是1000条这个大家能够理解了吧OK这就是啊这就是它的两种模式的区别那么一种是集群一种呢就是这个广播模式啊那么如何去设置它的模式呢就通过我们的Ctrl目中去做一个设置那么来看一下在Ctrl目里面的它有一个模式点set什么呢set我们一个model就是一个message一个model
[04:58] 那么我们来看一下它需要接收的是一个Message Model的一个这样的一个枚举在这个里面呢可以看到是不是两种模式啊那么上面这种模式呢是不是就是这个叫广播对吧然后呢这个Broadcast然后呢这个下面这个呢就是我们的Clastic那就是我们这个集群的模式OK那么你根据需求去做一个设置啊就可以了哎呀好嘞那么
[05:22] 我们回到刚刚的Demo里面那么通过一个MessageMessage一个Demo比如说我们设置它是个集群那么OK设置集群是不是只有一个能够接收到那么设置广播就所有的都可以接收到OK好嘞那么这个就是我们所讲的一个消息的一个模式好那么关于这个消息的模式我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

