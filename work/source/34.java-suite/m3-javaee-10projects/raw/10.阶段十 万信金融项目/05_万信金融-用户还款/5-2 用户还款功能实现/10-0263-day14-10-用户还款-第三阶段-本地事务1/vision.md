# 画面线理解：day14-10-用户还款-第三阶段-本地事务1

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-10-用户还款-第三阶段-本地事务1_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:45, 01:22, 02:05, 02:47, 03:21, 04:51, 06:15, 07:09, 07:45, 08:16, 09:39, 10:07, 10:32, 11:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:19:29

1) 这一组画面整体在讲什么（一句话）：
讲解还款服务中确认还款的业务流程与对应的 Java 代码实现，包括消息确认、本地事务处理、数据库状态更新等环节。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示还款服务与 RocketMQ 之间的消息确认流程图，包含发送确认消息、消息接收成功、接收回调、执行本地事务、发送执行结果、修改消息状态、接收消息重试、通过 feign 向存管代理服务发请求等步骤。
画面2：展示还款服务与存管代理服务之间的消息处理流程图，包含更新交易记录、确认还款成功、处理请款确认还款、更新交易记录状态为“未同步”、更新交易记录状态为“已同步”、更新交易记录状态为“已还款”等步骤。
画面3：展示还款服务接口定义，新增 confirmRepayment 方法，参数为 RepaymentPlan 和 RepaymentRequest。
画面4：展示还款服务接口定义，新增 confirmRepayment 方法，参数为 RepaymentPlan 和 RepaymentRequest。
画面5：展示还款服务中生成还款计划的代码，包括获取投标信息、计算还款月数、生成还款计划、保存还款计划等。
画面6：展示数据库表结构，表名为 receivable_plan，包含 ID、USER_ID、TENDER_ID、REPAYMENT_ID、NUMBER_OF_INSTALLMENTS、INTEREST、PRINCIPAL、AMOUNT、SHOULD_RECEIVABLE_DATE、RECEIVABLE_STATUS、CREATE_DATE、COMMISSION 等字段。
画面7：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面8：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面9：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面10：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面11：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面12：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面13：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面14：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
/**
 * 确认还款处理
 * @param repaymentPlan
 * @param repaymentRequest
 * @return
 */
Boolean confirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest);
```

画面4：
```java
/**
 * 确认还款处理
 * @param repaymentPlan
 * @param repaymentRequest
 * @return
 */
Boolean confirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest);
```

画面5：
```java
// 1.4 计算还款月数
Double ceil = Math.ceil(projectDTO.getPeriod() / 30.0);
Integer month = ceil.intValue();

// 1.5 还款方式，只针对等额本息
String repaymentWay = RepaymentDTO.getRepaymentWay();

if (repaymentWay.equals(RepaymentWayCode.FIXED_REPAYMENT.getCode())) {
    EqualIntervalsRepayment fixedRepayment = RepaymentUtil.fixedRepayment(projectDTO, getAmount(), projectDTO.getPeriod());
    List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
}
```

画面6：
```sql
CREATE TABLE `receivable_plan` (
  `ID` bigint(20) NOT NULL,
  `USER_ID` bigint(20) NOT NULL,
  `TENDER_ID` bigint(20) NOT NULL,
  `REPAYMENT_ID` bigint(20) NOT NULL,
  `NUMBER_OF_INSTALLMENTS` int(11) NOT NULL,
  `INTEREST` decimal(10,2) NULL,
  `PRINCIPAL` decimal(10,2) NULL,
  `AMOUNT` decimal(10,2) NULL,
  `SHOULD_RECEIVABLE_DATE` datetime NULL,
  `RECEIVABLE_STATUS` tinyint(4) NULL,
  `CREATE_DATE` datetime NULL,
  `COMMISSION` decimal(10,2) NULL,
  `REPAYMENT_PLAN_ID` bigint(20) NOT NULL,
  `REPAYMENT_PLAN_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_CODE` varchar(50) NULL,
  `REPAYMENT_PLAN_NAME` varchar(255) NULL,
  `REPAYMENT_PLAN_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_REMARK` varchar(255) NULL,
  `REPAYMENT_PLAN_CREATE_DATE` datetime NULL,
  `REPAYMENT_PLAN_UPDATE_DATE` datetime NULL,
  `REPAYMENT_PLAN_DELETE_FLAG` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_DATE` datetime NULL,
  `REPAYMENT_PLAN_DELETE_USER_ID` bigint(20) NULL,
  `REPAYMENT_PLAN_DELETE_REASON` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE` varchar(50) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE` varchar(50) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE` varchar(50) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE` varchar(50) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE` varchar(50) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS
