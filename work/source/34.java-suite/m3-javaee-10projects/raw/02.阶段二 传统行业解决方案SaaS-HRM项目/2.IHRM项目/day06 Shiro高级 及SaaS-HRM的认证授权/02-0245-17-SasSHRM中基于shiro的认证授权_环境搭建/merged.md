# 17-SasSHRM中基于shiro的认证授权：环境搭建

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\17-SasSHRM中基于shiro的认证授权：环境搭建_【海量资源尽在 ubkz.com】.mp4
- 时长 9分36秒（音频 576s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那接下来呢我们就可以写代码的形式把这个功能给它实现在这边呢我已经把我们的HRM这个系统呢已经打开了那接下来呢我们关注的首先第一件事就是搭建环境搭建环境很简单就是打开我们的Fupom在其中添加上我们的依赖jar 包其实就可以了好了那在这个依赖jar 包呢我就不废话了直接从我们之前案例的工程当中把这一段全部Ctrl C
[00:30] copy过来好了call到这边control re那好了我们这个依赖的部分已经搞定了那接下来呢我们关注的其实就是我们这边写法的里面的几个比较重要的几个组件首先第一个realm域第二个realm域那这个realm域究竟是在做什么那我们都知道对于用户登录来说它有一个认证的realm那接下来那还有很多的其他的微服务
[01:00] 那比如说有企业管理的微服务比如说还有其他的雇员管理的微服务比如还有薪资等等的这些微服务那这些微服务我们重点关注的是不是就是获取安全数据也就是我们授权的这个ROM所以对于我们来说我们这个ROM其实呢写成一个也好写成两个也罢都无所谓但是千万别忘了如果你写成一个公共的ROM那写成公共ROM的话那你这个用户认证的这个系统
[01:26] 或者认证的这个过程由于你认证的时候要连接你用户Service用户DO那你这个企业微服务里面可能就用不了能理解吧所以对于我们而言对于我们而言这个room我们可能要写两个一个是挂载到用户微服务当中用来做认证的一个是我们公共的room这个公共的room主要是为了获取授权数据因为授权数据它都是固定的是从redis里面直接获取就可以了不用跟数据库产生任何交道
[01:57] OK那好了这些我们都做了一个简单的分析做了一个简单的分析那还有一个就是我们叫做share的一个绘画管理那share这个绘画管理呢这个机制其实比较简单用我们之前写的那套代码就可以了因为基本上都是大同小异的那好了接下来我们把这几个固定的内容先给它搞定好了这个固定的内容呢首先这个share绘画管理器因为它是固定的
[02:23] 那这个代码呢也比较简单我可以直接从我们之前的这个工程当中直接给它copy过来好了我们之前工程当中写了一个sessioncustom session manager那这个session manager我们的绘画管理里面不涉及到什么高深的技术问题注意这个session manager公共的每一个微服务都要用因为这里面才能得到你的session id才要跟redis进行交互所以对于我们而言这个呢可以把它写到我们公共的模块下云comment下
[02:54] 好了在这边呢我去创建一个新的包啊右键Java就把它叫做share.session抱歉share.session好了我们把它叫做叫做什么呢就这代码这个名称就跟我之前写的一样吧customsessionm-a-n-a-g-iok
[03:32] 好了里面的代码呢就跟我们之前写的基本上是一样的我从这边直接call过来了Ctrl C Ctrl V拿过来好了需要各位注意的是这个是我们自己写的我们叫做Session Manager那在这个Session Manager当中有一点点需要我们改造的内容那我们之前呢现在我们之前这个案例的这个代码呢其实也是从请求头里面拿到一个叫做Authorization这么一个请求头信息那希望各位要注意的是在我们的
[04:03] SaaS人力资源管理系统当中我们的请求头那请求头信息当中它包含的是一个以B而开头的这么一个字符串BEAR注意我们之前的请求头信息B加空格是不是接着后面写的是你这个token那我们现在这个token其实是用session ID来进行管理的或者来进行替换的所以对于我们而言我们提取的session ID咱们就需要做一个简单的处理那所以我这边ID就等于ID
[04:36] 点replace all好了replace all那接着我们要把bier空格给它替换成空或者把它去掉其实就可以了OK各位朋友注意啊就是我们这个字母别写错了是因为我们这边前端传递的这个bier首字母应该是大写的才可以好了那这样一来呢我们这个自定义的绘画管理器就已经写好了跟我们之前的案例基本上是差不多的
[05:04] 那在里面呢只不过是对这个我们前端传递的这个BIR做了一个格外的处理其实就可以了剩下基本上都是差不多那Session Manager构造好了之后我们接下来关注的就可以去写我们叫做任务的域那我们这个任务的域刚才也做过分析也是包含两类一个是在登录微服务里面有一个认证相关的任务那还有一个我们叫做获取安全数据也就是在去进行授权的这么一个任务
[05:34] 那这个授权room其实就是做去得到一些授权数据其实就可以了所以对于我们而言这个room应该是一个公共的room公共的room所以对于我们而言先把这个公共的给它搞出来好了那在这边的同样回到我们的代码部分公共的也是放到common下那在这边右键去创建一个class那我叫做share.好了这回就是realmroom
[06:03] 那我给它起一个名字比如说呢就叫做iHRM那对于一个ROM来说呢我们之前呢也写过很多的代码我们之前打开可以来看ROM要去定义的话需要去实现需要去继承AlsoRacingROM需要继承它继承它实现里面的两个方法其实就可以了好了引下包接着两个方法好了这两个方法呢第一个我们都知道它是我们的授权方法好了接着第二个
[06:40] 是我们的叫做认证方法那我们在当前的这个公共的叫做公共的room公共的room当中我们主要做的事情是不是就是获取我们叫做安全数据接着构造我们的权限权限信息其实就可以了那这个很明显很明显应该是我们的授权方法要做的事那我们认证方法
[07:09] 由于要查询用户数据库由于要查询用户的Service使用用户的DU等等那我可能企业里面没有所以我这个里面先不写我们重点关注的授权这个应该也能理解没错吧OK我们这边呢先把结构给它写出来那我们这个公共的这个任务先定义到这边那接下来根据我们这张图形那我们在用户登录的这边用户登录的时候是不是也需要一个任务那这个任务主要目的是不是就是去获取到
[07:39] 用户的信息获取到用户的用户密码进行比较那这一个我们要自己在企业微服里面搞一个room那这个企业微服里面我想说了认证你要有认证的方法那授权是不是跟我们刚才这个授权方法应该是一样的都是去看一下你认证的数据或者你的安全数据里面的一些全新信息没错吧所以呢我们需要在企业微服当中去搞一个room那搞一个room那怎么做更加方便或者更加合适
[08:08] 其实很简单很简单我自己定一个比如说叫做user room去继承我这个HRM room那这样以来我里面写一套公共的授权方法不就可以了吧所以接下来呢我们先把这个结构也给它写出来在system系统微服务里面这里面要有登录的逻辑所以我在这边写一个share roomR-E-A-L-M好了给它起一个我比如说就叫做user roomOK
[08:41] 那这个room呢我们说过了要继承我们写的ihrmroom那继承它我们重写里面的认证方法即可好了那接着呢这边呢刚才我们写自定义room的时候呢少写了一件事情不知道各位还有印象吗就是说对于我们来说希望可以对这个room起一个我们独一无二的一个名字比如说我就叫做ihrmroom
[09:10] 好了这边注意我这个user room里面我就不起名字了为什么我们这边用副类的名字其实就可以因为我们别忘了在share当中它存数据认证或者授权的时候我们可以根据room名称获取现在虽然我写的是两个类但是我的room名称是不是应该都是用的是一个这样一来其实更加统一我们的数据OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 Shiro 框架，自定义 Session 管理器和 Realm 来实现用户认证与授权。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 JWT 和 Shiro 两种认证授权方式的对比图，左侧为 JWT 方式，右侧为 Shiro 方式，图中包含流程图和文字说明。
画面 2: 展示了 shiro-Spring Boot 项目的 pom.xml 文件，其中包含了 Shiro 相关的依赖配置。
画面 3: 展示了 CustomSessionManager.java 文件，其中定义了获取 sessionid 的方法。
画面 4: 展示了在 IntelliJ IDEA 中右键点击项目目录，弹出的上下文菜单。
画面 5: 展示了在 IntelliJ IDEA 中弹出的“Create New Class”对话框，用于创建新的类。
画面 6: 展示了 CustomSessionManager.java 文件，其中定义了获取 sessionid 的方法。
画面 7: 展示了在 IntelliJ IDEA 中右键点击 Controller 包，弹出的上下文菜单。
画面 8: 展示了在 IntelliJ IDEA 中右键点击 Controller 包，弹出的上下文菜单。
画面 9: 展示了 CustomRealm.java 文件，其中定义了 doGetAuthorizationInfo 方法。
画面 10: 展示了 IrmRealm.java 文件，其中定义了 doGetAuthorizationInfo 和 doGetAuthenticationInfo 方法。
画面 11: 展示了在 PowerPoint 中选中“Realm 域”文字，弹出的“选择对象”对话框。
画面 12: 展示了在 IntelliJ IDEA 中弹出的“Create New Class”对话框，用于创建新的类。
画面 13: 展示了 IrmRealm.java 文件，其中定义了 doGetAuthorizationInfo 和 doGetAuthenticationInfo 方法。
画面 14: 展示了 UserRealm.java 文件，其中定义了 doGetAuthorizationInfo 和 doGetAuthenticationInfo 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-spring</artifactId>
    <version>1.3.2</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-core</artifactId>
    <version>1.3.2</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-redis</artifactId>
    <version>1.8.0</version>
