# 21-shiro认证与授权：执行流程分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\21-shiro认证与授权：执行流程分析_【海量资源尽在 ubkz.com】.mp4
- 时长 5分46秒（音频 346s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们看过了Sheryl它的一个认证授权当然我们也自定了一个realme域那其实这个realme域是我们以后常见的这么一种使用方式那究竟它这个整个的代码是怎么流转过去的呢我们可以在这边以debug的形式我们简单的来看一下我们就以登录为例这边的打一个断点debug的形式我们来执行一下看一下效果好了debug执行走好了接着呢我就往下去走了走走走
[00:33] 走到当天这句话我点击的是单步进入进入F7那进入之后呢这个里面的这个代码呢其实都不难看起来也比较好理解那这边呢开始往下走注意这里面的第二行是不是就是通过了安全管理器调用它的login方法来执行了那我往下走一步进去那进入到这个安全管理器里面的login方法各位会发现默认的安全管理器呢实际是一个default security manager默认安全管理器
[01:04] 那在安全管理器里面调用了是类似点assenticate这么一个方法那assenticate这么一个方法究竟在干什么我们再进去一起来看一下进去那进去之后呢就会发现这个方法里面return类似点assenticator这个assenticator各位应该都熟悉啊我们之前呢说的是他的抱歉说的是他的叫什么呢找到我们这张图是不是认证调用的就是这个assenticator这玩意儿是不是就是我们的认证器啊
[01:35] 那通过认证器是不是最终要想方设法的调用的realm所以我们继续去往下跟这个源码继续电进去好了调用我们认证器里面的authenticate的方法把token传下去各位这个token这边已经有了就是我们刚才构造url name password的token好了走那进来之后呢这边有一个基本的一个判断判断这个就不管它了继续走走不管注意这边又调用了类似点doauthenticate的方法我们进去来看一下
[02:06] 好了进来了之后注意慢慢的它的阵容就已经浮现出来了继续往下走这边ConnectionRoomRooms等于类似点GetRooms是因为我们所有的内容都已经注册到Sheryl那Sheryl就能够拿到所有的Room域那么往下走一步呢各位来看这个集合里面有多少个元素点开来看这个集合元素里面只有一个Set1那我们打开看一下是谁是不是就是我们的自己定义好的这个权限的这个Room域啊
[02:35] 那接下来呢我们继续往下走进去好了继续往下走好了各位来看这回呢就调用我们realme域的里面getaccenticateinfo方法那这个realme域究竟是谁那这位也看到了是不是执行的就是我们全线验证的这个realme域里面的认证方法注意这是认证这个方法所以这样一来它的一个执行逻辑就比较明确了
[03:06] 那在我们的讲义当中呢其实也把他这个认证和我们授权的这几个步骤呢这边以图形的形式跟各位做了一个分享首先呢就是这个认证流程我们的subject调用他的登录方法进入到我们的security manager那security manager这刚才我们看过了也是执行login方法那security manager又借助他的认证的这个认证器那认证器里面找到了所有的任务欲那我们找到是我们自己写好的一个认证的一个我们自己写好的这么一个任务欲执行他的方法
[03:36] 是完成认证的这么一个操作所以对于我们这个认证来说呢一共就这么几步执行落方执行方法传递给Street Manager那Street Manager里面设置好了之后接着里面就开始Street Manager去委托我们的认证器进行认证那这个认证器呢真正的要做身份认证了它是我们整个身份的一个入口点认证的入口点在这里面呢它其实委托呢很多个我们这边的策略就你认证有很多策略
[04:04] 那它里面的策略呢不管是什么策略其实就俩第一个策略是这样的如果你只有一个认证器进入你当前如果你只有一个ROM域这是你当前的一个的如果你有两个或者多个执行多个的就这么一个策略好了接下来认证器会把相应的这个token传递给我们自己写好的ROM在我们自己写好的ROM里面完成身份认证的这么一个信息操作好了这个身份认证我们看过了之后接下来就是这个授权了
[04:31] 那其实这个不管是授权还是我们这个身份认证它的流程都是差不多的如果各位感兴趣的话可以自己debug形式走一下这边呢为了咱们的节省一点点课程时间我就不再去debug让各位一个一个去看了其实都是一样的那这边呢在身份授权的时候也是通过subject当然了你可以调用它的has row方法或者is permitted的方法这两个方法任选其一它都会进入到我们的security manager
[05:01] 那Street Manager又去委托给不同的我们的授权管理器来做那授权管理器接着去找到我们的RumorView一步一步的完成操作即可好了这个就是我们整个今天入门的这么一个案例通过入门的案例想让各位来了解的就是Sherlock框架究竟能干什么Sherlock框架它的结构究竟是什么样子以及我们之后要写Sherlock框架其实最重要的就是围绕在如何获取Subject以及我们如何自定义RumorView那在RumorView里面我们想方设法的
[05:30] 构造它的认证或者我们登录的比较方法是构造我们的权限信息即可当然了不管是认证还是授权它的执行流程都离不开SubjectSecurity Manager离不开我们的自定义领域OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Shiro 认证流程的源码调试与架构原理，通过调试器逐步跟踪 `Subject.login()` 方法调用链，结合 PPT 图解说明认证与授权的核心组件及其协作关系。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示测试类 `ShiroTest03.java` 中的 `@Test void testLogin()` 方法，调用 `subject.login(token)` 执行登录认证，其中 `token` 是 `UsernamePasswordToken` 类型。
画面 2: 调试器断点进入 `DelegatingSubject.login()` 方法，显示 `this.securityManager.login(this, token)` 被调用。
画面 3: 调试器断点进入 `DefaultSecurityManager.login()` 方法，显示 `this.authenticate(token)` 被调用。
画面 4: 展示 PPT 页面“4.2 Shiro的内部结构”，图中包含“Security Manager”、“Authenticator”、“Authorizer”、“Pluggable Realms”等核心组件，以及“Subject”指向“Security Manager”的流程。
画面 5: 调试器断点进入 `AbstractAuthenticator.authenticate()` 方法，显示 `this.doAuthenticate(token)` 被调用。
画面 6: 调试器断点进入 `ModularRealmAuthenticator.doAuthenticate()` 方法，显示 `this.assertRealmConfigured();` 被调用。
画面 7: 调试器断点进入 `ModularRealmAuthenticator.doAuthenticate()` 方法，显示 `realms = java.util.ArrayList@1167`，并展开查看 `realms` 的内容。
画面 8: 调试器断点进入 `ModularRealmAuthenticator.doSingleRealmAuthentication()` 方法，显示 `realm = org.apache.shiro.realm.ModularRealm`。
画面 9: 展示 PPT 页面“(1) 认证流程”，图中包含“Subject”指向“Security Manager”，“Security Manager”指向“Authenticator”，“Authenticator”指向“Pluggable Realms”的流程。
画面 10: 展示 PPT 页面“(2) 授权流程”，图中包含“Subject”指向“Security Manager”，“Security Manager”指向“Authorizer”，“Authorizer”指向“Pluggable Realms”的流程。
画面 11: 展示 PPT 页面“(2) 授权流程”，图中包含“Subject”指向“Security Manager”，“Security Manager”指向“Authorizer”，“Authorizer”指向“Pluggable Realms”的流程。
画面 12: 展示 PPT 页面“(2) 授权流程”，图中包含“Subject”指向“Security Manager”，“Security Manager”指向“Authorizer”，“Authorizer”指向“Pluggable Realms”的流程。
画面 13: 展示 PPT 页面“4.2 Shiro的内部结构”，图中包含“Security Manager”、“Authenticator”、“Authorizer”、“Pluggable Realms”等核心组件，以及“Subject”指向“Security Manager”的流程。
画面 14: 展示 PPT 页面“(1) 认证流程”，图中包含“Subject”指向“Security Manager”，“Security Manager”指向“Authenticator”，“Authenticator”指向“Pluggable Realms”的流程。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```java
@Test
public void testLogin() {
    Subject subject = SecurityUtils.getSubject();
    String username = "zhangsan";
    String password = "123456";
    UsernamePasswordToken token = new UsernamePasswordToken(username, password);
    //执行login >realm中的认证方法
    subject.login(token);
    //提示：
    //realm中的授权方法
    System.out.println(subject.hasRole("role1"));
    System.out.println(subject.isPermitted("user:save"));
}
```

