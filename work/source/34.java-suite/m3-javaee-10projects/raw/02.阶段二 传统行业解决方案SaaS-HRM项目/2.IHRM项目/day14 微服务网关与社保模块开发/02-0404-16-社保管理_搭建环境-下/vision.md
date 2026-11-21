# 画面线理解：16-社保管理：搭建环境-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\16-社保管理：搭建环境-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:16, 01:26, 01:34, 01:42, 01:58, 02:07, 02:33, 02:45, 03:15, 03:45, 04:07, 04:27, 04:52, 05:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:20:04

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Postman 调用 Spring Boot 服务的登录接口和获取企业设置接口，并展示相关代码和配置文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：IDEA 编辑器中显示 SocialSecurityApplication.java 的 main 方法，其中包含 @Bean 注解定义的 IdWorker、JwtUtils 和 OpenEntityManagerInViewFilter。
画面2：浏览器开发者工具 Network 面板显示登录请求的 Request Payload，包含 mobile 和 password 字段。
画面3：桌面多窗口视图，展示多个开发工具和文档窗口。
画面4：浏览器开发者工具 Network 面板显示登录请求的 Response Headers，状态码为 200。
画面5：Postman 中配置了登录请求的 Body，包含 mobile 和 password 字段。
画面6：IDEA 编辑器中显示 SocialSecurityController.java 的 settings 方法，用于查询企业设置。
画面7：Postman 中登录请求的响应结果，显示错误信息。
画面8：Postman 中准备发送 GET 请求以获取企业设置。
画面9：Postman 中 GET 请求的响应结果，显示成功获取企业设置的 JSON 数据。
画面10：IDEA 编辑器中显示项目结构，包含 SocialSecurityController.java 和 settings/Result 等类。
画面11：IDEA 编辑器中显示 ihm_gate 模块的 application.yml 配置文件，包含多个服务的路径和敏感头配置。
画面12：IDEA 控制台显示 Spring Boot 启动日志，包含 Eureka 服务注册和 Ribbon 负载均衡信息。
画面13：IDEA 控制台显示 Spring Boot 启动日志，包含服务注册成功和 Eureka 服务发现信息。
画面14：IDEA 编辑器中显示 ihm_gate 模块的 application.yml 配置文件，包含 ihm-social-security 服务的路径和敏感头配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public static void main(String[] args) {
    SpringApplication.run(SocialSecurityApplication.class, args);
}
@Bean
public IdWorker idWorker() { return new IdWorker(); }
@Bean
public JwtUtils jwtUtils() { return new JwtUtils(); }
//解决no session
@Bean
public OpenEntityManagerInViewFilter openEntityManagerInViewFilter() { return new OpenEntityManagerInViewFilter(); }
```

画面2：
```json
{
  "mobile": "1280000002",
  "password": "123456"
}
```

画面5：
```json
{
  "mobile": "1280000002",
  "password": "123456"
}
```

画面6：
```java
package com.ihrm.social.controller;
import ...
@RestController("/social/security")
public class SocialSecurityController extends BaseController {
    @Autowired
    private CompanySettingsService companySettingsService;
    /**
     * 查询企业是否设置过社保
     */
    @RequestMapping(value = "/settings", method = RequestMethod.GET)
    public Result settings() {
        CompanySettings cs = companySettingsService.findById(companyId);
        return new Result(ResultCode.SUCCESS, cs);
    }
}
```

画面11：
```yaml
uri: http://127.0.0.1:9001 # 时路径对应的实际服务的url路径
serviceId: ihm-company # 指定Eureka注册中心中的服务id
stripPrefix: false # 对指定路由开启自定义敏感头
sensitiveHeaders: true # 对指定路由开启自定义敏感头
customSensitiveHeaders: true # 对指定路由开启自定义敏感头
path: /sys/ # 指定请求URL的请求规则
serviceId: ihm-system # 指定Eureka注册中心中的服务id
stripPrefix: false # 对指定路由开启自定义敏感头
sensitiveHeaders: true # 对指定路由开启自定义敏感头
customSensitiveHeaders: true # 对指定路由开启自定义敏感头
path: /employee/ # 指定请求URL的请求规则
serviceId: ihm-employee # 指定Eureka注册中心中的服务id
stripPrefix: false # 对指定路由开启自定义敏感头
sensitiveHeaders: true # 对指定路由开启自定义敏感头
customSensitiveHeaders: true # 对指定路由开启自定义敏感头
```

画面14：
```yaml
uri: http://127.0.0.1:9001 # 时路径对应的实际服务的url路径
serviceId: ihm-social-security # 指定Eureka注册中心中的服务id
stripPrefix: false # 对指定路由开启自定义敏感头
sensitiveHeaders: true # 对指定路由开启自定义敏感头
customSensitiveHeaders: true # 对指定路由开启自定义敏感头
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
