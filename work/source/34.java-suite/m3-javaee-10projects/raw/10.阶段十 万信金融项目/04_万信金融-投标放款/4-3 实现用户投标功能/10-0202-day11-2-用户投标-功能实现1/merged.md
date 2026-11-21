# day11-2-用户投标-功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-2-用户投标-功能实现1_【海量资源尽在 666java.com】.mp4
- 时长 18分42秒（音频 1123s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把接口4和接口5这两个接口呢定好定好之后呢咱接下来就按照接口来实现功能那按照顺序咱应该先实现接口4这个功能对不对那这个功能呢咱大概回顾一下它具体是要实现什么功能是不是前端要从这开始对不对点击这个确认出界按钮然后呢就会发一个请求
[00:30] 对吧就到交易中心了那么交易中心这边要实现啥功能呢那我们这个图里边说了是只是实现一个什么呀保存这个投标信息那实际上咱一会实现的时候你会发现这块的这个业务非常非常复杂我们在保存这个投标信息之前呢还有很多工作要做咱这个图里边只是提到了这个什么呀保存投标信息这一项功能而已因为我们把所有的功能都累到这个
[00:58] 图当中这个这个就就有点影响这个整个图的这个这个效果所以说我们这只列出来一个功能那咱接下来这个代码从哪开始咱们这个DAO层的代码是不用编写了那些Map接口啥的咱之前该编写都已经编写过了那咱直接就是从要层开始要层呢咱也是在接口当中是不是新增一个方法叫CreditsTender也就是用户投标嘛我们先来在这里边
[01:30] 就要保存这个投标信息这个其实就是右层的这个接口那我们就给它粘过来直接呢找到对右层的这个接口在这里边呢我们新增一个方法好这是这个方法大家瞅一眼吧发名字叫create tinder那么这个参数呢咱定义接口的时候让大家瞅过一眼这里边是不是就是前端传过来的一个标底的ID和一个投标金额吧
[02:09] 然后我们整个全部处理完之后呢会返回给Controller数据是不是这个数据呢我们会封装到tender DTO里边到时候用到时候再说吧这里边反正这个各种各样的信息全部都有这是要从的接口才能搞定搞定之后呢我们接下来就需要在实现类当中实现这个方法那咱先把这个方法生成一下那在这里边我们是不是就该实现哪一块的功能了呀
[02:43] 对该实现接口四这个功能那接口四这个功能你看咱当时定义接口的时候你瞅瞅你看这里边一下子有几个功能九块小功能其实还是很多的你看咱保存这个投标信息是不是只是其中之一对不对在保存之前有很多工作要做那你看就像咱蒋毅当时说了说这这个又非常非常复杂我们要拆翻成若干部分一个一个来所以这个大家要这个有点心理准备
[03:13] 那首先是这样我们在保存这个投标信息之前呢我们有很多这个前置条件的这个判断工作要做你比如说我们要判断什么呀投标金额是否大于最小投标金额还有这个用户的账号余额是否足够对不对我们有很多这个条件要判断这个判断都通过了我们在进行什么呀对信息的一个保存所以说呢咱把整个这个复杂业务拆成一块一块实现啊
[03:43] 那咱先实现的就是这一块就是前置条件判断的一个准备工作那就是这两个工作啊这两个工作呢我们单独给大家解释一下首先就是说呢对于P2P平台来说啊它都有一个最小投标金额的一个规定啥意思呢你比如说你作为投资人你想投标你不能投一块钱吧你不能投十块钱吧这个我觉得这个没这个必要就不要凑这个任劳了对不对那我们P2P平台肯定有个规定比如说
[04:14] 你要投资最少得1000块钱起是不是啊所以说呢我们要判断啊你这个投标金额是否满足我们P2P平台这个要求这个大家应该能明白什么意思吧那第二个这个大家都能理解你账户有个够我比如说我要投1万块钱对不对哎这个投标的时候哎我们一检查发现你账户里边就5000块钱对不对那你肯定不能投标啊是不是所以说呢这些东西都是我们首先要进行的一些什么呀条件判断
[04:46] 那咱现在先做一些准备工作比如说我们这个最小投标金额怎么获取到我们刚才说了这个最小投标金额是不是P2P平台的一个规定对不对那这个东西我们会配到Apollo里边把它做一个配置项放到Apollo里边那你将来在什么地方用比如说你将来要判断对不对这个投标金额是否大于这个最小投标金额那你在实验这个功能的时候就从Apollo上导到这个值然后就可以进行判断
[05:16] 所以说我们接下来做的第一个准备工作就是你要检查你的阿布罗上是否做了这个配置啊就是最小投资金额的这个配置这个配置呢我们要放到这个放到交易中心里面你看我这边都已经配过你的有没有配你要检查啊在application里面我给你找找啊是哪一项就这一项就这一项大家看到了我们这个平台规定最小投资金额是多少啊100
[05:50] 你只要手里边有100块钱就可以来我们P2P平台进行投资门槛非常低所以你要把这个配置给加上这个我们将来要用这个值就是100这个值这是一个准备工作非常简单那第二个准备工作大家看这我们将来是不是要判断这个账户的余额够不够那你要判断这个功能你首先是不是得先查出来当前这个用户账户还有多少钱是不是
[06:19] 所以我们接下来要做一个准备工作就是实现查询当前用户的账户余额功能那将来我们在这判断的时候就可以用那我们要想查询账户的余额那得去哪查呀你得去哪查账户的余额用户的余额对不对我们得去consumer用户中心网站发请求去查询所以我们接下来呢要把这个功能给实现一下就从这开始我们要实现
[06:52] 查询账户余额的功能那这个呢是一个小功能啊我就不再单独分析了它就是查询当前用户的一个一个账户余额啊所以我们就直接快速的把这块代码给编写完那套路跟以前一样还是在consumer API的接手当中我们要新增这么一个查询当前余额的什么呀方法对不对还是先定义接口我们找一找这个API里边的谁呀对
[07:22] consumer我们查询用户余额呢是通过consumer用户中心来查好我们缺一个这个DTO类是不是我们把它粘过来了去资料文件夹里面找一下就是它我们看粘到什么地方API consumer好我们直接给它粘过来就是这儿了好粘过来之后呢咱们接下来一起看一看这个方法就是获取当前用户余额的这个方法名字见名之义对不对
[07:56] 然后呢这个参数不用说了就是用户的这个什么编号啊就是用户的那个唯一标识然后查出来的余额信息大家能看出来是不是封装到这个DTO对象里面那这里边都有啥呢咱可以看一看用户相关的一些信息呗用户的标识用户的编码对吧这个啊不是这比如说这个就是咱想用要的那个值吗就是可用余额对不对啊该有的信息这里边都封装好是不是这是接口咱要定义好
[08:27] 接手定义好之后接下来是不是该实现方法那咱现在Controller里边先来一个空实现consumerconsumer里边的Controller对不对我们找一找找一找Controller他现在应该要报错了Controller我们把这个方案先生成一下呗就这个方法我们把一些注解先给他加上Spark的注解啊Spark mvc的一些注解我们先给他加上
[09:06] 包括这个pass variable对不对我们都要加进来加到这个地方大家看一下他这个这个用户的编号他是不是通过这个在路径里边就传过来对于resful风格我们这要加一个注解pass variable这个不再说了那咱接下来就要实现这个功能咋实现这个功能呢大家想这个余额去哪查要想老师你这很明显在在consumer里边查你这个代码都在
[09:39] consumer这个微服里边写着呢你肯定去consumer里边查那咱打开数据库找到这个谁啊consumer这个表咱看看这个表里边有没有咱想要的这个什么样的余额信息看一看有吗没有没有这个余额不在consumer表里边但是呢这个余额它是属于用户的余额所以从页上来讲咱要查询用户的余额还得通过谁啊通过通过这个用户中心
[10:12] 但是呢其实用户中心里边它是不包含这个什么呀余额信息的那余额在哪你说余额在哪大家想余额在哪余额保存在银行存款系统当中咱当时开户的时候说了嘛他要开通两个账户其中一个账户是不是就是银行存款系统账户那我们的余额信息是在银行存款系统里边保存着明白什么意思吗所以我们现在要想查询
[10:44] 用户的余额信息我们需要通过用户服务往哪发请求啊对往存款系统这边发请求来查询这个余额信息那有个学员会说老师我们以前不是说过吗凡是跟银行存款系统打交道都要先通过谁啊存款代理服务对不对那你这个你刚才说要在用户中心直接就去访问存款系统来查这个用户余额吗对没错那为什么我们这一次不通过存款代理服务呢因为咱这个只是查一下用户的余额不是交易
[11:14] 对不对我们不是开户不是发标不是投标不是做交易的只是查个数据而已啊所以说呢我们就准备在用户服务中这边直接就发请求到哪银行存款系统直接去查这个用户的余额就行了说这个呢我们要给大家说一说具体怎么实现呢这个代码不要求大家实现你直接拿过来用就行了啊大家看一下呃我们单独封装了一个方法就是这个方法
[11:45] 那这个方法里边呢大家这个代码大家大概都能看懂啊你看这儿是不是就是获得那个谁啊对获得那个银行存款系统的那个基本法路径啊咱以前都写过然后呢这个接口啊或者这个路径其实就是用来查询对用户余额信息的然后呢我们把当前这个用户的这个编号是不是传给他他就能查这个用户的什么余额信息我们发起这个请求呢还是用咱之前提到过的okhttpclient
[12:16] 通过他怎么着啊对从用户中心这边直接发请求到银行存款系统请求过去之后那边就会进行查询查询出来的结果呢会返回给我们在这啊response对不对然后呢我们解析这个结果从这里边呢我们就能拿到这个谁啊拿到我们想要的这个用户移过他把相关的信息就封装成这个DTO对象大家看这封装成这个对象然后呢再封装成rest response
[12:46] 然后返回给啥返回给我们用户中心所以我们这儿是单独封装成的一个方法你直接把这个方法给他拷过来直接用就行了因为这跟这是要跟呃银行那边打交道的而银行那边系统呢并不是咱开发的啊所以这个代码大家就不用过我们直接你就直接粘到这个这个control了这这个地方就行了直接伸过来就行了咱这里边缺的一些东西呢咱一会要补啊一会要补一补
[13:17] 这边可能会缺一些类啊或者需要倒一些包对不对这些事情咱一会儿再说啊那我有了这个方法之后大家想一下我是不是应该在这个地方调用一下这个方法这个查询用户余额这个功能是不是搞定了对不对你看一下咱们的讲义你看有了这个方法之后你看这我在这是不是control了这个方法里面是不是直接就调用这个方法就导到这个这个我们想要的这个DTO对象了
[13:45] 那么这个用户的余额是不是就封装到了这个什么呀DTO对象里面所以说呢咱接下来把这块代码给补一下就行了就这个地方我们直接是不是调用这个方法就行然后呢把这个用户的编号给他对给他传进去然后他反而的是什么呀他反而的是rest response那你看我们需要返回给前端的是不是正好就是一个这样一个东西对不对
[14:15] 你看咱简单里边是声明一个变量接收了一下我这就不再接收了直接就返回了一步到位完事那我在这直接就可以什么呀对return你看什么意思吧哎就是将来呢我们要往这发请求是不是然后呢调用这个方法在这个方法里边呢我们又调用这个方法这个方法里边呢是不是通过okhttp client往银行存款系统发请求然后呢得到了什么呀用户余额封装了dto对象里边
[14:45] 然后呢我们在这儿就接收住接收住之后呢直接返回给谁啊对返回给调用方当然他不他不应该是前端啊不应该是前端应该是交易中心嘛是不是啊应该是交易中心啊就返回他了他这个想怎么用怎么用这个就是他那边的事啊说这是这块功能然后呢咱接下来你看这里边是不是还缺一些东西需要我们进行倒包的我们倒一倒啊我们先看这个request我们先倒一下包啊我们应该倒这个ok http是不是
[15:15] response我们也需要懂response也是ok utp的这个log日志的话你不想写的话你可以先把它干掉我们这里边是不是没有加那个serv4g是不是好我们把这个加上吧加上之后呢我们再瞅瞅这个还有这个东西是不是需要我们诸一下对不对或者说获取一下然后给他在这个地方去干什么去使用呢
[15:51] 咱把这个值给获取一下吧这个值咱以前在实现开户工程的时候都搞过是不是通过这个谁呀at value注解我们就可以拿到手对不对private应该是一个字符串类型吧是吧那我们这个地方的这个值你还有印象吗这个值这个值应该怎么写啊这里边一个dollar符号一个大果号吧对不对这里边的那个名字我们看看
[16:23] 查查Apollo吧我们也想不起来了我们找一找这应该是用户中心是吧他从用户中心取这个这个这个值呢我看用中心配的有没有用中心还没有配呀是不是还没有配的话那你就参考哪呢我想想啊你像这个从外带里服这边应该配的有吧你可以把它粘过来我们瞅一瞅是这个值吧对不对对就是他
[16:54] 我们怎么着呢我们这样文本是不是然后就是这个东西哎我们复制一下复制完之后呢我们回到这个卡丝幽默这边然后呢把这个配置呢给他加上新增配置嗯那这样吧通过这种方式编辑将过来对不对提交发布发布
[17:22] 这个事情我们就准备好了那就把这个值给他干什么呀对考过来往这一放这个就搞定这样搞定之后接下来还有一个错误还有一个问题就是这个对象okhttp这个对象怎么办这个对象我们直接在这扭啊直接在这扭啊怎么扭呢我们就是privateokhttp
[17:52] 应该是他对然后呢在这呢我们就直接拧一个okhttp client这么子拧还不行我们需要调用他的一个new builder方法先造一个构造器然后再通过构造器的build方法哎就得到了这个okhtt client对象通过他就可以发请求了你看这俩东西一补上这块代码是不是就没问题了对不对
[18:20] 那截止到目前吧咱就把什么功能给搞定了咱看一看讲义啊两个准备工作啊一个是在Apollo上配置了这个什么呀最小投标金额将来判断的时候我们就可以用了还有一个就是我们实现了查询用户的什么呀这个账户余额功能将来判断的时候也可以用

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在微服务架构中实现投标功能，包括定义数据模型、编写服务接口与实现、调用存管系统查询用户余额，以及通过 Apollo 配置中心管理相关配置。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了“用户投标业务流程图”，图中包含“浏览器APP”、“交易中心”、“用户服务”、“存管代理服务”、“存管系统”五个模块，通过编号步骤描述了从用户发起投标到存管系统更新账户余额的完整流程。
画面 2: 展示了 IDE 中的 `TenderDTO.java` 文件，定义了投标数据传输对象，包含 `id` 字段和注解 `@JsonSerialize(using = ToStringSerializer.class)`。
画面 3: 展示了 PPT 文档，标题为“2.3.2.1 功能实现”，内容包括在 `ProjectService` 接口中新增 `createTender` 方法，以及在 `ProjectServiceImpl` 中实现该方法的两个前置条件：A. 检查 Apollo 上是否配置最小投标金额（`mini.investment.amount 100.0`）；B. 实现查询账户余额功能，需在 `ConsumerAPI` 接口中新增查询当前余额的方法。
画面 4: 展示了 `ProjectServiceImpl.java` 文件中 `createTender` 方法的实现，其中包含一个私有方法 `getProjectRemainingAmount`，用于计算项目剩余金额。
画面 5: 展示了 `BalanceDetailsDTO.java` 文件，定义了用户余额信息的数据传输对象，包含 `consumerId`、`userNo`、`changeType`、`freezeAmount`、`balance`、`applyTime` 等字段。
画面 6: 展示了 `ConsumerController.java` 文件，其中包含 `getBorrower` 和 `getBalance` 方法的定义，以及一个测试方法 `testResources`。
画面 7: 展示了 `ConsumerController.java` 文件中 `getBalance` 方法的实现，方法签名是 `getBalance(String userNo)`。
画面 8: 展示了 `ConsumerController.java` 文件中 `getBalanceFromDepository` 方法的实现，使用 `OkHttpClient` 发起 HTTP 请求获取用户余额。
画面 9: 展示了 `ConsumerController.java` 文件中 `getBalanceFromDepository` 方法的实现，使用 `RestTemplate` 发起 HTTP 请求获取用户余额。
画面 10: 展示了 `ConsumerController.java` 文件中 `getBalanceFromDepository` 方法的实现，使用 `RestTemplate` 发起 HTTP 请求获取用户余额。
画面 11: 展示了 Apollo 配置中心的界面，显示了 `consumer-Service` 项目下的多个配置项，包括 `Swagger.enable`、`spring.mvc.throw-exception-if-no-handler-found`、`micro_service.spring-boot-http`、`micro_service.spring-Eureka`、`micro_service.spring-hystrix`、`micro_service.spring-ribbon` 等。
画面 12: 展示了 Apollo 配置中心的界面，显示了 `consumer-Service` 项目下的多个配置项，包括 `Swagger.enable`、`spring.mvc.throw-exception-if-no-handler-found`、`micro_service.spring-boot-http`、`micro_service.spring-Eureka`、`micro_service.spring-hystrix`、`micro_service.spring-ribbon` 等。
画面 13: 展示了 `ConsumerController.java` 文件中 `hello` 方法的实现，使用 `@Autowired` 注入 `ConsumerService`，并定义了一个测试接口 `@GetMapping("/hello")`。
画面 14: 展示了 PPT 文档，内容为“2.1 前置条件判断准备工作（投标金额是否大于最小投标金额、账户余额是否足够）”，并列出 A、B、C 三个子项，其中 C 项是“在 ConsumerController 类中实现该方法”，并显示了 `getBalance` 方法的注解和签名。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 2:
```java
package cn.ictast.waningzp.api.transaction.model;

import ...

/**
 * 投标信息
 */
public class TenderDTO {
    @JsonSerialize(using = ToStringSerializer.class)
    private Long id;
    // 按标用户标识
}
```