画面 2:
```java
public void login(AuthenticationToken token) throws AuthenticationException {
    this.clearRunIdentitiesInternal();
    Subject subject = null;
    PrincipalCollection principals;
    if (subject instanceof DelegatingSubject) {
        DelegatingSubject delegating = (DelegatingSubject)subject;
        principals = delegating.getPrincipals();
        host = delegating.getHost();
    } else {
        principals = subject.getPrincipals();
    }
    if (principals == null && principals.isEmpty()) {
```

画面 3:
```java
public Subject login(Subject subject, AuthenticationToken token) throws AuthenticationException {
    try {
        info = this.authenticate(token);
    } catch (AuthenticationException var7) {
        AuthenticationException ae = var7;
        if (this.onFailedLogin(token, ae, subject)) {
            throw ae;
        }
    }
    try {
        this.onFailedLogin(token, ae, subject);
    } catch (Exception var8) {
        if (log.isInfoEnabled()) {
            log.info("onFailedLogin method threw an exception. Logging and propagating original AuthenticationException.");
            throw var8;
        }
    }
}
```

画面 5:
```java
public final AuthenticationInfo authenticate(AuthenticationToken token) throws AuthenticationException {
    if (token == null) {
        throw new IllegalArgumentException("Method argument (authentication token) cannot be null.");
    } else {
        log.trace("Authentication attempt received for token [" + token + "] by this Authenticator");
        AuthenticationInfo info;
        if (info == null) {
            String msg = "No account information found for authentication token [" + token + "] by this Authenticator";
            throw new AuthenticationException(msg);
        }
        AuthenticationException ae = null;
        try {
            info = this.doAuthenticate(token);
        } catch (Throwable var7) {
            ae = var7;
        }
        if (ae != null) {
            throw ae;
        }
        return info;
    }
}
```

