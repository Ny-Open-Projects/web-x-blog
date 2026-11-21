# 画面线理解：17-SasSHRM中基于shiro的认证授权：环境搭建

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\17-SasSHRM中基于shiro的认证授权：环境搭建_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:30, 02:35, 02:57, 03:19, 03:43, 05:15, 05:55, 06:18, 07:23, 07:47, 08:30, 08:58, 09:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:37:41

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 Shiro 框架，自定义 Session 管理器和 Realm 来实现用户认证与授权。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 JWT 和 Shiro 两种认证授权方式的对比图，左侧为 JWT 方式，右侧为 Shiro 方式，图中包含流程图和文字说明。
画面 2: 展示了 shiro-springboot 项目的 pom.xml 文件，其中包含了 Shiro 相关的依赖配置。
画面 3: 展示了 CustomSessionManager.java 文件，其中定义了获取 sessionid 的方法。
画面 4: 展示了在 IntelliJ IDEA 中右键点击项目目录，弹出的上下文菜单。
画面 5: 展示了在 IntelliJ IDEA 中弹出的“Create New Class”对话框，用于创建新的类。
画面 6: 展示了 CustomSessionManager.java 文件，其中定义了获取 sessionid 的方法。
画面 7: 展示了在 IntelliJ IDEA 中右键点击 controller 包，弹出的上下文菜单。
画面 8: 展示了在 IntelliJ IDEA 中右键点击 controller 包，弹出的上下文菜单。
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
