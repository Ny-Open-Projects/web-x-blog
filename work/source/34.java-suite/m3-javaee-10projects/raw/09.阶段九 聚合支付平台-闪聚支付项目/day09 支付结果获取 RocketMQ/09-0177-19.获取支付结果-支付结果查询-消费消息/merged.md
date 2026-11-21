# 19.获取支付结果-支付结果查询-消费消息

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\19.获取支付结果-支付结果查询-消费消息【海量资源尽在 666java.com】.mp4
- 时长 14分49秒（音频 889s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们继续来实现支付结果查询那刚才我们实现了发送一条查询支付结果的消息那么这个支付渠道代理服务呢他自己发消息啊他呢发了一个延迟消息后边呢他自己要接收到这个消息来调用支付宝的接口来查询交易的状态对吧好那么接下来我们因为要
[00:23] 接收消息嘛所以我们肯定要写一个消费者对吧我们写一个消费者的话这里边需要让他去监听刚才我们的topic是吧所以这里边呢我们定一个叫pay consumer然后这里边呢哎我们来回顾一下当初我们去写rocket m crew他的消费者程序是怎么做的这里边呢需要指定一个什么topic还有一个消费者的组对吧那topic的话这里边各位是啥
[00:53] 各位你能随便写吗不能你得看当初你发消息你是发到那个topic对不对那么你现在呢去监听你就要监听这个topic看见了吗那这个消费者组的话我们可讲义保持一致然后呢我们起一个组名相同组内的消费者是不是组成一个集群啊好那么我们现在呢就可以让他实现我们说的这个监听
[01:23] 那么这个监听接口实现的时候我们是不是之前学过Rock的MQ啊是不是需要指定一个什么啊一个类型吧那这个类型也就是说你这个如果接消息接成字不串那你就写String对吧但现在因为我们是个延迟消息大家还有印象吗我们当初讲过这个叫做消费从事是吧也就是说呀这个消息你不能一直让他从事你要不能正常消费他可能就一直去发嘛对不对所以呢
[01:53] 我们建议你用一个叫做messageext的这个类然后它呢就可以获取到什么啊有印象吗获取到我们说的从事的什么次数对不对好那这个代码一会我们再洗啊你记着这个事好那么各位现在呢我们就把这个基本的框框就建起来了这个方法一旦被调用就表示接收到消息了那接收到消息很显然
[02:20] 很简单嘛我们就需要把它解析出来对不对这就拿到了这个消息这个消息的内容是什么呢你发的是什么它消息的内容就是什么对吧但是呢它在发送的时候呀它会发成一个接生串那我们需要做的事是把这个接生串给它转换成对象
[02:46] 那具体转成什么对象你得看你发的时候是发的什么对象你发的时候是不是发的叫payment response DTO这个对象对吧所以你在转的时候你也得什么把它转成资格类型的这个对象所以我们就把JSON string放进去这时候呢我们这个类型你得指定明白了吧
[03:11] 好那这样的话我们是不是就把这个消息就算接收到并且也都解析了对所以这里边呢我们就将消息转成对象搞定了吧那么接下来我们要做的事是什么他接收到消息他要干嘛他光接收消息吗他肯定是要调用支付宝的什么订单状态的查询接口嘛对那
[03:39] 调用支付宝的订单状态查询接口当初我们是不是写过这个接口也是在支付渠道代理服务对不对那当初我们是不是写了一个叫你看往下翻是不是有个叫query看见了吗所以现在呢你要调用这个方法很显然你需要在这个里头去把它给注进去对吧注进去好那这样的话我们是不是表达注进去了注进去了之后呢我们就可以拿这个Service让它去调查询看见了吗但是它一调的话
[04:07] 那你就需要两个参数对不对需要两个参数那这两个参数从哪找呢从哪找呢这里头有没有啊里头有没有那肯定有呀因为当初你发消息的时候你看你点开你看你发的时候你是你怎么做的你看是不是一个发送然后你看谁调他的谁把这个参数传给他了你看他传了啥参数是不是订单号有了吧
[04:36] 还有一个你看content里边是不是放的是谁是不是叫做支付渠道参数对吧给你放进去放进去的目的就是为了将来让你去接到消息调用支付宝的接口用来懂了吧所以这呢我们就可以来拿东西了第一个拿出订单这不用说了吧这就是我们说的什么叫做订单号一会我们要传是不是另外还有一个这个很重要这拿的是谁contentcontent这个
[05:05] 刚才也说了吗它是一个啥content是一个什么类型有时候老师刚才明明它就是一个这个啥类型啊叫做AliConfigureParam这个类型但是你别忘了啊你现在接的消息都是JSON串你明白了吗对吧你这你看你看你虽然把它转成什么转成这个对象了对吧但是这个对象里面这个content它是个JSON串对不对
[05:35] 所以这一点要注意了对我们呢需要去把它接到然后呢把它对转成我们说的这个把Jason转成我们说的这个类型你明白了吧就这个非常的重要啊这个非常重要所以现在呢我们就要做这件事哎你现在呢你是要把它拿到这个拿到这个content的啊它是一个字幕串吗对吧那这个字幕串它不认那我们得把它转一下吧
[06:03] 然后呢你把它放进去我们让它弄成字幕串好那这个是一个content就相当于是我们的这个paramers这个它是一个字幕串然后呢然后你要把它转成对象怎么转成对象json它就是个json串然后呢那你准备把它转成哪个对象你原来放的时候是不是就是放的这个ali configure然后呢paramers对不对所以你把它转成它那我问你
[06:35] 现在这参数是不是就搞定那么他搞定了这个就有了这个也可以放进去那我问你这是不是就相当于调用支付宝的订单查询接口查询他的订单状态我是不是就拿到了对拿到了这个结果了之后呢各位我们接下来要做什么事啊你现在是不是要接收到这个消息然后呢开始查对吧然后有时候老师那查完了查完了接下来呢
[07:06] 接下来就是后边的事了查完了之后呢要将这个消息在这个消息现在这消息里头是啥是不是就是我们说的这个订单的一个状态对将订单状态然后呢再次看好再次发到MQ你再回到那再回到我们的技术方案你别着急看一下因为我们不是说了吗他是不是要查询
[07:32] 第二步是不是查询查询完了之后他是不是要把这个支付结果再次发到MQ接下来交易服务是不是才从MQ里边去拿对不对所以这应该是再次发到MQ但这个事呢一会儿我再做你记着一会儿我再发但这个现在你拿到这个状态这个结果到底对不对现在还未知因为之前我说过如果你取到的这个结果就这个人还没有支付呢
[07:59] 你去查询了那这个结果我问你你是不是就拿不到拿不到你就得再次一会儿让broker再把消息推给你你是不是才能再次进行消费你懂我意思吧你就你不能让这个方法如果这个状态不对你不能让这个方法结束明白了吗所以现在呢对我们要做一件事怎么事呢对我们要判断一下我们判断一下怎么判断呀我们得判断他的这个订单状态你是不是拿到一个结果呀
[08:28] 对吧我们的订单状态看好我们的订单状态有好几个对吧有什么unknown对吧那你说你如果拿到一个结果你说你这个状态就是一个unknown那你觉得他能行吗他肯定不行他必须再次来消费还要查证明现在这个人还没有支付我说的对不对所以各位这就是我们说的你必须在这要做判断你必须要判断
[08:57] 我们就用ecross判断然后呢把它放进去看懂了吧然后呢这就是我们说如果它是一个no那对不起你必须还要再消费还要再消费让它从事消费那怎么办你就要抛异常量对不对我们说当没有获取到订单的这个结果时那么我们要抛出异常那么这个时候呢我们说这个broker
[09:27] 对会再次从事让你把消息推给你懂了吧抛出异常那么后边会再次从事消费好那么这样的话我们是不是就需要抛出一个异常对吧抛出一个异常那这个异常呢就抛出一个run time异常就行了啊好就状态未知请等待从事行吧但是还有一点你不光它是一个NO这个状态你要抛异常我跟你说
[09:57] 也就是说其实这个状态呢我觉得只要不是成功然后不是最终我们说的这个结束你比如说当前还在等待支付那么你这个也不能结束懂了吧所以你还得再加一个判断就是说如果当前对他是unknown或者说他是等待支付那么你就要跑那过一会呢是不是就这个方法
[10:28] 再次从事消费然后呢又调用支付宝的结果查直到查询为止对不对直到查到我们说的状态为止但是话又说回来了如果说这个订单本身就有问题那怎么办呢因为我当时是不是教过大家说如果说这个你咱们不能无限制的让他去从事消费吧你可以是不是来一个从事的次数判断如果当比如说到第十次大概这个时间应该是基本上能够
[10:56] 完成了所以你就不要再查了对吧这个我们要把这个信息写到数据库之前我们是不是讲过RocketMQ那个从事消费那块大家可以复习一下所以这个大家回头可以自己去完善一下这个代码也就是这里面呢我们可以说看好啊对如果说哎这个从事的这个次数达到
[11:18] 一定的什么数量那么这个时候呢我们就不要再从事消费那这时候呢我们要将这个消息记录到数据库对吧然后呢有专门的这个程序单独的程序或人工进行处理懂这意思吧那么大家参考我当初讲的RocketMQ的从事消费这一块然后把这块代码大家可以尝试写一下好那么到这儿其实说它这个消费
[11:49] 做完了吧我们看一下履一下首先他拿到消息然后呢转成我们说的payment response DTO然后呢从中我们得到订单号然后呢得到我们说的这个是支付渠道参数对吧而支付渠道参数它是一个json串所以我们需要把它转成json然后呢这时候就开始调用支付宝的订单状态查询这个结果我们当初测试过是不是已经成功了那么拿到结果我们要判断如果是unknow或者说是支付中那么不行
[12:17] 抛一场下次是不是就再次重拾消费了对大概就是这么一个内容那么这里边还有一个细节我刚才忘了说了什么细节呢当初我们在发消息的时候大家还有印象吗他在发消息的时候呢他专门里边写了一个什么message等于支付宝接口的这个标识知道为什么吗因为将来这个接口是微信支付的时候我跟你说啊他这个
[12:47] 也会来消费将来也会调微信的去查懂吧所以这儿呢对我们要判断一下判断啥就是如果说你拿到的这个结果注意啊在这判断如果说我们拿到了这个结果是阿里WAP那么我们就才调用这个支付宝的查询如果是微信那么你就要调用微信的查询接口
[13:20] 懂我意思吗所以这个if我们得把它加上去然后呢这里边让它等于谁啊你拿到消息是谁你get message点然后呢这里边你原来你发的时候你看你是不是写了一个你看啊你发的时候是不是写了一个叫这个属性啊message嘛对吧所以你这人要取出来嘛取出来对吧所以这个时候就表示啥呀对它是
[13:51] 支付宝的这个接口那么我们就要调它大家看懂了吗对就这么做那么这呢它可能就出现了一些问题然后我们把它提出来就行了这样大家是不是就明白了吗然后否则否则就是其实应该就是微信嘛如果是微信什么什么对吧那微信的那个代码其实我们现在就可以写进去就是这个叫做微信GS API看到这个代码的逻辑了吧
[14:27] 就我们应该是这么写然后这呢就开始将来我们要写叫调用微信的接口查询订单懂了吧哎好那这个呃叫做支付结果查询我们说消费消息的这个代码咱们就写完了好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 RocketMQ 实现支付订单状态的异步通知与结果更新，包括消息生产者、消费者代码及业务逻辑处理。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了消息生产者 PayProducer.java 的代码，其中定义了发送消息的 Topic 为 "TP_PAYMENT_ORDER"，并使用 rocketMQTemplate.syncSend 方法发送消息，设置了超时时间为 1000ms，重试级别为 3。
画面 2: 展示了项目结构，重点指向了 PayConsumer 类所在的包路径。
画面 3: 展示了 PayConsumer.java 中的 MessageExt 对象的 get 方法列表，用于获取消息体内容。
画面 4: 展示了 PayConsumer.java 中的 @RocketMQMessageListener 注解，指定了 topic 为 "TP_PAYMENT_ORDER"，consumerGroup 为 "CID_PAYMENT_CONSUMER"。
画面 5: 展示了 PayConsumer.java 中的 onMessage 方法，用于接收消息并解析 JSON 字符串。
画面 6: 展示了 PayConsumer.java 中的业务逻辑，调用 payChannelAgentService.queryPayOrderById 方法查询订单状态。
画面 7: 展示了 PPT 内容，标题为“6.5.3 接收消息”，说明 PayConsumer 类监听 "TP_PAYMENT_ORDER" 队列。
画面 8: 展示了 PayConsumer.java 中的代码，解析消息体并调用 payChannelAgentService.queryPayOrderByAli 方法。
画面 9: 展示了 PPT 内容，标题为“6.6 支付结果更新”，并列出了根据支付状态进行不同处理的逻辑。
画面 10: 展示了 PPT 内容，标题为“6.6 支付结果更新”，并列出了当支付状态未知或用户支付中时抛出异常的代码。
画面 11: 展示了 PayConsumer.java 中的代码，处理支付状态并抛出异常。
画面 12: 展示了 PayChannelAgentServiceTest 类中的测试代码，调用 payProducer.payOrderNotice 方法发送通知。
画面 13: 展示了 PayConsumer.java 中的代码，根据支付状态进行判断并抛出异常。
画面 14: 展示了 PPT 内容，标题为“6.5.3 接收消息”，并列出了 PayConsumer 类监听 "TP_PAYMENT_ORDER" 队列。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```java
private static final String TOPIC_ORDER = "TP_PAYMENT_ORDER";
@Authorized
RocketMQTemplate rocketMQTemplate;
//发送消息（置信支付订单状态）
public void payOrderNotice(PaymentResponseDTO paymentResponseDTO) {
//发送消息
Message<PaymentResponseDTO> message = MessageBuilder.withPayload(paymentResponseDTO).build();
rocketMQTemplate.syncSend(TOPIC_ORDER, message, timeout: 1000, delayLevel: 3);
```

