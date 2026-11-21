# 画面线理解：20-SasSHRM中基于shiro的认证授权：自定义realm-授权

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\20-SasSHRM中基于shiro的认证授权：自定义realm-授权_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:07, 00:54, 00:56, 01:05, 01:14, 01:30, 01:55, 01:59, 02:16, 02:26, 02:43, 02:57, 03:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:40:13

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Shiro 框架中实现用户认证与授权，通过自定义 Realm 类获取用户信息、权限和角色，并将其封装为 AuthenticationInfo 和 AuthorizationInfo 返回。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 UserRealm.java 文件中 doGetAuthenticationInfo 方法的实现，用于处理用户登录认证。
- 代码逻辑：根据手机号查找用户，校验密码，若用户存在且密码匹配，则构造 SimpleAuthenticationInfo 并返回；否则返回 null。
- 代码片段：
  ```java
  User user = userService.findByMobile(mobile);
  if(user != null && user.getPassword().equals(password)) {
      ProfileResult result = null;
      if("user".equals(user.getLevel())) {
          result = new ProfileResult(user);
      } else {
          Map map = new HashMap();
          if("coAdmin".equals(user.getLevel())) {
              map.put("envVisible","1");
          }
          List<Permission> list = permissionService.findAll(map);
          result = new ProfileResult(user,list);
      }
      //构造方法，安全数据，密码，realm域名
      SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(result,user.getPassword(),this.getName());
      return info;
  }
  //返回null，会抛出异常，标识用户名和密码不匹配
  return null;
  ```

画面 2：
- 显示 UserRealm.java 文件中 doGetAuthenticationInfo 方法的实现，与画面 1 代码相同，但注释更详细。
- 代码片段：
  ```java
  protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
      UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
      String mobile = upToken.getUsername();
      String password = new String(upToken.getPassword());
      User user = userService.findByMobile(mobile);
      if(user != null && user.getPassword().equals(password)) {
          ProfileResult result = null;
          if("user".equals(user.getLevel())) {
              result = new ProfileResult(user);
          } else {
              Map map = new HashMap();
              if("coAdmin".equals(user.getLevel())) {
                  map.put("envVisible","1");
              }
              List<Permission> list = permissionService.findAll(map);
              result = new ProfileResult(user,list);
          }
          //构造方法，安全数据，密码，realm域名
          SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(result,user.getPassword(),this.getName());
          return info;
      }
      return null;
  }
  ```

画面 3：
- 显示 Postman 工具界面，正在向 http://localhost:8081/user/home 发送 POST 请求。
- Authorization 头部包含 Base64 编码的用户名和密码。
- 状态码为 200 OK，表示请求成功。

画面 4：
- 显示 CustomRealm.java 文件中 doGetAuthenticationInfo 方法的实现，用于处理用户登录认证。
- 代码逻辑：获取用户名和密码，查找用户，校验密码，若匹配则构造 SimpleAuthenticationInfo 并返回；否则返回 null。
- 代码片段：
  ```java
  protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
      UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
      String username = upToken.getUsername();
      String password = new String(upToken.getPassword());
      User user = userService.findByMobile(username);
      if(user != null && user.getPassword().equals(password)) {
          //构造方法，安全数据，密码，realm域名
          SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(user,user.getPassword(),this.getName());
          return info;
      }
      return null;
  }
  ```

画面 5：
- 显示 CustomRealm.java 文件中 doGetAuthorizationInfo 方法的实现，用于处理用户权限认证。
- 代码逻辑：获取用户，构造 SimpleAuthorizationInfo，遍历角色权限并添加到 roles 中，最后返回 info。
- 代码片段：
  ```java
  protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
      User user = (User) principalCollection.getPrimaryPrincipal();
      SimpleAuthorizationInfo info = new SimpleAuthorizationInfo();
      Set<String> roles = new HashSet<>();
      Set<String> perms = new HashSet<>();
      for (Role role : user.getRoles()) {
          roles.add(role.getRoleName());
          for (Permission perm : role.getPermissions()) {
              perms.add(perm.getPerms());
          }
      }
      info.setRoles(roles);
      info.setStringPermissions(perms);
      return info;
  }
  ```

画面 6：
- 显示 IrmRealm.java 文件中 doGetAuthorizationInfo 方法的实现，用于处理用户权限认证。
- 代码逻辑：获取用户，构造 ProfileResult，获取权限信息，返回 null。
- 代码片段：
  ```java
  protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
      ProfileResult result = (ProfileResult)principalCollection.getPrimaryPrincipal();
      //获取权限信息
      return null;
  }
  ```

画面 7：
- 显示 ProfileResult.java 文件中构造方法的实现，用于封装用户信息和权限。
- 代码逻辑：根据用户对象和权限列表，设置用户名、公司、公司ID、菜单和权限。
- 代码片段：
  ```java
  public ProfileResult(User user, List<Permission> list) {
      this.mobile = user.getMobile();
      this.username = user.getUsername();
      this.company = user.getCompanyName();
      this.companyId = user.getCompanyId();
      Set<String> menus = new HashSet<>();
      Set<String> aps = new HashSet<>();
      for (Permission perm : list) {
          String code = perm.getCode();
          if(perm.getPerms() == 1) {
              menus.add(code);
          } else if(perm.getPerms() == 2) {
              aps.add(code);
          } else {
              aps.add(code);
          }
      }
      this.roles.put("menus",menus);
      this.roles.put("aps",aps);
  }
  ```

画面 8：
- 显示 IrmRealm.java 文件中 doGetAuthorizationInfo 方法的实现，用于处理用户权限认证。
- 代码逻辑：获取用户，构造 ProfileResult，获取权限信息，返回 null。
- 代码片段：
  ```java
  protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
      ProfileResult result = (ProfileResult)principalCollection.getPrimaryPrincipal();
      //获取权限信息
      return null;
  }
  ```

画面 9：
- 显示 IrmRealm.java 文件中 doGetAuthorizationInfo 方法的实现，用于处理用户权限认证。
- 代码逻辑：获取用户，构造 ProfileResult，获取权限信息，返回 null。
- 代码片段：
  ```java
  protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
      ProfileResult result = (ProfileResult)principalCollection.getPrimaryPrincipal();
      //获取权限信息
      return null;
  }
  ```

画面 10：
- 显示 UserController.java 文件中 ProfileResult 类的实现，用于封装用户信息和权限。
- 代码逻辑：根据用户对象和权限列表，设置用户名、公司、公司ID、菜单和权限。
- 代码片段：
  ```java
  public ProfileResult(User user, List<Permission> list) {
      this.mobile = user.getMobile();
      this.username = user.getUsername();
      this.company = user.getCompanyName();
      this.companyId = user.getCompanyId();
      Set<String> menus = new HashSet<>();
      Set<String> aps = new HashSet<>();
      for (Permission perm : list) {
          String code = perm.getCode();
          if(perm.getPerms() == 1) {
              menus.add(code);
          } else if(perm.getPerms() == 2) {
              aps.add(code);
          } else {
              aps.add(code);
          }
      }
      this.roles.put("menus",menus);
      this.roles.put("aps",aps);
  }
  ```

画面 11：
- 显示 IrmRealm.java 文件中 doGetAuthorizationInfo 方法的实现，用于处理用户权限认证。
- 代码逻辑：获取用户，构造 ProfileResult，获取权限信息，返回 null。
- 代码片段：
  ```java
  protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
      ProfileResult result = (ProfileResult)principalCollection.getPrimaryPrincipal();
      //获取权限信息
      return null;
  }
  ```

画面 12：
- 显示 IrmRealm.java 文件中 doGetAuthorizationInfo 方法的实现，用于处理用户权限认证。
- 代码逻辑：获取用户，构造 ProfileResult，获取权限信息，返回 null。
- 代码片段：
  ```java
  protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
      ProfileResult result = (ProfileResult)principalCollection.getPrimaryPrincipal();
      //获取权限信息
      return null;
  }
  ```

画面 13：
- 显示 IrmRealm.java 文件中 doGetAuthorizationInfo 方法的实现，用于处理用户权限认证。
- 代码逻辑：获取用户，构造 ProfileResult，获取权限信息，返回 null。
- 代码片段：
  ```java
  protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
      ProfileResult result = (ProfileResult)principalCollection.getPrimaryPrincipal();
      //获取权限信息
      return null;
  }
  ```

画面 14：
- 显示 IrmRealm.java 文件中 doGetAuthorizationInfo 方法的实现，用于处理用户权限认证。
- 代码逻辑：获取用户，构造 ProfileResult
