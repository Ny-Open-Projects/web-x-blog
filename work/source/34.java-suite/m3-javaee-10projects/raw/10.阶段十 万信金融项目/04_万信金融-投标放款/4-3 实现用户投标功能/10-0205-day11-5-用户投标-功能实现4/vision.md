# 画面线理解：day11-5-用户投标-功能实现4

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-5-用户投标-功能实现4_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:47, 01:09, 02:43, 06:05, 07:34, 07:55, 08:56, 09:59, 10:52, 12:03, 14:46, 16:11, 17:03, 17:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:33:00

1) 这一组画面整体在讲什么（一句话）：
演示在 Java 项目中如何实现投资标的校验逻辑，包括金额最小投资限制、用户余额校验、标的是否满标等业务判断，并展示相关代码和配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 ProjectServiceImpl.java 中判断投资金额是否大于最小投标金额的代码，调用 configService 获取最小投资金额，并抛出 BusinessException。
画面2：展示用户投资的业务流程图，包含“调用端/APP”、“交易中心”、“用户服务”、“存管代理服务”、“存管系统”等模块，以及各模块间的调用关系。
画面3：展示数据库表结构，表名为 yz_transaction_1，包含字段如 ID、PROJECT_ID、STATUS、CREATE_TIME 等，以及索引信息。
画面4：展示 ProjectServiceImpl.java 中判断用户账户余额是否足够，调用 consumerApiAgent 获取余额，并与投资金额比较。
画面5：展示 ProjectServiceImpl.java 中判断标的是否满标，通过 projectInvestDTO 获取项目状态，若为“FULLY”则抛出异常。
画面6：展示 ProjectInvestDTO 类的成员方法，包括 getId()、getAmount()、setAmount() 等。
画面7：展示 ProjectServiceImpl.java 中判断标的是否满标，使用 project.getProjectStatus() 获取状态并判断。
画面8：展示 ProjectServiceImpl.java 中判断标的是否满标，使用 project.getProjectStatus() 获取状态并判断。
画面9：展示 ProjectServiceImpl.java 中获取剩余金额，调用 project.getProjectRemainingAmount()。
画面10：展示 ProjectServiceImpl.java 中判断剩余金额是否满足最小投标金额，使用 BigDecimal.compareTo() 方法。
画面11：展示 ProjectServiceImpl.java 中使用 BigDecimal 的 subtract 方法计算剩余金额。
画面12：展示 ProjectServiceImpl.java 中使用 BigDecimal 的 subtract 方法计算剩余金额。
画面13：展示 ProjectServiceImpl.java 中使用 TransactionErrorCode 枚举类，抛出 BusinessException。
画面14：展示 ProjectServiceImpl.java 中判断剩余金额是否满足最小投标金额，使用 BigDecimal.compareTo() 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//1 判断投标金额是否大于最小投标金额
BigDecimal amount=new BigDecimal(projectInvestDTO.getAmount());
BigDecimal minInvestmentAmount=configService.getMiniInvestmentAmount();
if(amount.compareTo(minInvestmentAmount) < 0) {
    throw new BusinessException(TransactionErrorCode.E_150109);
}
```

画面4：
```java
//1.2 判断用户账户余额是否足够
LoginInfo user=SecurityUtil.getUser();
RestResponse<ConsumerDTO> restResponse=consumerApiAgent.getOurConsumer(user.getMobile());
RestResponse<BalanceDetailDTO> balanceDetailDTO=restResponse.getBalance(restResponse.getResult());
BigDecimal myBalance=balanceDetailDTO.getBalance();
if(myBalance.compareTo(amount) < 0) {
    throw new BusinessException(TransactionErrorCode.E_150112);
}
```

画面5：
```java
//1.3 判断标的是否满标，标的的状态为FULLY表示满标
Project project = projectInvestDTO.getIO();
if(project.getProjectStatus().equalsIgnoreCase("FULLY")) {
    throw new BusinessException(TransactionErrorCode.E_150114);
}
```

画面9：
```java
//1.4 判断投标金额是否达到剩余金额
BigDecimal remainingAmount = project.getProjectRemainingAmount(project);
```

画面10：
```java
//1.5 判断此次投标后的剩余金额是否满足最小投标金额
BigDecimal subtractRemainingAmount = remainingAmount.subtract(amount);
if(amount.compareTo(remainingAmount) < 0) {
    throw new BusinessException(TransactionErrorCode.E_150111);
}
```

画面11：
```java
BigDecimal subtract = remainingAmount.subtract(amount);
```

画面13：
```java
//1.5 判断此次投标后的剩余金额是否满足最小投标金额
BigDecimal subtractRemainingAmount = remainingAmount.subtract(amount);
int result = subtract.compareTo(configService.getMiniInvestmentAmount());
if(result < 0) {
    throw new BusinessException(TransactionErrorCode.E_150111);
}
```

画面14：
```java
//1.4 判断投标金额是否达到剩余金额
BigDecimal remainingAmount = project.getProjectRemainingAmount(project);
if(amount.compareTo(remainingAmount) < 0) {
    throw new BusinessException(TransactionErrorCode.E_150111);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：流程图标题为“用户投资业务流程图”，包含以下模块和调用关系：
- “调用端/APP” → “交易中心” → “用户服务” → “存管代理服务” → “存管系统”
- “调用端/APP” → “交易中心” → “存管系统”
- “用户服务” → “存管代理服务”
- “存管代理服务” → “存管系统”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
