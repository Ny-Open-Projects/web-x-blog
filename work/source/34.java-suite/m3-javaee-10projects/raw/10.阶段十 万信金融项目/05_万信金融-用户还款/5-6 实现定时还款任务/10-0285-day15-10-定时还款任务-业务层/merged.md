# day15-10-定时还款任务-业务层

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-6 实现定时还款任务
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-6 实现定时还款任务\day15-10-定时还款任务-业务层_【海量资源尽在 666java.com】.mp4
- 时长 4分24秒（音频 264s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们把数据防暗层的代码呢修改了一下那数据防暗层的代码发生了变化之后业务层的代码是不是也应该跟着发生变化对不对也就是说我们接下来要修改业务层的代码因为业务层要调用数据防暗层嘛你数据防暗层这个方法都变了我们是不是增加俩参数嘛对不对那你业务层的代码肯定要相应的发生这个调整那咱需要先找到业务层的这个接口就这
[00:28] 你看咱要曾当时跟用户还款相关的方法我们找一找啊应该是应该是一个是这个一个是这个你看看是不是你看这是查询到期的还款计划这是执行什么呀用户还款你看当时是不是都是一个参数就是那个日期嘛对不对那刚才大家看到了我们的数据法案层已经不是一个参数是不是又增加了两个参数对不对那所以说你的这个要藏要发生相应的变化
[00:58] 这个地方我是不是都要增加什么呀参数啊增加两个一个是这个什么呀分片总数啊一个是分片项这是一个地方啊还有一个地方还有一个地方是在下边是在哪呢是在这对不对在这一样啊也是需要增加这两个参数那这个样子吧我为了让大家做对比啊前后做对比我这样原来的这个呢我
[01:34] 不删掉了啊不在这直接进行修改了我给你保留下来你去做一个对比可以吧下下这个地方也是一样你做一个对比吧那你说被注视掉的是不是原来的他只传传进来一个什么样日期啊然后现在用的是都是几个参数的对三个参数那我们的接口一改你想一想这个实现类是不是自然也会应该会报错了吧对不对因为原来你雕呢是不是都是使用的都是这个什么一个参数的方法现在你变成
[02:14] 三个参数他应该会报错你看这边都已经报错了是不是报错的话呢咱就要进行修改啊都需要修改哪些地方呢咱一起找一找啊很简单哪个地方报错你就改哪个吧是不是你看这是不是又报错这就应该是不是还要再增加两个参数嘛对不对增加两个参数我从接口里边给他粘过来你接口变了实际上肯定也得变是不是那你这传的数据肯定也不是一个了吧
[02:47] 需要传sharding count还有sharding item是不是然后再看还有哪报错呀还有一个方法是不是这个地方是不是也得需要再增加两个参数那这在调温的时候是不是也需要传一共传几个字三个字再加上一个sharding count再加上一个sharding item是不是那为了能让大家将来很方便的看到这个分片的这个效果我准备在这个地方
[03:18] 往控制台输出一些数据啊大家看走到这儿的时候这个什么盗窃的缓缓计划其实都已经查证出来这儿在进行便利对不对我在这呢准备跟入门案例一样打印一个东西啊打印比如说这个什么呀啊当前分片把那个分片像分片纸给他打印出来吧啊加上这个应该是sharding item是吧sharding item然后再加上
[03:48] 我是不是得把这个查询出来的这个还款计划给他打印出来那查询出来还款计划不就是这个repayment plan吗是不是这是在便利的这个过程当中产生的这个对象大家看我又增加了这么一条输出语句啊将来我启动比如说启动两个什么呀微服务那你在这两个微服的控制台你就看看这条输出语句是不是一个是什么呀举个例子啊一个是什么呀奇说的一个是什么呀偶说的是不是在进行平均分配啊这是我们把
[04:19] 这个什么样EOS代码就修改完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个还款服务的代码实现，包括 Mapper 接口定义、Service 层逻辑、分库分表处理以及数据持久化操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PlanMapper.java 文件，定义了两个查询方法 selectDueRepayment，用于根据日期查询还款计划，并包含分库分表的参数。
画面 2: 展示 RepaymentService.java 文件，定义了 executeRepayment 方法，用于处理还款业务，包含注释说明其功能。
画面 3: 展示 RepaymentService.java 文件，聚焦在 confirmRepayment 方法，用于确认还款。
画面 4: 展示 RepaymentService.java 文件，聚焦在 executeRepayment 方法，注释说明其功能。
画面 5: 展示 PlanMapper.java 文件，再次聚焦在 selectDueRepayment 方法。
画面 6: 展示 RepaymentService.java 文件，聚焦在 executeRepayment 方法，注释说明其功能。
画面 7: 展示 RepaymentServiceImpl.java 文件，展示类的包名、继承关系及成员变量，包括多个 Mapper 和 Agent。
画面 8: 展示 RepaymentServiceImpl.java 文件，聚焦在 executeRepayment 方法，注释说明其功能。
画面 9: 展示 RepaymentServiceImpl.java 文件，聚焦在 saveRepaymentDetail 方法，注释说明其功能。
画面 10: 展示 RepaymentServiceImpl.java 文件，聚焦在 saveRepaymentDetail 方法，注释说明其功能。
画面 11: 展示 RepaymentServiceImpl.java 文件，聚焦在 selectDueRepayment 方法，注释说明其功能。
画面 12: 展示 RepaymentServiceImpl.java 文件，聚焦在 executeRepayment 方法，注释说明其功能。
画面 13: 展示 RepaymentServiceImpl.java 文件，聚焦在 executeRepayment 方法，注释说明其功能。
画面 14: 展示 RepaymentServiceImpl.java 文件，聚焦在 executeRepayment 方法，注释说明其功能。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
import ...

