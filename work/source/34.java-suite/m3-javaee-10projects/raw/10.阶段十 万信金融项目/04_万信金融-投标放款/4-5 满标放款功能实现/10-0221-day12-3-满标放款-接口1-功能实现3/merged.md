# day12-3-满标放款-接口1-功能实现3

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-3-满标放款-接口1-功能实现3_【海量资源尽在 666java.com】.mp4
- 时长 8分53秒（音频 533s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们把第一阶段代码的编写完了这里边主要是生成了一个放款明信生成这个放款明信的目的是不是将来要把这个对象干什么呀往哪发对往存款代理服务那边发其实这呢就已经涉及到第一阶段的代码了对就是咱接下来该实现第一阶段了对第二阶段的这一块代码就是放款咱看一看这个图那就是3对吧3这个位置开始放款
[00:29] 那么这个地方呢就是交易中心要推动过什么非发起远程请求到哪儿从来在里服然后呢把刚才的这个load request这个又传过去了对不对这边呢他这个要干什么呀又是生成签名啊保存交易记录对吧他还要访问银行存款系统然后成功之后呢要更新交易记录数据状态对吧那我们的交易中心这边这个收到消息之后这边是不是要更新投标信息的状态改成什么呀改成一放快是不是
[00:58] 所以说呢这是我们接下来要把接口二这块的功能搞定那接口二的话我们刚才看到是不是上来就应该往什么呀往从代理服务那边发请求吧通过飞应是不是怎么通过飞应发远程请求啊咱前面是不是做了一个准备工作大家有印象吗在这里边我们是不是已经怎么着对把这个飞应代理这个方法是不是已经定义好了对不对我们接下来是不是要调用这个方法
[01:26] 接下来调用一下我们的业务层在这那就是depository对API的哪个方法应该是这个方法那调用这个方法它是不是就发起了远程请求然后我们需要把law request就是这个明细给它传过去传过去之后那么存款代理服务这边是不是该进行45678910对不对整个这一套操作
[01:56] 那这边他处理完之后呢我们交易中心这边是不是要判断他有没有放款成功对不对所以说我们这边要接收他的对结果啊他的反应值是什么呀大家最熟悉的rest response里边是一个字母串类型的范形rest responsetrain我们就叫rest response那我们接下来是不是要判断这个放款到底成功没成功怎么判断呢大家应该很熟悉了吧
[02:25] 怎么判断是那五个零那个判断了对不对所以我们接下来呢就是这么子来写从rest response 边是不是取那个状态码吗叫getget 谁呀getget 什么呀哎get没反应了点对get result 是吧他要跟谁比啊他要跟那五个零吗你还有印象吗就是depository那个叫return code对吧点
[02:56] 就是第一个五个零就是比较成功这个要跟他比那这个表成功了那else就表示什么失败了咱先把失败的情况先写一下失败的情况搁咱以前的套路咱一般会怎么办失败的时候是不是就抛一场对不对咱就直接srollnew businessexception里边的这个信息的话我们就找一找translation error code我们挑一个
[03:27] 挑哪个呢我们我们结合以往的经验我们应该是选的是113这个当然我之前跟大家说过啊如果你觉得这个提示信息不够怎么说呢呃不够清晰啊或者不够明确这个值你可以自己随便改这是先是我们事先判断了一个什么呀失败的情况啊失败的情况下我们就抛一场那一幅就表示什么呀成功成功我们需要干啥事成功你需要干啥事你看这个这个实际图呗你看
[03:58] 放款成功放款成功我们这边就要更新所有投标信息的状态为什么呀对已放款啊那他之前的状态是什么状态啊你看看之前的状态我们找一找哪个值啊字段有点多啊是就是这啊tender status你看他原来这应该是冻结吧对不对就是你你你你投标的时候你那个金额要被冻结吗然后呢现在呢放款成功呢我们这边就要改状态改成什么呀
[04:35] 你放款那是不是这个每个这个投标信息里面这个字段值都要改对不对没错啊只要是跟这个标的有关的这个投标信息这里面这个值都要改改成这个你放款那考虑到这个代码有可能这个将来在其他地方也会用到所以说我们准备呢抽出来抽成一个方法单独实现那我们就放到这儿吧我们就写个注释线啊我们现在这实现的啥功能
[05:12] 修改什么呀投标信息的状态为什么呀为以放款好咱单独写一个方法private void我们只是一个修改操作嘛对不对不需要什么反位置名字的话咱跟讲义保持一致吧虽然我们起什么名字都行
[05:43] 但是呢我们尽量跟奖励保持一致看看他这个名字叫啥名老长了啊那大家想我们都需要什么参数啊我们是不是要修改投标记录当中某个字段的值是吧那你是不是应该把投标记录给我投标记录我们前面是不是查询过了是不是就是一个集合嘛我们就把那个集合给他干什么扔过来就行了然后把这个集合里边每个记录里边的哪个字段啊对就是
[06:19] 又跑哪去了就这个字段只给他改一下就行那这是一个集合我是不是得进行什么呀循环便利啊对不对啊跟前面一样tenderlist.foreach啊这里边应该是tender那我取出来每个对象之后呢取出来每个对象之后呢你是不是就要修改他的值了啊修改他的这个字段的值刚才让大家看了叫set什么呀对set的tendertender status
[06:51] 那只给哪个呢你不能随便乱写我们这里边呢是给大家封装好了叫叫叫叫我一找找啊叫tree丁扣的啊tree丁扣的我们从这里边找一个找一个哎就是这个论就是一放过对吧你要这个值这是一个对象然后我们再调他的这个什么呀get code的方法就ok了然后分号加上
[07:20] 那这样子的话我们就把这个对象里边的这个值是不是从冻结给他改成了什么呀以放款然后呢我们去更新数据库更新数据库的话就要调用map解口啊tender Mapper我们调用他的up update by id呗是不是把这个tender对象一个一个扔进去大家看好啊我这是一个集合啊比如说这个集合里边呢呃又又有三个投票记录这里边是不是应该有三个tender对象便利的时候呢把每个
[07:49] tender对象里边这个值是不是都改成这个什么以放款然后调map接口把每一个对象都进行什么呀对进行更新就行那然后呢我在这要干什么呀是不是要调用这个方法了咱接下来呢调用一下这个方法那就是怎么写直接调用呗update叫这名是不是然后把刚才那个谁呀那个集合叫tender list是吧给他扔进去就行了这就完成了更新那这个
[08:21] 搞定之后还有啥活要干吗你看一看还有吗暂时没有啊暂时没有啊因为呢你看游同学学生说老师后边不是还有这个修改状态这个修改状态你得等到什么呀第三个阶段搞定之后你再去修改对不对现在呢我们只是把这个什么呀相当于是第二阶段啊这个又搞定了我们修改这么一个状态就12这个状态对不对所以说呢目前等于说是第二阶段啊第二阶段这个代码咱也编写完

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个贷款审批服务中，如何通过调用外部代理服务来确认贷款，并根据返回结果更新投标状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `ProjectServiceImpl` 类中 `loansApprovalStatus` 方法的代码，注释显示第一阶段是“生成放款明细”，第二阶段是“放款”，并调用 `generateLoanRequest` 方法。
画面2：光标移动到第二阶段“放款”注释行，准备编写放款逻辑。
画面3：展示 `DepositoryAgentApiAgent` 类的 `confirmLoan` 方法，用于确认贷款。
画面4：在 `ProjectServiceImpl` 中调用 `depositoryAgentApiAgent.confirmLoan(loanRequest)` 方法。
画面5：添加条件判断，检查 `restResponse.getResult()` 是否等于 `DepositoryReturnCode.RETURN_CODE_00000`。
画面6：如果条件不满足，则抛出 `BusinessException`，错误码为 `TransactionErrorCode.E_150113`。
画面7：切换到数据库管理工具，显示 `pjp_transaction` 数据库的表结构，包括 `project`、`tender` 等表。
画面8：回到代码编辑器，展示 `generateLoanRequest` 方法的实现，用于构建 `LoanRequest` 对象。
画面9：展示 `generateLoanRequest` 方法中设置 `loanRequest.setTd(project.getId())` 和 `loanRequest.setCommission(new BigDecimal(commission))`。
画面10：切换到桌面，显示多个窗口，包括数据库工具、代码编辑器和PDF文档。
画面11：在 `ProjectServiceImpl` 中调用 `updateTenderStatusAlreadyLoan` 方法来更新投标状态。
画面12：展示 `updateTenderStatusAlreadyLoan` 方法的实现，使用 `tender.setTenderStatus(TradingCode.LOAN.getCodec())`。
画面13：展示 `updateTenderStatusAlreadyLoan` 方法的实现，使用 `tender.setTenderStatus(TradingCode.LOAN.getCodec())`。
画面14：回到 `ProjectServiceImpl`，展示 `updateTenderStatusAlreadyLoan(tenderList)` 方法的调用。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public String loansApprovalStatus(Long id, String approveStatus, String commission) {
    //第一阶段：1. 生成放款明细
    // 核的信息
    Project project = getProjectById(id);
    // 投标信息
    QueryWrapper<Tender> queryWrapper = new QueryWrapper<>();
    queryWrapper.lambda().eq(Tender::getProjectId, id);
    List<Tender> tenderList = tenderMapper.selectList(queryWrapper);
    // 生成放款明细
    LoanRequest loanRequest = generateLoanRequest(project, tenderList, commission);
    //第二阶段：2. 放款
    //3. 修改状态
    //4. 启动还款
}
```

画面3：
```java
public class DepositoryAgentApiAgent {
    ...
    public RestResponse<String> confirmLoan(LoanRequest loanRequest) {
        ...
    }
}
```

画面4：
```java
RestResponse<String> restResponse = depositoryAgentApiAgent.confirmLoan(loanRequest);
```

画面5：
```java
if (restResponse.getResult().equals(DepositoryReturnCode.RETURN_CODE_00000)) {
```

画面6：
```java
} else {
    throw new BusinessException(TransactionErrorCode.E_150113);
}
```

画面8：
```java
public LoanRequest generateLoanRequest(Project project, List<Tender> tenderList, String commission) {
    LoanRequest loanRequest = new LoanRequest();
    ...
}
```

画面9：
```java
loanRequest.setTd(project.getId());
loanRequest.setCommission(new BigDecimal(commission));
```

画面11：
```java
private void updateTenderStatusAlreadyLoan(List<Tender> tenderList) {
    tenderList.forEach(tender -> {
        tender.setTenderStatus(TradingCode.LOAN.getCodec());
    });
}
```

画面12：
```java
tender.setTenderStatus(TradingCode.LOAN.getCodec());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

