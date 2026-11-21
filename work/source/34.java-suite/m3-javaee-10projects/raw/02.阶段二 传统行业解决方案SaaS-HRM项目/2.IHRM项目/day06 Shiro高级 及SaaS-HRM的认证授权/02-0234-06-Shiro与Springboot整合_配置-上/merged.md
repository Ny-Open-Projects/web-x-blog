# 06-Shiro与Springboot整合：配置-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\06-Shiro与Springboot整合：配置-上_【海量资源尽在 ubkz.com】.mp4
- 时长 12分3秒（音频 723s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 好了完成了我们第一个用户登录的一个改造第二个我们自定义RAM这些代码的一个编写那接下来呢如果想要Sherlock在我们这个Spring Boot的程序当中能够正常的运行起来能够让它正常的跑起来那接下来我们要完成的其实就是一个叫做Sherlock的一个配置那Sherlock这个配置呢相对来说相对来说不难它都是比较固定的一些内容
[00:33] 那我们在Springboard当中呢其实就可以通过Configuration这个注解配置到一个类上里面一个一个的EtaBin去配种用的需要的对象其实就能跟Spring我们整合到一起那好了接下来我们来看一下如何进行它这个整合的一个配置好了我们一般配置这个配置类的时候其实就跟我们这个启动类放到一起其实就可以了好了这边呢我去创建一个Class那这Class的名称呢我跟我这边讲义保持一致了Shera Configuration
[01:03] 好了上边呢想都不要想ata configuration里面有我shadow很多所有的配置那在我们的配置过程当中在我这个配置过程当中那我遵守的逻辑究竟有什么希望各位要注意这个里面我们基础用到的对象一共就这么几个首先呢第一个我们叫做创建room交给Spring容器来进行管理好了第二个
[01:33] 那我们都知道在shareware里面它有最重要的一个叫做安全管理器所以呢我们第二步就是创建安全管理器就是进行整合把所有交给Spring来进行管理那你这个RAM要进行管理安全管理器也要进行管理那还有第三个第三个是shareware在web工程要想应用进行我们的权限控制的一个比较核心的一个一个一个对象这个对象呢叫做配置shareware过滤器好了那除了shareware
[02:10] 抱歉点错了好了那对于这个Sheryl的过滤器呢其实说的不太正常啊其实说的不太严谨其实它是一个Sheryl的一个过滤器工厂那这一个工厂里面呢可能会委托很多的过滤器来帮助或者来协调我整个代码的一个权限控制那这几个我们看过了之后当然还有最底下一个因为我们一会儿要用到Sheryl的一些注解来进行配置它的一个
[02:42] 全线的一个控制用它的注解来做那最底下呢我们还需要开启对shadow注解的一个支持那这是我们要做的这么四件事好了那首先呢我们一个一个的来看首先第一个就是自定义我们的room那自定义room很简单eta bin创建对象好了写一方法啪不立刻那我们有返回值就叫做custom room那这个名字叫什么无所谓我习惯就是get开头了
[03:14] 好了那这个里面我们返回的就是return new一个我们自己定义的cast realme对象其实就可以那这样一来它就能够创建对象放到容器当中当然了我们自己写的这convex room里面这边有一个依赖auto Service auto wear已经都配置成功了没问题那接下来就是第二个叫做创建安全管理器那创建安全管理器同样的etabin这个逻辑都是一模一样的public注意返回值security managerser
[03:46] SE 抱歉SECURITY Security ManagerMANAJR注意别选测包我们用share提供的好了接下来这边就GET我个人习惯好接下来我们这边用其实就是从Spring容器当中获取这个ROM其实就可以接着我可以把它以参数的形式传递过来然后配置都是大同小异的接下来我们这边
[04:18] 配置安全管理器那这个安全管理器那我们怎么去做呢其实得到这么一个对象就可以了那我们之前的逻辑全部都是使用的是一个default注意这边用的是一个叫做default web security manager因为我们现在是用的是一个web程序default d f d f a u l tweb security manager
[04:48] 这个是用的是我们默认的web应用程序的一个安全管理器了好了security manager等于new一个好了这个对象呢拿过来借助构造方法呢可以对它进行复制把RAM传递根据那好了这样一来呢RAM域已经有了好了那这样一来RAM域我们已经配置好了那配置好了之后接着我们底下其实就可以returnsecurity manager当然你这边如果不想用构造方法的话你不想用构造方法
[05:19] 你同时也可以通过Security Manager打点我们叫做Set Room把我们当前这个Room传递过来其实都是一样的OK那这样一来我们的Room就已经有了那为什么要这样配置是因为我们之前说过了对于Security Manager来说它管理了所有的Room所以你创建的这个安全管理器它要知道所有Room的信息OK好了那第二步也不多说了他们基本上都是大同小异的还有第三步的一个配置那第三步的一个配置A to BPublic
[05:49] 那这个呢我们叫做filter的filter工厂其实就是我们share的过滤器工厂那这个工厂的叫什么呢叫做share filter factory b好了这边呢写的稍微简单一点吧就叫share filter吧好了那我们可以通过security manager把这个security manager也传递过来ok好了那接下来在这边呢先跟各位来简单的说一下这个share的过滤器工厂
[06:26] 究竟是在做什么好了在web我们程序中share进行权限控制全部是通过它的一组过滤器集合来进行控制注意它不是一个它是一组而这些或者这一组过滤器集合我们都需要给它进行指定
[06:58] 当然了我们如何去指定这一组一组的过滤器集合或者你究竟想用哪几个过滤器那这些呢我们一会儿会为各位简单的来进行说明当然我们现在要知道它是在做什么其实就是去配置它的所有的过滤器很多
[07:16] 当然除了这里面过滤器之外还可以去指定如果说你当前没有认证也就是没登录你要跳转到哪如果说你没有进行授权你要跳转到哪所以这里面是我整个拦截以及进行页面跳转的这么一个配置我们叫做Shared Filter Factory Beam也就是我们Shared过滤器工厂那这个Shared过滤器工厂其实也需要给它配置到安全管理器当中所以我把Supply Chain Manager也传递过来了
[07:44] 那么这里面的配置步骤究竟是怎么样的我们简单的来写一下首先第一个就是创建我们的过滤器工厂好了创建好了过滤器工厂第二个就是设置我们叫做安全管理器好了接着第三个那第三个里面它有一些自己通用的一些配置那这些通用的配置指的是我们的如果说你没有登录我就没有认证没有登录或者没有认证你跳转的登录
[08:15] 页面也可以去指定它那个登录成功的页面当然也可以指定它未授权跳转的我们叫做页面好了那接着我们继续往下看第四个第四个去设置我们的过滤器一组一组的设置过滤器集合好了接着接着那我们就可以返回我们这个Sherlock Factory工厂好那接着我们来看一下如何进行配置这个配置呢相对来说有点点麻烦我们先去创建一个Sherlock Factory
[08:47] sharefilter factorybin好了这边呢我叫做filter就叫sharefilter factory吧好了等于new一个sharefilter factorybin那好了接着配置安全管理器那其实是这样的就是说呢sharefilter我们叫做拦截器我们叫做过滤器过滤器控制或者拦截到了这些我们目标的URL之后接来是不是应该交由我们security manager里面的比如说是认证
[09:19] 它里面有room那比如说有认证它里面有room可以进行认证的操作比如说受传secret manager里面是不是有room那进行授权的一些操作也就判断有没有权限所以对于我们的过滤器拦截之后它接着要做什么其实全部是在安全管理器里面有体现所以我们factory打点set securityset security manager好了把安全管理器传进去
[09:52] 好那接下来里面就是一些通用的配置比如说你可以指定它没有登录要跳转的页面打点我们可以叫做set login url你这个没登录跳转到哪当然了这边呢其实可以跳转跳转到一个我们的url地址好了那接下来呢还可以去进行设置filter打点我们叫做set on also renaissance的url就是v
[10:23] 授权或者就是我们验定权限定权限失败的这么一个页面当了这个页面呢或者是到UIL来说你想跳转到哪其实都可以当然了也可以给他跳转到我们的一个动作方法里比如呢这边呢我有一个写好的一个地址抱歉这个还没写好啊比如说我这边也写跳转到一个地址任意的一个地址里面有时候这边可以来一个atrequestmyping好了value等于随便写
[10:57] 好了比如说我就叫做also arrow就想挑团之道那怎么办public死去类型的我就叫做also arrowreturn当然了我这边的这个方法呢可以接收一个参数啊英特类型参数intercode好了我底下就可以进行判断了returncode等于等于1比如说1未登录那如果是2的话我就显示未授权
[11:35] OK那接着呢我这边要访问其实就可以让它跳转到我当前的这个界面好了那我这边可以跳转到当前的这个界面给它搭一个扣参数等于1那底下这个未授权我就可以给它跳转到还是这个页面只不过后面给它加一个2其实就可以了那我们当前的通用配置已经结束了之后接着就可以设置它这个叫做过滤器的集合

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 Spring Boot 项目中，通过自定义 Realm 和配置 Shiro 安全管理器与过滤器工厂，实现用户认证与权限控制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 UserController 中的 login 方法，使用 UsernamePasswordToken 进行登录，调用 Subject.login 方法。
- 代码：`@RequestMapping(value="/login") public String login(String username,String password) { try { UsernamePasswordToken upToken = new UsernamePasswordToken(username,password); Subject subject = SecurityUtils.getSubject(); subject.login(upToken); return "登录成功"; }catch (Exception e) { return "用户密码错误"; } }`

