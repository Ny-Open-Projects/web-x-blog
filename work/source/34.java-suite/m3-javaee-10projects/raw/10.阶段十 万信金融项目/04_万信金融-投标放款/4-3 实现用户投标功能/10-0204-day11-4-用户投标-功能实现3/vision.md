# 画面线理解：day11-4-用户投标-功能实现3

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-4-用户投标-功能实现3_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:33, 01:49, 03:10, 03:35, 03:52, 05:28, 06:03, 06:46, 07:38, 08:45, 09:23, 10:04, 12:21, 13:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:32:23

1) 这一组画面整体在讲什么（一句话）：
实现投资标创建前的最小投资金额校验和用户余额校验逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构和代码，说明A：检查Apollo是否配置最小投标金额（配置项为mini.investment.amount=100.0），B：实现查询用户余额功能，C：在ConsumerController中实现该方法。
画面2：展示代码中判断投标金额是否大于最小投标金额的逻辑，以及用户余额查询的逻辑。
画面3：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面4：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面5：展示ConfigService类中获取最小投资金额的配置方法，从Apollo配置文件读取。
画面6：展示代码中抛出BusinessException异常的逻辑。
画面7：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面8：展示代码中判断用户余额是否足够，如果不足则抛出异常。
画面9：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面10：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面11：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面12：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面13：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面14：展示代码中判断用户余额是否足够，如果不足则抛出异常。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
A: 检查Apollo是否配置最小投标金额
已配置 mini.investment.amount 100.0
最小投标金额
B: 实现查询用户余额功能，在ConsumerAPI接口中新增查询当前余额的方法：
/**
获取当前应用用户余额信息
@param userNo 用户编码
@return
*/
RestResponse<BalanceDetailsDTO> getBalance(String userNo);
C: 在ConsumerController类中实现该方法：
@Override
@ApiOperation("获取用户可用余额")
@ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "string")
@GetMapping("/1/balances/{userNo}")
public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable string userNo) {
return balanceFromDepository;
}
画面2：
@Override
public TenderDTO createTender(ProjectInvestDTO projectInvestDTO) {
//前置条件判断
//1.判断投标金额是否大于最小投标金额
BigDecimal amount = new BigDecimal(projectInvestDTO.getAmout());
BigDecimal miniInvestmentAmount = configService.getMiniInvestmentAmount();
if (amount.compareTo(miniInvestmentAmount) < 0) {
throw new BusinessException(TransactionErrorCode.E_150109);
}
//2.判断用户账户余额是否足够
画面3：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面4：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面5：
public BigDecimal getAnnualRate() {
return getBorrowerAnnualRate().subtract(getCommissionAnnualRate());
}
//最小投标金额
public BigDecimal getMiniInvestmentAmount() {
//如配置文件中没有就默认，这些项目都配置 100.0，可以使用配置文件的
return BigDecimal.valueOf(config.getProperty("key:mini.investment.amount", "100.0"));
}
画面6：
if (amount.compareTo(miniInvestmentAmount) < 0) {
throw new BusinessException(TransactionErrorCode.E_150109);
}
画面7：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面8：
//投资者要投的金额 string -> BigDecimal
BigDecimal amount = new BigDecimal(projectInvestDTO.getAmout());
//判断金额是否符合最小投标
final BigDecimal miniInvestmentAmount = configService.getMiniInvestmentAmount();
//业务判断
if (amount.compareTo(miniInvestmentAmount) < 0) {
log_warn("投标金额小于最小投标");
throw new BusinessException(TransactionErrorCode.E_150109);
}
画面9：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面10：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面11：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面12：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面13：
if (amount.compareTo(miniInvestmentAmount) < 0) {
throw new BusinessException(TransactionErrorCode.E_150109);
}
画面14：
if (amount.compareTo(miniInvestmentAmount) < 0) {
throw new BusinessException(TransactionErrorCode.E_150109);
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“2.2 实现前置条件判断”，内容包括：
- 投资者要投的金额 string -> BigDecimal
- 判断金额是否符合最小投标
- 获取最小投标金额
- 业务判断
- 如果金额小于最小投标，抛出异常
画面8：PPT标题为“2.2 实现前置条件判断”，内容包括：
- 投资者要投的金额 string -> BigDecimal
- 判断金额是否符合最小投标
- 获取最小投标金额
- 业务判断
- 如果金额小于最小投标，抛出异常
画面14：PPT标题为“2.2 实现前置条件判断”，内容包括：
- 投资者要投的金额 string -> BigDecimal
- 判断金额是否符合最小投标
- 获取最小投标金额
- 业务判断
- 如果金额小于最小投标，抛出异常

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
