# day11-8-用户投标-功能实现7

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-8-用户投标-功能实现7_【海量资源尽在 666java.com】.mp4
- 时长 11分31秒（音频 691s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们把3.2和3.3的功能全部搞定了接下来给3.43.4我们说了要转换成什么呀把这个tender对吧转换成dt对象然后再封装一些数据就行了那转换成dt对象这个对于大家来说不陌生了我们以前经常干这个事我们是不是要写一个方法对不对就这个方法convert tender entity to dt这里边代码跟咱之前见过一模一样我就不再跟大家说了我直接粘过来拿来用这个事情咱以前
[00:29] 做了好几次了对不对我这已经粘过了对不对粘过了咱在这拿着直接用呗就在这吧我就可以把这个前面的这个tender这个实体的对象是不是就给他扔进去扔进去之后呢出来的就是谁呀tender DTO对象先收一下这个DTO对象就有了有了之后呢我们还需要再往里边封装两块这个数据一块是标底相关的一块是这个什么呀预期收益对不对
[01:01] 那咱先封装这个什么呀标底相关的这个信息吧标底相关的信息呢我们主要是要它一个什么东西啊呃我们得去一个地方找一找去哪去projectproject的这个实体类当中我们给大家说一说我们需要整个什么东西啊你找一找就这个因为我们现在已经这个投投标了吧投标完之后呢我们要啊这个封装一个数据就是还款方式
[01:33] 我们要把这个给它封装到DTO对象里面返回那我们准备用哪种还款方式呢接下来大家看一看啊我首先就是要掉project因为是属于它里边的一个属性嘛叫setrepaymentway对吧还款方式这还款方式呢也是字不刷但是不能我们随便乱写我们也是封装好的这个美举啊我们给大家找一找叫repayment我看有没有这个啊
[02:03] repaymentvcode哎呦在这点点什么呢我们要点的是这个这个等额本息这个我们之前是不是在在一开始那时候给大家介绍过吗我们这个p2p项目里边默认的还款方式就是什么呀等额本息目前我们只针对这种情况做处理所以你就选这个值就行了等额本息这个我们是得在这进行一个什么呀封框的
[02:36] 这是我们往project里边是不是放了一个又新增了一个值对吧增加完这个值之后呢我们需要把这个什么呀整个project这个对象呢给它存到DTO对象里边要封装一下咋封装呢你看这里边有个方法叫set什么呀project我们把整个这个project对象给它存进去就行了但你看人家要的是什么project DTO啊而我这的project可不是DTO类型那怎么办那还得做转换
[03:07] 还得做转换啊那这个转换的方案咱以前都写过了咱直接调用了就是convert project entity什么呀to DTO就咱以前都写过用过把它把这个project的对象扔进去就行了啊把project的对象扔给他返回来是DTO对象啊然后呢再把DTO对象封装到这个什么呀tender里边那咱们封装标的信息这一步就搞定了这里边主要是多了一个缓缓方式咱需要设计一下啊
[03:36] 那最后呢我们就是计算一下这个什么样预期收益你作为投资人嘛我们说了你一投标我们就要告诉你你将来能赚多少钱对不对那这个预期收益呢大家看一下是哪个字段先给大家说一说这个预期收益是我们找找啊就这一个big decimal对吧我们要把这个值给计算出来然后存进去就行了那预期收益怎么计算这个呢其实大家不用管
[04:08] 我们是给大家封装好的代码有个公式这个大家不用管我们封装好大家直接拿用就行了这个呢我们是封装到叫income我给你找找啊income哎就是它这个youtube这里边有一个工具类啊它里边有个方法就这一个方法咱可以点进去看一看你看这是不是计算投资人预期收益的对吧就是采用等额本息的这种还款方式啊这里边呢其实就是
[04:38] 一个固定的一个什么呀一个计算公式能够计算一下到期之后对吧这个投资人大概能这个赚多少钱这块代码大家又不用管了我们直接调用一下就行但是大概大家要知道你看他这里边都要哪些参数你需要知道首先你投了多少钱然后就是利息对不对还有就是月数月数就是啥意思你借给对方借多少个月嘛这个其实就是人家借款人借多长时间了比如说人家借款人借六个月那这就是六
[05:08] 对不对这12个月这就是什么呀12因为他需要根据这些数据来计算什么呀对最终的这个收益所以你得大概知道我们需要给他传什么数据所以你看我在这要调用这个方案调用这个方案之前我们说了是不是要准备三个数据啊对不对都哪些数据啊都哪些数据啊一个就是这个你你投了多少钱这个值是从哪来的呀这个值是不是咱这个在这个一开始的这个参数里边吗在哪呢
[05:38] 就这个参数里边就有是不是那然后呢咱就在这儿啊稍等在这儿这个地方我们是不是就可以导到那个什么呀投标金额呢那就是从参数里边取一下呗点get但是呢你要注意这儿是它反而是什么呀字符串类型啊人家这个地方要的应该是big decimal吧是不是所以我们在这儿呢要做类型转换怎么做类型转换呢直接new一下就行了
[06:11] 这个big decimal的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的诟数的
[06:42] 哪个配置呢来我找一找是是哪个呀这个啊就这个我们要的就是这个值啊这个值那从阿布罗上怎么取这个值啊那是不是用configure Service对不对大家看讲义吧这块代码就不再给大家写了configure Service对不对这样给他方法就得到拿到呃我们这就是第几个参考第二个参考对不对那接下来还剩一个参考就是月份那月份从哪过去
[07:17] 这个月份的话大家要注意啊我们当时在投标发标的时候我们记录的应该是他的天数吧你看这个谁啊普尔这个对象啊我记得是天数你看是不是但是人家现在要月数那我们是不是得稍微计算一下那咋计算呢咱看看讲一吧你看啊这个方法是不是就得到了那个天数然后怎么给他转换成月月数呢除以三十万假设一个月三十天吧大概算一下
[07:50] 当然呢这个大家知道很有可能是除不尽对不对这很常见嘛除不尽怎么办呢你看我们做了一些处理这个SEL方法是不是应该是入上去对不对当然呢有的还会说老师那那那这里边有个细节问题就说比如说这个假设是算完之后是六个月多十天六个月零十天这个到时候怎么算这时候是这样的大家想一下我这是不是只是算一个预期收益就是一个大概的
[08:19] 明白什么意思吧那将来的话真实的收益他要根据什么呀具体的情况啊你比如说举个例子如果是六个月零十天那多出来这个十天的话我们就按天给他记就行了所以大家一定要注意这只是一个预期收益明白什么意思吧所以我们这样呢就大概的给他入上去对吧结果的入上去然后在这取一个什么呀整数就行了预期收益可以适当的稍微给他多算一下所以一定要知道预期是什么预期收益不是实际收益所以我们在这呢就可以
[08:50] 把这个东西拿过来拿到拿到哪呢我们就放到这吧然后呢我们就可以把这个月数对吧作为最后一个参数拿过来那这样子的话我们就得到了这个什么呀对得到了一个值这个值其实就是什么呀预期收益然后呢我们直接把这个预期收益呢给它封装到这个谁呀Tender DTO对象里边
[09:23] set应该是叫ex应该就是这个值把后边整个这一堆当然这一堆呢这个值呢你也可以生命一个变量我这就不再生命变量直接把这一堆直接扔到这个set方法里边就搞定了啊我们看一看这个代码稍微有点长是不是那该封装呢就全部封装完了封装完之后最后一定要记住我们是不是要把这个什么呀
[09:53] 对kender DTO对象作为该方法的返回值给它返回就行了这是我们第三大块代码就给大家想想完之后咱整体过一遍你看第三块的代码咱首先是不是判断这个从代理服务那边返回的这个结果如果是成功的话我们是不是做了好多业务处理如果是失败的话我们就抛了一个一场那成功的时候我们都做了哪些事情呢我们是不是修改了这个数据同步的状态给它改成什么样以同步做一个更新
[10:23] 然后呢我们又判断本次投标完之后这个标底有没有满标满标的话是不是更新了一个标底的状态给它改成了40对不对然后呢我们给它转化成DTO对象然后又封装了几块数据两块数据一个是标底的信息标底信息这块封装的时候主要是多设置了一个什么呀对新设置了一个这个还款方式就等和本息的那个还款方式然后呢又封装了一个信息就是预期收益预期收益呢我们这是有一个工具类有一个方法封装好了我们直接调用一下就行
[10:53] 你只需要知道他要什么要你的投标金额要那个什么呀利息利息呢是从Apollo上取出来了还有就是这个什么月数月数呢我们是根据这个天数换算这个地方给大家强调这是这只是预期收益啊你不要不要在这太较真然后该封证的封证完最终把这个return这个什么呀把这个tender DTO对象作为整个这个方法的什么呀反而是一个反复那到目前为止吧咱整个这块代码你看
[11:23] 非常非常多对吧很不容易我们就把它给全部编写完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在交易服务中，根据投标状态更新项目信息，包括计算利息、转换DTO对象、校验金额并抛出业务异常。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 代码：在 ProjectServiceImpl.java 中，判断投标结果，若为成功则更新项目状态为“已满标”（FULLY），并调用 updateById(project)。
- 代码：BigDecimal remainder = getProjectRemainingAmount(project); if (remainder.compareTo(new BigDecimal(0)) == 0) { project.setProjectStatus(ProjectCode.FULLY.getCode()); updateById(project); }

