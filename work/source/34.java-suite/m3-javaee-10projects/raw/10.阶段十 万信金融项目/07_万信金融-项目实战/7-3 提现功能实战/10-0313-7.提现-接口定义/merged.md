# 7.提现-接口定义

- 阶段：10.阶段十 万信金融项目
- 章节：07_万信金融-项目实战/7-3 提现功能实战
- 源文件：10.阶段十 万信金融项目\07_万信金融-项目实战\7-3 提现功能实战\7.提现-接口定义_【海量资源尽在 666java.com】.mp4
- 时长 7分37秒（音频 458s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好 需求分析搞定之后呢我们接下来就该定义接口了分成三个阶段对吧一个阶段一个阶段来咱先看看第一阶段啊1.1到1.7我们说叫生成提现这个请求数据对吧那么这里边呢一共涉及到两个接口第一个接口就是前端到用户中心对吧第二个接口呢就是用户中心到哪到存管代理服务跟充值呢还是一样的咱们先来看看
[00:30] 实际上就是第一个接口啊第一个接口呢它的功能就是要接收啊前端传过来的一些什么样数据比如说那个提现金额是不是那用户中心呢这边要保存然后呢用户中心还要发请求到哪到存管代理服那边让他那边去生成签名然后呢这边还要接收到签名返回给谁啊前端啊这是接口一吧它要实现的功能那由于呢是涉及到用户中心所以说呢这个接口呢咱仍然是要找到谁啊
[00:59] 对consumer API这个接口然后呢再新增一个方法叫create withdraw这个 withdraw就是什么意思啊提现的意思来看看这个方法吧仍然是几个参数啊对两个参数第一个参数是提现金额第二个参数呢是那个回调地址反正这类型呢仍然是rest response这个就不再说了然后咱看control你在实验这个方案的时候呢这个请求
[01:28] 路径我们统一一下大家跟奖励呢这个都保持什么呀保持一致就行了其他就不再说了这是第一个接口第二个接口呢我们说是不是这个谁呀用户中心发请求到什么呀对存款代理服务这边咱看看第二个这个接口那么这个接口呢它首先叫接收用户中心发过来的这个什么呀请求数据然后这边保存交易记录状态是未同步对吧
[01:57] 然后呢去生成对生成签名那具体咱看看由于涉及到存款代理服务所以说咱要找到这个接口叫depositoryargentap在这里新增一个方法仍然叫curatewithdraw什么呀required这里边呢就有一个涉及到一个新的类了啊一个新的类叫withdraw request大家应该能猜到他是干嘛他是不是就是封装这个什么呀
[02:26] 对封装这个请求数据的来让大家看一眼就这个封装用户提现的这个什么呀请求数据然后呢这个返回值呢还是这个rest response不再说了然后你在Controller那种实验这个方案的时候还是提醒大家注意这个什么呀这个防路径一定是什么开头的呀L开头的要跟简易保持一致为什么是L开头的因为咱这个服务也是供什么呀
[03:03] 供别的微服务去访问的就是不报了给谁啊前端这是需要大家注意的另外呢这里边啊就是这个阶段所涉及到的新的类还有一个叫Visual Record就是这个提现记录对不对因为我们说了这里边要保存这个这个提现这个交易记录嘛所以这里边呢涉及到一个新的类叫Visual Record让大家看一眼它涉及到一个对应的一个表对不对Visual下方线Record这个表呢其实也是在
[03:32] 咱们consumer里边也有啊是不是那么对应的这个实体类呢就是叫withdrawal record这里边有属性还有字段对不对就相信大家自己熟悉熟悉就行这是第一阶段嘛涉及到的两个接口咱就给大家说到这儿接下来呢就是第二阶段第二阶段很简单就咱们前面说过第二阶段是不是只涉及到前端和哪边对前端和
[04:05] 银行存款系统而这两块呢都不需要我们进行什么呀开发都是直接现成的提供给大家所谓第二阶段呢大家直接进行什么呀功能测试即可这是第二阶段就是请求提现啊其实这块就已经开始进行提现了对吧那接下来就是最后一阶段了第三阶段就是提现结果的一个什么呀一个通知对不对这个阶段涉及到几个接口呢应该也是两个
[04:35] 那首先是银行存款系统这边他操作完之后呢会通知发通知给谁啊给我们的对存款代理服对吧从来代理服务呢他这边收到通知之后要更新这个状态为什么要一同步这是一个接口对不对然后从来代理服还要发通知给谁啊给这个谁啊用户中心对吧用户中心接收到通知之后是不是也有一些后续的工作要处理咱看这两个接口吧第三阶段对吧接口三接口三你看
[05:06] 他要接收银行存款系统通知要更新那个状态对不对还要给用户中心在里面发通知那这里边呢咱就要找到这个类啊depository notify control类在这里边新增这么一个方案叫receivedepository withdrawalresult界名之一就是接收银行存款系统返回的这个什么呀提现的这个什么呀结果这里边这些数据这些参数就不再说了什么什么呀服务名
[05:37] 咱这应该是提现对不对平台编号啊这个签名啊还有具体的这个什么呀业务数据对吧等等等等我们最终呢是反应值大家都统一吧反而一个OK统一的这是第三个接口啊第四个接口的话是不是就是我们刚才说了第四个其实严格意义上不是interface啊不是它其实是一个消息的什么呀消费者嘛但有印象我们刚才说了你应该是这个谁啊呃用户中心是不是要接收什么呀
[06:10] 对存款代理服发过来的一个消息也就是用户中心这边其实是一个消息的消费者一个接收者那你应该找到这个类叫Gateway Notify Conceal More在这里边呢参考开户对吧或者参考充值都行然后加个几行代码然后去把这个接口4的这个功能给它实现了就行了另外呢你在
[06:38] 对这个阶段进行功能测试的时候跟前面一样啊你仍然是要找到银行存款系统当中的这个类叫VDRAWDetailed Service MPL找到这个类然后同样是把红框当中的这两个代码的这个注释给干什么呀去掉原因跟之前一样啊为什么一开始是注释掉是因为不影响是为了不影响什么呀前两个阶段的测试然后呢等你
[07:07] 测试到第三阶段的时候了为了看到这个第三阶段的这个效果呀这两行代码的注视就不能有了啊因为这两行代码是银行存款系统那边要要干什么呀要给存款代理服这边干什么要发通知了啊所以这两行代码这个时候第三阶段测试的时候就要把注视给干什么呀去掉了啊所以说这个细节呢你一定要特别特别注意这是用户提现吧整个这一块的这个接口呢咱就跟大家说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解用户中心服务与存管代理服务在提现业务中生成提现数据、请求提现及接收提现结果通知的接口定义与实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示PPT标题“2.2.1 接口定义”及子标题“2.2.1.1 用户中心生成提现数据接口(接口③)”。
- 列出接口描述：1) 接收用户填写的提现数据；2) 用户中心保存提现信息；3) 请求存管代理生成签名数据；4) 将签名数据返回给前端。
- 左侧导航栏显示当前章节为“2.2.1.1 用户中心生成提现数据接口”。

