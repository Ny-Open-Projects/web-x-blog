# 画面线理解：day14-5-用户还款-第二阶段-功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-5-用户还款-第二阶段-功能实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 02:19, 02:49, 04:39, 05:25, 06:21, 08:38, 09:52, 10:33, 11:14, 12:22, 13:14, 13:41, 14:34, 15:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:15:55

1) 这一组画面整体在讲什么（一句话）：
实现还款服务中，通过 Feign 调用存管代理服务进行预授权交易的业务逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 RepaymentController 中的 @PostMapping("/start-repayment") 方法，用于启动还款流程，接收 ProjectWithTendersDTO 参数。
画面2：展示还款服务与存管代理服务、存管系统的交互流程图，包含多个步骤如“生成还款计划”、“生成交易记录”、“预处理请求”等。
画面3：与画面2相同，为流程图的延续展示。
画面4：展示 RepaymentServiceImpl 中的 executeRepayment 方法，用于执行还款逻辑，调用 saveRepaymentPlan 方法。
画面5：展示 PPT 页面，内容为“4.2 功能实现”，包含 FeignClient 定义的接口 @FeignClient(value = "depository-agent-service") 和在 RepaymentServiceImpl 中实现的 preRepayment 方法。
画面6：与画面2相同，为流程图的延续展示。
画面7：展示 UserAutoPreTransactionRequest 类的定义，包含 @ApiModelProperty 注解的字段如 amount、requestNo、userNo 等。
画面8：展示 RepaymentServiceImpl 中的 preRepayment 方法，用于调用存管代理服务的 userAutoPreTransaction 方法。
画面9：展示 RepaymentServiceImpl 中的 preRepayment 方法，用于构造 UserAutoPreTransactionRequest 对象。
画面10：展示 RepaymentServiceImpl 中的 preRepayment 方法，用于设置请求流水号。
画面11：展示 RepaymentServiceImpl 的类定义，包含 @Service、@Transactional 注解，以及注入的 Mapper 对象。
画面12：展示 RepaymentServiceImpl 中的 startRepayment 方法，用于生成 RepaymentDetail 对象并插入数据库。
画面13：展示 RepaymentServiceImpl 中的 preRepayment 方法，用于调用存管代理服务的 userAutoPreTransaction 方法。
画面14：展示 RepaymentServiceImpl 中的 preRepayment 方法，用于返回调用存管代理服务的结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@ImplicitParam(name = "projectWithTendersDTO", value = "通过i5获取的信息",
        required = true, dataType = "ProjectWithTendersDTO",
        paramType = "body")
@PostMapping("/start-repayment")
public RestResponse<String> startRepayment(@RequestBody ProjectWithTenderDTO projectWithTendersDTO) {
    String result = repaymentService.startRepayment(projectWithTendersDTO);
    return RestResponse.success(result);
}
```

画面4：
```java
@Override
public void executeRepayment(String date) {
    //查询到期的还款计划
    List<RepaymentPlan> repaymentPlanList = selectDueRepayment(date);
    //生成还款明细
    repaymentPlanList.forEach(repaymentPlan -> {
        RepaymentDetail repaymentDetail = saveRepaymentDetail(repaymentPlan);
    });
    //未完待续
}

@Override
public Boolean preRepayment(RepaymentPlan repaymentPlan, String preRequestNo) {
    return null;
}

//保存还款计划到数据库
public String saveRepaymentPlan(ProjectWithTendersDTO projectWithTendersDTO,
        RepaymentPlan repaymentPlan) {
}
```

画面5：
```java
@FeignClient(value = "depository-agent-service")
public interface DepositoryAgentApiAgent {
    @PostMapping("/user-auto-pre-transaction")
    RestResponse<String> userAutoPreTransaction(@RequestBody UserAutoPreTransactionRequest userAutoPreTransactionRequest);
}

