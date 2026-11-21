# 10_RabbitMQ快速入门-消费者

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\10_RabbitMQ快速入门-消费者_【海量资源尽在 ubkz.com】.mp4
- 时长 10分10秒（音频 610s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 介绍完生产者的代码那么接下来我们来完成消费者的代码那么消费者和生产者其实非常类似这个地方呢刚才我们也看到了说Channel有个方法叫做Basic Publish还有一个方法呢叫做Basic Consumer其实就这不太一样那么我们在这个Consumer这个工程里边来不要写错地方我们在这里边呢创建一个类叫做直接把保也带上it黑马.consumer.
[00:30] consumer类名-hello world那么这个类名写好了之后呢我们psvm把闷方法写一下然后这个代码呢我就不再去再写一遍了我把这个代码有人复用的地方我都把它复制过来一直到这个地方我都把它复制过来注意看在这个里边呢有一些代码呢是一模一样的好
[00:59] 然后呢这里边会抛异常我们把这个异常呢给它抛出去啊把异常抛出去好抛出去之后呢这个代码就不报错了那么接下来我们来看一个小东西啊说这个地方呢channel我申请了一个现在我请问一下大家这个channel跟我们的producer里边这个channel一样不我相信很多同学觉得那代码都是一样的能不一样吗其实呢我们再回过头来看这个图你在这个地方看
[01:29] 我们的producer里边是不是有一个connection而consumer这个地方是不是也有个connection这是两个connection哦它们里边的channel也是不一样的connection也是不一样的好吧所以呢这个地方两个是没有什么关系的OK吧那么这样弄完了之后呢接下来再声明一个对列那么这句话其实可以不用因为刚才我们在写生产者代码的时候对列是不是已经声明了但是你把它放这儿也没有什么问题的
[01:57] 所以这个也OK的那么这个下来就是我们对应的一个发送代码了那么再来我们下来就接着来写对于消费者我们就不是发送了我们是接收那么就是接收消息接收消息怎么接收呢我们的channel刚才看了一个方法叫做basic consumer那么basic consumer我们用三个参数这个方法
[02:27] 还是同样的我们进去看一下这些方法的一个参数三个参数的这个方法好那么我们点到实现了好那么看一下这个方法其实很好去理解好Ctrl C复制一下那么我们把这个参数呢给它解释一下好可以来看一下那么这三个参数呢很好理解参数我们写一下第一个参数呢是QQ呢就是我们对列的名称
[02:58] 对列名称刚才是不是叫Hello World对吧然后呢第二个参数叫做Auto ACKACK呢翻译过来叫做Acknowledge确认的意思是否自动是否自动确认这个呢后期我们会重点去讲解它的确认机制那么自动确认什么意思呢就相当于以前我们发送短信好像短信有个短信的回值说收到了
[03:26] 那么自动确认的意思就是消费者消息一旦收到自动给MQ说一声这个消息我收到了自动的好还有第三个呢callbackcallback就是我们回调的一个函数回调回调的一个对象那么将来呢它可以监听着一些方法自动的执行那些方法那么我们可以把前两个参数可以把它设置一下第一个呢我们把它复制过来这个队列的名称得一样好放这
[03:56] 放这之后呢第二个呢是否要自动的回确认啊出好哎出完了之后呢第三个consumer那么我们就写一个consumer好这个consumer呢我们给它创建出来一个local的一个对象OK那么它其实要的是一个consumer对象那么这个玩意呢它有这个接口我们可以来看一下点进去看一下你看它是个接口那么接口有没有实现类呢看一下有实现类其实有一个default consumer
[04:25] 那么我们就可以来去创建一个default consumer而default consumer的创建呢注意它只有一个构造方法传一个channel的这么一个构造那么换句话说呢它没有提供空餐的构造那么我们这个地方呢就需要去创建这么一个对象了等于new一个default consumer那么这里边呢把我们创建好的这个channel传进去
[04:52] 但是呢这个default consumer创建完了之后呢它是一个空的一个实现我们需要对它进行复写方法所以我们用匿名内部类的方式再去实现一下它里边对应的一个方法out insert我们override一个method哪个方法呢有一个方法就是handlerhandlerdelivery就是处理收到的消息好那么这个消息呢这个方法其实是一个回调方法我们把它写一个注释
[05:22] 这是一个毁掉方法回掉方法当收到消息当收到消息后会自动自动执行该方法那么这个方法里边又有一些参数可以简单的来说一下那么这些方法的参数呢好今天的方法参数稍微有点多第一个呢consumer tag这是一个
[05:58] 消息的这是标识啊唯一的一个标识那么第二个呢env loop这个呢是来获取啊可以来获取对应的一些信息啊获取一些信息什么信息呢比如说交换机的信息啊什么什么routing key的信息啊路由key的一个信息啊等等哈那么第三个呢这是一个配置的一个property的一个信息啊
[06:27] 好这是一个配置的信息我们刚才是不是没有给配置的信息啊所以呢这个呢获取出来的数据呢就没有那么第四个呢就是我们最关心的body那么这个body呢就是我们真实的一个数据数据OK那么下来呢我们可以把这个信息呢给它打印一下sout一下我们一个一个来哈consumer tag好加上双引号加上我们写个写个冒号吧好
[06:58] 加上这个consumer tag我们复制几分啊复制几分呢第二个env这个那么env这个呢其实呢它是个对象啊我们可以用这个env点获取啊你看是不是可以获取它的routing key以及exchange呀我们可以来获取一下exchange那么我们这样吧我们把这个这个呢前面的打印的名称就要exchange了那么第二个呢env这个玩意呢获取一个routing key啊我们刚才说了其实这个routing key呢
[07:27] 跟我们对应的对联的名称是一样的如果你用默认的交换机的话那么第三个呢我们再来打印一下propertiesproperties也打印一下然后呢最后我们打印一下这个body这个body呢就是我们真实的数据了刚才我们说了我们发的数据呢叫做hello rapid mq对吧那么这个数据呢我们是一个字节数组我要把它转成一个字幕串所以呢我new string一下我把这个body呢给它放进去这样呢就转成了一个字幕串打印出来
[07:57] 那么这个消费者的代码其实也就写完了那么问一下消费者要不要去关闭资源呢消费者要不要关资源呀你注意啊消费者是不是相当于一个监听程序啊那你说你在这一直监听着等消息来了之后我然后去处理你把这个connection给它关闭了它还怎么监听所以呢消费者这个地方呢注意不要去关闭资源那么消费者弄完了之后呢我们把这个生产者给它停掉
[08:27] 然后呢我们把这个消费者呢给他开一下注意看好刚才这里边是不是有两条消息啊两条消息我们可以来看一下能不能把这两条消息给他拿到注意看我们打印的信息呢在这个地方呢注意啊我们打了一个两个三个四个五个一个两个三个四个五个这是不是一条消息下边是不是又是另外一条消息对吧可以来看一下这是
[08:53] 它的对应的消息的一个编号这是一个consumer的一个编号编号完事了之后呢exchange我们说了是一个空字物串所以呢它是个空的然后呢routing key你看是不是就是我们的对立名称然后呢properties配置信息这些配置信息里边是不是都是none因为我们没有传嘛然后呢body就是我们的消息消息呢叫做hello rabbit mq那么这样我们就收到了这两条消息那么至此呢我们的生产者和消费者的代码
[09:22] 都写完了写完了之后呢最后我们回到PPT来进行一个小结简单的去总结一下这些个生产者消费者的一些代码我们把它往后拉一下好简单的去做一个总结注意看我们在这个地方呢用了这种简单的模式简单模式里边呢有两个概念P呢是生产者C呢就是消费者红色的呢这是对列它呢类似于一个邮箱可以缓存一些消息
[09:51] 我们生产者投递完了消息之后呢你注意看消费者是不是过了一会儿启动了之后才去取的因为我们代码是先写的生产者发了消息之后我们看到了消息在队列里边了然后呢再编写的消息备者代码对吧OK那么这样呢我们的快速入门代码就写完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 RabbitMQ 的基础使用，通过 Java 代码演示生产者和消费者如何通过 Exchange 和 Queue 发送和接收消息。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了生产者代码文件 Producer_HelloWorld.java。
- 代码内容：String body = "hello RabbitMQ"; channel.basicPublish("hello_world", "hello_world", null, body.getBytes()); channel.close();
- 画面右上角有 RabbitMQ 的工作模式图：P（生产者）→ Exchange → Queue → C（消费者）。