画面 4:
```java
@RocketMQMessageListener(topic = "TP_PAYMENT_ORDER", consumerGroup = "CID_PAYMENT_CONSUMER")
public class PayConsumer implements RocketMQListener<MessageExt> {
```

画面 5:
```java
@Override
public void onMessage(MessageExt messageExt) {
    byte[] body = messageExt.getBody();
    String jsonString = new String(body);
    //将消息转成对象
    PaymentResponseDTO paymentResponseDTO = JSON.parseObject(jsonString, PaymentResponseDTO.class);
```

画面 6:
```java
//调用支付订单查询接口
payChannelAgentService.queryPayOrderById();
```

画面 7:
```java
package com.shanjumpay.paymentagent.message;
@lifaj
@Service
@RocketMQMessageListener(topic = "TP_PAYMENT_ORDER", consumerGroup = "CID_PAYMENT_CONSUMER")
public class PayConsumer implements RocketMQListener<MessageExt> {
@Resource
private PayChannelAgentService payAgentService;
@Override
public void onMessage(MessageExt messageExt) {
    log.info("开始消费支付结果查询消息: {}", messageExt);
    //取出消息内容
    String body = new String(messageExt.getBody(), StandardCharsets.UTF_8);
    PaymentResponseDTO response = JSON.parseObject(body, PaymentResponseDTO.class);
    String outTradeNo = response.getOutTradeNo();
    String msg = response.getMsg();
    String param = response.getContent();
    AliConfigParam aliConfigParam = JSON.parseObject(param, AliConfigParam.class);
```

