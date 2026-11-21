# 画面线理解：day08-16-交易中心保存标的-前后端集成测试1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-7 交易中心保存标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-7 交易中心保存标的信息\day08-16-交易中心保存标的-前后端集成测试1_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:21, 01:56, 03:19, 05:51, 07:09, 08:31, 09:41, 10:14, 11:21, 12:57, 14:24, 15:40, 16:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:54:32

1) 这一组画面整体在讲如何在用户登录后，通过 API 获取当前用户信息，并在业务逻辑中使用该信息进行风控校验和项目创建。

2) 按时间顺序列出每张画面的要点：
画面1: 展示文档中“3.2.3 发标业务的先决条件”章节，说明发标前需判断用户是否已开户并获取用户信息。代码片段：`/** 获取当前登录用户 */ @Return RestResponse<ConsumerDTO> getMyConsumer();`
画面2: 展示前端登录页面和浏览器开发者工具的网络请求，请求 URL 为 `http://127.0.0.1:3901/account/m...`，用于获取用户信息。
画面3: 展示文档中关于在 ConsumerController 中实现 getMyConsumer 方法的说明。代码片段：`@Override @ApiOperation("获取登录用户信息") @GetMapping("/my/consumers") public RestResponse<ConsumerDTO> getMyConsumer() { ConsumerDTO consumerDTO = consumerService .getMobile(SecurityUtil.getUser()).getMobile(); return RestResponse.success(consumerDTO); }`
画面4: 展示前端发标页面和浏览器开发者工具的网络请求，请求 URL 为 `http://127.0.0.1:3901/consumer/m...`，用于获取用户信息。
画面5: 展示前端首页和浏览器开发者工具的网络请求，请求 URL 为 `http://127.0.0.1:3901/token`，用于获取用户 token。
画面6: 展示 IDEA 中项目结构，包含多个微服务模块，如 `wanningzp-account-service`、`wanningzp-consumer-service` 等。
画面7: 展示 `ProjectServiceImpl.java` 中 `createProject` 方法的代码，用于创建项目并设置状态。代码片段：`projectDTO.setConsumerId(restResponse.getResult().getId()); projectDTO.setProjectNo(CodeUtil.getNo(CodePrefixCode.CODE_PROJECT_PREFIX)); projectDTO.setStatus(ProjectCode.COLLECTING.getCode());`
画面8: 展示 `ConsumerController.java` 中 `getCurConsumer` 方法的代码，用于获取当前登录用户信息。代码片段：`@Override @ApiOperation("获取登录用户信息") @GetMapping("/my/consumers") public RestResponse<ConsumerDTO> getMyConsumer() { ConsumerDTO consumerDTO = consumerService.getMobile(SecurityUtil.getUser()).getMobile(); return RestResponse.success(consumerDTO); }`
画面9: 展示 `ConsumerController.java` 中 `getCurConsumer` 方法的代码，用于获取当前登录用户信息。代码片段：`@Override @ApiOperation("获取登录用户信息") @GetMapping("/my/consumers") public RestResponse<ConsumerDTO> getMyConsumer() { ConsumerDTO consumerDTO = consumerService.getMobile(SecurityUtil.getUser()).getMobile(); return RestResponse.success(consumerDTO); }`
画面10: 展示 `SecurityUtil.java` 中 `getUser` 方法的代码，用于从请求中获取用户信息。代码片段：`public static LoginUser getUser() { ServletRequestAttributes servletRequestAttributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes(); if (servletRequestAttributes == null) { HttpServletRequest request = servletRequestAttributes.getRequest(); if (jwt instanceof LoginUser) { return (LoginUser) jwt; } } return new LoginUser(); }`
画面11: 展示 `ConsumerController.java` 中 `getMyConsumer` 方法的代码，用于获取当前登录用户信息。代码片段：`@Override @ApiOperation("获取登录用户信息") @GetMapping("/my/consumers") public RestResponse<ConsumerDTO> getMyConsumer() { ConsumerDTO consumerDTO = consumerService.getMobile(SecurityUtil.getUser()).getMobile(); return RestResponse.success(consumerDTO); }`
画面12: 展示 `ConsumerApiAgent.java` 中 `createProject` 方法的代码，用于创建项目。代码片段：`public RestResponse<ConsumerDTO> restResponse = consumerApiAgent.getCurConsumer(SecurityUtil.getSer());`
画面13: 展示 `ConsumerController.java` 中 `getCurConsumer` 方法的代码，用于获取当前登录用户信息。代码片段：`@Override @ApiOperation("获取登录用户信息") @GetMapping("/my/consumers") public RestResponse<ConsumerDTO> getMyConsumer() { ConsumerDTO consumerDTO = consumerService.getMobile(SecurityUtil.getUser()).getMobile(); return RestResponse.success(consumerDTO); }`
画面14: 展示 `ConsumerController.java` 中 `getCurConsumer` 方法的代码，用于获取当前登录用户信息。代码片段：`@Override @ApiOperation("获取登录用户信息") @GetMapping("/my/consumers") public RestResponse<ConsumerDTO> getMyConsumer() { ConsumerDTO consumerDTO = consumerService.getMobile(SecurityUtil.getUser()).getMobile(); return RestResponse.success(consumerDTO); }`

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1: `/** 获取当前登录用户 */ @Return RestResponse<ConsumerDTO> getMyConsumer();`
画面3: `@Override @ApiOperation("获取登录用户信息") @GetMapping("/my/consumers") public RestResponse<ConsumerDTO> getMyConsumer() { ConsumerDTO consumerDTO = consumerService .getMobile(SecurityUtil.getUser()).getMobile(); return RestResponse.success(consumerDTO); }`
画面7: `projectDTO.setConsumerId(restResponse.getResult().getId()); projectDTO.setProjectNo(CodeUtil.getNo(CodePrefixCode.CODE_PROJECT_PREFIX)); projectDTO.setStatus(ProjectCode.COLLECTING.getCode());`
画面10: `public static LoginUser getUser() { ServletRequestAttributes servletRequestAttributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes(); if (servletRequestAttributes == null) { HttpServletRequest request = servletRequestAttributes.getRequest(); if (jwt instanceof LoginUser) { return (LoginUser) jwt; } } return new LoginUser(); }`
画面11: `@Override @ApiOperation("获取登录用户信息") @GetMapping("/my/consumers") public RestResponse<ConsumerDTO> getMyConsumer() { ConsumerDTO consumerDTO = consumerService.getMobile(SecurityUtil.getUser()).getMobile(); return RestResponse.success(consumerDTO); }`
画面12: `public RestResponse<ConsumerDTO> restResponse = consumerApiAgent.getCurConsumer(SecurityUtil.getSer());`
画面13: `@Override @ApiOperation("获取登录用户信息") @GetMapping("/my/consumers") public RestResponse<ConsumerDTO> getMyConsumer() { ConsumerDTO consumerDTO = consumerService.getMobile(SecurityUtil.getUser()).getMobile(); return RestResponse.success(consumerDTO); }`
画面14: `@Override @ApiOperation("获取登录用户信息") @GetMapping("/my/consumers") public RestResponse<ConsumerDTO> getMyConsumer() { ConsumerDTO consumerDTO = consumerService.getMobile(SecurityUtil.getUser()).getMobile(); return RestResponse.success(consumerDTO); }`

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
