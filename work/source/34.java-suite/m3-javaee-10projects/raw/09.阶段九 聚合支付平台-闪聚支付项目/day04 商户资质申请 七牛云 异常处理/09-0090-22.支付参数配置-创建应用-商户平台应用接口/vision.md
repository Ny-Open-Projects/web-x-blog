# 画面线理解：22.支付参数配置-创建应用-商户平台应用接口

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\22.支付参数配置-创建应用-商户平台应用接口【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:03, 02:11, 02:56, 03:54, 04:47, 05:55, 07:17, 08:30, 09:23, 09:50, 10:38, 11:14, 11:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:16:02

1) 这一组画面整体在讲什么（一句话）：
演示如何在商户平台中创建应用接口，包括定义控制器、DTO类、服务层逻辑以及接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档大纲，定位到“4.2.2 商户平台应用创建应用接口(接口②)”章节，开始讲解接口定义。
画面2：在IDE中展示AppController类，定义了@Api注解和@RestController注解。
画面3：在IDE中展示AppController类，光标位于createApp方法上，准备编写实现。
画面4：展示AppDTO类的定义，包含多个@ApiModelProperty注解，用于描述字段含义。
画面5：在IDE中展示AppController类，编写了@ApiOperation和@PostMapping注解，定义了创建应用的接口。
画面6：展示文档大纲，定位到“4.2.2.2 接口测试”章节，开始讲解接口测试。
画面7：在Postman中测试创建应用接口，发送POST请求，但返回500 Internal Server Error。
画面8：展示Swagger UI界面，列出商户平台应用接口的各个端点。
画面9：在IDE中展示AppService类，编写了createApp方法的实现，包含商户校验逻辑。
画面10：在IDE中展示AppService类，编写了createApp方法的实现，包含商户校验逻辑。
画面11：在IDE中展示AppService类，编写了createApp方法的实现，包含商户状态校验逻辑。
画面12：在IDE中展示AppService类，编写了createApp方法的实现，包含生成应用ID和设置商户ID。
画面13：在IDE中展示AppService类，展示createApp方法的完整实现，包括日志和异常处理。
画面14：展示文档大纲，定位到“4.2.2.2 接口测试”章节，展示如何使用token进行接口测试。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
package com.shanjunpay.merchant.controller;

@Api(value = "商户平台-应用管理", tags = "商户平台-应用相关", description = "商户平台-应用相关")
@RestController
public class AppController {

画面2：
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author Administrator
 * @version 1.0
 */
@Api(value = "商户平台-应用管理", tags = "商户平台-应用相关", description = "商户平台-应用相关")
@RestController
public class AppController {

画面3：
package com.shanjunpay.merchant.controller;

@Api(value = "商户平台-应用管理", tags = "商户平台-应用相关", description = "商户平台-应用相关")
@RestController
public class AppController {

画面4：
@Data
@ApiModel(value = "AppDTO", description = "")
public class AppDTO implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "商户名称")
    private String appname;

    @ApiModelProperty(value = "所属商户")
    private Long merchantId;

    @ApiModelProperty(value = "应用公钥(RSAWithSHA256)")
    private String publicKey;

    @ApiModelProperty(value = "授权回调地址")
    private String notifyUrl;

画面5：
package com.shanjunpay.merchant.controller;

@Api(value = "商户平台-应用管理", tags = "商户平台-应用相关", description = "商户平台-应用相关")
@RestController
public class AppController {

    @ApiOperation("商户创建应用")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "app", value = "应用信息", required = true, dataType = "AppDTO", paramType = "body")
    })
    @PostMapping(value = "/my/apps")
    public AppDTO createApp(@RequestBody AppDTO app) {

画面6：
package com.shanjunpay.merchant.controller;

@Api(value = "商户平台-应用管理", tags = "商户平台-应用相关", description = "商户平台-应用相关")
@RestController
public class AppController {

    @ApiOperation("商户创建应用")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "app", value = "应用信息", required = true, dataType = "AppDTO", paramType = "body")
    })
    @PostMapping(value = "/my/apps")
    public AppDTO createApp(@RequestBody AppDTO app) {
        Long merchantId = SecurityUtil.getMerchantId();
        return appService.createApp(merchantId, app);
    }

