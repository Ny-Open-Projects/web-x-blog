# 画面线理解：13.RocketMQ研究-Rocket基础-消费重试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\13.RocketMQ研究-Rocket基础-消费重试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 01:42, 04:10, 04:40, 05:15, 05:49, 06:15, 07:17, 07:43, 08:26, 09:00, 09:36, 10:39, 10:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 03:12:00

1) 这一组画面整体在讲什么（一句话）：
讲解 RocketMQ 中消息消费失败后的重试机制与处理策略，包括延迟消息的级别设置、同步消息的重试逻辑以及实际生产中的处理方案。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 RocketMQ 延迟消息的介绍，说明延迟消息的实现方式和可用的延迟等级（1s/5s/10s/30s/1m/2m/3m/4m/5m/6m/7m/8m/9m/10m/20m/30m/1h/2h），并提到通过 setDelayTimeLevel() 方法设置。
画面 2: 展示了消费者端的 Java 代码，其中 onMessage 方法用于处理接收到的消息，当前代码为空。
画面 3: 在消费者端的 onMessage 方法中，添加了 if (false) 语句，用于演示逻辑。
画面 4: 展示了消费者端的代码，其中 onMessage 方法中添加了 throw new RuntimeException("处理消息失败！"); 语句，用于模拟处理失败。
画面 5: 展示了生产者端的 Java 代码，其中 onMessage 方法中添加了 throw new RuntimeException("处理消息失败！"); 语句，用于模拟处理失败。
画面 6: 展示了生产者端的 Java 代码，其中 testSendMsgByJson 方法用于发送消息，消息内容为 OrderExt 对象，包含 ID、money、title 和 createTime 字段。
画面 7: 展示了 RocketMQ 延迟消息的介绍，说明延迟消息的实现方式和可用的延迟等级（1s/5s/10s/30s/1m/2m/3m/4m/5m/6m/7m/8m/9m/10m/20m/30m/1h/2h），并提到通过 setDelayTimeLevel() 方法设置。
画面 8: 展示了 RocketMQ 延迟消息的介绍，说明延迟消息的实现方式和可用的延迟等级（1s/5s/10s/30s/1m/2m/3m/4m/5m/6m/7m/8m/9m/10m/20m/30m/1h/2h），并提到通过 setDelayTimeLevel() 方法设置。
画面 9: 展示了 RocketMQ 延迟消息的介绍，说明延迟消息的实现方式和可用的延迟等级（1s/5s/10s/30s/1m/2m/3m/4m/5m/6m/7m/8m/9m/10m/20m/30m/1h/2h），并提到通过 setDelayTimeLevel() 方法设置。
画面 10: 展示了消费者端的 Java 代码，其中 onMessage 方法中添加了 throw new RuntimeException("处理消息失败！"); 语句，用于模拟处理失败。
画面 11: 展示了消费者端的 Java 代码，其中 onMessage 方法中添加了 throw new RuntimeException("处理消息失败！"); 语句，用于模拟处理失败。
画面 12: 展示了消费者端的 Java 代码，其中 onMessage 方法中添加了 throw new RuntimeException("处理消息失败！"); 语句，用于模拟处理失败。
画面 13: 展示了 RocketMQ 延迟消息的介绍，说明延迟消息的实现方式和可用的延迟等级（1s/5s/10s/30s/1m/2m/3m/4m/5m/6m/7m/8m/9m/10m/20m/30m/1h/2h），并提到通过 setDelayTimeLevel() 方法设置。
画面 14: 展示了 RocketMQ 延迟消息的介绍，说明延迟消息的实现方式和可用的延迟等级（1s/5s/10s/30s/1m/2m/3m/4m/5m/6m/7m/8m/9m/10m/20m/30m/1h/2h），并提到通过 setDelayTimeLevel() 方法设置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1:
```java
// 1s/5s/10s/30s/1m/2m/3m/4m/5m/6m/7m/8m/9m/10m/20m/30m/1h/2h
```
画面 2:
```java
@Component
@RocketMQMessageListener(topic = "my-topic-obj", consumerGroup = "demo-consumer-group-obj")
public class ConsumerSimpleObj implements RocketMQListener<OrderExt> {

    @Override
    public void onMessage(OrderExt orderExt) {
        System.out.println(orderExt);
    }
}
```
画面 3:
```java
if (false) {
    notify();
    notifyAll();
    return;
}
```
画面 4:
```java
throw new RuntimeException("处理消息失败！");
```
画面 5:
```java
throw new RuntimeException("处理消息失败！");
```
画面 6:
```java
public void testSendMsgByJson() {
    OrderExt orderExt = new OrderExt();
    orderExt.setId(1122);
    orderExt.setMoney(999);
    orderExt.setTitle("测试");
    orderExt.setCreateTime(new Date());
}
```
画面 7:
```java
public class ConsumerSimple implements RocketMQListener<MessageExt> {

    @Override
    public void onMessage(MessageExt messageExt) {
        //取出当前重试次数
        int reconsumeTimes = messageExt.getReconsumeTimes();
        //当大于一定的次数后将消息写入数据库，由单独的程序或人工去处理
        if (reconsumeTimes >= 2) {
            //将消息写入数据库，之后正常返回
            return;
        }
        throw new RuntimeException(String.format("第%s次处理失败.", reconsumeTimes));
    }
}
```
画面 8:
```java
//将消息写入数据库，之后正常返回
return ;
```
画面 9:
```java
//将消息写入数据库，之后正常返回
return ;
```
画面 10:
```java
public void onMessage(MessageExt messageExt) {
    byte[] body = messageExt.getBody();
    String jsonString = new String(body);
    System.out.println(jsonString);
    if (false) {
        throw new RuntimeException("处理消息失败！");
    }
}
```
画面 11:
```java
public void onMessage(MessageExt messageExt) {
    byte[] body = messageExt.getBody();
    String jsonString = new String(body);
    System.out.println(jsonString);
    if (false) {
        throw new RuntimeException("处理消息失败！");
    }
}
```
画面 12:
```java
public void onMessage(MessageExt messageExt) {
    byte[] body = messageExt.getBody();
    String jsonString = new String(body);
    System.out.println(jsonString);
    if (false) {
        throw new RuntimeException("处理消息失败！");
    }
}
```
画面 13:
```java
1s 5s 10s 30s 1m 2m 3m 4m 5m 6m 7m 8m 9m 10m 20m 30m 1h 2h
```
画面 14:
```java
1s 5s 10s 30s 1m 2m 3m 4m 5m 6m 7m 8m 9m 10m 20m 30m 1h 2h
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“2.7 延迟消息”，子标题为“2.7.1 延迟消息介绍”。
画面 7: PPT 标题为“2.8.2 处理策略”，内容包括“当消息在消费时出现异常，此时消息将不断重试消费。RocketMQ 会一直重试消费吗？”、“答案是不会！”、“消息会按照延迟消息的延迟时间等级（1s 5s 10s 30s 1m 2m 3m 4m 5m 6m 7m 8m 9m 10m 20m 30m 1h 2h）从第3级开始重试，每试一次如果还不成功则延迟等级加1。”、“比如：一条消息消费失败，等待10s(第3级)进行重试，如果还没有被成功消费则延迟等级加1，即按第4级延迟等待，等30s继续进行重试，如此进行下去，直到重
