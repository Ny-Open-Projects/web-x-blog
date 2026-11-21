# 画面线理解：13-基于JWT的API权限校验：测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\13-基于JWT的API权限校验：测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:38, 00:51, 01:10, 01:28, 01:48, 02:07, 02:36, 02:56, 03:29, 04:00, 04:19, 04:29, 05:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:15:49

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的 HRM 系统中，如何通过自定义拦截器实现用户权限校验，并展示前端界面的权限分配与操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- IDE 界面，显示 `JwtInterceptor.java` 文件内容，正在编辑 JWT 权限校验逻辑。
- 代码片段：
  ```java
  //获取token处理
  String token = authorization.replace(target: "Bearer ", replacement: "");
  //解析token获取claims
  Claims claims = jwtUtils.parseJwt(token);
  if(claims == null) {
  //若claims获取不到当前用户的可访问api权限字符串
  String apis = (String) claims.get(key: "apis"); //api-user-delete,api-user-update
  HandlerMethod h = (HandlerMethod) handler;
  //获取方法上的requestmapping注解
  RequestMapping annotation = h.getMethodAnnotation(RequestMapping.class);
  //判断当前用户是否具有相应的请求权限
  if(apis.contains(name)) {
  request.setAttribute(s: "user_claims",claims);
  return true;
  } else {
  throw new CommonException(ResultCode.UNAUTHENTICATED);
  }
  }
  ```

画面 2：
- IDE 界面，显示 `JwtInterceptor.java` 文件内容，代码逻辑与画面 1 相同，但注释更完整。
- 代码片段：
  ```java
  @Override
  public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
  String authorization = request.getHeader("Authorization");
  //判断请求头中是否为空，是否为Bearer开头
  if(StringUtils.isEmpty(authorization) && authorization.startsWith("Bearer")) {
  //获取token处理
  String token = authorization.replace(target: "Bearer ", replacement: "");
  //解析token获取claims
  Claims claims = jwtUtils.parseJwt(token);
  if(claims == null) {
  //若claims获取不到当前用户的可访问api权限字符串
  String apis = (String) claims.get(key: "apis"); //api-user-delete,api-user-update
  HandlerMethod h = (HandlerMethod) handler;
  //获取方法上的requestmapping注解
  RequestMapping annotation = h.getMethodAnnotation(RequestMapping.class);
  //判断当前用户是否具有相应的请求权限
  String name = annotation.name();
  if(apis.contains(name)) {
  request.setAttribute(s: "user_claims",claims);
  return true;
  } else {
  throw new CommonException(ResultCode.UNAUTHENTICATED);
  }
  }
  }
  ```

画面 3：
- IDE 界面，显示 `JwtInterceptor.java` 文件内容，代码逻辑与画面 2 相同，但注释中 `ResultCode.UNAUTHENTICATED` 被修改为 `ResultCode.UNAUTHORISE`。
- 代码片段：
  ```java
  if(apis.contains(name)) {
  request.setAttribute(s: "user_claims",claims);
  return true;
  } else {
  throw new CommonException(ResultCode.UNAUTHORISE);
  }
  ```

画面 4：
- IDE 界面，显示 `JwtInterceptor.java` 文件内容，代码逻辑与画面 3 相同，但注释中 `ResultCode.UNAUTHORISE` 被修改为 `ResultCode.UNAUTHENTICATED`。
- 代码片段：
  ```java
  if(apis.contains(name)) {
  request.setAttribute(s: "user_claims",claims);
  return true;
  } else {
  throw new CommonException(ResultCode.UNAUTHENTICATED);
  }
  ```

画面 5：
- 浏览器界面，显示 HRM 系统的“权限设置”页面，展示“员工管理”模块下的权限列表。
- 页面内容：
  - 菜单名称：员工管理
  - 权限标识：employees
  - 操作：添加、查看、编辑、删除

画面 6：
- IDE 界面，显示 `UserController.java` 文件内容，展示用户登录和删除功能的代码。
- 代码片段：
  ```java
  @RequestMapping(value = "/user/{id}", method = RequestMethod.DELETE, name = "API-USER-DELETE")
  public Result delete(@PathVariable(value = "id") String id) {
  userService.deleteById(id);
  return new Result(ResultCode.SUCCESS);
  }

  /**
   * 用户登录
   * 1.通过service根据mobile查询用户
   * 2.生成jwt信息
   */
  @RequestMapping(value = "/login", method = RequestMethod.POST)
  public Result login(@RequestMap Map<String, String> loginMap) {
  String mobile = loginMap.get("mobile");
  String password = loginMap.get("password");
  User user = userService.findByMobile(mobile);
  if(user == null || user.getPassword().equals(password)) {
  return new Result(ResultCode.MOBILEORPASSWORDERROR);
  } else {
  //登录成功
  //获取所有角色
  StringBuilder sb = new StringBuilder();
  for (Role role : user.getRoles()) {
  //拼接所有角色的权限字符串
  sb.append(role.getApi());
  }
  //返回token
  return new Result(ResultCode.SUCCESS, sb.toString());
  }
  }
  ```

画面 7：
- 浏览器界面，显示 HRM 系统的“为【人事经理】分配权限”弹窗，展示可分配的权限项。
- 弹窗内容：
  - 勾选项：员工管理、用户新增按钮、用户删除按钮、用户修改按钮
  - 底部按钮：取消、确定

画面 8：
- 浏览器界面，显示 HRM 系统的“员工管理”页面，展示员工列表。
- 页面内容：
  - 员工信息：姓名、手机号、工号、部门
  - 操作：编辑、删除、查看

画面 9：
- 浏览器界面，显示 HRM 系统的“首页”页面，展示工作日历和快捷导航。
- 页面内容：
  - 工作日历：2019 年 11 月
  - 快速开始：人事日报、考勤查询、员工审核、组织架构

画面 10：
- 浏览器界面，显示 HRM 系统的“多窗口切换”页面，展示多个开发和测试工具窗口。
- 页面内容：
  - 窗口列表：Chrome、IDEA、Postman、SQLyog、PPT、流程图等

画面 11：
- 浏览器界面，显示 HRM 系统的“员工管理”页面，展示员工列表。
- 页面内容：
  - 员工信息：姓名、手机号、工号、部门
  - 操作：编辑、删除、查看

画面 12：
- 浏览器界面，显示 HRM 系统的“角色管理”页面，展示角色列表。
- 页面内容：
  - 角色名称：人事经理、管理员、人事专员、招聘专员
  - 操作：分配权限、修改、删除

画面 13：
- 浏览器界面，显示 HRM 系统的“员工管理”页面，展示员工列表。
- 页面内容：
  - 员工信息：姓名、手机号、工号、部门
  - 操作：编辑、删除、查看

画面 14：
- IDE 界面，显示 `UserController.java` 文件内容，展示用户删除功能的代码。
- 代码片段：
  ```java
  @RequestMapping(value = "/user/{id}", method = RequestMethod.DELETE, name = "API-USER-DELETE")
  public Result delete(@PathVariable(value = "id") String id) {
  userService.deleteById(id);
  return new Result(ResultCode.SUCCESS);
  }
  ```
