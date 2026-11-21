# 画面线理解：08-Shiro与Springboot整合：测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\08-Shiro与Springboot整合：测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:18, 00:28, 00:43, 01:20, 01:26, 01:44, 02:13, 02:56, 03:02, 03:19, 03:47, 04:25, 04:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:31:43

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 Shiro 进行权限控制，包括配置 Shiro 过滤器、自定义 Realm、使用 Postman 测试接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 IntelliJ IDEA 中项目结构，选中 ShiroApplication.java，代码中包含 @SpringBootApplication(scanBasePackages = "cn.itcast.shiro") 和 @EntityScan("cn.itcast.shiro.domain") 注解。
画面 2: Windows 开始菜单界面，显示了 IntelliJ IDEA、Visual Studio Code、Postman 等应用程序图标。
画面 3: Postman 启动界面，显示“Opening control valves to antimatter nacelles...”的加载动画。
画面 4: IntelliJ IDEA 中 ShiroConfiguration.java 文件，代码中定义了 ShiroFilterFactoryBean，设置了登录页、未授权页和过滤器链。
画面 5: Postman 界面弹出更新提示，显示当前版本为 6.5.3，包含安全修复和新功能。
画面 6: Postman 中新建请求，方法为 GET，URL 为 localhost:8081/user/home。
画面 7: Postman 中 URL 改为 localhost:8081/user。
画面 8: IntelliJ IDEA 中 ShiroConfiguration.java 文件，代码中定义了 AuthorizationAttributeSourceAdvisor，用于支持注解式权限控制。
画面 9: Windows 桌面，显示“黑马程序员”和“博学谷”的标志。
画面 10: SQLyog Ultimate 数据库管理工具界面，处于空状态。
画面 11: SQLyog 中连接到本地数据库，显示了 shiro_db 数据库的表结构和数据。
画面 12: IntelliJ IDEA 中 CustomRealm.java 文件，代码中实现了用户名密码验证逻辑，使用了 MD5 加密。
画面 13: IntelliJ IDEA 中 ShiroApplication.java 文件，控制台输出了 Spring Boot 启动日志，包括 Hibernate 查询语句。
画面 14: Postman 中发送 POST 请求到 localhost:8081/user，请求体中包含用户名和密码，响应状态为 200 OK。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package cn.itcast.shiro;
import ...
@SpringBootApplication(scanBasePackages = "cn.itcast.shiro")
@EntityScan("cn.itcast.shiro.domain")
public class ShiroApplication {
    public static void main(String[] args) {
        SpringApplication.run(ShiroApplication.class, args);
    }
    @Bean
    public OpenEntityManagerInViewFilter openEntityManagerInViewFilter() { return new OpenEntityManagerInViewFilter(); }
}
```

画面 4:
```java
// 设置 shiro 的过滤器
public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) {
    // 1. 创建过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    // 2. 设置安全管理器
    filterFactory.setSecurityManager(securityManager);
    // 3. 通用配置（跳转登录页，为授权跳转的页面）
    filterFactory.setLoginUrl("/autherror?code=1"); // 跳转到登录页
    filterFactory.setUnauthorizedUrl("/autherror?code=2"); // 未授权的url
    // 4. 设置过滤器集合
    // 设置所有的过滤器，有顺序map
    // key = 拦截的url地址
    // value = 一个过滤器
    Map<String, String> filterMap = new LinkedHashMap<>();
    filterMap.put("/user/home", "anon"); // 当前请求地址可以匿名访问
    filterMap.put("/user/**", "authc"); // 当前请求地址必须认证之后才可以访问
    filterFactory.setFilterChainDefinitionMap(filterMap);
    return filterFactory;
}
```

画面 8:
```java
// 开启对shiro注解的支持
@Bean
public AuthorizationAttributeSourceAdvisor authorizationAttributeSourceAdvisor(SecurityManager securityManager) {
    AuthorizationAttributeSourceAdvisor advisor = new AuthorizationAttributeSourceAdvisor();
    advisor.setSecurityManager(securityManager);
    return advisor;
}
```

画面 12:
```java
UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
String username = upToken.getUsername();
String password = new String(upToken.getPassword());
// 1. 列表用户表中是否存在该用户名
User user = userService.findByName(username);
// 2. 判断密码是否正确
if (user != null && user.getPassword().equals(password)) {
    // 3. 如果，验证成功，返回认证信息，realm
    SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(user, user.getPassword(), this.getName());
    return info;
}
// 4. 不一致，返回null（抛出异常）
return null;
```

画面 12 (控制台输出):
```
2018-12-02 20:48:34,023 INFO 10344 --- [nio-8081-exec-1] c.i.c.s.shiro.ShiroApplication : Started ShiroApplication in 7.911 seconds (JVM running for 12.251)
2018-12-02 20:48:34,023 INFO 10344 --- [nio-8081-exec-1] o.s.w.s.DispatcherServlet : FrameworkServlet 'dispatcherServlet': initialization completed
2018-12-02 20:48:34,023 INFO 10344 --- [nio-8081-exec-1] o.s.w.s.DispatcherServlet : FrameworkServlet 'dispatcherServlet': initialization completed
Hibernate: select user_0_.user_id as user_id1_0_, user_0_.user_name as user_nam2_0_, user_0_.password as password3_0_, user_0_.role_id as role_id4_0_, user_0_.permission_id as permission_id5_0_ from user user_0_ where user_0_.user_name = ?
Hibernate: select role_0_.role_id as role_id1_0_, role_0_.role_name as role_nam2_0_, role_0_.permission_id as permission_id3_0_ from role role_0_ where role_0_.role_id = ?
Hibernate: select permission_0_.permission_id as permission_id1_0_, permission_0_.permission_name as permission_name2_0_ from permission permission_0_ where permission_0_.permission_id = ?
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
