# 画面线理解：22-SasSHRM中基于shiro的认证授权：测试认证

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\22-SasSHRM中基于shiro的认证授权：测试认证_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:55, 01:18, 02:09, 02:48, 03:40, 04:16, 04:28, 04:40, 05:16, 05:42, 07:14, 07:51, 08:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:41:55

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 Shiro 权限框架，实现基于 JWT 的用户认证与权限控制，包括控制器、Realm、配置类和自定义 SessionManager 的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示项目结构，选中 UserController.java，展示其 profile 接口的原始实现，使用 HttpServletRequest 获取用户信息。
画面 2: 切换到 UserRealm.java，展示 Shiro Realm 的实现，用于认证和授权，包含用户密码验证和权限设置。
画面 3: 在 UserController.java 中，将 HttpServletRequest 替换为 SecurityUtils.getSubject()，开始使用 Shiro 获取用户信息。
画面 4: 在 UserController.java 中，继续使用 Shiro 获取用户信息，代码逻辑与画面 3 类似，但注释更详细。
画面 5: 切换到 BaseController.java，展示一个基础控制器，用于设置请求参数和获取用户信息。
画面 6: 在 BaseController.java 中，展示如何使用 Shiro 获取用户信息，代码逻辑与画面 5 类似。
画面 7: 在 BaseController.java 中，继续展示使用 Shiro 获取用户信息，代码逻辑与画面 6 类似。
画面 8: 在 BaseController.java 中，展示 Spring AOP 相关的注解和类，如 @ThisTargetAnnotationPointcut。
画面 9: 在 BaseController.java 中，展示 IDE 的自动补全功能，提示 ProfileResult 类的 get 方法。
画面 10: 显示一个加载动画界面，提示“Launching escape pods...”，可能是系统启动或测试环境加载。
画面 11: 显示 Postman 的界面，准备发送 HTTP 请求。
画面 12: 显示 ShiroConfiguration.java 的代码，配置 ShiroFilterFactoryBean，设置登录和未授权 URL。
画面 13: 显示 CustomSessionManager.java 的代码，自定义 SessionManager，从请求头中提取 JWT 并设置 session。
画面 14: 在 Postman 中，发送 POST 请求到 /sys/profile，请求头包含 Authorization: Bearer xxx，返回 JSON 数据，包含用户信息和权限。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@RequestMapping(value="/profile",method = RequestMethod.POST)
public Result profile(HttpServletRequest request) throws Exception {
    String userid = claims.getDid();
    //获取用户信息
    User user = userService.findById(userid);
    //根据不同用户级别获取用户权限
    ProfileResult result = null;
    if("user".equals(user.getLevel())) {
        result = new ProfileResult(user);
    }else {
        Map map = new HashMap();
        if("coAdmin".equals(user.getLevel())) {
            map.put("enVisible","1");
        }
        List<Permission> list = permissionService.findAll(map);
        result = new ProfileResult(user,list);
    }
    return new Result(ResultCode.SUCCESS,result);
}
```

画面 2:
```java
import java.util.List;
import java.util.Map;

public class UserRealm extends IhmRealm {

    @Autowired
    private UserService userService;

    @Autowired
    private PermissionService permissionService;

