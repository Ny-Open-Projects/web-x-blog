# 07-Shiro与Springboot整合：配置-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\07-Shiro与Springboot整合：配置-下_【海量资源尽在 ubkz.com】.mp4
- 时长 8分42秒（音频 522s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了那接下来呢我们就可以去设置一下这个过滤器这些这个集合啊那对于过滤器而言呢Sheryl里面支持很多种我们可以打开讲义一起来看一下Sheryl当中的过滤器它一共有这么十个12345678910一共有这么十个那对于这十个过滤器而言我们常用的其实就有这边黑色字体显示的那首先有ANNO
[00:28] 那这个ANO它代表的什么意思它其实首先这没参数它是开放权限的那ANO代表的是你当前这个URL地址其实只要是人就能登录代表的含义匿名用户或者游客谁都能访问那接着呢还有一个叫做AUTHC那对于AUTHC它代表的含义究竟是什么它指的是修认证也就是说你要要用AUTHC这个过滤器的话你必须要先登录
[00:59] OK这两个能够理解的话接下来呢就是说还有一个叫做Promise这个Promise后面有一个中框号里面有一参数叫user这个啥意思啊这个是指的是你呢需要具有某种权限才可以访问这个地址那这个权限究竟叫什么究竟叫什么后面是你权限的一个标志比如说你定义了一个叫做user这么一个标志
[01:29] 那接下来你就是说你这个用户必须要具备user这个标志你才能访问当前拦截的这个地址那当前底下还有个叫做rosros叫做admin这个指的是你访问的这个或者你已经拦截到的这个UIL地址必须要具备admin这个角色才能进行访问OK那当然了还有一些什么logout叫做authcbase
[01:53] 还有user ssl还有这个reset和pod等等这几个由于不常用咱们可以简单的来看一下其实就可以了比如说logout它指的是注销的一个方法你如果一这个拦截这个url其实它就是在执行注销那注销之后会跳转到一个地址然后这个auth base它指的是基本的一个认证还有user表示必须存在用户
[02:16] 好了好了底下呢这边是resetreset其实就是reset风格的它里面可以指定一个方法名还有它的请求方式还有pot8081这个指的是如果不存在这个的话就跳转到这个主机的8081端口当然了这里面的内容我们不常用经常用的其实就是annoautcpromise还有这个rose好那这个呢我们简单的看了一下那接下来就是说啊
[02:42] 那你怎么就知道一个地址它执行的是ANON或者AUTHC那我们都知道过滤器它是不是需要配置你这个过滤器要拦截的地址URL地址那这个URL地址如果你配置成filter叫做ANO那也就意味着你前面配置的请求地址某某那它其实就是一个匿名登录那如果你配置这个地址叫做AUTHA那其实它代表的就是需要进行认证
[03:11] 那这个地址呢可以配置很多种那同时这边呢需要跟各位提一个醒那大家能看到我其实代表的是一个地址它具备的一个配置一个地址它具备一个配置那这个就比较明显是不是可以指定的是一个集合或者map集合那这个map的key其实代表的是你的请求地址那你的value是不是指定的它其实这个过滤器的这个类型啊
[03:34] OK那这个我们看过了之后那接下来我们回到我们的代码来看一下我们这个过滤器应该如何进行配置那我们都知道配置过滤器呢其实它其实代表的是一个MAP集合那所以我们这边可以设置所有的叫做过滤器那这个过滤器的key就是我们请求的URL地址所以所有的过滤器那我们通过的是一个MAP集合来进行控制那它的key
[04:04] 就等于我们过滤的或者拦截的UIL地址那这个value其实等于我们的过滤器类型好了这个我们看过了之后那接下来就有朋友就疑问啊就疑问就是说啊你整个过滤器这个配置有可能要对同一个UIL配置很多次所以这边我需要强调一下你有很多个过滤器
[04:35] 很多个UIL可能有相同的UIL地址那针对这些我们如何进行配置其实我们这边的MAP选择有顺序的MAP集合其实就可以了好那这边的我们这个MAP集合用的什么呢就可以用一个叫做Linked HACMAP那所以简单的把这个代码我们写一下就可以了好了MAP死菌类型的我们的UIL地址死菌类型的我们叫做过滤器的类型那好了接着来一个FilterMAP等于New一个
[05:13] new一个link的hashi map那好了这边我们可以去进行设置filter map打点我们叫做put往里面存一值比如说呢我设置的是user-home那这个user-home呢我就来一个annoanno抱歉annon说错了annon好了它代表的是当前当前请求地址
[05:53] 可以匿名访问好了那就是所有人都可以访问好了那接下来filter map打点继续put那么这边put一个user-行星AUTHC那这个代表的含义是当前我们的请求地址必须认证之后可以访问好了那接下来
[06:25] 那我们这边的过滤器集合我们还差最后一步我们只是把这个过滤器集合给它写出来了那这个过滤器如何进行应用也就需要把它配置到我们的filter当中filter factory当中进行管理filter factory打点我们叫做set filter chaindefinition mapOK接着我们return我们写好的filter factory即可那这样一来我这个工厂已经配置成功了
[06:59] 那这个工厂配置成功了之后接着就是第四步要开启对share-all-structure的一个支持那share-all-structure的这个支持呢在今天的这个资料当中啊第五天资源好了这边有个基本配置其中有一个这个文件啊这个文件我其实都已经写好了只需要我们拿到最下边的这一句话配置share-all-structure的支持把它Ctrl-Ccall过来即可
[07:29] 那这个对shadow的注解支持呢我们一般是这样配的当然了我们这个注解一会儿会用一把如果你不配这句话的话注解其实就用不了OK那这样一来我整个shadow的这个配置类其实就已经都配置好了那这里面呢我们着重的是第一个ROM要自行定义安全管理器要定义其中着重要跟我们强调一下就是安全管理器和ROM的一个关系那以及我们这个
[07:54] Sherlock的过滤器工厂那Sherlock的过滤器工厂首先各位要明白它是什么意思在web应用程序当中我们Sherlock是通过过滤性的形式对每一个UIL进行拦截那拦截到了之后根据你过滤器的配置的不同ANO或者AOTC等等等等根据这些不同的配置那它进行不同的处理如果ANO不做任何处理那如果AOTC它会进行判断看一下是否认证如果是Promise看一下是否有权限
[08:24] OK那如果说呢如果说没有权限它会跳转到一些页面如果没有登录它会跳转到一些不同的URL地址我们都已经配置成功了那还有一个别忘了就是Carol对Sheryl注解的一个支持OK这就是我们整个它的一个整合的配置

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Shiro 框架中过滤器（Filter）的配置与使用，包括过滤器的类型、配置方式以及如何通过过滤器链实现权限控制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Shiro 过滤器的类型说明，包括 anon、authc、logout、authcBasic、ssl、perms[user]、roles[admin]、rest[user]、port[8081] 等过滤器及其作用。
画面2：展示 Shiro 过滤器的类型说明，包括 anon、authc、logout、authcBasic、ssl、perms[user]、roles[admin]、rest[user]、port[8081] 等过滤器及其作用。
画面3：展示 Shiro 过滤器的类型说明，包括 anon、authc、logout、authcBasic、ssl、perms[user]、roles[admin]、rest[user]、port[8081] 等过滤器及其作用。
画面4：展示 Shiro 过滤器的类型说明，包括 anon、authc、logout、authcBasic、ssl、perms[user]、roles[admin]、rest[user]、port[8081] 等过滤器及其作用。
画面5：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面6：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面7：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面8：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面9：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面10：展示 Windows 桌面，包含“黑马程序员”和“博学谷”的标志。
画面11：在 Notepad++ 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面12：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面13：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。
画面14：在 IntelliJ IDEA 中展示 Shiro 过滤器配置代码，包括创建 ShiroFilterFactoryBean、设置 SecurityManager、配置登录和未授权 URL。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
//配置安全管理器
@Bean
public SecurityManager securityManager(CustomRealm realm) {
    DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm);
    securityManager.setRealm(realm);
    return securityManager;
}

