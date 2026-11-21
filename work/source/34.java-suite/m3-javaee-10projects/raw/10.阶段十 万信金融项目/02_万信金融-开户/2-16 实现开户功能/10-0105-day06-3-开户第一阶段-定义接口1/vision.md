# 画面线理解：day06-3-开户第一阶段-定义接口1

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-3-开户第一阶段-定义接口1_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:31, 01:28, 05:51, 06:49, 07:18, 08:25, 09:43, 10:08, 10:50, 11:06, 11:44, 12:12, 12:55, 13:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:14:14

1) 这一组画面整体在讲什么（一句话）：
讲解银行开户流程的系统架构与代码实现，重点是用户中心生成开户数据接口的定义与开发。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示开户业务流程图，包含浏览器/App、用户中心、存管代理服务、存管系统、开卡银行五个模块，以及各模块间交互的详细步骤（如1.1生成开户请求数据、1.2准备开户基础数据、2.1跳转相关开户接口等）。
画面2：PPT页面，标题为“3.3 第一阶段: 生成开户数据”，内容包括“3.3.1 需求分析”和“3.3.2 接口定义”，并指出在“wanning2p-api”工程中新增`createConsumer`方法。
画面3：文件资源管理器，显示“wanning2p > day06”目录下的文件，包括“开户业务流程图.jpg”、“系统对接规范与安全机制方案.docx”等。
画面4：PPT页面，标题为“接口参数”，展示“请求”和“返回”两个部分的参数表，包括参数名称、必填、类型、长度、参数说明等字段。
画面5：PPT页面，展示“请求”部分的参数表，包含userNo、requestNo、realName、userRole、mobile、cardNumber、callbackUrl等字段。
画面6：IDEA开发工具界面，显示“wanning2p-api”工程结构，同时弹出多个窗口，包括“wanning2p-apollo”、“adminservice”、“Apollortal”、“configservice”等。
画面7：Notepad++编辑器，显示“GatewayRequest.java”文件内容，包含`@ApiModel`注解定义的类，字段包括`serviceNames`、`platformNo`、`requestData`、`signature`、`depositoryUrl`。
画面8：IDEA开发工具界面，显示“ConsumerRequest.java”文件内容，包含`@ApiModel`注解定义的类，字段包括`id`、`username`、`fullname`、`idnumber`、`bankCode`、`cardnumber`、`mobile`、`role`、`requestNo`、`userNo`、`callbackUrl`。
画面9：IDEA开发工具界面，显示“ConsumerRequest.java”文件内容，展示`@ApiModel`注解定义的类，字段包括`id`、`username`、`fullname`、`idnumber`、`bankCode`、`cardnumber`、`mobile`、`role`、`requestNo`、`userNo`、`callbackUrl`。
画面10：IDEA开发工具界面，显示“ConsumerRequest.java”文件内容，展示`@ApiModel`注解定义的类，字段包括`id`、`username`、`fullname`、`idnumber`、`bankCode`、`cardnumber`、`mobile`、`role`、`requestNo`、`userNo`、`callbackUrl`。
画面11：IDEA开发工具界面，显示“GatewayRequest.java”文件内容，包含`@ApiModel`注解定义的类，字段包括`serviceNames`、`platformNo`、`requestData`、`signature`、`depositoryUrl`。
画面12：IDEA开发工具界面，显示“ConsumerAPI.java”文件内容，包含`RestResponse register(ConsumerRegisterDTO consumerRegisterDTO)`和`RestResponse GatewayRequest createConsumer(ConsumerRequest consumerRequest)`方法。
画面13：IDEA开发工具界面，显示“ConsumerController.java”文件内容，包含`@ApiOperation("用户注册")`和`@PostMapping(value = "/consumers")`方法。
画面14：IDEA开发工具界面，显示“ConsumerController.java”文件内容，包含`@ApiOperation("生成开户请求数据")`和`@PostMapping(value = "/my/consumers")`方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```
1. 在wanning2p-api工程中的ConsumerAPI接口中新增createConsumer方法：
    * 生成开户请求数据
    @param consumerRequest 开户信息
    @return
    RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);

2. 在wanning2p-consumer-service工程的ConsumerController类中实现该方法：
```

