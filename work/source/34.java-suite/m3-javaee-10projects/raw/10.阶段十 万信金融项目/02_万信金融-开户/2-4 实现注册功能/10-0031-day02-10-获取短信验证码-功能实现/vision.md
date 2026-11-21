# 画面线理解：day02-10-获取短信验证码-功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-10-获取短信验证码-功能实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 02:59, 04:32, 05:47, 07:59, 09:08, 10:27, 11:48, 12:56, 15:28, 16:44, 17:41, 18:13, 18:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:19:25

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现短信验证码服务，从控制器层到服务层，再到调用外部短信接口并配置相关参数。

2) 按时间顺序列出每张画面的要点：
画面1：展示 AccountController.java 文件，其中定义了获取手机验证码的接口方法 @GetMapping("/sms/{mobile}")，并使用 @ApiImplicitParam 注解指定参数 mobile 为 String 类型。
画面2：展示 AccountService.java 接口文件，其中定义了获取短信验证码的方法 getsMSCode(String mobile)。
画面3：展示 AccountServiceImpl.java 文件，其中实现了 AccountService 接口，但当前方法体为空，仅返回 null。
画面4：在项目结构中选中 SmsService.java 文件，准备创建短信服务类。
画面5：打开 SmsService.java 文件，准备编写短信服务实现。
画面6：展示一个系统架构流程图，描述了用户注册流程中各服务（浏览器/App、用户中心服务、UAA认证服务、统一账户服务、验证码服务）之间的交互顺序。
画面7：打开 Apollo 配置中心页面，地址为 localhost:8070/config.html#/appId=account-service，页面为空白，准备进行配置。
画面8：在 SmsService.java 中，使用 OkHttpUtil.post() 方法发起 HTTP 请求。
画面9：在 SmsService.java 中，设置 HTTP 请求的 URL 为 http://localhost:56085/sailing/generate?effectiveTime=300&name=sms。
画面10：在 SmsService.java 中，使用 @Value("${sms.url}") 注解注入短信接口 URL。
画面11：在 SmsService.java 中，高亮显示了 @Value("${sms.url}") 注解。
画面12：在 SmsService.java 中，使用 @Value("${sms.enable}") 注解注入短信服务开关。
画面13：在 SmsService.java 中，添加了判断开关是否开启的逻辑，如果关闭则返回成功响应。
画面14：在 AccountServiceImpl.java 中，注入 SmsService 并在实现方法中调用它。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AccountController implements AccountAPI {

    @Override
    @ApiOperation("获取手机验证码")
    @ApiImplicitParam(name = "mobile", value = "手机号", dataType = "String")
    @GetMapping("/sms/{mobile}")
    public RestResponse getSmsCode(@PathVariable String mobile) {
        return null;
    }
}
```

画面2：
```java
package cn.itcast.wanxing2p.account.service;

public interface AccountService {
    // 获取手机短信验证码
    RestResponse getsMSCode(String mobile);
}
```

画面3：
```java
package cn.itcast.wanxing2p.account.service;

import org.springframework.stereotype.Service;

@Service
public class AccountServiceImpl implements AccountService {

    @Override
    public RestResponse getSmsCode(String mobile) {
        return null;
    }
}
```

画面4：
```java
package cn.itcast.wanxing2p.account.service;

@Service
public class SmsService {
}
```

画面5：
```java
package cn.itcast.wanxing2p.account.service;

@Service
public class SmsService {

    public RestResponse getSmsCode(String mobile) {
    }
}
```

画面6：
流程图内容：
- 浏览器/App → 用户中心服务 → UAA认证服务 → 统一账户服务 → 验证码服务
- 1. 用户输入手机号 → 2. 获取验证码 → 3. 获取短信验证码 → 4. 发送短信
- 5. 返回此次校验标识 → 6. 返回手机是否已注册 → 7. 检查手机号是否已注册 → 8. 校验短信验证码 → 9. 返回校验结果
- 10. 返回结果 → 11. 未注册 → 12. 发起注册请求 → 13. 客户注册 → 14. 保存注册信息 → 15. 返回注册结果 → 16. 注册成功

画面7：
URL: localhost:8070/config.html#/appId=account-service

画面8：
```java
public RestResponse getSmsCode(String mobile) {
    OkHttpUtil.post();
}
```

画面9：
```java
public RestResponse getSmsCode(String mobile) {
    OkHttpUtil.post("http://localhost:56085/sailing/generate?effectiveTime=300&name=sms", "");
}
```

画面10：
```java
@Value("${sms.url}")
private String smsURL;
```

画面11：
```java
@Value("${sms.url}")
private String smsURL;
```

画面12：
```java
@Value("${sms.enable}")
private Boolean smsEnable;
```

画面13：
```java
public RestResponse getSmsCode(String mobile) {
    if (!smsEnable) {
        return RestResponse.success();
    }
    return OkHttpUtil.post(smsURL + "/generate?effectiveTime=300&name=sms", json("{mobile:" + mobile + "}");
}
```

画面14：
```java
@Autowired
private SmsService smsService;

@Override
public RestResponse getSmsCode(String mobile) {
    return smsService.getSmsCode(mobile);
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面6：架构图标题为“用户注册流程”，图中包含五个服务模块：浏览器/App、用户中心服务、UAA认证服务、统一账户服务、验证码服务。流程图描述了用户从输入手机号到注册成功的完整流程，包含16个步骤，其中步骤3和步骤4是与验证码服务的交互。

5) 无。
