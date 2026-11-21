# 画面线理解：15.统一处理token（功能测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\15.统一处理token（功能测试）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:30, 00:43, 00:57, 01:21, 01:31, 02:01, 02:20, 02:48, 03:06, 03:36, 03:51, 04:16, 04:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:43:03

1) 这一组画面整体在讲如何通过拦截器实现接口权限控制，并处理文件上传时的用户身份验证和线程局部变量（ThreadLocal）的使用。

2) 按时间顺序列出每张画面的要点：
画面1：在IntelliJ IDEA中，展示TokenInterceptor类的代码，该类实现了HandlerInterceptor接口，用于在请求处理前进行权限判断。代码中包含对@NoAuthorization注解的检查，以及从请求头获取token并查询用户信息的逻辑。
画面2：在调试模式下，TokenInterceptor的preHandle方法被调用，断点位于判断handler是否为HandlerMethod的代码行，变量信息显示当前请求的handler和request对象。
画面3：在调试模式下，TokenInterceptor的preHandle方法继续执行，断点位于从请求头获取token并查询用户信息的代码行，变量信息显示当前请求的handler和request对象。
画面4：在调试模式下，TokenInterceptor的preHandle方法继续执行，断点位于判断handler是否为HandlerMethod的代码行，变量信息显示当前请求的handler和request对象。
画面5：在Advanced REST Client中，用户尝试上传文件，但请求头中缺少Authorization，导致服务器返回500错误。
画面6：在IntelliJ IDEA中，展示MovementsService类的saveMovements方法，该方法用于处理文件上传，但当前请求不是multipart类型，导致抛出异常。
画面7：在Advanced REST Client中，用户尝试上传文件，但请求头中缺少Authorization，导致服务器返回500错误。
画面8：在IntelliJ IDEA中，展示NoAuthorization注解的定义，该注解用于标记不需要权限验证的接口。
画面9：在Advanced REST Client中，用户上传文件，请求头中包含Authorization，服务器返回200成功。
画面10：在IntelliJ IDEA中，展示RedisCacheInterceptor类的代码，该类用于缓存处理，代码中包含对RedisTemplate的初始化和配置。
画面11：在IntelliJ IDEA中，展示MovementsService类的saveMovements方法，该方法用于处理文件上传，代码中包含从ThreadLocal中获取用户信息并设置Publish对象的逻辑。
画面12：在IntelliJ IDEA中，展示MovementsService类的saveMovements方法，该方法用于处理文件上传，代码中包含从ThreadLocal中获取用户信息并设置Publish对象的逻辑。
画面13：在Advanced REST Client中，用户上传文件，请求头中包含Authorization，服务器返回500错误。
画面14：在Typora中，展示day03.md文档的内容，该文档介绍了如何使用ThreadLocal来存储和获取用户信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
```java
public class TokenInterceptor implements HandlerInterceptor {
    @Autowired
    private UserService userService;

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response) {
        //判断，请求的方法是否包含了 @NoAuthorization，如果包含了，就不需要做处理
        if(handler instanceof HandlerMethod) {
            HandlerMethod handlerMethod = (HandlerMethod) handler;
            NoAuthorization annotation = handlerMethod.getMethod().getAnnotation(NoAuthorization.class);
            if(annotation != null) {
                return true;
            }
        }
        String token = request.getHeader("Authorization");
        User user = this.userService.queryUserByToken(token);
        if(null == user) {
            response.setStatus(401); //无权限
            return false;
        }
        return true;
    }
```

画面2：
```java
if(handler instanceof HandlerMethod) {
    HandlerMethod handlerMethod = (HandlerMethod) handler;
    NoAuthorization annotation = handlerMethod.getMethod().getAnnotation(NoAuthorization.class);
    if(annotation != null) {
        return true;
    }
}
```

画面3：
```java
String token = request.getHeader("Authorization");
User user = this.userService.queryUserByToken(token);
if(null == user) {
    response.setStatus(401); //无权限
    return false;
}
```

画面6：
```java
public Boolean saveMovements(String textContent,
                             String location,
                             String longitude,
                             String latitude,
                             MultipartFile[] multipartFile) {
    User user = UserThreadLocal.get();
    Publish publish = new Publish();
    publish.setUserId(user.getId());
```

画面8：
```java
package com.tanhua.server.utils;
import java.lang.annotation.*;
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface NoAuthorization {
}
```

画面10：
```java
private static ObjectMapper mapper = new ObjectMapper();
@Autowire
private RedisTemplate<String, String> redisTemplate;
@Value("${tanhua.cache.enable}")
private Boolean enable;
@Override
if (!enable) {
    return true;
}
```

画面11：
```java
public Boolean saveMovements(String textContent,
                             String location,
                             String longitude,
                             String latitude,
                             MultipartFile[] multipartFile) {
    User user = UserThreadLocal.get();
    Publish publish = new Publish();
    publish.setUserId(user.getId());
```

画面14：
```java
public boolean savePublish(String textContent,
                           String location,
                           MultipartFile[] multipartFile) {
    User user = UserThreadLocal.get();
    Publish publish = new Publish();
    publish.setUserId(user.getId());
    publish.setText(textContent);
    publish.setLocation(location);
    publish.setSeeType(1);
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面14：
标题：2.3.5. 使用ThreadLocal
内容：
```java
//获取当前线程的用户信息
User user = UserThreadLocal.get();
Publish publish = new Publish();
publish.setUserId(user.getId());
publish.setText(textContent);
publish.setLocation(location);
publish.setSeeType(1);
```

5) 无
