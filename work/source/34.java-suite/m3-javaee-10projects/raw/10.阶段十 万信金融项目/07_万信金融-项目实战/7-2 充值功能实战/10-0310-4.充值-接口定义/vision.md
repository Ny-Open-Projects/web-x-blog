# 画面线理解：4.充值-接口定义

- 阶段：10.阶段十 万信金融项目
- 章节：07_万信金融-项目实战/7-2 充值功能实战
- 源文件：10.阶段十 万信金融项目\07_万信金融-项目实战\7-2 充值功能实战\4.充值-接口定义_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:21, 00:53, 03:20, 03:54, 04:38, 04:54, 05:32, 07:13, 07:43, 08:18, 08:59, 10:36, 12:59, 13:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:52:10

1) 这一组画面整体在讲什么（一句话）：
讲解充值业务的三个阶段：第一阶段生成充值数据、第二阶段请求充值、第三阶段充值结果通知，重点是用户中心生成充值数据接口和接收通知接口的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PDF文档“2.2.1 第一阶段：生成充值数据”，内容包括“2.2.1 需求分析”和“2.2.2 接口定义”。
画面2：PDF文档中“2.2.2.1 用户中心生成充值数据接口（接口③）”部分，列出接口描述的四点要求。
画面3：IDE中显示`RechargeRecord.java`类代码，包含`@Table("recharge_record")`注解和字段定义。
画面4：IDE中`RechargeRecord.java`类代码，鼠标选中`@Table("recharge_record")`注解。
画面5：IDE中`RechargeRequest.java`类代码，包含多个`@ApiModelProperty`注解定义字段。
画面6：PDF文档中“第一阶段：生成充值数据(图中1.1-1.7)”的业务流程图，包含多个步骤和流程指向。
画面7：PDF文档中“2.2.1 需求分析”部分，内容与画面1相同。
画面8：PDF文档中“在DepositoryAgent接口中新增createRechargeRecord方法”和“在DepositoryAgentController类中实现该方法”的代码片段。
画面9：PDF文档中“2.2.2.1 用户中心生成充值数据接口（接口③）”部分，内容与画面2相同。
画面10：PDF文档中“2.2.2.1 用户中心生成充值数据接口（接口③）”部分，内容与画面2相同。
画面11：PDF文档中“2.3 第二阶段：请求充值”和“2.4 第三阶段：充值结果通知”的标题。
画面12：PDF文档中“2.4.2.2 用户中心服务接收通知接口（接口④）”的代码片段，包含`@ApiImplicitParams`注解和`@RequestMapping`注解。
画面13：PDF文档中“RechargeDetailsServiceImpl.java”类代码片段，包含`//产生充值成功信息`和`//更新充值记录结果`注释。
画面14：PDF文档中“2.2.2.1 用户中心生成充值数据接口（接口③）”部分，内容与画面2相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
@Table("recharge_record")
public class RechargeRecord implements Serializable {
    private static final long serialVersionUID = 1L;
    @TableId(value = "ID", type = IdType.AUTO)
    private Long id;
    @TableField("CONSUMER_ID")
    private Long consumerId;
}
```

画面5：
```java
public class RechargeRequest {
    @ApiModelProperty("标识")
    private Long id;
    @ApiModelProperty("用户编号")
    private String userNo;
    @ApiModelProperty("请求流水号")
    private String requestNo;
    @ApiModelProperty("充值金额")
    private BigDecimal amount;
    @ApiModelProperty("负有回调URL")
    private String callbackUrl;
}
```

画面8：
```java
/**
 * 用户充值
 */
@ApiOperation("生成充值请求数据")
@ImplicitParam(name = "rechargeRequest", value = "充值信息", required = true,
        dataType = "RechargeRequest", paramType = "body")
@PostMapping("/recharges")
public RestResponse<GatewayRequest> createRechargeRecord(@RequestBody RechargeRequest rechargeRequest){
    return null;
}
```

画面12：
```java
@ApiOperation("接受银行存管系统通知结果")
@ApiImplicitParams({
        @ApiImplicitParam(name = "serviceName", value = "请求的银行存管接口名", required = true, dataType = "String", paramType = "query"),
        @ApiImplicitParam(name = "platformNo", value = "平台号，平台与存管系统签约时获取", required = true, dataType = "String", paramType = "query"),
        @ApiImplicitParam(name = "signature", value = "存管代理服务签名", required = true, dataType = "String", paramType = "query"),
        @ApiImplicitParam(name = "reqData", value = "业务数据参数", required = true, dataType = "String", paramType = "query")
})
@RequestMapping(value = "/gateway", method = RequestMethod.GET, params = "serviceName=RECHARGE")
public String receivedRechargeResult(
        @RequestParam("serviceName") String serviceName,
        @RequestParam("platformNo") String platformNo,
        @RequestParam("signature") String signature,
        @RequestParam("reqData") String reqData){
    return null;
}
```

画面13：
```java
//产生充值成功信息
//producer: recharge(rechargeRequest.getApCode(), response);
//更新充值记录结果
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面6：流程图标题“第一阶段：生成充值数据(图中1.1-1.7)”，包含以下步骤和流程指向：
- 1. 前端填写充值信息（如果用户尚未开户，会被自动跳转到开户界面）
- 2. 前端请求用户中心服务充值
- 3. 用户中心服务准备充值数据
- 4. 用户中心服务请求存管代理服务生成交易记录（未同步），并对充值数据进行签名
- 5. 存管代理服务将签名后的充值数据返回给用户中心
- 6. 用户中心将充值数据返回给前端
- 7. 前端携带充值信息请求银行存管系统
- 8. 存管代理服务通知用户中心服务
- 9. 用户中心服务收到通知后，需要保存充值记录，并更新余额
- 10. 用户中心服务通知前端充值成功

画面11：标题“2.3 第二阶段：请求充值”和“2.4 第三阶段：充值结果通知”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
