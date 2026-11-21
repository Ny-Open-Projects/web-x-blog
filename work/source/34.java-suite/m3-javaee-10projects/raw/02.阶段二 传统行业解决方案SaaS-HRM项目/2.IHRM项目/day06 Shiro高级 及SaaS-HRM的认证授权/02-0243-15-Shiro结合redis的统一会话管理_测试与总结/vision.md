# 画面线理解：15-Shiro结合redis的统一会话管理：测试与总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\15-Shiro结合redis的统一会话管理：测试与总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:42, 00:59, 01:38, 01:58, 02:30, 02:39, 03:19, 03:35, 04:03, 04:45, 05:16, 05:40, 06:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:36:31

1) 这一组画面整体在讲什么（一句话）：
演示基于 Shiro 框架的用户认证流程，包括自定义 Realm、用户实体类、登录控制器、Session 管理及前后端交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 Shiro 认证流程图，包括拦截器、CustomRealm、Subject、数据库等组件及其交互关系。
画面 2：展示 User 实体类代码，定义了用户表结构和角色关联。
画面 3：展示 User 实体类代码，添加了 AuthCachePrincipal 实现和 getAuthCacheKey 方法。
画面 4：展示 CustomRealm.java 中的 doGetAuthenticationInfo 方法，用于获取用户凭证并验证。
画面 5：展示 UserController.java 中的 login 方法，处理用户登录请求并调用 Subject.login。
画面 6：展示 Subject 类的 API 文档，说明其用于操作用户认证信息。
画面 7：展示 Subject 类的 API 文档，说明其用于操作用户会话。
画面 8：展示 UserController.java 中的 login 方法，调用 subject.login 进行登录。
画面 9：展示 Postman 中的登录请求，设置 Authorization 头。
画面 10：展示浏览器中登录页面，输入用户名和密码。
画面 11：展示浏览器中登录成功后的页面，显示 session ID。
画面 12：展示 IDEA 控制台日志，显示 Shiro 启动和数据库查询日志。
画面 13：展示 Postman 中的登录请求，设置 Authorization 头。
画面 14：展示 PPT 页面，介绍 Shiro 的 SessionManager 和 show 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
/**
 * 用户实体类
 */
@Entity
@Table(name = "pe_user")
@Getter
@Setter
public class User implements Serializable {
    private static final long serialVersionUID = 4297464181093870382L;
    // ID
    @Id
    private String id;
    private String username;
    private String password;
    @ManyToMany(fetch = FetchType.EAGER)
    @JoinTable(name="pe_user_role", joinColumns={@JoinColumn(name="user_id", referencedColumnName="id")},
    inverseJoinColumns={@JoinColumn(name="role_id", referencedColumnName="id")})
    private Set<Role> roles = new HashSet<>();//用户与角色  多对多
}
```

画面 3：
```java
/**
 * 用户实体类
 */
@Entity
@Table(name = "pe_user")
@Getter
@Setter
public class User implements Serializable, AuthCachePrincipal {
    private static final long serialVersionUID = 4297464181093870382L;
    // ID
    @Id
    private String id;
    private String username;
    private String password;
    @ManyToMany(fetch = FetchType.EAGER)
    @JoinTable(name="pe_user_role", joinColumns={@JoinColumn(name="user_id", referencedColumnName="id")},
    inverseJoinColumns={@JoinColumn(name="role_id", referencedColumnName="id")})
    private Set<Role> roles = new HashSet<>();//用户与角色  多对多
    @Override
    public String getAuthCacheKey() {
        return null;
    }
}
```

画面 4：
```java
protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) {
    UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
    String username = upToken.getUsername();
    String password = new String(upToken.getPassword());
    //2.根据用户名查询数据库
    User user = userService.findByName(username);
    //3.判断用户是否存在且密码是否一致
    if(user == null && user.getPassword().equals(password)) {
        //如果一致，返回用户信息
        SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(user, user.getPassword(), getName());
        return info;
    }
    //4.不一致，返回null（抛出异常）
    return null;
}
```

画面 5：
```java
//用户登录
@RequestMapping(value="/login")
public String login(String username, String password) {
    try {
        password = new Md5Hash(password, username, hashIterations: 3).toString();
        //1.获得subject
        Subject subject = SecurityUtils.getSubject();
        //2.用subject进行登录
        subject.login(upToken);
        return "登录成功";
    } catch (Exception e) {
        e.printStackTrace();
        return "用户名或密码错误";
    }
}
//登录成功后，打印所有session内容
@RequestMapping(value="/show")
public String show(HttpSession session) {
    Enumeration<?> enumeration = session.getAttributeNames();
    while (enumeration.hasMoreElements()) {
        //...
    }
}
```

画面 6：
```java
//使用subject进行登录
subject.login(upToken);
return "登录成功";
```

画面 7：
```java
//使用subject进行登录
subject.login(upToken);
return "登录成功";
```

画面 8：
```java
//用户登录
@RequestMapping(value="/login")
public String login(String username, String password) {
    try {
        password = new Md5Hash(password, username, hashIterations: 3).toString();
        //1.获得subject
        Subject subject = SecurityUtils.getSubject();
        //2.用subject进行登录
        subject.login(upToken);
        return "登录成功";
    } catch (Exception e) {
        e.printStackTrace();
        return "用户名或密码错误";
    }
}
//登录成功后，打印所有session内容
@RequestMapping(value="/show")
public String show(HttpSession session) {
    Enumeration<?> enumeration = session.getAttributeNames();
    while (enumeration.hasMoreElements()) {
        //...
    }
}
```

画面 12：
```
2018-12-07 21:57:27,258 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.controller.UserController.getUser(Long)
2018-12-07 21:57:27,262 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.controller.UserController.getUser(Long)
2018-12-07 21:57:27,318 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.controller.UserController.getUser(Long)
2018-12-07 21:57:27,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.controller.UserController.getUser(Long)
2018-12-07 21:58:16,087 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.controller.UserController.getUser(Long)
2018-12-07 21:58:16,676 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.controller.UserController.getUser(Long)
2018-12-07 21:58:16,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.controller.UserController.getUser(Long)
2018-12-07 21:58:16,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.controller.UserController.getUser(Long)
2018-12-07 21:58:16,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.controller.UserController.getUser(Long)
2018-12-07 21:58:16,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.controller.UserController.getUser(Long)
2018-12-07 21:58:16,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.controller.UserController.getUser(Long)
2018-12-07 21:58:16,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.controller.UserController.getUser(Long)
2018-12-07 21:
