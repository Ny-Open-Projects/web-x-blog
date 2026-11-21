# 画面线理解：day12-12-满标放款-接口4-业务层-生成还款计划

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-12-满标放款-接口4-业务层-生成还款计划_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:43, 01:14, 01:38, 01:48, 02:13, 02:38, 02:49, 03:11, 03:25, 04:25, 05:05, 05:30, 05:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:53:50

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中实现等额本息还款计划的计算逻辑，包括获取项目信息、计算月数、调用工具类生成还款计划并保存。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 代码文件：`RepaymentServiceImpl.java`
- 代码内容：
```java
//1.1 获取借款人还款计划
ProjectDTO projectDTO = projectWithTendersDTO.getProject();
//1.2 获取投标信息
List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
//1.3 计算还款的月数
Double ceil = Math.ceil(projectDTO.getPeriod()/30.0);
Integer month = ceil.intValue();
//1.4 还款方式，只针对等额本息
String repaymentWay = projectDTO.getRepaymentWay();
//1.5 生成还款计划
//1.6 生成投资人应收明细
```

画面 2：
- 代码文件：`RepaymentServiceImpl.java`（部分代码）
- 代码内容：
```java
// 平台收益利息
final Map<Integer, BigDecimal> commissionMap = receipt.getCommissionMap();
// 对应上
planList.forEach(plan -> {
    // 按投资人收佣规则存到数据库
    saveReceivablePlan(plan, tender, principalMap, interestMap, commissionMap);
});
}
else {
    // 其他还款方式，暂不处理
    return "-1";
}
return "00000";
```

画面 3：
- 代码文件：`RepaymentUtil.java`
- 代码内容：
```java
/**
 * 等额本息计算还款方式为等额本金和利息
 * 公式：每月还款本金 = (贷款本金 / 还款月数) + (贷款本金 - 已还本金) * 月利率 / 12
 * 公式：每月应还利息 = (贷款本金 - 已还本金) * 月利率 / 12
 * @param invest 总借款额（贷款本金）
 * @param monthRate 月利率
 * @param month 还款月数
 * @return 每月还款本金明细
 */
private static BigDecimal getRepaymentAmount(BigDecimal invest, Double monthRate, int month) {
    return invest.multiply(new BigDecimal(monthRate)).divide(new BigDecimal(12), 2, BigDecimal.ROUND_DOWN);
}
```

画面 4：
- 代码文件：`RepaymentUtil.java`
- 代码内容：
```java
private static Map<Integer, BigDecimal> getCapitalAmountList(BigDecimal invest, double monthRate, int month) {
    Map<Integer, BigDecimal> map = new HashMap<>();
    double monthPri = getCapitalPrincipal(invest, month, monthRate);
    for (int i = 1; i <= month; i++) {
        BigDecimal monthRes = new BigDecimal(val + (invest.doubleValue() - monthPri * (i - 1)) * monthRate / 12);
        map.put(i, monthRes);
    }
    return map;
}
```

画面 5：
- 代码文件：`RepaymentUtil.java`
- 代码内容：
```java
/**
 * 等额本金计算还款方式为等额本金和利息
 * 公式：每月还款本金 = 贷款本金 / 还款月数
 * 公式：每月应还利息 = (贷款本金 - 已还本金) * 月利率 / 12
 * @param invest 总借款额（贷款本金）
 * @param monthRate 月利率
 * @param month 还款月数
 * @return 每月还款本金明细
 */
private static BigDecimal getCapitalAmount(BigDecimal invest, double monthRate, int month) {
    BigDecimal monthPri = invest.divide(new BigDecimal(month), 2, BigDecimal.ROUND_DOWN);
    BigDecimal count = new BigDecimal(month);
    count = count.multiply(new BigDecimal(monthRate));
    return count;
}
```

画面 6：
- 代码文件：`RepaymentUtil.java`
- 代码内容：
```java
/**
 * 计算月利率
 * @param yearRate 年利率
 * @param month 月数
 * @return 月利率
 */
public static EqualInterestRepayment fixedRepayment(BigDecimal invest, BigDecimal yearRate, int month, BigDecimal amount) {
    double monthRate = yearRate.doubleValue() / 12;
    EqualInterestRepayment equalInterestRepayment = new EqualInterestRepayment();
    // 封装数据
    equalInterestRepayment.setAmount(getRepaymentAmount(invest, monthRate, month));
    equalInterestRepayment.setInterestMap(getRepaymentList(invest, monthRate, month));
    equalInterestRepayment.setPrincipalMap(getRepaymentPrincipalList(invest, monthRate, month));
    equalInterestRepayment.setTotalAmount(getRepaymentTotal(invest, monthRate, month));
    equalInterestRepayment.setInterest(getRepaymentInterest(invest, monthRate, month));
    return equalInterestRepayment;
}
```

