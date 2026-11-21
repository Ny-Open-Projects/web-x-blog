# 画面线理解：06-Shiro与Springboot整合：配置-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\06-Shiro与Springboot整合：配置-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:33, 01:02, 02:11, 03:27, 03:55, 04:44, 05:17, 05:46, 07:30, 09:39, 10:36, 10:55, 11:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:30:13

1) 这一组画面整体在讲什么（一句话）：
在 Spring Boot 项目中，通过自定义 Realm 和配置 Shiro 安全管理器与过滤器工厂，实现用户认证与权限控制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 UserController 中的 login 方法，使用 UsernamePasswordToken 进行登录，调用 Subject.login 方法。
- 代码：`@RequestMapping(value="/login") public String login(String username,String password) { try { UsernamePasswordToken upToken = new UsernamePasswordToken(username,password); Subject subject = SecurityUtils.getSubject(); subject.login(upToken); return "登录成功"; }catch (Exception e) { return "用户密码错误"; } }`

画面 2：
- 展示 Shiro 的核心组件 SecurityManager 的作用，并展示 ShiroConfiguration 类中配置自定义 Realm 的代码。
- 代码：`@Configuration public class ShiroConfiguration { //配置自定义的Realm @Bean public CustomRealm getRealm() { return new CustomRealm(); } }`

画面 3：
- 展示在 IntelliJ IDEA 中创建新类的对话框，准备创建 CustomRealm 类。

画面 4：
- 展示 ShiroConfiguration.java 文件，其中包含注解 @Configuration 和类定义，以及注释“1.创建 realm”、“2.创建安全管理器”、“3.配置 shiro 的过滤器”。

画面 5：
- 展示 CustomRealm.java 文件，定义了继承 AuthorizingRealm 的自定义 Realm 类，包含 setUserName 方法和授权方法 doGetAuthorizationInfo。
- 代码：`public class CustomRealm extends AuthorizingRealm { public void setUserName(String name) { super.setName("customrealm"); } @Autowired private UserService userService; protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) { //授权方法 } }`

画面 6：
- 展示在 ShiroConfiguration.java 中，为 SecurityManager 选择合适的实现类，当前选中 DefaultWebSecurityManager。

画面 7：
- 展示在 ShiroConfiguration.java 中，为 SecurityManager 选择合适的实现类，当前选中 DefaultWebSessionManager。

画面 8：
- 展示 ShiroConfiguration.java 文件，配置了 SecurityManager 和过滤器工厂。
- 代码：`@Configuration public class ShiroConfiguration { //1.创建 realm @Bean public CustomRealm getRealm() { return new CustomRealm(); } //2.创建安全管理器 @Bean public SecurityManager getSecurityManager(CustomRealm realm) { DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm); return securityManager; } }`

画面 9：
- 展示 ShiroConfiguration.java 文件，展示 Spring 的注解列表，如 @Bean、@Configuration、@Component 等。

画面 10：
- 展示 ShiroConfiguration.java 文件，开始配置 Shiro 的过滤器工厂。
- 代码：`@Bean public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) { }`

画面 11：
- 展示 ShiroFilterFactoryBean 的方法列表，如 setSecurityManager、setLoginUrl、setUnauthorizedUrl 等。

画面 12：
- 展示 ShiroConfiguration.java 文件，配置 ShiroFilterFactoryBean 的 SecurityManager、登录 URL 和未授权 URL。
- 代码：`filterFactory.setSecurityManager(securityManager); filterFactory.setLoginUrl("/login"); filterFactory.setUnauthorizedUrl("/unauthorized");`

画面 13：
- 展示 UserController.java 文件，展示 login 方法中使用了 @Value 注解注入的属性，如 subject、retu 等。

画面 14：
- 展示 ShiroConfiguration.java 文件，配置了 ShiroFilterFactoryBean 的 SecurityManager、登录 URL 和未授权 URL。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```java
//用户登录
@RequestMapping(value="/login")
public String login(String username,String password) {
    try {
        UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
        Subject subject = SecurityUtils.getSubject();
        subject.login(upToken);
        return "登录成功";
    }catch (Exception e) {
        return "用户密码错误";
    }
}
```

画面 2：
```java
@Configuration
public class ShiroConfiguration {
    //配置自定义的Realm
    @Bean
    public CustomRealm getRealm() {
        return new CustomRealm();
    }
}
```

画面 4：
```java
@Configuration
public class ShiroConfiguration {
    //1.创建 realm
    //2.创建安全管理器
    //3.配置 shiro 的过滤器
}
```

画面 5：
```java
public class CustomRealm extends AuthorizingRealm {
    public void setUserName(String name) {
        super.setName("customrealm");
    }
    @Autowired
    private UserService userService;
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        //授权方法
    }
}
```

画面 8：
```java
@Configuration
public class ShiroConfiguration {
    //1.创建 realm
    @Bean
    public CustomRealm getRealm() {
        return new CustomRealm();
    }
    //2.创建安全管理器
    @Bean
    public SecurityManager getSecurityManager(CustomRealm realm) {
        DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm);
        return securityManager;
    }
}
```

画面 10：
```java
@Bean
public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) {
}
```

画面 12：
```java
filterFactory.setSecurityManager(securityManager);
filterFactory.setLoginUrl("/login");
filterFactory.setUnauthorizedUrl("/unauthorized");
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2：
- PPT 标题：Shiro 的核心组件 SecurityManager 的作用。
- 内容：SecurityManager 是 Shiro 架构的心脏，用于协调内部的多个组件完成全部认证授权的过程。例如通过调用 realm 完成认证与登录。使用基于 springboot 的配置方式完成 SecurityManager, Realm 的装配。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
