# 画面线理解：day13-8-可靠消息实现最终一致性-入门案例-bank2-消费消息

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-8-可靠消息实现最终一致性-入门案例-bank2-消费消息_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:52, 01:13, 01:50, 02:36, 03:18, 04:50, 06:16, 07:21, 07:39, 08:08, 08:45, 09:15, 09:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:05:34

1) 这一组画面整体在讲如何使用 RocketMQ 实现银行转账消息的可靠消费，包括消息生产者、消费者代码编写、事务消息处理及相关配置。

2) 按时间顺序列出每张画面的要点：
画面1：展示 `AccountInfoServiceImpl` 类，其中 `updateAccountBalance` 方法使用 `@Transactional` 注解，并包含事务回滚逻辑。
画面2：在 `AccountInfoServiceImpl` 类中，鼠标悬停在 `@Transactional(isolation = Isolation.SERIALIZABLE)` 注解上，显示其作用。
画面3：展示 `EnsureMessageConsumer` 类的初始状态，提示需要实现 `RocketMQListener` 接口。
画面4：在 `EnsureMessageConsumer` 类中，开始编写 `onMessage` 方法的骨架。
画面5：在 `EnsureMessageConsumer` 类中，显示 `RocketMQListener` 的构造函数参数列表。
画面6：切换到 `BankMessageProducer` 类，展示其所在项目结构。
画面7：展示 RocketMQ 的 Producer Group 与 Consumer Group 架构图，说明其作用。
画面8：展示 PPT 页面，标题为“5.3.4 功能测试”，内容为“bank1本地事务失败，则bank1不发送转账消息”。
画面9：在 `EnsureMessageConsumer` 类中，开始编写 `onMessage` 方法，解析 JSON 消息。
画面10：在 `EnsureMessageConsumer` 类中，使用 `@Autowired` 注解注入 `AccountInfoService`。
画面11：展示多个窗口，包括 `day13` 文件夹和 PPT 页面。
画面12：在 `EnsureMessageConsumer` 类中，添加 `@RocketMQListener` 注解并指定 topic 和 consumerGroup。
画面13：在 `EnsureMessageConsumer` 类中，编写业务逻辑，调用 `accountInfoService.updateAccountBalance` 方法。
画面14：在 `AccountInfoServiceImpl` 类中，高亮显示 `if (idExists != 0)` 条件判断语句。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
import org.springframework.transaction.annotation.Isolation;
import org.springframework.transaction.annotation.Transactional;

@Service
@MSF4
public class AccountInfoServiceImpl implements AccountInfoService {
    private AccountInfoDao accountInfoDao;

    @Transactional(isolation = Isolation.SERIALIZABLE)
    public void updateAccountBalance(AccountChangeEvent accountChange) {
        int idExists = accountInfoDao.indexById(accountChange.getAccountId());
        if (idExists != 0) {
            accountInfoDao.updateAccountBalance(accountChange.getAccountId(), accountChange.getAmount());
            accountInfoDao.add(accountChange.getToId());
        }
    }
}
```

画面3：
```java
package cn.itcast.wanxin.ensure.demo.bank2.message;

public class EnsureMessageConsumer implements {
    // ... (未完整显示)
}
```

画面4：
```java
package cn.itcast.wanxin.ensure.demo.bank2.message;

public class EnsureMessageConsumer implements RocketMQListener<String> {
    @Override
    public void onMessage(String message) {
    }
}
```

画面5：
```java
public class EnsureMessageConsumer implements RocketMQListener<String> {
    @Override
    public void onMessage(String message) {
    }
}
```

画面9：
```java
public void onMessage(String message) {
    System.out.println("待转消息。" + message);
    // 原始消息
    final JSONObject jsonObject = JSON.parseObject(message);
    AccountChangeEvent accountChangeEvent = JSON.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
}
```

画面10：
```java
@Autowired
private AccountInfoService accountInfoService;
```

画面12：
```java
@RocketMQListener(topic = "topic_ensure_transfer", consumerGroup = "consumer_ensure_transfer")
public class EnsureMessageConsumer implements RocketMQListener<String> {
    @Autowired
    private AccountInfoService accountInfoService;
```

画面13：
```java
public void onMessage(String message) {
    System.out.println("销售消息。" + message);
    // 原始消息
    final JSONObject jsonObject = JSON.parseObject(message);
    AccountChangeEvent accountChangeEvent = JSON.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    // 执行本地事务
    accountChangeEvent.setAccountId("2");
    accountInfoService.updateAccountBalance(accountChangeEvent);
}
```

画面14：
```java
@Transactional(isolation = Isolation.SERIALIZABLE)
public void updateAccountBalance(AccountChangeEvent accountChange) {
    int idExists = accountInfoDao.indexById(accountChange.getAccountId());
    if (idExists != 0) {
        accountInfoDao.updateAccountBalance(accountChange.getAccountId(), accountChange.getAmount());
        accountInfoDao.add(accountChange.getToId());
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面7：
架构图：
- Producer Group A 包含 P1、P2、P3，指向 Broker 集群。
- Consumer Group A 包含 C1、C2、C3，指向 Broker 集群。
- Producer Group B 包含 P1、P3，指向 Broker 集群。
- Consumer Group B 包含 C1、C2、C3，指向 Broker 集群。
文字说明：
1. Producer Group：用于表示一个发送消息应用，一个 Producer Group 下包含多个 Producer 实例，可以是多台机器，也可以是一台机器的多个进程，或者一个进程的多个 Producer 对象。一个 Producer Group 可以发送多个 Topic 消息。Producer Group 作用如下：
   - 标识一类 Producer；
   - 可以通过运维工具查询这个发送消息应用下有多少个 Producer 实例；
   - 发送分布式事务消息时，如果 Producer 中途意外宕机，Broker 会主动回调 Producer Group 内任意一台机器来确认事务状态。
2. Consumer Group：用于表示一个消费消息应用，一个 Consumer Group 下包含多个 Consumer 实例，可以是多台机器，也可以是多个进程，或者是一个进程的多个 Consumer 对象。一个 Consumer Group 下的多个 Consumer 以均摊方式消费消息。如果设置为广播方式，那么这个 Consumer Group 下的每个实例都消费全部数据。

画面8：
PPT 标题：5.3.4 功能测试
内容：
- bank1本地事务失败，则bank1不发送转账消息。

5) 无。
