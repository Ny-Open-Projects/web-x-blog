# 画面线理解：09-基于jwt的用户鉴权：使用拦截器统一处理claims

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\09-基于jwt的用户鉴权：使用拦截器统一处理claims_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 01:22, 02:17, 02:39, 03:02, 03:48, 04:25, 04:57, 05:19, 05:57, 06:12, 06:35, 07:03, 07:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:13:26

1) 这一组画面整体在讲什么（一句话）：
实现一个基于 Spring MVC 的 JWT 拦截器，用于在请求进入控制器方法前解析并验证 JWT Token，并将用户信息存入请求属性中。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 JwtInterceptor.java 文件，定义了 preHandle 方法用于拦截请求，注释说明了其功能：简化 token 处理、统一用户权限校验、判断用户是否具有当前接口权限。
画面 2: 在 preHandle 方法中添加了注释，说明了从 token 中解析出 claims 并将其绑定到 request 中。
画面 3: 展示了 preHandle 方法中获取 request 对象的代码，但未完成。
画面 4: 在 preHandle 方法中添加了注释，说明了通过 request 获取 token 信息。
画面 5: 展示了 UserContoller.java 中的 profile 接口，用于根据用户 ID 获取用户权限信息。
画面 6: 在 JwtInterceptor.java 中添加了 @Autowired 注解，用于注入 JwtUtils。
画面 7: 在 preHandle 方法中添加了注释，说明了从 token 中解析 claims 并将其绑定到 request 中。
画面 8: 在 JwtInterceptor.java 中添加了 @Component 注解，使其成为 Spring Bean。
画面 9: 展示了 UserContoller.java 中的 profile 接口，用于根据用户 ID 获取用户权限信息。
画面 10: 在 profile 接口中，从 request 中获取 claims 对象，并根据用户等级设置权限。
画面 11: 展示了 UserContoller.java 中的 login 接口，用于用户登录并返回 JWT Token。
画面 12: 展示了 BaseContoller.java 中的 setServletRequest 方法，用于设置 request、response、claims 等属性。
画面 13: 展示了 UserContoller.java 中的 profile 接口，用于根据用户 ID 获取用户权限信息。
画面 14: 展示了 BaseContoller.java 中的 setServletRequest 方法，用于设置 request、response、claims 等属性。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 自定义拦截器
 * 继承HandlerInterceptorAdapter
 * preHandle:进入到控制器方法之前执行的内容
 * boolean true: 可以继续执行控制器方法
 * false: 拦截
 * postHandler: 执行控制器方法之后执行的内容
 * afterCompletion:  响应结束之后执行的内容
 * 1.简化获取token数据的代码编写（判断是否登录）
 * 2.统一的用户权限校验（是否登录）
 * 3.判断用户是否具有当前访问接口的权限
 */
public class JwtInterceptor extends HandlerInterceptorAdapter {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        // 1.
        return true;
    }
}
```

画面 2:
```java
/**
 * 自定义拦截器
 * 继承HandlerInterceptorAdapter
 * preHandle:进入到控制器方法之前执行的内容
 * boolean true: 可以继续执行控制器方法
 * false: 拦截
 * postHandler: 执行控制器方法之后执行的内容
 * afterCompletion:  响应结束之后执行的内容
 * 1.简化获取token数据的代码编写（判断是否登录）
 * 2.统一的用户权限校验（是否登录）
 * 3.判断用户是否具有当前访问接口的权限
 */
public class JwtInterceptor extends HandlerInterceptorAdapter {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        // 1.通过request获取请求token信息
        // 2.从token中解析获取claims
        // 3.将claims绑定到request中
    }
}
```

画面 3:
```java
public class JwtInterceptor extends HandlerInterceptorAdapter {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        // 1.通过request获取请求token信息
        // 2.从token中解析获取claims
        // 3.将claims绑定到request中
    }
}
```

画面 4:
```java
/**
 * 自定义拦截器
 * 继承HandlerInterceptorAdapter
 * preHandle:进入到控制器方法之前执行的内容
 * boolean true: 可以继续执行控制器方法
 * false: 拦截
 * postHandler: 执行控制器方法之后执行的内容
 * afterCompletion:  响应结束之后执行的内容
 * 1.简化获取token数据的代码编写（判断是否登录）
 * 2.统一的用户权限校验（是否登录）
 * 3.判断用户是否具有当前访问接口的权限
 */
