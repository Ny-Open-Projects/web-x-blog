# 18-shiro认证与授权：自定义realm-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\18-shiro认证与授权：自定义realm-上_【海量资源尽在 ubkz.com】.mp4
- 时长 6分34秒（音频 394s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们简单的看了一下这种基于NI的用户的认证以及授权那其实我们发现使用Sherlock进行认证授权的话比较简单直接就能进行一个判断那接下来我们想说了就是对于咱们真实的企业当中应用的话其实没有人说以配置文件的形式去搞这些内容这个就太不灵活了那在我们真实的应用场景当中呢这个我们的用户的数据我们的这些它的权限的一些信息
[00:30] 是不是应该存放到数据库当中去进行存储那这个时候呢就要求我们那这些内容应该想方设法的从数据库进行提取出来那这个就涉及到了我们刚才给各位介绍share的时候说过的这个叫做RAM因为RAM是我们安全数据的来源那这些数据从哪来我们应该在RAM当中想方设法的跟我们的底层数据库进行交互所以接下来我们来看一下如何去自己定一个RAM在RAM当中去
[01:00] 完成用户的认证完成用户的授权等等的这些操作那好了在这边呢我去定义我们的一个新的一个配置文件Ctrl C Ctrl A好了这个配置文件呢我就叫做-3了-3那这个配置文件里面注意这回跟我们之前的写法都不太一样因为这个里面要用到了
[01:26] 第一个叫做MEM它其实就是定义我们全部配置文件的一个声明部分在这个声明部分里面首先呢PRM这个REM是我们自己定义的REM的域这个REM一般也叫做REM域那这个REM域应该写到哪我把它比如说写到cn.itcast.share.就是Promission注意这个是我们自己要填写的并且要写到这个包下那这样一来Share就知道了我有一个REM
[01:56] 那接下来呢我们这个REM是不是应该统一交给Security Manager进行管理所以接下来呢我要做的是第二件事就是注册REM少写一个L注册这个REM我们叫做Security ManagerM-A-N-A-J-R好了那接下来如何去注册呢其实也不难Security Manager点它有一个方法点REMS等于
[02:29] 导致引用一下我们刚才创建的这关系好了这样一来我的配置文件已经搞定了那配置文件搞定了之后就是说呀那在我这个工程当中呢这边已经局限了我要写ROM就必须要写在这个包下并且以它进行命名所以接下来呢我就可以Ctrl C Copy过来Ctrl C Copy过来在我的jar 包下在我的Java目录下去创建我们的一个ROM域好了这个里面是我们自定的ROM域对象对象
[03:04] 那我们自定义用文语对象应该如何去写呢那我们需要注意需要继承继承一个room它叫做also aothresisting roomaoth算了我在这边直接写吧继承一个tenseaothorizinroom好了继承它那继承它之后呢需要
[03:37] 我们叫做重写里面的方法其中的方法那这个方法呢一共有两个我们一起来看一下好了这两个方法呢第一个方法呢这个方法都比较长啊而且也比较绕叫做do get also recession info好了第二个叫做do getauthentication info那这两个究竟代表的是啥意思首先上面这个代表的是授权
[04:17] 那好了底下这个代表的是认证那好了接下来呢我们就对这几个方法呢做一个简单的声明授权方法那授权方法其实就是获取到里面的主要目的就是获取到用户的授权数据那授权数据说的还是比较正式里面其实就是用户的用户的权限数据主要目的就是干这个的那还有第二个
[04:51] 第二个呢叫做do get authentication info它的主要目的就是用来认证那认证的目的是干嘛呢就是根据用户名密码判断就是进行登录根据用户名密码进行登录那登录了之后呢可以将我们的用户数据保存它做的事情就这两个所以这个认证其实就是我们传统的登录授权呢其实就是判断一些数据的
[05:23] 那好了这个将用户数据保存这个用户数据呢我们叫做安全数据安全数据OK好这两个方法我们看过了之后接下来就是说这两个方法里面如何去写那在这边的写自定义room的时候呢一般我们还会重写它其中的一个方法就是叫做setName重写它里面的方法好了我这边直接写吧public viewid叫做setName
[05:53] 此句类型的name因为这个日用文语啊可能又写很多它是通过这个name的方式进行辨别的直接super点再name好了把name传进去就是这个name呢就是你当前叫什么名字我们一般推荐就是你当前这个日用文语你写的叫什么名字这边就写什么其实就可以了OK这个一般的我们都要这么做定义日用文名
[06:20] 因为这个room可能写很多那这个时候呢在shadow当中它有一个认证处理的一个过程那处理的过程一般是根据名称的形式来做的好了那这个一来呢我基本的这个方法的结构咱们就已经构建出来了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

