# day07-6-开户第三阶段-功能实现7

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day07-6-开户第三阶段-功能实现7_【海量资源尽在 666java.com】.mp4
- 时长 11分54秒（音频 715s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好刚才呢我们把用户中心这边如何从Rocky的MQ取消息的基本代码编下来一下啊这些其实都是一个准备工作啊你像这个创建这个消费者对象啊设置什么呀对Name Server呀还要设置这个消费地点就从最后一个进行消费啊然后设置你要从哪个主题哪个标签来取消息啊等等等等但是这里边最核心的代码我还没写就是谁啊对就是剪辑器
[00:29] 因为监听器它是主要负责从MQ取消息的那将来一旦有人发过来消息了这个监听器就从MQ取消息取到消息之后呢我们可以做后续的一些业务处理那咱接下来呢就把这块代码给编写一下怎么进入注册这个代码是不是调用一个方法对吧default然后dr叫registermessagelisten是吧那么这个方法里边呢有一个参数是一个接口
[00:59] 那一般有两种写法第一个就是传进来一个什么匿名内部类对象还有就是你可以用Lambda表示那么匿名内部类这种写法的话啊就是他相对于Lambda表示代码的可读性会好一些Lambda表示呢他写下来会少事一些反正这个你根据个人的爱好对吧萝卜白菜各有所爱你用匿名内部类也行用Lambda表示也可以那我这呢先用匿名内部类的这种写法把它的一些信息
[01:29] 给大家展示出来你看这个匿名内部类的这个代码的可动性还是比较好你看我溜溜的是他吗可不是啊这是一个接口啊我溜的是后边这这这个类这是一个类吗只是没名字吗匿名的吗那匿名内部类吗我溜的是这个实现类的一个对象啊这个类是不是实现了这个接口然后我们主要是重写这个方法在这个方法里边接收这个什么呀消息啊然后做后续的一些业务处理当然这个地方你也可以给它改造成
[01:58] 什么呀那么的两个事都可以那我们接下来就开始在这个方法里边具体去这个编译代码实验功能那首先我们就要获取消息是不是这是咱最重要的一件事会消息怎么获取消息在这我说获取消息这个事其实你都不用管这个监听器这个对象他会帮你搞定他获取到消息之后他就放到这个这个参照里面我们从这里边直接就可以干什么取消息怎么去啊他是一个集合吗即刻怎么取消息给他方法我们就给他0就行我们就就一个消消息啊
[02:28] 那么我们这个得到这个消息之后呢我们用message这个类来接受一下这个消息其实这就拿到手了就这么简单拿到手之后呢它是一个message对象是吧那我们应该怎么着它是一个message对象我们是不是应该从这个对象里面还要取其他的一些信息这里边都可以取取具体消息的内容取这个消息的什么呀topic消息的标签等等的好多信息我们都可以取那咱们接下来把这些信息给取一下因为这样
[03:02] 信息化这些数据呢一会都要用那咱就开始取一下先取这个谁呀topic然后我们用这个字幕串来接收一下train接收一下这是topic然后还有什么呀标签tag是吧等于还是从这里面message对象里边起的啊给个tag对然后呢还有就是这个什么消息的内容了
[03:39] 消息的内容就是message.get里面大家还有一印象吗get body是吧有没有get body然后大家看它获取到是不是一个字节数组看这是一个字节数组对不对字节数组我们咋用那也没法用对不对字节数组也没法用我们需要把它转换成对转换成字符串怎么转呢简单啊大家在基础班的时候应该学过new字符串代参构造是不是就可以把它转换成字符串
[04:10] 那这里边你最好设置一下什么呀编码我们采用utf-8的这个编码这个地方呢不建议你直接写utf-8万一不小心写错了啊我们这呢有一个这个相对也是一个工具类吧点从这里边取utf-8这样不容易写错好这是我们把该取的消息啊或者从消息里边把该取的数据都已经取出来取出来之后呢接下来咱就要做后续的什么要处理
[04:38] 当你接收到消息的时候我们要做什么业务处理呢你看这个图呗3.3这个地方是接收到这个消息了然后接下来就要做业务处理就是更新用户信息更新用户信息咱们前面是不是在业务层已经搞定过了那这其实就是一个调用呗是不是那我们先把业务层的那个Service先注进来然后呢就是private叫consumer Service对吧consumer Service那
[05:17] 我们接下来就调用一下他的那个方法叫啥名你还有印象吗consumer Service.modify刚写的吧modify result你看这个方案要一个什么类型的参数啊depository consumer response哎这个参数从哪来啊我们说了我们前面说过这个东西不就是银行这个返回的数据我们封装成这个类型然后从来代理服务又把它发通到咱们这边发到哪了呢
[05:46] 其实他发过来就是这个body就是这个body只不过这这目前是一个jason串啊大家有印象吗这个rocky的mq发收发消息的时候是不是都是jason串来收发那我们既然要做了事是吧把这个jason串给他转换成什么类型啊对转换成这个depository consumer response就ok了怎么转换这个大家自然会想到谁啊是fast jason对不对那这样呢这个代码我先不调用我们要做一个准备工作就是
[06:15] 这个gson.path什么样对没错然后把谁给扔进去把这个body就是消息体然后还需要一个称号就是你要告诉他要把这个阶段转转什么类型我们刚才说什么类型对depository我们找一找dpositorydepositoryconsumerresponse对转成这个类型然后
[06:44] 转化完之后呢我们直接用它来接收一下接收接完之后呢我们是不是就有了这个对象然后呢我们就可以调用什么呀对业务层consumerservice的modify什么呀raise out方法然后把这个对象直接对传进来然后这就相当于是做了什么呀对做了业务处理然后处理完之后呢大家看一下我们这个
[07:16] 方法其实是还有一个返回值啊就是一个状态对不对一个状态那这个反位置我们怎么处理呢那这样咱干脆这样咱做一个异常处理吧如果没有问题我们反而什么如果有问题我们反而什么整个这一块我们加上一个try catch做一个异常处理完善一下这个代码那如果出异常我们就返回这么一个值return我们这给大家提供了有这么一个现成的东西叫co
[07:55] Nsumerconsumer掏一下就这个刚才没出来如果有问题的话我们就应该返回这个什么reconsumerlater这个值对如果说一切正常的话我们返回谁如果正常的话我们就在这返回和他相反的一个值应该就是这个谁对success没错就成功成功获取到消息
[08:27] 没有任何问题应该是这么写啊一查反而什么值成功应该返回什么值这样子会更加的这个代码会更加的完善一些这个值不知道大家有没有印象是不是表示要重视吗就是你你出问题相当于是可能没有收到消息没有正确的获取消息那他稍微要重视吗我们的rocky的mq有重视机制吗啊这个就表示成功了啊就成功消费
[08:53] 那另外呢咱这里边还有一个细节其实这个细节目前对于咱们来说这个这个对于这个代码来说其实也没啥问题但是很快或者说将来呢我们这个代码还要给哪个地方就这个地方这个细节我们要给大家说一下这个地方其实这个细节咱们前面在这提过就这个地方我们说这个咱们consumer这边将来他会接收到各个干嘛消息但这个消息呢我们通过这个标签进行了分类比如说我们前面说有有有开户咱现在是走到开户
[09:22] 将来有销户还有什么有充值客户要充值吗还有就是提现要什么发标要做交易那么不同的业务其实这个标签的值是不一样那不同的业务其实在这在处理的时候这个代码也是什么不一样所以其实我们这应该是要做什么做判断了就判断你收到这个消息它是属于哪个什么标签你是开户
[09:48] 你是开户的话我应该是不是就走这两行代码对不对那如果说你是充值或者是提现或者是销户那还能走这两行代码吗那就不能所以考虑到将来我们这个代码是不能这么写还要改所以我们这儿呢干脆直接给它改一改啊这儿呢需要你加一个依附判断就是判断呀你本次这个消息它是这个标签是哪个值啊标是哪个值我们这个怎么判断那我们的这个标签是不是这个tag我们已经获取到这个值了啊然后呢第二
[10:18] 第二十页我们跟谁进行判断我们跟这个因为我们目前这个业务是不是开户开户我们这个业务是跟谁进行判断我们是跟他当时是在哪个地方发消息的时候是不是设置过这个值了发消息是在存款代理这边我们看看就这个值这个是表示开户我们应该是跟这保持当时咱说了这个地方其实搞成
[10:53] 静态常量或者搞上美剧都行搞上静态常量比较合适这样能写的话容易写错你最好是粘过来那我其实这个地方这个细节的意思是这样将来你收到消息他的这个tag就是一个标签有可能是这个开户也有可能是充值也有可能是什么呀提现不同的标签接下来你要处理的业务是什么呀不一样比如说我们这目前做的是开户那开户的话我一判断如果这是开户那我这是要走这两行代码就OK了
[11:22] 那将来如果是别的业务比如是销户比如说充值比如说提现那你后边是不是还要接着写什么呀对接着进行什么呀一幅判断就行了而不同的标签对应的这个不同的什么呀业务处理说这个呢这个代码我们要完善一下那截止到目前吧咱们就把哪一块代码写完了看这个图把开户业务第三阶段用户中心整个这一块的代码就全部编写完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 RocketMQ 消费者中实现消息的接收、解析和业务处理，并调用下游服务完成开户业务。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 GatewayNotifyConsumer 类中初始化 RocketMQ 消费者并订阅主题 "TP_GATEWAY_NOTIFY_AGENT" 的代码。
画面2: 展示了为消费者注册消息监听器的方法，准备重写 consumeMessage 方法。
画面3: 展示了在 consumeMessage 方法中定义了消息处理所需的工具类和常量。
画面4: 展示了通过 message.getStoreHostBytes() 获取消息存储主机信息。
画面5: 展示了通过 message.getStoreHostBytes() 获取消息存储主机信息。
画面6: 展示了 GatewayNotifyConsumer 类的类注解 @Component 和属性注入的配置。
画面7: 展示了在 consumeMessage 方法中调用 consumerService 的方法。
画面8: 展示了使用 JSON.parseObject 方法解析消息体。
画面9: 展示了将解析后的消息体转换为 DepositoryConsumerResponse 对象。
画面10: 展示了在 try 块中调用 consumerService.modifyResult 方法。
画面11: 展示了在 catch 块中处理异常并返回 RECONSUME_LATER。
画面12: 展示了在 try 块中调用 consumerService.modifyResult 方法。
画面13: 展示了 ConsumerServiceImpl 类中的 modifyResult 方法，用于更新银行卡信息并调用 bankCardService.saveOrUpdate。
画面14: 展示了开户业务的流程图，包括浏览器/App、用户中心、存管代理服务、存管系统和开卡银行之间的交互。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```java
@Value("${RocketMQ.name-server}")
private String nameServer;

public GatewayNotifyConsumer() throws MQClientException {
    DefaultMQPushConsumer defaultMQPushConsumer = new DefaultMQPushConsumer(consumerGroup);
    defaultMQPushConsumer.setNamesrvAddr(nameServer);
    defaultMQPushConsumer.setConsumeFromWhere(ConsumeFromWhere.CONSUME_FROM_LAST_OFFSET);
    defaultMQPushConsumer.subscribe(topic: "TP_GATEWAY_NOTIFY_AGENT", subExpression: "*");
    //注册监听器
    defaultMQPushConsumer.registerMessageListener(new MessageListenerConcurrently() {
        @Override
        public ConsumeConcurrentlyStatus consumeMessage(List<MessageExt> msgs, ConsumeConcurrentlyContext context) {
            return null;
        }
    });
    defaultMQPushConsumer.start()
}
```

