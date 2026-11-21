# 画面线理解：03_后台微服务其他必须配置项配置

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\03_后台微服务其他必须配置项配置【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:06, 01:17, 01:24, 01:44, 01:57, 02:10, 02:27, 03:20, 03:44, 04:15, 04:32, 05:14, 05:26, 05:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:27:40

1) 这一组画面整体在讲什么（一句话）：
演示 Spring Boot 项目中登录模块的控制器、配置类和过滤器的实现，以及相关的 Jackson 序列化、过滤器和安全配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 `LoginController.java` 文件，其中定义了 `@RestController` 和 `@RequestMapping("/api/v1/login")`。
- 方法 `login_auth` 被 `@PostMapping("/login_auth")` 注解，调用 `apUserLoginService.loginAuth(user)`。
- 项目结构显示了 `heimaleadnews-login` 模块。

画面 2：
- 展示了 `InitConfig.java` 文件，位于 `com.heima.article.config` 包下。
- 项目结构显示了 `heimaleadnews-article` 模块。

画面 3：
- 在 `InitConfig.java` 中添加了 `@Configuration` 注解。

画面 4：
- 展示了 `InitJacksonConfig.java` 文件，位于 `com.heima.common.common.init` 包下。
- 代码中定义了 `@Configuration` 和 `@Bean` 注解，用于配置 `ObjectMapper`。

画面 5：
- 项目结构中选中了 `InitJacksonConfig.java` 文件。

画面 6：
- 展示了 `InitConfig.java` 文件，位于 `com.heima.behavior.config` 包下。
- 代码中添加了 `@ComponentScan("com.heima.common.common.init")` 注解。

画面 7：
- 展示了 PPT 页面，标题为“1.2 其他配置项（必须配置）”。
- 子标题“1.2.1 配置 jackson 解析”和“1.2.2 配置过滤”。
- 代码片段显示了 `@Configuration` 和 `@ComponentScan` 注解。

画面 8：
- 展示了 `AppTokenFilter.java` 文件，位于 `com.heima.common.web.app` 包下。
- 方法 `doFilter` 中包含对请求头的判断和 `checkToken` 方法的调用。
- 方法 `checkToken` 中包含对 token 的解析和验证逻辑。

画面 9：
- 展示了 `AppTokenFilter.java` 文件，继续展示 `checkToken` 方法的逻辑。
- 包含对用户信息的设置和 token 过期的处理。

画面 10：
- 展示了 `AppTokenFilter.java` 文件，继续展示 `checkToken` 方法的逻辑。
- 包含对用户信息的设置和 token 过期的处理。

画面 11：
- 展示了 PPT 页面，标题为“1.2 其他配置项（必须配置）”。
- 子标题“1.2.1 配置 jackson 解析”和“1.2.2 配置过滤”。
- 代码片段显示了 `@Configuration` 和 `@ComponentScan` 注解。

画面 12：
- 展示了 `AppTokenFilter.java` 文件，位于 `com.heima.login.config` 包下。
- 代码中定义了 `@Order(2)` 和 `@WebFilter` 注解。
- 方法 `doFilter` 中包含对请求头的判断和 `checkToken` 方法的调用。

画面 13：
- 展示了 `SecurityConfig.java` 文件，位于 `com.heima.login.config` 包下。
- 代码中添加了 `@Configuration` 注解。

画面 14：
- 展示了 PPT 页面，标题为“1.2 其他配置项（必须配置）”。
- 子标题“1.2.1 配置 jackson 解析”和“1.2.2 配置过滤”。
- 代码片段显示了 `@Configuration` 和 `@ComponentScan` 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```java
@RestController
@RequestMapping("/api/v1/login")
public class LoginController implements LoginControllerApi {
    @Autowired
    private ApUserLoginService apUserLoginService;

    @PostMapping("/login_auth")
    public ResponseResult loginAuth(@RequestBody ApUser user) {
        return apUserLoginService.loginAuth(user);
    }
}
```

画面 2：
```java
package com.heima.article.config;

public class InitConfig {
}
```

画面 3：
```java
@Configuration
public class InitConfig {
}
```

画面 4：
```java
@Configuration
public class InitJacksonConfig {

    @Bean
    public ObjectMapper objectMapper() {
        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper = ConfusionModule.registerModule(objectMapper);
        return objectMapper;
    }
}
```

画面 5：
- 无新代码，仅显示项目结构。