画面 2：
- 展示 Shiro 的核心组件 SecurityManager 的作用，并展示 ShiroConfiguration 类中配置自定义 Realm 的代码。
- 代码：`@Configuration public class ShiroConfiguration { //配置自定义的Realm @Bean public CustomRealm getRealm() { return new CustomRealm(); } }`

画面 3：
- 展示在 IntelliJ IDEA 中创建新类的对话框，准备创建 CustomRealm 类。

画面 4：
- 展示 ShiroConfiguration.java 文件，其中包含注解 @Configuration 和类定义，以及注释“1.创建 realm”、“2.创建安全管理器”、“3.配置 shiro 的过滤器”。

画面 5：
- 展示 CustomRealm.java 文件，定义了继承 AuthorizingRealm 的自定义 Realm 类，包含 setUserName 方法和授权方法 doGetAuthorizationInfo。
- 代码：`public class CustomRealm extends AuthorizingRealm { public void setUserName(String name) { super.setName("customrealm"); } @Autowired private UserService userService; protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) { //授权方法 } }`

画面 6：
- 展示在 ShiroConfiguration.java 中，为 SecurityManager 选择合适的实现类，当前选中 DefaultWebSecurityManager。

画面 7：
- 展示在 ShiroConfiguration.java 中，为 SecurityManager 选择合适的实现类，当前选中 DefaultWebSessionManager。

