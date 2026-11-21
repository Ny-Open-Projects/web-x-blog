# 画面线理解：day04-21-认证拦截功能环境准备

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-9 实现认证拦截功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-9 实现认证拦截功能\day04-21-认证拦截功能环境准备_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:20, 02:07, 02:48, 03:57, 04:21, 05:18, 06:15, 07:10, 07:45, 08:28, 11:08, 12:56, 14:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:55:06

1) 这一组画面整体在讲什么（一句话）：
讲解基于 Spring Cloud 的微服务架构中，如何通过网关、认证中心和资源服务实现统一的用户认证与权限控制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了微服务架构图，包含接入方（WEB、移动端、第三方接入）、网关、认证服务（UAA）、资源服务（服务1、服务2、服务n）等组件及其交互流程。
画面 2: 在 IDEA 中展示 `pom.xml` 文件，添加了 Spring Cloud Starter Netflix Eureka 和 Spring Boot Starter Data Redis 的依赖。
画面 3: 在 IDEA 中展示 `pom.xml` 文件，添加了 Spring Cloud Starter Security 和 Spring Security JWT 的依赖。
画面 4: 展示了 PPT 页面，内容为“1.4.2 环境准备”，并列出了 `cn.itcast.wanxing2p.gateway.config.ResourceServerConfig`、`cn.itcast.wanxing2p.gateway.config.RestAccessDeniedHandler`、`cn.itcast.wanxing2p.gateway.config.RestAuth2ExceptionEntryPoint` 三个配置类的描述。
画面 5: 展示了 PPT 页面，内容为“如果网关接收到的请求uri符合/consumer/**表达式，该请求将被转发至consumer-service（用户中心）。为了便于权限拦截，我们将服务内部的接口进行了细分，大体分为三类”，并列出了三类接口的访问方式。
画面 6: 展示了 PPT 页面，内容为“小王是黑马程序员的一名学员，（暂时）登录黑马程序员技术论坛，如下图所示：”，并展示了一个登录界面。
画面 7: 在 IDEA 中展示 `ResourceServerConfig.java` 文件，内容为 `@Configuration @EnableResourceServer public class ResourceServerConfig extends ResourceServerConfigurerAdapter { ... }`。
画面 8: 展示了 PPT 页面，内容为“小王是黑马程序员的一名学员，（暂时）登录黑马程序员技术论坛，如下图所示：”，并展示了一个登录界面。
画面 9: 在 IDEA 中展示 `ResourceServerConfig.java` 文件，内容为 `@Configuration @EnableResourceServer public class ResourceServerConfig extends ResourceServerConfigurerAdapter { ... }`。
画面 10: 在 IDEA 中展示 `ResourceServerConfig.java` 文件，内容为 `public static final String RESOURCE_ID = "wanxing-resource"; private AuthenticationEntryPoint point = new RestAuth2ExceptionEntryPoint(); private RestAccessDeniedHandler handler = new RestAccessDeniedHandler();`。
画面 11: 在 IDEA 中展示 `ResourceServerConfig.java` 文件，内容为 `resources.authenticationEntryPoint(point).accessDeniedHandler(handler);`。
画面 12: 在 IDEA 中展示 `ResourceServerConfig.java` 文件，内容为 `http.sessionManagement().sessionCreationPolicy(SessionCreationPolicy.IF_REQUIRED).and().httpSecurity().authorizeRequests().antMatchers("/consumer/**").denyAll().antMatchers("/consumer/my/**").access(attribute: "#oauth2.hasScope('read') and #oauth2.clientHasRole('ROLE_CONSUMER')").antMatchers("/consumer/**").permitAll();`。
画面 13: 展示了多个窗口，包括 IntelliJ IDEA、Apollo 配置中心、Postman、SQL Server Management Studio、cmd 窗口等，显示了服务启动和配置管理的场景。
画面 14: 展示了微服务架构图，包含接入方（WEB、移动端、第三方接入）、网关、认证服务（UAA）、资源服务（服务1、服务2、服务n）等组件及其交互流程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-configuration-processor</artifactId>
    <optional>true</optional>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
<dependency>
    <groupId>org.apache.commons</groupId>
</dependency>
```

画面 3:
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-security</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-jwt</artifactId>
</dependency>
```

画面 4:
```java
cn.itcast.wanxing2p.gateway.config.ResourceServerConfig
描述：Spring Security OAuth2 资源服务实现，用于网关对接入客户端的权限拦截，可以指定某个接入客户端只允许访问部分资源服务
cn.itcast.wanxing2p.gateway.config.RestAccessDeniedHandler
描述：修改网关错误响应与平台整体风格一致，无需关注。
cn.itcast.wanxing2p.gateway.config.RestAuth2ExceptionEntryPoint
描述：修改网关错误响应与平台整体风格一致，无需关注。
```

画面 5:
```java
如果网关接收到的请求uri符合/consumer/**表达式，该请求将被转发至consumer-service（用户中心）。为了便于权限拦截，我们将服务内部的接口进行了细分，大体分为三类：
1. 受保护的C端用户接口（C端用户登录后可访问）
   Url格式：/服务名称/my/资源名称/*
2. 受保护的B端用户接口（B端用户登录后可访问）
   Url格式：/服务名称/m/资源名称/*
3. 公开资源
   Url格式：/服务名称/资源名称/*
```

画面 6:
```java
public class ConsumerServerConfig extends ResourceServerConfigurerAdapter {
    @Autowired
    private TokenStore tokenStore;
    @Override
    public void configure(ResourceServerSecurityConfigurer resources) throws Exception {
        resources.tokenStore(tokenStore).resourceId(RESOURCE_ID)
                .stateless(true);
        resources.authenticationEntryPoint(point).accessDeniedHandler(handler);
    }
    @Override
    public void configure(HttpSecurity http) throws Exception {
        http.sessionManagement().sessionCreationPolicy(SessionCreationPolicy.IF_REQUIRED)
                .and().httpSecurity().authorizeRequests()
                .antMatchers("/consumer/**").denyAll()
                .antMatchers("/consumer/my/**").access(attribute: "#oauth2.hasScope('read') and #oauth2.clientHasRole('ROLE_CONSUMER')")
                .antMatchers("/consumer/**").permitAll();
    }
}
```

画面 7:
```java
@Configuration
@EnableResourceServer
public class ResourceServerConfig extends ResourceServerConfigurerAdapter {
    @Autowired
    private TokenStore tokenStore;
    @Override
    public void configure(ResourceServerSecurityConfigurer resources) throws Exception {
        resources.tokenStore(tokenStore).resourceId(RESOURCE_ID)
                .stateless(true);
    }
}
```

画面 8:
```java
public class ResourceServerConfig extends ResourceServerConfigurerAdapter {
    @Autowired
    private TokenStore tokenStore;
    @Override
    public void configure(ResourceServerSecurityConfigurer resources) throws Exception {
        resources.tokenStore(tokenStore).resourceId(RESOURCE_ID)
                .stateless(true);
    }
}
```

画面 9:
```java
@Configuration
@EnableResourceServer
public class ResourceServerConfig extends ResourceServerConfigurerAdapter {
    @Autowired
    private TokenStore tokenStore;
    @Override
    public void configure(ResourceServerSecurityConfigurer resources) throws Exception {
        resources.tokenStore(tokenStore).resourceId(RESOURCE_ID)
                .stateless(true);
    }
}
```

画面 10:
```java
public static final String RESOURCE_ID = "wanxing-resource";
private AuthenticationEntryPoint point = new RestAuth2ExceptionEntryPoint();
private RestAccessDeniedHandler handler = new RestAccessDeniedHandler();
```

画面 11:
```java
resources.authenticationEntryPoint(point).accessDeniedHandler(handler);
```

画面 12:
```java
http.sessionManagement().sessionCreationPolicy(SessionCreationPolicy.IF_REQUIRED).and().httpSecurity().authorizeRequests().antMatchers("/consumer/**").denyAll().antMatchers("/consumer/my/**").access(attribute: "#oauth2.hasScope('read') and #oauth2.clientHasRole('ROLE_CONSUMER')").antMatchers("/consumer/**").permitAll();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题为“1.4.2 环境准备”，架构图中：
- “WEB”、“移动端”、“第三方接入”指向“网关”。
- “网关”指向“认证”和“资源”。
- “认证”指向“统一账号服务”。
- “资源”指向“微服务1”、“微服务2”、“微服务n”。

画面 4: 标题为“1.4.2 环境准备”，内容为三个配置类的描述。

画面 5: 标题为“如果网关接收到的请求uri符合/consumer/**表达式，该请求将被转发至consumer-service（用户中心）。为了便于权限拦截，我们将服务内部的接口进行了细分，大体分为三类”，并列出了三类接口的访问方式。

画面 6: 标题为“小王是黑马程序员的一
