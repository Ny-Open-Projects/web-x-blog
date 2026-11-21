# 10_高级特性-延迟队列-代码实现

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\10_高级特性-延迟队列-代码实现_【海量资源尽在 ubkz.com】.mp4
- 时长 14分26秒（音频 867s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 介绍完延迟对类的基本的概念以及它的使用方式之后接下来我们就在代码中来实现这么一个功能那么为了让大家更好地理解这个流程我们还是一样把这个图截一下给它贴到桌面的右上角贴过来之后呢我们参照这幅图来完成订单库存取消库存这么一个功能当然在这我们肯定不去操作数据库了
[00:29] system.out的方式来输出一些日志来看一下主要就是来实现一个发完消息之后过一会儿才能收到消息这么一个延迟的功能那么首先呢其实你会发现啊这个东西跟刚才我们写的那个死性交换机的代码是很类似的首先还是要定义正常的对列正常的交换机定义死性的交换机和死性对列然后呢他们做一个绑定给正常对列再设置一个过期时间对吧
[00:59] 就完事了其实代码没有什么我们来实现一下那么实现一下呢我们写一个注释吧写个注释这个地方呢叫做死性不是死性啊叫做延迟对立延迟对立呢第一个我们还是要定义正常的交换机交换机和对立然后呢第二个呢我们要去定义
[01:28] 死性的交换机和对列对吧然后第三个去绑定那绑定完事之后呢你还需要去设置正常的对列过期时间对吧为30分钟这样我们的整个的延迟对列这么一个功能架子就打好了然后呢写个生产者发消息写个消费者收消息代码就写完了
[01:55] 那么我们首先先给这个正常交换机和对列起个名字正常的一个交换机我们就起名为order吧order-q好因为是订单系统的消息对吧然后对order-exchange这是交换机s-a-h-a-n-j-e那么正常的这个对列呢我们也要order-q那么如果是死性的话呢我们只需要在这个后边给它加个后置就可以了加一个下滑线
[02:24] 下滑线DLX那么同理啊这个地方呢也同样加一个下滑线DLX好嘞那么这个基本的逻辑我们分析完了之后接下来就来写代码写个注释第一步我们看这个是定义正常的正常这个玩意呢我们还是一样我们把这个Q呢给它写一下不是QargumentsQ由一由一Q然后呢ID这个名我们已经起好了outer刚Q
[02:55] 好下来呢就是namename呢也叫这个名然后接下来正常的交换机我们叫做topic的exchange名呢也起好了order-exchange并且呢去绑定一下这个对列partner呢我们就写order.警号了然后呢对列呢我们就绑定的是order-q这个正常的我们就定义完了然后呢死性的跟正常的没有什么区别所以我们复制一遍复制一份出来呢
[03:26] 我们把这个注释给它修改一下把名字呢做一个替换orderq-dlx给它替换一下替换一下交换机的名字呢也替换一下好然后替换完事之后呢这个地方我们给它加一个dlx.order.仅号那么死性的和正常的这两个都定义完了定义完了之后呢下来是不是就绑定啊在正常的对列这一块呢我们来做一个第三步
[03:56] 绑定和设置过期时间这么一个动作那么接下来呢我们来去设置这个队列的参数还是那句话设置参数你这些参数的键的名称不要去记号我们只需要去复制一下就可以了刚才我们也说了说我们这个队列要去绑定一个死性的交换机需要设置两个参数第一个参数呢是死性交换机的名称第二个是路由的K
[04:24] 那么下来呢我们在这里边复制一下这是对列对列里边呢我们给它设置一个参数叫做死性交换机的名称好交换机的名称呢我们给个value交换机的名称刚才我们也看到了叫做order-exchange-dlx然后呢接下来我们第二个事第二事呢我们复制一份吧复制一份呢就是路由的k我们再来看一下叫这个名沾过来之后呢
[04:55] 把它放在这个地方路由的k呢我们刚才起的是dlx.order.仅号那么我们这个地方呢因为它是要取消库存所以呢我们给它起个实际的意义cancel吧cancel好第三个事呢我们还要去设置一个东西叫做过期时间那么过期时间呢我们再把这个ttl也给它设置一下
[05:20] 那么TTL这块呢我们就不设置30分钟了因为30分钟我们实在是等不起啊我们就给它设置10秒钟就可以了10秒123好10秒并且呢设置一下这个value的type加完点long点integer好那么这样我们的对列和交换机声明绑定的关系我们就弄完了弄完了之后接下来我们在test里边可以先做这么第一件事
[05:48] 我们在这里边呢可以来发送消息好写一个cherry test好test然后呢叫做public void叫做test delete吧delay就是延迟对的延迟的意思那么在这里边呢我们什么都不做什么都不做的目的是啥呢我们当这个方法一旦运行的之后呢这里边是不是就会创建出来这个交换机和对立以及他们的绑定关系啊要不是待会儿我先启动这个生产者会报错的
[06:17] 所以呢我们可以这样先运行一下运行一下之后呢我们看一下这个绑定的关系有没有建立出来哈稍等好运行成功了之后呢我们来看一下这边来看一下稍等我们可以刷一下刷一下之后呢哎哎这个地方是没有建立出来哈说明他还没有去发送消息的时候呢是不是就没有建立出来啊那没有关系啊我们就给他随便呢在这个地方执行一下其他的一个方法执行下这个方法也是可以的好执行一下
[06:48] 我们想让他提前把这些对列给他创建出来创建一下之后呢你看是不是有了order开头的这两个对列以及对应的一个交换机来看一下order开头的交换机是不是也有了OK有了之后呢接下来我们再重新来编写这个代码那发送消息就非常简单了我们在下边来发送消息发送消息呢我们就来发送订单消息
[07:16] 这个地方呢其实将来啊将来是在订单系统中下单后成功后去发送的消息啊我们现在就模拟啊rabbit template.convert and send你注意是不是要给正常的这个交换机和对列发呀所以呢这个地方写的这个名字我们来看一下交换机的名称把它复制过来就可以了叫做order exchange它的一个路由k是order.仅号
[07:46] 好这个地方我们把它粘过来然后呢这是交换机的名称路由K呢是order.我们比如说叫做messageorder信息然后呢接下来我们给一个订单的信息啊就是说订单信息好比如说ID写个1对吧然后逗号然后呢再写一个比如说它的下单的时间time等于写个时间吧随便写一个
[08:14] 好嘞那么这样呢我们的代码呢就写完了消息就发出去了那么为了让大家待会能看到一个10秒钟之后这里边才会收到消息这么一个过程所以呢在这个地方呢我们给它打印一下东西打印一个倒计时啊10秒将来肯定是不用的好for ifor i呢i等于10吧倒计时嘛i大于0大于0i减减
[08:46] 然后呢我们直接再打印一下这个i就可以了我们再加一个点点啊然后没打完一次呢我们给它休眠一秒钟啊sleep一下打完一次睡一秒那么这样过十秒钟之后就能打印出来这么十个数字了那么这个生产者的代码就这样编写完了写完了之后呢下来我们来写对应的消费者消费者呢也是比较容易的
[09:14] 消费者的代码呢我们还是一样我们给他找一个复制一个就可以了复制一个之后呢我们这个地方叫做orderorderlistener那么在orderlistener里边呢我们这样吧我们把这上面的下边的代码往下拉一下要不是看不见了orderlistener里边呢首先呢我们还是来接收消息打印消息没有问题那么处理业务逻辑这块呢其实他要处理的我们就不让他抛一长了
[09:39] 我们其实要干这么几件事第一件事我们要去根据这个订单的ID去查询其状态对吧好状态当然这个将来肯定是要调用业务层的查询数据库的一个方法来查询的那么这一块我们就不查询了我们直接打印日志然后第二个呢我们要去判断判断这个状态好状态是否是否为
[10:08] 支付成功对吧还有个状态是零啊还是一啊等等是吧那么如果没有支付成功呢我们应该干的事是取消这个订单然后呢回滚库存好那么这些操作如果都做完了对吧那么这个消息是不是就应该手动签收那么如果出现异常呢是不是就拒绝签收啊对吧那么这个代码就写完了
[10:32] 当然我们主要看的是这个消费者这一端是否是延迟了10秒钟之后才收到了消息那么这边order listener也写完了之后最后一件事我们在这里边注册一下好复制一份把上边这个给他注释掉注释掉之后呢这个里边呢我们叫做order listenerorder listener好嘞下边来监听的队列呢你注意啊格外这个地方要注意
[11:00] 他监听的可是这个死性的对立你如果监听这个正常的对立那么这个正常的对立是不是消息一来他就收到了只有这个死性的对立才有延迟的功能因为在这里边只有这个正常的对立消息过期了之后才会到这个死性的对立里边来是吗所以呢要监听这个死性的对立那么这个死性的对立这个名字呢我们可以来看一下这个名字好往下拉这个对立呢叫做Outer Q
[11:27] -DLX这个地方格外要小心好我们这个地方来写个注释延迟对立效果实现然后呢一定要监听的是这个死性对立啊探探探好很重要这句话那么这边也写完了之后接下来我们就可以来模拟实现这么一个效果了
[11:57] 那么首先呢我们先把这个地方的一个测试用力给它启动起来好稍等好嘞测试的消费呢就启动起来了启动起来之后呢我们来发送消息发送消息好我们把这个图呢我们就不要了不要了之后呢我们接下来发送能看到的哎不是这个哈下边这个这个方法test-delete是吧delete那么这个方法将来是这样的
[12:28] 你消息一旦这句话一直行消息就发出去了然后开始倒计时倒计时完成之后我们才能在这个消费的控制台上看到消息打印出来了那么你在发送立马发送之后是看不到的来看一下效果稍等走走一下之后呢看一下现在呢我们来看稍等啊你看开始打印了吧但是这边是不是没有消息啊对不对
[12:56] 这个消息其实已经发出去了但是这边没有收到只有这个消息时间打印完了过了10秒钟之后这边才能看到看这边是不是收到了对吧OK啊那有同学说你这个没有变绿条啊是因为我这个代码呢是不是阻塞了我们这样吧我们把它注释了我们不打印了你可以看一下这个效果我们重新来把这边呢也干掉干掉之后呢你注意现在来看好走发送消息其实这句话一执行消息就发出去了你看
[13:25] 它立马就会变成绿条绿了吧但是这边呢有延迟会等一会儿等多久呢10秒钟之后才能收到这个消息并且呢才能来判断这个订单是否支付成功OK这样我们就实现了这么一个延迟对列的一个效果怎么实现的呢TTL加死刑对列那么接下来最后我们来进行一个延迟对列的小结第一个延迟对列是指的是
[13:55] 消息进入对列之后可以被延迟一定的时间再进行消费这就是延迟对列的概念啊非常常见的常用的这么一个概念那么第二个就很关键了说RubitMQ呢它没有提供延迟对列的功能但是呢我们可以使用TTL加上DLX就是死性交换机来实现和延迟对列同样效果的这么一个功能OK那么对于延迟对列我们就讲解
[14:25] 完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 RabbitMQ 的 TTL + 死信队列机制实现订单延迟处理功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- PPT 标题：1. RabbitMQ 高级特性，子标题：1.6 延迟队列。
- 文字内容：很可惜，在RabbitMQ中并未提供延迟队列功能。但是可以使用：TTL + 死信队列 组合实现延迟队列的效果。
- 图形：展示订单系统 → Exchange → Queue → 库存系统 的流程，Queue 指向“库存系统”并标注“设置队列过期时间为30分钟”，同时 Queue 指向“死信队列（DLX）”。
- 图形标注：死信队列（DLX）指向“库存系统”并标注“判断订单状态”，然后分叉为“支付”、“什么都不做”、“取消订单，回滚库存”。