@AutoWired
private DepositoryAgentApiAgent depositoryAgentApiAgent;
```

画面7：
```java
public class UserAutoPreTransactionRequest {
    @ApiModelProperty(value = "冻结金额")
    private BigDecimal amount;
    @ApiModelProperty(value = "请求流水号")
    private String requestNo;
    @ApiModelProperty(value = "投资人用户编码")
    private String userNo;
    @ApiModelProperty(value = "预处理业务类型")
    private String bizType;
    @ApiModelProperty(value = "红包金额")
    private BigDecimal preMarketingAmount;
    @ApiModelProperty(value = "备注")
    private String remark;
}
```

画面8：
```java
@Override
public Boolean preRepayment(RepaymentPlan repaymentPlan, String preRequestNo) {
    //1. 请求数据
    final UserAutoPreTransactionRequest userAutoPreTransactionRequest =
            generateUserAutoPreTransactionRequest(repaymentPlan, preRequestNo);
    //2. 请求存管代理服务
    final RestResponse<String> restResponse = depositoryAgentApiAgent
            .userAutoPreTransaction(userAutoPreTransactionRequest);
    //3. 返回结果
    return DepositoryReturnCode.RETURN_CODE_00000.equals(restResponse.getResult());
}
```

画面9：
```java
private UserAutoPreTransactionRequest generateUserAutoPreTransactionRequest(RepaymentPlan repaymentPlan, String preRequestNo) {
    // 构造请求对象
    UserAutoPreTransactionRequest userAutoPreTransactionRequest = new UserAutoPreTransactionRequest();
    // 冻结金额
    userAutoPreTransactionRequest.setAmount(repaymentPlan.getAmount());
    // 预处理业务类型
    userAutoPreTransactionRequest.setBizType(PreprocessBusinessTypeCode.REPAYMENT.getCode());
    // 标的号
    userAutoPreTransactionRequest.setProjectNo(repaymentPlan.getProjectNo());
    // 请求流水号
    userAutoPreTransactionRequest.setRequestNo(preRequestNo);
    // 投资人用户编码
    userAutoPreTransactionRequest.setUserNo(repaymentPlan.getUserNo());
    // 关联业务实体标识
    userAutoPreTransactionRequest.setBidId(repaymentPlan.getId());
    // 返回结果
    return userAutoPreTransactionRequest;
}
```

画面11：
```java
@Service
@RequiredArgsConstructor
public class RepaymentServiceImpl implements RepaymentService {
    @Autowired
    private PlanMapper planMapper;
    @Autowired
    private ReceivablePlanMapper receivablePlanMapper;
    @Autowired
    private RepaymentDetailMapper repaymentDetailMapper;
    @Transactional(rollbackFor = BusinessException.class)
    public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
        //生成借款人还款计划
    }
}
```

画面12：
```java
if (repaymentPlan != null) {
    repaymentDetail = new RepaymentDetail();
    //还款计划标识
    repaymentDetail.setRepaymentPlanId(repaymentPlan.getId());
    //实付金额
    repaymentDetail.setAmount(repaymentPlan.getAmount());
    //实际还款时间
    repaymentDetail.setRepaymentDate(LocalDateTime.now());
    //请求流水号
    repaymentDetail.setRequestNo(CooloUtil.getNo(CodePrefixCode.CODE_REQUEST_PREFIX));
    //未同步
    repaymentDetail.setStatus(StatusCode.STATUS_OUT.getCode());
    //保存详情
    repaymentDetailMapper.insert(repaymentDetail);
}
return repaymentDetail;
```

画面13：
```java
@Override
public Boolean preRepayment(RepaymentPlan repaymentPlan, String preRequestNo) {
    //1. 请求数据
    UserAutoPreTransactionRequest userAutoPreTransactionRequest = generateUserAutoPreTransactionRequest(repaymentPlan, preRequestNo);
    //2. 请求存管代理服务
    RestResponse<String> restResponse = depositoryAgentApiAgent.userAutoPreTransaction(userAutoPreTransactionRequest);
    //3. 返回结果
    return restResponse.getResult().equals(DeputyReturnCode.RETURN_CODE_00000);
}
```

画面14：
```java
@Override
public Boolean preRepayment(RepaymentPlan repaymentPlan, String preRequestNo) {
    //1. 请求数据
    UserAutoPreTransactionRequest userAutoPreTransactionRequest = generateUserAutoPreTransactionRequest(repaymentPlan, preRequestNo);
    //2. 请求存管代理服务
    RestResponse<String> restResponse = depositoryAgentApiAgent.userAutoPreTransaction(userAutoPreTransactionRequest);
    //3. 返回结果
    return restResponse.getResult().equals(DeputyReturnCode.RETURN_CODE_00000);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：PPT 标题为“4.2 功能实现”，内容包含：
- 定义 Feign 代理：@FeignClient(value = "depository-agent-service")
- 在 RepaymentServiceImpl 类中实现 preRepayment 方法。

画面2、3、6：展示还款服务与存管代理服务、存管系统的交互流程图，包含以下步骤：
- 还款服务 → 存管代理服务 → 存管系统
- 步骤1.1：查询到期的还款计划
- 步骤1.2：生成还款计划，状态为“未同步”
- 步骤1.3：生成还款明细，状态为“未同步”
- 步骤1.4：通过存管生成签名及账单
- 步骤1.5：保存交易记录，状态为“未同步”
- 步骤1.6：预处理请求，状态为“处理中”
- 步骤1.7：存管处理成功，状态为“已处理”
- 步骤1.8：更新交易记录，状态为“已同步”
- 步骤1.9：更新交易记录，状态为“已同步”
- 步骤1.10：还款