画面7：
{
  "mobile": "13333333333",
  "password": "string",
  "username": "string",
  "verifCode": "string",
  "verifKey": "sm2:2178c6e492a4c8b5c55c696e4608"
}

画面8：
POST /my/merchants/save

画面9：
public AppDTO createApp(Long merchantId, AppDTO app) throws BusinessException {
    if (merchantId == null) {
        throw new BusinessException(CommonErrorCode.E_200009);
    }
    // 校验商户是否通过资质审核
    Merchant merchant = merchantMapper.selectById(merchantId);
    if (merchant == null) {
        throw new BusinessException(CommonErrorCode.E_200009);
    }
    // 校验商户状态
    String status = merchant.getStatus();
    if (!"2".equals(status)) {
        throw new BusinessException(CommonErrorCode.E_200003);
    }
    // 应用名不能重复
    // 插入应用名称

画面10：
public AppDTO createApp(Long merchantId, AppDTO app) throws BusinessException {
    if (merchantId == null) {
        throw new BusinessException(CommonErrorCode.E_200009);
    }
    // 校验商户是否通过资质审核
    Merchant merchant = merchantMapper.selectById(merchantId);
    if (merchant == null) {
        throw new BusinessException(CommonErrorCode.E_200009);
    }
    // 校验商户状态
    String status = merchant.getStatus();
    if (!"2".equals(status)) {
        throw new BusinessException(CommonErrorCode.E_200003);
    }
    // 应用名不能重复
    // 插入应用名称

画面11：
public AppDTO createApp(Long merchantId, AppDTO app) throws BusinessException {
    if (merchantId == null) {
        throw new BusinessException(CommonErrorCode.E_200009);
    }
    // 校验商户是否通过资质审核
    Merchant merchant = merchantMapper.selectById(merchantId);
    if (merchant == null) {
        throw new BusinessException(CommonErrorCode.E_200009);
    }
    // 校验商户状态
    String status = merchant.getStatus();
    if (!"2".equals(status)) {
        throw new BusinessException(CommonErrorCode.E_200003);
    }
    // 应用名不能重复
    // 插入应用名称

画面12：
// 生成应用ID
String appid = UUID.randomUUID().toString();
App entity = AppConvert.INSTANCE.dto2entity(appDTO);
entity.setAppId(appid);//应用id
entity.setMerchantId(merchantId);//商户id

画面13：
// 生成应用ID
String appid = UUID.randomUUID().toString();
App entity = AppConvert.INSTANCE.dto2entity(appDTO);
entity.setAppId(appid);//应用id
entity.setMerchantId(merchantId);//商户id

画面14：
{
  "appname": "这是输出应用名称",
  "notifyUrl": "string",
  "publicKey": "string"
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“4.2.2 商户平台应用创建应用接口(接口②)”，子标题为“4.2.2.1 接口定义”，内容包括“1) 接口描述”和“2) 接口定义如下：定义AppController类，并定义createApp方法”。
画面6：PPT标题为“4.2.2.2 接口测试”，子标题为“1、准备token”，内容为“用之前的TokenTemp.java来生成token，注意所指定的商户id必须审核通过。”
画面14：PPT标题为“4.2.2.2 接口测试”，子标题为“1、准备token”，内容为“用之前的TokenTemp.java来生成token，注意所指定的商户id必须审核通过。”
画面8：Swagger UI界面，列出商户平台应用接口的各个端点，包括GET /hello、POST /b1、GET /merchants/{id}、POST /merchants/register、POST /my/merchants/save、GET /sms、POST /upload。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
