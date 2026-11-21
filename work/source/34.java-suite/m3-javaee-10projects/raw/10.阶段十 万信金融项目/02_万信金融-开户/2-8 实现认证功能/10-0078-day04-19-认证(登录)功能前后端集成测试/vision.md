# 画面线理解：day04-19-认证(登录)功能前后端集成测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-8 实现认证功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-8 实现认证功能\day04-19-认证(登录)功能前后端集成测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:39, 00:47, 01:09, 01:13, 01:22, 01:27, 02:30, 02:32, 02:46, 02:52, 03:02, 03:09, 03:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:53:15

1) 这一组画面整体在讲什么（一句话）：
演示如何通过前端登录页面发起请求，后端服务生成令牌，并在浏览器中展示登录成功后的首页。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PDF文档“UAA服务配置指南”，章节3.1“集成UAA服务”介绍UAA服务是P2P平台的统一认证中心，使用Spring Security整合OAuth2.0实现授权服务。
画面2：展示PDF文档“UAA服务配置指南”，章节4.3.1“登录(生成令牌)”，说明登录时生成并返回令牌，访问路径为POST http://localhost:53020/uaa/token，并列出请求参数。
画面3：展示PDF文档“UAA服务配置指南”，章节4.3.3“前后端集成测试”，说明登录功能的前后端集成测试由学员自行完成。
画面4：展示PDF文档“黑马程序员”课程资料，章节4.7“前后端集成测试”，说明在Apollo中对网关服务增加路由配置。
画面5：展示PDF文档“黑马程序员”课程资料，章节4.7“前后端集成测试”，展示Apollo中配置的路由规则代码。
画面6：展示PDF文档“UAA服务配置指南”，章节4.3.3“前后端集成测试”，再次强调前后端集成测试由学员自行完成。
画面7：展示浏览器中万信金融登录页面，用户输入手机号和验证码。
画面8：展示浏览器开发者工具Network面板，显示登录请求已发送，同时弹出命令行窗口。
画面9：展示命令行窗口，显示服务启动日志，包括“Starting w...”和“给手机号15378791911发送验证码，801132”。
画面10：展示浏览器开发者工具Network面板，显示登录成功后页面加载，请求列表中包含“token”。
画面11：展示浏览器开发者工具Network面板，显示登录成功后页面加载，请求列表中包含“token”和“group-1”。
画面12：展示浏览器开发者工具Network面板，选中“token”请求，查看其响应头。
画面13：展示浏览器开发者工具Network面板，查看“token”请求的响应头，包含“Access-Control-Allow-Credentials: true”等。
画面14：展示浏览器开发者工具Network面板，查看“token”请求的响应体，包含“access_token”字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4和5中的配置代码：
```yaml
zull.routes.consumer-service.stripPrefix = false
zull.routes.account-service.stripPrefix = false
zull.routes.account-service.path = /account/**
zull.routes.consumer-service.path = /consumer/**
zull.retryable = true
zull.add-host-header = true
zull.ignoredServices = *
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4和5中的PPT标题：“4.7 前后端集成测试”，内容包括：
1. 在Apollo中对网关服务增加路由配置
2. 启动前端工程
3. 启动Apollo
4. 后端需要启动：
   - wanningp2p-discover-server微服务
   - wanningp2p-gateway-server微服务
   - wanningp2p-account-server微服务

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
