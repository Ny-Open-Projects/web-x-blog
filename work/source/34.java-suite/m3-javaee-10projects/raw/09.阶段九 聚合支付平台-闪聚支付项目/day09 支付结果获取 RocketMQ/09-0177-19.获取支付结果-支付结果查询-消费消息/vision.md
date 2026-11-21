# 画面线理解：19.获取支付结果-支付结果查询-消费消息

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\19.获取支付结果-支付结果查询-消费消息【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:58, 02:04, 02:55, 03:29, 04:23, 05:40, 06:57, 08:27, 09:45, 10:58, 12:37, 13:49, 14:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 03:16:24

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