画面 8：
- 展示 ShiroConfiguration.java 文件，配置了 SecurityManager 和过滤器工厂。
- 代码：`@Configuration public class ShiroConfiguration { //1.创建 realm @Bean public CustomRealm getRealm() { return new CustomRealm(); } //2.创建安全管理器 @Bean public SecurityManager getSecurityManager(CustomRealm realm) { DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm); return securityManager; } }`

画面 9：
- 展示 ShiroConfiguration.java 文件，展示 Spring 的注解列表，如 @Bean、@Configuration、@Component 等。

画面 10：
- 展示 ShiroConfiguration.java 文件，开始配置 Shiro 的过滤器工厂。
- 代码：`@Bean public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) { }`

画面 11：
- 展示 ShiroFilterFactoryBean 的方法列表，如 setSecurityManager、setLoginUrl、setUnauthorizedUrl 等。

画面 12：
- 展示 ShiroConfiguration.java 文件，配置 ShiroFilterFactoryBean 的 SecurityManager、登录 URL 和未授权 URL。
- 代码：`filterFactory.setSecurityManager(securityManager); filterFactory.setLoginUrl("/login"); filterFactory.setUnauthorizedUrl("/unauthorized");`

画面 13：
- 展示 UserController.java 文件，展示 login 方法中使用了 @Value 注解注入的属性，如 subject、retu 等。

画面 14：
- 展示 ShiroConfiguration.java 文件，配置了 ShiroFilterFactoryBean 的 SecurityManager、登录 URL 和未授权 URL。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```java
//用户登录
@RequestMapping(value="/login")
public String login(String username,String password) {
    try {
        UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
        Subject subject = SecurityUtils.getSubject();
        subject.login(upToken);
        return "登录成功";
    }catch (Exception e) {
        return "用户密码错误";
    }
}
```

画面 2：
```java
@Configuration
public class ShiroConfiguration {
    //配置自定义的Realm
    @Bean
    public CustomRealm getRealm() {
        return new CustomRealm();
    }
}
```

画面 4：
```java
@Configuration
public class ShiroConfiguration {
    //1.创建 realm
    //2.创建安全管理器
    //3.配置 shiro 的过滤器
}
```

画面 5：
```java
public class CustomRealm extends AuthorizingRealm {
    public void setUserName(String name) {
        super.setName("customrealm");
    }
    @Autowired
    private UserService userService;
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        //授权方法
    }
}
```

画面 8：
```java
@Configuration
public class ShiroConfiguration {
    //1.创建 realm
    @Bean
    public CustomRealm getRealm() {
        return new CustomRealm();
    }
    //2.创建安全管理器
    @Bean
    public SecurityManager getSecurityManager(CustomRealm realm) {
        DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm);
        return securityManager;
    }
}
```

画面 10：
```java
@Bean
public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) {
}
```

画面 12：
```java
filterFactory.setSecurityManager(securityManager);
filterFactory.setLoginUrl("/login");
filterFactory.setUnauthorizedUrl("/unauthorized");
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2：
- PPT 标题：Shiro 的核心组件 SecurityManager 的作用。
- 内容：SecurityManager 是 Shiro 架构的心脏，用于协调内部的多个组件完成全部认证授权的过程。例如通过调用 realm 完成认证与登录。使用基于 Spring Boot 的配置方式完成 SecurityManager, Realm 的装配。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