画面2:
```java
@Override
public ConsumeConcurrentlyStatus consumeMessage(List<MessageExt> msgs, ConsumeConcurrentlyContext context) {
    return null;
}
```

画面3:
```java
String uuid = UUID.randomUUID().toString();
Deque<String> deque = new ArrayDeque<>();
StackOverflowError stackOverflowError = new StackOverflowError();
StackIntracardException stackIntracardException = new StackIntracardException();
StringBuilder stringBuilder = new StringBuilder();
StringIndexOutOfBoundsException stringIndexOutOfBoundsException = new StringIndexOutOfBoundsException();
ScheduledThreadPoolExecutor scheduledThreadPoolExecutor = new ScheduledThreadPoolExecutor();
SQLTransformerFactory sqlTransformerFactory = new SQLTransformerFactory();
SealTransaction sealTransaction = new SealTransaction();
```

画面4:
```java
String message = message.getStoreHostBytes();
```

画面5:
```java
String body = new String(message.getStoreHostBytes(), StandardCharsets.UTF_8);
```

画面6:
```java
@Component
public class GatewayNotifyConsumer {
    @Value("${RocketMQ.consumer.group}")
    private String consumerGroup;
    @Value("${RocketMQ.name-server}")
    private String nameServer;
    @Autowired
    private ConsumerService consumerService;
```