画面 3:
```text
1.在ProjectService接口中新增createTender方法：
/**
 * 用户投标
 * @param projectInvestDTO
 * @return
 */
TenderDTO createTender(ProjectInvestDTO projectInvestDTO);

2.在ProjectServiceImpl类中实现该方法，由于业务非常复杂，我们拆分成若干部分逐一实现
2.1 前置条件判断准备工作（投标金额是否大于最小投标金额、账户余额是否足够）
A：检查Apollo上是否配置最小投标金额
    mini.investment.amount 100.0
B：实现查询账户余额功能，在ConsumerAPI接口中新增查询当前余额的方法：
    /**
     * 获取当前登录用户余额信息
     * @param userNo 用户编码
     * @return
     */
    RestResponse<BalanceDetailsDTO> getBalance(String userNo);
```

画面 4:
```java
@Override
public TenderDTO createTender(ProjectInvestDTO projectInvestDTO) {

}

/**
 * 获取标的剩余可投标额度
 * @param project
 * @return
 */
private BigDecimal getProjectRemainingAmount(Project project) {
    List<BigDecimal> decimalList = tenderMapper.selectAmountInvested(project.getId());
    BigDecimal amountInvested = new BigDecimal("0.0");
    for (BigDecimal d : decimalList) {
        amountInvested = amountInvested.add(d);
    }
    return amountInvested;
}
```

