# 13-基于JWT的API权限校验：测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\13-基于JWT的API权限校验：测试_【海量资源尽在 ubkz.com】.mp4
- 时长 5分22秒（音频 322s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] OK我们的代码呢都已经写好了那接下来呢我们就可以做一个简单的测试看一下当前这个API的权限能不能控制住那做这个测试呢其实很简单很简单我先呢把我这个服务呢给它重新启动一下CIS Term Application当然这边我需要跟各位说一下就是这边呢有一个小的问题是这样的那不管是你没登录还是你这边没有经过授权
[00:32] 我抛出的错误呢都是一个未登录的这么一个错误那我这边呢先对它做一个简单的处理吧先做一个处理就是说呢如果没有包含的话我来一个else好了我这边呢抛出一个异常那这个异常呢为了让它显得更明确一点呢我就叫权限不足了就是说你如果没有匹配的那就权限不足好了把这个异常呢搞得更加明确一些啊
[00:59] 好了这边呢再去进行一个启动这边我不管了让他去重启好了那接下来的事情呢我们可以打开我们的页面去看一下这个授权究竟好不好使OK我这边呢打开我的浏览器是登录方法那登录方法呢我先去看一下你第二个这个02呢就是我们的企业管理员点击进去
[01:22] 那在企业管理员里面呢这边有一个全线设置那对这个前线设置呢我再啰嗦两句员工管理里面有这么三个按钮这三个按钮背后每一个按钮是不是都应该要对应的是一个API的一个方法那我们来看一下这个用户删除的按钮它对应的API看一下就叫做API user delete就叫做API user delete那这个API user delete我们刚才已经把它配置到了user Controller里面的删除按钮上边删除API上面一模一样
[01:53] 那这个呢我们看过了之后那接下来那我这边呢如果说到某一个角色赋予了这个按钮的权限那这个API它就能够访问这个都能理解吧那接下来呢我们来看角色那角色的配权限的时候我们有一个员工管理人事经理他有一个员工管理那员工管理里面好了我把这个用户删除去掉那用户删除去掉的话那这个删除的API它能访问吗那不能访问了对不对那并且页面上按钮是不是也不能出来啊
[02:22] 也不能显示没错吧那接下来呢我们这边点击确定分配了那我们的员工呢其中有一个叫做ZBZ他呢就是03这个03呢他恰巧就是一个我们叫做人事经理他不能删好了那接下来在这边呢我去添加一个员工啊就是为了方便一会删除咱们做测试这边呢就代码写的稍微快一点了为了做测试嘛OK那好了接着我这边退出那退出登录我们用03进行登录
[02:55] 03进登录那03登录进来之后呢这边有他的员工那这边有他的员工那我这边呢已经做过了一个处理我把之前那个微缸if给他去掉了微缸if等于好了我们来了一个我们之前不是写了一个瘦某某某吗我把这个回退再显示回来就是这个微缸if瘦某某好了那这边呢把这个注释把这个呢if判断在天上那他删除就没有了那这边证明了我们页面全现
[03:27] 控制没问题能控制那如果说不小心啊你就搞了这么一个问题就是说呢你不小心前面这玩意儿啊你忘写了忘写这个衣服的判断就跟我一样那接下来呢你这个API你这个按钮就暴露出来了那暴露出来之后那我们能不能访问后台呢那显然不能因为你没有权限没有按钮的权限只不过我前端操作错了但是我后端还有防御性的措施啊我一点是不是应该告诉我权限不足啊
[03:57] 那我们一起来试一下删除走是不是权限不足那这样一来我们是不是已经就控制住了那现在权限不足的效果已经出来了那接下来呢我在这边啊再去对这个角色做一个权限的划分好了人事经理把这个运行按钮给他绑定上那绑定上了这边再退出来还是我们的03ZPZ走好了首先按钮没问题接着删除TTT好了
[04:31] 操作成功那这样一来我们就已经完成了更加细腻度的一个权限的一个控制就是API层面当然了我们API层面是不是通过我们的一个拦截器的方式统一的来进行处理那我们这个拦截器处理的思路就是通过你的所有权限放到了我们的JWT token数据当中来做的那我们在拦截器里面获取到了你所有token里面的权限可访问权限的API子幅创
[04:57] 那接着根据你request mapping里面的name属性来进行比较这种方式来做的OK那这种方式我们做到了之后但是希望各位要保证你要对哪个API接口进行保护那你就需要写一个name属性并且这个name应该是独一无二的这么一个配置它跟你的按钮是一一绑定上的OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
   * 1.通过Service根据mobile查询用户
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

