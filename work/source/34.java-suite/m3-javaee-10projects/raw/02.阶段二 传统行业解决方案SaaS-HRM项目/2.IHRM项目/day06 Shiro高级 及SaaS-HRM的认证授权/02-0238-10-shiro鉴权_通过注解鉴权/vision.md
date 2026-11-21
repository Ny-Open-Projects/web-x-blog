# 画面线理解：10-shiro鉴权：通过注解鉴权

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\10-shiro鉴权：通过注解鉴权_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:37, 00:55, 01:24, 01:47, 02:18, 02:44, 03:26, 03:46, 03:53, 04:14, 04:41, 05:01, 05:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:33:24

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Shiro 框架实现基于注解的权限控制，包括配置 FilterChain、使用 @RequiresPermissions 和 @RequiresRoles 注解，并处理异常。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 ShiroConfiguration.java 文件中配置 FilterChain 的代码。
- 代码内容：
  ```java
  Map(String,String) filterMap = new LinkedHashMap<>();
  //具有某中权限才能访问
  //用过滤器的形式配置请求地址的依赖权限
  //filterMap.put("/user/home","anon");//当前请求可以匿名访问
  //用过滤器的形式配置请求地址的依赖角色
  //filterMap.put("/user/home","perms:user-home");//不具指定的权限，跳转到setUnauthorizedUrl地址
  //用过滤器的形式配置请求地址的依赖角色
  //filterMap.put("/user/home","roles:系统管理员");
  filterMap.put("/user/**","authc");//当请求地址必须认证之后才可以访问
  filterFactory.setFilterChainDefinitionMap(filterMap);
  return filterFactory;
  ```
- 后续代码：
  ```java
  //开启对shiro注解的支持
  @Bean
  public AuthorizationAttributeSourceAdvisor authorizationAttributeSourceAdvisor(SecurityManager securityManager) {
      AuthorizationAttributeSourceAdvisor advisor = new AuthorizationAttributeSourceAdvisor();
      advisor.setSecurityManager(securityManager);
      return advisor;
  }
  ```

画面 2：
- 展示 UserController.java 文件，其中包含三个 HTTP 请求方法：home、add、find。
- 方法注解：
  ```java
  @RequestMapping(value = "/user/home")
  public String home() {
      return "访问个人主页成功";
  }

  @RequestMapping(value = "/user", method = RequestMethod.POST)
  public String add() {
      return "添加用户成功";
  }

  @RequestMapping(value = "/user", method = RequestMethod.GET)
  public String find() {
      return "查询用户成功";
  }
  ```

画面 3：
- 在 UserController.java 中，光标位于第 27 行，准备添加 Shiro 注解。
- 展示了 IDE 的自动补全建议，包括 @RequiresPermissions、@RequiresRoles 等注解。

画面 4：
- 在 UserController.java 中，第 27 行添加了注解：
  ```java
  @RequiresPermissions()
  ```
- 注释说明：访问此方法必须具备的权限。

画面 5：
- 在 UserController.java 中，第 27 行添加了注解：
  ```java
  @RequiresPermissions("user-home")
  ```
- 注释说明：访问此方法必须具备的权限。

画面 6：
- 在 UserController.java 中，第 27 行添加了注解：
  ```java
  @RequiresPermissions("user-home")
  ```
- 注释说明：访问此方法必须具备的权限。
- 方法注解：
  ```java
  @RequestMapping(value = "/user/home")
  public String home() {
      return "访问个人主页成功";
  }
  ```

画面 7：
- 展示项目结构，包括 src/main/java、src/main/resources 等目录。
- 展示 application.yml 文件。

画面 8：
- 展示项目启动时的控制台日志，显示 Shiro 的 FilterChain 初始化过程。
- 日志内容：
  ```
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.CharacterEncodingFilter.doFilterInternal(CharacterEncodingFilter.java:197)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HiddenHttpMethodFilter.doFilterInternal(HiddenHttpMethodFilter.java:77)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.RequestContextFilter.doFilterInternal(RequestContextFilter.java:99)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePer
