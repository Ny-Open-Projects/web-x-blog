# day14-13-用户还款-第三阶段-业务触发入口

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-13-用户还款-第三阶段-业务触发入口_【海量资源尽在 666java.com】.mp4
- 时长 18分31秒（音频 1111s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好截止到目前的话我们把用户还款业务当中第三阶段的功能呢全部开发完了啊就是这一块对吧那接下来的话咱需要像之前一样把业务触发入口里边的代码给他补一补补上之后呢我们主要是为了触发这个第三阶段业务的这个什么呀执行了大家看一看我们之前在这个业务触发入口里边是不是触发了什么呀第一阶段
[00:34] 业务的执行然后还触发了第二阶段业务的执行那咱接下来就要触发2.1对不对2.1发送消息这个消息一发说KIT MQ7成功之后是不是就该执行这个本地事务了对不对那就可以把我们刚才第三阶段实验的这个功能给它干什么打通了给它串起来了所以说我们接下来还是需要去完善什么呀业务出发入口里边带了那咱找一找这个什么呀业务出发的入口
[01:03] 这个入口在那你还有印象吗你要是忘了的话你就找卡车了咱当时是不是这搞了一个测试吗你有印象吗对不对这是我们用户操作的入口然后呢这个具体这个要操入口是不是在业务层的这个EQ的repayment的方法里边我们点进去你看一看啊在这里边你看这一块是不是就是在触发第一阶段这个业务的执行这样呢是在触发对第二阶段业务的执行
[01:33] 而且呢这个第二阶段处理完之后是不是返回了一个结果true false对吧那如果是true是不是证明第二阶段成功第二阶段成功咱接下来就该执行什么呀对就该触发第三阶段这个代码的执行第三阶段不就是2.1吗你只要把这个消息发出去了那下面这些功能是不是就自然就干什么呀对就往后推进了就串起来了所以说呢我们接下来的话在这就是要干什么呀把这个消息给他
[02:02] 发出去然后从而就出发第三阶段业务的执行那发消息咋发呀咱发消息是不是前面放到一个内当中了啊在哪呢在这个地方repayment producer对不对你看咱是不是有一个方法他是不是复杂发消息了对不对那咱是不是把他给注入到这个什么呀哎这个业务层我们在这儿一定有方法其实就搞定了啊咱看咱这个有没有注入过啊应该是没有吧好咱进来注入一下
[02:37] revet叫什么呀repaymentrepayment谁呀不是Service是pno对好然后接下来的话咱回到入口那个地方就是在这我们就要干什么呀我们就要调用repaymentrepayment什么呀producer对不对
[03:08] 然后他有个发送消息的方案就是这个confirm什么呀repayment我们一调了是不是就搞定然后大家看一下这个方案是不是要两个参数啊对不对第一个参数是啥第一个参数是这个还款计划这个还款计划你看咱当前是不是在这个循环里边你看这不就是还款计划了对不对第一个参数很好搞就拿手了关键是什么呀第二个参数第二个参数啊我们是不是要封装一个对象叫repayment什么呀request的对象
[03:37] 这个对象里边都要什么东西呢咱接下来要看一看啊repayment request咱找到这个类咱看它里边要封装的数据是不是非常多啊反正我们就是整体的思路就是你有一个对象它里边要啥我就把数据对吧通过set方法给它然后呢我们就可以放到这来用repayment request来我们看看啊这里边封装的东西也不少啊对不对
[04:12] 请求流水号预处理的要流水号标底的编码平台佣金放款明细看一看这里边还有一个明细啊这个业务的ID还款总额那这里边这个放款明细这里边是不是还涉及到一个实体类对不对我们还得进去封装它这里边你看都有啥投资人的用户编码这个向投资人收取的佣金派息对吧投资人应收的本金应收的利息等等等等
[04:43] 这个加上这个的话咱其实整个要封装的数据还是挺多的那咱干脆这样咱单独封装一个方法吧把这个数据呢给它封装到这个repayment request的里边咱单独定一个方法那就在这儿吧专门来封装这个什么呀请求数据的对不对先加一个注释呃构造吧构造还款信息请求
[05:17] 数据这个发展跟讲义保持一致啊这个我们找一找是在这对不对单独定义了一个方法那这个方法呢我们设计了两个策略第一个呢还是这个黄粉计划第二个呢是那个什么呀预处理的那个流水号这个流水号呢我们是不是在哪个地方已经给过了呀在这对不对在这个地方已经给过了我们一会可以这个取一下给他取出来呃然后呢第一个参数这个
[05:55] 肯定也是因为我们在封装这个repayment request的这个数据的时候呢这个对象的时候呢要用到它里边的数据所以说我们这个方法呢是设计了这两个参数那咱接下来这里边大概的思路就是干什么呀大概的思路就是你得先new出来这么一个对象嘛对吧然后呢然后你就是要调用调用什么调用它的一堆方法哪个方法对不对
[06:33] 就这一堆东西啊他需要啥子你该给就给就行了这是整个这么一个过程那咱接下来一个一个来啊我们先给他看哪些简单咱先给了吧你先挑几个简单的咱看看讲一吧这个有些比较简单的代码我就不再给大家说了大家看看这个什么呀还款的总额是不是从这个什么呀这个还款计划里边就可以取出来了对吧这个医药实体的ID也是还款计划的ID对吧包括这个什么呀
[07:04] 佣金是不是也是从缓缓计划里边取出来了标底的编码也是从缓缓计划里边取出来了是不是咱先把这几个简单的咱先拿过来那么接下来呢就是这个流水号这个流水号的话我们这个地方是要自己生成你的request number你看这个生成是不是跟之前是一样的嘛对不对这个给大家写一下吧repayment request对吧dear set谁呀不是这个啊是这个request number
[07:46] 然后呢我们怎么去生成一个那个那个什么呀流水号是不是要通过一个工具类叫code youtubecode number youtube对不对然后呢调用他的什么get number方法然后这里边要通过code prefix code来生成code prefix code我们这个请求流水号的话应该是code request的prefix那就是它了这个我们以前经常用嘛那这样子的话我们就生成了一个流水号
[08:15] 然后再往下我们看还有哪些需要封装的呀嗯在哪呢我们刚才是哪啊是这对吧这是流水号对吧然后呢还有一个预处理的业务流程这个流水号我们说的是不是在上面直接就可以拿到手吗pre request the number这个将来会通过参数传进来对你看我们这有个参数将来我们调这个方法时候的传进来了这个是我们很容易得到的
[08:56] 然后还缺一些东西还缺啥你看我们这里边还有什么没给放快明细这个放快明细你还得这个循环便利一下对不对存到一个什么存到一个集合里边这个放快明细其实就是刚才大家看到这个连着对吧我们还得往这个实体对象里边进行封装这个会相对来说麻烦一些然后上面还有呢上面你看这一块这块是不是在查这个什么呀营收计划
[09:31] 为什么要查这个应收计划你看这是一个集合叫receivable plan list对不对你看看在在这我们是对它进行便利吗因为这个方法明细需要根据这个什么呀应收计划里边的一些数据来干什么呀来生成所以说你看我们要想这个生成这个什么呀这个方法明细我们得先查出来这个应收计划这个应收计划怎么查呢就是根据什么呀
[10:01] 对repayment id根据这个还款计划呢我们就可以把它查出来所以咱接下来把最后这块代码呢给它补上我们我们就跟讲一样吧写到最上面吧到时候大家看的时候是一致的那这样呢我们应该就是干什么呀根据还款计划id然后查询相对应的什么呀对应收计划
[10:35] 这个怎么查呢我们是不是应该要通过哪个表应该叫receivable plan对吧map他就是操作这个这个什么应收计划的这个map接口我们调他的一个方法应该叫select list因为他有可能是多条数据那我们在做查询的时候是不是应该有一个条件吗这个条件我们也是要用varps来进行封装varps
[10:59] 点什么呀对那么大query别忘了这儿呢需要设置范形我们这个范形呢就是对receivable plan那这个条件是什么呢我们接下来需要进行封装是不是就是一个相等判断的吧EQ拿着这个谁呀拿着这个还款计划的ID在哪里还款计划的ID就是这个它的值呢是不是就从这个什么呀repayment plan
[11:31] 这个参数里边我们就可以取出来在这对吧点给他一分号哎大家看这个查询我们是不是搞定了然后他查出来的是不是一个集合吗list这里边的范行肯定也是receive plan然后呢我们起一个名字来接收一下啊receive plan list就这个
[12:10] 那我们查这个集合的目的是不是为了接下来要干什么呀对接下来要给这个东西生成值哪个东西呢我们说了现在就差这个谁了呀就差这个哪个东西呢set我们看这儿吧就差这个什么呀这个放个明信了那这个放个明信里边的数据呢要通过刚才我们查出来的这个谁呀营收计划去生成
[12:41] 你有10个计划你就应该对应10个什么呀对应收明细他们是对应关系的我接下来呢我们要便利他啊然后取出来数据然后再进行封装那这儿的话应该就是直接这个进行这个什么呀4一起这个便利了啊好咱接下来开始编写这里边的代码因为咱这一块最终要封装的是不是这个东西是不是这个东西对吧一个集合弹里边是范形
[13:17] 有这么一个范围那也说呢我们是不是得先new这么一个对象然后往里边封装数据封装完之后呢存到一个集合里边就搞定了所以你看我这呢得先new这么一个对象然后是不是开始往里边这个封装数据都封装哪些数据呢这个代码就不再给大家写了啊纯粹就是这个这个调一堆什么呀setter方法往里边扔数据就行了这个派息呢咱不需要啊咱现在用不着不用管它
[13:59] 这个变量名的话我们可以改一下啊对吧这个投资人用户编码佣金本金利息对吧你开始用封装这就封装完了封装完之后呢我们说是不是这个这个因为这是一个循环了这个对象也是多个我是不得给他保存到一个什么样集合里边这个集合的话我们是不是需要提前在这给他创建出来这个范形是不是就是这个类的然后呢我们起个名字叫
[14:35] 叫什么呀detail request等于near ar ar list好那基亚来的话在循环过程当中是不是应该是没有一个对象然后封装完数据之后我在这就要把它存到什么呀对集合里边第二什么呀add detail什么呀request加注释吧添加到什么呀集合哎对然后呢
[15:09] 然后呢这个集合有了之后我接下来是不是就可以进行什么呀进行封装了然后调用这个谁呀上面这个对象叫repayment requestrepayment request.应该是谁我们看一看是这个吧对不对然后呢就把这个集合放进去哎这块呢我们就封装完了那封装完之后呢我们直接把这个谁呀对
[15:40] 最终封装好的这个对象作为反正反而就想那这个方法我们封装好之后呢我们是不是就可以干什么呀是不是就可以在上面调用一下然后是不是就得到这个值了然后我们就可以作为参数给他扔进去去使用一下来咱看一看我可以在在哪呢在这对不对我们是不是要调用这个方法哎他要什么呀
[16:08] 两个参数啊对不对一个就是那个还款计划就是repayment plan还有一个是那个什么呀预处理流水号这个预处理流水号咋得的这预处理流水号呢我们可以在我们看看啊前面我们是不是没有没有取过那应该是在这里边啊repayment detail我们看这里边有没有应该就是这个啊应该是这个所以说呢我们就可以怎么着呢我们可以在这对不对
[16:44] 第二样我注意平板的底2点get你平板的底2啊第二get什么request number来得到这个值就行了嘛然后我们存起来tree p r e r e r e q u e s t对吧然后呢这个东西不就有了吗我们放到哪里啊对放到这里然后呢他是不是返回的一个一个什么一个值就是那个什么呀
[17:14] repayment request就是封装好的数据我们接收一下然后呢我们就可以把这个repayment request是不是做第二个参数往这一放哎搞定那咱整体看一看啊咱现在做的事情是什么呀是完善这个什么呀业务出发入口里边的代码大家看一下这是出发第一阶段代码的执行这是出发第二阶段那这呢是出发什么呀第三阶段
[17:44] 第三件呢我们主要出发了是不是就是让他发送这个消息这个消息一发他是不是就往后推了对不对往后推进了呃然后呢我们在调用这个这个发消息的这个方案的时候呢他是不是要两个参数吗一个是repayment plan这个好办是不是我们直接就有啊关键就是这个repayment request这个请求对象我们需要进行封装由于他里边呢这个数据比较多啊我们就单独什么呀
[18:11] 这个封装了一个方法在这里边呢对这个他要啥反正我们给啥呗封装成一个方法啊然后在这儿一定要方法得到这个对象啊然后放到这儿就可以作为参数使用了这是咱们这个什么呀第三阶段吧这个业务出发入口这一块我们也搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中实现还款业务的流程，包括生成还款明细、调用外部服务、处理结果并更新数据库状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示还款业务的时序图，包含多个步骤，如生成还款明细、调用外部服务、更新交易记录等。
画面2：时序图中，展示“2.1 发送确认还款事务请求”和“2.2 确认还款受理”等步骤。
画面3：在 IDE 中展示 `RepaymentServiceImpl.java` 文件，其中包含 `preRepayment` 方法，用于调用外部服务并返回结果。
画面4：展示 `RepaymentDetailRequest` 类的定义，包含多个字段，如 `userNo`、`commission`、`dividend`、`amount`、`interest`。
画面5：展示 `executeRepayment` 方法，其中调用 `preRepayment` 方法并处理返回结果。
画面6：展示 `generateRepaymentRequest` 方法，用于构造还款请求对象。
画面7：展示 PPT 页面，包含“还款明细信息请求数据”和“还款请求”等信息。
画面8：展示 PPT 页面，包含“还款请求”和“还款明细请求”等信息。
画面9：展示 `RepaymentServiceImpl.java` 文件，其中包含 `generateRepaymentRequest` 方法。
画面10：展示 `RepaymentServiceImpl.java` 文件，其中包含 `preRepayment` 方法。
画面11：展示 `RepaymentServiceImpl.java` 文件，其中包含 `generateRepaymentRequest` 方法。
画面12：展示 `RepaymentServiceImpl.java` 文件，其中包含 `preRepayment` 方法。
画面13：展示 `RepaymentServiceImpl.java` 文件，其中包含 `executeRepayment` 方法。
画面14：展示 `RepaymentServiceImpl.java` 文件，其中包含 `executeRepayment` 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
@Override
public Boolean preRepayment(RepaymentPlan repaymentPlan, String preRequestNo) {
    //1.构造请求数据
    UserAutoFreeTransactionRequest userAutoFreeTransactionRequest = repaymentService.generateUserAutoFreeTransactionRequest(repaymentPlan);
    //2.请求存管代理服务
    RestResponse<String> restResponse =depositoryAgentApiAgent.userAutoFreeTransaction(userAutoFreeTransactionRequest);
    //3.返回结果
    return restResponse.getResult().equals(RepositoryReturnCode.RETURN_CODE_00000.getCoode());
}
```

画面4：
```java
public class RepaymentDetailRequest {
    @ApiModelProperty(value = "还款人用户编码")
    private String userNo;
    @ApiModelProperty(value = "向投资人收取的佣金")
    private BigDecimal commission;
    @ApiModelProperty(value = "派息")
    private BigDecimal dividend;
    @ApiModelProperty(value = "投资人应得本金")
    private BigDecimal amount;
    @ApiModelProperty(value = "投资人应得利息")
    private BigDecimal interest;
}
```

画面5：
```java
public void executeRepayment(String date) {
    //查询到期还款计划
    List<RepaymentPlan> repaymentPlanList = selectDueRepayment(date);
    //生成还款明细
    repaymentPlanList.forEach(repaymentPlan -> {
        RepaymentDetail repaymentDetail = generateRepaymentDetail(repaymentPlan);
        //还款处理
        Boolean preRepaymentResult = preRepayment(repaymentPlan, repaymentDetail.getPreRequestNo());
        if (preRepaymentResult) {
            //未完结
            System.out.println("还款处理成功");
            repaymentProducer.confirmRepayment(repaymentPlan, repaymentDetail);
        }
    });
}
```

画面6：
```java
private RepaymentRequest generateRepaymentRequest(RepaymentPlan repaymentPlan, String preRequestNo) {
    //根据还款计划，获取还款明细
    Final List<ReceivablePlan> receivablePlanList = receivablePlanMapper.selectList(
            Wrappers.<ReceivablePlan>lambdaQuery()
                    .eq(ReceivablePlan::getRepaymentId, repaymentPlan.getRepaymentId())
                    .eq(ReceivablePlan::getRepaymentPlanId, repaymentPlan.getRepaymentPlanId())
                    .eq(ReceivablePlan::getRepaymentPlanStatus, repaymentPlan.getRepaymentPlanStatus())
                    .eq(ReceivablePlan::getRepaymentPlanType, repaymentPlan.getRepaymentPlanType())
                    .eq(ReceivablePlan::getRepaymentPlanNo, repaymentPlan.getRepaymentPlanNo())
                    .eq(ReceivablePlan::getRepaymentPlanName, repaymentPlan.getRepaymentPlanName())
                    .eq(ReceivablePlan::getRepaymentPlanDesc, repaymentPlan.getRepaymentPlanDesc())
                    .eq(ReceivablePlan::getRepaymentPlanStatus, repaymentPlan.getRepaymentPlanStatus())
                    .eq(ReceivablePlan::getRepaymentPlanType, repaymentPlan.getRepaymentPlanType())
                    .eq(ReceivablePlan::getRepaymentPlanNo, repaymentPlan.getRepaymentPlanNo())
                    .eq(ReceivablePlan::getRepaymentPlanName, repaymentPlan.getRepaymentPlanName())
                    .eq(ReceivablePlan::getRepaymentPlanDesc, repaymentPlan.getRepaymentPlanDesc())
                    .eq(ReceivablePlan::getRepaymentPlanStatus, repaymentPlan.getRepaymentPlanStatus())
                    .eq(ReceivablePlan::getRepaymentPlanType, repaymentPlan.getRepaymentPlanType())
                    .eq(ReceivablePlan::getRepaymentPlanNo, repaymentPlan.getRepaymentPlanNo())
                    .eq(ReceivablePlan::getRepaymentPlanName, repaymentPlan.getRepaymentPlanName())
                    .eq(ReceivablePlan::getRepaymentPlanDesc, repaymentPlan.getRepaymentPlanDesc())
                    .eq(ReceivablePlan::getRepaymentPlanStatus, repaymentPlan.getRepaymentPlanStatus())
                    .eq(ReceivablePlan::getRepaymentPlanType, repaymentPlan.getRepaymentPlanType())
                    .eq(ReceivablePlan::getRepaymentPlanNo, repaymentPlan.getRepaymentPlanNo())
                    .eq(ReceivablePlan::getRepaymentPlanName, repaymentPlan.getRepaymentPlanName())
                    .eq(ReceivablePlan::getRepaymentPlanDesc, repaymentPlan.getRepaymentPlanDesc())
                    .eq(ReceivablePlan::getRepaymentPlanStatus, repaymentPlan.getRepaymentPlanStatus())
                    .eq(ReceivablePlan::getRepaymentPlanType, repaymentPlan.getRepaymentPlanType())
                    .eq(ReceivablePlan::getRepaymentPlanNo, repaymentPlan.getRepaymentPlanNo())
                    .eq(ReceivablePlan::getRepaymentPlanName, repaymentPlan.getRepaymentPlanName())
                    .eq(ReceivablePlan::getRepaymentPlanDesc, repaymentPlan.getRepaymentPlanDesc())
                    .eq(ReceivablePlan::getRepaymentPlanStatus, repaymentPlan.getRepaymentPlanStatus())
                    .eq(ReceivablePlan::getRepaymentPlanType, repaymentPlan.getRepaymentPlanType())
                    .eq(ReceivablePlan::getRepaymentPlanNo, repaymentPlan.getRepaymentPlanNo())
                    .eq(ReceivablePlan::getRepaymentPlanName, repaymentPlan.getRepaymentPlanName())
                    .eq(ReceivablePlan::getRepaymentPlanDesc, repaymentPlan.getRepaymentPlanDesc())
                    .eq(ReceivablePlan::getRepaymentPlanStatus, repaymentPlan.getRepaymentPlanStatus())
                    .eq(ReceivablePlan::getRepaymentPlanType, repaymentPlan.getRepaymentPlanType())
                    .eq(ReceivablePlan::getRepaymentPlanNo, repaymentPlan.getRepaymentPlanNo())
                    .eq(ReceivablePlan::getRepaymentPlanName, repaymentPlan.getRepaymentPlanName())
                    .eq(ReceivablePlan::getRepaymentPlanDesc, repaymentPlan.getRepaymentPlanDesc())
                    .eq(ReceivablePlan::getRepaymentPlanStatus, repaymentPlan.getRepaymentPlanStatus())
                    .eq(ReceivablePlan::getRepaymentPlanType, repaymentPlan.getRepaymentPlanType())
                    .eq(ReceivablePlan::getRepaymentPlanNo, repaymentPlan.getRepaymentPlanNo())
                    .eq(ReceivablePlan::getRepaymentPlanName, repaymentPlan.getRepaymentPlanName())
                    .eq(ReceivablePlan::getRepaymentPlanDesc, repaymentPlan.getRepaymentPlanDesc())
                    .eq(ReceivablePlan::getRepaymentPlanStatus, repaymentPlan.getRepaymentPlanStatus())
                    .eq(ReceivablePlan::getRepaymentPlanType, repaymentPlan.getRepaymentPlanType())
                    .eq(ReceivablePlan::getRepaymentPlanNo, repaymentPlan.getRepaymentPlanNo())
                    .eq(ReceivablePlan::getRepaymentPlanName, repaymentPlan.getRepaymentPlanName())
                    .eq(ReceivablePlan::getRepaymentPlanDesc, repaymentPlan.getRepaymentPlanDesc())
                    .eq(ReceivablePlan::getRepaymentPlanStatus, repaymentPlan.getRepaymentPlanStatus())
                    .eq(ReceivablePlan::getRepaymentPlanType, repaymentPlan.getRepaymentPlanType())
                    .eq(ReceivablePlan::getRepaymentPlanNo, repaymentPlan.getRepaymentPlanNo())
                    .

