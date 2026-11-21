# 10.RocketMQ快速入门之发送消息（同步）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\10.RocketMQ快速入门之发送消息（同步）【海量资源尽在 ubkz.com】.mp4
- 时长 9分35秒（音频 576s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好我们接着继续那么接下来我们来看一下发送消息的API的使用那么发送消息呢又分两种那么一种是同步一种是异步首先我们先来看同步OK那么我们还是进入到我们这个工程里面我们来创建一个包这个包呢我们把它称之为就叫producer叫send吧send啊send messagesend messageOK
[00:29] 好那么这个就是我们测试这个发送消息然后呢我们在这个里面呢创建一个类啊叫做sync然后呢producer然后呢我们去写一个main方法好那么我们来看一下首先呢我们还是需要创建一个default mq producer哎就他然后呢去new一个default mq啊producer好然后呢我们是不是就可以去
[00:58] 大家呢还是需要先给他设置一个他的一个分组那么就叫浩克好那么下面呢我们去给他设置一个NemoServer把前面这个代码我们贴过来那么就他把他呢拿过来吧然后呢我们在设置完成之后呢我们就可以去启动我们这个ProducerStart然后呢我们这个位置给他抛出一层抛出一层Exception
[01:29] 然后呢在最后啊给他去来一个先把这个代码先写好然后在这个里面做一个发送啊来发送这个消息然后呢producer.sendsendmessage看一下是不是有一个message对象啊然后呢我们去给他去构造一个message对象sage啊message对象注意要用这个包下面的message对象
[01:59] 那么message等于new一个message哎呀ok好然后呢我们去给他去做一个设置把这个消息发送出去那么我们其实给这个消息需要设置一些他的参数啊那么我们来看他的一些构造参数啊构造参数呃构造参数那么他有一个空的构造参数还有一些其他的构造参数那么这样咱们呃找一个参数给他设置吧比如说我们用这个啊
[02:26] 三个参数那么第一个参数呢就是第一个参数呢就是topic就是你要去发送到哪个topic里面去然后呢还有呢就是一个tags对啊tags还有一个就是body就是我们这个消息体是一个字节数组这样的一个消息体那么这样咱们就叫用这个吧这个构造参数吧因为这个构造参数呢相对会少一点一会儿我们来讲一下这个message的一些它的一些字段好了那么我们来看一下
[02:54] 那么设置三个参数那么第一个参数呢就是topic对吧那么topic发送到哪里呢就发送到我们刚刚所创建的topic那就叫什么呢叫my topic哎ok把它呢好位过来那么发送到他然后呢有一个叫tagstags呢我们就把它称之为叫什么呢就叫比方说叫my tag吧然后呢body就是我们的消息体那么消息体呢我们是不是应该在这个位置定义一个message等于
[03:25] 经营一个消息的内容就是什么呢我的第一个消息OK好那么我们把这个消息去拿到它的一个直接宿主点盖的什么BAT通过一个什么UTFUTF-8的一个字编码去拿到一个这个match者然后去做一个发送那么在发送完成之后它会有一个返回值
[03:52] 那么这个返回值呢是一个叫做send result的一个对象那么在这个里面呢我们可以去拿到它一些内容包括什么呢叫做get什么比如有message id那么这个就是它的一个消息id对不对那么把它打印出来那么叫做消息id然后呢冒号加一个它这是第一个这个内容那么还有什么呢我们可以看一下那么比如说还有get什么get叫做message queue
[04:18] messq就是我们那个消息对列它的一些这个信息消息对列ok这是第二个第三个呢我们来看一下那么我们还需要给大家去还看有没有其他内容我们来看一下get什么还有getq的offset这是它的一个偏移令消息的一个offsetoffset值好那么我们来看一下还有没有一些其他的一些这个内容可以拿到get比如说
[04:49] 消息ID我们拿到了对吧可能就差不多吧就这么多OK那么先打印这么多当然了我们也可以直接简单一点就是直接这样直接把这个SendUitOut打印出来是不是也可以好嘞好那么我们做一个消息的一个发送走来看一下这个消息能不能够发送成功呢来看一下那么等待它的一个发送好那么我们可以看到这个消息它已经发送成功了那么消息ID那么可以看到是这样的一个消息ID
[05:21] 那么也就是说我们这个消息去发送到我们这个消息对吧他发送到我们的Rockdamq服务器之后我们服务器会返回一个这个对象在这个对象中呢是不是有一个消息ID那么以后呢我们是不是就可以通过这个消息ID去查找我们这个消息啊OK是可以的那么消息对列他的一些信息那么可以看到他topic是不是叫my topicblock name就是我们刚刚所设的这个block name然后呢qid就是我们对列的id
[05:50] 那么前面我们在创建的时候我们给这个topic是不是设置了有8个这个message queue那么其中他拿到了一个序列为3的也就是说第4个这个queue对不对那么其实我们创建完成之后可以在这个位置有一个状态我们来看一下在这个状态中我们其实可以看到他有什么多个我们这个message queue那么他的queue id是从0开始那么我们刚刚看到是不是queue等于3的这个可以看到这个里面是不是已经有一个
[06:18] 最大点的是不是就是1那么也就是说这个上面其实已经有一个消息了哎OK好那么我刚刚从这个返回值里面是不是也可以看到这个信息包括它的offset值目前是0再往后是不是就会变成1继续往后面去走然后这个是send result下面有它的一些内容可以去看一下那么OK好那么我们接下来先大致的对这个match这个对象的有一些基本的一个了解
[06:45] match对象中会有这么几个内容需要我们去注意一下那么首先第一个是topic就是我们的一个topic的名字topic的名字那么第二个是body就是我们的一个消息体就是消息的内容它必须是传递的是一个字节数组对吧,字节数组所以我们刚刚是不是去通过UTF-8拿了它的一个字节数组然后第三个就是一个text
[07:11] 这个tags是它有点类似于我们邮件中的那个标签那种标签方便我们做一些这个过滤做一些过滤那么比如说我们设置一个tag比如说我们叫user比如说我们要去设置一些哪些是user相关的一些这个消息是不是就会比较方便还有什么呢还有是我们的一个这个叫做kiss当然了这个和这个都是属于选填项选填你不填也是可以的也是OK的那么这个kiss呢就是
[07:41] 他呢是建议我们去设置一些这个比如说订单号啊商品ID啊作为一个key因为他是可以保证一个唯一嘛
[07:49] OK那么是这样的一个case完全是我们的一个业务的一个设置的一个值跟我们业务相关的一个值它跟这个消息其实本身没什么关系这跟我们的业务有关系的还有什么像这个flag这个也是一个选田还有这个是一个消息的延迟消息延迟那么0表示不延迟大于0会待定的时间去做一个消费就延迟的一个消费
[08:15] 那么最后一个这个是表示我们这个消息是否在服务器落盘后才返回应答那么这个也是个选点项那默认是一个chew
[08:25] 那么你可以把它设置为一个fos那么大概我们这个message的一个对象它这个结构大概有这么多其实我们一般在设置的时候我们这几个是比较有用的这个是必须的还有什么还有它还有什么还有是它还有它往往我们来讲的话是比较去有用的像后面这三个相对用的会比较少一点ok好那么我们刚刚所设置的是不是就设置这三个来看一下
[08:52] 那么设置就是一个是topic一个是tag一个是tag那么OK好那么现在我们这个消息是不是就已经发送完成了当然了我们可以在这个位置来查看一下看一下我们的消息我们通过我们的一个message的ID可以去做一个这个查询比如说我们找一个topic就是mytopic那么消息的ID是不是就刚刚我们所看到一个消息ID通过它去做一个这个查找走那么是不是就找到我们的一个消息
[09:19] 那么这个消息的内容可以看到在这个位置是不是就是我的第一个消息这个消息已经成功发送到我们的这个服务器哎OK好嘞好那么关于我们的这个消息的一个发送当然它是一个同步的一个发送啊那么这个我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package cn.itcast.RocketMQ.sendmsg;
import org.apache.RocketMQ.client.producer.DefaultMQProducer;
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
package cn.itcast.RocketMQ;
import org.apache.RocketMQ.client.producer.DefaultMQProducer;
import org.apache.RocketMQ.client.producer.SendResult;
import org.apache.RocketMQ.common.message.Message;
import org.apache.RocketMQ.remoting.common.RemotingHelper;
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

