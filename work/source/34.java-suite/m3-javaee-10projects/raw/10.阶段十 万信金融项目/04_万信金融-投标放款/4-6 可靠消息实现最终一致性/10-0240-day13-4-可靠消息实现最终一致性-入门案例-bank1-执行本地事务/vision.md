# 画面线理解：day13-4-可靠消息实现最终一致性-入门案例-bank1-执行本地事务

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-4-可靠消息实现最终一致性-入门案例-bank1-执行本地事务_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 02:03, 03:06, 03:56, 07:39, 09:02, 10:33, 12:26, 13:45, 15:04, 15:57, 16:50, 17:45, 18:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:02:19

1) 这一组画面整体在讲什么（一句话）：
演示如何在 RocketMQ 中实现事务消息，通过编写事务监听器来确保消息发送与本地事务的一致性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 RocketMQ 事务消息的流程图，包含本地事务、发送方、服务端（Broker）、接收方四个组件及其交互流程。
画面2：展示项目结构，当前在“分布式事务”章节，具体到“3.3.4 功能测试”下的“4.1 正常流程”。
画面3：展示代码，讲解 RocketMQ 事务监听器的两个核心功能：执行本地事务和检查消息回查。
画面4：展示 TransferTransactionListenerImpl 类的定义，标注了 @Component 和 @RocketMQTransactionListener 注解。
画面5：展示 executeLocalTransaction 方法的代码框架。
画面6：展示 BankMessageProducer.java 中 sendAccountChangeEvent 方法，使用 rocketMQTemplate 发送消息。
画面7：展示消息体解析部分，使用 JSON.parseObject 解析消息体。
画面8：展示解析消息体并获取 accountChange 字段。
画面9：展示 TransferTransactionListenerImpl 类中定义的 private AccountInfoService 字段。
画面10：展示 executeLocalTransaction 方法中解析消息体并创建 AccountChangeEvent 对象。
画面11：展示 executeLocalTransaction 方法中执行本地事务的 try-catch 逻辑。
画面12：展示 executeLocalTransaction 方法中根据事务执行结果返回 COMMIT 或者 ROLLBACK。
画面13：展示 executeLocalTransaction 方法中解析消息体并创建 AccountChangeEvent 对象。
画面14：展示 TransferTransactionListenerImpl 类中定义的 private AccountInfoService 字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：无代码。
画面2：无代码。
画面3：无代码。
画面4：
```java
package cn.itcast.wanxin.ensuremessage.bank1.message;

import lombok.extern.slf4j.Slf4j;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.core.RocketMQLocalTransactionState;
import org.springframework.stereotype.Component;

@Slf4j
@Component
@RocketMQTransactionListener(txProducerGroup = "producer_ensure_transfer")
public class TransferTransactionListenerImpl implements RocketMQLocalTransactionListener {
```
画面5：
```java
@Override
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    return null;
}

@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    return null;
}
```
画面6：
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class BankMessageProducer {

    @Resource
    private RocketMQTemplate rocketMQTemplate;

    public void sendAccountChangeEvent(AccountChangeEvent accountChange) {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("accountChange", accountChange);
        Message<String> msg = MessageBuilder.withPayload(jsonObject.toJSONString()).build();
        rocketMQTemplate.sendMessageInTransaction("producer_ensure_transfer",
                "topic_ensure_transfer",
                msg, null);
    }
}
```
画面7：
```java
// 解析消息体
JSON.parseObject(new String(msg.getPayload()), Object.class)
```
画面8：
```java
// 解析消息体
final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
AccountChangeEvent accountChangeEvent =
    jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
```
画面9：
```java
@Autowired
private AccountInfoService accountInfoService;
```
画面10：
```java
// 接收并解析消息
final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
AccountChangeEvent accountChangeEvent =
    jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
```
画面11：
```java
// 执行本地事务
Boolean isCommit = true;
try {
    accountInfoService.doUpdateAccountBalance(accountChangeEvent);
} catch (Exception e) {
    isCommit = false;
}
```
画面12：
```java
// 退回执行结果
if (isCommit) {
    return RocketMQLocalTransactionState.COMMIT;
} else {
    return RocketMQLocalTransactionState.ROLLBACK;
}
```
画面13：
```java
// 接收并解析消息
final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
AccountChangeEvent accountChangeEvent =
    jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
```
画面14：
```java
@Autowired
private AccountInfoService accountInfoService;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：架构图，包含四个组件：
- 本地事务（A服务数据库）指向发送方（A服务）。
- 发送方（A服务）指向服务端（Broker）。
- 服务端（Broker）指向接收方（B服务）。
- 发送方（A服务）指向服务端（Broker）的箭头标注“1. 发送半消息”。
- 服务端（Broker）指向发送方（A服务）的箭头标注“2. 半消息发送成功”。
- 服务端（Broker）指向发送方（A服务）的箭头标注“4. Commit或者Rollback”。
- 服务端（Broker）指向接收方（B服务）的箭头标注“Commit: 投递消息”。
- 服务端（Broker）指向接收方（B服务）的箭头标注“Rollback: 不投递消息”。
- 发送方（A服务）指向本地事务（A服务数据库）的箭头标注“3. 执行本地事务”。
- 本地事务（A服务数据库）指向发送方（A服务）的箭头标注“6. 检查本地事务的状态”。
- 服务端（Broker）指向发送方（A服务）的箭头标注“5. 未收到4的确认时，回查事务状态”。
- 服务端（Broker）指向发送方（A服务）的箭头标注“7. 根据事务的状态Commit/Rollback”。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
