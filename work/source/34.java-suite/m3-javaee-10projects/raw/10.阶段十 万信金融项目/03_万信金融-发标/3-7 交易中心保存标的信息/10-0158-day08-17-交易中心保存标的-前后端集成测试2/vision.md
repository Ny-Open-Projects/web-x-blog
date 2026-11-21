# 画面线理解：day08-17-交易中心保存标的-前后端集成测试2

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-7 交易中心保存标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-7 交易中心保存标的信息\day08-17-交易中心保存标的-前后端集成测试2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:35, 00:38, 01:07, 01:14, 01:22, 01:27, 01:35, 01:46, 01:49, 02:14, 02:45, 03:04, 03:35, 03:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:55:24

1) 这一组画面整体在讲什么（一句话）：
演示一个基于微服务架构的用户登录与交易流程，涉及网关、认证服务、消费者服务、交易服务及数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- IDE中展示`ProjectServiceImpl.java`文件，其中`createProject`方法调用`consumerApiAgent.getCurConsumer(...)`获取用户信息，并设置项目状态为`COLLECTING`。
- 代码片段：
  ```java
  private ConfigService configService;
  @Override
  public ProjectDTO createProject(ProjectDTO projectDTO) {
      RestResponse<ConsumerDTO> restResponse = consumerApiAgent.getCurConsumer(SecurityUtil.getSer().getMobile());
      projectDTO.setConsumerId(restResponse.getRtnId());
      projectDTO.setProjectCode(restResponse.getRtnCode());
      projectDTO.setProjectName(projectDTO.getProjectCode() + "_"+ CodeUtil.getCodePrefix());
      // 标的状态修改
      projectDTO.setProjectStatus(ProjectCode.COLLECTING, getCode());
      // 标的可用性修改，不同步
  }
  ```

画面2：
- 展示一个微服务架构图，包含接入方（WEB、移动端、第三方接入）、网关、认证服务（UAA）、多个微服务（微服务1、2、3...n）。
- 流程说明：
  1. 接入方通过网关接入。
  2. 网关将请求转发至认证服务（UAA）进行认证。
  3. 认证服务返回用户信息。
  4. 网关将认证后的请求转发至对应的微服务。
  5. 认证服务提供统一账号服务。
  6. 注：UAA服务提供了标准化的认证方式配置，可拆分为两个维度：domain、用户组、SaaS用户、应用平台、认证类型、认证策略、二阶段认证等。

画面3：
- 展示多个窗口，包括IDE、数据库管理工具（SQLyog）、浏览器（Google Chrome）、以及多个服务的终端窗口（如adminService、coreService、ApolloPortal）。
- 说明：演示系统各组件的运行状态和交互。

画面4：
- 与画面2相同，展示微服务架构图。

画面5：
- IDE中展示`ConsumerController.java`文件，其中定义了两个REST接口：
  - `@ApiOperation("获取登录用户信息")`，对应路径`/currConsumer/{mobile}`，调用`consumerService.getMobile(...)`。
  - `@ApiOperation("获取登录用户信息")`，对应路径`/my/consumers`，调用`consumerService.getCurConsumer(...)`。

画面6：
- IDE中展示`ConsumerApiAgent.java`文件，定义了一个`ConsumerApiAgent`接口，包含一个方法：
  ```java
  @FeignClient(value = "consumer-service")
  public interface ConsumerApiAgent {
      @GetMapping("/consumer/currConsumer/{mobile}")
      RestResponse<ConsumerDTO> getCurConsumer(@PathVariable("mobile") String mobile);
  }
  ```

画面7：
- 数据库管理工具SQLyog中展示`p2p_consumer`表的数据，包含多个字段如`ID`、`USERNAME`、`MOBILE`、`USER_TYPE`、`ROLE`、`STATUS`等。

画面8：
- 浏览器中展示一个名为“万信金融”的Web页面，页面包含一个“立即借款”按钮。
- 网络面板显示了请求的响应状态码为200，资源包括`index.js`、`index.css`等。

画面9：
- 浏览器中展示“万信金融”页面，显示“申请成功”，并提示“资料审核中”。
- 网络面板显示了请求的响应状态码为200。

