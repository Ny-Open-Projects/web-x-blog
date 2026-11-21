# 11-shiro的会话管理：介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\11-shiro的会话管理：介绍_【海量资源尽在 ubkz.com】.mp4
- 时长 9分30秒（音频 570s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 我们已经呢完成了share它的认证和授权的这么两个功能那对于这两个功能呢其实咱们使用起来都比较简单就是做一些相应的配置其实就可以了那但是有的朋友会有这样一种疑问那我们一起来看一下是这样的就是说呢我这个代码里面写的内容呢找到我们自定的RAM域当中那我底下有一个认证方法用户登录那用户登录了之后呢这边有一个就是把安全数据
[00:32] 哎返回了那接下来呢各位在看授权那看授权的时候我这边是不是想方设法获取到了我们这个安全数据啊那这个时候咱们的疑问就来了就是说你登录之后这个安全数据放到了什么地方你怎么在授权的时候就能得到相应的这个安全数据呢好了是这样的在share当中它其实是可以把你这个安全数据把它保存到内存当中的
[01:04] 那在我这边呢给各位准备了一张图形咱们打开一起来看一下里面重点说的就是我们认证和授权这个安全数据的一个存储的一个问题好了这边呢我把这张图形打开和各位简单的来做一个分析那首先呢我们来看底下这个流程那当用户呢在页面输入用户名称密码进行登录之后咱们呢在我们的控制器内当中通过subject也就是主体点击它的login方法
[01:33] 那logging方法最后会传导到我们自定的任务域里面的认证方法认证方法跟数据库打交道获取然后比较比较是否验证通过那如果验证通过它其实就是把这个安全数据存取下来了那存取下来之后接下来你访问某一个UIL地址的时候就是上边了咱们开始做授权那授权的时候通过拦截器当然了这边写的拦截器写的不太正确其实是一个过滤器
[01:59] 那通过过滤器的形式接着进入到我们的叫做授权的这个方法那这个授权的方法咱们就要获取这个安全数据那这边的安全数据提到了很多次有存有取那究竟放到什么地方比较合适那注意我们现在不管是用什么形式现在是Spring Boot那对于Spring Boot来说其实它也是一个web的形式在里面有
[02:22] 所以对于web程序来说我们登录了之后把数据放到什么地方获取的时候应该从哪获取那就比较明了了我们一般是不是可以把这个数据放到session当中来做那有的朋友就说了你这代码里面一点session的内容都没提现那session究竟在哪呢好了那接下来就是我们重点关注的shareware里面的第二块内容叫做绘画管理
[02:51] 那Sheryl呢其实内置了一个它自己的绘画管理的这么一套机制也就是说这个绘画管理全部都是通过Sheryl来进行控制那Sheryl提供的这个绘画呢咱们可以在Java SE当中去用也可以在Java E环境当中去用也就是说普通的Java程序能用Web程序也能用它不依赖于任何底层容器可以单独使用好了那接下来通过Sheryl的绘画管理呢可以对你整个的这个绘画进行
[03:21] 这个统一的一个认证统一的一个管理的这么一个过程那这个叫做session manager那注意我说的这个session manager现在不代表的就是web程序的这个session了而是他自己定义的一套绘画叫做session manager那接着我们来看一下什么是share的绘画管理那这个绘画管理呢或者session manager它是管理subject里面的session的创建维护删除等等这个一系列的一个一套工作的那这个session
[03:49] 注意这个session现在不仅仅局限于web当中的那个http session在普通的应用当中你也可以创建一个session这么一个对象只要能完成http session相应的那套逻辑其实就可以了那在这个session manager当中它是一套顶层组件所以说白了这玩意儿其实是一个接口是一个接口这玩意儿是用谁去管理呢通过shareware当中的security manager也就是说security manager要对你的session manager负责
[04:19] 那刚才我们说过这个绘画管理它其实是一个接口那它呢提供了三个默认实现这三个默认实现第一个default session manager这个default session manager是要自己去实现session的逻辑的是要自己去实现session逻辑那接下来我们一般用shadow其中用的是web应用那在web环境当中它提供了两个一个叫做server container session manager也用于web环境
[04:48] 注意它直接使用的Servlet容器当中的绘画那Servlet容器当中的绘画不就是HTTP Session吗好了那接下来还有Default Web Session Manager那Default Web Session Manager它也是Web环境那这个是自己绘画也就是说这个绘画你可以自己改你不想用HTTP Session可以你可以自己写比如说你把它放到Redis里
[05:14] 比如方能把它放到数据库里面只要能够完成session咱们传统session的功能其实就可以了存入session不就是往里存往中取吗记住session id吗没错吧那如果你想自己去改写是不是就应该用这个default web session manager来做啊ok好了这个是跟各位来提了就是说对于我们这个share的绘画管理的这套机制
[05:38] 那其实呢咱们可以做一个简单的验证来看一下就是说我们现在这个web程序什么都没写也没写security manager究竟用的是哪一个session manager也没告他你当前share用哪一个实现那究竟是存到了哪哎这边想跟各位说其实如果你什么都不写默认其实咱们web环境就用的是supplate container session manager也就是说默认把它存到了http session当中
[06:08] 那这边呢底下有一段简单的代码这段简单代码其实呢我们可以写一下就来验证一下默认是不是就把这个安全数据放到了HTTP session当中OK这边呢打开我的idea咱们把这个方法呢给它完善一下做一个简单的测试其实就可以了好了这边呢找到我们刚才的测试controlleruser Controller我就不再去写新的Controller了我在这边呢补充一个新的方法即可
[06:37] 好了当然这个request mapping等等呢我就从讲义上call了这个代码相对来说比较简单全部都拿过来咱们主要是做一个验证即可pdf call的这个代码呢有一点点简单的问题啊我们把它做一个简单的修改ok好了call过来这个代码呢简单的咱们来看一下写了一个方法叫做show给他请求的时候呢我们来了个链接就叫做show里面传递一个参数hb session那么接下来呢这边做的事情session.get attribute names
[07:18] 得到所有session当中它的名称那好了接着进行fault循环便利那便利之后我们根据名称获取它每一个值接着进行打印其实就可以了好了这个代码呢我们拿过来之后我们做一个简单的验证好了这边重新启动一下我的Tomcat哎错了重新启动一下我这个Springboard的程序好了这个程序让它进行启动程序让它进行启动我们打开Postman
[07:47] 首先咱们是不是最终要验证存到哪了咱们说放到了session当中我们只需要登录之后接着点击view方法点击我们刚才的售方法去验证一下看一下是否在session当中打印出了这些数据其实即可好了在这边先去登录send好了这边呢已经登录成功那接下来呢这边我们发送的是一个新的请求叫做售方法好了send
[08:17] 好了查看session成功那接下来我们关注session是否已经都有了好了各位来看这边的数据其实已经给我们打印出来了session当中的数据有很多有很多好了但其中我们关注的其实就是最底下这一个最底下这一个我们存储到session当中的key的名字什么default subject content什么什么一个session key好了看value send.itcast我们叫做user对象那各位我们之前在热密当中
[08:48] 认证成功之后是不是往这个返回了一个对象往里面放了一个安全数据叫做user那这边是把这个安全数据从session当中获取出来了OK好了那这样一来呢我们就已经得知对于Sheryl而言她默认把安全数据在web应用程序里面其实存储到了我们的http session当中那我们没做任何的操作是借助Sheryl当中的绘画管理来做的
[09:15] 那它的绘画管理是一个接口它提了三种实现方式那这三种实现默认使用的是Servlet Context SessionContainer Session Manager借助Servlet的绘画来做OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Shiro 框架中用户登录认证流程、自定义 Realm 实现、Session 会话管理及前后端交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 UserController.java 中的用户登录方法 @RequestMapping(value="/login")。
- 代码逻辑：获取用户名密码，MD5 加密，创建 UsernamePasswordToken，调用 Subject.login()，返回登录结果。
- 代码片段：
  ```java
  @RequestMapping(value="/login")
  public String login(String username,String password) {
      try {
          password = new Md5Hash(password,username,hashIterations:3).toString();
          UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
          Subject subject = SecurityUtils.getSubject();
          subject.login(upToken);
          return "登录成功";
      }catch (Exception e) {
          e.printStackTrace();
          return "用户名或密码错误";
      }
  }
  ```

