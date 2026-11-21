# day14-10-用户还款-第三阶段-本地事务1

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-10-用户还款-第三阶段-本地事务1_【海量资源尽在 666java.com】.mp4
- 时长 11分40秒（音频 701s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把这个图当中第一步这块功能搞定了就是还款服务网RocketMQ发这个什么呀半消息是不是那咱结合这个图看咱接下来该实现哪一块功能二和三咱不用管吧那是不是就该四了就是还款服务这边要执行本地事务那他这个本地事务主要是要做一些数据库操作大家看一下就是更新一些数据对吧比如说这个还款明细
[00:31] 这个状态我们要改成以同步对吧这个投资人的应收明细要改成以收对不对还款计划的状态要改成以还款啊这是我们既然要实现这块功能那这块功能的话大家注意一下啊你这两样图要结合着看呃他对应的其实就是咱这个业务流程当中的这块2.2大家看一下是不是在2.2之前呢我们就是第二阶段吧我们是不是已经冻结了这个还款金额了是不是啊
[01:01] 我们说只要这个还款金额冻结了呢基本上就能保证这个还款成功啊那冻结了还款金额之后呢我们在阶段三吧就是2.2这一块我们就要处理本地事务就是做一些数据的更新当然我们前面分析过嘛这一块是不是跟下边这个第四阶段是不是一个一个一个原子性绑定的一个问题就是它存在分布式事务的问题对不对但是按照这个流程呢我们接下来的确是该执行还款服务这边的这个什么呀
[01:29] 本地数那这块功能代码我们应该写到业务层由业务层呢去调用Mapper接口对吧来实现这几个什么呀更新操作呃那所以说呢咱接下来还是要找到业务层的接口啊咱先定义一个方法然后再去实现它在这对不对好我们在最下边再定义一个方法来我们一起看一下讲义啊
[01:56] 这个最终要实现的功能刚才说了就是更新还款明细以同步更新应收明细以收更新还款计划是什么以还款你看我们在这个接口当中是不是要新增一个方法叫confirm对吧repayment的方法这个方法有一个返回值是不二类型的那就是成功没成功对不对这个什么名字我们跟奖励保持一致方法名
[02:33] 那咱接下来重点要看的是不是这两个参数都是啥咱一起瞅一瞅一个是还款计划一个是那个什么呀这是什么呀对这是还款的那个请求对象对不对这里边也封装了很多数据那我们在更新这些数据的时候呢就需要用到这两个参数对象里边的一些数据啊所以说我们需要把他俩都传进来就咱一会实现功能的时候你就能具体看到哎我们都要从这里边取什么数据
[03:03] 这是咱又新增了这么一个方法用来干啥处理本地事务的啊就是做一些数据的更新咱把这个注释呢也给他拿过来好这是接口里边方法咱就定义好定义好之后呢咱去实现类当中啊把这个方法呢给它生成出来然后开始实现功能有点卡啊咱看看生成到什么地方好在这对不对啊这里边呢我们说了是不是主要进行一些数据库操作吗一共要做哪些事情呢
[03:46] 来咱罗来一下啊分析分析首先我们要实现的一个功能就是什么状态要给啊对更新什么呀还款明细改成什么呀以同步然后呢还有什么功能啊对更新什么呀应收明细为什么呀以收啊还有什么功能啊
[04:18] 第三个还是更新谁啊对最后一个是更新还款计划还款计划更新成什么呀以还款对吧那其实这个第二步的话啊我们还要再给他拆分的更细一点啊第二步其实应该准确来讲是这样子他应该是更新哪个表呢大家注意看一下啊
[04:46] 对他应该更新的是这个receiveable plan这个表的状态那这是不是有个状态盖成什么呀已收啊这个大家一定要注意了我们之前这个表里边已经有数据了是不是在在哪个阶段在前面实现哪个功能的时候啊那满标放快是不是我们往这里边视频下六十长数据嘛当时我们说是五个投资人一共十二七然后五乘十二是不六十对不对我们要更新这个表的状态
[05:16] 所以说我这样的给你改一改然后呢其实第二步呢我们还可以再拆分啊第二步我们这里边你看我这样给你写吧这是2.1啊第二步我们还要做一个事就是保存数据到哪个表呢给大家看一下我们目前呢你看啊呃这个表这个表还有这个表这三个表是不是都已经有数据了但是这个表还没数据这个表其实才是真正的应收
[05:57] 明细表那这个时候呢我们就应该往这个表里边保存数据了为什么因为我们现在是不是在进行还款我们以前说过我这边还款了你那边就干什么呀收到钱了从我这边还款一实现你这边就应该产生什么呀应收明细啊所以我们就需要往这个表里边给保存数据了那这个名字呢就是resale detail是吧
[06:22] 所以我们其实具体的数据库操作一共有四个我们拆分的细点那接下来一个一个来吧先说第一步我们说叫更新还款明细为这个状态改成什么呀对改成已同步因为在之前我们这个还款明细它默认应该都是什么呀未同步现在要改成什么呀已同步那这个代码怎么写呢是不是就是增加改良当中的什么呀改是吧就是更新那我们直接调用右层呗我们应该直接调用什么呀
[06:52] 对数据访问层呗数据访问层的话我们应该用的是哪个MAP接口啊应该是黄款明细嘛应该是这个Repayment Detail是吧MAP更新操作我们应该是调用什么呀Update方法大家看一下对吧然后呢这个代码大家应该还有印象吧那第一个参数到我们暂时不需要啊给他一个什么呀空就行了第二个参数是我们重点需要来来给值的啊就是这个Warp
[07:23] 这里边是不是也是封装这个什么呀都更新哪些字段还有这个什么条件是不是那咱这呢就是WRAPPWARPS第二咱还是用Lambda的那种写法Lambda update对吧然后呢这呢还需要设置一个范形那自然就是repayment detail因为我们修改的是这个表嘛然后呢接下来我们就要先设置什么东西对我们要设置要改哪个字段
[07:54] 我们要改哪个字段了是不是那个状态嘛对不对那应该怎么写就是repayment detail那个状态应该是这个啊这个然后值呢值从哪来啊值是不是就改成那个什么呀以同步嘛以同步那个是在stay有个枚句吗status code点同步就是这个status下限1就是0改成1嘛然后呢我们需要dell给它go的
[08:26] 然后还没完啊还没完那我要是现在就这么结束了呢是不是意味着这个表里边所有的数据这个字段的值都被改了对不对那显然是不符合我们的这个需求的啊我们要改的是对本次进行还款了对不对这这这条数据大家看一下咱这个还款明细应该就是这个表
[08:49] 是不是你你肯定不是所有的这个数据都要进行更新吧对不对肯定是更新某一条啊或者说符合条件的这个某些数据那我们这里边需要设置一个条件那根据什么来进行更新呢那你要根据ID可以吧对不对然后根据这个什么request number都可以对吧这俩都是能够进行这个唯一区别的是不是那我们看看这俩值我们能得到谁对吧能得到谁我们就用谁呗那咱看看啊这两个值呢我们
[09:19] 有办法从哪取到呢你只能是从这两个参数对象里面去想办法是不是因为咱手头上就这两个参数啊我们看能不能从这个参数里边哎找到我们想要的东西那这里边的话我们就需要从第二个参数里边来去因为第二个参数里边封装的有这个纸啊就这个这个什么呀流水号好我们看一看他这里边的属性吗之前咱们看过一次啊我们主要是要这个要这个
[09:50] 那咱就要在这封装一个条件是不是用EQ是不是EQ应该写到哪儿这个EQ我点不出来了点EQ对不对然后我们的条件是根据哪个字段我们刚才说的对这个request number值是从哪去第二个参数叫repayment request点
[10:23] 第二这个get get对注意了我们调呢是pre request number就是预处理这个流水号这个是大家一定要注意的好我们看一下是不是缺这个什么小果号配对的这个问题啊好我们看这个set方法应该是到哪到这啊然后是EQ啊是不是最后呢缺一个小果号对吧
[10:56] 你看这个代码写起来稍微有点长这是咱们第几个更新呢第一个更新就写出来了那咱这样吧这个代码这么长我们把这个值给它取出来这个值呢有可能在下面还要用我们把它单独放到第一行存到一个变量里边string p r e r e q u e s trequest number
[11:28] 然后呢我们把它是不是放到哪放到这就OK了这第一个更新操作呢咱就搞定了对不对更新还还名称为一同步

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解还款服务中确认还款的业务流程与对应的 Java 代码实现，包括消息确认、本地事务处理、数据库状态更新等环节。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示还款服务与 RocketMQ 之间的消息确认流程图，包含发送确认消息、消息接收成功、接收回调、执行本地事务、发送执行结果、修改消息状态、接收消息重试、通过 feign 向存管代理服务发请求等步骤。
画面2：展示还款服务与存管代理服务之间的消息处理流程图，包含更新交易记录、确认还款成功、处理请款确认还款、更新交易记录状态为“未同步”、更新交易记录状态为“已同步”、更新交易记录状态为“已还款”等步骤。
画面3：展示还款服务接口定义，新增 confirmRepayment 方法，参数为 RepaymentPlan 和 RepaymentRequest。
画面4：展示还款服务接口定义，新增 confirmRepayment 方法，参数为 RepaymentPlan 和 RepaymentRequest。
画面5：展示还款服务中生成还款计划的代码，包括获取投标信息、计算还款月数、生成还款计划、保存还款计划等。
画面6：展示数据库表结构，表名为 receivable_plan，包含 ID、USER_ID、TENDER_ID、REPAYMENT_ID、NUMBER_OF_INSTALLMENTS、INTEREST、PRINCIPAL、AMOUNT、SHOULD_RECEIVABLE_DATE、RECEIVABLE_STATUS、CREATE_DATE、COMMISSION 等字段。
画面7：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面8：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面9：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面10：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面11：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面12：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面13：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。
画面14：展示还款服务中 confirmRepayment 方法的代码，包括更新还款明细、保存还款计划、更新还款计划状态等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
/**
 * 确认还款处理
 * @param repaymentPlan
 * @param repaymentRequest
 * @return
 */