画面7:
```java
consumerService.
```

画面8:
```java
String text = JSON.parseObject(body, DepositoryConsumerResponse.class);
```

画面9:
```java
DepositoryConsumerResponse response = JSON.parseObject(body, DepositoryConsumerResponse.class);
consumerService.modifyResult(response);
```

画面10:
```java
consumerService.modifyResult(response);
```

画面11:
```java
try {
    Message message = msgs.get(0);
    String topic = message.getTopic();
    String tag = message.getTags();
    String body = new String(message.getBody(), StandardCharsets.UTF_8);
    DepositoryConsumerResponse response = JSON.parseObject(body, DepositoryConsumerResponse.class);
    consumerService.modifyResult(response);
} catch (Exception e) {
    return ConsumeConcurrentlyStatus.RECONSUME_LATER;
}
return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
```

画面12:
```java
try {
    Message message = msgs.get(0);
    String topic = message.getTopic();
    String tag = message.getTags();
    String body = new String(message.getBody(), StandardCharsets.UTF_8);
    DepositoryConsumerResponse response = JSON.parseObject(body, DepositoryConsumerResponse.class);
    consumerService.modifyResult(response);
} catch (Exception e) {
    return ConsumeConcurrentlyStatus.RECONSUME_LATER;
}
return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
```