画面2：
- 展示了消费者代码文件 Consumer_HelloWorld.java。
- 代码内容：public class Consumer_HelloWorld { ... }，光标位于类定义处。

画面3：
- 展示了多个文件和 PPT 页面的缩略图，包括 RabbitMQ 的安装与配置相关材料。
- 画面右上角有 RabbitMQ 的工作模式图。

画面4：
- 展示了消费者代码中创建 ConnectionFactory 的部分。
- 代码内容：ConnectionFactory factory = new ConnectionFactory(); factory.setHost("172.16.98.133"); factory.setVirtualHost("/"); factory.setUsername("heima"); factory.setPassword("heima"); Connection connection = factory.newConnection();

画面5：
- 展示了创建 Channel 的代码。
- 代码内容：Channel channel = connection.createChannel();
- 画面右侧有 channel.queueDeclare() 方法的注释说明。

画面6：
- 展示了声明队列的代码。
- 代码内容：channel.queueDeclare("hello_world", true, false, false, null);
- 画面右侧有方法参数的注释说明。

画面7：
- 展示了 RabbitMQ 客户端库的类文件结构。
- 代码内容：Decompiled class file, bytecode version 52.0 (Java 8)。
- 画面右侧有 Channel 类的多个方法。

画面8：
- 展示了 RabbitMQ 客户端库的类文件结构。
- 代码内容：Choose Implementation of Consumer (10 found)。
- 画面右侧有多个 Consumer 类的实现。

