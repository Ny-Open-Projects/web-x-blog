# 画面线理解：day06-14-开户第一阶段-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-14-开户第一阶段-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 02:15, 04:10, 05:24, 05:54, 07:00, 07:42, 07:54, 08:30, 09:00, 11:26, 11:42, 12:29, 13:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:22:54

1) 这一组画面整体在讲什么（一句话）：
演示如何在用户中心服务中实现“生成开户数据”的接口，包括在Controller中定义接口、在Service中实现业务逻辑、以及通过Postman进行接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档，明确当前任务是“3.3.1 需求分析”和“3.3.2 接口定义”，并指出需要在“warxinp2p-ap”工程的ConsumerAPI接口中新增createConsumer方法。
画面2：在IDEA中定位到ConsumerController类，显示其继承自ConsumerAPI接口，并包含一个测试方法“@ApiOperation("Hello")”。
画面3：在Postman中准备调用“开户生成开户数据”接口，Body中填写了测试数据，包括“name”、“idCard”、“bankCode”、“certificates”和“mobile”。
画面4：在Postman中切换到Query Parameters，设置“access_token”参数用于认证。
画面5：在IDEA中查看ConsumerController的代码，高亮显示了“@ApiOperation("生成开户请求数据")”注解和“createConsumer”方法的定义。
画面6：在IDEA中查看ConsumerController代码，高亮显示了“@ApiImplicitParam”注解，用于定义“consumerRequest”参数。
画面7：在IDEA中查看ConsumerController代码，高亮显示了“@PostMapping”注解和“createConsumer”方法的实现，其中调用了“consumerService.createConsumer(consumerRequest)”。
画面8：在IDEA中查看ConsumerController代码，高亮显示了“@ApiOperation("过网关保护资源，进行认证拦截测试")”注解。
画面9：在IDEA中查看ConsumerServiceImpl类，高亮显示了“createConsumer”方法的实现，其中包含对用户是否已开户的判断和对银行卡状态的判断。
画面10：在IDEA中查看ConsumerServiceImpl类，高亮显示了“if (bankCardDTO == null || bankCardDTO.getStatus() == StatusCode.STATUS_IN.getCode())”条件判断。
画面11：在IDEA中查看ConsumerServiceImpl类，高亮显示了“consumerRequest.setId(consumerDTO.getId())”和“consumerRequest.setMobile(CodeUtil.getMobileCode())”代码。
画面12：在Postman中发送请求，成功返回了响应，显示“code: 0”和“msg: “成功””。
画面13：展示多个开发工具窗口，包括IDEA、Postman、SQLyog、ApolloPortal等，说明这是一个多模块、多服务的分布式系统。
画面14：在Postman中查看成功请求的响应，显示了“code: 0”、“msg: “成功””和“result”对象，其中包含“certificates”、“platformNo”、“signature”和“url”等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 生成开户请求数据
 * @param consumerRequest 开户信息
 * @return
 */
RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);
```

画面5：
```java
@ApiOperation("生成开户请求数据")
@ApiImplicitParam(name = "consumerRequest", value = "开户信息", required = true, dataType = "ConsumerRequest")
@PostMapping("/my/consumers")
public RestResponse<GatewayRequest> createConsumer(@RequestBody ConsumerRequest consumerRequest) {
```

画面6：
```java
@ApiOperation("生成开户请求数据")
@ApiImplicitParam(name = "consumerRequest", value = "开户信息", required = true, dataType = "ConsumerRequest")
@PostMapping("/my/consumers")
public RestResponse<GatewayRequest> createConsumer(@RequestBody ConsumerRequest consumerRequest) {
```

画面7：
```java
@ApiOperation("生成开户请求数据")
@ApiImplicitParam(name = "consumerRequest", value = "开户信息", required = true, dataType = "ConsumerRequest")
@PostMapping("/my/consumers")
public RestResponse<GatewayRequest> createConsumer(@RequestBody ConsumerRequest consumerRequest) {
    consumerRequest.setMobile(SecurityUtil.getUser().getMobile());
    return consumerService.createConsumer(consumerRequest);
}
```

画面9：
```java
@Override
@Transactional
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    // 判断该交易的执行行是否已开户
    if (ConsumerDTO consumerDTO = bankCardService.getBankCard(consumerRequest.getMobile())) {
        throw new BusinessException(ConsumerErrorCode.E_140105);
    }

    // 判断提交过来的银行卡是否已绑定
    BankCardDTO bankCardDTO = bankCardService.getBankCard(consumerRequest.getBankNumber());
    if (bankCardDTO == null || bankCardDTO.getStatus() == StatusCode.STATUS_IN.getCode()) {
        throw new BusinessException(ConsumerErrorCode.E_140151);
    }
```

画面10：
```java
// 判断提交过来的银行卡是否已绑定
BankCardDTO bankCardDTO = bankCardService.getBankCard(consumerRequest.getBankNumber());
if (bankCardDTO == null || bankCardDTO.getStatus() == StatusCode.STATUS_IN.getCode()) {
    throw new BusinessException(ConsumerErrorCode.E_140151);
}
```

画面11：
```java
// 更新用户的ID
consumerRequest.setId(consumerDTO.getId());
// 产生请求流水号和商户号
consumerRequest.setMobile(CodeUtil.getMobileCode());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“3.3 第一阶段: 生成开户数据”，子标题为“3.3.1 需求分析”和“3.3.2 接口定义”。
画面13：展示了一个多窗口的开发环境，包括IDEA、Postman、SQLyog、ApolloPortal等，但未提供具体的架构图或流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
