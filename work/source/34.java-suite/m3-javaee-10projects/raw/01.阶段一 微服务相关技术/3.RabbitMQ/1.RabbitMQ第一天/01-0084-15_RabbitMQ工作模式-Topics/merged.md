# 15_RabbitMQ工作模式-Topics

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\15_RabbitMQ工作模式-Topics_【海量资源尽在 ubkz.com】.mp4
- 时长 11分26秒（音频 686s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接下来我们来说最后一种工作模式Topics通配服模式它呢功能也是最为强大的一种模式那么我们可以来看这两幅图首先看左边这幅图还是一样生产者发消息给Exchange交换机交换机再把对应的消息路由到不同的对列里边去那么这个时候呢首先呢这个交换机指的类型是Topic那么你注意看它路由或者说绑定对列的时候
[00:30] 它指定的这个路由K是带新号下边是带仅号的是一种表达式的形式那么这种表达式的形式呢里边新号表示了恰好一个单词而仅号表示零个或多个单词那么也就是说将来我们在发送消息给一个路由K比如说A.orange.c然后呢这个时候发了一个路由K到这个里边来
[00:56] 然后呢就能匹配到这个新.orange.新这么一个路由K两个匹配了之后呢就会把消息分发到Q1里边来那么这个了解了之后呢我们可以来看这边这幅图这幅图里边你注意看这里边呢Qs里边在exchange和Q绑定的时候呢它有这么一个通配符的一种方式比如说第一个usa.警号然后呢警号.news
[01:25] 那第一个呢相当于以USA开头的消息我都可以接收第二个呢是以News结尾的消息我都可以接收第三个以Weather结尾的第四个以这个玩意结尾开头的是吧那么上来上来我们来看它发送消息的时候发送消息的时候呢指定了很多的一个路由K比如说第一个USA.News那么USA.News这个
[01:50] 路由K跟谁匹配呢我们可以来看一下第一个usa.jim号可不可以匹配因为jim号代表零个或多个嘛后边news就可以忽略掉是吧所以呢第一个可以匹配而us.news它是不是以news结尾所以呢以这个结尾的是不是也可以发换句话说将来这条消息发过来之后呢第一个队列和第二个队列是不是都可以收得到大概就是这么个意思啊那么知道这个意思之后呢还是一样我们来截一幅图
[02:20] 接完一个图之后呢我们来写个代码代码一写大家其实基本上就能明白这个东西了这里边有两个关键点第一个呢就是它的交换机类型是topic第二个呢你要知道通配符新代表一个单词仅号代表零个和多个而且呢它们的对应的这个路由k必须里边是以点和多部分组成的好嘞那么下来我们来写代码写代码之前呢我们来提出一个小的需求刚才啊我们发现我们用那个
[02:49] 用那个刚才我们发的这个叫做direct的方式或者说routing的方式我们都可以进行一个消息的分发那么direct的方式呢它是不管3721它将消息发给每一个队列而我们的routing方式呢可以指定定向的去发送但是routing的方式呢它只能指定一个参数就是说我比如说我控制error级别的日志对吧我要监控存到数据库
[03:17] 但是现在我有一个新的需求需求就是什么呢需求是我现在除了error级别的信息我还想把订单系统里边的所有日志我都需要去监控就是除了error级别的还有订单系统里边的不管什么级别的信息我都想去监控一下那这个时候呢我们将来的一个日志的路由K就有两部分组成了一个是系统的名称.
[03:46] 日志的级别那么这个时候怎么来完成我们来写代码好我们来复制一下这个地方呢我们叫做topictopic好那么在topics里边呢我们一样我们先把这个名字exchange交换器的名字改成topic然后呢对应的这个对列的名字呢我们也改成topic好改一下
[04:15] 改完了之后呢接下来我们来进行一个绑定的动作那么在绑定的时候呢注意看在绑定的时候在这个声明的时候这个里边声明的时候就是绑定的时候那么绑定的时候呢是不是要指定对应的一个路由K啊那么这个路由K呢注意这个绑定的时候呢路由K是不是有两部分组成这个路由K啊我们来写一下这个R O U T I N GROTING K它呢是两部分
[04:44] 第一部分呢是系统的名称好点日志的级别的级别级别那我的需求是啥呢我的需求是所有EROR级别的日志存数据库然后呢所有orderORDRorder系统的日志存入
[05:15] 因为order非常重要,我希望把所有的日志都存在数据库里面所以我们在绑定的时候,Q1和这个extrins绑定的时候我们可以这样来绑定我们可以写第一个,它以order结尾,前边以error结尾前边我不管是啥,比如说我们这个地方为了让大家两个通配服都用一下这个地方我就用仅号了,仅号.error1
[05:41] 其实我们明确的知道如果只有两部分的话对吧如果只有两部分的话用信号是不是也是没有问题的对不对OK当然用仅号也可以那么在这个地方第二种order下面的or d rorder d r比如说这个地方我就用信号好吧那么这两种是不是都要存数据库里面没问题吧当然这个地方还是要改成q1对吧q1和这两个都绑定然后再来q2
[06:10] Q2呢不管什么级别的信息我都期望打印到控制台上那怎么办呢那我就这样写嘛前边是新第二新只要是符合这个规则的是不是都可以OK吧那么下来呢我们就可以来去发送信息了那么发信息的时候呢这个时候呢我们来发一个比如说我们发一个other.info好那么将来这个信息发出去之后注意啊发出去之后是不是会被Q1和Q2这两个对立是不是都可以收到啊
[06:39] 对吧它应该都满足嘛这些条件那么这样弄完了之后呢我们可以来启动一下启动一下诶注意啊这个地方的启动肯定会有问题啊我们可以先来看一下这个里边的一个exchange交换机其实这个地方交换机呢我们少改了一个东西啊我们可以来看一下绑定的规则啊虽然这样绑定了是吧但是呢将来一定会出问题为什么呢因为我们没有去修改这个交换机的类型
[07:09] 还是我们刚才还是一种广播的类型是吧所以呢我们把这个先删除掉删除掉之后呢删掉删掉之后呢我们重新来去改一下这个类型之后我们再来启动啊改成类型改成topic啊这个地方一定要注意要改这个topic的类型改完了之后呢我们重新来启动好启动一下启动一下之后呢现在我们来看对列里边是否有数据信息啊
[07:36] 来看一下先看一下绑定的情况task topic来看是不是绑定了Q1是绑了两次Q2绑了一次对吧绑的是新点新那么接下来呢我们来看Q4是不是有两个对列两个对列一个topic Q1 topic Q2两个里边是不是都有消息了当然刚才是因为发送的第一次发送有问题啊所以呢这个地方呢我们删了重新发了一下而已好嘞那么这样弄完了之后呢接下来我们再来把
[08:04] 消费者也一写啊我们复制一份消费者这个地方呢我们就写topic1topic1topic1里边呢我们在这个里边呢第一个呢是把日志信息呢我们往上边比如说我们topic1我们看一下刚才的topics里边我们稍等我们看一下这个里边是要存到数据库1是要存数据库对吧那么这个地方呢我们就把这个名字改一下
[08:33] 改成topic1然后呢这个是topic2topic2好qename然后呢我们qename呢我们把它往下边qenameqename呢我们把信息呢存到数据库好存入数据库OK吧好然后呢接下来再复制一份topic2topic2呢我们希望把日志信息呢给它打印到控制台
[09:04] 把日志信息吸第五个打印打印控制台好这个是呢拖Q2完事了吧那么这样就写完了写完了之后呢我们可以来启动一下启动一下好再来启动一下这个注意看现在是不是每一个Q1和Q2都能收到两条信息啊好嘞那么都收到两条信息之后呢我们再来去测试我们再来测试发送端
[09:35] 发送端这一端呢我们找到topic就是发送端注意看然后呢现在我们发消息的时候呢我们需要改的是这个地方的路由k现在呢order.infook没有问题但是现在呢我不给order发了我给goo子发没问题吧goo子的info信息那么这个时候呢是不是只有对应的下边q2才能收到信息q1是不是就不匹配了对吧那么我们可以来看一下q2可以收到q1就收不到了
[10:05] 我们来运行一下这个生产者Q2可以收到吧可以是不是可以收到了Q1收得到吗是不是收不到我们可以再来改一个比如说我想改ERROR现在呢商品系统固执系统里边有个ERROR信息ERROR信息呢我们来运行一下这个时候是不是两个都可以收得到了稍等你看这边是不是收到了这边呢是不是也收到了这就是我们所说的TOPIC的一种模式
[10:36] topic的模式呢主要是可以用通配服让我们的控制或者说路由的规则更加的灵活我们可以来看一下说这个地方呢简单的去做一个小节说topic这个主题我们也可以称它为通配服的模式然后呢可以实现pubsub的功能也可以实现路由的功能只是topic呢在配置routingtale的时候可以使用通配服显得更加的灵活一些那么我们同时还说了
[11:05] 这个信号和警号分别对应的信号是一个单词警号是零到多个单词那么这个通配服模式我们也就讲解完毕了那么至此所有的模式除了最后一个RPC的模式我们没有讲之外其他的五种模式我们都讲解完毕

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 RabbitMQ 的 Topics 通配符模式，通过代码演示如何创建 Topic Exchange、绑定队列以及发送和接收带路由键的消息。

2) 按时间顺序列出每张画面的要点：
画面 1: PPT 标题为“4. RabbitMQ 的工作模式”下的“4.4 Topics 通配符模式”，展示了一个 Topic Exchange 的示意图，包含路由键模式：* .orange.*、*.rabbit.*、lazy.#。
画面 2: IDE 中展示 Producer_Routing.java 代码，定义了三个队列绑定到 Topic Exchange，路由键分别为 error、info、warning。
画面 3: IDE 中展示 Producer_Topics.java 代码，定义了 Topic Exchange 和三个队列的绑定关系，路由键分别为 * .error、*.order、*.*。
画面 4: RabbitMQ 管理界面显示了所有队列，包括 test_direct_queue1、test_direct_queue2、test_fanout_queue1、test_fanout_queue2、work_queue。
画面 5: RabbitMQ 管理界面显示了 Topic Exchange test_topic 的绑定关系，绑定到三个队列，路由键分别为 * .error、*.order、*.*。
画面 6: RabbitMQ 管理界面显示了所有交换机，包括 amq_direct、amq_fanout、amq_headers、amq_match、amq.RabbitMQ.trace、test_direct、test_fanout、test_topic。
画面 7: RabbitMQ 管理界面显示了所有交换机，包括 amq_direct、amq_fanout、amq_headers、amq_match、amq.RabbitMQ.trace、test_direct、test_fanout、test_topic。
画面 8: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 9: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 10: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 11: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 12: IDE 中展示 Producer_Topics.java 代码，定义了发送消息的方法，路由键为 goods.error。
画面 13: IDE 中展示 Producer_Topics.java 代码，定义了发送消息的方法，路由键为 goods.error。
画面 14: PPT 标题为“4. RabbitMQ 的工作模式”下的“4.4 Topics 通配符模式”，子标题为“2. 代码编写”。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 2:
```java
String exchangeName = "test_direct";
channel.queueDeclare(queueName, true, false, false, null);
channel.queueBind(queueName, exchangeName, "error");
channel.queueBind(queueName, exchangeName, "info");
channel.queueBind(queueName, exchangeName, "warning");
```

画面 3:
```java
String exchangeName = "test_fanout";
channel.exchangeDeclare(exchangeName, BuiltinExchangeType.FANOUT, true, false, null);
String queueName = "test_fanout_queue1";
channel.queueDeclare(queueName, true, false, false, null);
channel.queueBind(queueName, exchangeName, "");
```

画面 5:
```java
// 绑定关系
To Routing key Arguments
test_topic_queue1 * .error
test_topic_queue1 order
test_topic_queue1 *.*
```

画面 8:
```java
@Override
public void handleDelivery(String consumerTag, Delivery delivery) throws IOException {
    System.out.println("Exchange: " + delivery.getEnvelope().getExchange());
    System.out.println("RoutingKey: " + delivery.getEnvelope().getRoutingKey());
    System.out.println("Properties: " + delivery.getProperties());
    System.out.println("Body: " + new String(delivery.getBody()));
}
```

画面 12:
```java
String body = "日志消息：张三调用了findAll方法...日志级别：info...";
channel.basicPublish(exchangeName, "goods.error", null, body.getBytes());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: PPT 标题为“4. RabbitMQ 的工作模式”，子标题为“4.4 Topics 通配符模式”，架构图显示 P 指向 X，X 指向 Q1 和 Q2，Q1 指向 C1，Q2 指向 C2。
画面 4: RabbitMQ 管理界面表格数据包括 Virtual host、Name、Features、State、Ready、Unacked、Total、incoming deliver/get、ack。
画面 5: RabbitMQ 管理界面表格数据包括 To、Routing key、Arguments。
画面 6: RabbitMQ 管理界面表格数据包括 Virtual host、Name、Type、Features、Message rate in、Message rate out。
画面 7: RabbitMQ 管理界面表格数据包括 Virtual host、Name、Type、Features、Message rate in、Message rate out。
画面 8: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 9: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 10: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 11: IDE 中展示 Consumer_Topics.java 代码，定义了消费者处理消息的方法 handleDelivery。
画面 12: IDE 中展示 Producer_Topics.java 代码，定义了发送消息的方法，路由键为 goods.error。
画面 13: IDE 中展示 Producer_Topics.java 代码，定义了发送消息的方法，路由键为 goods.error。
画面 14: PPT 标题为“4. RabbitMQ 的工作模式”，子标题为“4.4 Topics 通配符模式”，子标题为“2. 代码编写”。

5) 无

