# 画面线理解：03-自定义realm：认证的操作步骤分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\03-自定义realm：认证的操作步骤分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:16, 00:30, 00:57, 01:52, 01:57, 02:37, 02:49, 03:38, 04:05, 04:13, 04:24, 04:39, 04:45, 06:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:28:08

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Shiro 框架实现用户认证，重点是自定义 Realm 并集成 UserService 进行权限和认证逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 UserController.java 中的 login 方法，使用 Subject.login() 进行认证，调用 SecurityUtils.getSubject() 获取 Subject。
画面 2: PPT 展示 Shiro 认证流程图，Subject 调用 login(token) 方法，由 Security Manager 调用 Authenticator。
画面 3: PPT 展示 Shiro 认证流程图的详细说明，Security Manager 调用 Authenticator，Authenticator 调用 Realm 进行身份验证。
画面 4: 与画面 1 相同，展示 UserController.java 中的 login 方法。
画面 5: 在 UserController.java 中右键创建新类，弹出 Create New Class 对话框，Name 为 "CustomRealm"。
画面 6: 展示创建的 CustomRealm.java 文件，内容为 public class CustomRealm extends AuthorizingRealm { }。
画面 7: 展示 CustomRealm.java 文件，包含 import 语句和两个空方法 doGetAuthorizationInfo 和 doGetAuthenticationInfo。
画面 8: 在 CustomRealm.java 中为 doGetAuthenticationInfo 方法添加注释。
画面 9: 在 CustomRealm.java 中为 doGetAuthorizationInfo 方法添加注释。
画面 10: 在 CustomRealm.java 中为 doGetAuthorizationInfo 方法添加注释。
画面 11: 在 CustomRealm.java 中为 doGetAuthorizationInfo 方法添加注释。
画面 12: 在 CustomRealm.java 中为 doGetAuthenticationInfo 方法添加注释。
画面 13: 在 CustomRealm.java 中为 doGetAuthenticationInfo 方法添加注释。
画面 14: 在 CustomRealm.java 中为 doGetAuthenticationInfo 方法添加注释。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    try {
        UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
        //1.获取Subject
        Subject subject = SecurityUtils.getSubject();
        subject.login(upToken);
        return "登录成功";
    }catch (Exception e) {
        return "用户名或密码错误";
    }
}
```

画面 6:
```java
package cn.itcast.shiro.realm;
import org.apache.shiro.realm.AuthorizingRealm;
//自定义的realm
public class CustomRealm extends AuthorizingRealm {

}
```

画面 7:
```java
import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;

/**
 * 自定义的realm
 */
public class CustomRealm extends AuthorizingRealm {

    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        return null;
    }

    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        return null;
    }
}
```

画面 12:
```java
//1.获取登录的用户名密码（token）
//2.根据用户名查询数据库
//3.判断用户是否存在或者密码是否一致
//4.如果一致，返回null（抛出异常）
//5.不一致，返回null（抛出异常）
return null;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2:
标题: (1) 认证流程
流程图结构:
1. Subject → login(token)
2. Subject → Security Manager
3. Security Manager → Authenticator
4. Authenticator → Realm

画面 3:
标题: (2) 授权流程
流程图结构:
1. Subject → Security Manager
2. Security Manager → Authenticator
3. Authenticator → Realm
4. Realm → Authentication Strategy
5. Authentication Strategy → Realm

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
