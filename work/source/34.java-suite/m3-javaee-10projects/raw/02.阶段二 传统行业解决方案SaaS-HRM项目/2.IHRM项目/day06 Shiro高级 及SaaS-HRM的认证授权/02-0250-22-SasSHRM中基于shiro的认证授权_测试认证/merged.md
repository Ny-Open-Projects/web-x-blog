# 22-SasSHRM中基于shiro的认证授权：测试认证

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\22-SasSHRM中基于shiro的认证授权：测试认证_【海量资源尽在 ubkz.com】.mp4
- 时长 8分53秒（音频 533s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 完成了share的所有配置之后那接下来呢我们就可以对它进行一个测试那么的测试的逻辑是这样的用户呢可以模拟登录进入到我们的login方法那login方法之后进入到我们的叫做自定义room那在room当中我们开始进行密码的这么一个验证那接下来呢把数据安全数据存放到我们的shareroom当中那接下来就是说认证
[00:30] 执行成功之后我们接下来呢是不是还可以进行访问当前用户的所有用户资料或者用户信息那访问用户信息的时候这个时候就疑问了那我们之前使用的逻辑是这样的这里面呢是不是叫的还是Claims获取啊那这种方式获取好像还是有点点麻烦那我们使用Share的时候其实已经把所有的用户信息全部都放到了我们的Redis服务器当中各位来看认证之后是不是就是Profile叫做Result
[00:59] 那我们只需要获取信息的时候这一些内容我们都不需要了只需要想方设法的我们叫做获取到session中的安全数据是不是就可以了那获取安全数据怎么做呢很简单security utils打点注意打点get subject这个是得到我们的用户主体那得到用户主体之后接下来我们就可以通过subject
[01:31] 获取所有的安全数据集合好了接着呢得到我们的获取安全数据那好了我们来看一下如何去做subject打点里面有个方法get par simple 私得到所有是一个集合connection好了那接下来呢我们只需要拿到里面最主要的这一个其实就可以了打点get primary par simple好了这些代码咱们之前应该都看过
[01:59] 那这样一来这个其实代表的就是我们安全数据那安全数据可以把它做一个强制转型转化成profile result即可那这样一来我们获取用户资料的这一步其实也就写好了那当然了其实有的朋友还有一些疑问就是说很多的地方我们很多的地方
[02:24] 都用到了我们叫做企业名称企业ID用户ID等等那这些内容我们之前把它抽取到了base Controller当中那抽取到base Controller当中我们之前的写法是通过解析JWT来进行获取的这些应该各位还有印象那我们现在没有JWT了我们现在用什么注意我把这个方法呢上面这个注释起来使用JWT方式获取
[02:55] 好了那接下来呢我们给他来一个新的就是使用share的方式获取好了那使用share获取result response基本上都是一模一样那接下来我们底下就是通过share那通过share跟刚才的逻辑一样我们只需要想方设法的得到company id得到company name其实就可以了那这些我们如何去获取呢其实很简单我们只需要得到安全数据跟刚才的套路是一模一样的
[03:29] 得到安全数据我们一起来找一下Ctrl C这边拿过来Ctrl VOK当然我们这边呢也可以去做一个基本的判断If POS不等于None并且POS.isEmpty就是不等于空好了那接下来呢我们在中间呢就可以获取安全数据
[04:14] 那获取到了之后对我们公共的company id和我们的company name进行复制类似点company id等于result打点get company id我们往里存放了类似点company name等于result点get company nameokget company抱歉company那这样一来我们就使用share的方式也能够获取这些基本的数据
[04:46] 好了那这些我们都写好了之后我们可以启动一下我们的服务找到我们系统v服务的启动类c system application好了走好了这边呢系统让他去启动让他去启动那接下来呢我们关注的其实就是可以做一个简单的测试了现在呢我这边启动已经启动成功了并且呢我底下已经打开了两个postman那主要问题其实就是为了防止啊
[05:19] 在一个里面呢请求会有影响好了并且呢我们这边呢已经打开了我这个redis各位可以看一下redis目前来说呢什么数据都没有那好了接下来我们就可以去做这个测试那我们的测试逻辑很简单注意我一共有两个postman第一个postman发起登录那第二个postman我在里面先去看一下能不能够访问用户信息默认肯定没登录他就不能访问不能访问代表的是不是就是让我去登录啊
[05:47] 那如果说我在投信息里面给它挂载了我们的Session ID那这样一来Session ID匹配到了我是不是就可以把我们的用户数据再给它获取出来OK那好了我们开始首先打开底稿那我们访问登录Post的方法来进行访问Localhost好了我的端口名叫做9002好了我请求的Sys-login好了加上我们的Body那在这边呢简单的设置一下
[06:19] 我们这边全部都是json的形式来做的所以我这边填写我们登录的名字登录的手机号mobile以及password好了我们这边的用户密码都是123456那接着走send好了这边告诉我其实我已经登录成功了并且返回了我们的token值好了接下来token我们已经有了那接下来注意在这边在我们的第二个postment当中我们还是去访问
[06:58] Ctrl C拿过来这边Ctrl V注意我们访问的是我们的第二个接口PRO那这个接口呢我们都知道是用来获取用户信息的那这个用户信息的接口我们再来看一下那首先呢就是在我们这边的shared pageshared page里面说过了其他的那些内容必须登录才能访问那必须登录都能访问那我第二个显然没有登录那没有登录它就会跳转到Auth arrow告诉我你需要登录才能够访问那我send一下你会发现我
[07:29] 你还未登录那这边符合我们的需求那接下来我们只需要在我访问用户信息的时候以投信息的形式把Session ID挂载上是不是就可以了那好了我们找到Header添加一个新的投信息那么投信息它的key是什么我们一起找一下好了这边呢我找到Session Manager里面咱们定义好的Bier加空格Ctrl Ccall过来Bier加空格好了那接下来呢我们的Session ID在这边呢也call一把
[08:07] Ctrl C 靠过来那对于我们这个投信息它的key或者它的名称是什么呢我们也把它拿过来好了这边呢叫做also relationOK那好了接着我们一起来试一下是否有数据走各位来看就目前而言我挂载了投信息我们的session id之后是不是就能得到我们的数据并且这也符合我们的需求好了那接下来呢有的朋友就说如果你不挂载的话我把它关掉你再走是不是就没有登录啊那这样也就意味着
[08:36] 这个符合我们刚才说的一个逻辑如果你第一次登录之后得到了session id在其他的地方如果你在投信息里面把session id挂载过去那我们就能完成用户的认证以及获取用户信息这个流程

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

