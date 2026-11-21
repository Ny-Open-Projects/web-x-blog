# 画面线理解：day04-17-认证(登录)功能测试(过网关)

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-8 实现认证功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-8 实现认证功能\day04-17-认证(登录)功能测试(过网关)_【海量资源尽在 666java.com】.mp4
- 抽帧：12 帧 @ 00:47, 01:15, 01:19, 01:23, 01:26, 01:56, 02:00, 02:02, 02:05, 02:06, 02:31, 02:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:52:05

1) 这一组画面整体在讲如何通过 Postman 发起 OAuth2.0 认证请求，并结合 Apollo 配置中心管理微服务的路由规则。

2) 按时间顺序列出每张画面的要点：
画面1：Postman 中选中“统一认证中心”集合下的“登录获取令牌”请求，准备发送。
画面2：IntelliJ IDEA 中打开项目 wanxingzp-uaa-service，准备启动服务。
画面3：在 IntelliJ IDEA 中，点击“Run”菜单，准备运行服务。
画面4：在 IntelliJ IDEA 的运行配置中，将 Main class 设置为 cn.itcast.wanxingzp.uaa.GatewayServer，启动网关服务。
画面5：Postman 中编辑 POST 请求，设置 URL 为 http://localhost:5331/oauth/token，Body 为 form-data 格式，包含 grant_type、client_id、client_secret、username、password、domain、authenticationType 等参数。
画面6：浏览器访问 Apollo 配置中心首页，显示项目列表。
画面7：浏览器访问 Apollo 配置中心的配置页面，URL 为 localhost:8070/config.html#/?appId=gateway-server。
画面8：在 Apollo 配置中心，选择“application”配置项，查看其下多个微服务的配置。
画面9：在 Apollo 配置中心，点击“新增配置”按钮，准备添加新的配置。
画面10：在 Apollo 配置中心，编辑“application”配置项，显示其内容，包括多个 zuul.routes 的配置。
画面11：Postman 中再次显示“登录获取令牌”请求的 Body 参数。
画面12：Postman 中发送请求后，显示响应结果，包含 access_token、token_type、expires_in、scope、code 等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4 中的运行配置：
Main class: cn.itcast.wanxingzp.gateway.GatewayServer
JVM options: -Dspring.profiles.active=dev -Dserver.port=8080
Program arguments: 
Working directory: 
Environment variables: 
Use classpath of modules: wanxingzp-gateway-server
Include dependencies with "Provided" scope: true
Spring Boot JAR: Default (1.8.0-SNAPSHOT)
Shorten command line: true
Enable debug output: false
Hide banner: true
Enable launch optimization: true
Enable JMX Agent: true
Running debug actions: Do nothing
On Update actions: Do nothing
On frame destruction: Do nothing
Active profiles: dev

画面10 中的 Apollo 配置内容：
zuul.routes.consumer-service.stripPrefix = false
zuul.routes.account-service.stripPrefix = false
zuul.routes.naa-service.stripPrefix = false
zuul.routes.account-service.path = /account
zuul.routes.consumer-service.path = /consumer
zuul.routes.naa-service.path = /naa
zuul.retryable = true
zuul.add-host-header = true
zuul.ignoredServices = 

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
