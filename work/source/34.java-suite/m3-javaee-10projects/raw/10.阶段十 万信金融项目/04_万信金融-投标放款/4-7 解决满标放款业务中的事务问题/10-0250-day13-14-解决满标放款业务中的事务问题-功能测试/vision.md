# 画面线理解：day13-14-解决满标放款业务中的事务问题-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-7 解决满标放款业务中的事务问题
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-7 解决满标放款业务中的事务问题\day13-14-解决满标放款业务中的事务问题-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:36, 01:59, 04:13, 05:17, 06:41, 08:28, 09:03, 10:07, 10:42, 11:37, 12:16, 12:51, 13:45, 15:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:10:17

1) 这一组画面整体在讲什么（一句话）：
演示分布式事务场景下的业务流程图、Apollo配置中心的参数设置、以及相关Java服务代码的实现细节，重点在于如何通过RocketMQ实现最终一致性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示一个业务流程图，描述了从“开始”到“故障成功”的多个步骤，涉及“修改标的”、“生成还款计划”、“启动还款”等操作，图中包含多个编号步骤（如10、11、12、13、14、15、16、17、18、19、20、21、22、23、24、25）。
画面2：展示Apollo配置中心的界面，列出了多个已发布配置项，包括数据库连接信息、分库策略、项目ID映射规则等。
画面3：展示IDE中ProjectServiceImpl.java文件的代码，包含一个@Transactional注解的方法updateProjectStatusAndStartRepayment，用于更新项目状态并启动还款。
画面4：展示“万信金融管理平台”的“标的放款管理”页面，列出了多个借款标的，包括借款人、金额、创建时间、期限、状态、年化利率等信息。
画面5：展示PPT内容，标题为“分布式事务（一）”，其中包含一个关于RocketMQ如何解决分布式事务最终一致性的流程图，图中包含“本地事务”、“发送方”、“服务端”、“接收方”四个节点，以及它们之间的交互流程。
画面6：展示PPT内容，标题为“5.4.3 功能测试”，其中包含“5.4.4 Apollo配置（交易中心）”部分，列出三个配置项及其值：borrower.annual.rate=0.05、commission.borrower.annual.rate=0.02、commission.investor.annual.rate=0.01，并说明这三个数据不能为0。
画面7：展示IDE中RepaymentServiceImpl.java文件的代码，包含一个方法startRepayment，用于启动还款流程。
画面8：展示IDE中RepaymentServiceImpl.java文件的代码，包含一个方法saveRepaymentPlan，用于保存还款计划。
画面9：展示IDE中RepaymentServiceImpl.java文件的代码，包含一个方法saveRepaymentPlan，用于保存还款计划，其中包含SQL语句：UPDATE project SET ... WHERE ID = ?。
画面10：展示IDE中RepaymentServiceImpl.java文件的代码，包含一个方法saveRepaymentPlan，用于保存还款计划，其中包含注释“获取每期利息”、“获取每期本金”。
画面11：展示IDE中StartRepaymentMessageConsumer.java文件的代码，包含一个onMessage方法，用于处理消息。
画面12：展示PPT内容，标题为“5.4.3 功能测试”，其中包含“5.4.4 Apollo配置（交易中心）”部分，列出三个配置项及其值：borrower.annual.rate=0.05、commission.borrower.annual.rate=0.02、commission.investor.annual.rate=0.01，并说明这三个数据不能为0。
画面13：展示浏览器中Apollo配置中心的空白页面。
画面14：展示业务流程图，描述了从“开始”到“故障成功”的多个步骤，涉及“修改标的”、“生成还款计划”、“启动还款”等操作，图中包含多个编号步骤（如10、11、12、13、14、15、16、17、18、19、20、21、22、23、24、25）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```
# 已发布
spring.shardingsphere.d.s1.driver-class-name
jdbc:mysql://localhost:3306/p2p_transaction_1_fuse
# 已发布
spring.shardingsphere.d.s1.username
root
# 已发布
spring.shardingsphere.d.s1.password
123
# 已发布
spring.shardingsphere.d.s1.database-strategy.inline.sharding-column
CONSUMER_ID
# 已发布
spring.shardingsphere.d.s1.database-strategy.inline.algorithm
ds$->{CONSUMER_ID % 2}
# 已发布
spring.shardingsphere.d.s1.table-strategy.inline.sharding-column
ID
# 已发布
spring.shardingsphere.d.s1.table-strategy.inline.algorithm
project.$->{ID % 2}
```

画面3：
```java
@Transactional(rollbackFor = BusinessException.class)
@Override
public Boolean updateProjectStatusAndStartRepayment(Project project) {
    project.setProjectStatus(ProjectCode.REPAYING.getCode());
    return true;
}
```

画面7：
```java
// 保存应还款计划数据
planlist.forEach(plan -> {
    saveReceivablePlan(plan, tenderDTO, receipt);
});
else {
    return "-1";
}
System.out.println(10/0);
return DepositoryReturnCode.RETURN_CODE_00000.getCode();
```

画面8：
```java
// 保存还款计划到数据库
public List<RepaymentPlan> saveRepaymentPlan(ProjectDTO projectDTO, EqualInterestRepayment fixedRepayment) {
    List<RepaymentPlan> repaymentPlanList = new ArrayList<>();
    // 获取每期利息
    final Map<Integer, BigDecimal> interestMap = fixedRepayment.getInterestMap();
    // 获取每期本金
    final Map<Integer, BigDecimal> commissionMap = fixedRepayment.getPrincipalMap();
    fixedRepayment.getPrincipleMap().forEach((k, v) -> {
        // ...
    });
}
```

画面9：
```sql
UPDATE project SET
    IS_ASSIGNMENT=?,
    REPAYMENT_WAY=?,
    AMOUNT=?,
    PROJECT_STATUS=?,
    CREATE_DATE=?,
    STATUS=?,
    WHERE ID = ?
```

画面11：
```java
@org.apache.rocketmq.spring.annotation.RocketMQMessageListener(
    consumerGroup = "defaultGroup",
    topic = "p2p.repayment.message"
)
public class StartRepaymentMessageConsumer implements MessageListenerConcurrent {
    @Override
    public ConsumeResult consumeMessage(ConsumeRequest consumeRequest) {
        // ...
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：
标题：分布式事务（一）
流程图：
- 本地事务 → 发送方 → 服务端 → 接收方
- 发送方 → 服务端（发送消息）
- 服务端 → 接收方（消息消费）
- 本地事务 → 服务端（执行本地事务）
- 服务端 → 接收方（返回消息）

画面6：
标题：5.4.3 功能测试
子标题：5.4.4 Apollo配置（交易中心）
表格数据：
- borrower.annual.rate: 0.05
- commission.borrower.annual.rate: 0.02
- commission.investor.annual.rate: 0.01

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
