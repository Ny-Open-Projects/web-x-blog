# 画面线理解：day12-13-满标放款-接口4-业务层-保存还款计划

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-13-满标放款-接口4-业务层-保存还款计划_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 02:22, 03:42, 05:44, 07:58, 10:53, 11:46, 13:17, 14:40, 16:37, 17:13, 18:41, 19:28, 20:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:54:47

1) 这一组画面整体在讲什么（一句话）：
讲解如何在万通金融项目中实现等额本息还款计划的计算与数据库持久化，包括相关实体类、服务层代码及数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档，讲解等额本息还款方式的计算公式。
画面2：展示数据库表结构，列出还款计划表（repayment_plan）的字段和索引。
画面3：展示还款计划实体类（RepaymentPlan）的代码，包含金额、应还款日期、状态等字段。
画面4：展示服务层代码，定义了保存还款计划的方法。
画面5：展示服务层代码，调用固定还款计算工具类（FixedRepayment）获取利息和本金映射。
画面6：展示服务层代码，使用循环创建还款计划对象并设置属性。
画面7：展示课程文档目录，定位到还款服务功能实现章节。
画面8：展示服务层代码，设置还款计划对象的属性，包括项目ID、借款人信息、期数、利息、本金等。
画面9：展示服务层代码，设置还款计划的应还款日期、状态和创建时间，然后调用mapper插入数据库。
画面10：展示服务层代码，定义了还款服务接口（RepaymentService）和实现类（RepaymentServiceImpl）。
画面11：展示服务层代码，设置还款计划对象的借款人ID、项目编号、期数、利息、本金等属性。
画面12：展示服务层代码，调用saveRepaymentPlan方法保存还款计划。
画面13：展示服务层代码，根据还款方式判断是否是等额本息还款。
画面14：展示服务层代码，如果还款方式不是等额本息，则返回-1。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
月利率 = 借款年利率 / 12
每月还款额=借款本金×[1+月利率]^(n-1)×月利率 / [1+月利率]^(n-1) - 1]
第n月还款额 = 本金×月利率×[1+月利率]^(n-1) - 1] / [1+月利率]^(n-1) - 1]

画面2：
Columns (13)
| COLUMN_NAME | DATA_TYPE | NULL | DEFAULT | COMMENT |
|-------------|-----------|------|---------|---------|
| CONSUMER_ID | bigint(20) | NOT NULL | | 借款人用户标识 |
| USER_NO | varchar(50) | NOT NULL | | 借款人用户编码 |
| PROJECT_NO | varchar(120) | NOT NULL | | 借款人项目编号 |
| INTEREST | decimal(17,10) | NOT NULL | | 利息 |
| PRINCIPAL | decimal(17,10) | NOT NULL | | 本金 |
| SHOULD_REPAYMENT_DATE | datetime | NULL | | 应还款日期 |
| REPAYMENT_STATUS | varchar(50) | NOT NULL | | 计划创建状态 |
| CREATE_DATE | datetime | NULL | | 年化利率(平台佣金，利息) |
| COMMISSION | decimal(10,2) | NULL | | 平台佣金 |

画面3：
private BigDecimal amount;
@ApiModelProperty("应还款日期")
private LocalDate shouldRepaymentDate;
@ApiModelProperty("还款状态")
private String repaymentStatus;
@ApiModelProperty("创建时间")
private LocalDateTime createDate;