画面 8:
```java
//调用支付订单查询接口
PaymentResponseDTO response = payChannelAgentService.queryPayOrderByAli(aliConfigParam, outTradeNo);
```

画面 9:
```java
//返回查询获得的支付状态
if (TradeStatus.UNKNOWN.equals(result.getTradeState()) || TradeStatus.USERPAYING
.equals(result.getTradeState())) {
    //在支付状态未知或支付中，抛出异常重置消息
    log.info("支付代理 - 支付状态未知，等待重试");
    throw new RuntimeException("支付状态未知，等待重试");
}
```

画面 10:
```java
//返回查询获得的支付状态
if (TradeStatus.UNKNOWN.equals(result.getTradeState()) || TradeStatus.USERPAYING
.equals(result.getTradeState())) {
    //在支付状态未知或支付中，抛出异常重置消息
    log.info("支付代理 - 支付状态未知，等待重试");
    throw new RuntimeException("支付状态未知，等待重试");
}
```

画面 11:
```java
//特订单状态，再次发起...
```

画面 12:
```java
notice.setMsg("ALIPAY_WAP"); //标识是支付宝的接口
//发送消息
payProducer.payOrderNotice(notice);
```

画面 13:
```java
//判断支付状态
if ("ALIPAY_WAP".equals(paymentResponseDTO.getMsg())) {
    //调用支付宝查询订单接口
    PaymentResponseDTO response = payChannelAgentService.queryPayOrderByAli(aliConfigParam, outTradeNo);
    if (TradeStatus.UNKNOWN.equals(response.getTradeState()) || TradeStatus.USERPAYING.equals(response.getTradeState())) {
        throw new RuntimeException("支付状态未知，等待重试");
    }
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 7:
标题：6.5.3 接收消息
内容：定义 PayConsumer 类，监听 "TP_PAYMENT_ORDER" 队列。

画面 9:
标题：6.6 支付结果更新
内容：根据支付状态进行不同处理，包括未知状态和用户支付中状态。

画面 10:
标题：6.6 支付结果更新
内容：当支付状态未知或用户支付中时，抛出异常并等待重试。

5) 无。

