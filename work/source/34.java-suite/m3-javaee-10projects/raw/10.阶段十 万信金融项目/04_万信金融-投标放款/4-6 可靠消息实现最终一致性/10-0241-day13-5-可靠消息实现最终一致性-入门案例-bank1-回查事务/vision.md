# 画面线理解：day13-5-可靠消息实现最终一致性-入门案例-bank1-回查事务

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-5-可靠消息实现最终一致性-入门案例-bank1-回查事务_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:42, 00:57, 01:10, 02:44, 03:10, 04:16, 05:00, 05:46, 06:09, 06:32, 07:44, 08:20, 09:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:03:14

1) 这一组画面整体在讲什么（一句话）：
演示 RocketMQ 事务消息的实现原理与代码结构，包括本地事务执行、消息确认、以及事务状态回查的逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`executeLocalTransaction(Message msg, Object arg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoService` 的 `doUpdateAccountBalance` 方法执行本地事务。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    //1.解析并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.执行本地事务
    boolean inCommit = true;
    try {
        accountInfoService.doUpdateAccountBalance(accountChangeEvent);
    } catch (Exception e) {
        inCommit = false;
    }
    //3.返回执行结果
    if(inCommit) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面2：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`checkLocalTransaction(Message msg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoDao` 的 `isExistTx` 方法检查事务是否存在。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //1.接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.查询事务
    accountInfoDao.isExistTx(accountChangeEvent);
}
```

画面3：
- PPT 标题：5.3.2.4 Maven 工程
- 内容：在 IDEA 中导入 Maven 工程 `wanxin-ensure-message-demo`，其中 `ensure-message-demo-bank1` 负责操作张三账户，连接数据库 bank1；`ensure-message-demo-bank2` 负责操作李四账户，连接数据库 bank2。
- 项目结构图：显示了 `pom.xml` 文件和两个子模块 `ensure-message-demo-bank1`、`ensure-message-demo-bank2`。

画面4：
- PPT 标题：5.2 RocketMQ 可靠消息
- 内容：
  1. 数据库操作
  2. 发送消息
  3. 消息接收方与本地事务的原子性问题
  4. 消息重试机制
  5. 事务消息的必要性

画面5：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`checkLocalTransaction(Message msg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoDao` 的 `isExistTx` 方法检查事务是否存在。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //1.接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.查询事务
    accountInfoDao.isExistTx(accountChangeEvent);
}
```

画面6：
- 代码文件：`AccountInfoServiceImpl.java`
- 方法：`doUpdateAccountBalance(AccountChangeEvent accountChange)`
- 代码逻辑：调用 `accountInfoDao` 的 `updateAccountBalance` 方法更新账户余额。
- 代码片段：
```java
@Override
@Transactional(isolation = Isolation.SERIALIZABLE)
public void doUpdateAccountBalance(AccountChangeEvent accountChange) {
    accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
    accountInfoDao.addTx(accountChange.getAccountNo(), accountChange.getAmount());
}
```

画面7：
- 代码文件：`AccountInfoServiceImpl.java`
- 方法：`doUpdateAccountBalance(AccountChangeEvent accountChange)`
- 代码逻辑：调用 `accountInfoDao` 的 `updateAccountBalance` 方法更新账户余额。
- 代码片段：
```java
@Override
@Transactional(isolation = Isolation.SERIALIZABLE)
public void doUpdateAccountBalance(AccountChangeEvent accountChange) {
    accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
    accountInfoDao.addTx(accountChange.getAccountNo(), accountChange.getAmount());
}
```

画面8：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`executeLocalTransaction(Message msg, Object arg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoService` 的 `doUpdateAccountBalance` 方法执行本地事务。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    //1.解析并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.执行本地事务
    boolean inCommit = true;
    try {
        accountInfoService.doUpdateAccountBalance(accountChangeEvent);
    } catch (Exception e) {
        inCommit = false;
    }
    //3.返回执行结果
    if(inCommit) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面9：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`checkLocalTransaction(Message msg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoDao` 的 `isExistTx` 方法检查事务是否存在。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //1.接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.查询事务
    accountInfoDao.isExistTx(accountChangeEvent);
}
```

画面10：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`executeLocalTransaction(Message msg, Object arg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoService` 的 `doUpdateAccountBalance` 方法执行本地事务。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    //1.解析并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.执行本地事务
    boolean inCommit = true;
    try {
        accountInfoService.doUpdateAccountBalance(accountChangeEvent);
    } catch (Exception e) {
        inCommit = false;
    }
    //3.返回执行结果
    if(inCommit) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面11：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`checkLocalTransaction(Message msg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoDao` 的 `isExistTx` 方法检查事务是否存在。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //1.接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.查询事务
    accountInfoDao.isExistTx(accountChangeEvent);
}
```

画面12：
- 架构图：RocketMQ 事务消息流程图
- 结构：
  - 本地事务（A服务数据库） → 发送方（A服务） → 服务端（Broker） → 接收方（B服务）
  - 发送方 → 服务端：1. 发送半消息；2. 半消息发送成功
  - 服务端 → 发送方：4. Commit 或者 Rollback
  - 发送方 → 服务端：5. 未收到4的确认时，回查事务状态
  - 服务端 → 发送方：6. 检查本地事务的状态
  - 服务端 → 接收方：7. 根据事务的状态 Commit/Rollback

画面13：
- 数据库界面：`bank1` 数据库
- 表：`t_account`
- 数据：`account_no` 为 `00011`，`account_balance` 为 `10000`。
- 操作：执行 SQL `UPDATE t_account SET account_balance = account
