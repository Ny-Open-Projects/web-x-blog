# 画面线理解：day12-14-满标放款-接口4-业务层-生成投资人应收明细

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-14-满标放款-接口4-业务层-生成投资人应收明细_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 04:09, 07:18, 08:15, 11:11, 11:46, 12:39, 13:53, 15:01, 16:01, 16:30, 17:17, 18:19, 20:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:55:45

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中实现等额本息还款计划的计算与数据持久化，涉及代码逻辑、数据库表结构及流程图。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 RepaymentServiceImpl.java 文件中计算等额本息还款计划的核心代码。
- 代码逻辑：根据还款方式判断，若为 FIXED_REPAYMENT，则调用 RepaymentUtil.fixedRepayment 方法计算固定还款计划。
- 代码片段：
  ```java
  //1.3 计算还款的月数
  Double ceil = Math.ceil(projectDTO.getProjectPeriod() / 30.0);
  Integer month = ceil.intValue();

  //1.4 还款方式，只针对等额本息
  String repaymentWay = projectDTO.getRepaymentWay();

  if (repaymentWay.equals(RepaymentWayCode.FIXED_REPAYMENT.getCode())) {
      EqualInterestRepayment fixedRepayment = RepaymentUtil.fixedRepayment(projectDTO.getAmount(), projectDTO.getBorrowAnnualRate(), projectDTO.getProjectPeriod(), projectDTO.getTendersDTO().getTenders());
  }
  ```

画面 2：
- 继续展示 if 分支内的代码，调用 RepaymentUtil.fixedRepayment 方法。
- 代码片段：
  ```java
  EqualInterestRepayment fixedRepayment = RepaymentUtil.fixedRepayment(projectDTO.getAmount(), projectDTO.getBorrowAnnualRate(), projectDTO.getProjectPeriod(), projectDTO.getTendersDTO().getTenders());
  ```

画面 3：
- 展示 TenderDTO.java 文件中与还款计划相关的字段定义。
- 代码片段：
  ```java
  //标的期限(单位:天) -- 允许字段
  private Integer projectPeriod;

  //年化利率(投资年利率) -- 允许字段
  private BigDecimal projectAnnualRate;

  //标的
  private ProjectDTO project;

  //预期收益
  private BigDecimal expectedIncome
  ```

画面 4：
- 展示 RepaymentServiceImpl.java 文件中，将计算好的还款计划保存到数据库的代码。
- 代码片段：
  ```java
  //1.8 保存还款计划
  List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
  ```

画面 5：
- 展示 PPT 页面，内容为“2.1.2 收款计划”下的“2.1.2.2 收款计划”部分。
- PPT 结构：
  - 2.1.2 收款计划
    - 2.1.2.1 收款计划
    - 2.1.2.2 收款计划
      - 2.1.2.2.1 收款计划
      - 2.1.2.2.2 收款计划
      - 2.1.2.2.3 收款计划
      - 2.1.2.2.4 收款计划
      - 2.1.2.2.5 收款计划
      - 2.1.2.2.6 收款计划

画面 6：
- 展示数据库表 pyp_repayment 的结构。
- 表结构：
  - Columns (13):
    - ID
    - CONTRACT_ID
    - USER_NO
    - TENDER_ID
    - AMOUNT
    - INTEREST
    - PRINCIPAL
    - RECEIVABLE_STATUS
    - CREATE_DATE
    - COMMISSION
    - NUMBER_OF_PERIODS
    - REPAYMENT_PLAN_ID
    - REPAYMENT_PLAN
  - Indexes (1):
    - IDX_REPAYMENT_PLAN

画面 7：
- 展示 RepaymentServiceImpl.java 文件中，保存还款计划到数据库的代码。
- 代码片段：
  ```java
  public List<RepaymentPlan> saveRepaymentPlan(ProjectDTO projectDTO, EqualInterestRepayment fixedRepayment) {
      List<RepaymentPlan> repaymentPlanList = new ArrayList<>();
      final Map<Integer, BigDecimal> interestMap = new HashMap<>();
      final Map<Integer, BigDecimal> principalMap = new HashMap<>();
      final Map<Integer, BigDecimal> commissionMap = new HashMap<>();
  }
  ```

画面 8：
- 展示数据库表 pyp_repayment 的结构。
- 表结构：
  - Columns (13):
    - ID
    - CONTRACT_ID
    - USER_NO
    - TENDER_ID
    - AMOUNT
    - INTEREST
    - PRINCIPAL
    - RECEIVABLE_STATUS
    - CREATE_DATE
    - COMMISSION
    - NUMBER_OF_PERIODS
    - REPAYMENT_PLAN_ID
    - REPAYMENT_PLAN
  - Indexes (1):
    - IDX_REPAYMENT_PLAN

