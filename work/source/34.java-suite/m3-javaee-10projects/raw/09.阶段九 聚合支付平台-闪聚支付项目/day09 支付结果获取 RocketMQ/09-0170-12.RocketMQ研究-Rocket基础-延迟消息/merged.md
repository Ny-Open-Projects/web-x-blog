# 12.RocketMQ研究-Rocket基础-延迟消息

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\12.RocketMQ研究-Rocket基础-延迟消息【海量资源尽在 666java.com】.mp4
- 时长 8分40秒（音频 520s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们继续来讲解RocketMQ的基础知识接下来我们要学习的是一个延迟消息那么延迟消息呢也叫定时消息这是什么意思呢刚才我们演示的什么同步啊异步啊其实我们当初是只要以执行发送它就发出去了对吧这个消息就发出去了但是延迟消息则不一样那延迟消息顾名思义就是在一定时间之后再发
[00:27] 那其实在一个在生产当中有很多的应用场景啊那你比如说在电商的交易系统当中这个用户下单之后呢我们说哎这过多长时间呢把订单呢如果没有支付就关闭那这个时候我们可能就需要给这个什么哎管订单的这个微服务呢发一个延迟消息哎比如说这个订单呢是啊30分钟如果没有支付就关那我们就可以在30分钟之后呢我们让他执行
[00:55] 那你肯定是先发一个消息这个消息呢让它延迟30分钟执行大家能理解吗这就是延迟消息它的使用场景那RocketMQ的延迟消息怎么实现呢非常简单也是我们在调用发送消息的API方法的时候我们要指定你延迟多长时间但是这个多长时间不是任意让你设置的延迟时间存在18个等级假如说我们延迟的时候呢指定一级
[01:25] 它就会延迟一秒假如说我们指定延迟三级那么它就会延迟三十秒执行大家能理解吗对这就是一个一个的等级总共十八级那最高的十八级是两个小时是这样那么有时候老师呢怎么设置这个延迟的等级呢调用它的set delay time level这个方法就行了好下面呢我们就来演示一下那我们呢还是需要去
[01:54] 来写一个测试方法的还在我们的生产的当中来写吧在这儿这儿我要发送的是一个什么延迟消息好那么延迟消息呢仍然不管发啥消息你都得有什么呀对都得有topic然后还有这个我还有发还发对象吧那么在这个里头我们要发的话怎么发呢咱们先看它的API我先看API
[02:23] 那现在我们要发延迟消息这里边你看在同步方法当中就有一个看后边前边这两个参数你看这个同步方法四个重载方法第二个后边是不是有一个叫delay level看见吗这就是延迟的等级但是这个但是这个好像不是那么简单你注意看难到哪里难到第二个参数复杂第二个参数为啥复杂呢
[02:51] 因为原来你没发现嘛我们就直接把对象放到这儿了对不对但是第二个参数你看一下吧它是一个message对吧但message到底是什么呢我们鼠标放上去它是spring的一个什么一个类型是不是啊它是spring的一个消息类型那好了那么我们这么弄啊首先啊你把这个topic放这儿这没得说吧好然后现在呢我们就不能直接把对象放这儿了对吧那你就需要怎么做呀你就需要来
[03:21] 看好啊你就需要来构建消息体这构建消息体构建成什么样的格式呢就构建成message就构建成message但是你在构建的时候还好这个spring它是不是让构建成它的这个类型呀是不是就它呀但是呢还好它给我们提供了一个builder专门用来构建的你把对象放进去对它就可以build成一个什么一个message了
[03:52] 看见了吗然后你就把它放进去后边还有两个参数一个是timeout一个是delay leveldelay level简单就是我们说的18级比如说我们指定3我们指定3那就是延迟几啊延迟10秒刚才你看到了是吧是吗看一下18级第三级第三级是不是10秒对吧那么那这个timeout呢timeouttimeout可是你发送消息的操作时间
[04:21] 它的单位是毫秒所以我们比如说发消息那肯定是一秒之后就发了嘛所以呢我就写一个什么我就写一个这个这个1000嘛就表示一秒这个叫是什么呀叫发消息的什么超时时间好那么这个超时时间呢它的单位是毫秒记着啊好这个呢就是我们说的什么延迟等级总共18级好这是消息这个是我们说的topic
[04:54] 对这样就OK了这个就是我们说的发送一个什么延迟消息是不是特别简单呀关键难的点是啥就是我们之前没有学过这个message你需要去把这个消息给它构建出来对吧把它构建出来那我们现在呢发送完消息的之后我们是不是也可以去干嘛去打印一下这个日志然后呢你得测吧那测的话怎么做呀还是需要在生产者这来吧再写一个
[05:24] 行吧然后呢这个呢就是我们刚才写的这个延迟消息然后在这呢我们去把这个方法名变一下就行了嘛行不行好然后呢这样是不是就可以发送了其实这个内容你看跟这个内容差不多啊因为他这个还是在原来的这个topic下是吧那现在呢我们就准备发吧换个换个消息啊好换个消息好现在发送
[05:53] 那发送各位你说我们咋观察效果呀咋观察效果呀这个消费者是不是在等着监听呢我们是不是延迟让他10秒呀好来吧我这只要发送成功在生产者的这个控制台上我刚才是不是打了一行日志啊那他呢只要输出了就说明这个消息发出去了对不对那这个消息发出去了哎你看吧等注意把它关掉你等是不是都已经
[06:24] 我怎么感觉好像已经输出出来了呀看好等消费者呀消费者是要等10秒的对不对消费者来来这儿所以这个这个那我们怎么弄啊我们控制台吧看这儿啊搜一下有没有我们刚才的消息就是他吧再确认一下啊消息发的太多了在生产者的测试程序当中我们先看你
[06:59] 你发的这个消息啊我们是五是不是一对五的一个消息啊对吧啊这个他要发一个延迟消息延迟消息调错方法咯是这个对吧send message by jason delay对不对哎发这个看好我再发一个看好啊所以我刚才我感觉一晃而过我好像感觉就是发马上就发出去了是不是那现在我们看我调用这个方法了吧好注意看啊
[07:31] 你看他是不是生产者执行完了生产者执行完了你等着等着消费者我们数一下现在基本上已经过五六秒了吧然后再等个三四秒你看没错吧这就是延迟消息对这就是延迟消息好那么这我刚才用的是同步的方法发延迟吗他其实一步也支持发延迟这个一步发延迟的方法呢其实你看代码可能稍微多一些但是我给大家说一下
[08:01] 那么这个一步发延迟其实还是用的template这个模板类只不过呢它这个方法你要注意这个直接的这个模板方法没有一步发延迟它需要get一个什么生产者然后呢点send只因它的send的方法注意这里面message一定注意一步发延迟这个message不是同步发延迟里面的这个message了这个message是什么是RocketMQ的原生类型
[08:28] 懂吧你看着我的例子代码自己测试一下一不发言时大家自学我这就不说了这就是我们说的延迟消息我们就讲完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 RocketMQ 中使用同步延迟消息，包括代码实现和测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了课程文档的“2.7 延迟消息”章节，其中“2.7.1 延迟消息介绍”部分说明了延迟消息的用途和设置方法。
- 文档中提到延迟时间存在八个等级（1/5s/10s/30s/1m/2m/3m/4m/5m/6m/7m/8m/9m/10m/20m/30m/1h/2h），并指出使用 setDelayTimeLevel() 设置与时间对应的延迟级别即可。