画面 7：
- 代码文件：`EqualInterestRepayment.java`
- 代码内容：
```java
/**
 * 等额本息还款计划
 * @author winhao@itcast.cn
 * @since 2019/5/22
 */
public class EqualInterestRepayment {
    /**
     * 每月还款本金
     */
    private BigDecimal amount;
    /**
     * 每月还款利息、期数、利息
     */
    private Map<Integer, BigDecimal> interestMap;
    /**
     * 每月还款本金、期数、本金
     */
    private Map<Integer, BigDecimal> principalMap;
    /**
     * 本息和
     */
    private BigDecimal totalAmount;
    /**
     * 总利息
     */
    private BigDecimal totalInterest;
}
```

画面 8：
- 代码文件：`EqualInterestRepayment.java`
- 代码内容：
```java
/**
 * 等额本息还款计划
 * @author winhao@itcast.cn
 * @since 2019/5/22
 */
public class EqualInterestRepayment {
    /**
     * 每月还款本金
     */
    private BigDecimal amount;
    /**
     * 每月还款利息、期数、利息
     */
    private Map<Integer, BigDecimal> interestMap;
    /**
     * 每月还款本金、期数、本金
     */
    private Map<Integer, BigDecimal> principalMap;
    /**
     * 本息和
     */
    private BigDecimal totalAmount;
    /**
     * 总利息
     */
    private BigDecimal totalInterest;
}
```

画面 9：
- 代码文件：`RepaymentServiceImpl.java`
- 代码内容：
```java
//1.1 获取借款人还款计划
ProjectDTO projectDTO = projectWithTendersDTO.getProject();
//1.2 获取投标信息
List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
//1.3 计算还款的月数
Double ceil = Math.ceil(projectDTO.getPeriod()/30.0);
Integer month = ceil.intValue();
//1.4 还款方式，只针对等额本息
String repaymentWay = projectDTO.getRepaymentWay();
//1.5 生成还款计划
//1.6 生成投资人应收明细
```

画面 10：
- 代码文件：`RepaymentServiceImpl.java`
- 代码内容：
```java
/**
 * 生成 等额本息还款计划
 * @param invest 本金
 * @param monthRate 月利率
 * @param month 期数
 * @return 还款计划
 */
public static EqualInterestRepayment fixedRepayment(BigDecimal invest, BigDecimal yearRate, int month, BigDecimal amount) {
    double monthRate = yearRate.doubleValue() / 12;
    EqualInterestRepayment equalInterestRepayment = new EqualInterestRepayment();
    // 封装数据
    equalInterestRepayment.setAmount(getRepaymentAmount(invest, monthRate, month));
    equalInterestRepayment.setInterestMap(getRepaymentList(invest, monthRate, month));
    equalInterestRepayment.setPrincipalMap(getRepaymentPrincipalList(invest, monthRate, month));
    equalInterestRepayment.setTotalAmount(getRepaymentTotal(invest, monthRate, month));
    equalInterestRepayment.setInterest(getRepaymentInterest(invest, monthRate, month));
    return equalInterestRepayment;
}
```

画面 11：
- 代码文件：`RepaymentServiceImpl.java`
- 代码内容：
```java
//1.1 获取借款人还款计划
ProjectDTO projectDTO = projectWithTendersDTO.getProject();
//1.2 获取投标信息
List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
//1.3 计算还款的月数
Double ceil = Math.ceil(projectDTO.getPeriod()/30.0);
Integer month = ceil.intValue();
//1.4 还款方式，只针对等额本息
String repaymentWay = projectDTO.getRepaymentWay();
//1.5 生成还款计划
RepaymentUtil.fixedRepayment(projectDTO.getAmount(), projectDTO.getBorrowerAnnualRate(), month, projectDTO);
//1.6 生成投资人应收明细
```

画面 12：
- 代码文件：`RepaymentServiceImpl.java`
- 代码内容：
```java
//1.1 获取借款人还款计划