画面 2:
- IDE 界面：显示项目结构和 `spring-RabbitMQ-producer.xml` 文件。
- XML 配置代码：
```xml
<rabbit:queue name="queue_dlx" id="queue_dlx"><rabbit:queue>
<rabbit:topic-exchange name="exchange_dlx"><rabbit:exchange>
<rabbit:bindings>
    <rabbit:binding exchange="exchange_dlx" queue="queue_dlx" />
</rabbit:bindings>
</rabbit:exchange>
</rabbit:queue>
</rabbit:bindings>
```

画面 3:
- RabbitMQ Management 界面：显示队列列表，包含 `queue_dlx`、`test_queue_confirm`、`test_queue_dlx`、`test_queue_ttl`。
- 队列特性：`queue_dlx` 标记为 D（Durable）、DLX、Q（Queue）；`test_queue_dlx` 标记为 D、TTL、DLX、Q。

画面 4:
- RabbitMQ Management 界面：在“Add a new queue”区域，Arguments 部分显示：
  - x-dead-letter-exchange: String
  - x-dead-letter-routing-key: String
  - x-message-ttl: String

画面 5:
- IDE 界面：显示 `ProducerTest.java` 文件，`testDlx()` 方法中包含注释“测试过期时间，死信消息”和“测试长超时后，消息死信”。
- 代码片段：
```java
// 测试长超时后，消息死信
for (int i = 0; i < 20; i++) {
    rabbitTemplate.convertAndSend("test_exchange_dlx", "test.dlx.haha", "我是一条消息，我会死吗？");
}
```

