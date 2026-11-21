# 14_RabbitMQ工作模式-Routing

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\14_RabbitMQ工作模式-Routing_【海量资源尽在 ubkz.com】.mp4
- 时长 10分52秒（音频 652s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接下来我们来介绍Routing 路由工作模式那么这种模式还是稍微会有点麻烦为了让大家更好的理解这种模式首先我们先来提出一个小需求刚才我们注意看刚才我们做的这个小案例我们发送了一条消息然后发送了一个日志这个日志的级别是info那么它会把它打印到控制台上并且另外一个消费者也收到了一个info级别的日志将它存到了数据库
[00:30] 这样显然好像不是很合理对吧因为我们要存数据库的日志信息一般都是一些比较严重的日志信息比如像ERROR级别的日志信息我们才需要存到数据库你如果将INFO级别的日志信息也存到数据库那数据库早晚有一天会被人干挂掉所以现在我们的需求就是同一条日志的信息由不同的人收到了之后呢干不同的事情比如说
[00:59] 第一个堆列收到了之后它打印到控制台上没有问题但是呢它打印的是info级别的日志信息那么将来如果是error级别的信息呢我就需要让它存到数据库了这个可以理解吧那么这样的操作怎么来实现呢我们就需要用到这种routing的路由模式那么路由模式我们先来看这个图啊这个图跟刚才其实很类似啊还是一个生产者把消息发给交换机交换机再把消息呢
[01:28] 给转发或者说路由到对应的队列然后呢由不同的消费者来处理注意看中间这个路由的方式交换机呢如果收到了是error级别的信息它就走上边这个分支了走上边这个分支然后呢把这个信息呢给第一个队列第一个队列呢将来可能就需要把消息呢存到数据库去那么如果是error呢它还会走下边这个分支啊你注意看下边什么也有个error
[01:56] 那么也有个arrow呢它也会把消息打印到控制台上那是呢如果将来你给一个日日信息是info级别的那么上边这个分支就不会再走了只会将info和running的日日级别的信息打印到控制台上而不会存储到数据库那么这样的系统设计起来应该更加合理所以呢这个地方我们要来完成这种需求我们就需要用到这种routing key什么叫做routing key呢
[02:25] 将来我们的交换机跟这个Q对列绑定的时候需要设置对应的routingK那么只有当消息发送的时候的routingK跟绑定的routingK一致的时候才能对应上这个对列存到这个对列也就是说将来在这个地方我们截个图其实呢将来在发送消息的时候我们把这个图呢给它简单的说一下就是将来在这个地方发送的时候这个地方
[02:55] 也会有一个routing k的在这个地方也有个routing k然后呢只要跟这个要匹配上才能到对应的对立那么当然我们把这个图呢还是一样放到这个U上角那么下来呢我们就可以来编码来实现刚才我们所说的这个需求我们把刚才的代码呢都给它停掉了停掉之后呢我们接下来来写代码还是一样我们来写这个生产者的代码复制一份这个地方呢我们就不叫pub sub了叫routing r o u
[03:25] T Routing的方式那么这个Routing的方式呢我们一样的我们在这个地方呢同样要去起交换机的名字那么这个交换机的名字这个时候呢我们就不能再用这个Fanout这种这种交换机的类型了我们需要换一个类型叫做DirectD R I E C T这么一个类型当然这是个名字类型应该在这个地方换Direct这种类型那么这种类型就要求你这一块
[03:55] 发消息指的RoutingK和将来绑定使用的RoutingK得一样才可以好嘞那么这两个地方我们一改然后呢我们把这个名字也给它改一下好改一下这个名字都改一下好改完了之后呢其他的地方暂时先不用去改造那么绑定的时候要注意啊这个地方呢我们要注意绑定对列交换机的时候这个地方这在声明
[04:23] 绑定的时候在哪呢在这个地方去绑定的实际上还是这个交换机和这两个队列分别绑定但是呢绑定的时候呢你看好第一个队列第一个队列第一个队列干啥呢第一个队列是不是要完成一个error级别的的信息的一个输出啊所以呢第一个级别绑定的是error级别的没问题吧那么第二个绑定的谁呢第二个队列跟这个交换机绑定然后呢他绑定的是info
[04:52] 好info那么有的同学说那你这玩这三个呢这才一个呀那你绑定三次不就行了吗好三次吧好EROR然后呢WARNINGWARNING注意看这是对列一的绑定对列一的绑定绑定的是EROR然后呢下边这是对列二的一个绑定注意绑定
[05:21] 然后绑定的是infoeror然后warningWARNING这将来如果路由K是下边三种都会走到C2里边去好那么这个body我们先不去换那么这个时候注意上面这样弄完了之后我们的队列和交换机的绑定就完成了
[05:45] 那么下面呢我们最关键的发送消息的时候除了指定交换机我们是不是还要指定这个消息对应的一个叫做routing k啊OK吧那么现在呢比如说我就让它叫infoOK吧叫info那么叫info之后呢我们发送完消息那么我们来运行一下注意看啊如果我们这个地方routing k是info发到了这个交换机里边去那么这个时候我们来问一下
[06:13] C第一个对列还能收到这个消息吗当然不了嘛刚刚说过是吧只有第二个对列是不是才可以收到个消息啊我们可以来看一下这个里边的来看一下这是不是有两个第一个对列你看是不是没有消息第二个对列是不是有消息我们同样呢也可以看一下Exchange对应的一个绑定的方式你看好它是不是绑定了这么两个对列只不过第二个对列绑定了三个Routing K而已嘛对吧好嘞
[06:42] 那么这样弄完了之后呢接下来我们就可以把消费者一次给他写一下消费者也是非常简单的我们来复制一个刚才的就可以了这个呢叫做routing1routing1routing1里边呢我们只需要把这个名字换一下就行了是吧这个地方叫做direct1
[07:07] 当然你只需要一个direct1就可以了因为两个我是为了待会复制起来比较方便direct1好然后在这里边direct1我们把它Q1就是Q1现在Q1做的不是打印控制台Q1我们做的是这个地方将日志打印的控制台也行吧OK吧这倒无所谓的事情然后我们再复制一个复制一个复制一个routine2注意routine2
[07:36] Routing2我们要干的事呢这个地方呢我们只需要把这个Q2是不是给它改一下就行了改一下之后呢将信息存储到这就不是打印控制台了这个是将信息存储到数据库对吧存储到数据库OK吧好那么下来呢我们就可以来去分别启动这两个Routing1和Routing2对吧那么现在哪个有消息啊是不是Q
[08:02] Q2有消息对吧这个写反了对吧我们在这个地方呢存储的数据库呢应该是Q1对吧然后呢打印的信息呢应该是Q2好改一下改一下之后呢我们分别来启动一下这两个消费者好启动一下注意看情况你看好现在呢是info级别的是不是打印的控制台上这个可以收到消息啊然后呢来看我们对应的routine2呢哎routine2起了吗还没起是吧我们来起一下
[08:32] 起一下看Routine2能收到消息吗你看它是不是收不到消息啊对吧收不到消息啊只有这个能收到消息那么下来我们再来验证哈再来验证比如说我再来发送消息啊注意现在这些配置相当于都配好了那么现在呢就可以来发送消息了将来可能就执行这两句话就可以了现在呢我们发一个张三调用了哪个方法呢比如说Delete方法这个Delete方法就是非常危险的方法OK吧当然了
[09:00] 而且呢调用这个方法呢还出错了出错了出错误了当然这个呢日日级别就很高比如说叫做arrowarrow级别的error级别的那么这个arrow级别的呢当然你这写arrow没有什么用啊主要是个routing k这个地方这个地方写arrow没问题吧那么现在这个地方写arrow了之后呢这两个对列是不是都能收到消息啊是这样的好那么我们可以来运行一下稍等正在运行
[09:32] 运行一下之后呢我们来看第一个第一个打印控制台是不是收到了呀因为这边是不是也绑定了然后再来看第二个存储数据库是不是也收到了OK吧就是这个样子将来呢如果说我们的日志级别不一样比如说我们随便再换一个Warning日志的级别不一样将来呢就可以去限定哪些队列可以收得到哪些队列呢收不到当然这个地方呢我们就不改了如果是Warning的信息我们可以来看一下
[10:00] 那么就是只能打印控制台存储数据库它就收不到了可以来看一下打印控制台是不是收到了刚才这条信息是上一次的嘛是吧然后存储数据库是不是没收到因为这个地方是不是两条这个地方只有一条对吧好嘞那么这就是我们所说的Routing路由的方式那么路由的方式呢我们讲完了那么下来呢我们来简单的总结一下总结一下说Routing模式要求对列在绑定交换机的时候
[10:29] 指定routing k是不是要指定routing k消息转发给符合routing k的一个对列其实你在发送消息的时候是不是也要指定这个routing k啊而且要注意啊注意的啥呢注意这个交换的类型得是direct才可以哈好嘞那么到这我们的对应的一个routing的模式我们就讲解完毕

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 RabbitMQ 的 Routing 路由模式，通过代码演示如何创建交换机、绑定队列和发送/接收消息。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Producer_Publish.java 文件中的代码，用于向名为 "test_direct" 的交换机发送消息，但未绑定队列，导致消息无法被消费。
画面2: 代码中注释了 "test_direct" 交换机的创建和绑定逻辑，但未实际执行。
画面3: 展示了 RabbitMQ 的 Routing 路由模式架构图，包含生产者 P、交换机 X、队列 C1 和 C2，以及路由键 error、info、warning。
画面4: 展示了 Producer_Routing.java 文件中的代码，创建了名为 "test_direct" 的 direct 交换机和队列，并绑定。
画面5: 代码中注释了 "test_direct" 交换机的创建和绑定逻辑，但未实际执行。
画面6: 代码中注释了 "test_direct" 交换机的创建和绑定逻辑，但未实际执行。
画面7: 展示了 RabbitMQ 管理界面的 Exchanges 页面，列出了包括 "test_direct" 和 "test_fanout" 在内的多个交换机。
画面8: 展示了 Consumer_Routing.java 文件中的代码，创建了连接工厂并设置连接参数。
画面9: 代码中注释了 "test_fanout" 交换机的创建和绑定逻辑，但未实际执行。
画面10: 代码中注释了 "test_fanout" 交换机的创建和绑定逻辑，但未实际执行。
画面11: 展示了 Consumer_Routing.java 文件中的代码，创建了消费者对象并设置回调方法。
画面12: 代码中注释了 "test_direct" 交换机的创建和绑定逻辑，但未实际执行。
画面13: 代码中注释了 "test_direct" 交换机的创建和绑定逻辑，但未实际执行。
画面14: 展示了 PPT 页面，标题为 "4. RabbitMQ 的工作模式"，子标题为 "4.3 Routing 路由模式" 和 "2. 代码编写"，并附有路由模式的架构图。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1:
```java
String body = "日志信息：张三调用了findAll方法...日志级别：info...";
channel.queueBind(queueName, exchangeName, "");
channel.basicPublish(exchangeName, "", basicProperties: null, body.getBytes());
channel.close();
connection.close();
```

