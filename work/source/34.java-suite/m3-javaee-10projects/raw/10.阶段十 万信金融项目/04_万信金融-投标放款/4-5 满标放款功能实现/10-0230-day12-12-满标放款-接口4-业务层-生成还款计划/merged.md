# day12-12-满标放款-接口4-业务层-生成还款计划

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-12-满标放款-接口4-业务层-生成还款计划_【海量资源尽在 666java.com】.mp4
- 时长 7分11秒（音频 431s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 现在呢我们是不是正在实现生成借款人还款计划这个功能那么刚才呢我们把该需要的这个数据是不是都已经拿到手了就是这些东西那咱接下来就根据这些信息呢去生成还款计划那么这个还款计划呀我们已经把这个功能抽取成方法放到一个工具类当中了让大家看看就这个工具类在YouTube这个包里边啊有一个工具类呢叫
[00:32] repayment youtube我们打开一起看一看这里边都实现了哪些功能封装了哪些方法那这里边这些东西其实跟这儿是有密切的关系的啊就是就这个地方等了本期的这个缓缓方式这里边是有一些公式吗对不对阅历历啊等等等等这些东西啊那么我们这个工具类当中他封装的这些方法呢主要就是根据这些公式吧来生成的一些什么呀数据一些值啊咱一起看一看
[01:03] 你看你比如说他就可以帮我们最终是可以生成这个什么还款计划然后还有哪些功能你看他可以帮我们计算每月偿还的本金和利息之和吗他还帮我们计算每个月偿还的利息是多少还有每个月偿还的本金是多少对不对还有什么呀你一共要还的这个总的利息是多少还有本金总和是不是等等等等然后这个本金的一个计划还有什么呀
[01:34] 每月偿还的本金和利息的制合对不对这是不进行什么私手股入的每月偿还的本金吧等等等等啊这个功能非常非常多啊包括他还写了有这个闷发来进行测试那对于咱来说呢咱就不用管这里边具体的细节了就是我之前给大家说这个公式吧你大概知道这个什么叫等额本息就行了至于这里边这个计算呀对吧金融当中的这些东西大家不用管它那这里边也是封装好的这个方法咱直接拿着用就行了
[02:03] 那咱现在是不是就是要干什么呀生成这个啊等额本息的这个还款计划那我们要调的方法呢就是这个方法啊fixed repayment我们就看一看这个方法他要啥咱就给他什么信息是不是就可以了对不对因为这是他要的一些东西是吧那一会呢他要啥我给他啥然后呢他计算完之后呢是不是会返回给我们一个什么呀返还值这个返还值里边呢应该是封装好的我们最终想要的一些东西咱可以看看
[02:31] 这边都封装啥封装的都是他计算出来的东西对吧每月还款的本息每月还款的什么利息每月还款的什么本金是不是然后本息总和总利息平台的抽息等等反正我们需要的一些东西他都计算好然后全部封装到这里边然后返回给我们这是有这么一个工具类里边的封装好了很多方法大家知道咋回事就行那咱接下来的话就调用这个方法开始生成这个什么还款计划
[03:02] 就是在这对不对我们调用这个工具类叫repayment youtube我们找一下就这个调用他的这个fixedrepayment的方法那么他呢一共要几个参数呢咱一起再熟悉熟悉应该是哪个呀这儿是吧你看第一个参数他表示什么本金就是说本金指的就是借款人借多少钱比如他借一万块钱这个一万就是什么本金
[03:36] 然后第二个参数就是那个什么月数就是你需要借多少时间我们换算成月数然后再往后大家看还有什么这个参数是表示什么这个顺序你注意一下它跟这可能不是完全对照这是利率年利率对吧这就是那个月数最后这个大家应该有印象是不是有平台的那个那个什么呀平台的佣金对吧大家还有印象吗我说我们P2P平台就是一个中介
[04:07] 我们就是从每笔交易当中去抽取什么样的佣金呢是不是啊这是咱们的佣金啊说这是这12344个参数对不对我们把这4个参数给他就行了啊我们看第一个参数我们跟他说的就是什么东西啊第一个参数呢就是这个本金对吧本金呢我们是不是从标的信息里边就可以取出来调哪个方式本金呢也就这个方这是本金然后第二参数是啥
[04:33] 第二个参数是那个什么年利率吧年利率也是从这个project里边去取应该是应该是这个应该是这个值然后第三个参数是那个月数月数不是在在在上面咱刚才刚计算过吗就是他然后最后一个参数就是啥最后一个参数就是这个我们平台抽取的佣金他也是在标的信息里边呢应该是
[05:06] 我们不太确定的话我们就去这个类当中我们找一找对不对找一找看这里边哪个是呢平台佣金是不是应该就是他了对应该就是他了平台佣金那我们就回到这把这个代码呢给他补充上就是他然后大家看一下这四个参数我该给的是不是都给过了对吧
[05:40] 然后呢在这个方法里边他就会进行什么呀计算啊或者说生成这个缓缓计划那么他生成的产生的一些数据呢我们刚才大家看到了是不是会返回一个值对不对封装到这个类当中我们接下来呢用他来接收一下这个值我们其他名字就叫叫啥了fix的repaymentfix的repayment其实这就是我们的什么呀缓缓计划啊我们就已经生成了
[06:13] 数据呢就封装到这里边那生成了还款计划之后这就完事了吗哎没有完事啊没有啊还款计划生成之后我们得把这个数据啊相当数据给它保存到什么保存到数据库里边你想一下你作为这个借款人的话你是不是随时都有可能去干什么呀通过咱们这个前端去查询那个什么还款计划对不对我得看看我我每个月还多少钱是不是这个每个月本金还多少啊利息还多少啊对不对我需要还多少时间啊
[06:43] 是不是你需要进行查询那你要想进行查询这些数据你是不是得存到什么数据库里边所以说我们接下来其实还有一步就是干什么对保存这个什么缓缓计划把它保存到数据库里边这一块有点复杂咱一会单独再说那么目前咱们就把生成缓缓计划的功能给搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