//filter工厂，设置对应的过滤器或默认条件
@Bean
public ShiroFilterFactoryBean shiroFilterSecurityManager() {
    //1.创建shiro过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    //2.设置安全管理员
    filterFactory.setSecurityManager(securityManager);
    //3.通用配置（登录页面，登录成功页面，登录失败页面）
    filterFactory.setLoginUrl("/autherror?code=1");//设置登录页面
    filterFactory.setUnauthorizedUrl("/autherror?code=2");//设置未授权页面
    //4.设置过滤器链
    //设置所有的过滤器，有顺序map
    //key - 拦截的url地址
    //value - 过滤器类型
    //5.设置过滤器
    filterFactory.setFilterChainDefinitionMap(filterMap);
    return filterFactory;
}

//开启对shior注解的支持
@Bean
public AuthorizationAttributeSourceAdvisor authorizationAttributeSourceAdvisor(SecurityManager securityManager) {
    AuthorizationAttributeSourceAdvisor advisor = new AuthorizationAttributeSourceAdvisor();
    advisor.setSecurityManager(securityManager);
    return advisor;
}

画面2：
//配置安全管理器
@Bean
public SecurityManager securityManager(CustomRealm realm) {
    DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm);
    securityManager.setRealm(realm);
    return securityManager;
}

