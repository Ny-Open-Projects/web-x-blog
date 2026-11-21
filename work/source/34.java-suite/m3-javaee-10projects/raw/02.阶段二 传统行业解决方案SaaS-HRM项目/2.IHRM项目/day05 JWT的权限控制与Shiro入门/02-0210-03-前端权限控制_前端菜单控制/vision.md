# 画面线理解：03-前端权限控制：前端菜单控制

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\03-前端权限控制：前端菜单控制_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:43, 01:00, 02:18, 02:55, 03:07, 03:51, 04:59, 05:31, 05:59, 06:43, 07:48, 08:17, 08:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:09:49

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 后端和 Vue 前端的 SAAS 人力资源管理系统（HRM）的开发与运行过程，包括后端权限控制逻辑、前端页面交互及 API 调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- IDE：IntelliJ IDEA，项目路径为 `ihrm_parent`。
- 代码文件：`UserController.java`，展示用户权限校验逻辑。
- 代码片段：
  ```java
  String token = authorization.replace(target: "Bearer ", replacement: "");
  //3.解析Token
  Claims claims = jwttUtils.parseJwt(token);
  String userid = claims.getDid();
  //获取当前用户
  User user = userService.findById(userid);
  ProfileResult result = null;
  if("user".equals(user.getLevel())) {
      result = new ProfileResult(user);
  }else {
      Map map = new HashMap();
      if("admin".equals(user.getLevel())) {
          map.put("envVisible", "1");
      }
      List<Permission> list = permissionService.findAll(map);
      result = new ProfileResult(ResultCode.SUCCESS, result);
  }
  return new Result(ResultCode.SUCCESS, result);
  ```

画面 2：
- IDE：IntelliJ IDEA，项目路径为 `ihrm_parent`。
- 代码文件：`SystemApplication.java`，展示 Spring Boot 启动类。
- 代码片段：
  ```java
  package com.ihrm.system;
  //1.配置springboot包扫描
  @SpringBootApplication(scanBasePackages = "com.ihrm")
  //2.配置jpa注解扫描
  @EntityScan(value = "com.ihrm.domain.system")
  public class SystemApplication {
      //启动方法
      public static void main(String[] args) { SpringApplication.run(SystemApplication.class, args); }
      @Bean
      public IdWorker idWorker() { return new IdWorker(); }
      @Bean
      public JwtUtils jwtUtils() { return new JwtUtils(); }
  }
  ```

画面 3：
- IDE：Visual Studio Code，打开 `user.js` 文件，界面为空白。

画面 4：
- IDE：IntelliJ IDEA，项目路径为 `ihrm_parent`。
- 代码文件：`UserController.java`，展示用户权限校验逻辑。
- 代码片段：
  ```java
  @RequestMapping(value = "/profile", method = RequestMethod.POST)
  public Result profile(HttpRequest request) throws Exception {
      //1.从请求头中获取token，名称-Authorization
      String authorization = request.getHeader("Authorization");
      if(StringUtils.isEmpty(authorization)) {
          throw new CommonException(ResultCode.UNAUTHENTICATED);
      }
      //2.解析Bearer令牌
      String token = authorization.replace(target: "Bearer ", replacement: "");
      Claims claims = jwttUtils.parseJwt(token);
      String userid = claims.getDid();
      //获取用户信息
  }
  ```

画面 5：
- 多窗口界面：Visual Studio Code、IntelliJ IDEA、SQLyog、PDF 文档、API 文档。
- 代码文件：`user.js`，展示登录逻辑。
- 代码片段：
  ```javascript
  LoginByUserName({ commit }, userInfo) {
      return new Promise((resolve, reject) => {
          axios.post('/api/login', userInfo).then(res => {
              commit('SET_TOKEN', res.data.token);
              localStorage.setItem('token', res.data.token);
              resolve();
          }).catch(err => {
              reject(err);
          });
      });
  }
  ```

画面 6：
- 浏览器：访问 `localhost:801`，显示 SAAS-HRM API 文档页面。

画面 7：
- 多窗口界面：Visual Studio Code、IntelliJ IDEA、SQLyog、PDF 文档、API 文档。
- 代码文件：`user.js`，展示登录逻辑。
- 代码片段：
  ```javascript
  LoginByUserName({ commit }, userInfo) {
      return new Promise((resolve, reject) => {
          axios.post('/api/login', userInfo).then(res => {
              commit('SET_TOKEN', res.data.token);
              localStorage.setItem('token', res.data.token);
              resolve();
          }).catch(err => {
              reject(err);
          });
      });
  }
  ```

画面 8：
- 浏览器：访问 `localhost:8011`，显示 SAAS-HRM 登录页面。

画面 9：
- IDE：Visual Studio Code，打开 `login.vue` 文件。
- 代码片段：
  ```vue
  <input type="text" v-model="loginForm.username" autocomplete="off" placeholder="用户名" />
  <input type="password" v-model="loginForm.password" autocomplete="off" placeholder="密码" />
  <div class="login-btn">
      <button @click="handleLogin">登录</button>
  </div>
  ```

画面 10：
- 浏览器：访问 `localhost:8080/#/login`，显示登录页面。
- 网络面板：显示登录请求成功，返回状态码 200。

画面 11：
- 浏览器：访问 `localhost:8080/#/dashboard`，页面空白。

画面 12：
- 浏览器：访问 `localhost:8080/#/dashboard`，页面空白。

画面 13：
- 浏览器：访问 `localhost:8080/#/employees`，显示员工管理页面。

画面 14：
- 浏览器：访问 `localhost:8080/#/employees`，显示员工管理页面，包含工作日历和快速导航。
