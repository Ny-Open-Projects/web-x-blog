# day14-4-用户还款-第一阶段-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-4-用户还款-第一阶段-功能测试_【海量资源尽在 666java.com】.mp4
- 时长 4分2秒（音频 243s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把出发业务操作的这个入口也给加上了那这呢也为咱接下来进行功能测试呢奠定了基础那大家看一下这个图啊我们用户缓缓整个这个业务呢整体下来还是比较复杂所以说我们计划呢是开发一点功能就测试一下开发一点功能呢就测试一下然后呢一步一步呢往后推进那咱目前呢是不是已经把第一阶段整个这个
[00:31] 功能全部开发完毕了就是图当中的接口一和什么呀接口二那咱呢刚才呢也把什么呀业务操作这个入口一个的加上那咱接下来对第一阶段的这个功能就可以进行测试了呃那怎么测试呢大家看一下这个图啊我们要是只测试第一阶段的话大家看看是不是就只需要启动哪个服务就行了对缓缓服务啊你看接口一接口二只跟谁有关呢
[00:59] 还款服有关啊其他服我们暂时不用管那大家看一下我目前呢已经把啊这个还款服呢已经给他干什么呀启动起来了你看他占用的端口号应该是53080对不对那接下来怎么测试呢大家看一下这是不是咱刚才增加的这个出发业务执行的这个入口是不是那我们是不是通过浏览器啊或者你通过铺子卖啊包括sweat感都行你往这发一个什么呀请求就行了啊传过来一个日期嘛然后他就走这个什么呀
[01:29] 右层的这个方法然后在这个方里边我们刚才变现代码让他调用了接口一和什么呀接口二那调完之后呢咱一会就观察一下这个表里边就是这个什么表repeatment detail这个表里边有没有保存什么呀对保存缓缓明细哎我们就知道第一阶段代码有没有问题那咱接下来就打开浏览器啊开始往这发请求localhost对不对我们是530多少啊
[01:58] 对080啊53080然后呢我们应该是接下来这个微服务的基本访问路径是不是就是repayment对吧repayment呃再接下来我们的访问路径应该是要看这个Controller是不是就这一块往这发请求吗伸过来对不对在这个路径当中我是不是还需要传过来一个日期吗而且这个日期的格式是不是中间是用杠拼接呢那这个值我到底给给给多少呢
[02:34] 那这个你要看看你的表了啊你得从表里边取一个数据给它对应上就是repayment plan这个表这个表呢咱找一找那个哪个字段就这个字段should repayment data这个咱当时说过了它是这个什么英环时间吗这是咱之前生成了12期这个还款计划了你就挑第一期呗反正咱测试对不对第一期是这个时间对不对粘过来粘过来给它放到这就行对不对
[03:04] 中间是杠啊中间是杠那咱既然是敲诡车就往这发请求了啊咱走啊前端肯定看不出来啥了吧咱主要看控制台啊他回来也没有报错好空台没有报错对不对大家看一下这个我们是先进行查询了吗你看咱这个业务是不是先进行查询查询按照是不是走到save save就是insert语句吧你看看这你看他是不是往这个什么呀环环铭系这个表里边应该是插了一条数据那咱去这个数据库里边瞅瞅呗
[03:36] 哪个表是不是repayment下载的detail对不对大家看这就插进来一条数据还款明细那这个还款明细应该对应的是哪个期哪一期的还款计划肯定是第一个我刚才挑的对吧1083.09是不是没错吧对不对这是咱目前就把用户还款业务当中的第一阶段这个功能全部自然通过

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过调用“还款服务”中的接口，触发系统自动处理逾期还款计划，并展示相关代码、数据库操作和流程图。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示还款服务与存管系统之间的交互流程图，包含多个步骤，如“1.1 查询到期的还款计划”、“1.2 生成还款明细”、“1.3 还款明细处理”、“1.4 通过税钥生成签名及摘要”、“1.5 插存交易记录”、“1.6 预处理请求”、“1.7 通知存管系统”、“1.8 更新交易记录”、“1.9 更新交易记录，状态为：已同步”、“1.10 还款处理成功”、“1.11 发送确认还款事务消息”、“1.12 确认还款处理”等。
画面2：展示IDE中RepaymentController类的代码，包含一个测试方法@ApiOperation("测试用户还款")，其内部调用repaymentService.executeRepayment(date)。
画面3：展示IDE中RepaymentServiceImpl类的executeRepayment方法，其中包含注释“//查询到期的还款计划”和“//生成还款明细”，并调用saveRepaymentDetail方法。
画面4：展示IDE中RepaymentServiceImpl类的executeRepayment方法，光标位于“//生成还款明细”注释下方。
画面5：展示浏览器地址栏中输入的URL：localhost:53080/repayment/execute-repayment/2019-11-11。
画面6：展示IDE中RepaymentController类的代码，与画面2相同。
画面7：展示SQLyog数据库管理工具中“repayment_plan”表的数据，包含多行记录，显示了不同期数的还款金额、利息、应还款日期等信息。
画面8：展示SQLyog数据库管理工具中“repayment_plan”表的数据，光标位于“repayment_detail”表的“NUMBER OF PERIODS”列。
画面9：展示多个窗口的切换视图，包括“万能全量”、“用户还款”、“wanningzp_apollo”、“adminService”、“configService”等。
画面10：展示IDE中RepaymentServiceImpl类的executeRepayment方法，终端中显示执行SQL语句，包括SELECT和INSERT语句。
画面11：展示IDE中RepaymentServiceImpl类的executeRepayment方法，光标位于“//生成还款明细”注释下方。
画面12：展示IDE中RepaymentServiceImpl类的executeRepayment方法，光标位于“//生成还款明细”注释下方。
画面13：展示SQLyog数据库管理工具中“repayment_plan”表的数据，光标位于“repayment_detail”表的“NUMBER OF PERIODS”列。
画面14：展示还款服务与存管系统之间的交互流程图，与画面1相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
String result = repaymentService.startRepayment(projectWithHeadersDTO);
return RestResponse.success(result);

