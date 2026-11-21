# day12-15-满标放款-接口4-Controller

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-15-满标放款-接口4-Controller_【海量资源尽在 666java.com】.mp4
- 时长 2分47秒（音频 167s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把右层的代码呢全部编写完了整个下来这个代码的确是比较多这个大家写的时候呢慢慢来吧一点一点来根据我这个拆分的这些什么呀步骤吧一步一步去编写就行了有些代码大家不用编写就是我刚才说的这个保存保存这个数据到数据库这里边像NEO对象啊然后特别是这种代码
[00:27] 赛车方法这一堆你可以直接沾过来拿用就行了知道他是什么意思就OK了那右层代码咱编完之后接下来是被把扛出来里边代码就完善一下对不对咱看出来里边是不是还是空时线来看这我们将来是不是应该是交易中心对吧这边是交易中心他要发请求对不对到哪到对还款微服务这边请求其实请求的就是还款微服的扛车
[00:55] 说咱接下来把Controller代码给完善一下就OK了这个比较简单我们找一找这个谁啊Controller你看咱这个Controller是不是当时是一个空实现嘛那这里边代码比较简单是不是就注入业务层调用一下业务层的方法是不是就OK了然后这儿先来一个注入那就是addauto-voteprivate那我们应该叫repayment什么呀Service好
[01:31] 这样我们就把右层的对象注进注进来之后呢注进来之后呢我们在这呢就调用咱刚才编写的start什么呀repayment这个方法就行了然后把这个参数给他扔进去是吧然后他是不是返回来有结果呀反正这个结果的话我们应该是单独用string类型给接收一下就那五个零嘛五个零比较成功的那五个零然后呢
[02:00] 然后呢怎么返回呢我们这儿是不是都是要的rest response对吧所以说你需要封装一下return rest response点那个方法是个size嘛然后把这个放进去就ok了这是Controller这块代码我们也晚上好啊晚上好了之后呢咱一会就要进行什么呀功能测试啊我们这一次呢也是直接就进行前后端
[02:30] 机身测试我们是不是要对整个什么呀对从接口1到什么呀接口4整个咱刚才啊一直编写的这一块代码就是满标放款吧整个这个业务的这个功能要进行前后端机身测试了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个还款服务的代码实现，包括服务层计算还款计划并生成应收明细，以及控制器层接收请求并调用服务层的方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 RepaymentServiceImpl.java 文件中，根据项目DTO获取还款计划并生成应收明细的逻辑，包含计算月数、判断还款方式、调用工具类生成还款计划、循环生成应收明细并保存。
画面2：展示 RepaymentServiceImpl.java 文件中，创建还款计划列表并遍历利息和手续费映射，为每个还款计划设置项目ID、用户标识、用户编码、还款计划ID、应收款信息、本金和利息。
画面3：展示 RepaymentServiceImpl.java 文件中，为应收计划对象设置应收款信息、本金和利息。
画面4：展示 RepaymentServiceImpl.java 文件中，循环遍历应收明细列表，调用 saveReceivablePlan 方法保存。
画面5：展示 RepaymentServiceImpl.java 文件中，为还款计划对象设置项目ID、用户标识、用户编码、还款计划ID、应收款信息、本金和利息。
画面6：展示 RepaymentServiceImpl.java 文件中，为应收计划对象设置应收款信息、本金和利息。
画面7：展示还款流程图，包含“还款申请”、“还款中心”、“存管机构”、“已还款”、“存管系统”等模块，以及各模块间的交互流程。
画面8：展示 RepaymentServiceImpl.java 文件中，为应收计划对象设置应收款信息、本金和利息。
画面9：展示 RepaymentController.java 文件中，定义了启动还款的 REST 接口，接收 ProjectWithTendersDTO 类型的请求体。
画面10：展示 RepaymentController.java 文件中，定义了私有属性 repaymentService。
画面11：展示 RepaymentController.java 文件中，调用 repaymentService 的 startRepayment 方法。
画面12：展示 RepaymentController.java 文件中，调用 repaymentService 的 startRepayment 方法。
画面13：展示 RepaymentController.java 文件中，返回 success 的响应。
画面14：展示还款流程图，包含“还款申请”、“还款中心”、“存管机构”、“已还款”、“存管系统”等模块，以及各模块间的交互流程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//1. 获取投标信息
List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
//2. 计算还款的月数
Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
Integer month = cell.intValue();
//3. 计算方式，只针对等额本息
String repaymentWay = projectDTO.getRepaymentWay();
if (repaymentWay.equals(RepaymentWayCode.FIXED_REPAYMENT.getCode())) {
    //4. 生成还款计划
    EqualInterestRepayment fixedRepayment = RepaymentUtil.fixedRepayment(projectDTO.getAmount(), projectDTO.getPeriod(), projectDTO.getRepaymentWay(), projectDTO.getInterestRate(), projectDTO.getCommissionRate());
    //5. 保存还款计划
    List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
    //6. 生成投资人应收明细
    for (TenderDTO tender : tenders) {
        EqualInterestRepayment receipt = RepaymentUtil.fixedRepayment(tender.getAmount(), tender.getProjectId(), projectDTO.getPeriod(), projectDTO.getRepaymentWay(), projectDTO.getInterestRate(), projectDTO.getCommissionRate());
        planList.forEach(plan -> {
            saveReceivablePlan(plan, receipt);
        });
    }
}
```
画面2：
```java
//保存还款计划
List<RepaymentPlan> repaymentPlanList = new ArrayList<>();
//获取每期利息
final Map<Integer, BigDecimal> interestMap = fixedRepayment.getInterestMap();
//获取每期手续费
final Map<Integer, BigDecimal> commissionMap = fixedRepayment.getCommissionMap();
fixedRepayment.getPrincipalMap().forEach((k, v) -> {
    final RepaymentPlan repaymentPlan = new RepaymentPlan();
    //标的id
    repaymentPlan.setProjectId(projectDTO.getId());
    //投标用户标识
    repaymentPlan.setConsumerId(projectDTO.getConsumerId());
    //投标用户编码
    repaymentPlan.setConsumerCode(projectDTO.getConsumerCode());
    //还款计划id
    repaymentPlan.setRepaymentId(projectDTO.getRepaymentId());
    //还款计划期数
    repaymentPlan.setNumberPeriods(k);
    //当期还款利息
    repaymentPlan.setInterest(interestMap.get(k));
    //当期还款本金
    repaymentPlan.setPrincipal(v);
    //还款计划状态
    repaymentPlan.setStatus(RepaymentPlanStatus.UNPAID.getCode());
    //还款计划类型
    repaymentPlan.setType(RepaymentPlanType.FIXED.getCode());
    //还款计划金额
    repaymentPlan.setAmount(repaymentPlan.getInterest().add(repaymentPlan.getPrincipal()));
    //还款计划创建时间
    repaymentPlan.setCreateTime(new Date());
    //还款计划更新时间
    repaymentPlan.setUpdateTime(new Date());
    //还款计划创建人
    repaymentPlan.setCreateBy("system");
    //还款计划更新人
    repaymentPlan.setUpdateBy("system");
    //还款计划备注
    repaymentPlan.setRemark("系统生成");
    //还款计划状态
    repaymentPlan.setStatus(RepaymentPlanStatus.UNPAID.getCode());
    //还款计划类型
    repaymentPlan.setType(RepaymentPlanType.FIXED.getCode());
    //还款计划金额
    repaymentPlan.setAmount(repaymentPlan.getInterest().add(repaymentPlan.getPrincipal()));
    //还款计划创建时间
    repaymentPlan.setCreateTime(new Date());
    //还款计划更新时间
    repaymentPlan.setUpdateTime(new Date());
    //还款计划创建人
    repaymentPlan.setCreateBy("system");
    //还款计划更新人
    repaymentPlan.setUpdateBy("system");
    //还款计划备注
    repaymentPlan.setRemark("系统生成");
    //还款计划状态
    repaymentPlan.setStatus(RepaymentPlanStatus.UNPAID.getCode());
    //还款计划类型
    repaymentPlan.setType(RepaymentPlanType.FIXED.getCode());
    //还款计划金额
    repaymentPlan.setAmount(repaymentPlan.getInterest().add(repaymentPlan.getPrincipal()));
    //还款计划创建时间
    repaymentPlan.setCreateTime(new Date());
    //还款计划更新时间
    repaymentPlan.setUpdateTime(new Date());
    //还款计划创建人
    repaymentPlan.setCreateBy("system");
    //还款计划更新人
    repaymentPlan.setUpdateBy("system");
    //还款计划备注
    repaymentPlan.setRemark("系统生成");
    //还款计划状态
    repaymentPlan.setStatus(RepaymentPlanStatus.UNPAID.getCode());
    //还款计划类型
    repaymentPlan.setType(RepaymentPlanType.FIXED.getCode());
    //还款计划金额
    repaymentPlan.setAmount(repaymentPlan.getInterest().add(repaymentPlan.getPrincipal()));
    //还款计划创建时间
    repaymentPlan.setCreateTime(new Date());
    //还款计划更新时间
    repaymentPlan.setUpdateTime(new Date());
    //还款计划创建人
    repaymentPlan.setCreateBy("system");
    //还款计划更新人
    repaymentPlan.setUpdateBy("system");
    //还款计划备注
    repaymentPlan.setRemark("系统生成");
    //还款计划状态
    repaymentPlan.setStatus(RepaymentPlanStatus.UNPAID.getCode());
    //还款计划类型
    repaymentPlan.setType(RepaymentPlanType.FIXED.getCode());
    //还款计划金额
    repaymentPlan.setAmount(repaymentPlan.getInterest().add(repaymentPlan.getPrincipal()));
    //还款计划创建时间
    repaymentPlan.setCreateTime(new Date());
    //还款计划更新时间
    repaymentPlan.setUpdateTime(new Date());
    //还款计划创建人
    repaymentPlan.setCreateBy("system");
    //还款计划更新人
    repaymentPlan.setUpdateBy("system");
    //还款计划备注
    repaymentPlan.setRemark("系统生成");
    //还款计划状态
    repaymentPlan.setStatus(RepaymentPlanStatus.UNPAID.getCode());
    //还款计划类型
    repaymentPlan.setType(RepaymentPlanType.FIXED.getCode());
    //还款计划金额
    repaymentPlan.setAmount(repaymentPlan.getInterest().add(repaymentPlan.getPrincipal()));
    //还款计划创建时间
    repaymentPlan.setCreateTime(new Date());
    //还款计划更新时间
    repaymentPlan.setUpdateTime(new Date());
    //还款计划创建人
    repaymentPlan.setCreateBy("system");
    //还款计划更新人
    repaymentPlan.setUpdateBy("system");
    //还款计划备注
    repaymentPlan.setRemark("系统生成");
    //还款计划状态
    repaymentPlan.setStatus(RepaymentPlanStatus.UNPAID.getCode());
    //还款计划类型
    repaymentPlan.setType(RepaymentPlanType.FIXED.getCode());
    //还款计划金额
    repaymentPlan.setAmount(repaymentPlan.getInterest().add(repaymentPlan.getPrincipal()));
    //还款计划创建时间
    repaymentPlan.setCreateTime(new Date());
    //还款计划更新时间
    repaymentPlan.setUpdateTime(new Date());
    //还款计划创建人
    repaymentPlan.setCreateBy("system");
    //还款计划更新人
    repaymentPlan.setUpdateBy("system");
    //还款计划备注
    repaymentPlan.setRemark("系统生成");
    //还款计划状态
    repaymentPlan.setStatus(RepaymentPlanStatus.UNPAID.getCode());
    //还款