/**
 * 还款人王珏计划 Mapper 接口
 */
public interface PlanMapper extends BaseMapper<RepaymentPlan> {

    @Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, 'Y-m-d') = #{date} AND")
    List<RepaymentPlan> selectDueRepayment(String date);

    @Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, 'Y-m-d') = #{date} AND")
    List<RepaymentPlan> selectDueRepayment(String date, @Param("shardingCount") int count, @Param("shardingItem") int item);
}
```

画面 2:
```java
void executeRepayment(String date);

// 还款预处理：冻结借款人应还款额
@Param("repaymentPlan")
@Param("prologueNo")
@Return
```

画面 3:
```java
// 默认还款处理
@Param("repaymentPlan")
@Param("repaymentRequest")
@Return
```

画面 4:
```java
// 查询所有到期的还款计划
@Param("date 格式：yyyy-MM-dd")
@Return
List<RepaymentPlan> selectDueRepayment(String date);

// 根据还款计划生成还款明细并保存
@Param("repaymentPlan")
@Return
RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan);

// 执行用户还款
@Param("repaymentPlan")
@Return
void executeRepayment(String date);
```

画面 5:
```java
import ...

/**
 * 还款人王珏计划 Mapper 接口
 */
public interface PlanMapper extends BaseMapper<RepaymentPlan> {

    @Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, 'Y-m-d') = #{date} AND")
    List<RepaymentPlan> selectDueRepayment(String date);

    @Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, 'Y-m-d') = #{date} AND")
    List<RepaymentPlan> selectDueRepayment(String date, @Param("shardingCount") int count, @Param("shardingItem") int item);
}
```

画面 6:
```java
// 查询所有到期的还款计划
@Param("date 格式：yyyy-MM-dd")
@Return
List<RepaymentPlan> selectDueRepayment(String date, int shardingCount, int shardingItem);
```

画面 7:
```java
package cn.icast.wanxing2p.repayment.Service;

import ...

@Service
@Clif4
public class RepaymentServiceImpl implements RepaymentService {

    @Autowired
    private PlanMapper planMapper;

    @Autowired
    private ReceivablePlanMapper receivablePlanMapper;

    @Autowired
    private RepaymentDetailMapper repaymentDetailMapper;

    @Autowired
    private DepositoryAgentApiAgent depositoryAgentApiAgent;

    @Autowired
    private ReceivableDetailMapper receivableDetailMapper;
}
```

画面 8:
```java
@Override
public void executeRepayment(String date) {
    // 查询到期的还款计划
    List<RepaymentPlan> repaymentPlanList = selectDueRepayment(date);

    // 生成还款明细
    repaymentPlanList.forEach(repaymentPlan -> {
        RepaymentDetail repaymentDetail = saveRepaymentDetail(repaymentPlan);
        // 还款预处理
        Boolean preRepaymentResult = preRepayment(repaymentPlan, repaymentDetail.getRequestNo());
    });
}
```

画面 9:
```java
@Override
public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) {
    RepaymentDetail repaymentDetail = null;
    if (repaymentDetail == null) {
        repaymentDetail = new RepaymentDetail();
        repaymentDetail.setRepaymentPlanId(repaymentPlan.getId());
        repaymentDetail.setAmount(repaymentPlan.getAmount());
        repaymentDetail.setCreateTime(new Date());
    }
    repaymentDetailMapper.insert(repaymentDetail);
    return repaymentDetail;
}
```

画面 10:
```java
@Override
public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) {
    RepaymentDetail repaymentDetail = null;
    if (repaymentDetail == null) {
        repaymentDetail = new RepaymentDetail();
        repaymentDetail.setRepaymentPlanId(repaymentPlan.getId());
        repaymentDetail.setAmount(repaymentPlan.getAmount());
        repaymentDetail.setCreateTime(new Date());
    }
    repaymentDetailMapper.insert(repaymentDetail);
    return repaymentDetail;
}
```

画面 11:
```java
@Override
public List<RepaymentPlan> selectDueRepayment(String date, int shardingCount, int shardingItem) {
    return planMapper.selectDueRepayment(date, shardingCount, shardingItem);
}

@Override
public short getShardingCount() {
    return shardingCount;
}
```

画面 12:
```java
@Override
public void executeRepayment(String date, int shardingCount, int shardingItem) {
    // 查询到期的还款计划
    List<RepaymentPlan> repaymentPlanList = selectDueRepayment(date, shardingCount, shardingItem);

    // 生成还款明细
    repaymentPlanList.forEach(repaymentPlan -> {
        RepaymentDetail repaymentDetail = saveRepaymentDetail(repaymentPlan);
        // 还款预处理
        Boolean preRepaymentResult = preRepayment(repaymentPlan, repaymentDetail.getRequestNo());
    });
}
```

画面 13:
```java
@Override
public void executeRepayment(String date, int shardingCount, int shardingItem) {
    // 查询到期的还款计划
    List<RepaymentPlan> repaymentPlanList = selectDueRepayment(date, shardingCount, shardingItem);

    // 生成还款明细
    repaymentPlanList.forEach(repaymentPlan -> {
        RepaymentDetail repaymentDetail = saveRepaymentDetail(repaymentPlan);
        System.out.println("还款预处理成功");
    });
}
```

画面 14:
```java
@Override
public void executeRepayment(String date, int shardingCount, int shardingItem) {
    // 查询到期的还款计划
    List<RepaymentPlan> repaymentPlanList = selectDueRepayment(date, shardingCount, shardingItem);

    // 生成还款明细
    repaymentPlanList.forEach(repaymentPlan -> {
        RepaymentDetail repaymentDetail = saveRepaymentDetail(repaymentPlan);
        System.out.println("当前分片：" + shardingItem + "，还款计划：" + repaymentPlan);
    });
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