画面 2：
- 展示了 IDE 中的代码，`ProducerSimple.java` 文件中定义了 `sendMsgByJson` 方法，用于发送消息。
- 代码中使用了 `rocketMQTemplate.convertAndSend(topic, orderExt)` 方法。

画面 3：
- 展示了 IDE 中的代码，`ProducerSimple.java` 文件中定义了 `sendMsgByJsonDelay` 方法，用于发送延迟消息。
- 代码中使用了 `rocketMQTemplate.syncSend` 方法。

画面 4：
- 展示了 IDE 中的代码，`ProducerSimple.java` 文件中定义了 `sendMsgByJsonDelay` 方法。
- 代码中使用了 `rocketMQTemplate.syncSend` 方法，参数包括 topic、message、timeout 和 delayLevel。

画面 5：
- 展示了 IDE 中的代码，`ProducerSimple.java` 文件中定义了 `sendMsgByJsonDelay` 方法。
- 代码中使用了 `MessageBuilder.withPayload(orderExt).build()` 方法构建消息。
- 代码中使用了 `rocketMQTemplate.syncSend` 方法。

画面 6：
- 展示了课程文档的“2.7.2 同步消息延迟”章节。
- 文档中展示了生产端的代码示例，包括使用 `MessageBuilder.withPayload(orderExt).build()` 构建消息，以及使用 `this.rocketMQTemplate.syncSend(topic, message, 1000, 3)` 发送消息。
- 文档中还提到了消费端需要“同自定义消息格式章节”。

画面 7：
- 展示了 IDE 中的项目结构，`test-RocketMQ` 项目下包含 `src/main/java` 和 `src/test/java` 目录。
- 项目中包含 `application.yml` 配置文件。

画面 8：
- 展示了 IDE 中的测试类 `ProducerSimpleTest.java`。
- 代码中定义了 `testSendMsgByJsonDelay` 方法，用于测试发送延迟消息。
- 代码中使用了 `producerSimple.sendMsgByJsonDelay("my-topic-obj", orderExt)` 方法。

画面 9：
- 展示了 IDE 中的测试结果，测试通过。
- 控制台输出了 Spring Boot 的启动日志。

画面 10：
- 展示了 IDE 中的项目结构，`test-RocketMQ` 项目下包含 `src/main/java` 和 `src/test/java` 目录。
- 项目中包含 `application.yml` 配置文件。

画面 11：
- 展示了 IDE 中的测试类 `ProducerSimpleTest.java`。
- 代码中定义了 `testSendMsgByJsonDelay` 方法，用于测试发送延迟消息。
- 代码中使用了 `producerSimple.sendMsgByJsonDelay("my-topic-obj", orderExt)` 方法。
- 控制台输出了测试日志。