画面 9：
- 展示 RepaymentServiceImpl.java 文件中，设置还款计划的详细信息。
- 代码片段：
  ```java
  //设置还款计划
  repaymentPlan.setNumberPeriods(repaymentPlan.getNumberPeriods());
  //设置还款计划
  repaymentPlan.setTenderId(tender.getId());
  //设置还款计划
  repaymentPlan.setConsumerId(tender.getConsumerId());
  //设置还款计划
  repaymentPlan.setTenderNo(tender.getTenderNo());
  //设置还款计划
  repaymentPlan.setRepaymentId(repaymentPlan.getId());
  //设置还款计划
  repaymentPlan.setInterest(interestMap.get(repaymentPlan.getNumberPeriods()));
  //设置还款计划
  repaymentPlan.setPrincipal(principalMap.get(repaymentPlan.getNumberPeriods()));
  //设置还款计划
  repaymentPlan.setAmount(repaymentPlan.getInterest().add(repaymentPlan.getPrincipal()));
  ```

画面 10：
- 展示 RepaymentServiceImpl.java 文件中，定义了 RepaymentService 接口的实现类。
- 代码片段：
  ```java
  public class RepaymentServiceImpl implements RepaymentService {
      @Autowired
      private PlanMapper planMapper;
      @Autowired
      private ReceiptMapper receiptMapper;
      @Autowired
      private RepaymentDetailMapper repaymentDetailMapper;
      @Autowired
      private RepaymentPlanMapper repaymentPlanMapper;
      @Autowired
      private RepaymentTaskMapper repaymentTaskMapper;
      @Autowired
      private RepaymentDetailService repaymentDetailService;
      @Autowired
      private RepaymentPlanService repaymentPlanService;
      @Autowired
      private RepaymentTaskService repaymentTaskService;
      @Autowired
      private RepaymentService repaymentService;
  }
  ```

画面 11：
- 展示 RepaymentServiceImpl.java 文件中，调用 saveRepaymentPlan 方法保存还款计划。
- 代码片段：
  ```java
  List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
  ```

画面 12：
- 展示 RepaymentServiceImpl.java 文件中，设置还款计划的详细信息。
- 代码片段：
  ```java
  //设置还款计划
  repaymentPlan.setNumberPeriods(repaymentPlan.getNumberPeriods());
  //设置还款计划
  repaymentPlan.setTenderId(tender.getId());
  //设置还款计划
  repaymentPlan.setConsumerId(tender.getConsumerId());
  //设置还款计划
  repaymentPlan.setTenderNo(tender.getTenderNo());
  //设置还款计划
  repaymentPlan.setRepaymentId(repaymentPlan.getId());
  //设置还款计划
  repaymentPlan.setInterest(interestMap.get(repaymentPlan.getNumberPeriods()));
  //设置还款计划
  repaymentPlan.setPrincipal(principalMap.get(repaymentPlan.getNumberPeriods()));
  //设置还款计划
  repaymentPlan.setAmount(repaymentPlan.getInterest().add(repaymentPlan.getPrincipal()));
  ```

画面 13：
- 展示 RepaymentServiceImpl.java 文件中，保存还款计划到数据库的代码。
- 代码片段：
  ```java
  public List<RepaymentPlan> saveRepaymentPlan(ProjectDTO projectDTO, EqualInterestRepayment fixedRepayment) {
      List<RepaymentPlan> repaymentPlanList = new ArrayList<>();
      final Map<Integer, BigDecimal> interestMap = new HashMap<>();
      final Map<Integer, BigDecimal> principalMap = new HashMap<>();
      final Map<Integer, BigDecimal> commissionMap = new HashMap<>();
  }
  ```

画面 14：
- 展示还款计划流程图。
- 流程图结构：
  - 起始节点：还款计划
  - 节点1：生成还款计划
  - 节点2：保存还款计划
  - 节点3：生成投资人的应收明细
  - 节点4：根据投标信息生成应收明细
  - 节点5：保存应收明细到数据库
  - 节点6：返回成功
  - 节点7：失败
  - 节点8：返回失败
  - 节点9：结束
  - 节点10：还款计划
  - 节点11：生成还款计划
  - 节点12：保存还款计划
  - 节点13：生成投资人的应收明细
  - 节点14：根据投标信息生成应收明细
  - 节点15：保存应收明细到数据库
  - 节点16：返回成功
  - 节点17：失败
  -
