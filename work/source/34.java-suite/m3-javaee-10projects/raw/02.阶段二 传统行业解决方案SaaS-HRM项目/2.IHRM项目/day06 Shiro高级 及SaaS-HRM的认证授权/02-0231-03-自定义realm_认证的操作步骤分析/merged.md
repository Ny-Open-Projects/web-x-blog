# 03-自定义realm：认证的操作步骤分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\03-自定义realm：认证的操作步骤分析_【海量资源尽在 ubkz.com】.mp4
- 时长 6分19秒（音频 379s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了我们已经改造了我们这个登录的这个方法那我们现在使用share的方式进行登录那share咱们都知道它有一个认证的这么一个过程当然也就是登录的这么一个过程那我们可以简单的一起看一下第五天这边的讲义我已经给各位打开了那在第五天里面我们详细的分析了对于share而言它进行认证也就是我们登录的这么一个逻辑
[00:28] 那我们在这边呢就直接看这张认证逻辑的这张图其实就可以了那么通过subject点击它的点login方法传递一个token过去这个token呢就是我们username and password的token里面存放了我们传递过来的用户名和密码那接着呢经过我们的security manager传递给我们左边的authenticationauthenticator这么一个我们叫做认证器
[00:52] 那认证器里面执行自己的认证逻辑执行自己的认证策略最终是不是它的认证的这些数据全部要交给我们叫做自定义的realme来做呀所以接下来我们要完成的就是在自定义的realme当中我们去搞出来一个我们用户名和密码判断的这么一套逻辑好了那接下来呢我们要做的事情就比较明确了那就是说我们要去完成自定义realme的这么一个过程
[01:22] 好了我们都知道realme其实就是realme获取安全数据的当然这安全数据其实就是登录之后你用户的一些数据比如可以得到你的用户名会得到你的用户信息角色信息直到你的权限信息等等那对于我们而言很简单咱们自定义realme需要去实现also also resendingrealmeOK那好了接下来我们可以回到代码部分自定义自己的我们叫做realme
[01:52] 好了在这边呢是有我的share我包下创建一个class把它放到realm.我叫做cast custom自定义的任务语realmok好了咱们自定义任务的时候需要我们叫做g乘a intense好了我这边已经call过来了哎静他那接着这个是我们自定义的任务语
[02:30] 那当然了对于自行日用密语来说呢需要去实现里面的两个方法或者重写里面的两个方法两个方法呢一个方法是用来做认证的一个方法是用来做授权的OK这个代码呢比较啰嗦把这个autoware去掉overwrite去掉好了那上面这个呢do get also releasinginfo这个其实是用来我们叫做做授权的这么一个方法好了那底下这个authentication info
[03:06] 它是用来我们叫做认证的方法那我们都知道在我们的登录过程当中只要借助了subject.login就会把我们这边传递过来那就会把我们这边的username和password以我们叫做token的形式传递到我们的我们域里面的认证方法里那这边参数各位比较明确了参数就是我们传递的用户名和密码
[03:37] 好了那这些我们都知道的话那接下来就是说在我这个方法里面真真正正的我们去查询数据库去比对数据库里面密码是否和我们这边我们传递过来的一致那当然了我们之前玩的这个自行RAM其实全部都是写的一些假的一些数据或者一些假的一些逻辑那我们这边真真正正的要联系数据库去查询我们叫做数据库信息那要查询的话我这边需要AutoWear
[04:05] 注入进我们的一个叫做user Service只有user Service才有我们跟数据库打交道的一些逻辑方面的一些内容在里面好了user serviceOK那好了接下来呢就是说我们这个认证方法咱们应该如何去写好了当然了我们这个逻辑呢其实还少一步啊就是我们需要去写一个vyd set我们叫做name的一个方法当然了这个set name方法呢其实就是说
[04:33] 对于我们的一个room来说呢它是通过这个指定的名称来进行判断究竟它的数据存在什么地方OK好了这边呢我们可以super super点set name好了这边呢我们就自己给它来一个比如说呢我就叫做cast room我们一般习惯把当前类名给它设置进去其实就可以了好了这些我们搞定了之后接下来围绕的就是认证那对于认证方法而言
[05:00] 那我们这边它的一个逻辑应该是怎么做呢其实不难也比较简单好了我们第一件事首先呢就应该获取你login传递过来的这个用户名密码登录的用户名和密码当然了这个用户密码全部都放在我们的token思当中好了接下来呢获取到了这些内容之后我们就可以根据我们的用户名叫做查询我们的数据库其实就是查询用户
[05:33] 好了那接下来呢接下来就可以去判断可以做一个简单的判断判断用户是否存在或者我们的密码是否匹配是否一致OK那如果一致的话就是返回我们叫做安全数据那接着如果不一致不一致很简单我们可以返回那
[05:59] 人们返回None这边简单说一下返回None它会叫做抛出异常那一旦抛出异常我们就可以进行补货就告诉它我们这边你传递的用户名和密码其实是错误的OK那好了这边我们这些逻辑都已经写好了剩下的事情就是补充里面的代码

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