画面 5:
```java
public class BalanceDetailsDTO implements Serializable {
    private static final long serialVersionUID = 1L;
    @ApiModelProperty(value = "用户标识")
    private Long consumerId;
    @ApiModelProperty(value = "用户编码，生成唯一，用户在存管系统标识")
    private String userNo;
    @ApiModelProperty(value = "账户变动类型 1.增加、2.减少、3.冻结、4.解冻")
    private Integer changeType;
    @ApiModelProperty(value = "冻结金额")
    private BigDecimal freezeAmount;
    @ApiModelProperty(value = "可用余额")
    private BigDecimal balance;
    @ApiModelProperty(value = "应用编码")
    private String applyCode;
}
```

画面 6:
```java
@ApiOperation("获取借款人用户信息")
@ApiImplicitParam(name = "id", value = "用户标识", required = true, dataType = "Long", paramType = "path")
@GetMapping("/my/borrowers/{id}")
public RestResponse<BorrowerDTO> getBorrower(@PathVariable Long id) {
    return RestResponse.success(consumerService.getBorrower(id));
}

@Override
@ApiOperation("获取用户可用余额")
@ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
@GetMapping("/1/balances/{userNo}")
public RestResponse<BalanceDetailsDTO> getBalance(String userNo) {
    return null;
}

@ApiOperation("过网关保护资源，进行认证拦截测试")
@ApiImplicitParam(name = "jsonToken", value = "访问令牌", required = true, dataType = "String")
@GetMapping(value = "/m/consumers/test")
public RestResponse<String> testResources(String jsonToken) {
    return RestResponse.success(EncryptUtil.decodeUTF8StringBase64(jsonToken));
}
```

