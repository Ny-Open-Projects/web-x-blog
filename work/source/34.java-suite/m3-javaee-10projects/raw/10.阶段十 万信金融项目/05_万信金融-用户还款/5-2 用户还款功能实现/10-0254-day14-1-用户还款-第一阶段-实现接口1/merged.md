# day14-1-用户还款-第一阶段-实现接口1

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-1-用户还款-第一阶段-实现接口1_【海量资源尽在 666java.com】.mp4
- 时长 7分5秒（音频 426s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们把第一阶段里边涉及到的两个接口呢全部定义好了那咱们接下来就进行功能实现先实现接口1吧接口1我们要实现的功能是不是查询到期的防范机啊这是很明显是一个数据库操作那咱是不是应该在什么数据防范层就是Mapper接口里边是不是开始编写代码对吧那咱先找到这个谁呀Mapper接口应该是他对不对
[00:30] 这个目前是不是还是空的呀对不对没空的那咱在这里边是不是需要定义方法来编写思考语句实现这个功能那有的学员会有一个疑问那咱之前这个实现这么多功能这个Mapper接口这里边好像咱没有自己定义过方法是不是因为咱当时都是继承了这是谁这是谁
[00:56] 这是不是MP的这个baseMapper这个接口对吧我们说继承了这个接口是不是基本的自然感应是不是全部都有对不对没错啊那咱这呢其实要实现的这个查询呢也不是很麻烦其实就俩条件那但是呢咱这里边呢涉及到日期的一些处理比如说格式上对不对所以说呢如果你通过MP啊它封装的这个API去实现的话没有那么灵活啊或者稍微有点麻烦所以我们这呢
[01:26] 准备像mybatties一样啊我们自己定义方法自己编写思考语句啊更加灵活一些那咱就定义一个方法写个思考语句来实现这个查询功能吧呃这个方法名咱跟讲义保持一致吧行吧方法名他叫这一块我就拿过来了因为咱刚才定义过这个接口嘛这个方法都是一样的大家看一看是吧还是传过来一个日期吗
[01:59] 然后进行查询查完之后呢查到的这个什么呀缓缓计划封装成绿色集合返回嘛这块大家都很清楚关键就是接下来我是不是要写思考语句实现这个功能啊s e l e c t对吧那这里边我是不是要包含一个什么呀思考语句啊这个搜索语句至关这个搜索语句啊至关重要这所以写出来了咱这功能其实就实现了所以咋写呢你看这儿呗
[02:32] 这个咱前面在定义接口的时候分析过啊我们说这个功能呢一共需要两个参数对吧一个是日期一个是什么呀状态而且这个状态这个值是固定死的你还不用管那咱根据这个分析咱们把这个sql一句写一写来s1l1cp flag的谁啊cform从哪查啊是不是就这个repayment什么呀plan表对不对从这查你号子你不要我就简写成slack星了啊
[03:02] 那我们说了有几个条件两个条件嘛一个是日期一个是什么呀状态那日期这块的话我们其实说白了就是做一个相等判断嘛是不是一个相当判断对就是这个谁呀这个那个字段名叫找找就是这个字段他呢干什么呀等于谁谁谁是这意思吧然后还有一个条件还有一个条件就是这个状态状态就是这个状态这个值
[03:35] 是布丁死的必须等于多少对等于0这个地方你看好了它是什么类型的蛙圈类型它可不是数字所以你看我这儿带有引号大家看大概我这个数据是不是就写出来了对不对但是呢这个日期这一块呢我们要做处理要对这个格式做处理我们前面在定义解课的时候不是说过了吗它是什么格式中间是杠对不对对中间是杠啊这种格式
[04:03] 所以说呢我们在思考语句里边呢要对这个字段的值进行处理我们要调用一个函数就是这个叫叫叫叫什么呀叫data format下滑线format就是这个format然后这里边你看有几个参数两个参数第一个参数就是这个这个日期嘛第二个参数就是那个格式第二个参数咱这么子来写呀
[04:39] 然后指定一个格式啊反正这个搜索里边这个格式应该这么写啊百分号Y杠然后百分号M杠然后百分号什么呀D对应该这么写这个你基本上也能猜出来啥意思吧年月日中间是什么呀对用杠来拼接啊所以这个函数呢其实是对这个日期这个值进行了什么呀格式化了进行果实上这个一定要注意
[05:10] 然后呢再往后这个问号肯定不是这么写对不对这个问号的话在咱们卖battis里边应该怎么写那个战划服应该是警号大口号对不对这里边写上谁呀d a t e这个咱一会跟参数做一个对应是不是就行了哎你看这个搜尾语也不是很复杂吧看好了一共有两个条件啊第二个条件是固定死了这个状态必须是凉只是第一个条件呢那由于他是日期嘛我们要对他做一个格式化然后
[05:39] 跟我们传进来的值做一个什么呀对相等判断就行大家看一下讲义你看讲义里边给我们提供的这个语句跟我们刚才写的应该是一样的吧你自己瞅一眼是不是一样啊那我就拿过来放到这儿了对不对就放到这里没错吧对这个咱们怎么说呢又存到代码咱就写完了写完之后是不是需要再不是这是什么呀数据房子存到代码咱就写完了啊
[06:12] 那这块代码写完之后咱接下来是不是应该要干什么呀要去右层进行调用啊右层的实现类比较咱找一找业务层的实现类就是这儿他这应该报错了呀我们是不是刚才定一接口了吗对对定了俩接口咱先把这两个方法都给他生成了应该是在下边吧在这儿就在
[06:41] 我们现在实现功能应该是这个功能吧那这就简单了是不是调Mapper接口里边咱刚才定义的那个方法就行了也就返回了那就是planmapper.刚才起了是不是这个名字对不对然后呢把这个什么日期扔进去就OK了这个接口1这个查询功能是不是咱就搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
    2. 在业务层 RepaymentServiceImpl 类中调用 Mapper 实现查询功能：
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
package cn.ictast.wanxingzp.repayment.Mapper;

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
package cn.ictast.wanxingzp.repayment.Service;

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
package cn.ictast.wanxingzp.repayment.Service;

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