画面4:
```java
String exchangeName = "test_direct";
channel.exchangeDeclare(exchangeName, BuiltinExchangeType.DIRECT, true, false, false, null);
String queueName = "test_direct_queue";
channel.queueDeclare(queueName, true, false, false, map);
channel.queueBind(queueName, exchangeName, "");
```

画面6:
```java
channel.queueBind(queueName, exchangeName, "error");
channel.queueBind(queueName, exchangeName, "info");
channel.queueBind(queueName, exchangeName, "warning");
```

画面8:
```java
factory.setHost("172.16.96.133"); // 默认 5672
factory.setPort(5672); // 默认 5672
factory.setUserName("heima"); // 用户名
factory.setPassword("heima"); // 密码
Connection connection = factory.newConnection();
Channel channel = connection.createChannel();
```

画面11:
```java
new DefaultConsumer(channel) {
    @Override
    public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) {
        System.out.println("Exchange: " + envelope.getExchange());
        System.out.println("RoutingKey: " + envelope.getRoutingKey());
        System.out.println("Properties: " + properties);
        System.out.println("Body: " + new String(body));
        System.out.println("消息主体已存储到数据库...");
    }
};
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14:
PPT 标题: "4. RabbitMQ 的工作模式"
子标题: "4.3 Routing 路由模式"
子标题: "2. 代码编写"
架构图: 生产者 P -> 交换机 X -> 队列 C1 (路由键: error, info)
架构图: 生产者 P -> 交换机 X -> 队列 C2 (路由键: error, warning)

5) 不要评价画面美观，不要输出与课程无关的内容。