画面 7:
```java
@ApiOperation("获取用户可用余额")
@ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
@GetMapping("/1/balances/{userNo}")
public RestResponse<BalanceDetailsDTO> getBalance(String userNo) {
    return null;
}
```

画面 8:
```java
private RestResponse<BalanceDetailsDTO> getBalanceFromDepository(String userNo) {
    String url = depositorURL + "/balance-details/" + userNo;
    BalanceDetailsDTO balanceDetailsDTO = new BalanceDetailsDTO();
    Request request = new Request.Builder().url(url).build();
    try (Response response = okHttpClient.newCall(request).execute()) {
        if (response.isSuccessful()) {
            String responseBody = response.body().string();
            balanceDetailsDTO = JSON.parseObject(responseBody, BalanceDetailsDTO.class);
            return RestResponse.success(balanceDetailsDTO);
        }
    } catch (IOException e) {
        log.warn("调用存管系统获取余额失败", url, e);
        return RestResponse.fail("获取失败");
    }
    return RestResponse.fail("获取失败");
}
```

画面 9:
```java
private RestResponse<BalanceDetailsDTO> getBalanceFromDepository(String userNo) {
    String url = depositorURL + "/balance-details/" + userNo;
    BalanceDetailsDTO balanceDetailsDTO = new BalanceDetailsDTO();
    Request request = new Request.Builder().url(url).build();
    try (Response response = restTemplate.getForEntity(url, BalanceDetailsDTO.class).getBody()) {
        if (response != null) {
            String responseBody = response.getBody().toString();
            balanceDetailsDTO = JSON.parseObject(responseBody, BalanceDetailsDTO.class);
            return RestResponse.success(balanceDetailsDTO);
        }
    } catch (IOException e) {
        log.warn("调用存管系统获取余额失败", url, e);

