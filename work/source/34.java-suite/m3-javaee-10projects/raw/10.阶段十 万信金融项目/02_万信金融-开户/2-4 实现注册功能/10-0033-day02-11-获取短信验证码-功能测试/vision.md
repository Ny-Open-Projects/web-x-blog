# 画面线理解：day02-11-获取短信验证码-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-11-获取短信验证码-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 02:16, 03:25, 03:54, 04:30, 07:08, 07:57, 08:39, 09:56, 10:20, 10:40, 11:09, 11:49, 12:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:20:39

1) 这一组画面整体在讲如何通过 Apollo 配置中心动态管理短信服务的开关和 URL，并在 Spring Boot 项目中实现短信验证码的发送与验证功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示 SmsService.java 代码，其中定义了 @Value("${sms.url}") 和 @Value("${sms.enable}") 注解，用于从配置中心注入短信 URL 和开关状态。方法 getSMSCode 会根据 smsEnable 是否为 true 来决定是否发送短信。
画面2：展示 SmsService.java 代码，与画面1相同，但光标位置不同，强调了 @Value 注解的使用。
画面3：展示 AccountController.java 代码，其中定义了 @GetMapping("/sms/{mobile}") 方法，用于获取手机验证码，调用 accountService.getSMSCode(mobile)。
画面4：展示 Apollo 配置中心界面，显示了 application 和多个关联配置项（如 micro_service.spring-boot-http、micro_service.spring-eureka 等）。
画面5：在 Apollo 配置中心的 application 配置项中，展示了已配置的 Key-Value 对，包括 swagger.enable、spring.mvc.throw-exception-if-no-handler-found、smsurl、smsenable 等。
画面6：展示一个流程图，描述了用户注册流程，包括用户输入手机号、获取验证码、验证验证码、注册等步骤，涉及用户中心服务、UAA认证服务、统一账户服务和短信服务。
画面7：展示 SmsService.java 代码，其中 getSMSCode 方法的实现，使用 OkHttpUtil.post 发送请求。
画面8：展示 Postman 中的“SAVE REQUEST”弹窗，用于保存请求。
画面9：展示 Postman 中的 GET 请求，URL 为 http://localhost:55030/account/tm/15370791917，用于获取验证码。
画面10：展示 SmsService.java 代码，其中定义了 verifySMCode 方法，用于验证短信验证码。
画面11：展示 Windows 资源管理器，路径为 waraninp2p > day02 > 资料，显示了一个名为“短信验证码服务”的文件夹。
画面12：展示 Postman 中的 GET 请求，URL 为 http://localhost:55030/account/tm/15370791917，用于验证短信验证码。
画面13：展示 AccountController.java 代码，其中定义了 @GetMapping("/sms/{mobile}") 和 @GetMapping("/sms/verify") 方法，用于获取和验证短信验证码。
画面14：展示 Postman 中的 GET 请求，URL 为 http://localhost:55030/account/tm/15370791917，返回的 JSON 数据包含 code、msg、result 和 content 字段。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
public class SmsService {
    @Value("${sms.url}")
    private String smsURL;
    @Value("${sms.enable}")
    private Boolean smsEnable;
    public RestResponse getSMSCode(String mobile) {
        if (smsEnable) {
            return OkHttpUtil.post(url: smsURL + "/generateEffectiveTime=300&name=sms", json: "{ \"mobile\": \"\" }");
        }
        return RestResponse.success();
    }
}
```

画面3：
```java
@GetMapping("/sms/{mobile}")
public RestResponse getSMSCode(@PathVariable String mobile) {
    return accountService.getSMSCode(mobile);
}
```

画面5：
```
Key: swagger.enable
Value: true
Key: spring.mvc.throw-exception-if-no-handler-found
Value: true
Key: smsurl
Value: http://localhost:56085/sms/
Key: smsenable
Value: true
```

画面10：
```java
public void verifySMCode(String key, String code) {
    StringBuilder params = new StringBuilder();
    params.append("verifyName=sms").append("&").append("VerificationKey=").append(key).append("&").append("VerificationCode=").append(code);
    OkHttpUtil.execute(params.toString());
}
```

画面13：
```java
@GetMapping("/sms/{mobile}")
public RestResponse getSMSCode(@PathVariable String mobile) {
    return accountService.getSMSCode(mobile);
}

@GetMapping("/sms/verify")
public RestResponse verifySMCode(@RequestParam("mobile") String mobile, @RequestParam("code") String code) {
    return accountService.verifySMCode(mobile, code);
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面6：流程图结构：
- 用户输入手机号 → 获取验证码 → 验证验证码 → 注册
- 用户中心服务 → UAA认证服务 → 统一账户服务 → 短信服务
- 1. 用户输入手机号
- 2. 获取验证码
- 3. 获取短信验证码
- 4. 发送短信
- 5. 返回此次校验标识
- 6. 返回验证码
- 7. 校验手机号是否已注册
- 8. 返回校验结果
- 9. 返回校验结果
- 10. 返回校验结果
- 11. 未注册
- 12. 发起注册请求
- 13. 用户注册
- 14. 返回注册结果
- 15. 返回注册结果
- 16. 注册成功

5) 无。
