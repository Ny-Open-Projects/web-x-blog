# 画面线理解：day11-6-用户投标-功能实现5

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-6-用户投标-功能实现5_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:15, 02:05, 02:38, 03:14, 04:23, 05:05, 06:21, 07:09, 07:31, 08:03, 08:34, 09:41, 10:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:33:55

1) 这一组画面整体在讲什么（一句话）：
演示投标项目创建流程中，前端发起请求后，交易中心服务如何调用用户服务、存管代理服务和存管系统，完成投标信息的保存、冻结资金、更新状态等核心业务逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 ProjectServiceImp.java 中的投标金额校验逻辑，包括最小投资金额、剩余金额和冻结金额的判断，以及对应的异常抛出。
画面2：展示 ProjectServiceImp.java 中的投标金额校验逻辑，包括最小投资金额、剩余金额和冻结金额的判断，以及对应的异常抛出。
画面3：展示 PPT 中的投标信息设置代码，包括设置投标金额、投标人信息、标的编码、状态、创建时间等。
画面4：展示 PPT 中的投标信息设置代码，包括设置投标金额、投标人信息、标的编码、状态、创建时间等。
画面5：展示 ProjectServiceImp.java 中的投标金额校验逻辑，包括最小投资金额、剩余金额和冻结金额的判断，以及对应的异常抛出。
画面6：展示 UserAutoPreTransactionRequest 类的定义，包含冻结金额、请求流水号、投资人用户编码、预处理业务类型、红包金额、备注等字段。
画面7：展示 ProjectServiceImp.java 中的投标信息保存逻辑，包括创建 Tender 对象并设置相关属性。
画面8：展示 DepositoryAgentApiAgent 接口定义，包含 createProject 和 userAutoPreTransaction 两个 REST 接口。
画面9：展示 UserAutoPreTransactionRequest 类的定义，包含冻结金额、请求流水号、投资人用户编码、预处理业务类型、红包金额、备注等字段。
画面10：展示 DepositoryAgentApiAgent 接口定义，包含 createProject 和 userAutoPreTransaction 两个 REST 接口。
画面11：展示 PPT 中的投标信息设置代码，包括设置投标金额、投标人信息、标的编码、状态、创建时间等。
画面12：展示 ProjectServiceImp.java 中的自动预处理请求构造和调用逻辑，包括创建 UserAutoPreTransactionRequest 对象并调用 depositoryAgentApiAgent.userAutoPreTransaction()。
画面13：展示投标流程的时序图，包括用户APP、交易中心、用户服务、存管代理服务、存管系统之间的交互流程。
画面14：展示 ProjectServiceImp.java 中的投标信息保存逻辑，包括创建 Tender 对象并设置相关属性。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//1.3 判断标是否是满标，标的的状态为NULL就表示满标
Project project = getProjectInvestDTO.getTid();
if(project.getProjectStatus().equalsIgnoreCase(anotherString: "FULLY")){
    throw new BusinessException(TransactionErrorCode.E_150114);
}
//1.4 判断投标金额是否达到未投标金额
BigDecimal remainingAmount = getProjectRemainingAmount(project);
if(amount.compareTo(remainingAmount) < 0){
    throw new BusinessException(TransactionErrorCode.E_150114);
}
//1.5 判断此次投标后的剩余金额是否满最小投标金额
//借款人需要信  现在已经投标了 5T  还剩 18900元
//公式：此次投标后剩余金额 - 目前剩余金额 = 本次投标金额
BigDecimal subtract = remainingAmount.subtract(amount);
int result = subtract.compareTo(configService.getTinInvestmentAmount());
if(result() < 0){
    throw new BusinessException(TransactionErrorCode.E_150114);
}
```

画面2：
```java
//2.1 保存投标信息并发送给存管代理服务
//2.2 发送数据给存管代理服务
//2.3 根据结果更新投标状态
else{
    throw new BusinessException(TransactionErrorCode.E_150110);
}
```

画面3：
```java
Final Tender tender = new Tender();
// 投资人投标金额，投标冻结金额
tender.setAmount(amount);
// 投标人用户标识
tender.setConsumerId(restResponse.getResult().getId());
// 投标人用户名
tender.setConsumerUsername(restResponse.getResult().getUsername());
// 投标人用户编码
tender.setUseNo(restResponse.getResult().getUseNo());
// 标的标识
tender.setProjectId(projectInvestDTO.getTid());
// 标的编码
tender.setProjectNo(project.getProjectNO());
// 标的状态
tender.setTenderStatus(TradingCode.FROZEN.getCode());
// 创建时间
tender.setCreateDate(LocalDateTime.now());
// 请求流水号
tender.setRequestNo(CodeOutUtil.getNo(CodePrefixCode.CODE_REQUEST_PREFIX));
// 可用状态
tender.setStatus(0);
// 标的项目名
tender.setProjectName(project.getName());
```

画面4：
```java
Final Tender tender = new Tender();
// 投资人投标金额，投标冻结金额
tender.setAmount(amount);
// 投标人用户标识
tender.setConsumerId(restResponse.getResult().getId());
// 投标人用户名
tender.setConsumerUsername(restResponse.getResult().getUsername());
// 投标人用户编码
tender.setUseNo(restResponse.getResult().getUseNo());
// 标的标识
tender.setProjectId(projectInvestDTO.getTid());
// 标的编码
tender.setProjectNo(project.getProjectNO());
// 标的状态
tender.setTenderStatus(TradingCode.FROZEN.getCode());
// 创建时间
tender.setCreateDate(LocalDateTime.now());
// 请求流水号
tender.setRequestNo(CodeOutUtil.getNo(CodePrefixCode.CODE_REQUEST_PREFIX));
// 可用状态
tender.setStatus(0);
// 标的项目名
tender.setProjectName(project.getName());
```

画面5：
```java
//1.3 判断标是否是满标，标的的状态为NULL就表示满标
Project project = getProjectInvestDTO.getTid();
if(project.getProjectStatus().equalsIgnoreCase(anotherString: "FULLY")){
    throw new BusinessException(TransactionErrorCode.E_150114);
}
//1.4 判断投标金额是否达到未投标金额
BigDecimal remainingAmount = getProjectRemainingAmount(project);
if(amount.compareTo(remainingAmount) < 0){
    throw new BusinessException(TransactionErrorCode.E_150114);
}
//1.5 判断此次投标后的剩余金额是否满最小投标金额
//借款人需要信  现在已经投标了 5T  还剩 18900元
//公式：此次投标后剩余金额 - 目前剩余金额 = 本
```

画面6：
```java
@Model
public class UserAutoPreTransactionRequest {
    @ModelProperty("冻结金额")
    private BigDecimal amount;
    @ModelProperty("请求流水号")
    private String requestNo;
    @ModelProperty("投资人用户编码")
    private String userNo;
    @ModelProperty("预处理业务类型")
    private String bizType;
    @ModelProperty("红包金额")
    private BigDecimal preMarketingAmount;
    @ModelProperty("备注")
    private String remark;
    @ModelProperty("请求流水号")
    private String requestNo;
}
```

画面7：
```java
//2.1 保存投标信息并发送给存管代理服务
final Tender tender = new Tender();
// 投资人用户标识
tender.setConsumerId(restResponse.getResult().getId());
// 投标人用户名
tender.setConsumerUsername(restResponse.getResult().getUsername());
// 投标人用户编码
tender.setUseNo(restResponse.getResult().getUseNo());
// 标的标识
tender.setProjectId(projectInvestDTO.getTid());
// 标的编码
tender.setProjectNo(project.getProjectNO());
// 标的状态
tender.setTenderStatus(TradingCode.FROZEN.getCode());
// 创建时间
tender.setCreateDate(LocalDateTime.now());
// 请求流水号
tender.setRequestNo(CodeOutUtil.getNo(CodePrefixCode.CODE_REQUEST_PREFIX));
// 可用状态
tender.setStatus(0);
// 标的项目名
tender.setProjectName(project.getName());
```

画面8：
```java
@FeignClient(value = "depository-agent-service")
public interface DepositoryAgentApiAgent {
    @PostMapping(value = "/depository-agent/1/createProject")
    public RestResponse<String> createProject(ProjectDTO projectDTO);
}
```

画面9：
```java
@Model
public class UserAutoPreTransactionRequest {
    @ModelProperty("冻结金额")
    private BigDecimal amount;
    @ModelProperty("请求流水号")
    private String requestNo;
    @ModelProperty("投资人用户编码")
    private String userNo;
    @ModelProperty("预处理业务类型")
    private String bizType;
    @ModelProperty("红包金额")
    private BigDecimal preMarketingAmount;
    @ModelProperty("备注")
    private String remark;
    @ModelProperty("请求流水号")
    private String requestNo;
}
```

画面10：
```java
@FeignClient(value = "depository-agent-service")
public interface DepositoryAgentApiAgent {
    @PostMapping(value = "/depository-agent/1/createProject")
    public RestResponse<String> createProject(ProjectDTO projectDTO);
    @PostMapping("/depository-agent/1/user-auto-pre-transaction")
    RestResponse<String> userAutoPreTransaction(UserAutoPreTransactionRequest userAutoPreTransactionRequest);
