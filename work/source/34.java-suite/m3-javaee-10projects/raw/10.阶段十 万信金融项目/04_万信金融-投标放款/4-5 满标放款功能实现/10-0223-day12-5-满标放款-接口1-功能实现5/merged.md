# day12-5-满标放款-接口1-功能实现5

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-5-满标放款-接口1-功能实现5_【海量资源尽在 666java.com】.mp4
- 时长 13分48秒（音频 828s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 刚才呢我们是不是把第三阶段的代码给编写完了那按照顺序的话接下来该实现第四阶段就是接口四的这个功能那咱通过这个图再回顾一下接口四大家看一下那么接口三这一块是不是把标底的一些状态是不是改成了还款中对不对那你这个状态不能白改是不是所以说你接下来最后一个阶段就是接口四这边就要启动什么呀还款
[00:33] 那我们这启动还款并不是指的是让这个借款人就开始还钱了不是啊我们这个地方呢相当于是还款的一个什么呀对一个初始的一个阶段这个时候呢我们主要是为了生成什么呀还款计划啊应收明细那也就是说呢比如说啊你你你借了这个这个银行的一些钱或者你带了一些款对吧那人家当时就会告诉你什么呀
[00:59] 你接下来每个月要还多少钱对吧你要付多少利息对不对等等等等其实就是我们要生成这么一个计划啊一个一个明细然后给这个谁要借款人让他心里边清楚这件事情所以说我们借口司啊他这个启动还款主要是由交易中心大家注意看啊这根柱子是不是交易中心吗是不是让他呢发请求给谁啊看这啊这是指的谁啊对我们新增加了这个什么还款微服务啊往这发请求
[01:28] 把他需要的数据呢给他发回去发回去之后呢这边主要就是刚才我说的就生成一个缓缓计划或者说一个什么呀应收的一个什么呀这个利息啊等等一些明细信息然后就可以了这是我们接下来接口4要实现的这个功能那咱们接下来就开始编写这个代码接口4这一块呢我们刚才说了交易中心是不是在交易中心对不对交易中心要发请求到哪
[01:58] 到这个缓缓微服那缓缓微服这边在生成缓缓计划和应收明信的时候他是需要一些数据他需要一些数据然后去计算呀对吧去生成这些东西那因此呢这些数据我们是不是应该通过22这一步给他干什么呀传过去他要啥我就给他传啥对不对那他都要啥数据呢咱先来先罗来一下啊把他要的数据先罗来出来这个代码应该写到哪这个代码肯定不能写到这了这个代码是不是得写到这个地方
[02:30] 大家看是不是你肯定是第三阶段执行成功我们才走第四阶段嘛对不对那我们刚才说首先要干什么呀对准备数据准备数据把这些数据准备好呢发给款款微服务他们他那边就会根据这些数据干什么呀对生成什么还款计划啊应收明细等等这些东西那我们都需要准备哪些数据呢这个呢你得看什么呀看这个谁啊接口四对不对看这个接口四里边他是这个当时怎么要求的
[03:01] 那我们找找这个接口司吧这个接口司我们是不是定义在这个谁啊对定义在还款微服务当中哎那这个接口应该是不是去API工程里面找啊还款的微服务repayment这是他的接口对不对然后你看我们这是不是又启动还款你看这里边他有一个参数叫project with tinder的DTO那这里边封装的就是他想要的数据啊所以说我们要进到这里边看一看
[03:29] 他这里边都要啥呢你看看都要要什么要标底信息对吧标底对象DTO对象啊还有什么呀所有的投标记录啊还有什么呀投资人让利益还有什么呀借款人让利啊其实就是投资人让出的这个利息啊还有借款人给平台这个设定的一些什么呀利息这些东西的话都是将来他要干什么要做计算去用的啊计算手用那比如说这两个利息
[03:57] 利率都是什么意思咱等到计算或者真正用它的时候我们到时候再说这是现阶段我们就是他要啥我就给他准备啥数据然后发给他就行了大家看是不是四块数据对不对那咱接下来就是准备这四个数据就行了一个一个来吧先准备啥呢我们先准备这个我先准备这个刚才那个谁啊标底信息吧好吧标底信息最简单吧
[04:28] 标的信息标的信息的话在哪标的信息的话大家想前面这个是不是就有这个标的信息吧我们找找你看这这就查出来过了对吧project但是呢刚才大家应该注意到人家这要的是你看DTO是不是所以我们这要做一个什么呀对类型转换怎么转我们以前是编写有这方面的方法对吧convertco
[04:58] NVRT Convert我们找找应该是谁应该是这个对吧然后我们把前面插出来Project对象给它扔进去就行了这时候我们不就得到了一个什么Project的DTO然后我们把它要封装到什么被封装到Project with Tenders DTO对象里面就行了这个对象是不是还不存在所以说准备数据我们首先得把对象给它干什么创建出来
[05:27] 直接溜了对吧然后这你直接就可以进行封装了吗直接就是project with tinder dt对吧第2他的什么呀setter方法应该是这个我们先封装这个标的信息是吧这不就封装进去一个吗然后继续接下来我们封装啥呢接下来我们就封装这个投标信息吧因为这个投标信息我们前面是不是也是现成的已经查出来过了对吧投标信息
[06:05] 投标信息的话大家往上面找一找啊就是就这个吧tender list呢对不对这就是投标信息嘛我们直接封装就行了直接调用他的set什么呀tenders把上面的这个什么呀tender list这个集合直接放进去哎这就搞定了哎大家看这里边他是不是报了一个错对不对那这个报错是因为啥因为啥呢还是类型转换你看看啊人家这要的是tender dto对不对
[06:36] 那我们前面这个tender list里边这个范想tender list你看是什么样是tender不是tender DTO那所以说我们是不是需要呃像之前一样这个方法大家见过是不是搞一个方法把一个集合他的范型对吧里边的这个对象的类型啊给他转换一下那这个代码咱以前写过我就不再给大家编写了我们从讲义里边给他拨过来用用就这个我们给他就放到哪
[07:13] 放到这吧放到这好大家看一下是不是传过来一个集合但是这个集合的范围是tender类型的对不对然后接下来我进行便利便利的时候是不是通过bin utils把它里边属性的值全部给谁啊给dto对象啊然后把dto呢存到一个新的集合里边反而这个集合就行这个代码咱以前见过啊那有了这个方法之后呢我在这怎么做呀是不是就调用刚才那个方法就行了啊convert
[07:53] 对吧convrdcomber的谁呢我们应该是tender啊就是第一个吧tender entity listto什么dto list还是做一个转换然后把这个集合呢给它扔进去就ok了对不对这是什么呀投标信息我们也封装好了好继续我们接下来还要封装啥接下来是不是要封装一个什么呀投资人让利投资人让利和什么呀对借款人让利
[08:26] 这俩具体有什么用啊表示什么意思你先不用管我们用的时候再说因为咱现在只是准备一下数据而已那这两个数据从哪来的哎这两个数据大家注意了啊这两个数据我们配置到了Apollo上啊咱一起看一看看看这个Apollo上的配置啊我们应该是找一找这个交易中心吧交易中心啊咱找一找application对不对这里边呢应该是
[09:06] 应该是拿两个对不对应该是拿两个那应该是这两个这两个啊你看咱前面是不是用过这个值吧最小投资金额吗当时是不是也是从阿布罗上取下来了那现在呢我们要用的是这两个这个呢应该是借款人的那个让利啊这个呢是什么呀投资人的让利我们要取这两个值这两个值那么怎么从阿布罗上取值
[09:33] 咱现在基本上总结出来两点一个是通过at value给他注进来一个是通过configure Service是不是好那咱在这呢就写一下这个代码啊我这呢就用configure Service来取了那就是configure这个代码是咱直接给大家提供的嘛这个configure Service点啊那这个应该是咱应该应该注入过来呀configure啊刚才敲错了啊这个点
[10:07] get我们要取的是一个是这个啊然后还有呢就是configure Service.get还有一个是这个啊一个是借款人一个是什么呀投资人让利嗯这个呢应该是什么借款人让利上面那个是投资人让利那我们得到这两个值之后呢得到这两个值之后呢我们是不是就可以调用setter方法把他们两个的值直接
[10:41] 对封装进去就行了我们就调上面这个dto对象直接进行set这个封装这应该是这个方法这个代码呢都会比较长一些好我们把它给粘到这里啊下面也是一样的啊project with tinder dto.set应该是这个方法set的方法啊然后把获取到的这个值呢把它放进去
[11:13] 那大家目前看一看啊我们目前的话是不是把需要准备的数据一共是四个吗我们全部准备到位了而且呢也封装到了这个什么呀Project with Tinder Tinder什么呀对Tinder DTO对象里面呢接下来干嘛接下来咱看这个图呗咱前面说了嘛你把这个数据准备好之后是不是要发请求对不对发请求到什么呀对缓缓微服务这边把数据给他他这边负责生成什么呀
[11:43] 还款计划应收明细那接下来是不是又要通过飞印去干什么远程请求了吗哎不是啊这个地方大家注意一点这个地方有点特殊呃先简单说一说啊呃这个地方怎么说呢就是说这个还款微服务这边他要生成这个还款计划应收明细他可能这个事会有点耗时啊有点耗时而且呢这是两个微服务之间的一个交互对不对这边呢业务处理会比较耗时那这个时候呢
[12:13] 它就涉及到分布式事物的问题涉及到什么呀分布式事物所以说呢我们这不准备用飞发起这个什么远程镜头准备通过什么呀通过RocketMQ来把这个数据作为消息给它传过去主要是考虑到这里边涉及到分布式事物那这块具体的东西我们后边会单独给它摘取出来详细的来做讲解那因此呢我们这儿
[12:49] 就先把这个功能先放一放你知道我们在第四阶段目前是把数据全部准备到位就等着干什么呀往那边发了啊后边呢我们把这个分布式事务啊Rookie的MQ整个这套东西讲完之后我们回过头来会补这一块的代码说这个需要大家知道怎么回事啊那这就是咱临时的先跳过去那我最后呢要得有一个返回值啊对不对那我这就直接返回一个字幕块就是审核成功呗
[13:22] 对吧啊这块咱先跳过去啊那这块跳过去的话咱目前是不是就把第1弹对第4阶段这块代码也就编写完这块其实比较简单是不是就是他要啥时候有就呃获取什么数据然后封装到这个DTO对象里边将来呢通过Rookie的MQ发过去让哪边对让缓缓微服务这边去生成缓缓计划和应收明细就行

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解一个项目还款服务的业务流程，包括状态变更、数据转换、配置获取和异常处理等核心逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示一个流程图，描述还款流程中涉及的多个状态变更和交互，如“修改状态”、“更新交易记录”、“成功”等。
画面 2: 显示 `ProjectServiceImpl.java` 文件中的代码，处理项目状态修改逻辑，包含对 `modifyProjectStatusDTO` 的设置和调用 `depositoryAgentApiAgent.modifyProjectStatus` 方法。
画面 3: 显示 `ProjectWithTendersDTO` 类的定义，包含 `project` 和 `tenders` 字段。
画面 4: 显示 `ProjectWithTendersDTO` 类中 `commissionInvestorAnnualRate` 和 `commissionBorrowerAnnualRate` 字段的定义。
画面 5: 显示 `ProjectServiceImpl.java` 文件中的代码，包含 `convertProjectEntityToDTO` 方法的调用。
画面 6: 显示 `ProjectServiceImpl.java` 文件中的代码，包含 `modifyProjectStatusDTO` 的设置和 `depositoryAgentApiAgent.modifyProjectStatus` 方法的调用。
画面 7: 显示 `ProjectServiceImpl.java` 文件中的代码，包含 `restResponse` 的判断和 `updateTenderStatusAlreadyLoan` 方法的调用。
画面 8: 显示 `ProjectServiceImpl.java` 文件中的 `convertTenderEntityToDTO` 方法实现，用于将 `Tender` 对象转换为 `TenderDTO`。
画面 9: 屏幕空白，仅显示任务栏。
画面 10: 显示 Apollo 配置中心的界面，展示 `micro_service.spring-boot-http` 和 `micro_service.spring-Eureka` 等配置项。
画面 11: 显示 `ProjectServiceImpl.java` 文件中的 `ConfigService` 类的注释，说明其功能。
画面 12: 显示 `ProjectServiceImpl.java` 文件中的 `ConfigService` 类的 `getCommissionInvestorAnnualRate` 方法调用。
画面 13: 显示 `ProjectServiceImpl.java` 文件中的代码，包含 `projectWithTendersDTO` 的初始化和 `configService` 的调用。
画面 14: 展示一个流程图，描述还款流程中涉及的多个状态变更和交互，如“修改状态”、“更新交易记录”、“成功”等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
modifyProjectStatusDTO.setId(project.getId());
modifyProjectStatusDTO.setProjectStatus(ProjectCode.REPAYING.getCode());
modifyProjectStatusDTO.setRequestNo(loanRequest.getRequestNo());
modifyProjectStatusDTO.setLoanRequest(getRequestNo());
//向代理调用事务发起请求
RestResponse<String> modifyProjectStatus = depositoryAgentApiAgent.modifyProjectStatus(modifyProject);
if (modifyProjectStatus.getReturnCode().equals(DepositReturnCode.RETURN_CODE_00000.getErrorCode())) {
    //如果处理成功，修改该状态方法中
    project.setProjectStatus(ProjectCode.REPAYING.getCode());
    updateById(project);
} else {
    throw new BusinessException(TransactionErrorCode.E_150113);
}
```

画面 3:
```java
public class ProjectWithTendersDTO {
    //标的
    private ProjectDTO project;
    //标的对应的所投投标记录
    private List<TenderDTO> tenders;
    //投资人让利率（投资人让利）
    private BigDecimal commissionInvestorAnnualRate;
    //借款人让利率（借款人让利）
    private BigDecimal commissionBorrowerAnnualRate
```

画面 5:
```java
convertProjectEntityToDTO
```

画面 6:
```java
ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO();
modifyProjectStatusDTO.setId(project.getId());
modifyProjectStatusDTO.setProjectStatus(ProjectCode.REPAYING.getCode());
modifyProjectStatusDTO.setRequestNo(loanRequest.getRequestNo());
modifyProjectStatusDTO.setLoanRequest(getRequestNo());
//向代理调用事务发起请求
RestResponse<String> modifyProjectStatus = depositoryAgentApiAgent.modifyProjectStatus(modifyProject);
if (modifyProjectStatus.getReturnCode().equals(DepositReturnCode.RETURN_CODE_00000.getErrorCode())) {
    //如果处理成功，修改该状态方法中
    project.setProjectStatus(ProjectCode.REPAYING.getCode());
    updateById(project);
}
```

画面 7:
```java
RestResponse<String> restResponse = depositoryAgentApiAgent.confirmLoan(loanRequest);
if (restResponse.getReturnCode().equals(DepositReturnCode.RETURN_CODE_00000.getErrorCode())) {
    //第二阶段：修改状态
    ModifyProjectStatusDTO modifyProjectStatusDTO = new ModifyProjectStatusDTO();
    modifyProjectStatusDTO.setId(project.getId());
    modifyProjectStatusDTO.setProjectStatus(ProjectCode.REPAYING.getCode());
    modifyProjectStatusDTO.setRequestNo(loanRequest.getRequestNo());
    modifyProjectStatusDTO.setLoanRequest(getRequestNo());
    //向代理调用事务发起请求
    RestResponse<String> modifyProjectStatus = depositoryAgentApiAgent.modifyProjectStatus(modifyProject);
    if (modifyProjectStatus.getReturnCode().equals(DepositReturnCode.RETURN_CODE_00000.getErrorCode())) {
        //如果处理成功，修改该状态方法中
        project.setProjectStatus(ProjectCode.REPAYING.getCode());
        updateById(project);
    }
}
```

画面 8:
```java
private TenderDTO convertTenderEntityToDTO(Tender tender) {
    if (tender == null) {
        return null;
    }
    TenderDTO tenderDTO = new TenderDTO();
    BeanUtils.copyProperties(tender, tenderDTO);
    return tenderDTO;
}
```

画面 11:
```java
//4.借款人让利
```

画面 12:
```java
project.configService.getCommissionInvestorAnnualRate()
```

画面 13:
```java
//外到到分方式事务
projectWithTendersDTO.setProject(convertProjectEntityToDTO(project));
projectWithTendersDTO.setTenders(convertTenderEntityListToDTOList(tenderList));
projectWithTendersDTO.setCommissionInvestorAnnualRate(configService.getCommissionInvestorAnnualRate());
projectWithTendersDTO.setCommissionBorrowerAnnualRate(configService.getCommissionBorrowerAnnualRate());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1:
- 标题：无
- 流程图结构：
  - “修改状态”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”指向“成功”
  - “成功”指向“更新交易记录”
  - “更新交易记录”