画面 6:
- RabbitMQ Management 界面：空白页面，仅显示“HTTP API | Command Line”。

画面 7:
- RabbitMQ Management 界面：显示队列列表，包含 `order_queue`、`order_queue_dlx`、`queue_dlx`、`test_queue_confirm`、`test_queue_dlx`、`test_queue_ttl`。
- 队列特性：`order_queue_dlx` 标记为 D、TTL、DLX、Q；`test_queue_dlx` 标记为 D、TTL、DLX、Q。

画面 8:
- IDE 界面：显示 `ProducerTest.java` 文件，`testDelay()` 方法中包含注释“测试消息延迟”。
- 代码片段：
```java
// 测试消息延迟
rabbitTemplate.convertAndSend("test_exchange_dlx", "test.dlx.haha", "我是一条消息");
```

画面 9:
- IDE 界面：显示 `ProducerTest.java` 文件，`testDelay()` 方法中包含注释“测试消息延迟”。
- 代码片段：
```java
@Test
void testDelay() throws InterruptedException {
    // 发送订单消息，待业务处理中，下订单成功后，发送消息
    for (int i = 1; i <= 10; i++) {
        rabbitTemplate.convertAndSend("order_exchange", "order.msg", "订单信息：id=" + i + ",time=" + System.currentTimeMillis());
        Thread.sleep(1000);
    }
}
```