画面 12：
- 展示了课程文档的“2.7.2 同步消息延迟”章节。
- 文档中展示了生产端的代码示例，包括使用 `MessageBuilder.withPayload(orderExt).build()` 构建消息，以及使用 `this.rocketMQTemplate.syncSend(topic, message, 1000, 3)` 发送消息。
- 文档中还提到了消费端需要“同自定义消息格式章节”。

画面 13：
- 展示了课程文档的“2.7.3 异步消息延迟（自学）”章节。
- 文档中展示了生产端的代码示例，包括使用 `this.rocketMQTemplate.getProducer().send(message, sendCallback)` 发送异步消息。
- 文档中还提到了消费端需要“同自定义消息格式章节”。

画面 14：
- 展示了课程文档的“2.7.3 异步消息延迟（自学）”章节。
- 文档中展示了生产端的代码示例，包括使用 `this.rocketMQTemplate.getProducer().send(message, sendCallback)` 发送异步消息。
- 文档中还提到了消费端需要“同自定义消息格式章节”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```
延迟消息也叫定时消息，比如在电商项目的交易系统中，当用户下单之后超过一段时间之后仍然没有支付，此时就需要将订单关闭。要实现该功能的话，可以在用户创建订单时就发送一条包含订单内容的延迟消息，该消息在一段时间之后投递给消息消费者，当消息消费者接收到该消息后，判断该订单的支付状态，如果处于未支付状态，则将该订单关闭。
RocketMQ的延迟消息实现非常简单，只需要发送消息前设置延迟的时间，延迟时间存在八个等级（1/5s/10s/30s/1m/2m/3m/4m/5m/6m/7m/8m/9m/10m/20m/30m/1h/2h），调用setDelayTimeLevel()设置与时间对应的延迟级别即可。
```

画面 2：
```
/**
 * 发送延迟消息
 * 消息内容为json格式
 */
public void sendMsgByJsonDelay(String topic, OrderExt orderExt) throws
JsonProcessingException, InterruptedException, RemotingException, MQClientException,
MQBrokerException {
    //发送同步消息，消息内容将orderExt转为json
    Message<OrderExt> message = MessageBuilder.withPayload(orderExt).build();
    //指定发送超时时间（毫秒）和延迟等级
    this.rocketMQTemplate.syncSend(topic, message, 1000, 3);
    System.out.println("send msg : " + orderExt);
}
```

画面 3：
```
/**
 * 发送延迟消息
 * 消息内容为json格式
 */
public void sendMsgByJsonDelay(String topic, OrderExt orderExt) throws
JsonProcessingException, InterruptedException, RemotingException, MQClientException,
MQBrokerException {
    //发送同步消息，消息内容将orderExt转为json
    Message<OrderExt> message = MessageBuilder.withPayload(orderExt).build();
    //指定发送超时时间（毫秒）和延迟等级
    this.rocketMQTemplate.syncSend(topic, message, 1000, 3);
    System.out.println("send msg : " + orderExt);
}
```

画面 4：
```
/**
 * 发送延迟消息
 * 消息内容为json格式
 */
public void sendMsgByJsonDelay(String topic, OrderExt orderExt) throws
JsonProcessingException, InterruptedException, RemotingException, MQClientException,
MQBrokerException {
    //发送同步消息，消息内容将orderExt转为json
    Message<OrderExt> message = MessageBuilder.withPayload(orderExt).build();
    //指定发送超时时间（毫秒）和延迟等级
    this.rocketMQTemplate.syncSend(topic, message, 1000, 3);
    System.out.println("send msg : " + orderExt);
}
```

画面 5：
```
/**
 * 发送延迟消息
 * 消息内容为json格式
 */
public void sendMsgByJsonDelay(String topic, OrderExt orderExt) throws
JsonProcessingException, InterruptedException, RemotingException, MQClientException,
MQBrokerException {
    //发送同步消息，消息内容将orderExt转为json
    Message<OrderExt> message = MessageBuilder.withPayload(orderExt).build();
    //指定发送超时时间（毫秒）和延迟等级
    this.rocketMQTemplate.syncSend(topic, message, 1000, 3);
    System.out.println("send msg : " + orderExt);
}
```

画面 6：
```
生产端：
/**
 * 发送延迟消息
 * 消息内容为json格式
 */
public void sendMsgByJsonDelay(String topic, OrderExt orderExt) throws
JsonProcessingException, InterruptedException, RemotingException, MQClientException,
MQBrokerException {
    //发送同步消息，消息内容将orderExt转为json
    Message<OrderExt> message = MessageBuilder.withPayload(orderExt).build();
    //指定发送超时时间（毫秒）和延迟等级
    this.rocketMQTemplate.syncSend(topic, message, 1000, 3);
    System.out.println("send msg : " + orderExt);
}

消费端：
同自定义消息格式章节。

测试：
//测试发送同步消息
@Test
```

画面 7：
```
application.yml