画面13:
```java
//保存银行卡信息
BankCard bankCard = new BankCard();
bankCard.setConsumerId(consumerRequest.getConsumerId());
bankCard.setBankCode(consumerRequest.getBankCode());
bankCard.setCardNumber(consumerRequest.getCardNumber());
bankCard.setMobile(consumerRequest.getMobile());
bankCard.setCardStatus(StatusCode.STATUS_OUT.getCode());
bankCard.setExistBankCard(bankCardService.getBankCardById(consumerRequest.getConsumerId()));
if (existBankCard != null) {
    bankCard.setId(existBankCard.getId());
}
bankCardService.saveOrUpdate(bankCard);
//准备数据，发送异步调用，把数据发到下游服务
return depositoryAgentAgent.createConsumer(consumerRequest);
```

画面14:
无代码或配置，为流程图。

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面14:
流程图标题：P2P平台开户业务流程图。
结构：
- 浏览器/App → 用户中心（1.1 发送开户请求数据）
- 用户中心 → 存管代理服务（1.2 准备开户所需基础数据，1.3 更新用户数据，1.4 发送开户请求数据，1.5 保存交易记录，状态为：未同步）
- 存管代理服务 → 存管系统（1.6 通过秘钥生成签名及数据，2.4 验证4要素，2.5 验证成功，2.6 保存客户信息，2.7 保存交易记录）
- 存管系统 → 开卡银行（1.7 返回开户请求数据，2.1 调用网关开户接口，2.2 显示开户界面，2.3 请写并提交信息，3.1 回调，3.2 更新交易记录，状态为：已同步，3.3 开户成功（重定向到p2p平台页面），3.4 更新用户信息）
- 开卡银行 → 存管代理服务（3.5 更新用户信息）
- 存管代理服务 → 用户中心（3.6 返回开户结果（MQ异步通知））
- 用户中心 → 浏览器/App（3.7 返回开户结果）

5) 无其他内容。

