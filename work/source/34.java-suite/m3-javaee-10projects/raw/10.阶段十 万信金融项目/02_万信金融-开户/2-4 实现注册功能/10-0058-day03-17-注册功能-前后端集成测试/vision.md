# 画面线理解：day03-17-注册功能-前后端集成测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-17-注册功能-前后端集成测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 01:00, 01:42, 02:15, 03:17, 03:43, 04:54, 06:45, 07:58, 09:27, 10:06, 10:32, 11:31, 12:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:39:21

1) 这一组画面整体在讲什么（一句话）：
演示如何通过配置 Apollo 实现前后端联调，包括网关路由配置、服务启动顺序、用户登录流程及后端接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面“4.7 前后端集成测试”，要点包括：1. 在 Apollo 中对网关服务增加路由配置（代码片段：`zuul.routes.consumer-service.stripPrefix = false` 等）；2. 启动前端工程；3. 启动 Apollo；4. 后端需要启动的服务列表（`waxinxp2p-discover-server`、`waxinxp2p-gateway-server`、`waxinxp2p-account-service`、`waxinxp2p-consumer-service`、短信验证码服务）。
画面2：PPT 页面“4.7 前后端集成测试”，要点同画面1，鼠标在代码片段上。
画面3：IDE 中展示 `AccountService` 服务的 `register` 方法代码，用于处理用户注册逻辑。
画面4：PPT 页面“4.7 前后端集成测试”，要点同画面1，鼠标在代码片段上。
画面5：PPT 页面“4.7 前后端集成测试”，要点同画面1，鼠标在代码片段上。
画面6：PPT 页面“5 用户登录”，要点包括：5.1 传统实现方式；注意：所有前端到后端的请求都经过网关服务（gateway-server），它是无处不在的，但很多图中并未画出，因为它是一个基础组件，没必要在每个图中都画出来。
画面7：浏览器显示用户登录页面，URL 为 `localhost:8081/#/pages/user/login`，页面包含“点击发送”和“登录”按钮。
画面8：PPT 页面“5 用户登录”，要点同画面6。
画面9：IDE 中展示 `ConsumerController` 的 `checkPhone` 方法代码，用于验证手机号。
画面10：PPT 页面“5 用户登录”，要点同画面6。
画面11：IDE 中展示 `ConsumerService` 的 `register` 方法代码，用于处理用户注册逻辑。
画面12：IDE 中展示 `ConsumerService` 的 `register` 方法代码，终端显示服务启动日志。
画面13：数据库管理工具（SQLyog）中显示 `p2p_consumer` 数据库的表结构，包括 `account`、`account_privilege`、`consumer` 等表。
画面14：浏览器显示用户登录页面，URL 为 `localhost:8081/#/pages/user/login`，页面包含“点击发送”和“登录”按钮，右侧显示网络请求响应数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```properties
zuul.routes.consumer-service.stripPrefix = false
zuul.routes.account-service.stripPrefix = false
zuul.routes.account-service.path = /account/**
zuul.routes.consumer-service.path = /consumer/**
zuul.retryable = true
zuul.add-host-header = true
zuul.ignoredServices =
```
画面3：
```java
public AccountDTO register(AccountRegisterDTO accountRegisterDTO) {
    Account account = new Account();
    account.setUserName(accountRegisterDTO.getUserName());
    account.setMobile(accountRegisterDTO.getMobile());
    account.setAccountPassword(accountRegisterDTO.getPassword());
    if (smsEnable) {
        account.setPasswordPassword(smsUtil.generateAccountRegisteredDTO().getMobile());
    }
    account.setDomain("2");
    save(account);
    return convertAccountEntity2DTO(account);
}
```
画面9：
```java
@ApiOperation("校验手机号")
@PostMapping("/checkPhone")
public ResponseEntity checkPhone(@RequestParam("phone") String phone) {
    // 业务逻辑
}
```
画面11：
```java
public String hi(String name) {
    return "hi," + name;
}
```
画面12：
```java
[main] INFO org.springframework.boot.context.embedded.tomcat.TomcatStarter: Tomcat started on port(s): 8080 (http)
[main] INFO org.springframework.boot.context.embedded.tomcat.TomcatStarter: Tomcat started on port(s): 8080 (http)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题“4.7 前后端集成测试”，内容包括：
- 1. 在 Apollo 中对网关服务增加路由配置（代码片段）
- 2. 启动前端工程
- 3. 启动 Apollo
- 4. 后端需要启动的服务列表（`waxinxp2p-discover-server`、`waxinxp2p-gateway-server`、`waxinxp2p-account-service`、`waxinxp2p-consumer-service`、短信验证码服务）
画面6：PPT 标题“5 用户登录”，内容包括：
- 5.1 传统实现方式
- 注意：所有前端到后端的请求都经过网关服务（gateway-server），它是无处不在的，但很多图中并未画出，因为它是一个基础组件，没必要在每个图中都画出来。
画面14：浏览器显示用户登录页面，右侧显示网络请求响应数据，包括：
- Name: 13877801912
- result: 1
- msg: "success"

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