画面 10:
- IDE 界面：显示 `OrderListener.java` 文件，`onMessage` 方法中包含注释“处理业务逻辑”。
- 代码片段：
```java
@Override
public void onMessage(Message message, Channel channel) throws Exception {
    long deliveryTag = message.getMessageProperties().getDeliveryTag();
    System.out.println(new String(message.getBody()));
    // 处理业务逻辑
    System.out.println("处理订单业务逻辑...");
    System.out.println("根据订单状态更新库存...");
    System.out.println("判断状态是否为未支付成功");
    System.out.println("取消订单，回滚库存...");
    // 手动确认消息
    channel.basicAck(deliveryTag, true);
}
```

画面 11:
- IDE 界面：显示 `spring-RabbitMQ-consumer.xml` 文件。
- XML 配置代码：
```xml
<rabbit:connection-factory id="connectionFactory" host="172.16.88.133" port="5672" username="guest" password="guest" virtual-host="/"/>
<context:component-scan base-package="com.itheima.listener" />
<rabbit:listener-container connection-factory="connectionFactory" acknowledge="manual" prefetch="1">
    <rabbit:listener ref="orderListener" queue-names="test_queue_confirm" />
    <rabbit:listener ref="divListener" queue-names="test_queue_dlx" />
</rabbit:listener-container>
```

画面 12:
- IDE 界面：显示 `ConsumerTest.java` 文件，`testDelay()` 方法中包含注释“测试消息延迟”。
- 代码片段：
```java
@Test
void testDelay() throws InterruptedException {
    // 发送订单消息，待业务处理中，下订单成功后，发送消息
    for (int i = 1; i <= 10; i++) {
        rabbitTemplate.convertAndSend("order_exchange", "order.msg", "订单信息：id=" + i + ",time=" + System.currentTimeMillis());
        Thread.sleep(1000);
    }
}
```

画面 13:
- IDE 界面：显示 `ConsumerTest.java` 文件，`testDelay()` 方法中包含注释“测试消息延迟”。
- 控制台输出：
```
订单信息：id=1, time=2019-09-17 16:41:47
处理订单业务逻辑...
根据订单状态更新库存...
判断状态是否为未支付成功
取消订单，回滚库存...
```

画面 14:
- PPT 标题：1. RabbitMQ 高级特性，子标题：1.6 延迟队列小结。