//filter工厂，设置对应的过滤器或默认条件
@Bean
public ShiroFilterFactoryBean shiroFilterSecurityManager() {
    //1.创建shiro过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    //2.设置安全管理员
    filterFactory.setSecurityManager(securityManager);
    //3.通用配置（登录页面，登录成功页面，登录失败页面）
    filterFactory.setLoginUrl("/autherror?code=1");//设置登录页面
    filterFactory.setUnauthorizedUrl("/autherror?code=2");//设置未授权页面
    //4.设置过滤器链
    //设置所有的过滤器，有顺序map
    //key - 拦截的url地址
    //value - 过滤器类型
    //5.设置过滤器
    filterFactory.setFilterChainDefinitionMap(filterMap);
    return filterFactory;
}

//开启对shior注解的支持
@Bean
public AuthorizationAttributeSourceAdvisor authorizationAttributeSourceAdvisor(SecurityManager securityManager) {
    AuthorizationAttributeSourceAdvisor advisor = new AuthorizationAttributeSourceAdvisor();
    advisor.setSecurityManager(securityManager);
    return advisor;
}

画面3：
//配置安全管理器
@Bean
public SecurityManager securityManager(CustomRealm realm) {
    DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm);
    securityManager.setRealm(realm);
    return securityManager;
}

//filter工厂，设置对应的过滤器或默认条件
@Bean
public ShiroFilterFactoryBean shiroFilterSecurityManager() {
    //1.创建shiro过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    //2.设置安全管理员
    filterFactory.setSecurityManager(securityManager);
    //3.通用配置（登录页面，登录成功页面，登录失败页面）
    filterFactory.setLoginUrl("/autherror?code=1");//设置登录页面
    filterFactory.setUnauthorizedUrl("/autherror?code=2");//设置未授权页面
    //4.设置过滤器链
    //设置所有的过滤器，有顺序map
    //key - 拦截的url地址
    //value - 过滤器类型
    //5.设置过滤器
    filterFactory.setFilterChainDefinitionMap(filterMap);
    return filterFactory;
}

//开启对shior注解的支持
@Bean
public AuthorizationAttributeSourceAdvisor authorizationAttributeSourceAdvisor(SecurityManager securityManager) {
    AuthorizationAttributeSourceAdvisor advisor = new AuthorizationAttributeSourceAdvisor();
    advisor.setSecurityManager(securityManager);
    return advisor;
}

画面4：
//配置安全管理器
@Bean
public SecurityManager securityManager(CustomRealm realm) {
    DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm);
    securityManager.setRealm(realm);
    return securityManager;
}

//filter工厂，设置对应的过滤器或默认条件
@Bean
public ShiroFilterFactoryBean shiroFilterSecurityManager() {
    //1.创建shiro过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    //2.设置安全管理员
    filterFactory.setSecurityManager(securityManager);
    //3.通用配置（登录页面，登录成功页面，登录失败页面）
    filterFactory.setLoginUrl("/autherror?code=1");//设置登录页面
    filterFactory.setUnauthorizedUrl("/autherror?code=2");//设置未授权页面
    //4.设置过滤器链
    //设置所有的过滤器，有顺序map
    //key - 拦截的url地址
    //value - 过滤器类型
    //5.设置过滤器
    filterFactory.setFilterChainDefinitionMap(filterMap);
    return filterFactory;
}

//开启对shior注解的支持
@Bean
public AuthorizationAttributeSourceAdvisor authorizationAttributeSourceAdvisor(SecurityManager securityManager) {
    AuthorizationAttributeSourceAdvisor advisor = new AuthorizationAttributeSourceAdvisor();
    advisor.setSecurityManager(securityManager);
    return advisor;
}

画面5：
//配置安全管理器
@Bean
public SecurityManager securityManager(CustomRealm realm) {
    DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager(realm);
    securityManager.setRealm(realm);
    return securityManager;
}

//filter工厂，设置对应的过滤器或默认条件
@Bean
public ShiroFilterFactoryBean shiroFilterSecurityManager() {
    //1.创建shiro过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    //2.设置安全管理员
    filterFactory.setSecurityManager(securityManager);
    //3.通用配置（登录页面，登录成功页面，登录失败页面）
    filterFactory.setLoginUrl("/autherror?code=1");//设置登录页面
    filterFactory

