# 画面线理解：14.统一处理token（功能实现）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\14.统一处理token（功能实现）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 01:42, 02:32, 03:24, 04:36, 05:14, 07:05, 09:56, 11:00, 11:38, 12:23, 13:06, 13:47, 14:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:42:30

1) 这一组画面整体在讲如何通过自定义拦截器（TokenInterceptor）结合 ThreadLocal 实现用户身份在请求链路中的传递与校验。

2) 按时间顺序列出每张画面的要点：
画面1：展示 MovementsController 中的 saveMovements 方法，接收文本内容、位置、图片等参数，并调用 movementsService 保存，最后返回 ResponseEntity.ok(null)。
画面2：展示 UserThreadLocal 类的初始定义，准备添加私有成员变量。
画面3：在 UserThreadLocal 类中定义了 ThreadLocal<User> 的静态变量 LOCAL。
画面4：展示 UserThreadLocal 类的完整结构，包含 set 和 get 方法，用于在当前线程中存储和获取用户对象。
画面5：展示 TokenInterceptor 类的初始结构，继承 HandlerInterceptor，包含 preHandle 方法。
画面6：在 TokenInterceptor 中，开始编写 preHandle 方法，准备获取请求头中的 token。
画面7：在 TokenInterceptor 中，通过 userService 查询用户，若用户为空则返回 401 状态码。
画面8：在 TokenInterceptor 中，将查询到的用户对象通过 UserThreadLocal.set(user) 存入当前线程。
画面9：在 TokenInterceptor 中，判断当前请求的方法是否包含 @NoAuthorization 注解，若包含则跳过拦截。
画面10：在 TokenInterceptor 中，通过反射获取方法上的 @NoAuthorization 注解。
画面11：在 MovementsController 中，将 saveMovements 方法改为 try-catch 结构，捕获异常并打印堆栈，最后返回 500 状态码。
画面12：展示 MovementsService 类，包含 @Reference 注解的 QuanZhiApi 和 @Autowired 注解的 picUploadService。
画面13：展示 TodayBestController 中的 queryTodayBest 方法，调用 todayBestService。
画面14：展示 day03.md 文档中关于使用 ThreadLocal 的代码片段，其中 User user = UserThreadLocal.get(); 用于获取当前线程中的用户对象。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
> saveMovements(@RequestParam("textContent") String textContent,
@RequestParam("Location") String location,
@RequestParam("Longitude") String longitude,
@RequestParam("Latitude") String latitude,
@RequestParam("ImageContent") MultipartFile[] multipartFile,
@RequestHeader("Authorization") String token) {
s.movementsService.saveMovements(textContent, location, longitude, latitude, multipartFile, token);
eEntity.ok(null);
```

画面2：
```java
package com.tanhua.server.utils;
public class UserThreadLocal {
private :
```

画面3：
```java
private static final ThreadLocal<User> LOCAL = new ThreadLocal<>();
```

画面4：
```java
package com.tanhua.server.utils;
import com.tanhua.server.pojo.User;
public class UserThreadLocal {
private static final ThreadLocal<User> LOCAL = new ThreadLocal<>();
private UserThreadLocal() {
}
public void set(User user) {
LOCAL.set(user);
}
public User get() {
return LOCAL.get();
}
```

画面5：
```java
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
@Component
public class TokenInterceptor implements HandlerInterceptor {
@Override
public boolean preHandle(HttpServletRequest request, HttpServletResponse response) {
request.getHeader();
return false;
}
```

画面6：
```java
import javax.servlet.http.HttpServletResponse;
@Component
public class TokenInterceptor implements HandlerInterceptor {
@Override
public boolean preHandle(HttpServletRequest request, HttpServletResponse response) {
return false;
}
```

画面7：
```java
@Component
public class TokenInterceptor implements HandlerInterceptor {
@Autowired
private UserService userService;
@Override
public boolean preHandle(HttpServletRequest request, HttpServletResponse response) {
String token = request.getHeader("Authorization");
User user = this.userService.queryUserByToken(token);
if(null == user) {
response.setStatus(401); //无权限
return false;
}
// 存储到当前的线程中
UserThreadLocal.set(user);
return true;
}
```

画面8：
```java
@Component
public class TokenInterceptor implements HandlerInterceptor {
@Autowired
private UserService userService;
@Override
public boolean preHandle(HttpServletRequest request, HttpServletResponse response) {
String token = request.getHeader("Authorization");
User user = this.userService.queryUserByToken(token);
if(null == user) {
response.setStatus(401); //无权限
return false;
}
// 存储到当前的线程中
UserThreadLocal.set(user);
return true;
}
```

画面9：
```java
@Override
if(handler
```

画面10：
```java
@Override
if(handler
```

画面11：
```java
@RequestBody
public ResponseEntity<Void> saveMovements(@RequestParam("textContent") String textContent,
@RequestParam("location") String location,
@RequestParam("longitude") String longitude,
@RequestParam("latitude") String latitude,
@RequestParam("imageContent") MultipartFile[] multipartFile,
@RequestHeader("Authorization") String token) {
try {
Boolean bool = this.movementsService.saveMovements(textContent, location, longitude, latitude, multipartFile, token);
if (bool) {
return ResponseEntity.ok(null);
}
} catch (Exception e) {
e.printStackTrace();
}
return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面12：
```java
@Service
public class MovementsService {
@Reference(version = "1.0.0")
private QuanZhiApi quanZhiApi;
@Autowired
private PicUploadService picUploadService;
```

画面13：
```java
roller {
ce todayBestService;
}
TodayBest() {
estService.queryTodayBest();
}
ation")
yRecommendUserList(RecommendUserQueryParam queryParam, @RequestHeader("Authorization") String token) {
estService.queryRecommendUserList(queryParam, token);
```

画面14：
```java
public boolean savePublish(String textContent,
String location,
MultipartFile[] multipartFile) {
//获取当前的登录信息
User user = UserThreadLocal.get();
Publish publish = new Publish();
publish.setUserId(user.getId());
publish.setText(textContent);
publish.setLocationName(location);
publish.setSeeType(1);
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面14：PPT标题为“2.3.5. 使用 ThreadLocal”，内容为代码片段，展示如何通过 ThreadLocal 获取当前线程中的用户对象。

5) 不要评价画面美观，不要输出与课程无关的内容。
