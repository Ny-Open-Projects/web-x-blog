# day11-4-用户投标-功能实现3

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-4-用户投标-功能实现3_【海量资源尽在 666java.com】.mp4
- 时长 13分22秒（音频 802s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才我们是不是做了两个准备工作第一个准备工作呢是在Apollo上配置了咱们P2P平台规定的最小投标金额对不对还有一个准备工作呢就是在用户中心这边实现了查询账户余额的功能那这两个准备工作做好之后呢咱接下来就开始实现这俩功能就是判断啊投标金额是否大于最小投标金额判断
[00:31] 账户的余额是否充足那接下来实现了这些功能呢我们是不是就应该写到这个什么地方来就该写到project Service mpr里吧是这吧因为咱刚才是不是定了一个接口这该实现功能了对不对那咱首先实现的第一个功能不一了啊我们这是在叫叫什么呀叫前置条件什么呀判断
[01:03] 第一个这个条件判断就是判断什么呀对投标金额是否大于什么呀最小投标金额第二个判断就是什么呀对判断用户账户余额是否足够来一个一个来吧首先搞定这个什么呀判断投标金额是否大于最小
[01:38] 投标计划那咱是不是导到这两个金额就行了一个是投标金额一个是最小投标金额是不是那咱先导到这个什么呀投标金额投标金额在哪投标金额不就是这个地方是不是前端传过来这个一万块钱吧是不是那我们前面在定义接口的时候说过这个前端在点击这个按钮是发了一个请求那他传过去了就有这个投标金额这个金额会封装到哪呀对其实就封装到这个DTO对象里边了吧那看一下
[02:08] 这个投标进口那这个就简单了我在这直接就可以干什么呀通过这个谁啊参数直接get方法就得到了这个什么呀对投标进口那我们这稍作处理我们要把它封装成这个big decimal这种类型我们其个名叫amount吧直接new啊这是一个一个对象然后呢我们把
[02:44] 咱们这个投标金额呢给它放进去给它封装成这个big decimal这种类型的对象就行了这是什么呀什么金额投标金额获取到投标金额获取到之后我们需要获取最小投标金额我们前面说了这个最小投标金额我们是配到阿卜罗上那在这个地方我们怎么获取到你要么通过Advalo租借注进来要么通过我们以前用过的这个东西这个你还有印象吗Configure Service
[03:14] 有印象没有我们这里边这个代码是咱提前给大家准备好通过这个方法我们就可以导到这个阿卜罗上配置的这个最小投标镜这个configure Service大家在呃他是放在我看这是交易中心是吧交易中心这个咱以前用过应该是在Service包里边就是这个这个大家有印象吗
[03:45] 对这是我们封装好的一个类码可以从Apollo上取那些配置的这个值的啊我们刚才调的方法就是这个获取最小投标金额这是咱刚才在Apollo里边配着的那个那个那个配置项了对不对所以说我们在这呢就直接得到了这个什么呀对直接得到这个最小投标金额然后接下来是把他俩要比一比对不对啊那我这得先接收一下呀嗯我们起个什么名字呢就起这样一个名字吧
[04:21] 这个稍微有点长那咋比啊接下来咋比他俩直接剪吗那可不行啊咱前面说过了这个是这这这这可不是什么呀普通的这个基本数学类型这是呃这是类是吧是对象啊big decimal怎么比呢那我们就要用到这个compare to方法那我应该怎么写呢应该是这么子来写的要用他的compare to方法这个在
[04:55] 加上基础当中应该是学过这个方法大家应该有印象吧给我们用compare2那这个结果怎么判断呢等于0的时候是不是表示这两个值是相等那如果是小于0呢小于0的话就说明前面这个知晓就是投标金额呢小于了什么呀我们规定的最小投标金额那这时候呢怎么办怎么办怎么办呢我们跟以前一样po异常
[05:25] 抛出我们自定义的那个什么呀business这个错误码的话我们就用这个transaction error code里边我们挑一个吧看看咱准备好的哪个比较合适呢是不是有这个吧投资金额小于最小投标金额对不对那就他的就他的那这事咱就办是不是第一个判断就搞定那接下来咱搞定第二个判断就是什么呀
[05:56] 对这个用户的账户余额是否充足那大家想一下这个账户余额是否充足我们是不是得先得到这个账户余额然后才能比较对吧这个账户余额咋得到账户余额咱在刚才是不是已经实现过这个功能这个功能在哪实现的呀是不是在consumer那边是不是你看我们刚才在这定义的接口是不是在Controller里边是不是实现了这个方法嘛对不对是不是
[06:25] 那但是我们现在这个代码是在哪是在交易中心啊那这个时候就意味着我们要在交易中心远程去访问谁consumer然后就可以得到这个什么呀章鱼了那这个时候就要用到什么用到飞通过飞发起远程调用所以说呢我们在实现第二个判断的时候呢我们需要做这么一件事就是说我们需要在consumer API而进它这个接口当中呢新增这么一个方法就是获取什么呀
[06:56] 这个查询当前余额的这么一个方法就是通过非议码这个大家比较熟悉我就不再编写了那我们就找到这个谁啊阿尔金哪个阿尔金的呀我们是不是访问这个卡丘玛的对不对在这里边我们在这再增加一个就行了有了这个我们是不是一调用这个方法就可以发起这个非议远程调用了是不是就可以得到这个什么呀余额了这个分号
[07:29] 注意这个consumer这一层要加上啊好那这个工作做完之后呢我们是不是就可以干什么呀通过这个fine代理对象调用这个方法来获取什么呀对获取账户余额那获取哪个账户的这个余额呢是不是他是不是要一个user number吗这个user number从哪来对不对想一想你要得到的是不是当前登录用户的这个余额是吧
[08:01] 那当前登录用户怎么得到这个大家还有印象吗我们以前是不是有个工具类叫叫叫什么呀S怎么写SECSecurityUtil对吧那封装好了吗以前也用过GETUTER通过这个方法我们就得到了当前的登录用户啊嗯他返回来应该是一个什么呀login user是不是loginuser哎我们接收一下
[08:32] 你看你这就得到了当前登录用户然后就可以调他的什么呀方法他要的是什么呀他要的是那个谁啊user number吧我记得对不对get user number找一找哎没有user number吗呃那这个login user这里边还的确是没有提供这个user number但是他是不是有手机号对不对那咱这样咱根据手机号做一次查询吧好吧
[09:02] 查一下优势对象然后这个优势对象里边肯定有优势对象是不是那这个也简单你看咱以前在这个非硬代理里边是不是有现成的这这这个就给你手手机上查询这个卡这边对象对不对那咱们就在这用一下啊看suma而进它点这个get convert consumer对不对然后呢我们就是user点get什么呀我不要这边我查了一下这个
[09:32] consumer对象了对不对你看他返回的是什么consumer DTO我们接收一下就是他接收一下接收一下之后我们从这里边把结果给他干什么取出来应该是get result对吧然后再点我们就可以get谁user你看就有个number是不是
[10:06] 我们就可以把这个东西呢直接放到这儿这就完事了好大家看一下啊就是说呢我们通过这个工具类呢可以指的直接得到当前这个东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东东
[10:37] user number明白什么意思吧又又多了一次这个这个发起这个呃非影响调用的这么一个步骤啊那这时候我们是不是又得到了这个什么呀对就得到了这个怎么说呢用户余额啊当然那他是封装到这么一个对象里边了啊所以在这呢我们也需要接收一下嗯我们就叫这个名字吧
[11:07] 那接收到之后接下来我们是不是要从这里边把这个用户的余额信息给他干什么呀对取出来啊怎么取呢那他不就是rest response吗我们要down get result然后再get这个谁啊就是他呗是不是这就是用户的余额信息我们就拿到手了我们是要用big decimal来接收一下那咱起个名字叫myb a l a n c e吧
[11:38] 我们这么接受一下那现在是不是该要的数据都拿到手了这是用户的余额那我们怎么判断用户的余额是否足够他是跟谁比跟谁比是不是跟你的这个谁跟本次投标金额比如说你要投1万而你的余额只有5000那就是不够嘛对不对那投当前的这个投标金额不就是这个吗是不是就是他那他俩是不是要比一下怎么比
[12:07] 那跟上面这个不应该是一样的吗对不对也是一个一幅然后通过什么呀compare to然后呢我们比一下这个就是怎么写啊my balance对不对然后点compare to和谁啊对还是跟这个投标近那如果说是小于零的就证明是不是这个余额小了对不对就余额不够了吗不够这个这个
[12:38] 投本子标了所以说这个时候怎么办这个时候跟上面一样我们抛一场抛一场这个错误码我们挑一个这个错误码应该是就这个用户余额不足请充值大家看没错对不对所以你看目前我们就把什么两个前置条件判断的工作给搞定了一个是判断投标金额是否大于最小投标金额
[13:13] 一个是判断用户账户的余额是否足够这是这块功能咱就开发到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现投资标创建前的最小投资金额校验和用户余额校验逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构和代码，说明A：检查Apollo是否配置最小投标金额（配置项为mini.investment.amount=100.0），B：实现查询用户余额功能，C：在ConsumerController中实现该方法。
画面2：展示代码中判断投标金额是否大于最小投标金额的逻辑，以及用户余额查询的逻辑。
画面3：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面4：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面5：展示ConfigService类中获取最小投资金额的配置方法，从Apollo配置文件读取。
画面6：展示代码中抛出BusinessException异常的逻辑。
画面7：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面8：展示代码中判断用户余额是否足够，如果不足则抛出异常。
画面9：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面10：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面11：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面12：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面13：展示代码中获取用户余额的逻辑，通过ConsumerAgent调用。
画面14：展示代码中判断用户余额是否足够，如果不足则抛出异常。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
A: 检查Apollo是否配置最小投标金额
已配置 mini.investment.amount 100.0
最小投标金额
B: 实现查询用户余额功能，在ConsumerAPI接口中新增查询当前余额的方法：
/**
获取当前应用用户余额信息
@param userNo 用户编码
@return
*/
RestResponse<BalanceDetailsDTO> getBalance(String userNo);
C: 在ConsumerController类中实现该方法：
@Override
@ApiOperation("获取用户可用余额")
@ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "string")
@GetMapping("/1/balances/{userNo}")
public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable string userNo) {
return balanceFromDepository;
}
画面2：
@Override
public TenderDTO createTender(ProjectInvestDTO projectInvestDTO) {
//前置条件判断
//1.判断投标金额是否大于最小投标金额
BigDecimal amount = new BigDecimal(projectInvestDTO.getAmout());
BigDecimal miniInvestmentAmount = configService.getMiniInvestmentAmount();
if (amount.compareTo(miniInvestmentAmount) < 0) {
throw new BusinessException(TransactionErrorCode.E_150109);
}
//2.判断用户账户余额是否足够
画面3：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面4：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面5：
public BigDecimal getAnnualRate() {
return getBorrowerAnnualRate().subtract(getCommissionAnnualRate());
}
//最小投标金额
public BigDecimal getMiniInvestmentAmount() {
//如配置文件中没有就默认，这些项目都配置 100.0，可以使用配置文件的
return BigDecimal.valueOf(config.getProperty("key:mini.investment.amount", "100.0"));
}
画面6：
if (amount.compareTo(miniInvestmentAmount) < 0) {
throw new BusinessException(TransactionErrorCode.E_150109);
}
画面7：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面8：
//投资者要投的金额 string -> BigDecimal
BigDecimal amount = new BigDecimal(projectInvestDTO.getAmout());
//判断金额是否符合最小投标
final BigDecimal miniInvestmentAmount = configService.getMiniInvestmentAmount();
//业务判断
if (amount.compareTo(miniInvestmentAmount) < 0) {
log_warn("投标金额小于最小投标");
throw new BusinessException(TransactionErrorCode.E_150109);
}
画面9：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面10：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面11：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面12：
private BigDecimal getProjectRemainingAmount(Project project) {
//根据标的，在投标表查询已控金额
List<BigDecimal> decimalList =
tenderMapper.selectAmountInvestedByProjectId(project.getId());
画面13：
if (amount.compareTo(miniInvestmentAmount) < 0) {
throw new BusinessException(TransactionErrorCode.E_150109);
}
画面14：
if (amount.compareTo(miniInvestmentAmount) < 0) {
throw new BusinessException(TransactionErrorCode.E_150109);
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“2.2 实现前置条件判断”，内容包括：
- 投资者要投的金额 string -> BigDecimal
- 判断金额是否符合最小投标
- 获取最小投标金额
- 业务判断
- 如果金额小于最小投标，抛出异常
画面8：PPT标题为“2.2 实现前置条件判断”，内容包括：
- 投资者要投的金额 string -> BigDecimal
- 判断金额是否符合最小投标
- 获取最小投标金额
- 业务判断
- 如果金额小于最小投标，抛出异常
画面14：PPT标题为“2.2 实现前置条件判断”，内容包括：
- 投资者要投的金额 string -> BigDecimal
- 判断金额是否符合最小投标
- 获取最小投标金额
- 业务判断
- 如果金额小于最小投标，抛出异常

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

