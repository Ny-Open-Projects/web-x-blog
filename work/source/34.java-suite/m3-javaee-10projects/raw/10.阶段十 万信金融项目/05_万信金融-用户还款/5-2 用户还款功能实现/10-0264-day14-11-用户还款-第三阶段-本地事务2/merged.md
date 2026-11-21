# day14-11-用户还款-第三阶段-本地事务2

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-11-用户还款-第三阶段-本地事务2_【海量资源尽在 666java.com】.mp4
- 时长 12分39秒（音频 759s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来咱搞定第二块这个功能第二个功能呢是要更新这个表对吧receive plan这个表把它里边那个状态改成什么呀一收那这个表的数据咱从哪来咱是不是得先得到数据然后再进行什么呀更新对吧就是说我要查一查查一查本次还款相关的这个什么呀这这个应收计划这个数据
[00:26] 我们相关联的数据我们得先查出来啊因为receiver plan这个表里边数据也很多呀是不是将来我们这个呃各个投资人对吧各个用户他所相关的这个应收明细这些数据全部在这一个表里边啊全部在这一个表里边那我们本次要更新的是哪些数据呢我们得查出来那这个怎么查呀这个我们看我们可以根据这个呃我们这个可以根据主见啊但是主见咱现在得不到啊
[00:56] 咱们手头上没有这个值我们手头上有哪个值呢我们手上有这个值还款计划的这个表示哎我们正好是不是应该是呃查出来跟这个还款计划相关的这个receivable什么呀plan而咱手头上呢这个值正好是可以找到的啊从那一参数里边就可以找到所以咱接下来的话要先做的事情就是根据还款什么呀对计划ad
[01:28] 查询什么呀对查询应收计划一个查询那咱进来写一写那应该用哪个Mapper接口呢自然就是receivablereceivable planMapper对我们查的是这个表然后呢我们就需要调用它的一个方法这有可能查出来多少数据我们应该是slack的什么list然后这里边是不是封装条件就行了
[02:01] 这里边我们怎么写还是WARPSWARPS.Lambda query对吧我们的条件就是EQ哪个字段呢刚才我们说了是不是那个什么呀那个那个那个那个什么还款计划的ID对不对那就是receivable plan它的哪个值应该是我找找应该是那个应收计划的ID在哪里这个
[02:35] 然后值啊值就是从第一个参数里边取出来的这不是英这不是那个还款计划我们做从这里边就能取出来点给他一这是我们的这个什么呀对查询条件然后我们这个地方还缺一个什么呀范形我给他加进来啊啊这不报错了然后他反过来是不是一个集合呀那我们在这需要接收一下
[03:10] 我们起个名字就叫啥呢就叫receive plan list然后呢这里边是不是还需要设置这个范形这是我们把需要更新的数据是不是先查出来了就是一个集合这个集合里边的这个数据就是要把这个状态改成什么呀已收到那你接下来是不是应该循环便利一个进行什么呀更新对吧所以说我们接下来呢要便利这个什么呀集合点
[03:53] for什么呀for一起啊那更新怎么更新呢这不是每个对象吗我们直接调他的setter方法啊他的setter方法我们要改谁呀改那个状态应该是这个状态对吧我们把它改成什么一这就是已收那然后呢我们就要调map接口的什么方法呀对update by什么id然后把这个什么呀receive plan这个对象把它放进去
[04:28] 这就完成了哪个更新啊对这个更新啊这一步我们就搞定了大家看一下我们首先是把需要更新的数据啊通过这个换换计划的ID进行关联查询查出来之后呢我们循环便利然后呢把里边每个对象的这个状态呢都进行了这个更新那这个更新的同时大家注意我们说了我们是不是还需要往这个什么呀receive detail这个表里边这个是应收明细对不对
[04:58] 需要往这个表里边来开始保存数据了那接下来这个代码就是我们是不是要new这个表对应的这个实体类对象然后呢给这些字段复职复完职之后呢DLMAPR接口是不是就可以进行保存了那咱接下来把这块代码写这块代码是不是得放到循环里边啊对吗你想想是不是有几个plan就应该对应有几个什么呀detail吗是不是它们是有对应关系的啊一个计划对应一个什么样明细
[05:27] 所以我们应该放到这个什么循环里边将来有几个plan我这边就保存几个什么对detail所以说这个需要大家注意接下来这个保存的话这个代码我就不再给大家写了这个比较简单我们刚才说了你看是不是又开始遇对象对不对然后呢掉塞的方法把需要给的值都给了然后掉什么呀map接口我们就搞定了这个什么呀保存我让大家过一遍
[05:57] 你看这是不是直接拗对象对不对我们说构造应受明细这个对象嘛然后呢开始给他复制刚才大家看到这个表里边其实没几个数据对吧三四个啊你看这是什么呀receiveable的id这个id呢我们用的你看这是谁呀对那个plan的id对不对他俩我刚才说的是有一对一的这个关联关系然后本息本息的话就是从这个plan里边就能取到啊时间的话这个就是当前时间呗然后呢这个什么呀
[06:25] 接下来就可以干什么呀保存了我们就可以调用这个map接口对不对这个接口是不是还不存在啊是不是还不存在我们有没有提供这个map接口啊那应该还没有因为这个表咱从来没有干什么呀操作过是不是你看这里边哎有了在这repayment detail是不是这个什么呀map那我们就可以把它给注入进来嘛我们看上面是不是没注入啊啊这是repayment detail
[06:56] 我们缺一个receival detail是不是那没有啊没有我们需要把它给创建出来这个创建这个数据访问层的接口对于大家来说应该是非常简单的一个事那我们起个名字叫ICIVABLE对吧然后DETAILMAPP然后呢我们需要让它继承是不是my belly plus的这个什么呀
[07:27] BaseMapperBaseMapper啊然后这个范形的话那不用说就是Receive什么呀Detail然后这个实体类是吧哎哎倒进来了倒进来了啊这个反应有点慢然后呢我们这加个注视这个就是操作什么表啊哎我们看看操作这个表得什么呀Mapper接口
[08:05] 然后光接口还不行我们是不是需要提供一个这个什么映射配置文件这个更简单了我们直接NEO出来就行了这个名字的话我们应该是对照这儿去写那还是阿姨CIVABLEDTAIL然后呢MAPP好然后这儿呢是不是要导一下那个接口这个接口应该是叫
[08:39] 啊啊一c icnd i cast 点应该是repayment 对吧点map在地儿对吧搞定这是数据房子你有然后呢我们在这是不是就可以把它注入进来了private d t a啊receivable i e c receivable什么呀detail map 是吧
[09:16] 有了这个之后接下来这一块这个保存它就简单了我们找一找刚才这个代码在这是不是你看这就不做错我们就可以调insert方法往这个表里边干什么呀对保存数据那这是哪一步啊第二步我们就全部搞定了接下来呢我们整这个第三步这是多一对果号然后咱接下来就实现最后一个更新是更新什么呀
[09:48] 还款计划为以还款那这个是不是应该这里边最简单的一个啊呃那这个还款计划不就是这个第一个参与对象吗我们接下来呢就调用这个对象的setter方法我们应该是改哪个状态叫repayment status应该就是他了啊给他改成什么1就行了对然后呢我们就调用这个谁啊接口repayment
[10:16] repayment应该是什么呀plan map是吧repayment没有吗我往上面瞅一瞅啊repayment哎还真是没有啊没有那我们需要注入进来repayment啊repayment plan啊plan那我们应该是不叫repayment plan了你看我们以前这起的是什么呀plan map啊导入过了我这个呢名字的问题啊
[11:03] 那我们这呢都不需要倒了我们这应该就是那 plan map然后第二update是吧掉update by d by然后呢把这个什么呀这个对象给他扔进去这事就搞定了搞定完之后呢你看大家看我们说这个方法它是有一个返回值对不对那我这怎么返回出force呢那你这就可以接收一下这个受影响的行数嘛对不对
[11:33] 他会返回这么一个值然后呢我在这就可以returnrws大于0哎大家看一下这个能看到吗i1t1对不对那如果他这个真的更新数据成功的话他的数据一定是什么呀这个值一定是大于0了所以他就戳服了就sus了呃这是咱把第三个这个更新搞定那这个搞定之后咱这个方案就编写完了最后千万不要忘了一点非常非常重要的
[12:05] 我们说呢整个这一块是不是咱的一个本地事务是不是本地事务你看这那对于这三个更新啊就是这几个数据库操作来说他们应该是不是一个本地事务对吧那所以说呢你应该在这个方案上应该还要加一个注解哪个注解对这个事务注解这个大家千万不要忘记了啊非常非常重要那这是咱相当于是把哪一块搞定了呀
[12:31] 对这个图当中就是2.2嘛然后呢这个图当中是不是就是4对不对

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在还款服务中，通过代码逻辑更新还款计划状态并持久化对应的还款明细。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `RepaymentServiceImpl.java` 中 `confirmRepayment` 方法的代码，重点是更新 `receivable_plan` 表的状态为“已还款”。
画面2：在 `confirmRepayment` 方法中，通过 `receivablePlanMapper.selectList(...)` 查询与还款请求关联的还款计划列表。
画面3：在 `confirmRepayment` 方法中，通过 `receivablePlanMapper.selectList(...)` 查询与还款请求关联的还款计划列表。
画面4：在 `confirmRepayment` 方法中，通过 `receivablePlanMapper.selectList(...)` 查询与还款请求关联的还款计划列表。
画面5：在 `confirmRepayment` 方法中，通过 `receivablePlanMapper.selectList(...)` 查询与还款请求关联的还款计划列表。
画面6：在 `confirmRepayment` 方法中，创建 `ReceivableDetail` 对象并设置其属性，然后调用 `receivableDetailMapper.insert(...)` 插入数据。
画面7：展示 `ReceivableDetailMapper.java` 文件，该文件是 MyBatis 的 Mapper 接口，继承自 `BaseMapper<ReceivableDetail>`。
画面8：展示 `RepaymentServiceImpl.java` 文件中 `startRepayment` 方法的代码，用于生成还款计划。
画面9：展示 `RepaymentServiceImpl.java` 文件中 `confirmRepayment` 方法的代码，重点是创建 `ReceivableDetail` 对象并插入数据库。
画面10：在 `confirmRepayment` 方法中，通过 `receivablePlan.setAmount(...)` 设置还款计划金额。
画面11：在 `confirmRepayment` 方法中，通过 `receivablePlan.setConsumerId(...)` 设置还款计划的消费者ID。
画面12：在 `confirmRepayment` 方法中，通过 `receivablePlan.setProjectId(...)` 设置还款计划的项目ID。
画面13：在 `confirmRepayment` 方法中，通过 `receivablePlan.setShouldRepaymentDate(...)` 设置还款计划的应还款日期。
画面14：展示一个流程图，描述了还款处理的完整流程，包括接收请求、更新交易记录、生成还款计划、插入还款明细等步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//2.1 更新receivable_plan表为：已收
receivablePlanMapper.update(entity: null, Wrappers.<RepaymentDetail>lambdaUpdate().set(RepaymentDetail::getStatus, StatusCode.STATUS_IN.getCode()));
```

画面2：
```java
//2.1 更新receivable_plan表为：已收
//根据还款计划id.查询应收计划
receivablePlanMapper.selectList(Wrappers.<ReceivablePlan>lambdaQuery().eq(ReceivablePlan::getRepaymentNo, preRequestNo));
```

画面3：
```java
//2.1 更新receivable_plan表为：已收
//根据还款计划id.查询应收计划
receivablePlanMapper.selectList(Wrappers.<ReceivablePlan>lambdaQuery().eq(ReceivablePlan::getRepaymentNo, preRequestNo));
```

画面4：
```java
//2.1 更新receivable_plan表为：已收
//根据还款计划id.查询应收计划
receivablePlanMapper.selectList(Wrappers.<ReceivablePlan>lambdaQuery().eq(ReceivablePlan::getRepaymentNo, preRequestNo));
```

画面5：
```java
//2.1 更新receivable_plan表为：已收
//根据还款计划id.查询应收计划
receivablePlanMapper.selectList(Wrappers.<ReceivablePlan>lambdaQuery().eq(ReceivablePlan::getRepaymentNo, preRequestNo));
```

画面6：
```java
//2.3 等存款数据到receivable_detail
//创建应收明细
ReceivableDetail receivableDetail = new ReceivableDetail();
//空值标识
receivableDetail.setReceivableId(receivablePlan.getId());
//实收金额
receivableDetail.setAmount(receivablePlan.getAmount());
//实收时间
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面7：
```java
package cn.ictast.wanxingzp.repayment.Mapper;

import cn.ictast.wanxingzp.repayment.entity.ReceivableDetail;
import com.baomidou.mybatisplus.core.Mapper.BaseMapper;

/**
 * @author
 */
public interface ReceivableDetailMapper extends BaseMapper<ReceivableDetail> {

}
```

