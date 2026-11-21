# day11-6-用户投标-功能实现5

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-6-用户投标-功能实现5_【海量资源尽在 666java.com】.mp4
- 时长 10分28秒（音频 628s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好刚才呢我们又增加了三个前置条件判断那截止到目前的话咱们的前置条件判断一共几个呀五个吧对吧你看这是一个两个三个四个五个那这五个前置条件判断啊搞定之后咱接下来就可以实现第二块功能就是
[00:29] 保存投标信息然后呢发送数据给存管代理服务咱接下来一个一个来我们把第二块也拆一下拆成两个步骤第一步呢就是保存投标对信息第二步呢就是什么呀发送数据给存管代理服务这块的话你可以
[00:57] 回顾一下实际图嘛你看这2.2和什么呀2.3吧你看这就是保存投标信息的对不对然后这呢就是干什么呀对把数据发到从管代理服务那边所以咱接下来要实现的就是这两块功能这两块都功能相来说比较简单但代码可能会比较多啊一会呢你就会知道我们要给很多值啊
[01:21] 首先咱说第一个功能吧保存投标信息保存投标信息无非就是把数据给存到哪个表里边对就是tender表就是这个表你看这这些数据是不是咱之前这个自己造的测试数据吧那咱一会儿把这个功能实现完之后呢就可以往这个表里边保存这个投标信息了那大家看一下这个表里边字段是不是也比较多对不对那要保存的话其实很简单我们直接溜一个是不是实体类对象然后通过setter方法
[01:51] 存一些值然后直接是不是就通过MP是吧就可以往表里边保存数据那咱看看讲义吧看讲义啊你看我们直接是不是就new了一个tender对象然后你看今下还是调用了一堆setter方法给值对吧给完值之后呢我们调用什么呀Mapper接口里边的insert方法哎就可以把这个对象的数据给保存到tender表里边
[02:19] 就这么简单当然呢它在保存的时候底层是不是通过什么呀sharding-gdbc是不是会遵循那个什么呀我们以前的分户分秒策略来进行保存那这块代码我就不在Ara给大家编写了因为它比较简单它只是说要给的值比较多一些而已那我就把这一块代码整个粘过来然后咱一起熟悉一下就行了咱们就粘到这儿吧咱一个一个来看看吧看这里边都封装了什么信息
[02:55] 首先我们往里边存了什么呀投标金额吧这个不再说了然后呢是投标人的用户ID用户名对不对投标人呢什么呀用户编码这些信息是不是都是从这获取到的啊从哪呢从前面这个地方咱们在做第二个这个前置条件判断的时候我们是不是得到了这个谁呀当前用户他的一些信息嘛对不对所以说你看下这一堆这个谁呀投标人呢这个什么呀
[03:25] 标识啊还有什么呀用户名啊编码啊都是从这儿获取的然后还有接下来就是标底的信息啊标底的标识标底的什么呀编码对不对还有这个谁啊投标状态而这个地方大家要注意一下投标的状态我们看现在给的这个状态是哪个状态啊咱瞅一眼是一个什么呀以冻结的状态对不对你看将来我们投标整个业务全部成功了之后会换成什么状态啊以放缓
[03:56] 目前是以冻结这是一个初始状态了创建时间当前时间吧然后呢请求流水号这个请求流水号大家应该有一像我们当时开户的时候是不是也有这个什么请求流水号就是凡是要跟存款代理服务打交道或者说跟银行存款系统打交道是不是都有这么一个流水号那我们看我们这个流水号的前缀跟之前有啥变化没有没啥变化就是那个发请求的那个流水号一个前缀啊
[04:25] 然后呢就是这个可用状态目前就是0吧将来会全部业务处理完之后会改成1是不是然后这是那个标底的名字就是那个什么左球先生第一次借款就这个就这个啊还有这个什么呀利率大概这几个属性的值我们需要给一给还挺多的然后呢这个数据给过之后呢我们直接调用这个tender map解构的insert方法就保存到了什么呀
[04:57] 这个腾在这个表里面啊所以说呢这个保存投标信息啊这个功能比较简单那这个咱要搞定接下来我们是不是要发送数据给存款代理服务了大家看这个图是不是就是2.3嘛对不对你看从交易中心发请求到哪到存款代理服务存款代理服务将来是不是要跟谁进行交货啊跟银行的存款系统交货所以说呢我们接下来
[05:25] 要在交易中心这边发请求到哪儿存在代理服务然后把它需要的一些数据给他干什么呀传过去那这个请求我们是不是还是通过飞这是微服务之间的这个相对远程调用吧我们通过飞那要想通过飞进行这个请求的话我们是不是得新建一个飞应代理接口对不对这个大家都比较熟了我们看看这个讲义大家看这他说呀我们是不是要发送数据给存在代理服务吗所以说需要新增一个什么呀
[05:56] 一个一个非印代理那我们就找到咱以前的这个depositoryargent APIargent对不对在这个接口当中新增一个方法将来我们调这个方法是不是就是相当于网什么呀网存款代理服务那边发请求传数据这个大家比较熟悉了我就不再给大家编写了我们找到这个argent包找到这个depositoryargent API这个接口然后粘过来
[06:29] 你看这个是不是咱以前发标那个时候造的这个fame这个代理对不对那咱现在又新增了一个新增了一个就是图标的时候用那这个地址呢大家要注意这个地址应该是存管代理服务那边的这个地址对不对等咱将来实现那一块功能的时候你再对照一下这个地址没写错就行然后呢这里边大家要注意当我们调了这个方法往这发请求的时候是不是有一个参数这个地方这个参数就是用来封装什么呀
[06:58] 我们给他传过去的数据了咱看看这里边他都要什么数据要什么数据啊你投标的金额呀请求的流水号啊投标人的这个什么呀编号啊你的这个业务是啥比如我们的业务就是投标对不对这个咱用用不着啊标底号我们要要传过去其他的这个有的咱暂时用不着大概这些信息吧就是存款代理服务那边需要要的我们封装到这个类当中了我们
[07:29] 到时候发请求的时候呢那传过去就行了所以说呢有了这个东西之后我们将来是不是调用这个方法就可以往往什么地方往存款代理服务那边发请求调这个方法多简单咱接下来在哪在这就可以调用对不对那就是depository是它吧点我们刚才刚加了一个方法就是这个方法那大家看你要调用这个方法你是不是得提前准备好这个对象了这个参数这个对象了所以说呢咱再
[07:58] 他之前还要创建一个对象然后往里边存数据这块代码呢我也不再给大家编写了大家看一下就这个地方构造请求数据对吧就是那个参数的那个类型直接拗一个然后他要查数据呢你就这样塞在方向往里边扔就行扔完之后呢放到这我们就发起这个远程调用好这块代码呢我就拿过来熟悉一下就行他就是多一些但是这个东西都不难
[08:31] 好咱一个一个过一遍吧首先我们就是直接六对象了对不对这个对象是不是就是封装这个请求数据的就是发给什么呀存款代理服务他的一些数据然后呢都有哪些数据呢你看我们刚才让大家瞅了一眼是不是这个投标的金额这个业务类型业务类型的话大家看一下我们的业务类型是投标啊他这应该是一个枚举哎咱点进去你看一眼就行是吧我们这个业务就是投标的业务嘛
[09:03] 然后还需要给的就是标底号标底号对吧project number还有那个我们前面生成的那个什么流水号啊还有投资人的这个编号对不对这些信息在前面都可以得到啊还有就是这个谁啊对这个投标的这个信息的ID主接主要就是要这几个值吧你通过setter方法一封装然后呢把这个对象往这儿一放
[09:34] 你调用这个方法是不是就发起了这个什么呀有什么调用那接下来是不是应该就是这个什么呀存款代理服务那边他应该去干什么呀他要什么生成签名啊要保存交易记录啊要这个访问什么呀银行存款系统啊对不对这些后续的处理咱还没实现了对不对后边咱就要实现那他处理完之后呢处理完之后呢他会返回给我们有结果呀对不对是不是那我们是不是要进行一个接收
[10:04] 处理完了一个结果再接受一下接受完之后呢我们是不是要从这里边取数据然后进行什么呀对进行一些数据的更新操作这个咱一会儿再实现这是目前吧咱们把第二块的这个功能就开发完了就是保存投标信息然后呢把这个数据呢发给谁啊发给存款代理服务了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示投标项目创建流程中，前端发起请求后，交易中心服务如何调用用户服务、存管代理服务和存管系统，完成投标信息的保存、冻结资金、更新状态等核心业务逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 ProjectServiceImp.java 中的投标金额校验逻辑，包括最小投资金额、剩余金额和冻结金额的判断，以及对应的异常抛出。
画面2：展示 ProjectServiceImp.java 中的投标金额校验逻辑，包括最小投资金额、剩余金额和冻结金额的判断，以及对应的异常抛出。
画面3：展示 PPT 中的投标信息设置代码，包括设置投标金额、投标人信息、标的编码、状态、创建时间等。
画面4：展示 PPT 中的投标信息设置代码，包括设置投标金额、投标人信息、标的编码、状态、创建时间等。
画面5：展示 ProjectServiceImp.java 中的投标金额校验逻辑，包括最小投资金额、剩余金额和冻结金额的判断，以及对应的异常抛出。
画面6：展示 UserAutoPreTransactionRequest 类的定义，包含冻结金额、请求流水号、投资人用户编码、预处理业务类型、红包金额、备注等字段。
画面7：展示 ProjectServiceImp.java 中的投标信息保存逻辑，包括创建 Tender 对象并设置相关属性。
画面8：展示 DepositoryAgentApiAgent 接口定义，包含 createProject 和 userAutoPreTransaction 两个 REST 接口。
画面9：展示 UserAutoPreTransactionRequest 类的定义，包含冻结金额、请求流水号、投资人用户编码、预处理业务类型、红包金额、备注等字段。
画面10：展示 DepositoryAgentApiAgent 接口定义，包含 createProject 和 userAutoPreTransaction 两个 REST 接口。
画面11：展示 PPT 中的投标信息设置代码，包括设置投标金额、投标人信息、标的编码、状态、创建时间等。
画面12：展示 ProjectServiceImp.java 中的自动预处理请求构造和调用逻辑，包括创建 UserAutoPreTransactionRequest 对象并调用 depositoryAgentApiAgent.userAutoPreTransaction()。
画面13：展示投标流程的时序图，包括用户APP、交易中心、用户服务、存管代理服务、存管系统之间的交互流程。
画面14：展示 ProjectServiceImp.java 中的投标信息保存逻辑，包括创建 Tender 对象并设置相关属性。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//1.3 判断标是否是满标，标的的状态为NULL就表示满标
Project project = getProjectInvestDTO.getTid();
if(project.getProjectStatus().equalsIgnoreCase(anotherString: "FULLY")){
    throw new BusinessException(TransactionErrorCode.E_150114);
}
//1.4 判断投标金额是否达到未投标金额
BigDecimal remainingAmount = getProjectRemainingAmount(project);
if(amount.compareTo(remainingAmount) < 0){
    throw new BusinessException(TransactionErrorCode.E_150114);
}
//1.5 判断此次投标后的剩余金额是否满最小投标金额
//借款人需要信  现在已经投标了 5T  还剩 18900元
//公式：此次投标后剩余金额 - 目前剩余金额 = 本次投标金额
BigDecimal subtract = remainingAmount.subtract(amount);
int result = subtract.compareTo(configService.getTinInvestmentAmount());
if(result() < 0){
    throw new BusinessException(TransactionErrorCode.E_150114);
}
```

画面2：
```java
//2.1 保存投标信息并发送给存管代理服务
//2.2 发送数据给存管代理服务
//2.3 根据结果更新投标状态
else{
    throw new BusinessException(TransactionErrorCode.E_150110);
}
```

画面3：
```java
Final Tender tender = new Tender();
// 投资人投标金额，投标冻结金额
tender.setAmount(amount);
// 投标人用户标识
tender.setConsumerId(restResponse.getResult().getId());
// 投标人用户名
tender.setConsumerUsername(restResponse.getResult().getUsername());
// 投标人用户编码
tender.setUseNo(restResponse.getResult().getUseNo());
// 标的标识
tender.setProjectId(projectInvestDTO.getTid());
// 标的编码
tender.setProjectNo(project.getProjectNO());
// 标的状态
tender.setTenderStatus(TradingCode.FROZEN.getCode());
// 创建时间
tender.setCreateDate(LocalDateTime.now());
// 请求流水号
tender.setRequestNo(CodeOutUtil.getNo(CodePrefixCode.CODE_REQUEST_PREFIX));
// 可用状态
tender.setStatus(0);
// 标的项目名
tender.setProjectName(project.getName());
```

画面4：
```java
Final Tender tender = new Tender();
// 投资人投标金额，投标冻结金额
tender.setAmount(amount);
// 投标人用户标识
tender.setConsumerId(restResponse.getResult().getId());
// 投标人用户名
tender.setConsumerUsername(restResponse.getResult().getUsername());
// 投标人用户编码
tender.setUseNo(restResponse.getResult().getUseNo());
// 标的标识
tender.setProjectId(projectInvestDTO.getTid());
// 标的编码
tender.setProjectNo(project.getProjectNO());
// 标的状态
tender.setTenderStatus(TradingCode.FROZEN.getCode());
// 创建时间
tender.setCreateDate(LocalDateTime.now());
// 请求流水号
tender.setRequestNo(CodeOutUtil.getNo(CodePrefixCode.CODE_REQUEST_PREFIX));
// 可用状态
tender.setStatus(0);
// 标的项目名
tender.setProjectName(project.getName());
```

画面5：
```java
//1.3 判断标是否是满标，标的的状态为NULL就表示满标
Project project = getProjectInvestDTO.getTid();
if(project.getProjectStatus().equalsIgnoreCase(anotherString: "FULLY")){
    throw new BusinessException(TransactionErrorCode.E_150114);
}
//1.4 判断投标金额是否达到未投标金额
BigDecimal remainingAmount = getProjectRemainingAmount(project);
if(amount.compareTo(remainingAmount) < 0){
    throw new BusinessException(TransactionErrorCode.E_150114);
}
//1.5 判断此次投标后的剩余金额是否满最小投标金额
//借款人需要信  现在已经投标了 5T  还剩 18900元
//公式：此次投标后剩余金额 - 目前剩余金额 = 本
```

画面6：
```java
@Model
public class UserAutoPreTransactionRequest {
    @ModelProperty("冻结金额")
    private BigDecimal amount;
    @ModelProperty("请求流水号")
    private String requestNo;
    @ModelProperty("投资人用户编码")
    private String userNo;
    @ModelProperty("预处理业务类型")
    private String bizType;
    @ModelProperty("红包金额")
    private BigDecimal preMarketingAmount;
    @ModelProperty("备注")
    private String remark;
    @ModelProperty("请求流水号")
    private String requestNo;
}
```

画面7：
```java
//2.1 保存投标信息并发送给存管代理服务
final Tender tender = new Tender();
// 投资人用户标识
tender.setConsumerId(restResponse.getResult().getId());
// 投标人用户名
tender.setConsumerUsername(restResponse.getResult().getUsername());
// 投标人用户编码
tender.setUseNo(restResponse.getResult().getUseNo());
// 标的标识
tender.setProjectId(projectInvestDTO.getTid());
// 标的编码
tender.setProjectNo(project.getProjectNO());
// 标的状态
tender.setTenderStatus(TradingCode.FROZEN.getCode());
// 创建时间
tender.setCreateDate(LocalDateTime.now());
// 请求流水号
tender.setRequestNo(CodeOutUtil.getNo(CodePrefixCode.CODE_REQUEST_PREFIX));
// 可用状态
tender.setStatus(0);
// 标的项目名
tender.setProjectName(project.getName());
```

画面8：
```java
@FeignClient(value = "depository-agent-Service")
public interface DepositoryAgentApiAgent {
    @PostMapping(value = "/depository-agent/1/createProject")
    public RestResponse<String> createProject(ProjectDTO projectDTO);
}
```

画面9：
```java
@Model
public class UserAutoPreTransactionRequest {
    @ModelProperty("冻结金额")
    private BigDecimal amount;
    @ModelProperty("请求流水号")
    private String requestNo;
    @ModelProperty("投资人用户编码")
    private String userNo;
    @ModelProperty("预处理业务类型")
    private String bizType;
    @ModelProperty("红包金额")
    private BigDecimal preMarketingAmount;
    @ModelProperty("备注")
    private String remark;
    @ModelProperty("请求流水号")
    private String requestNo;
}
```

画面10：
```java
@FeignClient(value = "depository-agent-Service")
public interface DepositoryAgentApiAgent {
    @PostMapping(value = "/depository-agent/1/createProject")
    public RestResponse<String> createProject(ProjectDTO projectDTO);
    @PostMapping("/depository-agent/1/user-auto-pre-transaction")
    RestResponse<String> userAutoPreTransaction(UserAutoPreTransactionRequest userAutoPreTransactionRequest);

