# 03_后台微服务其他必须配置项配置

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\03_后台微服务其他必须配置项配置【海量资源尽在 666java.com】.mp4
- 时长 6分4秒（音频 364s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续往下讲然后第二块呢是有一个其他配置项并且是必须配置这里边呢是有两个啊第一个是配置当前的JSON第二个是有一个过滤的配置咱们一会儿再说过滤啊咱们先说这个JSON这个JSON的封装呢其实咱们在第一天已经讲完了就是在第一天去把它去做了一个封装它的一个作用大家还知道吗
[00:24] 它的作用是不是在有一些数字ID进行参数传递的时候进行一些序列化也就是加密操作对吧比如说它在从后台传到前台的时候咱们需要加密从前台传到后台的时候咱们需要解密对吧那这个配置咱们之前都写过也加载过所以说这会儿你想让它生效的话你得去把它给作为配置也就是说你需要去扫描到当前的包才行
[00:53] 那这个咱们在每一个微服务模块下都需要这么去做所以说呢你把这个代码啊需要去在每一个微服务模块下去都得去呃加载进来行那咱们一个个去加啊比如说咱们先去从article开始打开它嗯这个config对吧你直接在这创建一个类这样的叫initconfig好然后这个呢是一个configuration是吧
[01:23] 还要去扫描一个包包呢其实就在那在com.com.init这个你可以在这找啊在当前的common下面找到commoncommon里边还有个common里边有个init里边呢其实就是当前的一个init jacksonconfig其实这个呢就是它的一个page类你加载完这个类之后呢它才能去生效所以说呢这个类啊
[01:50] 这个类应该是在每一个v服务下边都应该存在也就是当前这个东西好吧咱们就拷贝一下它在每一个v服务模块下他们都都去加进来啊然后首先是article然后是当前的行为好拷贝一下然后下面是login拷贝一下然后下面还有个user那这个就加完了啊加完之后啊咱们还有第二个配置需要去做就是有一个过滤这个过滤的
[02:29] 过滤的话呢主要是说的是用户验证的过滤器用户验证啊咱们也应当是在每一个微服务模块下都去加这么个东西那这个包下边其实咱们之前没有讲过咱们简单说一说啊就这个包下边呢主要是针对于当前的APP的一个认证的一些过滤器那咱们可以打开来看一看啊它在哪呢在当前的common包下边打开这有一个webweb呢其实在针对于每一个模块啊它都有
[03:00] 咱们现在只要去用的是当前的APP的ServoRate打开它那这里边有两个啊第一个呢是当前的一个Tag的签名是吧验证签名第二个是当前的一个验证的一个Token就是另牌嘛OK打开它啊打开它之后呢这里边有一行代码咱们需要去知道啊哪一行呢就是往下走往下走啊好就这一行看到了吧这一行呢其实呢就是往当前现成中去添加了一个用户
[03:31] 其实咱们在之前写代码的时候其实又不断的从当前现成中去拿当前的用户那用户怎么拿呢其实都是在这去做完验证之后把用户给装入到了当前的现成所以说这步很关键啊那这个过程呢其实就是解析JWT的过程那这个过程啊其实你前天呢需要去传一个Token过来然后呢这个Token呢其实就是用户的信息最终呢咱们是把它把这个串给解析
[03:57] 记完之后如果说没有问题咱们就把它装入到当前的APP Thread local中那就是当前现成中这时候你可以在你的任意一个位置就可以拿到当前的一个什么用户信息让你通过当前这个工具类是吧行啊那这个你想让它生效的话呢怎么办呢你得去加载它是一个order啊并且呢它是一个filter这时候它就会去过滤所有的请求好那这时候咱们就可以去怎么着呢咱们就可以去
[04:27] 在每一个微服务模块下边当然了咱们目前所用到的模块目前只有useruser需要用它下面这些东西咱们也有的时候咱们后期也会去加所以说你现在你可以先去加user后期用到的时候你可以再去加别其他的好吧行咱们先在user上面去把这个东西给它加进来好那不一样的是哪一块是configuration是差不多的但下面扫描包就不一样了就是不是components看
[04:57] 它啥呢它是一个serverletcomponent scan这时候你要把当前的包扫描一下就可以了好吧那咱们就手写一下在当前user那为什么加到这咱们一会去做测试的时候咱们再说好吧叫securitys-e-c-u-r-i-d-yconfig好吧下面是一个configurationat然后下面是一个serverletcomponent scan
[05:30] 扫描的包呢其实就是com.黑马com然后是webappsucurity好吧那这样的话他就能去生效了不能去走到当前那个哎我说的刚才那个什么过滤器好吧行那这个这一块内容呢咱们就算是设置完了啊行后期的话咱们如果有需要的话咱们再去重新去设置好吧行那关于
[06:00] 当前后台的其他配置项咱们就算做完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