画面2：
- 代码：else { throw new BusinessException(TransactionErrorCode.E_150113); }

画面3：
- 代码：在 project 变量后，IDE 提示 Project 类的 setter 方法，如 setProjectStatus(String projectStatus)。

画面4：
- 代码：在 project 变量后，IDE 提示 Project 类的 getter 方法，如 getProjectName()。

画面5：
- 代码：project.setRepaymentWay(RepaymentWayCode.FIXED_REPAYMENT.getDesc()); tenderDTO.setProject(convertProjectEntityToDTO(project)); // 封装项目信息

画面6：
- 代码：在 IncomeCalculate.java 中，计算利息的静态方法 getIncomeTotalInterest。
- 代码：public static BigDecimal getIncomeTotalInterest(BigDecimal invest, BigDecimal yearRate, int month) {
    double monthRate = yearRate.doubleValue() / 12;
    BigDecimal totalInterest = new BigDecimal(0);
    for (int i = 1; i <= month; i++) {
        BigDecimal multiply = invest.multiply(new BigDecimal(monthRate));
        BigDecimal sub = multiply.subtract(new BigDecimal(Math.pow(1 + monthRate, month)));
        totalInterest = totalInterest.add(sub);
    }
    return totalInterest;
}

画面7：
- 代码：在 ProjectServiceImpl.java 中，创建 TenderOverviewDTO 列表并遍历，将 Tender 实体转换为 TenderOverviewDTO。
- 代码：List<TenderOverviewDTO> tenderOverviewDTOs = new ArrayList<>(); tenderList.forEach(tender -> {
    TenderOverviewDTO tenderOverviewDTO = new TenderOverviewDTO();
    BeanUtils.copyProperties(tender, tenderOverviewDTO);
    tenderOverviewDTO.setConsumerUsername(CommUtil.hiddenMobile(tender.getConsumerUsername()));
    tenderOverviewDTO.setTenderAmount(tender.getAmount());
    tenderOverviewDTO.setTenderTime(tender.getCreateTime());
    tenderOverviewDTO.setTenderStatus(tender.getStatus());
    tenderOverviewDTO.setTenderId(tender.getId());
    tenderOverviewDTO.setTenderType(tender.getType());
    tenderOverviewDTO.setTenderUserId(tender.getUserId());
    tenderOverviewDTO.setTenderUserName(tender.getUserName());
    tenderOverviewDTO.setTenderUserPhone(tender.getUserPhone());
    tenderOverviewDTO.setTenderUserEmail(tender.getUserEmail());
    tenderOverviewDTO.setTenderUserAddress(tender.getUserAddress());
    tenderOverviewDTO.setTenderUserPostCode(tender.getUserPostCode());
    tenderOverviewDTO.setTenderUserProvince(tender.getUserProvince());
    tenderOverviewDTO.setTenderUserCity(tender.getUserCity());
    tenderOverviewDTO.setTenderUserDistrict(tender.getUserDistrict());
    tenderOverviewDTO.setTenderUserTown(tender.getUserTown());
    tenderOverviewDTO.setTenderUserVillage(tender.getUserVillage());
    tenderOverviewDTO.setTenderUserStreet(tender.getUserStreet());
    tenderOverviewDTO.setTenderUserBuilding(tender.getUserBuilding());
    tenderOverviewDTO.setTenderUserUnit(tender.getUserUnit());
    tenderOverviewDTO.setTenderUserRoom(tender.getUserRoom());
    tenderOverviewDTO.setTenderUserDoor(tender.getUserDoor());
    tenderOverviewDTO.setTenderUserDoorCode(tender.getUserDoorCode());
    tenderOverviewDTO.setTenderUserDoorName(tender.getUserDoorName());
    tenderOverviewDTO.setTenderUserDoorType(tender.getUserDoorType());
    tenderOverviewDTO.setTenderUserDoorStatus(tender.getUserDoorStatus());
    tenderOverviewDTO.setTenderUserDoorLock(tender.getUserDoorLock());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoor

