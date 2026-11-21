# 10-shiro鉴权：通过注解鉴权

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\10-shiro鉴权：通过注解鉴权_【海量资源尽在 ubkz.com】.mp4
- 时长 5分24秒（音频 325s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 那对于这个请求地址这个权限的校验呢其实除了过滤器之外还有一种形式就是需要用到注解那对于这个注解呢我们需要在底下做这个开启对Shera注解的一个支持那这些我们都搞定了之后接下来我们看一下这个注解应该如何去使用那比如说呢还是这个user-gum-home在举例那user-gum-home我们都知道我们都知道这个其实代表的是我user-control里面配置的这么一个请求路径
[00:32] 那这个请求路径代表的是home方法那我可以在这个方法上面添加注解使用share注解健全好那这个怎么做呢就是at这个注解的名称呢这个注解呢有很多我们一般用这么两个第一个叫做at requestpermissions那第二个叫做at requestrose那这两个注解呢我简单的说明一下这个是
[01:07] 访问此方法必须具备的权限究竟有什么好了这个代表的是访问此方法必须具备的角色究竟有什么那我们一般常用request叫做permissions来做其实就可以了好的在这边atrequestpermissions比如说呢还是跟刚才一样
[01:38] 我们这边呢只有具备了user.home这个权限user.home我们刚才说过张三他有李四王我都没有那只有张三登录的时候才没问题那需要跟各位注意说明一件事情说明这件事情是这样的就是说呢我们都知道用户健全呢其实可以有两种方式第一种方式呢就是过滤器那过滤器如果如果权限信息不匹配
[02:08] 那权限信息不匹配的话它其实就是跳转到了我们指定的这个set on also-reneged ULD 值好了第二种如果是使用我们叫做注解的形式形配置它呢会抛出叫做异常这个呢叫做 also-reneging exception它会抛出这么一个异常所以这两种呢如果不具备权限的话
[02:37] 它的处理方式是不一样的我们一起来看一下效果好了在这边我再重新启动一下当前的这个工程好了启动一下当前工程同样在这边呢我们来做一个测试先是呢用张三登录那张三登录成功了没什么问题那接着我再去访问Udergang Home张三他有权限访问成功那接下来替换成李四李四登录Session会重置
[03:13] Session重置之后我这边切换访问李四的user刚好我们走你发现爆出了一个500错误服务器内部异常我们来看一下服务器内部异常好了它爆出了这么一个错误叫做also reneging叫做exception好了所以对于注解的这种方式如果要去进行健全的话我们就有必要要对这个抛出的异常进行处理那其实这个处理也比较简单在今天的代码部分呢已经把这个基本的异常处理累
[03:43] 之前咱们都写过把它准备好了那我随便呢随便给它放到一个地方把这个类呢Ctrl C直接把它拷过来好了各位来看这个其实就是拦截了下这个异常进行统一处理那返回一个未授权这么几个字就是为了更加统一好了我这回再去重启一下服务好了这边让它去启动我这边呢打开Postman我们进行准备理似登录登录成功没有权限去访问好了经过我错误的统一处理
[04:26] 跳转出了未授权这么几个字好了那这样一来我整个授权的这个逻辑也就跟各位都说清楚了其实这个就是在我们讲义上都有进行授权呢其实是基于两种方式第一个是基于配置的我们可以通过过滤器来做第二个是基于注解那不管是配置还是注解它处理的逻辑不一样如果说是配置这种方式你权限信息不匹配跳转到我们指定的URL地址
[04:51] 那如果是注解会抛出异常所以我们要对这个异常进行统一处理OK那这样一来呢我整个Sheryl这个整合Spring Boot这个小的案例咱们就已经都说清了那通过这个案例想让各位来掌握的其实就是它整个案例搭建的什么一个过程以及它们整合的相关内容那我们自定义任务域的时候我们要从数据库里面获取内容进行比较以及我们授权的两种方式
[05:17] 那这两种方式一个是基于我们过滤器配置的一个是基于注解的方式来做OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Shiro 框架实现基于注解的权限控制，包括配置 FilterChain、使用 @RequiresPermissions 和 @RequiresRoles 注解，并处理异常。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 ShiroConfiguration.java 文件中配置 FilterChain 的代码。
- 代码内容：
  ```java
  Map(String,String) filterMap = new LinkedHashMap<>();
  //具有某中权限才能访问
  //用过滤器的形式配置请求地址的依赖权限
  //filterMap.put("/user/home","anon");//当前请求可以匿名访问
  //用过滤器的形式配置请求地址的依赖角色
  //filterMap.put("/user/home","perms:user-home");//不具指定的权限，跳转到setUnauthorizedUrl地址
  //用过滤器的形式配置请求地址的依赖角色
  //filterMap.put("/user/home","roles:系统管理员");
  filterMap.put("/user/**","authc");//当请求地址必须认证之后才可以访问
  filterFactory.setFilterChainDefinitionMap(filterMap);
  return filterFactory;
  ```
- 后续代码：
  ```java
  //开启对shiro注解的支持
  @Bean
  public AuthorizationAttributeSourceAdvisor authorizationAttributeSourceAdvisor(SecurityManager securityManager) {
      AuthorizationAttributeSourceAdvisor advisor = new AuthorizationAttributeSourceAdvisor();
      advisor.setSecurityManager(securityManager);
      return advisor;
  }
  ```

画面 2：
- 展示 UserController.java 文件，其中包含三个 HTTP 请求方法：home、add、find。
- 方法注解：
  ```java
  @RequestMapping(value = "/user/home")
  public String home() {
      return "访问个人主页成功";
  }

  @RequestMapping(value = "/user", method = RequestMethod.POST)
  public String add() {
      return "添加用户成功";
  }

  @RequestMapping(value = "/user", method = RequestMethod.GET)
  public String find() {
      return "查询用户成功";
  }
  ```

画面 3：
- 在 UserController.java 中，光标位于第 27 行，准备添加 Shiro 注解。
- 展示了 IDE 的自动补全建议，包括 @RequiresPermissions、@RequiresRoles 等注解。

画面 4：
- 在 UserController.java 中，第 27 行添加了注解：
  ```java
  @RequiresPermissions()
  ```
- 注释说明：访问此方法必须具备的权限。

画面 5：
- 在 UserController.java 中，第 27 行添加了注解：
  ```java
  @RequiresPermissions("user-home")
  ```
- 注释说明：访问此方法必须具备的权限。

画面 6：
- 在 UserController.java 中，第 27 行添加了注解：
  ```java
  @RequiresPermissions("user-home")
  ```
- 注释说明：访问此方法必须具备的权限。
- 方法注解：
  ```java
  @RequestMapping(value = "/user/home")
  public String home() {
      return "访问个人主页成功";
  }
  ```

画面 7：
- 展示项目结构，包括 src/main/java、src/main/resources 等目录。
- 展示 application.yml 文件。

画面 8：
- 展示项目启动时的控制台日志，显示 Shiro 的 FilterChain 初始化过程。
- 日志内容：
  ```
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.CharacterEncodingFilter.doFilterInternal(CharacterEncodingFilter.java:197)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HiddenHttpMethodFilter.doFilterInternal(HiddenHttpMethodFilter.java:77)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.RequestContextFilter.doFilterInternal(RequestContextFilter.java:99)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
  at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:100)
  at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:108)
  at org.springframework.web.filter.OncePer