@ApiOperation("测试用户还款")
@GetMapping("/execute-repayment/{date}")
public void testExecuteRepayment(@PathVariable String date) {
    repaymentService.executeRepayment(date);
}
```

画面3：
```java
public void executeRepayment(String date) {
    //查询到期的还款计划
    List<RepaymentPlan> repaymentPlanList = selectDueRepayment(date);
    //生成还款明细
    repaymentPlanList.forEach(repaymentPlan -> {
        RepaymentDetail repaymentDetail = saveRepaymentDetail(repaymentPlan);
    });
}
```

画面10：
```sql
Execute SQL: SELECT ID, REPAYMENT_PLAN_ID, AMOUNT, REPAYMENT_DATE, REQUEST_ID, STATUS FROM repayment_detail WHERE REPAYMENT_PLAN_ID = 118258312871560979
Time: 1 ms - ID: cn.iceat.wanningzp.repayment.Mapper.RepaymentDetailMapper.selectOne
Execute SQL: INSERT INTO repayment_detail (ID, REPAYMENT_PLAN_ID, AMOUNT, REPAYMENT_DATE, REQUEST_ID, STATUS) VALUES (118363589510074570, 118258312871560979, 118258312871560979, '2019-11-11', '118258312871560979', '0')
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1和画面14：展示还款服务与存管系统之间的交互流程图，包含多个步骤，如“1.1 查询到期的还款计划”、“1.2 生成还款明细”、“1.3 还款明细处理”、“1.4 通过税钥生成签名及摘要”、“1.5 插存交易记录”、“1.6 预处理请求”、“1.7 通知存管系统”、“1.8 更新交易记录”、“1.9 更新交易记录，状态为：已同步”、“1.10 还款处理成功”、“1.11 发送确认还款事务消息”、“1.12 确认还款处理”等。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

