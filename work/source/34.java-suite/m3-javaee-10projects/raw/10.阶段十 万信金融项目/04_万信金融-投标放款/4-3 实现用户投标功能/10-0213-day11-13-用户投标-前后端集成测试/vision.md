# 画面线理解：day11-13-用户投标-前后端集成测试

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-13-用户投标-前后端集成测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:00, 02:03, 05:20, 06:06, 07:49, 08:55, 09:36, 10:21, 11:27, 11:46, 13:52, 14:54, 15:19, 16:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:39:49

1) 这一组画面整体在讲一个用户投标功能的完整流程，包括前端页面交互、后端服务逻辑、数据库操作及配置中心的联动。

2) 按时间顺序列出每张画面的要点：
画面1：展示“用户投标业务测试.txt”文档，内容为“启动清单”和“测试清单”，包括“1. 删库工程”、“2. Apollo”、“3. 业务微服务工程”、“4. 银行存管系统”、“5. redis”、“6. ES”等启动项，以及“1. 投标已经开户的账户登录，并充值”、“2. 投标金额小于最小投标金额”等测试项。
画面2：展示一个“P2P平台”的系统架构图，包含“浏览器/APP”、“交易中心”、“用户服务”、“存管代理服务”、“存管系统”五个模块，通过箭头表示交互流程，例如“浏览器/APP”指向“交易中心”，“交易中心”指向“用户服务”等。
画面3：展示“用户投标业务测试.txt”文档，内容为空白。
画面4：展示浏览器页面，显示“出市详情”页面，包含“用户投标信息”和“金额”等字段，右侧为浏览器开发者工具的“Network”标签页。
画面5：展示浏览器页面，显示“出市详情”页面，金额为“5000 元”，下方有“选择出市”按钮，右侧为浏览器开发者工具的“Network”标签页。
画面6：展示数据库管理工具，显示“p2p_transaction_1”表的数据，包含“CUSTOMER_ID”、“USER_ID”、“PROJECT_ID”、“AMOUNT”、“TENDER_STATUS”等字段。
画面7：展示数据库管理工具，显示“p2p_depository_agent”表的数据，包含“REQUEST_ID”、“REQUEST_TYPE”、“OBJECT_TYPE”、“CREATE_DATE”等字段。
画面8：展示浏览器页面，显示“出市详情”页面，金额为“450 元”，下方有“选择出市”按钮，右侧为浏览器开发者工具的“Network”标签页。
画面9：展示IDE中的Java代码，包含“ProjectServiceImp.java”文件内容，其中包含“// 2. 判断标的是否满标，标的为满标则表示满标”和“// 4. 判断投标金额是否超过最小投标金额”等注释，以及SQL语句“SELECT IFNULL(SUM(AMOUNT), 0) AS total FROM p2p_transaction_1”。
画面10：展示IDE中的Java代码，包含“ProjectServiceImp.java”文件内容，其中包含“// 3. 判断标的是否满标，标的为满标则表示满标”和“// 4. 判断投标金额是否超过最小投标金额”等注释，以及SQL语句“SELECT ID, CONSUMER_ID, US...”。
画面11：展示IDE中的Java代码，包含“ProjectServiceImp.java”文件内容，其中包含“BigDecimal remainingAmount = getProjectRemainingAmount(project);”和“if (amount.compareTo(remainingAmount) > 0) { throw new BusinessException(TransactionErrorCode.E_150111); }”等代码，其中“throw new BusinessException(TransactionErrorCode.E_150111);”被高亮。
画面12：展示IDE中的Java代码，包含“ProjectServiceImp.java”文件内容，其中包含“BigDecimal remainingAmount = getProjectRemainingAmount(project);”和“if (amount.compareTo(remainingAmount) > 0) { throw new BusinessException(TransactionErrorCode.E_150111); }”等代码，其中“throw new BusinessException(TransactionErrorCode.E_150111);”被高亮，同时“Console”标签页显示“Load config failed, will retry in 1 SECONDS...”。
画面13：展示浏览器页面，显示“确认出市”页面，包含“出市金额：450”、“账户余额：5450”、“剩余支付：450元”等信息，下方有“确认出市”按钮，右侧为浏览器开发者工具的“Network”标签页。
画面14：展示IDE中的Java代码，包含“ProjectServiceImp.java”文件内容，其中包含“BigDecimal remainingAmount = getProjectRemainingAmount(project);”和“if (amount.compareTo(remainingAmount) > 0) { throw new BusinessException(TransactionErrorCode.E_150111); }”等代码，其中“throw new BusinessException(TransactionErrorCode.E_150111);”被高亮，同时“Console”标签页显示“Load config failed, will retry in 1 SECONDS...”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面9：
```java
// 2. 判断标的是否满标，标的为满标则表示满标
Project project = getByBid(ProjectInvestDTO.getCaseId());
if (project.getProjectStatus().equalsIgnoreCase(ProjectCode.FULLY.getCode())) {
    throw new BusinessException(TransactionErrorCode.E_150101);
}
// 4. 判断投标金额是否超过最小投标金额
BigDecimal remainingAmount = getProjectRemainingAmount(project);
if (amount.compareTo(remainingAmount) > 0) {
    throw new BusinessException(TransactionErrorCode.E_150111);
}
```
画面10：
```java
// 3. 判断标的是否满标，标的为满标则表示满标
Project project = getByBid(ProjectInvestDTO.getCaseId());
if (project.getProjectStatus().equalsIgnoreCase(ProjectCode.FULLY.getCode())) {
    throw new BusinessException(TransactionErrorCode.E_150101);
}
// 4. 判断投标金额是否超过最小投标金额
BigDecimal remainingAmount = getProjectRemainingAmount(project);
if (amount.compareTo(remainingAmount) > 0) {
    throw new BusinessException(TransactionErrorCode.E_150111);
}
```
画面11：
```java
BigDecimal remainingAmount = getProjectRemainingAmount(project);
if (amount.compareTo(remainingAmount) > 0) {
    throw new BusinessException(TransactionErrorCode.E_150111);
}
```
画面12：
```java
BigDecimal remainingAmount = getProjectRemainingAmount(project);
if (amount.compareTo(remainingAmount) > 0) {
    throw new BusinessException(TransactionErrorCode.E_150111);
}
```
画面14：
```java
BigDecimal remainingAmount = getProjectRemainingAmount(project);
if (amount.compareTo(remainingAmount) > 0) {
    throw new BusinessException(TransactionErrorCode.E_150111);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：架构图包含“浏览器/APP”、“交易中心”、“用户服务”、“存管代理服务”、“存管系统”五个模块，通过箭头表示交互流程，例如“浏览器/APP”指向“交易中心”，“交易中心”指向“用户服务”等。

5) 不要评价画面美观，不要输出与课程无关的内容。
