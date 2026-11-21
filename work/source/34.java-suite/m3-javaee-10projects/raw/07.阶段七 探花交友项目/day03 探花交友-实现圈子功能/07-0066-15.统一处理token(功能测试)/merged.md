# 15.统一处理token（功能测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\15.统一处理token（功能测试）_【海量资源尽在 666java.com】.mp4
- 时长 4分35秒（音频 276s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来测试一下我们刚刚所写的这个拦截器是否有效那么我们在我们拦截器的这个位置呢去打一个断点然后呢我们可以呢在我们的Service中呢也去打一个断点那么这样的话呢我们就可以来跑起来做一个测试了好那我们来等待一下它的一个启动好那么现在呢就启动起来了那么接下来呢我们去点击一下这个send发送那么就会
[00:28] 进入到我们这个端点了那我们来看一下它的一个执行效果那么来看一下这个呢并没有去标记我们的这个就是不需要做认证的然后呢我们下面来拿到我们的token拿到token呢去userservice去获取euro那么如果不为空如果不为空的就会走到这个位置来那么就return true会做一个放行ok然后呢
[00:54] 这个请求是不是又来了然后我们放过然后我们没有去没有是不是没有进入我们刚刚我们还没有进入Service因为我们在Service中是要求有一个我们图片上传的对吧但是现在并没有图片所以导致并没有进入也就是说参数目前的不符合规则我们就来一张图片可以测一下
[01:24] 然后呢往下面走走走走走走走走OK好通过那么这个时候那么现在呢就进入到了这个Controller然后呢我们啊就用Service然后呢往下面走来看一下这个user是不是已经就拿到这个user了就是我们前面在拦截器中所放到我们的本地线程中的啊这样的一个对象那么就拿到了
[01:48] 那么这样的话其实跟我们之前的这个业务逻辑呢就完全一致了啊只是说我们把这个优惠对象的一个获取呢是放到我们拦截器中的做一个统一的这样的一个处理那么显然是OK那么可能这块在上传啊会有点问题吧那我们这个就不用去关注它了因为我们之前是不是已经测试过了对吧测试过了这个是OK的啊好那么
[02:13] 好那么接下来呢我们就来测试一下当我们去标记为是一个什么unassertion的时候就是我们不需要去做一个我们这个认证的时候啊那么我们来看一下它的一个效果啊假设呢我们就是在我们的这个方法上面呢我们去加这样的一个注解那我们来看一下它呢会出现一个什么样的一个情况那么这个位置呢我们也来打一个断点啊然后呢我们把我们这个
[02:39] 把我们这个工程就是server这个工程呢重新启动一下好那我们来等待它的启动好那么现在呢就重启一起来了那么接下来我们来测试一下我们点击这个send发送那么请求呢就进入到我们的拦截器然后呢我们继续往下面走走走但是呢我们会发现并没有进入到我们这个Controller那个断点为什么呢原因是呢我们其实有加了一个redis的缓存那么其实我们
[03:08] 因为它缓冲做命中了那么我们测试的时候呢最好把它设置为什么呢False那么这样的话肯定就没问题了那么我们重新再启动一下再来测试一下好那么现在呢我们就启动起来了那么接下来我们再来做一个测试走Send呢去做一个发送请求是不是进入到我们这个拦截器然后呢我们通过哎你可以发现请求是不是进入到我们的这个Controller对吧然后呢我们再通过就会进入到我们的Service
[03:38] 继续往下面看你会发现这个这个none就是我们这个u的是不是就是为none对吧为none了那么显然呢这样的话呢就肯定会出错对吧肯定会报一个什么空子真的异常这样的一个错误了那么显然呢我们这个是不是我们这个就达到我们所
[03:57] 期望的这样的一个预期的一个效果了对吧那么如果说这个Controller的方法是不需要做认证的你就加它就OK了那么如果需要的话那就不用去加默认的都会去做一个这样的一个校验OK好
[04:12] 那么这样的话我们这个测试是不是就已经结束了对吧那么基本上还是符合我们预期的对不对只是大家在测试的时候需要注意一下就是需要把缓存要给它先关闭掉然后再做一个测试OK好那么关于我们统一处理Token的一个测试我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
private static ObjectMapper Mapper = new ObjectMapper();
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

