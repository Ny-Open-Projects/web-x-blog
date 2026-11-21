# 20-SasSHRM中基于shiro的认证授权：自定义realm-授权

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\20-SasSHRM中基于shiro的认证授权：自定义realm-授权_【海量资源尽在 ubkz.com】.mp4
- 时长 3分32秒（音频 213s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了我们已经完成了自定义room这个认证的这个逻辑那除了认证之外呢我们是不是还有一个叫做授权那我们这个授权呢实际就是放到我们这个HRM room当中其实就可以了我们现在关注的是它的授权方法那授权方法我们做的事情呢这回就比较简单了首先第一件事叫做获取安全数据那获取安全数据之后我们开始获取它里面的叫做权限信息
[00:34] 那接下来我们开始构造我们的权限数据就可以了数据好了那接下来我们来看一下如何去做其实构造权限数据就是我们的叫做返回值嘛好了首先第一个获取安全数据安全数据比较简单和我们之前写的这个代码和我们之前写的这个代码呢基本上是差不多的差不多的power simple connection.get or meprimary power simpleok
[01:08] 好那接下来我们这个安全数据叫做什么注意叫做profilresult好了这边呢做一个强制转型OK那这样一来安全数据已经有了那安全数据里面有很多的内容我们可以一起来浏览一下里面有手机号用户名密码等等等等有很多那除了这个还有一个肉丝是一个map集合那这个map集合里面装了三部分内容有按钮的有菜单的以及我们API的那这个API其实就是我们后台访问的接口
[01:38] 那所以我们判断权限我们授权的是不是就对这个API这个接口接口的权限做一个授权的一个过程其实就可以了所以在这边我们重点是拿到里面的APIS就可以好了那接下来呢回到我们这个HRM ROOT好了我们可以通过result打点get rows再打点get从里面拿到APIS那拿到的这个APIS呢
[02:10] 我们可以做一个简单的转型把它转化成注意啊这代码比较多呀我们把它转化成一个stat死菌的这么一个集合即可好了这边就是apsperms等于转型OK好那接下来呢就是说开始构造返回值构造返回值注意我们之前有一个小的技巧simplesmple加上你返回值的类型info等于new
[02:48] Ctrl C拿过来Ctrl VOK好了那接下来呢我们这个InkFour里面可以设置你的所有权限Add 死君Promission 死拿过来好了返回InkFour即可那这样一来我们就可以通过安全数据Result那通过这个Result得到你所有的API权限那得到所有API权限构造好了这个字符串权限信息那接着存到
[03:13] 我们的simple就是authorizationinfo当中那这样一来我们的授权的里面就有了你当前所有能够操作的API权限那接着我们一会儿经过配置进行它的拦截器处理就能对授权进行一个操作了OK那这样一来我整个Zenim Room里面的所有代码就已经都写好了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

