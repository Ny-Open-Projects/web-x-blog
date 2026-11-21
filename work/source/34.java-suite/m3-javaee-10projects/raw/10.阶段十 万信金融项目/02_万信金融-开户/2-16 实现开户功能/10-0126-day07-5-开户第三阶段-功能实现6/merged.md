# day07-5-开户第三阶段-功能实现6

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day07-5-开户第三阶段-功能实现6_【海量资源尽在 666java.com】.mp4
- 时长 10分41秒（音频 641s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好大家看这张图我们刚才是不是把用户中心这边的这块功能搞定了是不是接下来呢咱搞定这块功能那这块功能呢主要是跟MQ有关的就Rocky的MQ那呢他呢主要是从MQ要接收什么呀消息对那这个消息谁发的呀是不是存管代理服吗对不对这边啊他发消息给MQ了嘛那我们用户中心这边就要从MQ里边去
[00:30] 对取消息取完消息之后呢才去更新什么呀对用户的信息啊就调用咱刚才在要层写的那个代码咱接下来搞定这个如何从MQ去接收消息这个代码不知道大家还有没有印象咱以前是这个学习Droki的MQ的时候都写过这个代码稍微有点复杂对不对咱接下来把这个代码写一下那咱需要单独创建一个类啊
[01:00] 单独啊我们也是在message包当中单独创建一个类这个类就负责接收什么呀从代理服务那边发过来的这个消息或者说通知然后我们去找到这个谁呀consumer就是他了然后呢我们去哪然后我们是不是得单独建一个message包是吧单独建一个包叫mesage
[01:34] 然后呢在这里边我们需要单独新建一个类名字呢跟讲义保持一致然后呢上面呢我们先加一个注解交给spring进行管理componit那在这个类里边呢我们主要实现的功能就是接收对存罐代理服务那边发过来的这个消息或者说这个通知那具体实验这个功能的时候呢我们需要单独定义一个方法这个方法呢我们也跟讲义保持一致
[02:07] 这是一个构造方法那这里边我们这个代码怎么编写呢就我刚才问大家了这个如何从Rookie的MQ里边去取消息那取消息的话我问大家一下这个问题啊就是我们这边就是Consumer这边它是属于生产者还是消费者这儿这儿应该是生产者还是消费者对我们这边应该是消费者消费者是接收消息的嘛获取消息嘛对不对那这个代码你还有印象吗获取消息的话我们首先是不是要创建一个Consumer对象
[02:41] 当然这个consumer跟咱这个这个这个什么呀咱当前这个用户中心这个consumer可是两码事啊他这个consumer指的是Rocky的MQ里边接收消息的那一方叫消费者嘛叫consumer所以一定要注意那我们需要先创建出来这么一个对象啊这个对象的话我们直接new就是new default MQpush对吧consumer执行newdefaultdefault defaultdefaultdefault什么呀
[03:14] 对MQ它应该是属于消费者消费者是PushMQPush什么呀Consumer对没错就是它然后直接Nu出来就行了Default然后这可没完我们在Nu的时候呢我们需要调用它的一个代餐的这个什么呀对构造方法代餐的构造方案呢这里边需要设置这个组消费者这个组这个组呢这个值呢我们当初是不是配到Apollo上了
[03:46] 你还有印象吗Apollo我们是配到consumer这边的吧当然配过你也看看咱讲义里边在在哪在rocky的mq环境搭建的时候你看看这儿是不是我们增加过这个consumer这个组我们开始加到加到这儿这就是这个地方就是它那现在这个配置在Apollo上我们怎么从Apollo上来获取到这个配置
[04:21] 那我们可以直接这么来获取这么来写就是还是用以前那个什么注解at value注解就可以了也是可以的获取的方式不止一种那这里边我们要写的是一个表达式dollar大果号里边写的这个值呢就应该是从阿卜捞上这个键的名把这个名字给它拨过来然后呢给它扔到这里来通过这个at value
[04:53] 这个注解呢我们其实就拿到了这个值拿到这个值之后呢注入给谁呢我们声明一个属性呗Stream那就叫consumergrop对就这样然后呢需要把它作为参数放到这那这样子的话咱这个什么呀对这个消费者consumer这个对象就有那这个对象有了之后他要想干活要想取消息
[05:25] 你还得做一些设置比如说要设置这个什么呀Name Server是不是还要设置你从哪进行消费还要设置这个topic等等等等这些设置完之后他才能正确的从MQ当中获取到消息那咱们接下来进行相关的一些设置首先我们要设置的就是这个Name Server他的这个地址set names对就设置他这个值大家应该也有印象我们是不是也是配到Apollo上来看这
[05:56] Apollo上的哪个地方呀看表格吧哪个地方就是这我们本地嘛端口号9876是不是那我们是不是要获取这个值啊啊我们跟上面这个写法是一样的吗也是通过atvalue注解然后也是要写这么一个表达式然后把这个纸扔过来这样我们就得到这个name source的这个地址了啊然后private存进来
[06:31] 就叫NameSERVER注进来之后呢我们在这就可以用这是要配置这个什么NameSERVER的这个地址然后还有什么呀还要设置从哪进行消费Consumer我们不知道可能叫Default第二还有一个Set方式叫SetConsumerFromWhere
[07:01] 这个呢我们这个地方我们设置的时候呢都是从最后一个进行消费的这里边有一个值我们直接取叫就是这里边的叫lastlast of set我们从最后一个消费最后一个从最后一个开始还有什么大家想想我们以前在写这个代码的时候还需要啥对还要设置主题标签呀对不对你要从MQ获取哪个主题哪种标签的这个什么呀消息
[07:32] 然后还需要设置叫叫SC对吧叫啥叫不叫set叫sub这个sub sub哎就是这个方法啊你这里边他要几个参数两个参数第一个参数就是topic的名字第二个参数就是那个那个标签嘛标签我们前面说标签相当于是对topic的又又做了一个细分嘛那这俩值你可不能随便乱写特别是第一个值这个topic的这值你不能随便乱写啊要跟哪
[08:03] 进行对应啊跟哪进行对应啊我说这个消息谁发的呀消息是不是这个这个存管代理服务他那边发消息的时候你看这个地方他是什么值啊我们找到那个代码咱要对应上message是吧这里边你看当时发消息的时候你看这是不是这是那个topic后边这个是那个标签嘛就是tag对不对那我们应该跟这儿保持一致对吗对没错啊一定要跟这儿保持一致第一个参数你要这么写
[08:34] 那第二个参数按说我们是不是应该写哪个值啊按说我们是不是应该写这个就是开户个人开户但是呢我们这直接写了一个什么呀给了一个星星就比较所有了那为啥这我要给星呢这呢我要给大家解释一下就是目前咱们P2P里边涉及到的一个核心业务是目前咱只开发了一个开户对不对那将来呢我们其实还有销户将来还要充值还要提现还有这个发标
[09:05] 这个满标等各种各样的操作好多业务其实将来都是通过MQ来进行交货的那也就意味着将来这个只有可能是多种多样的但是呢我将来准备都通过这个类去干什么去接受明白什么意思吗就这有可能一会儿是A一会儿是B一会儿是C但是呢我这呢还是通过一个类去接受所以这我得显个星显个星之后呢我会进行判断嘛判断你发过来的是是开户的是销户的
[09:35] 还是充值的还是这个提现呢哎我进行判断判断完之后我再做相应的也有处理所以这呢我是写了一星表示接收啊所有只要是这个topic的啊所有的这个标签的这个消息这是不是我们做了一些什么样基本的设置然后设置完之后其实接下来最核心的也是这个最多的一块代码就是什么呀要注册对监听器这个代码比较多咱一会单独再写
[10:05] 然后监听器这块搞定完之后其实就是开始让他工作怎么工作了就调用他的什么方法对ST start就开始让他工作就OK了这是相当于咱复习了一下之前咱们学习过的Rocket MQ里边咱是如何怎么着如何从MQ里边去获取消息这些其实就是最基本的一些代码那么咱一会儿就把
[10:35] 注册监听器这里边最核心的一些代码给编写一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中配置并实现一个 RocketMQ 消费者，包括创建消费者类、设置 NameServer、订阅主题、配置消费参数，并通过 Apollo 配置中心管理相关配置。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了课程 PPT 的目录结构，当前章节为“3.2.2 用户中心生成”下的“3.2.2.2 RocketMQ 消费者”，并显示了 `GatewayNotifyConsumer` 类的代码，其中包含 `@Value("${RocketMQ.consumer.group}")`、`@Value("${RocketMQ.name-server}")` 和 `@Autowired private GatewayService consumerService;` 等注解和字段，以及 `consumer.subscribe(...)` 的订阅代码。
画面 2: 在 IDEA 中，右键点击 `ConsumerService` 类，弹出菜单，选择“Copy Path”，并显示了 `modifyResult: Depository(Consumer_Response response)` 方法中的部分代码，包括 `consumer = getResponse().getConsumerId()` 和 `BankCardService.update(...)`。
画面 3: 与画面 1 类似，展示了 PPT 目录和 `GatewayNotifyConsumer` 类代码，但代码中 `@Value("${RocketMQ.consumer.group}")` 后面有问号，且 `consumer.setNamesrvAddr(...)` 代码行被注释。
画面 4: 在 IDEA 中，显示了 `GatewayNotifyConsumer` 类的代码，但内容为空，仅包含 `public GatewayNotifyConsumer() throws MQClientException { }`。
画面 5: 在 IDEA 中，显示了 `GatewayNotifyConsumer` 类的代码，其中 `public GatewayNotifyConsumer() throws MQClientException {` 后面有 `DefaultMQPushConsumer defaultMQPushConsumer = new DefaultMQPushConsumer();`。
画面 6: 在 Apollo 配置中心页面，显示了 `micro_service.spring-cloud-hmily` 等配置项，但未显示具体配置内容。
画面 7: 在 IDEA 中，显示了 `GatewayNotifyConsumer` 类的代码，其中 `public GatewayNotifyConsumer() throws MQClientException {` 后面有 `DefaultMQPushConsumer defaultMQPushConsumer = new DefaultMQPushConsumer();`。
画面 8: 在 IDEA 中，显示了 `GatewayNotifyConsumer` 类的代码，其中 `public GatewayNotifyConsumer() throws MQClientException {` 后面有 `DefaultMQPushConsumer defaultMQPushConsumer = new DefaultMQPushConsumer();`。
画面 9: 在 Apollo 配置中心页面，显示了 `RocketMQ.consumer.group` 和 `RocketMQ.name-server` 等配置项，其中 `RocketMQ.name-server` 的值为 `127.0.0.1:9876`。
画面 10: 在 IDEA 中，显示了 `GatewayNotifyConsumer` 类的代码，其中 `public GatewayNotifyConsumer() throws MQClientException {` 后面有 `DefaultMQPushConsumer defaultMQPushConsumer = new DefaultMQPushConsumer();`。
画面 11: 在 IDEA 中，显示了 `GatewayNotifyConsumer` 类的代码，其中 `public GatewayNotifyConsumer() throws MQClientException {` 后面有 `DefaultMQPushConsumer defaultMQPushConsumer = new DefaultMQPushConsumer();`。
画面 12: 在 IDEA 中，显示了 `GatewayNotifyConsumer` 类的代码，其中 `public GatewayNotifyConsumer() throws MQClientException {` 后面有 `DefaultMQPushConsumer defaultMQPushConsumer = new DefaultMQPushConsumer();`。
画面 13: 在 IDEA 中，显示了 `GatewayNotifyConsumer` 类的代码，其中 `public GatewayNotifyConsumer() throws MQClientException {` 后面有 `DefaultMQPushConsumer defaultMQPushConsumer = new DefaultMQPushConsumer();`。
画面 14: 在 IDEA 中，显示了 `GatewayNotifyConsumer` 类的代码，其中 `public GatewayNotifyConsumer() throws MQClientException {` 后面有 `DefaultMQPushConsumer defaultMQPushConsumer = new DefaultMQPushConsumer();`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 1:
```java
private String consumerGroup;
@Value("${RocketMQ.name-server}")
private String mqNameServer;
@Autowired
private GatewayService consumerService;
public GatewayNotifyConsumer() throws MQClientException {
    DefaultMQPushConsumer consumer = new DefaultMQPushConsumer(consumerGroup);
    consumer.setNamesrvAddr(mqNameServer);
    consumer.setConsumeFromWhere(ConsumerFromWhere.CONSUME_FROM_LAST_OFFSET);
    // 订阅主题的通配符
    consumer.subscribe("TP_GATEWAY_NOTIFY_AGENT", "*");
    // 注册监听器
    consumer.registerMessageListener((MessageListenerConcurrently) (msgs, context) -> {
        Message msg = msgs.get(0);
    });
}
```
画面 2:
```java
modifyResult: Depository(Consumer_Response response) {
    consumer = getResponse().getConsumerId();
    if (consumer == null) {
        return null;
    }
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer);
    consumer.setConsumerId(consumer

