# 12-基于JWT的API权限校验：代码实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\12-基于JWT的API权限校验：代码实现_【海量资源尽在 ubkz.com】.mp4
- 时长 9分34秒（音频 575s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们的需求各位都已经明确了那接下来我们要做的事情就是先去改造我们登录的微服务在登录这边查询出你可以访问的所有API接口数据接着返回到JWT数据里好了在这边呢我找到我们的登录的控制器方法System下找到登录的User Controller在User Controller当中呢我们往上去找找到登录
[00:32] 那目前来说登录呢就是这样的写的里面的内容呢还是比较少比较少那我们登录成功的时候我们这边需要添加上你已经具备的就是获取到所有的获取到所有的可访问API权限好了那获取到所有可访问的API权限呢怎么做呢很简单user.getros好了我们可以放循环因为你有不同的角色有很多role
[01:06] OK角色呢我们已经全部都获取到了那不同的角色里面有不同的权限所以我们继续还要做fault循环好了这边呢就代表的是roserow打点get permissionperm那接着我们从这个里面提取只提取API权限所以permission点get tabif等于等于我们的API权限呢写过一个
[01:43] 我们基本的一个基本的一个常量啊permissionper misslnconstance打点我们的API如果你是这个类型的我才进行统计好了比如说呢那在这边呢我可以构造一个我们叫做API全线磁波串来一个string builderSBSB等于new一个string builder好了那接着呢如果比较相同的话我就可以注意
[02:15] 我们这边呢是用的是全线标识的形式来比较的所以我addadd的其实就是他这个标识打点叫做getcode好了继续打点addappendappend我们来一个逗号分隔其实就可以了好了那这样一来我们的全新字符串已经有了那接着来把这个全新字符串可以给他放到我们的JWT数据当中我们就可以map打点put好了map打点put放一个字符串吧就叫perms
[02:45] 算了叫APS吧APS好了那这是我们的一个字符串就是sb.toStream是因为我们一会做的是一个简单的验证啊所以我这边什么逗号多一个逗号少一个逗号其实无所谓我一会看一下包含是否包含就行了OK那这样一来呢我已经构造出了我们登录的这个方法也已经给他补充完整添加了他可访问的API全线字符串
[03:21] 好了那这个可访问的API全新的词幅串我们给它添加好那添加好了之后接下来我们关注的就是如何在拦截器当中获取并且比较也就是我们这张图里面画的第二件事请求过来我要在拦截器里面解析解析之后要能得到你的所有权限好了我们找到刚才写好的拦截器common bar下找到拦截器interceptor
[03:49] JWT Interceptor那找到拦截器之后我们在这个里面关注的其实就是看权限了ClamS里面有所有数据我们可以通过ClamS好了这边就是通过CLAAMS获取到当前用户可访获取到当前用户的可访问API权限API权限自动创好了那如何做不难ClamS打点
[04:22] get 那我们刚才存的key叫做APIS那我这边直接就是APIS拿到好了那他来到的是得到的是一个字符串我就来一个APIS的一个字符串这边呢做一个强制转型OK好了那接下来呢第二件事就是说啊你得到的这个APIS他这个字符串形式可能是这样的就是API-比如说呢user-delete当然我是举例比如呢API-user-我们叫做update
[04:53] 那可能得到是这么一个字符串那针对这个字符串你有这么多你当前访问的这个接口究竟叫什么究竟是什么咱们不清楚啊所以我们需要把你当前访问的这个接口给他找出来给他搞明白他究竟是哪个接口我们要搞清楚那并且呢你这个接口它的名称必须要跟我们全线的数据库标数据库里面记录的全线标识是不是要一致啊
[05:20] 我们这边权限标识里面呢如果说只看3你会发现有一个删除用户角色删除用户的API那这些权限标识都应该要匹配上才对呀所以呢接下来我们要做的时候希望各位要注意那我应该如何去做呢其实我们这边呢很简单比如说呢我一会儿想让他访问一下用户删除的这个接口叫做delete那用户删除接口我们上面是不是写了一个request mapping啊
[05:54] 那这个request mapping可以配置一个Name属性那这个Name属性其实指的是当前这个接口你可以给它起一个名称那我们这个名称是不是就可以跟你这个删除用户这个叫用户啊跟你这个叫做删除用户的API是不是可以给它绑定到一起是不是就可以了OK那好了这边Ctrl C给它拷过来好了Ctrl C这个拷的是标志啊Ctrl C给它拷过来OK
[06:29] 那接下来我们的拦截器里面就可以通过request mapping得到你当前的名称那接着我们来判断一下当前的名称是否在你的权限列表当中是不是就有了如果在权限列表继续往下执行如果不在返回你没有权限不就可以了那接着我们如何去做好了这边需要通过反射通过哎错了通过我们这个handler我们的
[07:01] 拦截器方法request response三个参数还有一个handler那handler指的是一个叫做handler method那这个呢其实可以对它做一个简单的强制转型就能够拿到我们当前访问方法上面的注解并且获得里面的属性OK那我们需要对handler做一个强制转型handler method它是Sprite VC的一个对象handler就叫H吧它就等于这边做一个强制转型handler
[07:35] 那有了之后呢接下来呢我们就可以通过这个handler method指的是我接下来要执行的方法其实说白了它得到的就是我们要执行的这个delay的方法如果你按上它那就是这个接口delay方法那么可以通过这个方法得到这个mapping那如何做也不难H打点叫做getgetmethod annotation那这个annotation就是当前method的方法上有什么我们是不是有一个request mapping啊
[08:06] 所以这边写的就是request mapping打点class那这样一来它就能够得到你当前执行切口方法上面的这个request mapping注解那得到注解我们是不是可以通过注解打点name得到注解上面的名称OK好了那这个handle获取到了之后接着来我们通过handle method获取我们接口上的request
[08:34] MAPPNJ注解那接着拿到注解我们可以获取当前当前请求当前请求接口中的叫做NAME属性好了这些都有的话那我们需要做一个比较判断当前用户是否具有相应的请求权限那怎么判断呢这边呢就做一个稍微简单的EIF我们APS
[09:10] 有所有的权限打点content如果包含你这个name那这样一来我就继续往下执行那如果不包含我就等着出错了OK好了这个就是我们整个的一个代码的层面上的一个编写OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
    //2.调用Service更新
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

