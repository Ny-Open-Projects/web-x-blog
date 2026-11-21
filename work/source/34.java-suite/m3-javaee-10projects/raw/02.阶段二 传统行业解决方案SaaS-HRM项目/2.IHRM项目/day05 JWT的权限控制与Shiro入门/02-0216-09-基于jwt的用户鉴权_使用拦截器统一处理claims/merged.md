# 09-基于jwt的用户鉴权：使用拦截器统一处理claims

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\09-基于jwt的用户鉴权：使用拦截器统一处理claims_【海量资源尽在 ubkz.com】.mp4
- 时长 7分58秒（音频 479s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了这个拦截器呢我们简单的说了一下那接下来呢我们要完成的就是在这个拦截器当中先把第一件事给它搞定就是简化我们获取token数据的这个代码的一个编写那我们的思路呢很简单是这样的思路呢很简单就是会有简化代码的一个编写当然这里面呢我们还要去判断是否登录啊判断是否登录那我们的思路很简单首先呢第一件事我们呢通过request获取到我们的
[00:34] token信息获取到我们请求token好了那接下来呢第二件事第二件事那就是从token中解析获取到我们的clamsclams那接着第三件事为了方便我们底下每一个控制器方法的一个访问那我们可以把这个clams直接绑定到request域域中那绑定到request域当中那接下来我们说过了
[01:12] 拦截器方法pro handler先去执行接着是不是再去执行每一个方法那也就是说执行到profile的时候require当中已经有了我们已经设置好的clam那这样一来我在控制器方法当中直接get获取就可以了好那接下来呢我们来看一下我们这个拦截器要想实现第一个功能我们的代码应该如何去进行编写那其实代码的逻辑呢比较简单跟上面的都是一一对应的去获取token
[01:42] 那获取token呢就这样了Ctrl C拿过来Ctrl V好了在这边呢我做一个简单的判断判断是判断这个头请求头信息是否为空或者是否以我们约定的bill开头所以我这个代码呢就可以这样if stj utils打点再点is empty判断一下它是否为空
[02:27] 当然了我们是最好是不唯空嘛不唯空并且就是这玩意儿它start with beer就是我们拿到的这个beer of trial那这样一来呢我们就执行下去好了那当然了就没有什么else不管你如果这都唯空了那就认为着你根本就没登录没登录一会儿我统一的抛出一个异常不就可以了吗好了那这边呢抛出一个异常当然这个异常呢我们之前也写过我就直接从这边拿过来了
[03:06] 好那接下来在里面呢我们要完成的事情就是第二件事第二件事是这样的就是说呢当前我这个投信息是以bill开头的所以我对这个字符串应该处理一下真正的去获取我们的token数据那获取这个token数据呢也比较简单死剧类型的比如说我就叫token t-o-k-e-n等于我们之前也做过处理就是替换字符串OK那替换好了字符串那接着我们开始解析token获取我们的clamps
[03:41] 那借助我们的JWT工具类当然了JWT工具类现在还没有at auto will一代注入进来private JWTutil JWTutil好了这边呢要想注入的话我上边呢就需要at components ump代表的是创建对象交给死亡容器管理他们是配合使用的吧好了那接下来呢我们在这边就可以借助JWT utils打点进行解析我们结果一个pairs方法把token传递进去
[04:12] 好了这样一来我们就能够得到clamps当然了对于这clamps呢我们可以做一个判断if clamps它得不等于空啊不等于空才认为着它有数据啊不等于那那不等于那我们要做的事情是不是就可以把它绑定到我们的request域那这样一来request打点我set attribute好了这个比如说我就叫做user下滑线clams那绑定到我们的request域上
[04:43] 好了绑定好了之后return true继续让它向下执行进入到我们的控制器方法OK那这样一来我们这个拦截器的代码呢其实就已经写好了当然我们现在只完成了第一件事那拦截器代码写好了之后那我们需要修改一下user Controller那现在user Controller里面这些内容一直到获取clam我们都可以把它哎沉掉了
[05:09] 那这个时候我应该如何去做呢其实很简单我们可以通过request打点get我们叫做attribute点getattribute那我们放的这个值呢叫做userclimb拿过来OK那这样一来呢我们就能够获取到我们的climb对象做一个强制转型OK那这样一来呢我们底下的后续处理其实都是一模一样的
[05:51] 那其实有的朋友就说呢我觉得这样写还是比较啰嗦还是比较麻烦那怎么办那别忘了我们这边呢是不是有一个叫做base Controller那在base Controller当中我是不是也可以这边定一个公共的一个属性比如说呢定义的这个公共属性呢就叫做抱歉我拷一下这个代码手写没什么必要claims好了那这边我们是不是通过在我们的代码部分做一个判断if
[06:25] 就这边直接抱歉我就直接拷过来了好了我们可以object obgoal等于它那接着呢我们做一个判断ifobject不等于呢好了那这边呢我们就可以类似点clam等于就是直接把object进行一个转强制转型就可以了OK那这样一来我user Controller里面这都不需要了直接clam思
[07:03] 点get id更简单更简单因为我们这边有公共的一些设置那当然了我们之前是不是说过一个其他的问题就是说这个hominy id跟这个hominy我们是想办法处理啊那想办法处理应该怎么去做呢其实这个也就不难了那我们现在由于你token当中有数据token当中有数据我直接就可以从clam里面获取比如说呢clam打点get
[07:32] 那我们存的是一个company id好了那这边呢同样的打点get存的是一个company name好了那前面呢我们做一个简单的强制转型就可以了ok那这样一来呢我们整个的之前的理流的问题咱们就已经都把它解决了ok

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