画面4：
```
请求
参数名称	必填	类型	长度	参数说明
userNo	Y	S	50	平台用户编号
requestNo	Y	S	50	请求流水号
realName	N	S	50	用户真实姓名
idNumber	N	S	50	用户证件号
userRole	Y	S	50	如投资人/借款人/担保机构
mobile	N	S	50	银行预留手机号
cardNumber	N	S	50	银行卡号
callbackUrl	Y	S	256	页面回调 URL

返回
参数名称	必填	类型	长度	参数说明
```

画面7：
```
package cn.ictcast.wanning2p.sql.depository.model;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

@ApiModel(value = "与银行存管系统对接使用的签名请求数据")
public class GatewayRequest {
    @ApiModelProperty("请求的存管接口名")
    private String serviceNames;
    @ApiModelProperty("平台编号，平台与存管系统签约时获取")
    private String platformNo;
    @ApiModelProperty("业务数据报文，json格式")
    private String requestData;
    @ApiModelProperty("对requestData参数的签名")
    private String signature;
    @ApiModelProperty("银行存管系统地址")
    private String depositoryUrl;
}
```

画面8：
```
package cn.ictcast.wanning2p.api.consumer.model;

@ApiModel(value = "ConsumerRequest", description = "平台-端用户开户信息")
public class ConsumerRequest {
    @ApiModelProperty("id")
    private Long id;
    @ApiModelProperty("用户名")
    private String username;
    @ApiModelProperty("真实姓名")
    private String fullname;
    @ApiModelProperty("身份证号")
    private String idnumber;
    @ApiModelProperty("银行编码")
    private String bankCode;
    @ApiModelProperty("银行卡号")
    private String cardnumber;
    @ApiModelProperty("手机号")
    private String mobile;
    @ApiModelProperty("角色")
    private String role;
    @ApiModelProperty("请求流水号")
    private String requestNo;
    @ApiModelProperty("用户编号")
    private String userNo;
    @ApiModelProperty("页面回调 URL")
    private String callbackUrl;
}
```

画面11：
```
package cn.ictcast.wanning2p.api.consumer.model;

@ApiModel(value = "GatewayRequest", description = "与银行存管系统对接使用的签名请求数据")
public class GatewayRequest {
    @ApiModelProperty("请求的存管接口名")
    private String serviceNames;
    @ApiModelProperty("平台编号，平台与存管系统签约时获取")
    private String platformNo;
    @ApiModelProperty("业务数据报文，json格式")
    private String requestData;
    @ApiModelProperty("对requestData参数的签名")
    private String signature;
    @ApiModelProperty("银行存管系统地址")
    private String depositoryUrl;
}
```

画面12：
```
RestResponse register(ConsumerRegisterDTO consumerRegisterDTO),
RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);
```

画面13：
```
@ApiOperation("用户注册")
@ApiImplicitParam(name = "consumerRegisterDTO", value = "注册信息", required = true,
        dataType = "AccountRegisterDTO", paramType = "body")
@PostMapping(value = "/consumers")
public RestResponse register(ConsumerRegisterDTO consumerRegisterDTO) {
    consumerService.register(consumerRegisterDTO);
    return RestResponse.success();
}

@Override
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    return null;
}
```

画面14：
```
@ApiOperation("用户注册")
@ApiImplicitParam(name = "consumerRegisterDTO", value = "注册信息", required = true,
        dataType = "AccountRegisterDTO", paramType = "body")
@PostMapping(value = "/consumers")
public RestResponse register(ConsumerRegisterDTO consumerRegisterDTO) {
    consumerService.register(consumerRegisterDTO);
    return RestResponse.success();
}

@Override
@ApiOperation("生成开户请求数据")
@PostMapping(value = "/my/consumers")
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    return null;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：架构图，包含五个模块：浏览器/App、用户中心、存管代理服务、存管系统、开卡银行。各模块间有带编号的箭头连接，表示流程顺序。
画面2：PPT标题“3.3 第一阶段: 生成开户数据”，内容包括“3.3.1 需求分析”和“3.3.2 接口定义”。
画面4：表格数据，标题“接口参数”，包含“请求”和“返回”两个部分，每个部分有“参数名称”、“必填”、“类型”、“长度”、“参数说明”等字段。
画面5：表格数据，标题“接口参数”，包含“请求”部分，字段包括“userNo”、“requestNo”
