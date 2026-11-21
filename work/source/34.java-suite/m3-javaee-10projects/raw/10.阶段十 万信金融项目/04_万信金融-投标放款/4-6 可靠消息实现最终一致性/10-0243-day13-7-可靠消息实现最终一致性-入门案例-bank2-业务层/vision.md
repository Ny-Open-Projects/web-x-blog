# 画面线理解：day13-7-可靠消息实现最终一致性-入门案例-bank2-业务层

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-7-可靠消息实现最终一致性-入门案例-bank2-业务层_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:02, 01:47, 02:21, 03:24, 04:12, 05:23, 07:02, 07:19, 08:32, 09:14, 10:11, 11:12, 12:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:04:53

1) 这一组画面整体在讲如何在 RocketMQ 消息系统中实现消息的可靠消费，通过本地事务控制确保消息消费成功后，本地业务操作一定执行成功，防止消息重复消费。

2) 按时间顺序列出每张画面的要点：
画面1：展示 TransferTransactionListenerImpl 类中的 checkLocalTransaction 方法，用于检查本地事务状态，根据是否存在事务记录返回 COMMIT 或 ROLLBACK。
画面2：展示 AccountInfoDao 接口中的 SQL 语句，用于查询账户信息和更新账户余额。
画面3：展示 AccountInfoDao 接口中的 SQL 语句，用于查询事务记录是否存在，并插入事务记录。
画面4：展示 AccountInfoDao 接口中的 SQL 语句，用于查询账户信息。
画面5：展示 AccountInfoService 类中 updateAccountBalance 方法的实现，用于更新账户余额。
画面6：展示 AccountInfoServiceImpl 类中的 updateAccountBalance 方法，包含事务注解和业务逻辑。
画面7：展示 AccountInfoServiceImpl 类中的 updateAccountBalance 方法，包含事务注解和业务逻辑。
画面8：展示 AccountInfoService 接口和 AccountInfoServiceImpl 类的定义。
画面9：展示 PPT 页面，内容为 RocketMQ 可靠消息的介绍，包括消息发送方执行本地事务与发送消息的原子性问题。
画面10：展示 AccountInfoServiceImpl 类中的 updateAccountBalance 方法，包含事务注解和业务逻辑。
画面11：展示 PPT 页面，内容为实现转发消息的步骤。
画面12：展示 AccountInfoServiceImpl 类中的 updateAccountBalance 方法，包含事务注解和业务逻辑。
画面13：展示 SQLyog 数据库管理工具界面，显示数据库连接和表结构。
画面14：展示 SQLyog 数据库管理工具界面，显示数据库连接和表结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString(key: "accountChange"), AccountChangeEvent.class);
    int isExistTx = accountInfoDao.isExistTx(accountChangeEvent.getTxNo());
    // 根据查询结果返回
    if(isExistTx != 0) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面2：
```java
// 修改其账号的余额
@Update("update account_info set account_balance=account_balance+#{amount} where account_no=#{accountNo}")
int updatedAccountBalance(@Param("accountNo") String accountNo, @Param("amount") Double amount);

// 查询账户信息
@Select("select * from account_info where where account_no=#{accountNo}")
AccountInfo findByIdAccountNo(@Param("accountNo") String accountNo);
```

画面3：
```java
// 查询事务记录是否存在
@Select("select count(1) from de_duplication where tx_no = #{txNo}")
int isExistTx(long txNo);

// 保存事务执行记录
@Insert("insert into de_duplication values(#{txNo},now());")
int addTx(long txNo);
```

画面6：
```java
@Service
@Slf4j
public class AccountInfoServiceImpl implements AccountInfoService {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Override
    @Transactional(isolation = Isolation.SERIALIZABLE)
    public void updateAccountBalance(AccountChangeEvent accountChange) {
        int isExistTx = accountInfoDao.isExistTx(accountChange.getTxNo());
        if(isExistTx == 0) {
            accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
            accountInfoDao.addTx(accountChange.getTxNo());
        }
    }
}
```

画面7：
```java
import cn.itcast.wanxin.ensure.demo.bank2.model.AccountChangeEvent;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.annotation.Isolation;
import org.springframework.stereotype.Service;
@Service
@Slf4j
public class AccountInfoServiceImpl implements AccountInfoService {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Override
    @Transactional(isolation = Isolation.SERIALIZABLE)
    public void updateAccountBalance(AccountChangeEvent accountChange) {
        accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
        accountInfoDao.addTx(accountChange.getTxNo());
    }
}
```

画面8：
```java
public interface AccountInfoService {
    /**
     * 更新账户余额
     * @param accountChange
     */
    void updateAccountBalance(AccountChangeEvent accountChange);
}

@Service
@Slf4j
public class AccountInfoServiceImpl implements AccountInfoService {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Override
    @Transactional(isolation = Isolation.SERIALIZABLE)
    public void updateAccountBalance(AccountChangeEvent accountChange) {
        int isExistTx = accountInfoDao.isExistTx(accountChange.getTxNo());
        if(isExistTx == 0) {
            accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
            accountInfoDao.addTx(accountChange.getTxNo());
        }
    }
}
```

画面9：
```text
5.2 RocketMQ可靠消息

RocketMQ 是一个来自阿里巴巴的分布式消息中间件，于 2012 年开源，并在 2017 年正式成为 Apache 顶级项目。Apache RocketMQ 4.3 之后的版本支持事务消息，为分布式事务实现提供了便利支持。因此，我们通过 RocketMQ 就可以解决前面的问题。

1.消息发送方执行本地事务与发送消息的原子性问题，也就是说如何保证本地事务执行成功，消息一定发送成功
```

画面10：
```java
public void updateAccountBalance(AccountChangeEvent accountChange) {
    accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
    accountInfoDao.addTx(accountChange.getTxNo());
}
```

画面11：
```text
3. 实现转发消息
```

画面12：
```java
@Override
@Transactional(isolation = Isolation.SERIALIZABLE)
public void updateAccountBalance(AccountChangeEvent accountChange) {
    accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
    accountInfoDao.addTx(accountChange.getTxNo());
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面9：
标题：5.2 RocketMQ可靠消息
内容：
- RocketMQ 是一个来自阿里巴巴的分布式消息中间件，于 2012 年开源，并在 2017 年正式成为 Apache 顶级项目。Apache RocketMQ 4.3 之后的版本支持事务消息，为分布式事务实现提供了便利支持。因此，我们通过 RocketMQ 就可以解决前面的问题。
- 1.消息发送方执行本地事务与发送消息的原子性问题，也就是说如何保证本地事务执行成功，消息一定发送成功

画面11：
标题：3. 实现转发消息

5) 不要评价画面美观，不要输出与课程无关的内容。
