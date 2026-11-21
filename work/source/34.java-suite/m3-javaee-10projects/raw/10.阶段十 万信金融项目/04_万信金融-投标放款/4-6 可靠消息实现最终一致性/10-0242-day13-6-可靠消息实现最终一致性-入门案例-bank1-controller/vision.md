# 画面线理解：day13-6-可靠消息实现最终一致性-入门案例-bank1-controller

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-6-可靠消息实现最终一致性-入门案例-bank1-controller_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:25, 00:55, 01:23, 01:52, 02:23, 02:52, 03:34, 04:02, 04:16, 04:30, 04:57, 05:33, 05:52, 06:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:04:07

1) 这一组画面整体在讲什么（一句话）：
演示如何在 RocketMQ 中实现消息的本地事务保障，通过自定义事务监听器来确保消息消费与数据库操作的最终一致性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `TransferTransactionListenerImpl` 类中 `checkLocalTransaction` 方法的代码，用于解析消息并根据数据库操作结果返回事务状态（COMMIT 或 ROLLBACK）。
画面2：展示 `TransferTransactionListenerImpl` 类中 `checkLocalTransaction` 方法的代码，注释说明了事务状态的初始设置和业务逻辑。
画面3：展示 `AccountInfoController` 类中 `transfer` 方法的代码，调用 `accountInfoService.updateAccountBalance` 方法进行转账操作。
画面4：展示 `AccountChangeEvent` 类的定义，包含 `accountNo`、`amount` 和 `txId` 三个私有属性。
画面5：展示 `AccountInfoController` 类中 `transfer` 方法的代码，调用 `accountInfoService.updateAccountBalance` 方法并传入 `AccountChangeEvent` 对象。
画面6：展示 `AccountInfoController` 类中 `transfer` 方法的代码，返回字符串“转账成功”。
画面7：展示 `AccountInfoServiceImpl` 类中 `updateAccountBalance` 方法的代码，调用 `bankMessageProducer.sendAccountChangeEvent` 发送消息，并定义 `doUpdateAccountBalance` 方法进行数据库操作。
画面8：展示 `TransferTransactionListenerImpl` 类中 `checkLocalTransaction` 方法的代码，注释说明了事务状态的初始设置和业务逻辑。
画面9：展示 `TransferTransactionListenerImpl` 类中 `executeLocalTransaction` 方法的代码，用于执行本地事务，通过 try-catch 块控制事务提交或回滚。
画面10：展示一个 PPT 页面，包含多个窗口截图，其中一个窗口显示了 `AccountChangeEvent` 类的定义，另一个窗口显示了 `TransferTransactionListenerImpl` 类的代码，还有一个窗口显示了 `SQLyog` 数据库管理工具的界面。
画面11：展示 `TransferTransactionListenerImpl` 类中 `executeLocalTransaction` 方法的代码，根据 `isCommit` 的值返回 `COMMIT` 或 `ROLLBACK`。
画面12：展示 `TransferTransactionListenerImpl` 类中 `checkLocalTransaction` 方法的代码，注释说明了事务状态的初始设置和业务逻辑。
画面13：展示 `SQLyog` 数据库管理工具中 `bank1` 数据库的 `tx_id` 表，显示了 `tx_id` 为 1 的记录。
画面14：展示 `TransferTransactionListenerImpl` 类中 `checkLocalTransaction` 方法的代码，注释说明了事务状态的初始设置和业务逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //查询de_duplication表
    int isExistTx = accountInfoDao.isExistTx(accountChangeEvent.getTxId());
    //根据查询结果返回
    if (isExistTx > 0) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面2：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //初始化事务状态
    RocketMQLocalTransactionState state;
    //解析消息中的业务数据
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //查询已执行事务
    int isExistTx = accountInfoDao.isExistTx(accountChangeEvent.getTxNo());
    if (isExistTx > 0) {
        state = RocketMQLocalTransactionState.COMMIT;
    } else {
        state = RocketMQLocalTransactionState.ROLLBACK;
    }
    return state;
}
```

画面3：
```java
@RestController
@S1f4
public class AccountInfoController {
    private AccountInfoService accountInfoService;
    @GetMapping(value = "/transfer")
    public String transfer() {
        accountInfoService.updateAccountBalance();
    }
}
```

画面4：
```java
package cn.itcast.wanxintz.ensuredemo.bank1.model;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class AccountChangeEvent implements Serializable {
    private String accountNo;
    private double amount;
    private long txId;
}
```

画面5：
```java
@RestController
@S1f4
public class AccountInfoController {
    private AccountInfoService accountInfoService;
    @GetMapping(value = "/transfer")
    public String transfer() {
        accountInfoService.updateAccountBalance(new AccountChangeEvent("1", amount: 100, System.currentTimeMillis()));
    }
}
```

画面6：
```java
@RestController
@S1f4
public class AccountInfoController {
    private AccountInfoService accountInfoService;
    @GetMapping(value = "/transfer")
    public String transfer() {
        accountInfoService.updateAccountBalance(new AccountChangeEvent("1", amount: 100, System.currentTimeMillis()));
        return "转账成功";
    }
}
```

画面7：
```java
@Autowired
private BankMessageProducer bankMessageProducer;
@Autowired
private AccountInfoDao accountInfoDao;
@Override
public void updateAccountBalance(AccountChangeEvent accountChange) {
    bankMessageProducer.sendAccountChangeEvent(accountChange);
}
@Override
@Transactional(isolation = Isolation.SERIALIZABLE)
public void doUpdateAccountBalance(AccountChangeEvent accountChange) {
    accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount(), accountChange.getTxId());
    accountInfoDao.addTx(accountChange.getTxId());
}
```

画面8：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //查询de_duplication表
    int isExistTx = accountInfoDao.isExistTx(accountChangeEvent.getTxId());
    //根据查询结果返回
    if (isExistTx > 0) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面9：
```java
@Override
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    //接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //执行本地事务
    Boolean isCommit = true;
    try {
        accountInfoService.doUpdateAccountBalance(accountChangeEvent);
    } catch (Exception e) {
        isCommit = false;
    }
    //返回执行结果
    if (isCommit) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面10：无代码或配置内容。

画面11：
```java
@Override
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    //接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //执行本地事务
    Boolean isCommit = true;
    try {
        accountInfoService.doUpdateAccountBalance(accountChangeEvent);
    } catch (Exception e) {
        isCommit = false;
    }
    //返回执行结果
    if (isCommit) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面12：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //查询de_duplication表
    int isExistTx = accountInfoDao.isExistTx(accountChangeEvent.getTxId());
    //根据查询结果返回
    if (isExistTx > 0) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面13：
```sql
SELECT tx_id, account_no, amount, create_time FROM tx_id WHERE tx_id = 1;
```

画面14：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //查询de_duplication表
    int isExistTx = accountInfoDao.isExistTx(accountChangeEvent.getTxId());
    //根据查询结果返回
    if (isExistTx > 0) {
        return RocketMQLocalTransactionState