画面2：
- 展示PPT内容，列出“2.2.1.1 用户中心生成提现数据接口(接口③)”的接口定义。
- 代码片段：在ConsumerApi接口中新增createWithdrawRecord方法：
  ```java
  /**
   * 生成用户提现数据
   * @param amount 提现金额
   * @param callbackUrl 回调地址
   * @return
   */
  RestResponse<GatewayRequest> createWithdrawRecord(String amount, String callbackUrl);
  ```
- 代码片段：在ConsumerController类中实现该方法：
  ```java
  @Override
  @ApiOperation("生成用户提现数据")
  @ApiImplicitParams({
  @ApiImplicitParam(name = "amount", value = "金额", required = true,
  dataType = "String", paramType = "query"),
  @ApiImplicitParam(name = "callbackUrl", value = "通知结果回调url",
  required = true,
  dataType = "String", paramType = "query")
  })
  @GetMapping("/my/withdraw-records")
  public RestResponse<GatewayRequest> createWithdrawRecord(String amount, String callbackUrl) {
      return null;
  }
  ```

画面3：
- 展示PPT内容，列出“第一阶段：生成提现数据”和“第二阶段：请求提现”、“第三阶段：提现结果通知”的业务流程。
- 第一阶段：1) 前端填写提现信息；2) 前端请求用户中心服务提现；3) 用户中心服务请求存管代理服务生成交易记录（未同步），并对提现数据进行签名；4) 存管代理服务将签名后的提现数据返回给用户中心；5) 用户中心将提现数据返回给前端。
- 第二阶段：1) 前端携带提现请求信息请求银行系统；2) 银行存管系统向前端返回提现信息确认页面；3) 前端确认完成提现请求到银行存管系统；4) 银行存管系统接收提现数据并进行校验，校验交易密码，未成功则将银行卡余额进行扣减。
- 第三阶段：1) 提现成功后银行存管系统异步通知存管代理服务；2) 存管代理服务接收提现成功通知更新交易状态为同步；3) 存管代理服务通知用户中心服务；4) 用户中心服务接收到提现成功的消息保存提现信息到用户中心服务。

画面4：
- 展示PPT标题“2.2.1.2 存管代理生成提现数据接口(接口②)”。
- 列出接口定义：1) 接收用户中心发来的提现请求数据；2) 保存请求记录；3) 生成签名数据。
- 左侧导航栏显示当前章节为“2.2.1.2 存管代理生成提现数据接口”。

画面5：
- 展示IDE中WithdrawRequest.java文件内容，显示类中定义的字段：
  ```java
  private String requestNo;
  @ApiModelProperty("提现金额")
  private BigDecimal amount;
  @ApiModelProperty("平台佣金")
  private BigDecimal commission;
  @ApiModelProperty("页面回调URL")
  private String callbackURL;
  @ApiModelProperty("银行卡号")
  private String cardNumber;
  @ApiModelProperty("银行预留手机号")
  private String mobile;
  ```

