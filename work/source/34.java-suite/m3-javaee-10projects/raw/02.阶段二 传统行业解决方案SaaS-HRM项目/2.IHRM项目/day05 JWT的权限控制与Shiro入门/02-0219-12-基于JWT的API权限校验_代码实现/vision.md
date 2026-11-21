# 画面线理解：12-基于JWT的API权限校验：代码实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\12-基于JWT的API权限校验：代码实现_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:19, 00:52, 01:10, 01:37, 02:11, 02:27, 03:33, 04:24, 05:20, 05:52, 07:20, 07:55, 08:20, 09:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:15:05

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过拦截器（Interceptor）为用户登录成功后动态获取并设置其可访问的 API 权限，并在后续请求中通过拦截器验证权限。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `SystemApplication.java` 启动类，配置了 `@SpringBootApplication` 和 `@EntityScan`，并注册了 `IdWorker`、`JwtUtils`、`OpenEntityManagerInViewFilter` 等 Bean。
画面2：展示 `UserController.java` 中的 `login` 方法，用于处理用户登录，验证手机号和密码，登录成功后返回 `Result` 对象。
画面3：在 `login` 方法中，登录成功后，开始为用户构建可访问的 API 权限集合。
画面4：在 `login` 方法中，通过 `for (Role role : user.getRoles())` 遍历用户角色。
画面5：在 `login` 方法中，通过 `for (Permission perm : role.getPermissions())` 遍历角色下的权限。
画面6：在 `login` 方法中，判断权限类型是否为 `PERMISSION_API`。
画面7：在 `login` 方法中，使用 `StringBuilder` 拼接所有符合条件的 API 权限码。
画面8：在 `login` 方法中，将拼接好的权限码字符串赋值给 `map.put("apis", sb.toString());`。
画面9：切换到数据库管理工具，展示查询用户权限的 SQL 语句，用于验证权限数据。
画面10：展示 `UserController.java` 中的 `update` 和 `delete` 方法，用于更新和删除用户。
画面11：切换到 `JwtInterceptor.java`，展示拦截器的 `preHandle` 方法，用于在请求处理前进行权限验证。
画面12：在 `preHandle` 方法中，通过 `StringUtils.isEmpty(authorization)` 判断请求头中是否包含 `Authorization`。
画面13：在 `preHandle` 方法中，通过 `claims.get("apis")` 获取用户权限码字符串。
画面14：在 `preHandle` 方法中，通过 `request.setAttribute("user_claims", claims);` 将权限信息设置到请求中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import ...
@SpringBootApplication(scanBasePackages = "com.ihrm")
@EntityScan(value="com.ihrm.domain.system")
public class SystemApplication {
    //启动方法
    public static void main(String[] args) { SpringApplication.run(SystemApplication.class,args); }
    @Bean
    public IdWorker idWorker() { return new IdWorker(); }
    @Bean
    public JwtUtils jwtUtils() { return new JwtUtils(); }
    @Bean
    public OpenEntityManagerInViewFilter openEntityManagerInViewFilter() {
        return new OpenEntityManagerInViewFilter();
    }
}
```

画面2：
```java
@PostMapping(value = "/login", method = RequestMethod.POST)
public Result login(@RequestBody Map<String, String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    User user = userService.findByMobile(mobile);
    //登录失败
    if(user == null || !user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEPASSWORDERROR);
    } else {
        //登录成功
        //获取到所有的可访问API权限
    }
}
```

画面3：
```java
//登录成功
//获取到所有的可访问API权限
for (Role role : user.getRoles()) {
```

画面4：
```java
for (Permission perm : role.getPermissions()) {
```

画面5：
```java
if(perm.getType() == PermissionConstants.PERMISSION_API) {
```

画面6：
```java
StringBuilder sb = new StringBuilder();
for (Role role : user.getRoles()) {
    for (Permission perm : role.getPermissions()) {
        if(perm.getType() == PermissionConstants.PERMISSION_API) {
            sb.append(perm.getCode()).append(",");
        }
    }
}
```

画面7：
```java
StringBuilder sb = new StringBuilder();
for (Role role : user.getRoles()) {
    for (Permission perm : role.getPermissions()) {
        if(perm.getType() == PermissionConstants.PERMISSION_API) {
            sb.append(perm.getCode()).append(",");
        }
    }
}
```

画面8：
```java
Map<String, Object> map = new HashMap<>();
map.put("company_id", user.getCompanyId());
map.put("company_name", user.getCompanyName());
String token = jwtUtils.createJwt(user.getId(), user.getUsername(), map);
return new Result(ResultCode.SUCCESS, token);
```

画面9：
```sql
SELECT u.mobile, u.password, u.name, u.id, u.role_id, u.company_id, u.status, u.create_time, u.update_time
FROM sys_user u, pt_role r, pt_user_role ur
WHERE u.id = ur.user_id AND r.id = ur.role_id AND r.status = 1 AND u.status = 1
```

画面10：
```java
@RequestMapping(value = "/user/{id}", method = RequestMethod.PUT)
public Result update(@PathVariable(value = "id") String id, @RequestBody User user) {
    //1.验证修改的用户id
    user.setId(id);
    //2.调用service更新
    userService.update(user);
    return new Result(ResultCode.SUCCESS);
}

@RequestMapping(value = "/user/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(value = "id") String id) {
    userService.deleteById(id);
    return new Result(ResultCode.SUCCESS);
}
```

画面11：
```java
@Override
public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
    //1.判断请求头中是否包含Authorization
    String authorization = request.getHeader("Authorization");
    if(StringUtils.isEmpty(authorization) || !authorization.startsWith("Bearer ")) {
        throw new CommonException(ResultCode.UNAUTHENTICATED);
    }
    //2.解析token获取claims
    String token = authorization.replace("Bearer ", "");
    Claims claims = jwtUtils.parseJwt(token);
    //3.通过claims获取当前用户的可访问API权限特点
    String apis = (String) claims.get("apis"); //api-user-delete,api-user-update
    //4.获取当前请求的RequestMapping注解
    HandlerMethod h = (HandlerMethod) handler;
    RequestMapping annotation = h.getMethodAnnotation(RequestMapping.class);
    String name = annotation.name();
    //5.判断当前用户是否有该请求的权限
    if(!apis.contains(name)) {
        throw new CommonException(ResultCode.UNAUTHENTICATED);
    }
    //6.将claims设置到request中
    request.setAttribute("user_claims", claims);
    return true;
}
```

画面12：
```java
String authorization = request.getHeader("Authorization");
if(StringUtils.isEmpty(authorization) || !authorization.startsWith("Bearer ")) {
```

画面13：
```java
String token = authorization.replace("Bearer ", "");
Claims claims = jwtUtils.parseJwt(token);
String apis = (String) claims.get("apis"); //api-user-delete,api-user-update
```

画面14：
```java
RequestMapping annotation = h.getMethodAnnotation(RequestMapping.class);
String name = annotation.name();
if(!apis.contains(name)) {
    throw new CommonException(ResultCode.UNAUTHENTICATED);
}
request.setAttribute("user_claims", claims);
return true;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