</dependency>
<repositories>
    <repository>
        <id>spring-snapshots</id>
        <name>Spring Snapshots</name>
        <url>https://repo.spring.io/snapshot</url>
    </repository>
</repositories>
```

画面 3:
```java
protected Serializable getSessionId(ServletRequest request, ServletResponse response) {
    //获取请求头Authorization中的值
    String id = WebUtils.toHttp(request).getHeader("Authorization");
    if(StringUtils.isEmpty(id)) {
        //如果无请求头，生成新的sessionid
        return super.getSessionId(request, response);
    } else {
        //返回sessionid
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_SOURCE, "header");
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID, id);
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_IS_VALID, Boolean.TRUE);
        return id;
    }
}
```

画面 9:
```java
protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
    User user = (User) principalCollection.getPrimaryPrincipal();
    //获取认证用户的所有角色、权限数据
    SimpleAuthorizationInfo info = new SimpleAuthorizationInfo();
    Set<String> roles = new HashSet<>(); //所有角色
    Set<String> perms = new HashSet<>(); //所有权限
    for (Role role : user.getRoles()) {
        roles.add(role.getName());
        for (Permission perm : role.getPermissions()) {
            perms.add(perm.getPermCode());
        }
    }
    info.setStringPermissions(perms);
    info.setRoles(roles);
    return info;
}
```

画面 10:
```java
package com.ihrm.common.shiro.realm;
import org.apache.shiro.authc.AuthenticationException;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authc.AuthorizationInfo;
import org.apache.shiro.authc.PrincipalCollection;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;
//公共的realm，获取安全数据，校验权限信息
public class IrmRealm extends AuthorizingRealm {

    //授权方法
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        return null;
    }

    //认证方法
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) {
        return null;
    }
}
```

画面 13:
```java
//公共的realm，获取安全数据，校验权限信息
public class IrmRealm extends AuthorizingRealm {

    //授权方法
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        return null;
    }

    //认证方法
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) {
        return null;
    }
}
```

画面 14:
```java
package com.ihrm.common.shiro.realm;
import org.apache.shiro.authc.AuthenticationException;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authc.AuthorizationInfo;
import org.apache.shiro.authc.PrincipalCollection;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;
//公共的realm，获取安全数据，校验权限信息
public class UserRealm extends AuthorizingRealm {

    //授权方法
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        return null;
    }

    //认证方法
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        return null;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“JWT的认证授权方式”和“Shiro的认证授权方式”，左侧流程图中“前端浏览器”指向“系统微服务”，“系统微服务”指向“企业微服务”，“企业微服务”指向“前端浏览器”；右侧流程图中“用户登录”指向“系统微服务”，“系统微服务”指向“Shiro会话管理”，“Shiro会话管理”指向“Redis服务”，“Redis服务”指向“Shiro会话管理”，“Shiro会话管理”指向“企业微服务”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

