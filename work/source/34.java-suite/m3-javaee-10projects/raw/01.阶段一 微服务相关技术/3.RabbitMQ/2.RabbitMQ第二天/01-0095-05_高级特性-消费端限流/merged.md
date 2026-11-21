# 05_高级特性-消费端限流

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\05_高级特性-消费端限流_【海量资源尽在 ubkz.com】.mp4
- 时长 10分45秒（音频 645s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接下来我们来介绍RapidMQ高级特性的第三个消费端限流我想提到限流这个词大家应该并不陌生之前我们在介绍MQ的作用的时候介绍了说MQ有一个非常重要的作用消风填谷我们可以先来回顾一下这个作用在这个地方我有个系统A它每秒最大处理1000个请求但是呢由于某些原因当我们的
[00:30] 请求数目瞬间增多的时候A系统就承载不了了比如说A系统作为一个秒杀的活动然后这个时候呢很多用户一起来每秒5000个请求如果全部打到A系统上那么A系统肯定它会崩溃或者说当机掉从而影响整个业务的正常流转那么我们解决的方案我们也说了我们说我们可以将这5000个请求啊给它发到MQ去然后呢MQ在每秒
[00:59] 给A系统1000个请求也就是说A系统每秒从MQ里边拉取1000个请求来处理这样呢就能保证A系统的一个稳定性那么每秒从MQ拉1000个请求换句话说就是在消费这些消息的时候我们做了一个限流这么一个处理那么除了这样的业务场景之外还有一些场景比如说A系统将来有一天呢要维护它要停机
[01:28] 那么我的生产者这边是不是一直在发消息那么消息肯定没有被消费一直堆积在MQ里边那么将来A系统在维护好了在启动的时候很多很多消息一次打到A系统上来A系统也会挂掉所以我们要做限流是非常有必要的来保证系统稳定性的这么一个手段它也非常的重要那么介绍完了限流的重要性以及作用之后接下来我们就来
[01:57] 代码里边来去编写限流的代码限流这一块呢还是跟消费端有关所以这块呢我们先来复制一个消费端这个消费端呢我们就起个名叫QOSQOS呢其实翻译过来叫做服务质量保障将来在那个AMQP Client里边有个方法就是QOS所以这个地方我们就写QOS Listener好我们给它复制过来之后呢我们把这个注释呢给它删掉好
[02:26] consumer的一个限流机制好然后呢我们把这个里边的代码呢都给它删掉了删掉了删掉了之后呢我们的代码就成这个样子了那么接下来我们来说一下限流这个代码怎么写或者说怎么来处理限流其实非常的简单它只需要两步就可以了第一步要去保证要去确保确保它的签收或者说consumer的ACK
[02:56] ACK的机制为手动确认的因为你只有手动确认了之后呢它的限流才会生效那么刚才我们也讲了手动确认Acknowledge等于Menu那么第二个呢我们需要去配置一个属性在哪配置呢在我们的这个Consumer的这个Listener Container就是监听器容器里边去配置上配置属性在哪配置呢在这个里边配置属性
[03:25] 这个属性的名字叫做perfetch这个perfetch的具体的数值就是我们要能够拉取的消息的最大数目那么比如说你perfetch等于1那么也就是说一次只从MQ里边拉取一条消息来消费只有当这个消息消费完毕之后才会拉取第二条举个例子我们在这写一下配置了这个1之后呢表示
[03:55] 表示消费端每次从MQ拉取一条消息来消费直到直到直到他手动确认确认消费完毕后才会继续拉取下一条
[04:27] 条消息那么如果你配个R呢这个配个R呢就是说每一次拉取两条消息了那你要配个1000呢那就是一次拉取1000条消息了就这么一个意思好嘞那么接下来呢我们就可以来完成一个配置那么这个地方呢我们在这个地方呢它本来这个容器呢就是一种手动确认的方式所以呢这个无需再更改那么我们把perfect这么一个属性给它配一下
[04:56] professional等于比如说我们等于1好我们就先配个1来看一个效果就可以了那么配完1之后呢我们这个地方为了方便一点我们把这个这样吧我们把这个listener呢给它注释掉复制一份然后呢我们把上边这个给它注释掉也就是说上边的listener它就不生效了好那么下边这个listener呢我们起这个名字QOS这么一个listener好把它复制过来改成小写
[05:27] 好改完了之后呢还是监听刚才这个confirm这个队列这个队列里边来看现在没有消息了待会我们来发送消息就行了那么发完消息之后呢我们现在来看我们在这里边呢我们还是一样我们在这里边呢打印一下消息打印一下你有一个stream然后呢在这里边message dear dearget body好弄完了之后呢接下来第一步获取消息获取消息获取了消息之后呢
[05:56] 我们第二步要处理业务逻辑处理业务逻辑我们就不写代码了然后处理成功了第三步我们进行签收签收签收我们用channel.basicack然而我们这个地方要获取message的它的一个delivery card好然后这个地方multiple我们设为true多支好这样我们代码就写完了写完了之后我们现在把消费端给它启动起来
[06:26] 启动起来启动起来之后呢现在没有消息它所以呢它就一直在这等待着等待着之后呢你注意看现在呢我们在这个地方来发送消息发送消息为了让大家看到效果我们在这个地方呢我们这样我们在这个地方生产消息的时候呢我们还是在这里放i这样吧我们重新来复制一份这个方法这个方法呢我们就复制一份专门来发送消息就可以了
[06:54] 这个地方呢叫做test send好发消息然后其他的我们都不用去设置了我们就只是来处理发送消息就行了好那么发消息呢我们为了看到效果所以呢我们在这里边多发几条for i我们发上个十条吧好我们把这两行代码呢给它放到复寻环里边去那么这样呢一次就可以向这个队列里边发送十条消息那么发完了之后呢我们来看一下效果刚才呢我们发现
[07:24] 这个地方的代码呢我们是打印了消息打印完消息之后呢我们处理业务逻辑对没有做然后呢进行一个签收对吧那么现在呢为了让大家看到效果所以呢我把这个签收给它注释掉注释掉之后呢注意看哈我现在perfect等于1那换句话说呢一次只拉取一条消息消费那么只有当手动确认完毕后才会拉取下一条消息那么现在我没有进行手动确认那换句话说
[07:52] 将来我只能打印出来这么一条消息因为他认为这个消息没有处理完他不会从MQ里边拉取另外的消息来消费好我们来停止掉重新来启动这个consumer启动完consumer之后呢我们把这些log打删除掉然后呢我们来启动一个producerproducer这块呢我们找到test我们把这个10条消息的给它发过去
[08:19] 稍等一下我们来看一下这里边是不是只能收到一条消息呢稍等看是不是只收到这一条消息啊这是消息的一个body嘛那么我们现在来看一下管控台你看这里边是不是有9条消息代销费但是有一条未被确认呢是这样的吧好我们只收到了一条消息那么有同学说跟刚才好像没有什么区别啊这个时候呢你注意看好我现在如果说把这个停止掉
[08:47] 停止掉之后呢我们把consumer里边这个perfect给它干掉干掉之后呢你注意看我还是没有进行一个签收的动作在这个地方呢我还是没有签收那么现在呢我来启动一次它就会把这里边的消息全部拿过来你可以看一下你看这些消息是不是全部都拉过来了一次相当于拉了10条消息过来那么如果说我进行签收了之后我们再看一下效果好
[09:17] 我再签收签收完事了之后呢我还是一次性的只去消费一条消息我们再来看一下这个效果它就会一条一条拉曲那么为了让大家看到一个效果所以呢我在这个地方呢我就加一个睡眠Thread.sleep比如说睡上个一秒钟大家就可以看到一秒消费一条一秒消费一条这样的一个操作稍等一下现在呢没有消息
[09:46] 我们需要重新的去发送这个消息好send发一下发10条大家可以看一下你看这样呢就依次拉取一条消息来消费这样呢就保护了我们这个系统的一个稳定性所以呢我们这个消费端限流用起来是非常简单的我们来小结一下只有两个操作第一个操作呢你在那个RabbitListenerContainer这个里边去配置一个perfect属性
[10:14] 那么一次拉取多少消息那么你这个属性是多大就可以了比如说你配个500配个1000都是可以的那要根据你系统的一个承载的一个量来决定的那么第二个呢要注意消费端的确认模式一定为手动的确认因为将来它只有确认完毕这些消息消费完了之后才能够继续去拉取如果你是自动的那这个东西呢就不生效了好嘞对于消费端限流我们就讲解完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 RabbitMQ 消费端限流的实现原理与代码配置，包括如何通过 prefetch 属性控制消费速度和手动确认机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示消费端限流的架构图，用户 → MQ → A系统（每秒最大处理1000请求）→ DB。
画面 2: 显示 ConsumerTest 测试类和 OosListener.java 代码，其中包含注释说明如何设置手动确认和 prefetch。
画面 3: 代码编辑器中高亮显示 OosListener.java 中的 @Component 注解和 onMessage 方法。
画面 4: RabbitMQ 管理界面，显示名为 "test_queue_confirm" 的队列，其 Durability 设置为 Durable。
画面 5: 显示 OosListener.java 中的 onMessage 方法，其中包含注释说明如何设置手动确认和 prefetch。
画面 6: 显示 pom.xml 文件，其中包含 spring-RabbitMQ 依赖。
画面 7: 显示 ProducerTest.java 中的代码，包含 rabbitTemplate.convertAndSend 方法调用。
画面 8: 显示 ProducerTest.java 中的 testSend 方法，包含 for 循环和 rabbitTemplate.convertAndSend 方法调用。
画面 9: 显示 OosListener.java 中的 onMessage 方法，其中包含注释说明如何设置手动确认和 prefetch。
画面 10: 显示测试结果，ConsumerTest 测试失败，输出 "message confirm..."。
画面 11: 显示 OosListener.java 中的 onMessage 方法，其中包含注释说明如何设置手动确认和 prefetch。
画面 12: 显示测试结果，ConsumerTest 测试失败，输出 "message confirm..."。
画面 13: 显示 OosListener.java 中的 onMessage 方法，其中包含注释说明如何设置手动确认和 prefetch。
画面 14: 展示消费端限流小结，包括在 <rabbitlistener-container> 中配置 prefetch 属性和确认模式为手动确认。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
//1. 处理业务逻辑
System.out.println("处理业务逻辑...");
//2. 手动确认
channel.basicAck(deliveryTag, multiple=true);
//3. 抛异常
channel.basicNack(deliveryTag, multiple=true);
//4. 拒绝消息
channel.basicReject(deliveryTag, true);
//5. 拒绝消息
channel.basicReject(deliveryTag, false);
//6. 拒绝消息
channel.basicReject(deliveryTag, true);
//7. 拒绝消息
channel.basicReject(deliveryTag, true);
//8. 拒绝消息
channel.basicReject(deliveryTag, true);
//9. 拒绝消息
channel.basicReject(deliveryTag, true);
//10. 拒绝消息
channel.basicReject(deliveryTag, true);
//11. 拒绝消息
channel.basicReject(deliveryTag, true);
//12. 拒绝消息
channel.basicReject(deliveryTag, true);
//13. 拒绝消息
channel.basicReject(deliveryTag, true);
//14. 拒绝消息
channel.basicReject(deliveryTag, true);
//15. 拒绝消息
channel.basicReject(deliveryTag, true);
//16. 拒绝消息
channel.basicReject(deliveryTag, true);
//17. 拒绝消息
channel.basicReject(deliveryTag, true);
//18. 拒绝消息
channel.basicReject(deliveryTag, true);
//19. 拒绝消息
channel.basicReject(deliveryTag, true);
//20. 拒绝消息
channel.basicReject(deliveryTag, true);
//21. 拒绝消息
channel.basicReject(deliveryTag, true);
//22. 拒绝消息
channel.basicReject(deliveryTag, true);
//23. 拒绝消息
channel.basicReject(deliveryTag, true);
//24. 拒绝消息
channel.basicReject(deliveryTag, true);
//25. 拒绝消息
channel.basicReject(deliveryTag, true);
//26. 拒绝消息
channel.basicReject(deliveryTag, true);
//27. 拒绝消息
channel.basicReject(deliveryTag, true);
//28. 拒绝消息
channel.basicReject(deliveryTag, true);
//29. 拒绝消息
channel.basicReject(deliveryTag, true);
//30. 拒绝消息
channel.basicReject(deliveryTag, true);
//31. 拒绝消息
channel.basicReject(deliveryTag, true);
//32. 拒绝消息
channel.basicReject(deliveryTag, true);
//33. 拒绝消息
channel.basicReject(deliveryTag, true);
//34. 拒绝消息
channel.basicReject(deliveryTag, true);
//35. 拒绝消息
channel.basicReject(deliveryTag, true);
//36. 拒绝消息
channel.basicReject(deliveryTag, true);
//37. 拒绝消息
channel.basicReject(deliveryTag, true);
//38. 拒绝消息
channel.basicReject(deliveryTag, true);
//39. 拒绝消息
channel.basicReject(deliveryTag, true);
//40. 拒绝消息
channel.basicReject(deliveryTag, true);
//41. 拒绝消息
channel.basicReject(deliveryTag, true);
//42. 拒绝消息
channel.basicReject(deliveryTag, true);
//43. 拒绝消息
channel.basicReject(deliveryTag, true);
//44. 拒绝消息
channel.basicReject(deliveryTag, true);
//45. 拒绝消息
channel.basicReject(deliveryTag, true);
//46. 拒绝消息
channel.basicReject(deliveryTag, true);
//47. 拒绝消息
channel.basicReject(deliveryTag, true);
//48. 拒绝消息
channel.basicReject(deliveryTag, true);
//49. 拒绝消息
channel.basicReject(deliveryTag, true);
//50. 拒绝消息
channel.basicReject(deliveryTag, true);
//51. 拒绝消息
channel.basicReject(deliveryTag, true);
//52. 拒绝消息
channel.basicReject(deliveryTag, true);
//53. 拒绝消息
channel.basicReject(deliveryTag, true);
//54. 拒绝消息
channel.basicReject(deliveryTag, true);
//55. 拒绝消息
channel.basicReject(deliveryTag, true);
//56. 拒绝消息
channel.basicReject(deliveryTag, true);
//57. 拒绝消息
channel.basicReject(deliveryTag, true);
//58. 拒绝消息
channel.basicReject(deliveryTag, true);
//59. 拒绝消息
channel.basicReject(deliveryTag, true);
//60. 拒绝消息
channel.basicReject(deliveryTag, true);
//61. 拒绝消息
channel.basicReject(deliveryTag, true);
//62. 拒绝消息
channel.basicReject(deliveryTag, true);
//63. 拒绝消息
channel.basicReject(deliveryTag, true);
//64. 拒绝消息
channel.basicReject(deliveryTag, true);
//65. 拒绝消息
channel.basicReject(deliveryTag, true);
//66. 拒绝消息
channel.basicReject(deliveryTag, true);
//67. 拒绝消息
channel.basicReject(deliveryTag, true);
//68. 拒绝消息
channel.basicReject(deliveryTag, true);
//69. 拒绝消息
channel.basicReject(deliveryTag, true);
//70. 拒绝消息
channel.basicReject(deliveryTag, true);
//71. 拒绝消息
channel.basicReject(deliveryTag, true);
//72. 拒绝消息
channel.basicReject(deliveryTag, true);
//73. 拒绝消息
channel.basicReject(deliveryTag, true);
//74. 拒绝消息
channel.basicReject(deliveryTag, true);
//75. 拒绝消息
channel.basicReject(deliveryTag, true);
//76. 拒绝消息
channel.basicReject(deliveryTag, true);
//77. 拒绝消息
channel.basicReject(deliveryTag, true);
//78. 拒绝消息
channel.basicReject(deliveryTag, true);
//79. 拒绝消息
channel.basicReject(deliveryTag, true);
//80. 拒绝消息
channel.basicReject(deliveryTag, true);
//81. 拒绝消息
channel.basicReject(deliveryTag, true);
//82. 拒绝消息
channel.basicReject(deliveryTag,

