# 15-Shiro结合redis的统一会话管理：测试与总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\15-Shiro结合redis的统一会话管理：测试与总结_【海量资源尽在 ubkz.com】.mp4
- 时长 7分0秒（音频 420s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了我们把这个自定义的整合的过程的配置全部都写好了那接下来我们就可以做测试了那我们在做测试的逻辑现在其实就变成了这样当我用户登录了之后是不是调用这种方法去存放安全数据那这个时候如果说你要把数据放到Redis里面借助了我们刚才Sheryl跟Redis整合的插件包的话那你这个安全数据需要实现一个接口
[00:28] 那实现什么接口注意我们一起来看一下我们这个任务域里面要往这回redis里要存安全数据那么安全数据第一个值就是user那这是一个对象user对象那这回这个user对象需要去实现一个接口那继续实现的接口叫什么叫做also catch possible好了那接下来呢我们去实现接口实现接口当中一个方法这个方法里面的内容返回none其实就可以了
[00:57] 那这个玩意是干什么呢我给各位也写到这边是我们Redis和Sherlock插件包提供的一个接口实现这个接口主要目的是干什么如果你实现这个接口其实就能把数据存到Redis里面就这个意思当然了里面有一个方法就是说你往这个Redis里面存放的时候你可以指定它的key是什么OK当然你不指定它有自己的默认值我们不需要关注了
[01:30] 好了那这样一来呢我们这样的整个的流程其实就已经写好了但是为了让我这个代码看起来更加好看一些或者更加易于我们的测试我在user Controller登录成功之后注意user Controller进行登录登录成功之后我想要打印一下我的session id因为别忘了我们这边已经把session id是不是给它放到了我们的请求头里面呀
[02:00] 那我们一会要进行测试的时候就需要往请求头里面放置一个session id那这个session id呢我们就可以把它打印出来来看一下我们的效果哎其实就可以了好了在登录这边如何获取session id注意这一回这个session是我们自己控制的那我们就不能想当然的什么http session那我们怎么办好了获取session那获取的session我们借助subject来做
[02:32] subjectsub这一ctsubject打点它有一个方法叫做get session打点get id就能得到我们的session id的这个值当然了我把这个值呢其实也返回回去就可以了sid等于加上好了返回给我们的响应ok那好了这样一来呢我们把这个代码呢基本上都已经改造好了
[03:13] 改造好了之后我在这边呢重新启动一下我们的服务OK重启这边不管了接着呢我们打开注意这个测试呢为了让它测试的更加好看一些啊我打开浏览器在浏览器这边发送一个请求得到数据那接着我们通过postman发送请求以这种形式来看因为我们都知道这样一来其实就是两个session那两个session他们之间肯定没有任何的一个关联
[03:42] 没错吧那我只需要在这个第二个里面第一个里面登录登录了之后把30ID放到第二个的请求头里面我看一下第二个能不能执行成功那如果能够执行成功其实就已经说明我们已经完成了相应的这个操作了好了在这边呢我们先去发送一个登录Ctrl CCtrl V我就用李四了那注意各位跟我一起来看一下我的Redis现在Redis数据全部都是空那我一点登录
[04:14] 它认证经过认证之后是不是要放到Redis的数据库里所以各位来走这边告诉我登录成功并且Session ID已经有了那么来看一下Redis服务器好了刷新一把你会发现有了这么一条数据有了这么一条数据当然这些数据是啥因为这个桌面软件其实不太智能它就显示成这样了二进制那我这边也就不关注了咱们已经注意到了我们已经把认证数据存放到Redis当中了
[04:44] 那好了接下来呢第二件事就是我们需要做一个验证那验证一下当前李斯这个人有没有访问权限那我们都知道我这边打开postman进行访问的时候由于我postman这边没有进行登录没登录呢所以我一点send他应该便告诉我未登录走未登录那如果说我不小心我加上了一个注意加上了一个请求头那这个请求头呢名字
[05:13] 我们来验证一下名字请求头的名称是不是他呀Session Manager请求头Also Renation没错那所以请求头就叫Also Renation那这个Value注意我们Value刚才就是他Also Renation靠过来不小心给删除了好了Value就是什么什么8A72浏览器里边8A72没问题那注意这一回我带了我们的请求头那这个请求头经过验证之后是不是就已登录
[05:47] 但是这个人没权限是不是应该给我返回一个未授权这么一句话呀那我们一起来看一下走给我来看那这样一来其实就已经验证了我刚才说的那句话我们已经登录登录成功把数据放到Redis那如果需要授权的地方那需要授权的地方其实就是根据你请求头里面的Session ID从Redis里面找找到了之后再去给你进行权限的验证的这么一个操作
[06:16] OK那这样一来呢我们整个的这个share基本的这个课程就已经跟各位都聊过了我们刚才一起看了一下我们如何在Springboard当中去使用share在Springboard当中如何完成最基本的认证完成最基本的授权以及咱们一个密码的一个加密的这么一个过程也看了一下对于share当中的绘画管理那share当中绘画管理其实我们可以借助它的一些机制把绘画存放到ready当中
[06:45] 那存放到ready当中那这样一来其实我们的绘画就变成了分布式那这样一来可以满足我们的我们叫做分布式应用也可以满足我们微服务应用共享redis里面的存储数据

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示基于 Shiro 框架的用户认证流程，包括自定义 Realm、用户实体类、登录控制器、Session 管理及前后端交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 Shiro 认证流程图，包括拦截器、CustomRealm、Subject、数据库等组件及其交互关系。
画面 2：展示 User 实体类代码，定义了用户表结构和角色关联。
画面 3：展示 User 实体类代码，添加了 AuthCachePrincipal 实现和 getAuthCacheKey 方法。
画面 4：展示 CustomRealm.java 中的 doGetAuthenticationInfo 方法，用于获取用户凭证并验证。
画面 5：展示 UserController.java 中的 login 方法，处理用户登录请求并调用 Subject.login。
画面 6：展示 Subject 类的 API 文档，说明其用于操作用户认证信息。
画面 7：展示 Subject 类的 API 文档，说明其用于操作用户会话。
画面 8：展示 UserController.java 中的 login 方法，调用 subject.login 进行登录。
画面 9：展示 Postman 中的登录请求，设置 Authorization 头。
画面 10：展示浏览器中登录页面，输入用户名和密码。
画面 11：展示浏览器中登录成功后的页面，显示 session ID。
画面 12：展示 IDEA 控制台日志，显示 Shiro 启动和数据库查询日志。
画面 13：展示 Postman 中的登录请求，设置 Authorization 头。
画面 14：展示 PPT 页面，介绍 Shiro 的 SessionManager 和 show 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
/**
 * 用户实体类
 */
