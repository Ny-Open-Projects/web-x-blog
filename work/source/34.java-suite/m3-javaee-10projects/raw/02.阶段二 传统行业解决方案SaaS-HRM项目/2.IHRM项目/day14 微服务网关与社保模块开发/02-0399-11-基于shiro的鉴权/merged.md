# 11-基于shiro的鉴权

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\11-基于shiro的鉴权_【海量资源尽在 ubkz.com】.mp4
- 时长 8分18秒（音频 499s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 在刚才呢我们一起看过了基于这种JWT token的这种校验方式那除了这种校验方式之外呢我们这个系统呢还跟各位聊了另一种统一的健全是不是叫做基于Sherald没错啦那同样的一张图形先来分析一下我们应该如何去做那同样的是这张图我截一大截一块放到一个新的图形当中OK拿过来接着做一个小小的改造
[00:39] OK我改一下好了那这回呢我们这边的token等等等等我全部都删掉那首先也是第一个那你请求过来之后请求过来之后是不是要在这边进行登录那么登录其实借助咱们的shareware完成了认证那各位别忘了咱们这个系统呢是用的是这种统一的这种session管理的这种机制
[01:03] 来完成的也就是说登录成功之后立马会把这些数据给它放到我们的ready stuff服务器当中ready服务器所以你登录成功之后就会向ready的服务器当中存放对应的一份好了这边就是存放对应的一份我们的用户数据我们说说这个用户数据我们把它叫做安全数据没错吧好了那接下来那接下来
[01:36] 我们就开始进行返回进行返回同样的跟之前这个逻辑差不多差不多我们这回呢也是返回了对应的一个token那这个token呢其实对于我们而言是我们自定义的一个叫做session id这玩意儿是我们自己给它定义出来的ok好了那咱们的请求登录完成了之后那接下来呢我们就开始比如说访问一下企业微服务
[02:06] 那访问企业微湖浏览器到我们的做网关这边是不是也需要在token当中也需要在我们的请求头当中给我们携带这么一个token注意这回我们叫做session id其实跟那个token放的位置差不多都是放到头里只不过刚才我们叫token给它定一个名字这回我们定义名字叫做session id
[02:28] 那这个session id到了我们的zoo网关那我们是不是就可以通过zoo网关结合session id直接从ready当中把这个数据给它取出来没错吧直接我们就可以在这个zoo网关中使用share获取到我们的用户数据那获取到了之后我们可以借助我们的share完成用户健全
[03:02] 还有印象吗那我们用shareware完成用户健全那怎么做呢其实这个就比较简单了我们要做的事情呢一共有两项第一项就是有需要shareware的相关配置那好了还有第二项第二项就是使用shareware的过滤器完成健全其实我们只不过是把之前那种健全由各个的微服务直接给它放到了做网关当中啊
[03:32] OK那接着我们来看一下应该怎么去把这个代码呢给它实现出来回到我们的idea当中好了把这些全部都关掉注意啊这个logging filter是我们刚才这种JWT的我把它注入起来不让它走了不让它走了好了那接下来把这个全部都关掉那我们之前呢自己玩过share相应的这些配置那从我们之前的这些代码当中搞一段share的配置Ctrl C拿到我们这边
[04:03] 网关当中好了放到这边Ctrl V好了Shared ConfigurationOK好了这边呢会有相应的一些错误的一些内容啊这个没关系是因为我们少一些依赖哎因为我们少一些依赖好了我们把这些依赖呢给他哎一个一个的全部都补充出来好了回到这边回到这边Pumpness Meal添加对应的依赖Dependence好了我们叫做
[04:41] IHRMOK好了这边的依赖呢添加好了之后我们这回再来看一下OK已经不会爆出任何的错误了好那注意啊咱们简单再来看一下我call过来的这个配置类这个配置类呢主要是去配置Shera的那其中用到了我们的一个RMU那这边呢去创建安全管理器底下就是配置它的一些核心过滤器那需要各位注意我把这个过滤器现在打开
[05:21] 现在打开了那这样一来也就意味着在我们的网关层所有的请求除了这两个除了这两个是不是都需要登录以及做全新交易之后才可以访问没错吧当然了底下我们这边也有我们的Redis相应的配置好了都比较简单咱们之前都聊过了OK那这样一来由于加入了Sherald
[05:45] 相关配置有了share的过滤器那这样一来你发送一个请求那这回请求其实发送到的是哪不是ZOO网关的过滤器因为我们已经注视掉了我们现在是不是进入到的就是share过滤器那在share的过滤器当中是不是同样去办成的全线校验等等相关的这些工作没错吧OK他们两个可以同时存在并且share过滤器也能好使那接着我们一起来试验一下
[06:15] 好了需要各位注意的是啊我们接下来呢就是要去测试一下咱们这个share配置究竟好不好那在这边呢打开我们的启动类在上边呢我加了一句话就让他去扫描一下com.ihrm那这个的主要目的就是为了去加载我们这边呢有一个公共的common模块里面可能有一些对象为了让我们的显示更加好一些我这边做了一个小的修改
[06:45] OK好了接下来呢咱们开始启动起来一起来看一下效果来走好了我把这个控制台内容呢清空一下OK现在呢这边已经启动成功了那接着我们打开Postman一起再来试一下OK好了各位来看还是跟之前套路一样先去请求一下9001 Company注意咱们的企业微服务那在企业微服务当中呢咱们没有
[07:42] 做任何权限交验所以我一点send能够得到箱子数据没有问题但是如果我请求的是9090请求网关那网关当中咱们是不是就有了箱子数据了所以我一点send各位会发现您还未登录没错吧那这样一来其实就已经说明了我们在网关层已经使用shadow完成了权限交验相应的这些功能那这样一来
[08:11] 我们的其他微服务是不是就可以不用全言教验了没错吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在Zuul网关中集成Shiro进行统一鉴权，包括JWT令牌处理、Shiro配置、Redis会话管理及应用启动流程。