Boolean confirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest);
```

画面4：
```java
/**
 * 确认还款处理
 * @param repaymentPlan
 * @param repaymentRequest
 * @return
 */
Boolean confirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest);
```

画面5：
```java
// 1.4 计算还款月数
Double ceil = Math.ceil(projectDTO.getPeriod() / 30.0);
Integer month = ceil.intValue();

// 1.5 还款方式，只针对等额本息
String repaymentWay = RepaymentDTO.getRepaymentWay();

if (repaymentWay.equals(RepaymentWayCode.FIXED_REPAYMENT.getCode())) {
    EqualIntervalsRepayment fixedRepayment = RepaymentUtil.fixedRepayment(projectDTO, getAmount(), projectDTO.getPeriod());
    List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
}
```

画面6：
```sql
CREATE TABLE `receivable_plan` (
  `ID` bigint(20) NOT NULL,
  `USER_ID` bigint(20) NOT NULL,
  `TENDER_ID` bigint(20) NOT NULL,
  `REPAYMENT_ID` bigint(20) NOT NULL,
  `NUMBER_OF_INSTALLMENTS` int(11) NOT NULL,
  `INTEREST` decimal(10,2) NULL,
  `PRINCIPAL` decimal(10,2) NULL,
  `AMOUNT` decimal(10,2) NULL,
  `SHOULD_RECEIVABLE_DATE` datetime NULL,
  `RECEIVABLE_STATUS` tinyint(4) NULL,
  `CREATE_DATE` datetime NULL,
  `COMMISSION` decimal(10,2) NULL,
  `REPAYMENT_PLAN_ID` bigint(20) NOT NULL,
  `REPAYMENT_PLAN_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_CODE` varchar(50) NULL,
  `REPAYMENT_PLAN_NAME` varchar(255) NULL,
  `REPAYMENT_PLAN_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_REMARK` varchar(255) NULL,
  `REPAYMENT_PLAN_CREATE_DATE` datetime NULL,
  `REPAYMENT_PLAN_UPDATE_DATE` datetime NULL,
  `REPAYMENT_PLAN_DELETE_FLAG` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_DATE` datetime NULL,
  `REPAYMENT_PLAN_DELETE_USER_ID` bigint(20) NULL,
  `REPAYMENT_PLAN_DELETE_REASON` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE` varchar(50) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE` varchar(50) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE` varchar(50) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE` varchar(50) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE` varchar(50) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS` tinyint(4) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_CODE_TYPE_STATUS_DESC` varchar(255) NULL,
  `REPAYMENT_PLAN_DELETE_REASON_CODE_TYPE_STATUS_CODE_TYPE_STATUS

