# 画面线理解：07-Shiro与Springboot整合：配置-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\07-Shiro与Springboot整合：配置-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:02, 02:14, 03:38, 04:32, 05:07, 05:15, 06:05, 06:50, 07:06, 07:17, 07:39, 07:48, 08:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:31:04

1) 这一组画面整体在讲什么（一句话）：
讲解 Shiro 框架中过滤器（Filter）的配置与使用，包括过滤器的类型、配置方式以及如何通过过滤器链实现权限控制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Shiro 过滤器的类型说明，包括 anon、authc、logout、authcBasic、ssl、perms[user]、roles[admin]、rest[user]、port[8081] 等过滤器及其作用。
画面2：展示 Shiro 过滤器的类型说明，包括 anon、authc、logout、authcBasic、ssl、perms[user]、roles[admin]、rest[user]、port[8081] 等过滤器及其作用。
画面3：展示 Shiro 过滤器的类型说明，包括 anon、authc、logout、authcBasic、ssl、perms[user]、roles[admin]、rest[user]、port[8081] 等过滤器及其作用。
画面4：展示 Shiro 过滤器的类型说明，包括 anon、authc、logout、authcBasic、ssl、perms[user]、roles[admin]、rest[user]、port[8081] 等过滤器及其作用。
画面5：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面6：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面7：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面8：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面9：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面10：展示 Windows 桌面，包含“黑马程序员”和“博学谷”的标志。
画面11：在 Notepad++ 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面12：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面13：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面14：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
//配置安全管理器
@Bean
public SecurityManager securityManager(CustomRealm realm) {
    DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm);
    securityManager.setRealm(realm);
    return securityManager;
}

//filter工厂，设置对应的过滤器或默认条件
@Bean
public ShiroFilterFactoryBean shiroFilterSecurityManager() {
    //1.创建shiro过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    //2.设置安全管理员
    filterFactory.setSecurityManager(securityManager);
    //3.通用配置（登录页面，登录成功页面，登录失败页面）
    filterFactory.setLoginUrl("/autherror?code=1");//设置登录页面
    filterFactory.setUnauthorizedUrl("/autherror?code=2");//设置未授权页面
    //4.设置过滤器链
    //设置所有的过滤器，有顺序map
    //key - 拦截的url地址
    //value - 过滤器类型
    //5.设置过滤器
    filterFactory.setFilterChainDefinitionMap(filterMap);
    return filterFactory;
}

//开启对shior注解的支持
@Bean
public AuthorizationAttributeSourceAdvisor authorizationAttributeSourceAdvisor(SecurityManager securityManager) {
    AuthorizationAttributeSourceAdvisor advisor = new AuthorizationAttributeSourceAdvisor();
    advisor.setSecurityManager(securityManager);
    return advisor;
}

画面2：
//配置安全管理器
@Bean
public SecurityManager securityManager(CustomRealm realm) {
    DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm);
    securityManager.setRealm(realm);
    return securityManager;
}

//filter工厂，设置对应的过滤器或默认条件
@Bean
public ShiroFilterFactoryBean shiroFilterSecurityManager() {
    //1.创建shiro过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    //2.设置安全管理员
    filterFactory.setSecurityManager(securityManager);
    //3.通用配置（登录页面，登录成功页面，登录失败页面）
    filterFactory.setLoginUrl("/autherror?code=1");//设置登录页面
    filterFactory.setUnauthorizedUrl("/autherror?code=2");//设置未授权页面
    //4.设置过滤器链
    //设置所有的过滤器，有顺序map
    //key - 拦截的url地址
    //value - 过滤器类型
    //5.设置过滤器
    filterFactory.setFilterChainDefinitionMap(filterMap);
    return filterFactory;
}

//开启对shior注解的支持
@Bean
public AuthorizationAttributeSourceAdvisor authorizationAttributeSourceAdvisor(SecurityManager securityManager) {
    AuthorizationAttributeSourceAdvisor advisor = new AuthorizationAttributeSourceAdvisor();
    advisor.setSecurityManager(securityManager);
    return advisor;
}

画面3：
//配置安全管理器
@Bean
public SecurityManager securityManager(CustomRealm realm) {
    DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm);
    securityManager.setRealm(realm);
    return securityManager;
}

//filter工厂，设置对应的过滤器或默认条件
@Bean
public ShiroFilterFactoryBean shiroFilterSecurityManager() {
    //1.创建shiro过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    //2.设置安全管理员
    filterFactory.setSecurityManager(securityManager);
    //3.通用配置（登录页面，登录成功页面，登录失败页面）
    filterFactory.setLoginUrl("/autherror?code=1");//设置登录页面
    filterFactory.setUnauthorizedUrl("/autherror?code=2");//设置未授权页面
    //4.设置过滤器链
    //设置所有的过滤器，有顺序map
    //key - 拦截的url地址
    //value - 过滤器类型
    //5.设置过滤器
    filterFactory.setFilterChainDefinitionMap(filterMap);
    return filterFactory;
}

//开启对shior注解的支持
@Bean
public AuthorizationAttributeSourceAdvisor authorizationAttributeSourceAdvisor(SecurityManager securityManager) {
    AuthorizationAttributeSourceAdvisor advisor = new AuthorizationAttributeSourceAdvisor();
    advisor.setSecurityManager(securityManager);
    return advisor;
}

画面4：
//配置安全管理器
@Bean
public SecurityManager securityManager(CustomRealm realm) {
    DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm);
    securityManager.setRealm(realm);
    return securityManager;
}

//filter工厂，设置对应的过滤器或默认条件
@Bean
public ShiroFilterFactoryBean shiroFilterSecurityManager() {
    //1.创建shiro过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    //2.设置安全管理员
    filterFactory.setSecurityManager(securityManager);
    //3.通用配置（登录页面，登录成功页面，登录失败页面）
    filterFactory.setLoginUrl("/autherror?code=1");//设置登录页面
    filterFactory.setUnauthorizedUrl("/autherror?code=2");//设置未授权页面
    //4.设置过滤器链
    //设置所有的过滤器，有顺序map
    //key - 拦截的url地址
    //value - 过滤器类型
    //5.设置过滤器
    filterFactory.setFilterChainDefinitionMap(filterMap);
    return filterFactory;
}

//开启对shior注解的支持
@Bean
public AuthorizationAttributeSourceAdvisor authorizationAttributeSourceAdvisor(SecurityManager securityManager) {
    AuthorizationAttributeSourceAdvisor advisor = new AuthorizationAttributeSourceAdvisor();
    advisor.setSecurityManager(securityManager);
    return advisor;
}

画面5：
//配置安全管理器
@Bean
public SecurityManager securityManager(CustomRealm realm) {
    DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm);
    securityManager.setRealm(realm);
    return securityManager;
}

//filter工厂，设置对应的过滤器或默认条件
@Bean
public ShiroFilterFactoryBean shiroFilterSecurityManager() {
    //1.创建shiro过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    //2.设置安全管理员
    filterFactory.setSecurityManager(securityManager);
    //3.通用配置（登录页面，登录成功页面，登录失败页面）
    filterFactory.setLoginUrl("/autherror?code=1");//设置登录页面
    filterFactory
