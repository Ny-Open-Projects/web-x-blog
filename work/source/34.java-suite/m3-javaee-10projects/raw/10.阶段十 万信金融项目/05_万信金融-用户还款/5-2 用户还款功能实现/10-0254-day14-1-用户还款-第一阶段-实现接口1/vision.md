# 画面线理解：day14-1-用户还款-第一阶段-实现接口1

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-1-用户还款-第一阶段-实现接口1_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:24, 00:31, 02:08, 02:12, 02:29, 02:32, 03:58, 05:44, 05:56, 06:23, 06:32, 06:34, 06:37, 06:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:13:01

1) 这一组画面整体在讲什么（一句话）：
演示如何在还款服务中，通过 MyBatis Mapper 接口定义查询到期还款计划的方法，并在 Service 层实现该功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 RepaymentDetail 实体类，包含 @TableField 注解定义的字段：repaymentPlanId, amount, repaymentDate。
画面 2: 展示 PlanMapper 接口，定义了 selectDueRepayment 方法。
画面 3: 展示 PlanMapper.java 文件，光标位于方法定义处，提示用户按 Ctrl+Shift+Alt+Enter 可以自动补全。
画面 4: 展示 PlanMapper.java 文件，光标位于方法定义处，提示用户按 Ctrl+Shift+Alt+Enter 可以自动补全。
画面 5: 展示数据库表 repayment_detail 的结构，包含 ID, REPAYMENT_PLAN_ID, AMOUNT, REPAYMENT_DATE, REQUEST_ID, STATUS 等字段。
画面 6: 展示数据库表 repayment_plan 的结构，包含 ID, CONSUMER_ID, PROJECT_ID 等字段。
画面 7: 展示 PlanMapper.java 文件，光标位于方法定义处，提示用户按 Ctrl+Shift+Alt+Enter 可以自动补全。
画面 8: 展示 PPT 页面，标题为“3.2 功能实现”，子标题“3.2.1 还款服务查询到期还款计划接口(接口①)”，内容包括：
    1. 实现数据访问层，在 PlanMapper 接口内定义 selectDueRepayment 方法：
        /* 查询所有到期的还款计划
        @return
        @Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, '%Y-%m-%d') = #{date} " +
        "AND REPAYMENT_STATUS = '0'")
        List<RepaymentPlan> selectDueRepayment(String date);
    2. 在业务层 RepaymentServiceImpl 类中调用 mapper 实现查询功能：
        @Override
        public List<RepaymentPlan> selectDueRepayment(String date) {
            return repaymentMapper.selectDueRepayment(date);
        }
画面 9: 展示 PlanMapper.java 文件，光标位于方法定义处，提示用户按 Ctrl+Shift+Alt+Enter 可以自动补全。
画面 10: 展示 RepaymentServiceImpl.java 文件，光标位于类定义处，提示用户按 Ctrl+Shift+Alt+Enter 可以自动补全。
画面 11: 展示 RepaymentServiceImpl.java 文件，光标位于类定义处，提示用户按 Ctrl+Shift+Alt+Enter 可以自动补全。
画面 12: 展示 RepaymentServiceImpl.java 文件，光标位于类定义处，提示用户按 Ctrl+Shift+Alt+Enter 可以自动补全。
画面 13: 展示 RepaymentServiceImpl.java 文件，光标位于类定义处，提示用户按 Ctrl+Shift+Alt+Enter 可以自动补全。
画面 14: 展示 RepaymentServiceImpl.java 文件，光标位于类定义处，提示用户按 Ctrl+Shift+Alt+Enter 可以自动补全。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
//还款计划标识
@TableField("REPAYMENT_PLAN_ID")
private Long repaymentPlanId;

//实收金额
@TableField("AMOUNT")
private BigDecimal amount;

//实际还款时间
@TableField("REPAYMENT_DATE")
private LocalDateTime repaymentDate;

//连接用户资金流水号（用于解析会计凭证）
//有借据、行营不支持单次“确定还款”，合并多个凭证处理的账务、折中做法。
```

画面 2:
```java
package cn.ictast.wanxingzp.repayment.mapper;

import ...

/**
 * 借款人还款计划 Mapper 接口
 */
public interface PlanMapper extends BaseMapper<RepaymentPlan> {
}
```

画面 3:
```java
import ...

/**
 * 借款人还款计划 Mapper 接口
 */
