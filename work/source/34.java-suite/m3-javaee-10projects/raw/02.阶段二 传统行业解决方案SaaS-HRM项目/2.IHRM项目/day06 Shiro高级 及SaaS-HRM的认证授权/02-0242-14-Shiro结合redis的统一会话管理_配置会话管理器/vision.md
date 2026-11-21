# 画面线理解：14-Shiro结合redis的统一会话管理：配置会话管理器

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\14-Shiro结合redis的统一会话管理：配置会话管理器_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:42, 02:02, 03:47, 04:38, 04:59, 05:57, 06:46, 07:21, 07:56, 08:30, 09:37, 10:43, 11:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:35:41

1) 这一组画面整体在讲什么（一句话）：
在 Spring Boot 项目中，通过 Shiro 框架实现基于 Redis 的会话管理与权限控制，包括自定义 SessionManager、RedisSessionDAO 和缓存管理器的配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 CustomSessionManager.java 中的 getSessionId 方法，用于从请求头中获取 sessionid，若无则生成新 sessionid。
画面 2：展示 PPT 页面，标题为“4.1.2 与 Spring Security 的对比”，内容对比 Shiro 与 Spring Security 的特性，如 API 简单性、支持的数据源、签名方式和性能。
画面 3：展示 ShiroConfiguration.java 代码，配置 filterMap，设置 "/user/**" 路径需要认证。
画面 4：展示 ShiroConfiguration.java 代码，定义 Redis 的 host 和 port 属性，用于连接 Redis。
画面 5：展示 ShiroConfiguration.java 代码，定义 RedisManager 类，用于操作 Redis。
画面 6：展示 ShiroConfiguration.java 代码，显示 IDE 的类型提示，提示用户可以按 Ctrl+Shift+Enter 来移动光标。
画面 7：展示 ShiroConfiguration.java 代码，定义 RedisSessionDAO，用于操作 Redis 会话。
画面 8：展示 ShiroConfiguration.java 代码，显示 IDE 的类型提示，提示用户可以按 Ctrl+Shift+Enter 来移动光标。
画面 9：展示 ShiroConfiguration.java 代码，定义 CustomSessionManager 并设置其 SessionDAO。
画面 10：展示 ShiroConfiguration.java 代码，定义 RedisCacheManager，用于缓存管理。
画面 11：展示 ShiroConfiguration.java 代码，显示 IDE 的类型提示，提示用户可以按 Ctrl+Shift+Enter 来移动光标。
画面 12：展示 ShiroConfiguration.java 代码，定义 CustomRealm、SecurityManager 和 ShiroFilterFactoryBean，用于权限控制和过滤器配置。
画面 13：展示 ShiroConfiguration.java 代码，显示 Redis 的 host 和 port 属性。
画面 14：展示 ShiroConfiguration.java 代码，定义 RedisCacheManager 并设置其 RedisManager。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
//头信息中具有sessionid
//请求头：Authorization, sessionid
//指定sessionId的获取方式
protected Serializable getSessionId(ServletRequest request, ServletResponse response) {
    //获取请求头Authorization中的值
    String id = WebUtils.toHttp(request).getHeader("Authorization");
    if(StringUtils.isEmpty(id)) {
        //如果没有携带，生成新的sessionid
        return super.getSessionId(request, response);
    } else {
        //返回sessionid;
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_SOURCE, "header");
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID, id);
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_IS_VALID, Boolean.TRUE);
        return id;
    }
}
```

画面 3：
```java
//用过滤器的形式配置请求地址的依赖权限
//filterMap.put("/user/home", ""); //不具有指定的权限，跳转到setUnauthorizedUrl地址
//用过滤器的形式配置请求地址的依赖角色
//filterMap.put("/user/home", "roles[系统管理员]");
filterMap.put("/user/**", "authc"); //当前请求地址必须认证之后可以访问
filterFactory.setFilterChainDefinitionMap(filterMap);
return filterFactory;
```

画面 4：
```java
@Value("${spring.redis.host}")
private String host;
@Value("${spring.redis.port}")
private String port;
```

画面 5：
```java
public RedisManager redisManager() {
    RedisManager redisManager = new RedisManager();
    redisManager.setHost(host);
    redisManager.setPort(port);
    return redisManager;
}
```

画面 7：
```java
public RedisSessionDAO redisSessionDAO() {
    RedisSessionDAO sessionDAO = new RedisSessionDAO();
    sessionDAO.setRedisManager(redisManager());
    return sessionDAO;
}
```

画面 9：
```java
public DefaultWebSessionManager sessionManager() {
    CustomSessionManager sessionManager = new CustomSessionManager();
    sessionManager.setSessionDAO(redisSessionDAO());
    return sessionManager;
}
```

画面 10：
```java
public RedisCacheManager cacheManager() {
    RedisCacheManager redisCacheManager = new RedisCacheManager();
    redisCacheManager.setRedisManager(redisManager());
    return redisCacheManager;
}
```

画面 12：
```java
//1.创建过滤器工厂
public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) {
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    filterFactory.setSecurityManager(securityManager);
    return filterFactory;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2：
标题：4.1.2 与 Spring Security 的对比
内容：
- Shiro较之 Spring Security，Shiro在保持强大功能的同时，还在简单性和灵活性方面拥有巨大优势。
  1. 简于理解的 Java Security API；
  2. 支持多种数据源（LDAP，JDBC，Kerberos，ActiveDirectory等）；
  3. 对角色的简单的签名（访问控制），支持多种度的签名；
  4. 支持一级缓存，以提升应用的性能。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
