# 画面线理解：day13-2-可靠消息实现最终一致性-入门案例-bank1-数据访问层

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-2-可靠消息实现最终一致性-入门案例-bank1-数据访问层_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:45, 02:49, 04:37, 05:06, 06:50, 08:31, 09:39, 10:28, 12:01, 13:11, 14:38, 15:04, 16:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:01:01

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Cloud 项目中，通过 RocketMQ 实现消息发送方（bank1）与消息接收方（bank2）之间的账户变更消息的可靠传输，包含事件定义、DAO层、消息生产者、事务消息等核心代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT标题页，内容为“5.3.3 功能实现”和“5.3.3.1 消息发送方bank1”，并提示“工程中提供的初始文件，由大家自行查看”。
画面2：展示PPT内容“5.3.2 环境搭建”，其中包含环境要求（数据库MySQL 5.7+、JDK 64位 jdk1.8+、微服务spring-boot 2.1.3、RocketMQ服务端4.5.0、RocketMQ客户端2.0.2-RELEASE）和“5.3.2.2 创建数据库”的说明，下方显示SQL语句：DROP TABLE IF EXISTS `de_duplication`;。
画面3：展示IDE中“AccountChangeEvent.java”文件，定义了账户变更事件类，包含字段accountNo、amount、txNo。
画面4：展示PPT内容“5.3.3.1 消息发送方bank1”，下方显示SQL语句：
UPDATE account_info SET account_balance=account_balance+#(amount)
WHERE account_no=#(accountNo);
SELECT * FROM account_info WHERE account_no=#(accountNo);
SELECT COUNT(1) FROM de_duplication WHERE tx_no = #{txNo};
画面5：展示IDE中“AccountInfoDao.java”文件，定义了接口方法，包含更新余额、查询账户信息、检查事务是否已执行的SQL语句。
画面6：展示IDE中“AccountInfoDao.java”文件，高亮显示更新余额的SQL语句。
画面7：展示PPT内容“3. 实现发送转账消息”，下方显示代码片段：
@Component
@RabbitListener
public class BankMessageProducer {
    @Resource
    private RocketMQTemplate rocketMQTemplate;
    ...
画面8：展示IDE中“message”包下右键新建文件的菜单，选项包括“Java Class”、“Kotlin File”、“XML Configuration File”等。
画面9：展示PPT内容“5.3.3.1 消息发送方bank1”，下方显示SQL语句：
SELECT * FROM account_info WHERE account_no=#(accountNo);
SELECT COUNT(1) FROM de_duplication WHERE tx_no = #{txNo};
画面10：展示IDE中“BankMessageProducer.java”文件，定义了消息生产者类，包含发送消息的方法。
画面11：展示IDE中“BankMessageProducer.java”文件，高亮显示导入的MessageBuilder类和Message类。
画面12：展示IDE中“BankMessageProducer.java”文件，高亮显示发送消息的代码：
Message<String> msg = MessageBuilder.withPayload(jsonObject.toJSONString()).build();
rocketMQTemplate.sendMessageInTransaction(msg, jsonObject.toJSONString());
画面13：展示IDE中“BankMessageProducer.java”文件，高亮显示事务消息状态处理方法：
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    RocketMQLocalTransactionState state = RocketMQLocalTransactionState.COMMIT;
    final JSONObject jsonObject = JSON.parseObject(new String(msg.getPayload()));
    ...
画面14：展示IDE中“AccountInfoServiceImpl.java”文件，定义了服务类，包含注入BankMessageProducer和AccountInfoDao的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
package cn.itcast.wanxinz.ensure.demo.bank1.model;
import ...
public class AccountChangeEvent implements Serializable {
    private String accountNo;
    // 变动金额
    private double amount;
    // 事务号、时间戳
    private long txNo;
}

画面4：
UPDATE account_info SET account_balance=account_balance+#(amount)
WHERE account_no=#(accountNo);
SELECT * FROM account_info WHERE account_no=#(accountNo);
SELECT COUNT(1) FROM de_duplication WHERE tx_no = #{txNo};

画面5：
import org.springframework.stereotype.Component;
public interface AccountInfoDao {
    // 修改某账号的余额
    @Param("accountNo") 账号
    @Param("amount") 变动金额
    @Return
    // Update "update account_info set account_balance=account_balance+#(amount) where account_no=#(accountNo)"
    int updateAccountBalance(@Param("accountNo") String accountNo, @Param("amount") Double amount);
    // 查询某账号信息
    @Param("accountNo") 账号
    @Return
    // Select "select * from account_info where account_no=#(accountNo)"
    AccountInfo findbyAccountId(@Param("accountNo") String accountNo);
    // 查询某事务是否已执行
    @Param("txNo") 事务号
    @Return
    // Select "select count(1) from de_duplication where tx_no = #{txNo}"
    int isExistTx(long txNo);
}

画面7：
@Component
@RabbitListener
public class BankMessageProducer {
    @Resource
    private RocketMQTemplate rocketMQTemplate;
    ...

画面10：
import cn.itcast.wanxinz.ensure.demo.bank1.model.AccountChangeEvent;
import com.alibaba.fastjson.JSONObject;
import org.apache.rocketmq.spring.core.RocketMQTemplate;
import java.util.Map;
public class BankMessageProducer {
    @Resource
    private RocketMQTemplate rocketMQTemplate;
    public void sendAccountChangeEvent(AccountChangeEvent accountChangeEvent) {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("accountChange", accountChangeEvent);
        Message<String> msg = MessageBuilder.withPayload(jsonObject.toJSONString()).build();
        rocketMQTemplate.sendMessageInTransaction(msg, jsonObject.toJSONString());
    }
}

画面11：
import cn.itcast.wanxinz.ensure.demo.bank1.model.AccountChangeEvent;
import com.alibaba.fastjson.JSONObject;
import org.apache.rocketmq.spring.core.RocketMQTemplate;
import org.springframework.messaging.Message;
import org.springframework.messaging.support.MessageBuilder;
import org.springframework.stereotype.Component;
import org.springframework.util.Assert;

画面12：
Message<String> msg = MessageBuilder.withPayload(jsonObject.toJSONString()).build();
rocketMQTemplate.sendMessageInTransaction(msg, jsonObject.toJSONString());

画面13：
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    // 初始化事务状态
    RocketMQLocalTransactionState state = RocketMQLocalTransactionState.COMMIT;
    final JSONObject jsonObject = JSON.parseObject(new String(msg.getPayload()));
    AccountChangeEvent accountChangeEvent = (AccountChangeEvent) jsonObject.get("accountChange");
    // 根据业务逻辑决定事务状态
    if (accountChangeEvent != null) {
        // 业务逻辑处理
        // 如果成功则提交事务
        state = RocketMQLocalTransactionState.COMMIT;
    } else {
        // 如果失败则回滚事务
        state = RocketMQLocalTransactionState.ROLLBACK;
    }
    return state;
}

画面14：
@Service
public class AccountInfoServiceImpl implements AccountInfoService {
    @Autowired
    private BankMessageProducer bankMessageProducer;
    @Autowired
    private AccountInfoDao accountInfoDao;
    @Override
    public void updateAccountBalance(AccountChangeEvent accountChange) {
        // 1. 查询账户信息
        AccountInfo accountInfo = accountInfoDao.findbyAccountId(accountChange.getAccountNo());
        // 2. 检查事务是否已执行
        if (accountInfoDao.isExistTx(accountChange.getTxNo())) {
            // 3. 事务已执行，直接返回
            return;
        }
        // 4. 更新账户余额
        accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
        // 5. 发送消息
        bankMessageProducer.sendAccountChangeEvent(accountChange);
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“5.3.3 功能实现”，副标题为“5.3.3.1 消息发送方bank1”。
画面2：PPT标题为“5.3.2 环境搭建”，包含子标题“5.3.2.1 环境要求”和“5.3.2.2 创建数据库”。
画面4：PPT标题为“5.3.3.1 消息发送方bank1”，下方列出SQL语句。
画面7：PPT标题为“3. 实现发送转账消息”，下方列出代码片段。
画面9：PPT标题为“5.3.3.1 消息发送方bank1”，下方列出SQL语句。
画面14：PPT标题为“5.3.3.1 消息发送方bank1”，下方列出代码片段。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