画面 6：
```java
@Configuration
@ComponentScan("com.heima.common.common.init")
public class InitConfig {
}
```

画面 7：
```java
@Configuration
@ComponentScan("com.heima.common.common.init")
public class InitConfig {
}

@Configuration
@ServiceComponentScan("com.heima.common.web.app.security")
public class SecurityConfig {
}
```

画面 8：
```java
public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain) throws IOException {
    HttpServletRequest request = (HttpServletRequest) req;
    HttpServletResponse response = (HttpServletResponse) res;
    ResponseResult<?> result = checkToken(request);
    if (true || result == null || !Contents.isProd()) {
        chain.doFilter(req, res);
    } else {
        response.setCharacterEncoding(Contents.CHARSET_NAME);
        response.setContentType("application/json");
        response.getOutputStream().write(JSON.toJSONString(result).getBytes());
    }
}

public ResponseResult checkToken(HttpServletRequest request) {
    String token = request.getHeader("token");
    if (StringUtils.isEmpty(token)) {
        Claims claim = AppJwtUtil.getClaimedBody(token);
        int result = AppJwtUtil.verifyToken(claim);
        if (result == 0 || result == -1) {
            ApUser user = new ApUser();
            user.setId(Long.valueOf((Integer) claim.get("id")));
            user = findUser(user);
            if (user.getId() != null) {
                AppThreadLocalUtils.setUser(user);
            }
        } else if (result == -2) {
            ResponseResult.setAppHttpCodeEnum(TOKEN_EXPIRE);
        } else if (result == -3) {
            ResponseResult.setAppHttpCodeEnum(TOKEN_INVALID);
        }
    }
    return null;
}
```

画面 9：
```java
public ResponseResult checkToken(HttpServletRequest request) {
    String token = request.getHeader("token");
    if (StringUtils.isEmpty(token)) {
        Claims claim = AppJwtUtil.getClaimedBody(token);
        int result = AppJwtUtil.verifyToken(claim);
        if (result == 0 || result == -1) {
            ApUser user = new ApUser();
            user.setId(Long.valueOf((Integer) claim.get("id")));
            user = findUser(user);
            if (user.getId() != null) {
                AppThreadLocalUtils.setUser(user);
            }
        } else if (result == -2) {
            ResponseResult.setAppHttpCodeEnum(TOKEN_EXPIRE);
        } else if (result == -3) {
            ResponseResult.setAppHttpCodeEnum(TOKEN_INVALID);
        }
    }
    return null;
}
```

画面 10：
```java
public ResponseResult checkToken(HttpServletRequest request) {
    String token = request.getHeader("token");
    if (StringUtils.isEmpty(token)) {
        Claims claim = AppJwtUtil.getClaimedBody(token);
        int result = AppJwtUtil.verifyToken(claim);
        if (result == 0 || result == -1) {
            ApUser user = new ApUser();
            user.setId(Long.valueOf((Integer) claim.get("id")));
            user = findUser(user);
            if (user.getId() != null) {
                AppThreadLocalUtils.setUser(user);
            }
        } else if (result == -2) {
            ResponseResult.setAppHttpCodeEnum(TOKEN_EXPIRE);
        } else if (result == -3) {
            ResponseResult.setAppHttpCodeEnum(TOKEN_INVALID);
        }
    }
    return null;
}
```

画面 12：
```java
import com.heima.utils.JWTUtils;
import io.jsonwebtoken.Claims;
import org.apache.commons.lang3.StringUtils;
import org.springframework.core.annotation.Order;
import org.springframework.web.filter.GenericFilterBean;
import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Order(2)
@WebFilter(filterName = "appTokenFilter", urlPatterns = "/")
public class AppTokenFilter extends GenericFilterBean {

    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain) throws IOException {
        HttpServletRequest request = (HttpServletRequest) req;
        HttpServletResponse response = (HttpServletResponse) res;
        ResponseResult<?> result = checkToken(request);
        if (true || result == null || !Contents.isProd()) {
            chain.doFilter(req, res);
        } else {
            response.setCharacterEncoding(Contents.CHARSET_NAME);
            response.setContentType("application/json");
            response.getOutputStream().write(JSON.toJSONString(result).getBytes());
        }
    }

    public ResponseResult checkToken(HttpServletRequest request) {
        String token = request.getHeader("token");
        if (StringUtils.isEmpty(token)) {
            Claims claim = AppJwtUtil