画面 2：
- 展示 CustomRealm.java 中的 doGetAuthenticationInfo 方法。
- 代码逻辑：从 token 获取用户名密码，通过 userService 根据用户名查询用户，校验密码，返回 SimpleAuthenticationInfo。
- 代码片段：
  ```java
  protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
      UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
      String username = upToken.getUsername();
      String password = new String(upToken.getPassword());
      User user = userService.findByName(username);
      if(user == null || !user.getPassword().equals(password)) {
          //4.如果一致，安全验证通过
          SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(user,user.getPassword(),this.getName());
          return info;
      }
      return null;
  }
  ```

画面 3：
- 展示 Windows 桌面，桌面上有“黑马程序员”和“博学谷”的标志，以及“ihrm”文件夹图标。

画面 4：
- 展示 Shiro 认证与授权的安全数据流程图。
- 结构：访问 url 地址 → 拦截器 → CustomRealm（授权方法）→ 获取安全数据 → 安全数据。
- Subject（主体）→ login 方法 → CustomRealm（认证方法）→ 验证通过 → 存储安全数据 → 数据库。

画面 5：
- 展示 Shiro 认证与授权的安全数据流程图。
- 结构：访问 url 地址 → 拦截器 → CustomRealm（授权方法）→ 获取安全数据 → 安全数据。
- 用户名/密码 → Subject（主体）→ login 方法 → CustomRealm（认证方法）→ 验证通过 → 存储安全数据 → 数据库。