画面10：
- 展示多个窗口，包括IDE、数据库管理工具、浏览器、以及多个服务的终端窗口。
- 说明：演示系统各组件的运行状态和交互。

画面11：
- 浏览器中展示“万信金融”页面，显示“资料审核中”，并提示“审核中”。
- 网络面板显示了请求的响应状态码为200，请求体包含JSON数据：
  ```json
  {
    "name": "田博士",
    "description": "个人生活消费",
    "type": "NEW",
    "period": 120,
    "annualRate": 0.06
  }
  ```

画面12：
- 数据库管理工具SQLyog中展示`p2p_transaction`数据库的表结构，包含多个表如`p2p_account`、`p2p_deposit`、`p2p_transaction`等。

画面13：
- 数据库管理工具SQLyog中展示`p2p_transaction`数据库的`project`表，包含字段如`ID`、`DESCRIPTION`、`TYPE`、`PERIOD`、`ANNUAL_RATE`、`REPAYMENT`等。

画面14：
- 展示一个流程图，包含“交易端/APP”、“交易中心”、“交易代理服务”、“标的特性服务”、“存管系统”等模块。
- 流程说明：
  1.1 交易端/APP发起请求。
  1.2 交易中心处理请求。
  1.3 交易端/APP接收响应。
  2.1 交易中心处理请求。
  2.2 交易代理服务处理请求。
  2.3 标的特性服务处理请求。
  2.4 存管系统处理请求。
  2.5 交易中心处理请求。
  2.6 交易代理服务处理请求。
  2.7 标的特性服务处理请求。
  2.8 存管系统处理请求。
  2.9 交易中心处理请求。
  2.10 交易代理服务处理请求。
  2.11 标的特性服务处理请求。
  2.12 存管系统处理请求。
  2.13 交易中心处理请求。
  2.14 交易代理服务处理请求。
  2.15 标的特性服务处理请求。
  2.16 存管系统处理请求。
  2.17 交易中心处理请求。
  2.18 交易代理服务处理请求。
  2.19 标的特性服务处理请求。
  2.20 存管系统处理请求。
  2.21 交易中心处理请求。
  2.22 交易代理服务处理请求。
  2.23 标的特性服务处理请求。
  2.24 存管系统处理请求。
  2.25 交易中心处理请求。
  2.26 交易代理服务处理请求。
  2.27 标的特性服务处理请求。
  2.28 存管系统处理请求。
  2.29 交易中心处理请求。
  2.30 交易代理服务处理请求。
  2.31 标的特性服务处理请求。
  2.32 存管系统处理请求。
  2.33 交易中心处理请求。
  2.34 交易代理服务处理请求。
  2.35 标的特性服务处理请求。
  2.36 存管系统处理请求。
  2.37 交易中心处理请求。
  2.38 交易代理服务处理请求。
  2.39 标的特性服务处理请求。
  2.40 存管系统处理请求。
  2.41 交易中心处理请求。
  2.42 交易代理服务处理请求。
  2.43 标的特性服务处理请求。
  2.44 存管系统处理请求。
  2.45 交易中心处理请求。
  2.46 交易代理服务处理请求。
  2.47 标的特性服务处理请求。
  2.48 存管系统处理请求。
  2.49 交易中心处理请求。
  2.50 交易代理服务处理请求。
  2.51 标的特性服务处理请求。
  2.52 存管系统处理请求。
  2.53 交易中心处理请求。
  2.54 交易代理服务处理请求。
  2.55 标的特性服务处理请求。
  2.56 存管系统处理请求。
  2.57 交易中心处理请求。
  2.58 交易代理服务处理请求。
  2.59 标的特性服务处理请求。
  2.60 存管系统处理请求。
  2.61 交易中心处理请求。
  2.62 交易代理服务处理请求。
  2.63 标的特性服务处理请求。
  2.64 存管系统处理请求。
  2.65 交易中心处理请求。
  2.66 交易代理服务处理请求。
  2.67 标的特性服务处理请求。
  2.68 存管系统处理请求。
  2.69 交易中心处理请求。
