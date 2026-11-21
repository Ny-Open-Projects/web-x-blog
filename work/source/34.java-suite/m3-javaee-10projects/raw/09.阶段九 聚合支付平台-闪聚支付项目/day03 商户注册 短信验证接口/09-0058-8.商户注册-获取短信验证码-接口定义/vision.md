# 画面线理解：8.商户注册-获取短信验证码-接口定义

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\8.商户注册-获取短信验证码-接口定义【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 03:05, 04:03, 05:25, 06:21, 07:06, 07:49, 08:49, 09:39, 10:14, 11:40, 12:52, 13:56, 14:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:53:05

1) 这一组画面整体在讲如何在商户平台应用中通过 RestTemplate 调用短信服务接口来获取验证码，并在 Controller 和 Service 层实现相应的接口定义。

2) 按时间顺序列出每张画面的要点：
画面1：展示使用 RestTemplate 获取验证码的测试方法代码，包含 URL 和请求体设置。
画面2：展示项目结构，重点在 MerchantController 类，其中包含一个测试接口。
画面3：展示接口定义，要求在 MerchantController 中添加 getSMSCode 接口方法。
画面4：展示 @ApiImplicitParam 注解的参数配置，用于定义手机参数。
画面5：展示 @ApiImplicitParam 注解的参数配置，用于定义手机参数。
画面6：展示 MerchantController 中的 getSMSCode 方法，返回 null。
画面7：展示 Nacos 配置管理界面，列出多个配置文件。
画面8：展示 Swagger UI 的 /sms 接口测试页面，参数为 phone。
画面9：展示 RestTemplateTest.java 中的 getSMSCode 方法，设置请求头和 URL。
画面10：展示 Service 接口定义，要求在 SmsService 中添加 sendMsg 方法。
画面11：展示 SmsService.java 文件，包含 @Service 注解。
画面12：展示项目结构，重点在 MerchantController 类。
画面13：展示 MerchantController 中的 getSMSCode 方法，调用 smsService.sendMsg。
画面14：展示 SmsService 接口定义，包含 sendMsg 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//获取验证码测试方法
@Test
public void testGetSmsCode(){
    String url = "http://localhost:56085/sailing/generate?name=sms&effectiveTime=600"; //验证码过期时间为600秒
    String phone = "13434143434";
    log.info("使用短信服务发送验证码：url:{}", url);

    //请求体
    Map<String, Object> body = new HashMap();
    body.put("mobile", phone);

    //请求头
    HttpHeaders httpHeaders = new HttpHeaders();
```

画面3：
```java
@ApiOperation("获取手机验证码")
@ApiImplicitParam(name = "phone", value = "手机号", required = true, dataType = "String",
        paramType = "query")
@GetMapping("/sms")
public String getSMSCode(@RequestParam String phone) {
    log.info("向手机号:()发送验证码", phone);
    ...
}
```

画面4：
```java
@ApiImplicitParam(value = "name", name = "name", required = true, dataType = "String", paramType = "query")
public String getSMSCode(@RequestParam("phone") String phone) {
    ...
}
```

画面6：
```java
return merchantDTO;
```

画面9：
```java
//验证码服务发送请求，获取验证码
//http://localhost:56085/sailing/generate?effectiveTime=600&name=sms
@Test
public void getSMSCode() {
    String url = "http://localhost:56085/sailing/generate?effectiveTime=600&name=sms";

    //请求体
    Map<String, Object> body = new HashMap();
    body.put("mobile", "1343434");

    //请求头
    HttpHeaders httpHeaders = new HttpHeaders();
    httpHeaders.setContentType(MediaType.APPLICATION_JSON);
    httpHeaders.set("Content-Type", "application/json");
    //请求头
    httpHeaders.set("Accept", "application/json");
```

画面10：
```java
package com.shanjugay.merchant.service;

/**
 * 为了方便程序复用在 SmsService 接口中添加sendMsg方法用来获取验证码：
 */
public interface SmsService {
    /**
     * 获取短信验证码
     * @param phone
     * @return
     */
    String sendMsg(String phone);
}
```

画面11：
```java
@Service
public class SmsServiceImpl implements SmsService {
    @Override
    public String sendMsg(String phone) {
        return "验证码已发送";
    }
}
```

画面13：
```java
MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
return merchantDTO;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：
标题：2.3.2.1 接口定义
内容：
1、接口交互流程如下：
   1) 获取手机号
   2) 向验证码服务请求发送验证码并得到响应
   3) 响应前端验证码发送结果
2、在 MerchantController 类中添加 getSMSCode 接口方法，此接口供前端调用。

画面10：
标题：3、Service 接口定义如下
内容：
为了方便程序复用在 SmsService 接口中添加 sendMsg 方法用来获取验证码：

画面14：
标题：3、Service 接口定义如下
内容：
为了方便程序复用在 SmsService 接口中添加 sendMsg 方法用来获取验证码：

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