画面4：
//保存还款计划到数据库
public List<RepaymentPlan> saveRepaymentPlan(ProjectDTO projectDTO,
EqualInterestRepayment fixedRepayment) {

画面5：
List<RepaymentPlan> repaymentPlanList = new ArrayList<>();
//获取每期利息
final Map<Integer, BigDecimal> interestMap = fixedRepayment.getInterestMap();
//平台收取佣金
final Map<Integer, BigDecimal> commissionMap = fixedRepayment.getCommissionMap();
//获取每期本金
fixedRepayment.getPrincipalMap().forEach((k, v) -> {
画面6：
final RepaymentPlan repaymentPlan = new RepaymentPlan();
//新的还款计划
repaymentPlan.setProjectId(projectDTO.getProjectId());
//借款人用户标识
repaymentPlan.setConsumerId(projectDTO.getConsumerId());
//借款人用户编码
repaymentPlan.setProjectNo(projectDTO.getProjectNo());
//期数
repaymentPlan.setNumberOffPeriods(k);
//当前还款利息
repaymentPlan.setInterest(interestMap.get(k));
//还款本金
repaymentPlan.setPrincipal(v);

画面7：
//平台收取佣金
final Map<Integer, BigDecimal> commissionMap = fixedRepayment.getCommissionMap();
//获取每期本金
fixedRepayment.getPrincipalMap().forEach((k, v) -> {
//新的还款计划
final RepaymentPlan repaymentPlan = new RepaymentPlan();
//借款人用户标识
repaymentPlan.setConsumerId(projectDTO.getConsumerId());
//借款人用户编码
repaymentPlan.setProjectNo(projectDTO.getProjectNo());
//期数
repaymentPlan.setNumberOffPeriods(k);
//当前还款利息
repaymentPlan.setInterest(interestMap.get(k));
//还款本金
repaymentPlan.setPrincipal(v);

画面8：
//平台收取佣金
final Map<Integer, BigDecimal> commissionMap = fixedRepayment.getCommissionMap();
//获取每期本金
fixedRepayment.getPrincipalMap().forEach((k, v) -> {
//新的还款计划
final RepaymentPlan repaymentPlan = new RepaymentPlan();
//借款人用户标识
repaymentPlan.setConsumerId(projectDTO.getConsumerId());
//借款人用户编码
repaymentPlan.setProjectNo(projectDTO.getProjectNo());
//期数
repaymentPlan.setNumberOffPeriods(k);
//当前还款利息
repaymentPlan.setInterest(interestMap.get(k));
//还款本金
repaymentPlan.setPrincipal(v);

画面9：
//应还款日期，当前业务等待
repaymentPlan.setShouldRepaymentDate(DateUtil.now());
//计划创建时间
repaymentPlan.setCreateDate("0");
//设置平台佣金
repaymentPlan.setCommission(commissionMap.get(k));
//保存到数据库
planMapper.insert(repaymentPlan);
repaymentPlanList.add(repaymentPlan);

画面10：
package cn.ictast.wanxing2p.repayment.service;
import ...
@Service
@Qualifier("repaymentService")
public class RepaymentServiceImpl implements RepaymentService {

画面11：
//平台收取佣金
final Map<Integer, BigDecimal> commissionMap = fixedRepayment.getCommissionMap();
//获取每期本金
fixedRepayment.getPrincipalMap().forEach((k, v) -> {
//新的还款计划
final RepaymentPlan repaymentPlan = new RepaymentPlan();
//借款人用户标识
repaymentPlan.setConsumerId(projectDTO.getConsumerId());
//借款人用户编码
repaymentPlan.setProjectNo(projectDTO.getProjectNo());
//期数
repaymentPlan.setNumberOffPeriods(k);
//当前还款利息
repaymentPlan.setInterest(interestMap.get(k));
//还款本金
repaymentPlan.setPrincipal(v);

画面12：
//保存还款计划到数据库
public List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);

画面13：
//计算还款的月数
Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
Integer month = ceil.intValue();
//还款方式，只计付等额本息
String repaymentWay = projectDTO.getRepaymentWay();
if (repaymentWay.equals(RepaymentWayCode.FIXED_REPAYMENT.getCode())) {

画面14：
//计算还款的月数
Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
Integer month = ceil.intValue();
//还款方式，只计付等额本息
String repaymentWay = projectDTO.getRepaymentWay();
if (repaymentWay.equals(RepaymentWayCode.FIXED_REPAYMENT.getCode())) {
EqualInterestRepayment fixedRepayment = RepaymentUtil.fixedRepayment(projectDTO.getAmount(), projectDTO.getPeriod());
List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
} else {
return "-1";
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“3.2.5 还款服务启动还款接口(接口④)”，子标题“3.2.5.1 还款方式”。
画面7：PPT标题为“3.2.5 还款服务启动还款接口(接口④)”，子标题“3.2.5.2 功能实现”。
画面13：PPT标题为“3.2.5 还款服务启动还款接口(接口④)”，子标题“3.2.5.5 生还款计划”。
画面14：PPT标题为“3.2.5 还款服务启动还款接口(接口④)”，子标题“3.2.5.6 生成投资人应收明细”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