public interface PlanMapper extends BaseMapper<RepaymentPlan> {
    @Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, '%Y-%m-%d') = #{date} " +
            "AND REPAYMENT_STATUS = '0'")
    List<RepaymentPlan> selectDueRepayment(String date);
}
```

画面 4:
```java
import ...

/**
 * 借款人还款计划 Mapper 接口
 */
public interface PlanMapper extends BaseMapper<RepaymentPlan> {
    @Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, '%Y-%m-%d') = #{date} " +
            "AND REPAYMENT_STATUS = '0'")
    List<RepaymentPlan> selectDueRepayment(String date);
}
```

画面 5:
```sql
Columns (6)
Field          Type          Comment
ID             bigint(20)     主键
REPAYMENT_PLAN_ID bigint(20)     还款计划ID
AMOUNT         decimal(10,2)     金额
REPAYMENT_DATE datetime     实际还款时间
REQUEST_ID     varchar(50)     请求流水号
STATUS         tinyint(4)     可用状态
```

画面 6:
```sql
Columns (13)
Field          Type          Comment
ID             bigint(20)     主键
CONSUMER_ID    bigint(20)     借款人用户标识
PROJECT_ID     bigint(20)     项目标识
```

画面 7:
```java
import ...

/**
 * 借款人还款计划 Mapper 接口
 */
public interface PlanMapper extends BaseMapper<RepaymentPlan> {
    @Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, '%Y-%m-%d') = #{date} " +
            "AND REPAYMENT_STATUS = '0'")
    List<RepaymentPlan> selectDueRepayment(String date);
}
```

画面 8:
```java
/* 查询所有到期的还款计划
@return
@Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, '%Y-%m-%d') = #{date} " +
"AND REPAYMENT_STATUS = '0'")
List<RepaymentPlan> selectDueRepayment(String date);
```

画面 9:
```java
import ...

/**
 * 借款人还款计划 Mapper 接口
 */
public interface PlanMapper extends BaseMapper<RepaymentPlan> {
    @Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, '%Y-%m-%d') = #{date} " +
            "AND REPAYMENT_STATUS = '0'")
    List<RepaymentPlan> selectDueRepayment(String date);
}
```

画面 10:
```java
package cn.ictast.wanxingzp.repayment.service;

import ...

@Service
@Mapper
public class RepaymentServiceImpl implements RepaymentService {
    @Autowired
    private PlanMapper planMapper;
    @Autowired
    private ReceivablePlanMapper receivablePlanMapper;
    @Override
    @Transactional(rollbackFor = BusinessReception.class)
    public String startRepayment(ProjectWithTenderDTO projectWithTenderDTO) {
        ProjectDTO projectDTO = projectWithTenderDTO.getProject();
        return null;
    }
}
```

画面 11:
```java
package cn.ictast.wanxingzp.repayment.service;

import ...

@Service
@Mapper
public class RepaymentServiceImpl implements RepaymentService {
    @Autowired
    private PlanMapper planMapper;
    @Autowired
    private ReceivablePlanMapper receivablePlanMapper;
    @Override
    @Transactional(rollbackFor = BusinessReception.class)
    public String startRepayment(ProjectWithTenderDTO projectWithTenderDTO) {
        ProjectDTO projectDTO = projectWithTenderDTO.getProject();
        return null;
    }
}
```

画面 12:
```java
//封装投资人应收明细
ReceivablePlan receivablePlan = new ReceivablePlan();
//快照信息标识
receivablePlan.setTenderId(tender.getId());
//设置期数
receivablePlan.setNumberPeriods(repaymentPlan.getNumberOfPeriods());
//投资人用户编号
receivablePlan.setConsumerId(consumer.getId());
//投资人用户编号
receivablePlan.setUserId(consumer.getId());
//还款计划标识
receivablePlan.setRepaymentPlanId(repaymentPlan.getId());
//应收利息
receivablePlan.setInterest(repaymentPlan.getInterest());
//应收本金
receivablePlan.setPrincipal(repaymentPlan.getPrincipal());
//应收本金 - 应收利息 - 应收利息
receivablePlan.setAmount(repaymentPlan.getInterest().add(receivablePlan.getPrincipal()));
```

画面 13:
```java
@Override
public List<RepaymentPlan> selectDueRepayment(String date) {
    return planMapper.selectDueRepayment(date);
}
@Override
public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) {
    return null;
}
//保存还款计划到库
public List<RepaymentPlan> saveRepaymentPlan(ProjectDTO projectDTO,
        EqualInterestRepayment fixedRepayment) {
    List<