画面9：
- 展示了消费者代码中创建消费者对象的代码。
- 代码内容：Consumer consumer = new DefaultConsumer(channel); channel.basicConsume("hello_world", true, consumer);

画面10：
- 展示了消费者代码中重写 handleDelivery 方法的代码。
- 代码内容：public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) { ... }
- 画面右侧有 Envelope 类的属性方法提示。

画面11：
- 展示了消费者代码中重写 handleDelivery 方法的代码。
- 代码内容：System.out.println("consumerTag: " + consumerTag); System.out.println("Exchange: " + envelope.getExchange()); System.out.println("RoutingKey: " + envelope.getRoutingKey()); System.out.println("properties: " + properties); System.out.println("body: " + new String(body));

画面12：
- 展示了消费者代码中重写 handleDelivery 方法的代码。
- 代码内容：System.out.println("body: " + new String(body));
- 画面下方有控制台输出：properties: ... body: hello RabbitMQ

画面13：
- 展示了 PPT 页面，标题为“1.6 RabbitMQ 简介”。
- 内容：Exchange: message 到达 broker 的第一站，根据分发规则，匹配查找表中的 routing key，分发消息到 queue 中去。Queue: 消息最终被送到这里等待 consumer 取走。Binding: exchange 和 queue 之间的连接，binding 中可以包含 routing key，Binding 信息被保存到 exchange 中的查询表中，用于 message 的分发依据。

画面14：
- 展示了 PPT 目录页。
- 内容：目录包括：MQ 的基本概念、RabbitMQ 的安装和配置、RabbitMQ 快速入门、RabbitMQ 的工作模式、Spring 整合 RabbitMQ。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
String body = "hello RabbitMQ";
channel.basicPublish("hello_world", "hello_world", null, body.getBytes());
channel.close();
```

画面4：
```java
ConnectionFactory factory = new ConnectionFactory();
factory.setHost("172.16.98.133");
factory.setVirtualHost("/");
factory.setUsername("heima");
factory.setPassword("heima");
Connection connection = factory.newConnection();
```

画面5：
```java
Channel channel = connection.createChannel();
```

画面6：
```java
channel.queueDeclare("hello_world", true, false, false, null);
```

画面9：
```java
Consumer consumer = new DefaultConsumer(channel);
channel.basicConsume("hello_world", true, consumer);
```

画面10：
```java
public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) {
    System.out.println("consumerTag: " + consumerTag);
    System.out.println("Exchange: " + envelope.getExchange());
    System.out.println("RoutingKey: " + envelope.getRoutingKey());
    System.out.println("properties: " + properties);
    System.out.println("body: " + new String(body));
}
```

画面11：
```java
System.out.println("Exchange: " + envelope.getExchange());
System.out.println("RoutingKey: " + envelope.getRoutingKey());
System.out.println("properties: " + properties);
System.out.println("body: " + new String(body));
```

画面12：
```java
System.out.println("body: " + new String(body));
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面13：
- 标题：1.6 RabbitMQ 简介
- 内容：
  - Exchange: message 到达 broker 的第一站，根据分发规则，匹配查找表中的 routing key，分发消息到 queue 中去。常见的类型有：direct (point-to-point), topic (publish-subscribe) and fanout (multicast)。
  - Queue: 消息最终被送到这里等待 consumer 取走。
  - Binding: exchange 和 queue 之间的连接，binding 中可以包含 routing key，Binding 信息被保存到 exchange 中的查询表中，用于 message 的分发依据。

画面14：
- 标题：目录
- 内容：
  - MQ 的基本概念
  - RabbitMQ 的安装和配置
  - RabbitMQ 快速入门
  - RabbitMQ 的工作模式
  - Spring 整合 RabbitMQ

5) 不要评价画面美观，不要输出与课程无关的内容。

