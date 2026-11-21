# 画面线理解：day14-12-用户还款-第三阶段-消息监听

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-12-用户还款-第三阶段-消息监听_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:14, 02:03, 03:23, 04:51, 06:21, 07:17, 08:29, 09:18, 10:46, 11:30, 13:12, 13:45, 14:58, 15:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:21:21

1) 这一组画面整体在讲什么（一句话）：
在 RocketMQ 中实现确认还款事务消息监听器，通过本地事务确保消息与数据库操作的最终一致性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程文档“5.3 确认还款事务消息监听类”，并显示了 `ConfirmRepaymentTransactionListener.java` 文件的代码，其中包含 `@Component` 注解和 `executeLocalTransaction` 方法的实现。
画面 2: 展示了 `ConfirmRepaymentTransactionListener.java` 文件的开头部分，包含包声明和导入语句。
画面 3: 展示了 `executeLocalTransaction` 方法的实现，其中包含注释“//收到消息后执行本地事务”和“//进行事务状态回查”。
画面 4: 展示了 `executeLocalTransaction` 方法中解析消息体的代码，使用 `JSON.parseObject` 解析 JSON 字符串。
画面 5: 展示了 `confirmRepayment` 方法的实现，用于发送确认消息。
画面 6: 展示了 `executeLocalTransaction` 方法中解析消息体的代码，使用 `JSON.parseObject` 解析 JSON 字符串。
画面 7: 展示了 `executeLocalTransaction` 方法中调用 `repaymentService.confirmRepayment` 执行本地事务。
画面 8: 展示了 `checkLocalTransaction` 方法中返回 `RocketMQLocalTransactionState.COMMIT` 的代码。
画面 9: 与画面 1 相同，再次展示课程文档“5.3 确认还款事务消息监听类”。
画面 10: 展示了 `RepaymentServiceImpl.java` 文件中 `confirmRepayment` 方法的实现，包含数据库操作。
画面 11: 展示了 `executeLocalTransaction` 方法中解析消息体的代码，使用 `JSON.parseObject` 解析 JSON 字符串。
画面 12: 展示了 `checkLocalTransaction` 方法中调用 `newRepaymentPlanMapper.selectById` 查询数据库。
画面 13: 展示了 `checkLocalTransaction` 方法中判断 `newRepaymentPlan` 是否为 null 并检查状态。
画面 14: 展示了 RocketMQ 事务消息的架构图，说明 Broker 与发送方、接收方的通信机制。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Component
@RocketMQTransactionListener(txProducerGroup = "PID_CONFIRM_REPAYMENT")
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
    @Autowired
    private RepaymentService repaymentService;

    @Override
    public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        //1.解析消息
        final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
        RepaymentPlan repaymentPlan = JSON.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
        RepaymentRequest repaymentRequest = JSON.parseObject(jsonObject.getString("repaymentRequest"), RepaymentRequest.class);
    }
```

画面 2:
```java
package cn.itcast.wanxingzp.repayment.message;
import org.apache.rocketmq.spring.core.RocketMQTransactionListener;
import org.springframework.stereotype.Component;
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
```

画面 3:
```java
@Component
@RocketMQTransactionListener(txProducerGroup = "PID_CONFIRM_REPAYMENT")
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
    @Override
    //收到消息后执行本地事务
    public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        //1.解析消息
        //2.执行本地事务
        //3.返回结果
    }
    @Override
    //进行事务状态回查
    public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
        return null;
    }
```

画面 4:
```java
@Component
@RocketMQTransactionListener(txProducerGroup = "PID_CONFIRM_REPAYMENT")
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
    @Autowired
    private RepaymentService repaymentService;

    @Override
    //收到消息后执行本地事务
    public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        //1.解析消息
        final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
        //2.执行本地事务
        //3.返回结果
    }
```

画面 5:
```java
@Resource
private RocketMQTemplate rocketMQTemplate;

public void confirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
    JSONObject jsonObject = new JSONObject();
    jsonObject.put("repaymentPlan", repaymentPlan);
    jsonObject.put("repaymentRequest", repaymentRequest);
    Message<String> msg = MessageBuilder.withPayload(jsonObject.toJSONString()).build();
    rocketMQTemplate.sendMessageInTransaction("PID_CONFIRM_REPAYMENT", destination: "TP_CONFIRM_REPAYMENT", msg, null);
}
```

画面 6:
```java
@Component
@RocketMQTransactionListener(txProducerGroup = "PID_CONFIRM_REPAYMENT")
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
    @Autowired
    private RepaymentService repaymentService;

    @Override
    //收到消息后执行本地事务
    public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        //1.解析消息
        final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
        RepaymentPlan repaymentPlan = JSON.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
        RepaymentRequest repaymentRequest = JSON.parseObject(jsonObject.getString("repaymentRequest"), RepaymentRequest.class);
        //2.执行本地事务
        //3.返回结果
    }
```

画面 7:
```java
@Component
@RocketMQTransactionListener(txProducerGroup = "PID_CONFIRM_REPAYMENT")
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
    @Autowired
    private RepaymentService repaymentService;

    @Override
    //收到消息后执行本地事务
    public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        //1.解析消息
        final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
        RepaymentPlan repaymentPlan = JSON.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
        RepaymentRequest repaymentRequest = JSON.parseObject(jsonObject.getString("repaymentRequest"), RepaymentRequest.class);
        //2.执行本地事务
        repaymentService.confirmRepayment(repaymentPlan, repaymentRequest);
        //3.返回结果
    }
```

画面 8:
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //1.解析消息
    JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    RepaymentPlan repaymentPlan = JSON.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
    //2.查询事务状态
    RepaymentPlan newRepaymentPlan = newRepaymentPlanMapper.selectById(repaymentPlan.getId());
    //3.返回结果
    if (newRepaymentPlan != null && newRepaymentPlan.getRepaymentStatus().equals("1")) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面 10:
```java
//1.根据还款计划id查询还款计划
List<ReceivablePlan> receivablePlanList = receivablePlanMapper.selectList(Wrappers.<ReceivablePlan>lambdaQuery().eq(ReceivablePlan::getRepaymentPlanId, repaymentPlan.getId()));
//2.保存数据到receivable_detail表
ReceivableDetail receivableDetail = new ReceivableDetail();
receivableDetail.setReceivableId(receivablePlan.getId());
//应收款标识
receivableDetail.setAmount(receivablePlan.getAmount());
//应收款日期
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面 11:
```java
@Component
@RocketMQTransactionListener(txProducerGroup = "PID_CONFIRM_REPAYMENT")
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
    @Autowired
    private RepaymentService repaymentService;

    @Override
    //收到消息后执行本地事务
    public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        //1.解析消息
        final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
        RepaymentPlan repaymentPlan = JSON.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
        RepaymentRequest repaymentRequest = JSON.parseObject(jsonObject.getString("repaymentRequest"), RepaymentRequest.class);
        //2.执行本地事务
        //3.返回结果
    }
```

画面 12:
```java
//2.查询事务状态
RepaymentPlan newRepaymentPlan = newRepaymentPlanMapper.selectById(repaymentPlan.getId());
//3.返回结果
if (newRepaymentPlan != null && newRepaymentPlan.getRepaymentStatus().equals("1")) {
    return RocketMQLocalTransactionState.COMMIT;
} else {
    return RocketMQLocalTransactionState.ROLLBACK;
}
```

画面