    //认证方法
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
        String mobile = upToken.getUsername();
        String password = new String(upToken.getPassword());
        User user = userService.findByMobile(mobile);
        if(user != null && password.equals(password)) {
            ProfileResult result = null;
            if("user".equals(user.getLevel())) {
                result = new ProfileResult(user);
            }else {
                Map map = new HashMap();
                if("coAdmin".equals(user.getLevel())) {
                    map.put("enVisible","1");
                }
                List<Permission> list = permissionService.findAll(map);
                result = new ProfileResult(user,list);
            }
            return new SimpleAuthenticationInfo(user, password, getName());
        }
        return null;
    }
}
```

画面 3:
```java
@RequestMapping(value="/profile",method = RequestMethod.POST)
public Result profile(HttpServletRequest request) throws Exception {
    //获取session中的安全数据
    Subject subject = SecurityUtils.getSubject();
    //1.subject获取所有的安全数据集合
    PrincipalCollection principals = subject.getPrincipals();
    //2.获取安全数据
    ProfileResult result = null;
    String userid = claims.getDid();
    //获取用户信息
    User user = userService.findById(userid);
    //根据不同用户级别获取用户权限
    if("user".equals(user.getLevel())) {
        result = new ProfileResult(user);
    }else {
        Map map = new HashMap();
        if("coAdmin".equals(user.getLevel())) {
            map.put("enVisible","1");
        }
        List<Permission> list = permissionService.findAll(map);
        result = new ProfileResult(user,list);
    }
    return new Result(ResultCode.SUCCESS,result);
}
```

画面 4:
```java
@RequestMapping(value="/profile",method = RequestMethod.POST)
public Result profile(HttpServletRequest request) throws Exception {
    //获取session中的安全数据
    Subject subject = SecurityUtils.getSubject();
    //1.subject获取所有的安全数据集合
    PrincipalCollection principals = subject.getPrincipals();
    //2.获取安全数据
    ProfileResult result = null;
    String userid = claims.getDid();
    //获取用户信息
    User user = userService.findById(userid);
    //根据不同用户级别获取用户权限
    if("user".equals(user.getLevel())) {
        result = new ProfileResult(user);
    }else {
        Map map = new HashMap();
        if("coAdmin".equals(user.getLevel())) {
            map.put("enVisible","1");
        }
        List<Permission> list = permissionService.findAll(map);
        result = new ProfileResult(user,list);
    }
    return new Result(ResultCode.SUCCESS,result);
}
```

画面 5:
```java
public class BaseController {
    protected HttpServletRequest request;
    protected HttpServletResponse response;
    protected String companyId;
    protected String companyName;
    protected Claims claims;
    @ModelAttribute
    public void setReqAnReq(HttpServletRequest request,HttpServletResponse response) {
        this.request = request;
        this.response = response;
        Object obj = request.getAttribute("user_claims");
        if(obj != null) {
            this.claims = (Claims) obj;
            this.companyId = (String)claims.get("companyId");
            this.companyName = (String)claims.get("companyName");
        }
    }
}
```

画面 6:
```java
//使用 shiro获取
@ModelAttribute
public void setReqAnReq(HttpServletRequest request,HttpServletResponse response) {
    this.request = request;
    this.response = response;
    //获取session中的安全数据
    Subject subject = SecurityUtils.getSubject();
    //1.subject获取所有的安全数据集合
    PrincipalCollection principals = subject.getPrincipals();
    //2.获取安全数据
    if(principals != null && principals.isEmpty()) {
        ProfileResult result = (ProfileResult)principals.getPrimaryPrincipal();
        this.companyId = (String)result.get("companyId");
        this.companyName = (String)result.get("companyName");
    }
}
```

画面 7:
```java
//使用 shiro获取
@ModelAttribute
public void setReqAnReq(HttpServletRequest request,HttpServletResponse response) {
    this.request = request;
    this.response = response;
    //获取session中的安全数据
    Subject subject = SecurityUtils.getSubject();
    //1.subject获取所有的安全数据集合
    PrincipalCollection principals = subject.getPrincipals();
    //2.获取安全数据
    if(principals != null && principals.isEmpty()) {
        ProfileResult result = (ProfileResult)principals.getPrimaryPrincipal();
        this.companyId = (String)result.get("companyId");
        this.companyName = (String)result.get("companyName");
    }
}
```

画面 8:
```java
//使用 shiro获取
@ModelAttribute
public void setReqAnReq(HttpServletRequest request,HttpServletResponse response) {
    this.request = request;
    this.response = response;
    //获取session中的安全数据
    Subject subject = SecurityUtils.getSubject();
    //1.subject获取所有的安全数据集合
    PrincipalCollection principals = subject.getPrincipals();
    //2.获取安全数据
    if(principals != null && principals.isEmpty()) {
        ProfileResult result = (ProfileResult)principals.getPrimaryPrincipal();
        this.companyId = (String)result.get("companyId");
        this.companyName = (String)result.get("companyName");
    }
}
```

画面 9:
```java
//使用 shiro获取
@ModelAttribute
public void setReqAnReq(HttpServletRequest request,HttpServletResponse response) {
    this.request = request;
    this.response = response;
    //获取session中的安全数据
    Subject subject = SecurityUtils.getSubject();
    //1.subject获取所有的安全数据集合
    PrincipalCollection principals = subject.getPrincipals();
    //2.获取安全数据
    if(principals != null && principals.isEmpty()) {
        ProfileResult result = (ProfileResult)principals.getPrimaryPrincipal();
        this.companyId = (String)result.get("companyId");
        this.companyName = (String)result.get("companyName");
    }
}
```

画面 12:
```java
@Bean
public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) {
    //1.设置安全管理
