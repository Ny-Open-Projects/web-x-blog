# 画面线理解：day07-6-开户第三阶段-功能实现7

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day07-6-开户第三阶段-功能实现7_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 02:01, 03:24, 03:48, 04:24, 05:02, 06:00, 06:37, 07:04, 08:04, 09:39, 10:02, 10:38, 11:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:31:26

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
@Value("${rocketmq.name-server}")
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
    @Value("${rocketmq.consumer.group}")
    private String consumerGroup;
    @Value("${rocketmq.name-server}")
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