2) 按时间顺序列出每张画面的要点：
画面1：展示Zuul网关中从请求头获取token的Java代码片段，以及Shiro统一鉴权章节标题。
画面2：绘制了JWT鉴权流程图，展示“调用端”向“zuul网关”发送token，网关将token传递给“系统微服务”和“企业微服务”。
画面3：在流程图中增加“redis服务器”节点，表示“系统微服务”和“企业微服务”将用户数据存放在Redis服务器。
画面4：在流程图中修改“系统微服务”和“企业微服务”向“zuul网关”传递的token内容，改为“自定义的sessionid”。
画面5：展示IntelliJ IDEA中Shiro配置文件的目录结构，以及LoginFilter.java文件中的部分代码。
画面6：展示ShiroConfiguration.java文件中创建Realm和SecurityManager的代码。
画面7：展示ShiroConfiguration.java文件中配置Shiro过滤器工厂的代码，包括设置登录URL、未授权URL和过滤器映射。
画面8：展示ShiroConfiguration.java文件中配置RedisManager、RedisSessionDAO和CustomSessionManager的代码。
画面9：展示ShiroConfiguration.java文件中配置Shiro过滤器工厂的代码，包括设置登录URL、未授权URL和过滤器映射。
画面10：展示ShiroConfiguration.java文件中配置RedisCacheManager的代码。
画面11：展示IntelliJ IDEA中项目结构，包含多个模块如ihrm_common、ihrm_company等。
画面12：展示GateApplication.java文件中的Spring Boot启动类代码，以及控制台日志显示应用启动成功。
画面13：展示GateApplication.java文件中的Spring Boot启动类代码。
画面14：展示GateApplication.java文件中的Spring Boot启动类代码，以及控制台日志显示应用启动成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
// 2) 从上下文中获取request对象
HttpServletRequest req = ctx.getRequest();
// 3) 从请求中获取token
String token = req.getHeader("Authorization");
// 4) 判断
if(token == null || "".equals(token.trim())){
    // 没有token，登录校验失败，拦截
    ctx.setSendZuulResponse(false);
    // 返回401状态码，也可以考虑重定向到登录页面
    ctx.setResponseStatusCode(HttpStatus.UNAUTHORIZED.value());
}
// 校验通过，可以将用户信息放入上下文，继续向后执行
return null;
```

画面6：
```java
@Configuration
public class ShiroConfiguration {
    //1.创建realm
    @Bean
    public IRealm getRealm() {
        return new IRealm();
    }
    //2.创建安全管理器
    @Bean
    public SecurityManager getSecurityManager(IRealm realm) {
        DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager();
        securityManager.setRealm(realm);
        //自定义的会话管理器注册到安全管理器中
        securityManager.setSessionManager(sessionManager());
        //自定义的缓存管理器注册到安全管理器中
        securityManager.setCacheManager(cacheManager());
        return securityManager;
    }
}
```

画面7：
```java
//3.配置shiro的过滤器工厂
@Bean
public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) {
    //1.创建过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    //2.设置安全管理器
    filterFactory.setSecurityManager(securityManager);
    //3.设置登录URL，未授权URL
    filterFactory.setLoginUrl("/autherror/code=1"); //登录url
    filterFactory.setUnauthorizedUrl("/autherror/code=2"); //未授权的url
    //4.设置过滤器映射
    Map<String,String> filterMap = new LinkedHashMap<>();
    filterMap.put("/sys/login", "anon");
    filterMap.put("/autherror", "anon");
    //5.设置过滤器链定义
    filterFactory.setFilterChainDefinitionMap(filterMap);
    return filterFactory;
}
```

画面8：
```java
public RedisManager redisManager() {
    RedisManager redisManager = new RedisManager();
    redisManager.setHost("localhost");
    redisManager.setPort(6379);
    return redisManager;
}
public RedisSessionDAO redisSessionDAO() {
    RedisSessionDAO sessionDAO = new RedisSessionDAO();
    sessionDAO.setRedisManager(redisManager());
    return sessionDAO;
}
public DefaultWebSessionManager sessionManager() {
    CustomSessionManager sessionManager = new CustomSessionManager();
    //sessionManager.setSessionIdCookieEnabled(false);
    sessionManager.setSessionIdRewritingEnabled(false);
    sessionManager.setSessionDAO(redisSessionDAO());
    return sessionManager;
}
```

画面10：
```java
public RedisCacheManager cacheManager() {
    RedisCacheManager redisCacheManager = new RedisCacheManager();
    redisCacheManager.setRedisManager(redisManager());
    return redisCacheManager;
}
```

画面12：
```java
package com.ihrm.gate;
@SpringBootApplication(scanBasePackages = "com.ihrm")
//开启zuul网关功能
@EnableZuulProxy
//开启服务发现功能
@EnableDiscoveryClient
public class GateApplication {
    public static void main(String[] args) {
        SpringApplication.run(GateApplication.class);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2：
- 标题：JWT的鉴权
- 结构：调用端 → zuul网关 → 系统微服务（token）；调用端 → zuul网关 → 企业微服务（token）
画面3：
- 结构：系统微服务 → 存放 → redis服务器（用户数据）；企业微服务 → 存放 → redis服务器（用户数据）
画面4：
- 结构：系统微服务 → 传递 → zuul网关（自定义的sessionid）；企业微服务 → 传递 → zuul网关（自定义的sessionid）

5) 不要评价画面美观，不要输出与课程无关的内容。

