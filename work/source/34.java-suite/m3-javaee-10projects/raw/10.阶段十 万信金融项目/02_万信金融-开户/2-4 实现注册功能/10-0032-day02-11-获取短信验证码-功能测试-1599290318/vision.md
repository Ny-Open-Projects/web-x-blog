# 画面线理解：day02-11-获取短信验证码-功能测试-1599290318

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-11-获取短信验证码-功能测试-1599290318_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:17, 03:02, 03:22, 04:00, 05:09, 06:22, 07:50, 09:04, 10:02, 10:56, 11:40, 12:26, 14:00, 15:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:20:03

1) 这一组画面整体在讲一个基于 Spring Cloud 的微服务系统中，如何通过 Apollo 配置中心动态管理短信服务的开关和 URL，并通过 Swagger 和 Postman 调用短信接口。

2) 按时间顺序列出每张画面的要点：
画面1：展示 IDEA 中 SmsService.java 文件，其中定义了 @Value("${sms.url}") 和 @Value("${sms.enable}") 注解，用于从配置中心注入短信服务的 URL 和开关状态。
画面2：展示一个系统架构流程图，描述了用户中心服务、统一账户服务、认证服务、短信服务之间的交互流程。
画面3：IDEA 中 SmsService.java 文件，高亮显示 @Value("${sms.enable}") 注解，强调其配置注入功能。
画面4：IDEA 中，鼠标点击了 application.yml 文件，准备查看或编辑配置。
画面5：IDEA 中 AccountController.java 文件，高亮显示 @ApiOperation("获取手机验证码") 注解和 @GetMapping("/sms/{mobile}") 方法，说明该接口用于获取短信验证码。
画面6：Apollo 配置中心界面，显示了多个命名空间，包括 micro_service.spring-boot-http、micro_service.spring-eureka、micro_service.spring-hystrix、micro_service.spring-ribbon、micro_service.spring-boot-druid。
画面7：Swagger UI 页面，显示正在加载中。
画面8：Swagger UI 页面，显示了 GET 请求的响应结果，响应体为 {"code": 0, "msg": "", "result": {"key": "sms:95cf..."}, "content": "null"}。
画面9：Windows 资源管理器，显示了 runSms-student.bat 文件，内容为启动短信服务的脚本。
画面10：Swagger UI 页面，显示了 GET /sms/{mobile} 接口的参数输入框，输入手机号 15378791917。
画面11：Swagger UI 页面，显示了 GET 请求的响应结果，响应体为 {"code": 0, "msg": "", "result": {"key": "sms:95cf..."}, "content": "null"}。
画面12：Postman 界面，显示了 GET 请求的 URL 和响应体，响应体为 {"code": 0, "msg": "", "result": {"key": "sms:95cf..."}, "content": "null"}。
画面13：IDEA 中 AccountService.java 文件，高亮显示了 getSMSCode(String mobile) 方法和 verifyCode(String key, String code) 方法，说明短信服务的实现逻辑。
画面14：Postman 界面，显示了 GET 请求的 URL 和响应体，响应体为 {"code": 0, "msg": "", "result": {"key": "sms:95cf..."}, "content": "null"}。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package cn.itcast.wanxingzp.account.service;

import ...

@Service
public class SmsService {
    @Value("${sms.url}")
    private String smsURL;
    @Value("${sms.enable}")
    private Boolean smsEnable.
}
```

画面5：
```java
@Api(value = "统一账户服务的API")
public class AccountController implements AccountAPI {

    private AccountService accountService;

    @ApiOperation("测试")
    @GetMapping("/hello")
    public String hello() { return "hello".}
    
    @ApiOperation("获取手机验证码")
    @GetMapping("/sms/{mobile}", value = "手机号", dataType = "String")
    public RestResponse getSMSCode(@PathVariable String mobile) { return accountService.getSMSCode(mobile); }
}
```

画面13：
```java
@Autowired
private SmsService smsService;

@Value("${sms.enable}")
private Boolean smsEnable.

@Override
public RestResponse getSMSCode(String mobile) {
    return smsService.getSMSCode(mobile);
}

@Override
public Integer checkMobile(String mobile, String key, String code) {
    smsService.verifyCode(key, code);
    QueryWrapper<Account> wrapper=new QueryWrapper<>();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：架构图标题为“222平台”，图中包含五个服务模块：浏览器/App、用户中心服务、UAA认证服务、统一账户、验证码服务。流程如下：
1. 浏览器/App → 用户中心服务（输入手机号）
2. 用户中心服务 → 统一账户（获取验证码）
3. 统一账户 → 验证码服务（获取短信验证码）
4. 验证码服务 → 统一账户（发送短信）
5. 统一账户 → 用户中心服务（返回验证码）
6. 用户中心服务 → 浏览器/App（返回结果）
7. 用户中心服务 → 统一账户（检查手机号是否已注册）
8. 统一账户 → 用户中心服务（返回结果）
9. 用户中心服务 → 统一账户（返回结果）
10. 用户中心服务 → 浏览器/App（返回结果）
11. 浏览器/App → 用户中心服务（未注册）
12. 用户中心服务 → 统一账户（发送注册请求）
13. 统一账户 → 用户中心服务（返回注册结果）

5) 不要评价画面美观，不要输出与课程无关的内容。