画面 6:
```java
protected AuthenticationInfo doAuthenticate(AuthenticationToken authenticationToken) throws AuthenticationException {
    this.assertRealmConfigured();
    Collection<Realm> realms = this.getRealms();
    if (realms.size() == 1) {
        return this.doSingleRealmAuthentication(realms.iterator().next(), authenticationToken);
    } else {
        return this.doMultiRealmAuthentication(realms, authenticationToken);
    }
}
```

画面 7:
```java
realms = java.util.ArrayList@1167
{
    serialVersionUID: long = 8683452581122892189
    DEFAULT_CAPACITY: int = 10
    DEFAULT_EMPTY_DATA: java.lang.Object = [java.lang.Object]
    DEFAULT_ELEMENT_DATA: java.lang.Object = [java.lang.Object]
    size: int = 1
    MAX_ARRAY_SIZE: int = 2147483639
    modCount: int = 1
    java.util.AbstractCollection.MAX_ARRAY_SIZE = 2147483639
}
```

画面 8:
```java
protected AuthenticationInfo doSingleRealmAuthentication(Realm realm, AuthenticationToken token) {
    if (!realm.supports(token)) {
        String msg = "Realm [" + realm + "] does not support authentication token [" + token + "]. Please ensure that the realm supports the token type.";
        throw new UnsupportedTokenException(msg);
    } else {
        AuthenticationInfo info = realm.getAuthenticationInfo(token);
        if (info == null) {
            String msg = "Realm [" + realm + "] was unable to find account for the submitted AuthenticationToken.";
            throw new UnknownAccountException(msg);
        }
        return info;
    }
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 4: 标题“4.2 Shiro的内部结构”。图中“Subject”指向“Security Manager”。图中“Security Manager”包含“Authenticator”、“Authorizer”、“Session Manager”、“Cache Manager”等组件。“Pluggable Realms (1 or more)”位于“Security Manager”下方，由“Security Manager”指向。“Security Manager”指向“Pluggable Realms”。
画面 9: 标题“(1) 认证流程”。图中“Subject”指向“Security Manager”（编号1）。图中“Security Manager”指向“Authenticator”（编号3）。图中“Authenticator”指向“Pluggable Realms (1 or more)”（编号5）。
画面 10: 标题“(2) 授权流程”。图中“Subject”指向“Security Manager”（编号2）。图中“Security Manager”指向“Authorizer”（编号3）。图中“Authorizer”指向“Pluggable Realms (1 or more)”（编号4）。
画面 11: 标题“(2) 授权流程”。图中“Subject”指向“Security Manager”（编号2）。图中“Security Manager”指向“Authorizer”（编号3）。图中“Authorizer”指向“Pluggable Realms (1 or more)”（编号4）。
画面 12: 标题“(2) 授权流程”。图中“Subject”指向“Security Manager”（编号2）。图中“Security Manager”指向“Authorizer”（编号3）。图中“Authorizer”指向“Pluggable Realms (1 or more)”（编号4）。
画面 13: 标题“4.2 Shiro的内部结构”。图中

