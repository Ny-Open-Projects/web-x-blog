# 画面线理解：18-shiro认证与授权：自定义realm-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\18-shiro认证与授权：自定义realm-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:27, 00:56, 01:13, 02:51, 03:27, 03:48, 04:13, 04:50, 05:29, 05:53, 06:00, 06:05, 06:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:18:57

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Shiro 中自定义 Realm，通过重写 doGetAuthorizationInfo 和 doGetAuthenticationInfo 方法来实现用户认证和授权功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示测试类 ShiroTest02.java 中的 testLogin 方法，用于验证用户登录和权限检查。
画面2：展示 shiro-test-2.ini 配置文件内容，定义了用户和角色信息。
画面3：展示 shiro-test-2.ini 配置文件内容，定义了用户和角色信息。
画面4：在 IntelliJ IDEA 中，右键点击 shiro-test-2.ini 文件，弹出“Copy”对话框，准备复制文件。
画面5：在 IntelliJ IDEA 中，右键点击 shiro-test-2.ini 文件，弹出“New”菜单，准备创建新文件。
画面6：打开 PermissionRealm.java 文件，准备编写自定义 Realm。
画面7：在 PermissionRealm.java 中，弹出“Select Methods to Implement”对话框，选择需要重写的抽象方法。
画面8：在 PermissionRealm.java 中，编写了基本的类结构和方法声明。
画面9：在 PermissionRealm.java 中，为 doGetAuthorizationInfo 方法添加了注释说明。
画面10：在 PermissionRealm.java 中，为 doGetAuthenticationInfo 方法添加了注释说明。
画面11：在 PermissionRealm.java 中，开始编写 setUserName 方法。
画面12：在 PermissionRealm.java 中，为 setUserName 方法选择合适的参数类型。
画面13：在 PermissionRealm.java 中，为 setUserName 方法添加了注释说明。
画面14：在 PermissionRealm.java 中，为 setUserName 方法添加了注释说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
// 1. 创建 SecurityManager 工厂
SecurityManager securityManager = factory.getInstance();
// 2. 设置 SecurityManager
SecurityUtils.setSecurityManager(securityManager);

@Test
public void testLogin() {
    Subject subject = SecurityUtils.getSubject();
    String username = "11111";
    String password = "123456";
    UsernamePasswordToken token = new UsernamePasswordToken(username,password);
    // 登录成功之后，获取到的 subject 对象就是当前登录的用户
    // 通过 subject 可以判断用户是否具有某种角色，是否具有某个权限
    System.out.println(subject.hasRole("role1"));
    System.out.println(subject.isPermitted("user:save"));
}
```

画面2：
```ini
[users]
zhangsan=123456,role1,role2
lisi=123456,role2

[roles]
role1=user:save,user:update
role2=user:find
```

画面6：
```java
package cn.itcast.shiro;

// 自定义 realms 对象
// 继承 AuthorizingRealm
public class PermissionRealm extends AuthorizingRealm {
```

画面7：
```java
org.apache.shiro.realm.AuthorizingRealm
org.apache.shiro.realm.AuthenticatingRealm
```

画面8：
```java
import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;

// 自定义 realms 对象
// 继承 AuthorizingRealm
public class PermissionRealm extends AuthorizingRealm {

    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        return null;
    }

    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        return null;
    }
}
```

画面9：
```java
import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;

// 自定义 realms 对象
// 继承 AuthorizingRealm
public class PermissionRealm extends AuthorizingRealm {

    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        // 获取到用户的授权数据（用户的权限数据）
        return null;
    }

    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        // 根据用户名去密码登录，将用户数据保存（安全数据）
        return null;
    }
}
```

画面10：
```java
import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;

// 自定义 realms 对象
// 继承 AuthorizingRealm
public class PermissionRealm extends AuthorizingRealm {

    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        // 获取到用户的授权数据（用户的权限数据）
        return null;
    }

    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        // 根据用户名去密码登录，将用户数据保存（安全数据）
        return null;
    }
}
```

画面11：
```java
import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;

// 自定义 realms 对象
// 继承 AuthorizingRealm
public class PermissionRealm extends AuthorizingRealm {

    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        // 获取到用户的授权数据（用户的权限数据）
        return null;
    }

    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        // 根据用户名去密码登录，将用户数据保存（安全数据）
        return null;
    }

    public void setName(String name) {
        super.setName(name);
    }
}
```

画面12：
```java
import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;

// 自定义 realms 对象
// 继承 AuthorizingRealm
public class PermissionRealm extends AuthorizingRealm {

    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        // 获取到用户的授权数据（用户的权限数据）
        return null;
    }

    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        // 根据用户名去密码登录，将用户数据保存（安全数据）
        return null;
    }

    public void setName(String name) {
        super.setName(name);
    }
}
```

画面13：
```java
import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;

// 自定义 realms 对象
// 继承 AuthorizingRealm
public class PermissionRealm extends AuthorizingRealm {

    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        // 获取到用户的授权数据（用户的权限数据）
        return null;
    }

    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        // 根据用户名去密码登录，将用户数据保存（安全数据）
        return null;
    }

    public void setName(String name) {
        super.setName(name);
    }
}
```

画面14：
```java
import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;

// 自定义 realms 对象
// 继承 AuthorizingRealm
public class PermissionRealm extends AuthorizingRealm {

    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        // 获取到用户的授权数据（用户的权限数据）
        return null;
    }

    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        // 根据用户名去密码登录，将用户数据保存（安全数据）
        return null;
    }

    public void setName(String name) {
        super.setName(name);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
