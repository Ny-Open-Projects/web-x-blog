# 画面线理解：7.提现-接口定义

- 阶段：10.阶段十 万信金融项目
- 章节：07_万信金融-项目实战/7-3 提现功能实战
- 源文件：10.阶段十 万信金融项目\07_万信金融-项目实战\7-3 提现功能实战\7.提现-接口定义_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:12, 01:40, 02:01, 02:39, 03:25, 03:45, 04:00, 04:19, 04:35, 05:03, 05:54, 06:17, 07:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:54:31

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