public class JwtInterceptor extends HandlerInterceptorAdapter {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        // 1.通过request获取请求token信息
        String authorization = request.getHeader("Authorization");
        if (StringUtils.isEmpty(authorization) && authorization.startsWith("Bearer ")) {
            // 2.从token中解析获取claims
            // 3.将claims绑定到request中
        }
    }
}
```

画面 5:
```java
/**
 * 自定义拦截器
 * 继承HandlerInterceptorAdapter
 * preHandle:进入到控制器方法之前执行的内容
 * boolean true: 可以继续执行控制器方法
 * false: 拦截
 * postHandler: 执行控制器方法之后执行的内容
 * afterCompletion:  响应结束之后执行的内容
 * 1.简化获取token数据的代码编写（判断是否登录）
 * 2.统一的用户权限校验（是否登录）
 * 3.判断用户是否具有当前访问接口的权限
 */
public class JwtInterceptor extends HandlerInterceptorAdapter {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        // 1.通过request获取请求token信息
        String authorization = request.getHeader("Authorization");
        if (StringUtils.isEmpty(authorization) && authorization.startsWith("Bearer ")) {
            // 2.从token中解析获取claims
            String token = authorization.replace("Bearer ", replacement: "");
            Claims claims = jwtUtils.parseJwt(token);
            // 3.将claims绑定到request中
            request.setAttribute("user_claims", claims);
        }
    }
}
```

画面 6:
```java
/**
 * 自定义拦截器
 * 继承HandlerInterceptorAdapter
 * preHandle:进入到控制器方法之前执行的内容
 * boolean true: 可以继续执行控制器方法
 * false: 拦截
 * postHandler: 执行控制器方法之后执行的内容
 * afterCompletion:  响应结束之后执行的内容
 * 1.简化获取token数据的代码编写（判断是否登录）
 * 2.统一的用户权限校验（是否登录）
 * 3.判断用户是否具有当前访问接口的权限
 */
public class JwtInterceptor extends HandlerInterceptorAdapter {
    @Autowired
    private JwtUtils jwtUtils;
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        // 1.通过request获取请求token信息
        String authorization = request.getHeader("Authorization");
        if (StringUtils.isEmpty(authorization) && authorization.startsWith("Bearer ")) {
            // 2.从token中解析获取claims
            String token = authorization.replace("Bearer ", replacement: "");
            Claims claims = jwtUtils.parseJwt(token);
            // 3.将claims绑定到request中
            request.setAttribute("user_claims", claims);
        }
    }
}
```

画面 7:
```java
/**
 * 自定义拦截器
 * 继承HandlerInterceptorAdapter
 * preHandle:进入到控制器方法之前执行的内容
 * boolean true: 可以继续执行控制器方法
 * false: 拦截
 * postHandler: 执行控制器方法之后执行的内容
 * afterCompletion:  响应结束之后执行的内容
 * 1.简化获取token数据的代码编写（判断是否登录）
 * 2.统一的用户权限校验（是否登录）
 * 3.判断用户是否具有当前访问接口的权限
 */
public class JwtInterceptor extends HandlerInterceptorAdapter {
    @Autowired
    private JwtUtils jwtUtils;
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        // 1.通过request获取请求token信息
        String authorization = request.getHeader("Authorization");
        if (StringUtils.isEmpty(authorization) && authorization.startsWith("Bearer ")) {
            // 2.从token中解析获取claims
            String token = authorization.replace("Bearer ", replacement: "");
            Claims claims = jwtUtils.parseJwt(token);
            // 3.将claims绑定到request中
            request.setAttribute("user_claims", claims);
        }
    }
}
```

画面 8:
```java
/**
 * 自定义拦截器
 * 继承HandlerInterceptorAdapter
 * preHandle:进入到控制器方法之前执行的内容
 * boolean true: 可以继续执行控制器方法
 * false: 拦截
 * postHandler: 执行控制器方法之后执行的内容
 * afterCompletion:  响应结束之后执行的内容
 * 1.简化获取token数据的代码编写（判断是否登录）
 * 2
