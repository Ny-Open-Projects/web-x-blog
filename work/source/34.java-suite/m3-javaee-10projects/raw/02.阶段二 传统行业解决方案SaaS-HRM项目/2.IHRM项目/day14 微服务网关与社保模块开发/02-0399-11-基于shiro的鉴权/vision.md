# 画面线理解：11-基于shiro的鉴权

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\11-基于shiro的鉴权_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:27, 01:45, 02:31, 03:43, 04:10, 04:26, 04:55, 05:14, 05:42, 06:16, 07:08, 07:25, 08:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:17:14

1) 这一组画面整体在讲如何在Zuul网关中集成Shiro进行统一鉴权，包括JWT令牌处理、Shiro配置、Redis会话管理及应用启动流程。

2) 按时间顺序列出每张画面的要点：
画面1：展示Zuul网关中从请求头获取token的Java代码片段，以及Shiro统一鉴权章节标题。
画面2：绘制了JWT鉴权流程图，展示“调用端”向“zuul网关”发送token，网关将token传递给“系统微服务”和“企业微服务”。
画面3：在流程图中增加“redis服务器”节点，表示“系统微服务”和“企业微服务”将用户数据存放在Redis服务器。
画面4：在流程图中修改“系统微服务”和“企业微服务”向“zuul网关”传递的token内容，改为“自定义的sessionid”。
画面5：展示IntelliJ IDEA中Shiro配置文件的目录结构，以及LoginFilter.java文件中的部分代码。
画面6：展示ShiroConfiguration.java文件中创建Realm和SecurityManager的代码。
画面7：展示ShiroConfiguration.java文件中配置Shiro过滤器工厂的代码，包括设置登录URL、未授权URL和过滤器映射。
画面8：展示ShiroConfiguration.java文件中配置RedisManager、RedisSessionDAO和CustomSessionManager的代码。
画面9：展示ShiroConfiguration.java文件中配置Shiro过滤器工厂的代码，包括设置登录URL、未授权URL和过滤器映射。
画面10：展示ShiroConfiguration.java文件中配置RedisCacheManager的代码。
画面11：展示IntelliJ IDEA中项目结构，包含多个模块如ihrm_common、ihrm_company等。
画面12：展示GateApplication.java文件中的SpringBoot启动类代码，以及控制台日志显示应用启动成功。
画面13：展示GateApplication.java文件中的SpringBoot启动类代码。
画面14：展示GateApplication.java文件中的SpringBoot启动类代码，以及控制台日志显示应用启动成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
// 2) 从上下文中获取request对象
HttpServletRequest req = ctx.getRequest();
// 3) 从请求中获取token
String token = req.getHeader("Authorization");
// 4) 判断
if(token == null || "".equals(token.trim())){
    // 没有token，登录校验失败，拦截
    ctx.setSendZuulResponse(false);
    // 返回401状态码，也可以考虑重定向到登录页面
    ctx.setResponseStatusCode(HttpStatus.UNAUTHORIZED.value());
}
// 校验通过，可以将用户信息放入上下文，继续向后执行
return null;
```

画面6：
```java
@Configuration
public class ShiroConfiguration {
    //1.创建realm
    @Bean
    public IRealm getRealm() {
        return new IRealm();
    }
    //2.创建安全管理器
    @Bean
    public SecurityManager getSecurityManager(IRealm realm) {
        DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager();
        securityManager.setRealm(realm);
        //自定义的会话管理器注册到安全管理器中
        securityManager.setSessionManager(sessionManager());
        //自定义的缓存管理器注册到安全管理器中
        securityManager.setCacheManager(cacheManager());
        return securityManager;
    }
}
```

画面7：
```java
//3.配置shiro的过滤器工厂
@Bean
public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) {
    //1.创建过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    //2.设置安全管理器
    filterFactory.setSecurityManager(securityManager);
    //3.设置登录URL，未授权URL
    filterFactory.setLoginUrl("/autherror/code=1"); //登录url
    filterFactory.setUnauthorizedUrl("/autherror/code=2"); //未授权的url
    //4.设置过滤器映射
    Map<String,String> filterMap = new LinkedHashMap<>();
    filterMap.put("/sys/login", "anon");
    filterMap.put("/autherror", "anon");
    //5.设置过滤器链定义
    filterFactory.setFilterChainDefinitionMap(filterMap);
    return filterFactory;
}
```

画面8：
```java
public RedisManager redisManager() {
    RedisManager redisManager = new RedisManager();
    redisManager.setHost("localhost");
    redisManager.setPort(6379);
    return redisManager;
}
public RedisSessionDAO redisSessionDAO() {
    RedisSessionDAO sessionDAO = new RedisSessionDAO();
    sessionDAO.setRedisManager(redisManager());
    return sessionDAO;
}
public DefaultWebSessionManager sessionManager() {
    CustomSessionManager sessionManager = new CustomSessionManager();
    //sessionManager.setSessionIdCookieEnabled(false);
    sessionManager.setSessionIdRewritingEnabled(false);
    sessionManager.setSessionDAO(redisSessionDAO());
    return sessionManager;
}
```

画面10：
```java
public RedisCacheManager cacheManager() {
    RedisCacheManager redisCacheManager = new RedisCacheManager();
    redisCacheManager.setRedisManager(redisManager());
    return redisCacheManager;
}
```

画面12：
```java
package com.ihrm.gate;
@SpringBootApplication(scanBasePackages = "com.ihrm")
//开启zuul网关功能
@EnableZuulProxy
//开启服务发现功能
@EnableDiscoveryClient
public class GateApplication {
    public static void main(String[] args) {
        SpringApplication.run(GateApplication.class);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2：
- 标题：JWT的鉴权
- 结构：调用端 → zuul网关 → 系统微服务（token）；调用端 → zuul网关 → 企业微服务（token）
画面3：
- 结构：系统微服务 → 存放 → redis服务器（用户数据）；企业微服务 → 存放 → redis服务器（用户数据）
画面4：
- 结构：系统微服务 → 传递 → zuul网关（自定义的sessionid）；企业微服务 → 传递 → zuul网关（自定义的sessionid）

5) 不要评价画面美观，不要输出与课程无关的内容。
