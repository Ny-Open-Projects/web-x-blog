# 画面线理解：15.商户注册-商户平台应用注册商户接口-校验验证码

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\15.商户注册-商户平台应用注册商户接口-校验验证码【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:09, 02:28, 03:13, 04:29, 05:15, 06:05, 07:42, 08:29, 09:17, 10:13, 10:43, 11:16, 11:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:57:59

1) 这一组画面整体在讲商户注册流程中的短信验证码校验功能实现，包括前端接口、服务层代码、调用流程及测试验证。

2) 按时间顺序列出每张画面的要点：
画面1: 展示PPT页面“2.1.1 系统交互流程”，图中包含“消费者”、“商户平台”、“商户服务”、“Sms平台”、“验证到服务”等节点，通过箭头展示商户注册流程。
画面2: IDE中展示MerchantController.java文件，其中包含获取手机验证码和商户注册的两个接口方法，注解为@ApiOperation和@ApiModelProperty。
画面3: IDE中展示SmsServiceImp.java文件，代码中使用RestTemplate调用短信服务，处理响应并抛出异常。
画面4: IDE中展示SmsServiceImp.java文件，代码中定义了checkVerifyCode方法，用于校验验证码，其中包含URL拼接逻辑。
画面5: Postman中展示发送验证码的请求，参数为verifyKey和verifyCode，响应为200状态码。
画面6: IDE中展示SmsServiceImp.java文件，代码中处理短信服务响应，抛出异常。
画面7: IDE中展示SmsServiceImp.java文件，代码中定义了checkVerifyCode方法，用于校验验证码，其中包含URL拼接逻辑。
画面8: IDE中展示SmsServiceImp.java文件，代码中使用RestTemplate调用短信服务，处理响应并抛出异常。
画面9: IDE中展示MerchantController.java文件，代码中调用smsService.checkVerifyCode方法进行验证码校验。
画面10: Postman中展示响应头和响应体，响应体为JSON格式，包含code、msg、result字段。
画面11: Postman中展示发送短信验证码的请求，参数为phone，请求方法为GET。
画面12: IDE中展示MerchantController.java文件，代码中调用smsService.checkVerifyCode方法进行验证码校验。
画面13: IDE中展示调试信息，显示验证码校验成功，返回结果为true。
画面14: PPT页面“2.4.3.2 校验验证码实现”，展示在SmsService中定义校验验证码的service接口和实现方法。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面2:
```java
@ApiOperation("获取手机验证码")
@ApiModelProperty(value = "手机号", name = "phone", required = true, dataType = "String")
public String getVerifyCode(@RequestParam("phone") String phone) {
    return smsService.sendMsg(phone);
}

@ApiOperation("商户注册")
@ApiModelProperty(value = "商户注册信息", name = "merchantRegisterVO", required = true, dataType = "MerchantRegisterVO")
@PostMapping("/merchant/register")
public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
    smsService.checkVerifyCode(merchantRegisterVO.getVerifyKey(), merchantRegisterVO.getVerifyCode());
    return null;
}
```

画面3:
```java
Map bodyMap = null;
try {
    exchange = restTemplate.exchange(sms_url, HttpMethod.POST, httpEntity, Map.class);
    Log.info("请求验证码服务，得到响应:{}", JSON.toJSONString(exchange));
    bodyMap = exchange.getBody();
} catch (RestClientException e) {
    throw new RuntimeException("发送验证码失败");
}
if (bodyMap == null || bodyMap.get("result") == null) {
    throw new RuntimeException("发送验证码失败");
}
Map result = (Map) bodyMap.get("result");
String key = (String) result.get("key");
Log.info("得到发送验证码对应的key:{}", key);
return key;
```

画面4:
```java
@Override
public void checkVerifyCode(String verifyKey, String verifyCode) {
    //校验验证码的url
    String url = "http://localhost:56085/sailing/verify?name=sms&verificationCode=" + verifyCode + "&verificationKey=" + verifyKey;
```

画面6:
```java
Log.info("请求验证码服务，得到响应:{}", JSON.toJSONString(exchange));
bodyMap = exchange.getBody();
} catch (RestClientException e) {
    throw new RuntimeException("发送验证码失败");
}
if (bodyMap == null || bodyMap.get("result") == null) {
    throw new RuntimeException("发送验证码失败");
}
Map result = (Map) bodyMap.get("result");
String key = (String) result.get("key");
Log.info("得到发送验证码对应的key:{}", key);
return key;
```

画面7:
```java
@Override
public void checkVerifyCode(String verifyKey, String verifyCode) {
    //校验验证码的url
    String url = "http://localhost:56085/sailing/verify?name=sms&verificationCode=" + verifyCode + "&verificationKey=" + verifyKey;
```

画面8:
```java
@Override
public void checkVerifyCode(String verifyKey, String verifyCode) {
    //校验验证码的url
    String url = "http://localhost:56085/sailing/verify?name=sms&verificationCode=" + verifyCode + "&verificationKey=" + verifyKey;
    //使用restTemplate请求验证码服务
    ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
    Log.info("请求验证码服务，得到响应:{}", JSON.toJSONString(exchange));
    bodyMap = exchange.getBody();
    if (bodyMap == null || bodyMap.get("result") == null) {
        throw new RuntimeException("校验验证码失败");
    }
}
```

画面9:
```java
@ApiOperation("商户注册")
@ApiModelProperty(value = "商户注册信息", name = "merchantRegisterVO", required = true, dataType = "MerchantRegisterVO")
@PostMapping("/merchant/register")
public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
    smsService.checkVerifyCode(merchantRegisterVO.getVerifyKey(), merchantRegisterVO.getVerifyCode());
    return null;
}
```

画面12:
```java
@ApiOperation("商户注册")
@ApiModelProperty(value = "商户注册信息", name = "merchantRegisterVO", required = true, dataType = "MerchantRegisterVO")
@PostMapping("/merchant/register")
public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
    smsService.checkVerifyCode(merchantRegisterVO.getVerifyKey(), merchantRegisterVO.getVerifyCode());
    return null;
}
```

画面13:
```java
try {
    //使用restTemplate请求验证码服务
    ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
    Log.info("请求验证码服务，得到响应:{}", JSON.toJSONString(exchange));
    bodyMap = exchange.getBody();
    if (bodyMap == null || bodyMap.get("result") == null) {
        throw new RuntimeException("校验验证码失败");
    }
    if (bodyMap.get("result").equals("true")) {
        Log.info("验证码校验成功");
        return true;
    }
}
```

画面14:
```java
/**
 * 校验验证码，抛出异常则校验无效
 * @param verifyKey 验证码key
 * @param verifyCode 验证码
 */
void checkVerifyCode(String verifyKey, String verifyCode);

public void checkVerifyCode(String verifyKey, String verifyCode) {
    //实现校验验证码的逻辑
    String url = smsUrl + "/verify?name=sms&verificationCode=" + verifyCode + "&verificationKey=" + verifyKey;
    ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
    try {
        //请求校验验证码
        ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1: 标题“2.1.1 系统交互流程”，图中“消费者”指向“商户平台”，“商户平台”指向“商户服务”，“商户服务”指向“Sms平台”，“Sms平台”指向“验证到服务”，“验证到服务”指向“商户平台”。
画面14: 标题“2.4.3.2 校验验证码实现”，图中“在SmsService中定义校验验证码的service接口”指向“在SmsServiceImpl中定义校验验证码的service实现方法”。

5) 无。
