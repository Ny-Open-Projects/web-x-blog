# 画面线理解：21-shiro认证与授权：执行流程分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\21-shiro认证与授权：执行流程分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:29, 00:37, 00:56, 01:28, 01:53, 02:06, 02:27, 02:43, 03:28, 04:28, 04:30, 05:02, 05:20, 05:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:21:10

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
