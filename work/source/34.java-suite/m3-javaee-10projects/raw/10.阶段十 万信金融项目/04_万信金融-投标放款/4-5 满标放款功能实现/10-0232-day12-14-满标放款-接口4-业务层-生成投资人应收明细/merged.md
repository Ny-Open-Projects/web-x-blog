# day12-14-满标放款-接口4-业务层-生成投资人应收明细

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-14-满标放款-接口4-业务层-生成投资人应收明细_【海量资源尽在 666java.com】.mp4
- 时长 20分10秒（音频 1210s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把生成借款人还款计划整个这块功能呢全部搞定了那接下来咱该实现第二块功能就是生成投资人的应收明细那这块代码的话我们也可以拆成两小块第一小块呢就是我们就是根据什么呀投标信息生成应收明细
[00:30] 这块大家注意啊应收明细是不是针对投资人呢就是每个投资人呢这个在满标之后他都应该能有一份什么呀手里边都应该有一份什么呀经收明细他要看看他这个这个将来对吧我一共会赚多少钱吗对不对这个每个月他能这个收回来这个本金有多少利息有多少对吧等等这些信息他也要这个能看到这样一个东西出来啊所以说我们是根据投标信息
[00:59] 去生成这个什么呀应收明细的然后呢第二块小功能就是我们需要干什么呀我们需要保存应收明细到数据库中这个东西呢它也得保存在数据库里边那大家想啊我如果是投资人的话我投了一个标买标之后呢我随时都有可能登录这个什么呀前端对然后查一查这个什么呀应收明细就我们刚才说了我都能收多少利息啊这个
[01:30] 每个月能收多少本金收多少利息等等所有的信息他得能查呀是不是随时都能查所以说这个应收明细呢我们在第一步生成之后呢还是需要把它保存到数据库里边所以说呢第二块功能呢我们整体把它拆分成这两小块啊这是需要大家注意的然后咱既然就开始编码一块一块实现功能那这个代码呢我不能写到这儿啊不能写到这儿我们得放到这个衣服里啊放到这儿往这里边去写
[02:01] 放在这儿啊这个大家一定要注意那咱先实现第一个功能吧就是根据投标信息去生成这个什么呀应收名系我们刚才说了应该是每个投资人都要生成一个什么呀应收名系那我带一个问题如果一个标底有十个人投标然后满标了那我们就应该生成几个人的这个应收名系啊几个人十个人对吧我刚才说有十个人
[02:32] 去投标了吗就有10个投资人吗然后每个投资人是不是都应该有一个应收明细所以说呢我们这儿你要是有10个投资人这儿就应该生成10个什么呀应收明细对不对所以说呢这儿明显是一个一个什么呀循环吧对不对我说一个投资人就有一个应收明细嘛而一般一个标的往往都是什么呀有多个什么呀对投资人呢那咱这个投资人在哪
[03:01] 投资人咱看看上边不就是这么吞袋子吗对不对是他不是你看我们这这个参数里边是不是有一个这个属性就是tenders你看我们可以进去再看一遍是不是投标记录吗对吧跟投标相关所有的数据全部封装到tender DTO里边然后呢再封装到什么list集合里面所以说这个tenders就是包含了所有的投标信息里边就有所有的什么呀对投资人所以说我们在生成这个应收明细的时候呢它本身应该是一个循环
[03:34] 那我们这个代码就应该这么写啊使用这个谁啊tenders对吧这个集合然后对它进行什么呀便利嗯然后我先把这个栏目表是先写出来是这个样子吧对不对那这就是表示要对这个集合进行便利啊这集合里边有10个投资人我就循环几次10次然后生成几条应收明线对10条应收明线啊所以说这块大家一定要搞清楚那这个应收明线到底怎么生成呢怎么生成呢大家注意看这
[04:08] 前面我们在生成还款计划的时候是调用了一个工具类叫repayment youtube调用它里边的一个方法叫fixed repayment有印象吧是不是它里边传了一些参数对不对那我们现在在实现这个什么呀生成应收明细的时候其实还是调用这个工具类的这个方法有的同学会说那老是不应该啊对不对这个是生成还款计划了你这是生成应收明细的这功能都不一样你怎么能调用同一个方法
[04:37] 那这个地方大家想一想啊你想想这个还款计划和应收明细是不是差不多你看借款人还的这个东西不就是投资人收的东西你明白什么意思吧借款人每个月还了多少钱不就是投资人每个月应收多少钱了咱前面其实一开始在给大家介绍这个还款计划和应收明细的时候就说过其实还款计划和应收明细它里边有好多这个数据都是什么呀
[05:09] 都是一样的啊其实都是一个东西一样的啊只不过是站在不同的角度吗你站在这个借款人的角度他就是还款计划你站在投资人的角度他就是什么呀应收明细但实际上他里边好多数据都是什么呀一样的啊一样的所以说呢我们在生成这个应收明细的时候呢还是掉了这个方法但是传进来的数据肯定就不太一样了啊不太一样
[05:34] 你不管是还款计划还是这个应收明细它是不是都是针对那个叫等额本息的这个算法吗是不是来生成的所以我们调的方法肯定是一样但是传的数据是不一样的刚才说了你这边你看你这传的这些数据它就是生成还款计划那一会儿你看看我们要想生成这个应收明细虽然调的方法是同一个方法但是传进来数据你看看它肯定是不一样的这我们这应该怎么写呢我们这就要这么字来写了直接就是
[06:04] repayment youtube直接调这个方法啊fixedrepayment那我们接下来传的数据跟这个生成还款计划是不一样的啊我们都要传啥呢第一个参数大家还有印象吗第一个参数呢是那个金额对不对那我们这呢应该传进来的是投标金额我们要生成投资人的应收明细就跟他的什么投标金额有关举个例子你投的越多理论来讲是不是挣的应该越多
[06:35] 明白什么意思吗所以这呢传进来的是投标的金额投标金额怎么得到是不是掉了这个给的方法对不对这就是投标金额然后接下来还有什么东西啊好那个利率对不对那个利率利率应该是找找啊应该就是这个啊应该就是这个利率那是什么意思的话你要是忘了的话我们可以去tender dto里边瞅一瞅
[07:08] tnd呀对吧dtdto对不对tender dto我们可以看看啊就这年利率嘛就是他啊呃然后呢第三个参数是啥第三个参数就是这个七数七数就是你借给人家这个钱借多长时间吗借12个月6个月对不对多长时间其实这个还是前面这个值就这个月数在哪在这
[07:44] 他借12个月借12个月就是这个是借款人他要借钱借多少时间借12个月那你不就是投投资投多少时间投12个月对不对其实值是一样的值是一样的然后还有最后一个参数最后一个参数就是那个平台佣金平台佣金的话我们是从这个参数里边来取的get commission对不对就这个值平台佣金
[08:15] 所以你会发现你看你这对比一下这个方法这个方法调的方法都是一样但里边传的数据是不一样的啊不一样那然后呢呃我们说了这是一个循环嘛那么那么他生成的这个应收明细应该是什么呀对应该是多个的那不管几个吧他生成一个我们是不是要接收对不对所以我这边呢应该要干什么呀要接收一下啊是不是还是这个数据类型吗反正这还是这个数据类型啊
[08:45] 然后呢我们起个名字就有阿姨阿姨起个啥名CEIPT吧接受一下啊那我拿一个问题如果这个投资人有10个人那这个循环就会进行10次那这个方案就掉10次然后最终会生成10个什么呀对应收明细啊我们在学校过程当中都存到这个变量里边了所以说这个功能在目前就实现了啊就是生成每个投标人
[09:17] 对吧每个投资人吧他的这个是每个银声明信那接下来咱就要实现这个功能那这个功能是不是你看是不是应该放到这个循环里边大家想想是不是因为你看你十个投资人那他就会生成十个银声明信你应该是生成一个保存到数据库里边生成一个再保存到什么呀数据库里边是这意思吧对不对所以说这个代码也应该放到这个循环里边生成一个明信我就保存一个明信生成一个银声明信我就保存一个银声明信
[09:47] 那这块的话我们跟这个生成还款计划一样吧你看生成还款计划的时候呃生成完之后我们保存对吧保存的时候是单独抽取出来一个方法那我们这跟他保持一致吧我们也单独抽取出来一个方法来实现保存这个什么呀应收明细到数据库这个保存功能其实也很简单就跟这是一样的啊你就是你有一个什么样一个对象然后通过塞着方法给他的属性复制然后呢调麦粉接口进行保存就行了
[10:16] 那他就是代码比较麻烦因为他的这个字段化属性比较多啊大家看一下我们这个应收明线应该保存到这个表里这个表receivable 对吧plan你看一下是不是你看这边投标人的信息对吧啊期数啊对吧应收的利息本金本息时间状态创建时间年化利率等等等等我们说吧就是往这个表里边什么呀对保存数据
[10:46] 那跟这个表肯定相对应的是不是有一个谁呀实体类我们要做的事就是你有一个实体类调用赛转方法给这一堆东西干什么呀自断啊复职复安职之后调没法接口哎保存完事那这块的话我们就看看这个讲义吧看这啊看这你看他是单独抽取出来一个方法叫save receivable plan对不对就是保存一个名气到什么呀数据库然后你看这里边是不是干什么呀你看这里边在这
[11:16] 我是不是new这个实体内码receivable plan这个实体内然后下面就是调用他的setter方法开始往里边干什么复制复安值之后啊到最后就调mehre解口什么方法insert法就进行保存我这个代码的话我就不再给大家编写了我们拿过来一起看一下就行了就他没有啥难度就是比较麻烦啊因为字段比较多嘛那我就放到这了对不对嗯还有一部分啊还有这一块
[11:53] 大家再下去你在编写这块代码的时候你就对照这个实体类对照那个或者表的表里边那个字段就可以了那咱把整个这块过一遍吧看一下啊呃首先呢这个这是发明对吧然后我们看传进来几个参数啊三个参数啊第一个参数你看啊这叫repayment planrepayment plan是啥repayment plan你往上找找repayment plan是不是它是不是我们上面生成的这个什么还款计划
[12:26] 那里面的数据我们最终是不是放到这个集合里面我们当时在生成这个保存这个环环计划的时候就说了嘛他返回一个集合的目的就是因为我们在下面这个地方就是生成这个投资人应收明细的时候是不是要用嘛对不对这是一个参数啊然后就是这个什么呀对投标信息嘛他的DTO然后这个就是生成的那个什么呀对应收明细吧就在这2.1嘛刚生成的这个应收明细我们刚才说了嘛生成一个保存一个生成一个保存一个
[12:58] 所以说你看我们这个单独出取出来的这个方法呢我们是一共设计了几个参数呀对三个参数啊这是需要大家注意的然后咱看里边的代码它跟前面那个保存什么呀保存这个什么呀保存款款计划这个套路基本上是一模一样的来一起看一看你看它一开始是先得到了一些什么信息呀本金的信息对不对从这个什么呀从这个生成的应收明细里边
[13:29] 来获取一下应收多少本金啊应收多少利息啊还有这个什么呀这是啥这是平台的佣金吗这些基本信息他先从这个什么呀应收明细里边先获取到获取到之后呢然后继续他就要干什么呀没有这个什么呀receive plan这个对象我们看看你看这个类他对应的其实就我们刚才说的这个表啊然后你看这里边每个属性
[13:58] 是不是有对应这个表里边的每个什么呀不断啊这个你下次自己过一遍就行了就利用这个对象利用对象之后就开始调用这个对象的一堆什么呀setter方法往里边复制嘛比如说这个投标人的ID对吧这个什么呀七数还有什么呀投标人的用用户标识consumer ID还有这个什么呀用户编码对吧还有这个这个这个谁呀缓缓计划的那个标识缓缓计划
[14:29] repayment plan就是他那也就是说呢大家要知道这个应收明细其实跟还款计划是不是有对应关系是不是哪个人借的钱哪个人借给他钱的他俩之间是不是有对应关系嘛就是我刚才说的借款人每个月还多少钱对应的就是投资人每个月应收多少钱是不是他有对应关系的所以他这边会保存一下这个什么呀保存一下还款这个计划的这个ID
[14:58] 就这个主件还有就是价就是封装这个上面我们得到这个什么呀利息本金这些信息开始掉塞的方向里边存了你看利息本金还有本息和对不对注意这是big decimal类型的啊不能用加号直接进行加号运算要用ADD方法时间对不对还有什么呀然后这个状态状态默认都是什么呀未收状态一开始都是未收将来收到钱的话再改嘛然后创建的时间还有这个什么呀对佣金
[15:30] 然后该给的值全部都给完之后我们就可以调用map接口的什么方法对insert的方法来实现保存那这个接口我们前面已经定义过了但是这儿是不是还没有注入进来对不对说那咱接下来的话回到最上面在这儿好我们要注入一下private叫啥名啊reci应该是这个对吧receivable plan Mapper
[16:06] 把它注进来注进来之后呢下面这个地方应该就不报错了对不对所以你看这儿就是我们单独封装出来一个方法啊就是把这个应收明细给它保存到什么呀数据库里边具体来说就是保存到这个表里边这时候大家要注意那这个发定好之后我们是不是就要在这调用一下对不对在这调用一下叫save什么呀restable plan一共有几个参数啊三个参数第一个参数是不是证明那个还款计划对吧
[16:36] 那个缓缓计划那个对象在哪是不是在这嘛对不对所以我们这应该要进行遍地的啊就是plan list there什么呀对for each啊这样呢就是怎么写plan对我们应该这么子来写把它呢放到这里边啊因为我刚才说了嘛我们在生成或者保存这个营收明细的时候它是不是要用到之前的这个什么呀缓缓计划这个信息啊就这个集合
[17:10] 要用它里边的你看刚才你看他是不是用到他的这个ID了吗是不是你看啊你看啊不仅是用的ID还用到他的什么呀期税啊利息啊本金对吧好多信息他都需要使用的所以我们在这呢要循环他把每一个这个环环计划的对象传进来然后还需要啥这还需要这个什么呀Tender DTO还需要啥还需要就是
[17:41] 上面生成的这个什么应收明细大家看对不对是吧我们应该这么写啊保存应收明细到最后应该这么写啊我们单独抽了一个方法但你在调这个方法的时候呢需要放到这个循环里边因为它里边要用到这个什么还款计划这个对象所以说这是需要也是需要大家注意的一个细节吧那到目前为止吧咱就把第二大块功能就是生成投资人应收明细并保存到什么呀
[18:12] 数据库里边这个功能反应搞定搞定完之后呢最后这我们还要完善一下就这个地方这个地方可不能return到啊对不对如果上面代码在执行过程当中都没有出问题的话我们这是不是应该返回成功对不对返回成功怎么怎么返回啊返回个什么值呢返回什么值我们以前大家应该有印象我们以前成功是不是用五个零秒似的大家有印象吧对你这可以写五个零当然这呢我们要给大家简单说一说就是
[18:44] 有的会讲老师我想返回一个零我想返回一个success我想返回一个yes我想返回一个ok行吗可以但是呢你在企业当中这个开发的时候呢你们应该要进行什么统一啊比如在这个项目当中成功就用五个零秒是或者成功就用什么ok表示你们要整个项目要进行什么统一啊而我们根据咱们这个项目以往的这个前面这个代码咱们成功一般是不是都是用五个零秒是的对不对所以你这可以直接写五个零
[19:13] 或者说你也可以去咱们之前有个地方是定义的有个有那个成量值就是那个美剧吧美剧应该是应该是deposit return code里边我记得啊你看是不是这个对不对五个两啊你用他也行这样给他扣的方法其实你这样给他扣的话最终得到还是那五个零啊所以说你可以用这个值也可以直接像我刚才一样直接写双一号里边写什么呀写什么五个零都行啊但是我还还是我刚才给大家说的你在前端开发的时候像这种
[19:43] 数据你应该是整个项目要进行什么统一的你五个零也行yes也行ok也行success也行就是一定要进行什么统一那这块咱完善了之后呢咱们整个什么功能就全部搞定了大家看看咱这个流程图在这个图当中呢我们是哪个接口四对不对就生成缓缓计划还有营生明细整个这块功能就全部搞定

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