画面6：
- 展示IDE中WithdrawRecord.java文件内容，显示类中定义的字段：
  ```java
  @Data
  @Table(name = "withdraw_record")
  public class WithdrawRecord implements Serializable {
      private static final long serialVersionUID = 1L;
      // 主键
      @TableId(value = "ID", type = IdType.AUTO)
      private Long id;
      // 用户标识
      @TableField("CONSUMER_ID")
      private String consumerId;
  ```

画面7：
- 展示IDE中WithdrawRecord.java文件内容，显示类中定义的字段：
  ```java
  // 用户编码，生成唯一-用户在存管系统标识
  @TableField("USER_NO")
  private String userNo;
  // 主键
  @TableField("AMOUNT")
  private BigDecimal amount;
  // 平台佣金
  @TableField("COMMISSION")
  private BigDecimal commission;
  // 触发时间
  @TableField("CREATE_DATE")
  private Date createDate;
  ```

画面8：
- 展示PPT内容，列出“2.2.1.2 存管代理生成提现数据接口(接口②)”的接口定义。
- 代码片段：在DepositoryAgentApi接口中新增createWithdrawRecord方法：
  ```java
  /**
   * 用户提现
   * @param withdrawRequest
   * @return
   */
  RestResponse<GatewayRequest> createWithdrawRecord(withdrawRequest withdrawRequest);
  ```
- 代码片段：在DepositoryAgentController类中实现该方法：
  ```java
  @Override
  @ApiOperation("生成提现请求数据")
  @ApiImplicitParam(name = "withdrawRequest", value = "提现信息", required = true,
  dataType = "withdrawRequest", paramType = "body")
  @PostMapping("/withdraw")
  public RestResponse<GatewayRequest> createWithdrawRecord(@RequestBody WithdrawRequest withdrawRequest) {
      return null;
  }
  ```

画面9：
- 展示PPT内容，列出“2.2.1.2 存管代理生成提现数据接口(接口②)”的接口定义。
- 代码片段：在DepositoryAgentController类中实现该方法：
  ```java
  @Override
  @ApiOperation("生成提现请求数据")
  @ApiImplicitParam(name = "withdrawRequest", value = "提现信息", required = true,
  dataType = "withdrawRequest", paramType = "body")
  @PostMapping("/withdraw")
  public RestResponse<GatewayRequest> createWithdrawRecord(@RequestBody WithdrawRequest withdrawRequest) {
      return null;
  }
  ```

画面10：
- 展示PPT中的业务流程图，标题为“第一阶段：生成提现数据(图中1.1-1.7)”。
- 流程图结构：
  - 前端填写提现信息 → 前端请求用户中心服务提现 → 用户中心服务请求存管代理服务生成交易记录（未同步），并对提现数据进行签名 → 存管代理服务将签名后的提现数据返回给用户中心 → 用户中心将提现数据返回给前端。
  - 详细步骤：
    1. 前端填写提现信息。
    2. 前端请求用户中心服务提现。
    3. 用户中心服务请求存管代理服务生成交易记录（未同步），并对提现数据进行签名。
    4. 存管代理服务将签名后的提现数据返回给用户中心。
    5. 用户中心将提现数据返回给前端。

画面11：
- 展示PPT内容，列出“2.3 第二阶段：请求提现”、“2.4 第三阶段：提现结果通知”。
- 左侧导航栏显示当前章节为“2.4.2.2 用户中心服务接收通知接口(接口④)”。

画面12：
- 展示PPT内容，列出“2.4.2.2 用户中心服务接收通知接口(接口④)”。
- 代码片段：
  ```java
  @RequestMapping(value = "/gateway", method = RequestMethod.GET, params = {
  "serviceName", "platformNo", "signature", "reqData"
  })
  public String receivedDepositoryWithdrawResult(
  @RequestParam("serviceName") String serviceName,
  @RequestParam("platformNo") String platformNo,
  @RequestParam("signature") String signature,
  @RequestParam("reqData") String reqData) {
      return "OK";
  }
  ```
- 文本说明：银行存管系统提现成功会通知存管代理服务，存管代理服务会通知用户中心服务，用户中心收到通知后需要保存提现记录，并更新余额。这里并不是严格意义上的的接口，而是一个消息消费者(GatewayNotifyConsumer.java)，在开户时已经使用过。参考之前代码实现接收存管代理服务发来的通知，并更新数据。

画面13：
- 展示PPT内容，列出“2.4.2.2 用户中心服务接收通知接口(接口④)”。
- 左侧导航栏显示当前章节为“2.4.2.2 用户中心服务接收通知接口(接口④)”。

画面14：
- 展示PPT内容，列出“2.4.2.2 用户中心服务接收通知接口(接口④)”。
- 代码片段：