@Entity
@Table(name = "pe_user")
@Getter
@Setter
public class User implements Serializable {
    private static final long serialVersionUID = 4297464181093870382L;
    // ID
    @Id
    private String id;
    private String username;
    private String password;
    @ManyToMany(fetch = FetchType.EAGER)
    @JoinTable(name="pe_user_role", joinColumns={@JoinColumn(name="user_id", referencedColumnName="id")},
    inverseJoinColumns={@JoinColumn(name="role_id", referencedColumnName="id")})
    private Set<Role> roles = new HashSet<>();//用户与角色  多对多
}
```

画面 3：
```java
/**
 * 用户实体类
 */
@Entity
@Table(name = "pe_user")
@Getter
@Setter
public class User implements Serializable, AuthCachePrincipal {
    private static final long serialVersionUID = 4297464181093870382L;
    // ID
    @Id
    private String id;
    private String username;
    private String password;
    @ManyToMany(fetch = FetchType.EAGER)
    @JoinTable(name="pe_user_role", joinColumns={@JoinColumn(name="user_id", referencedColumnName="id")},
    inverseJoinColumns={@JoinColumn(name="role_id", referencedColumnName="id")})
    private Set<Role> roles = new HashSet<>();//用户与角色  多对多
    @Override
    public String getAuthCacheKey() {
        return null;
    }
}
```

画面 4：
```java
protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) {
    UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
    String username = upToken.getUsername();
    String password = new String(upToken.getPassword());
    //2.根据用户名查询数据库
    User user = userService.findByName(username);
    //3.判断用户是否存在且密码是否一致
    if(user == null && user.getPassword().equals(password)) {
        //如果一致，返回用户信息
        SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(user, user.getPassword(), getName());
        return info;
    }
    //4.不一致，返回null（抛出异常）
    return null;
}
```

画面 5：
```java
//用户登录
@RequestMapping(value="/login")
public String login(String username, String password) {
    try {
        password = new Md5Hash(password, username, hashIterations: 3).toString();
        //1.获得subject
        Subject subject = SecurityUtils.getSubject();
        //2.用subject进行登录
        subject.login(upToken);
        return "登录成功";
    } catch (Exception e) {
        e.printStackTrace();
        return "用户名或密码错误";
    }
}
//登录成功后，打印所有session内容
@RequestMapping(value="/show")
public String show(HttpSession session) {
    Enumeration<?> enumeration = session.getAttributeNames();
    while (enumeration.hasMoreElements()) {
        //...
    }
}
```

画面 6：
```java
//使用subject进行登录
subject.login(upToken);
return "登录成功";
```

画面 7：
```java
//使用subject进行登录
subject.login(upToken);
return "登录成功";
```

画面 8：
```java
//用户登录
@RequestMapping(value="/login")
public String login(String username, String password) {
    try {
        password = new Md5Hash(password, username, hashIterations: 3).toString();
        //1.获得subject
        Subject subject = SecurityUtils.getSubject();
        //2.用subject进行登录
        subject.login(upToken);
        return "登录成功";
    } catch (Exception e) {
        e.printStackTrace();
        return "用户名或密码错误";
    }
}
//登录成功后，打印所有session内容
@RequestMapping(value="/show")
public String show(HttpSession session) {
    Enumeration<?> enumeration = session.getAttributeNames();
    while (enumeration.hasMoreElements()) {
        //...
    }
}
```

画面 12：
```
2018-12-07 21:57:27,258 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.Controller.UserController.getUser(Long)
2018-12-07 21:57:27,262 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.Controller.UserController.getUser(Long)
2018-12-07 21:57:27,318 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.Controller.UserController.getUser(Long)
2018-12-07 21:57:27,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.Controller.UserController.getUser(Long)
2018-12-07 21:58:16,087 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.Controller.UserController.getUser(Long)
2018-12-07 21:58:16,676 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.Controller.UserController.getUser(Long)
2018-12-07 21:58:16,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.Controller.UserController.getUser(Long)
2018-12-07 21:58:16,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.Controller.UserController.getUser(Long)
2018-12-07 21:58:16,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.Controller.UserController.getUser(Long)
2018-12-07 21:58:16,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.Controller.UserController.getUser(Long)
2018-12-07 21:58:16,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.Controller.UserController.getUser(Long)
2018-12-07 21:58:16,752 INFO 6628 [main] org.springframework.web.servlet.DispatcherServlet: Mapped ["/user/{id}"] onto public java.lang.String com.itheima.shiro.Controller.UserController.getUser(Long)
2018-12-07 21:

