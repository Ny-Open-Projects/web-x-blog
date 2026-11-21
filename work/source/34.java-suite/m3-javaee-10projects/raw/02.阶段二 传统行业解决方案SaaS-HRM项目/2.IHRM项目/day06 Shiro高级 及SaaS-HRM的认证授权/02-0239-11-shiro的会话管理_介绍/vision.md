# 画面线理解：11-shiro的会话管理：介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\11-shiro的会话管理：介绍_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 00:30, 01:07, 01:21, 02:11, 03:36, 06:09, 06:37, 06:45, 07:03, 07:36, 07:46, 08:47, 09:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:34:03

1) 这一组画面整体在讲什么（一句话）：
演示 Shiro 框架中用户登录认证流程、自定义 Realm 实现、Session 会话管理及前后端交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 UserController.java 中的用户登录方法 @RequestMapping(value="/login")。
- 代码逻辑：获取用户名密码，MD5 加密，创建 UsernamePasswordToken，调用 Subject.login()，返回登录结果。
- 代码片段：
  ```java
  @RequestMapping(value="/login")
  public String login(String username,String password) {
      try {
          password = new Md5Hash(password,username,hashIterations:3).toString();
          UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
          Subject subject = SecurityUtils.getSubject();
          subject.login(upToken);
          return "登录成功";
      }catch (Exception e) {
          e.printStackTrace();
          return "用户名或密码错误";
      }
  }
  ```

画面 2：
- 展示 CustomRealm.java 中的 doGetAuthenticationInfo 方法。
- 代码逻辑：从 token 获取用户名密码，通过 userService 根据用户名查询用户，校验密码，返回 SimpleAuthenticationInfo。
- 代码片段：
  ```java
  protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
      UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
      String username = upToken.getUsername();
      String password = new String(upToken.getPassword());
      User user = userService.findByName(username);
      if(user == null || !user.getPassword().equals(password)) {
          //4.如果一致，安全验证通过
          SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(user,user.getPassword(),this.getName());
          return info;
      }
      return null;
  }
  ```

画面 3：
- 展示 Windows 桌面，桌面上有“黑马程序员”和“博学谷”的标志，以及“ihrm”文件夹图标。

画面 4：
- 展示 Shiro 认证与授权的安全数据流程图。
- 结构：访问 url 地址 → 拦截器 → CustomRealm（授权方法）→ 获取安全数据 → 安全数据。
- Subject（主体）→ login 方法 → CustomRealm（认证方法）→ 验证通过 → 存储安全数据 → 数据库。

画面 5：
- 展示 Shiro 认证与授权的安全数据流程图。
- 结构：访问 url 地址 → 拦截器 → CustomRealm（授权方法）→ 获取安全数据 → 安全数据。
- 用户名/密码 → Subject（主体）→ login 方法 → CustomRealm（认证方法）→ 验证通过 → 存储安全数据 → 数据库。

画面 6：
- 展示 PPT 页面，标题为“2.1 什么是 shiro 的会话管理”。
- 内容：SessionManager（会话管理器）管理 Subject 的 session，由 SecurityManager 管理。
- shiro 提供了三个默认实现：DefaultSessionManager、ServletContainerSessionManager、DefaultWebSessionManager。
- 代码片段：
  ```java
  //登录成功后，打印所有session内容
  @RequestMapping(value="/show")
  ```

画面 7：
- 展示 PPT 页面，标题为“2.1 什么是 shiro 的会话管理”。
- 内容：SessionManager（会话管理器）管理 Subject 的 session，由 SecurityManager 管理。
- shiro 提供了三个默认实现：DefaultSessionManager、ServletContainerSessionManager、DefaultWebSessionManager。
- 代码片段：
  ```java
  public String show(HttpSession session) {
      //获取session中所有的键值
      Enumeration<?> enumeration = session.getAttributeNames();
      //遍历enumeration中的
      while (enumeration.hasMoreElements()) {
          //获取session键值
          String name = enumeration.nextElement().toString();
          //根据键值获取session中的值
          Object value = session.getAttribute(name);
          //打印结果
          System.out.println("<b>"+ name + "</b>" + value + "<br/>");
      }
      return "查看session成功";
  }
  ```

画面 8：
- 展示 PPT 页面，标题为“2.2 应用场景分析”。
- 内容：展示 show 方法的代码。

画面 9：
- 展示 PPT 页面，标题为“2.2 应用场景分析”。
- 内容：展示 show 方法的代码。

画面 10：
- 展示 UserController.java 中的 show 方法和 autherror 方法。
- 代码片段：
  ```java
  @RequestMapping(value="/show")
  public String show(HttpSession session) {
      //获取session中所有的键值
      Enumeration<?> enumeration = session.getAttributeNames();
      //遍历enumeration中的
      while (enumeration.hasMoreElements()) {
          //获取session键值
          String name = enumeration.nextElement().toString();
          //根据键值获取session中的值
          Object value = session.getAttribute(name);
          //打印结果
          System.out.println("<b>"+ name + "</b>" + value + "<br/>");
      }
      return "查看session成功";
  }
  @RequestMapping(value="/autherror")
  public String autherror(int code) {
      return code==1?"未登录":"未授权";
  }
  ```

画面 11：
- 展示项目结构，包含 src、target、pom.xml 等目录。
- 展示 UserController.java 中的 show 方法和 autherror 方法。

画面 12：
- 展示 Postman 工具界面。
- 请求地址：http://localhost:8081/user/home。
- 请求方法：POST。
- 请求体：未设置。
- 历史记录中包含多个登录请求。

画面 13：
- 展示 CustomRealm.java 中的 doGetAuthenticationInfo 方法。
- 日志信息：显示了 Spring Boot 启动时的框架初始化日志，包括 DispatcherServlet、FrameworkServlet、Hibernate 等。

画面 14：
- 展示 PPT 页面，标题为“2. Shiro 中的会话管理”。
- 内容：SessionManager（会话管理器）管理 Subject 的 session，由 SecurityManager 管理。
- shiro 提供了三个默认实现：DefaultSessionManager、ServletContainerSessionManager、DefaultWebSessionManager。
- 代码片段：
  ```java
  //登录成功后，打印所有session内容
  @RequestMapping(value="/show")
  ```