画面 6：
- 展示 PPT 页面，标题为“2.1 什么是 shiro 的会话管理”。
- 内容：SessionManager（会话管理器）管理 Subject 的 session，由 SecurityManager 管理。
- shiro 提供了三个默认实现：DefaultSessionManager、ServletContainerSessionManager、DefaultWebSessionManager。
- 代码片段：
  ```java
  //登录成功后，打印所有session内容
  @RequestMapping(value="/show")
  ```

画面 7：
- 展示 PPT 页面，标题为“2.1 什么是 shiro 的会话管理”。
- 内容：SessionManager（会话管理器）管理 Subject 的 session，由 SecurityManager 管理。
- shiro 提供了三个默认实现：DefaultSessionManager、ServletContainerSessionManager、DefaultWebSessionManager。
- 代码片段：
  ```java
  public String show(HttpSession session) {
      //获取session中所有的键值
      Enumeration<?> enumeration = session.getAttributeNames();
      //遍历enumeration中的
      while (enumeration.hasMoreElements()) {
          //获取session键值
          String name = enumeration.nextElement().toString();
          //根据键值获取session中的值
          Object value = session.getAttribute(name);
          //打印结果
          System.out.println("<b>"+ name + "</b>" + value + "<br/>");
      }
      return "查看session成功";
  }
  ```

画面 8：
- 展示 PPT 页面，标题为“2.2 应用场景分析”。
- 内容：展示 show 方法的代码。

画面 9：
- 展示 PPT 页面，标题为“2.2 应用场景分析”。
- 内容：展示 show 方法的代码。

画面 10：
- 展示 UserController.java 中的 show 方法和 autherror 方法。
- 代码片段：
  ```java
  @RequestMapping(value="/show")
  public String show(HttpSession session) {
      //获取session中所有的键值
      Enumeration<?> enumeration = session.getAttributeNames();
      //遍历enumeration中的
      while (enumeration.hasMoreElements()) {
          //获取session键值
          String name = enumeration.nextElement().toString();
          //根据键值获取session中的值
          Object value = session.getAttribute(name);
          //打印结果
          System.out.println("<b>"+ name + "</b>" + value + "<br/>");
      }
      return "查看session成功";
  }
  @RequestMapping(value="/autherror")
  public String autherror(int code) {
      return code==1?"未登录":"未授权";
  }
  ```

画面 11：
- 展示项目结构，包含 src、target、pom.xml 等目录。
- 展示 UserController.java 中的 show 方法和 autherror 方法。

画面 12：
- 展示 Postman 工具界面。
- 请求地址：http://localhost:8081/user/home。
- 请求方法：POST。
- 请求体：未设置。
- 历史记录中包含多个登录请求。

画面 13：
- 展示 CustomRealm.java 中的 doGetAuthenticationInfo 方法。
- 日志信息：显示了 Spring Boot 启动时的框架初始化日志，包括 DispatcherServlet、FrameworkServlet、Hibernate 等。

画面 14：
- 展示 PPT 页面，标题为“2. Shiro 中的会话管理”。
- 内容：SessionManager（会话管理器）管理 Subject 的 session，由 SecurityManager 管理。
- shiro 提供了三个默认实现：DefaultSessionManager、ServletContainerSessionManager、DefaultWebSessionManager。
- 代码片段：
  ```java
  //登录成功后，打印所有session内容
  @RequestMapping(value="/show")
  ```