画面8：
```java
private ReceivablePlanMapper receivablePlanMapper;
private RepaymentDetailMapper repaymentDetailMapper;
private DepositoryAgentApiAgent depositoryAgentApiAgent;

@Transactional(rollbackFor = BusinessException.class)
public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
    //2.1 生成借款人还款计划
    //2.2 获取还款计划的信息
    ProjectDTO projectDTO = projectWithTendersDTO.getProject();
    //2.3 获取投标信息
    List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
```

画面9：
```java
//2.3 等存款数据到receivable_detail
//创建应收明细
ReceivableDetail receivableDetail = new ReceivableDetail();
//空值标识
receivableDetail.setReceivableId(receivablePlan.getId());
//实收金额
receivableDetail.setAmount(receivablePlan.getAmount());
//实收时间
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面10：
```java
//2.3 等存款数据到receivable_detail
//创建应收明细
ReceivableDetail receivableDetail = new ReceivableDetail();
//空值标识
receivableDetail.setReceivableId(receivablePlan.getId());
//实收金额
receivableDetail.setAmount(receivablePlan.getAmount());
//实收时间
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面11：
```java
//2.3 等存款数据到receivable_detail
//创建应收明细
ReceivableDetail receivableDetail = new ReceivableDetail();
//空值标识
receivableDetail.setReceivableId(receivablePlan.getId());
//实收金额
receivableDetail.setAmount(receivablePlan.getAmount());
//实收时间
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面12：
```java
//2.3 等存款数据到receivable_detail
//创建应收明细
ReceivableDetail receivableDetail = new ReceivableDetail();
//空值标识
receivableDetail.setReceivableId(receivablePlan.getId());
//实收金额
receivableDetail.setAmount(receivablePlan.getAmount());
//实收时间
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面13：
```java
//2.3 等存款数据到receivable_detail
//创建应收明细
ReceivableDetail receivableDetail = new ReceivableDetail();
//空值标识
receivableDetail.setReceivableId(receivablePlan.getId());
//实收金额
receivableDetail.setAmount(receivablePlan.getAmount());
//实收时间
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面14：
无代码或配置，为流程图。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
流程图标题：用户还款计划处理流程图。
流程图结构：
- 起始节点：用户发起还款请求。
- 步骤1.6：发送处理请求，调用接口。
- 步骤1.7：压线还款金额。
- 步骤1.8：原交易成功。
- 步骤2.1：发送确认还款事务消息。
- 步骤2.2：默认还款处理。
- 步骤2.3：处理确认还款请求。
- 步骤2.4：更新交易记录，状态为“已同步”。
- 步骤2.5：根据还款计划生成签名及摘要。
- 步骤2.6：更新还款交易信息为“已还款”。
- 步骤3.1：更新交易记录，状态为“已同步”。
- 步骤3.2：更新还款计划，状态为“已还款”。
- 步骤3.3：更新还款明细，状态为“已还款”。
- 步骤3.4：更新还款计划，状态为“已还款”。
- 步骤3.5：更新还款明细，状态为“已还款”。
- 步骤3.6：更新还款计划，状态为“已还款”。
-

