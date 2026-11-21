# 20-shiro认证与授权：自定义realm-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\20-shiro认证与授权：自定义realm-下_【海量资源尽在 ubkz.com】.mp4
- 时长 9分36秒（音频 576s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了认证的方法我们写好了之后呢接下来我们关注的就是上面这个叫做授权那授权什么意思授权指的是你认证成功也就是登录成功之后我们来判断一下你当前的这个人呢是否具备操作某一个的权限好了所以这边呢我们简单的写一下授权的主要目的它就是查询就是根据认证认证的数据获取到
[00:32] 我们用户的权限信息它的主要目的就是这样你登录成功不是有一个用户吗我这里面主要目的就根据用户去得到你当前的这个权限信息那在这个里面呢注意各位那在这里面呢它提供了这么一个参数这个参数呢叫做Per Simple ConnectionPer Simple Connection这Per Simple Connection里面包含了所有已认证
[01:04] 的安全数据那我想问各位如果你登录成功了之后我们的安全数据是不是叫user name啊所以这边必然能够通过connection获取到安全数据好了那接下来呢还有一个就是返回值authorization info这个authorization info指的是我们的授权数据所以在这个方法它的主要目的就是根据你的user name去得到它的授权数据授权数据就是全信息我们一般的做法在里面应该怎么办呢首先
[01:35] 我们一般的做法一般的做法我们简单的说一下步骤第一件事获取到我们的安全数据我们指的是Uder Name当然了还有一些程序里面呢可能是用户ID好了接着第二件事那干嘛呢就可以根据ID或者名称查询用户那用户有了之后接下来呢去查询用户的角色
[02:06] 和全线信息那接着第四全线信息那接着第四件事构造我们的返回其实就可以了那这个代码呢这边呢简单说一下我只是跟各位说的正式系统我们应该这么办但是我们现在是测试所以这里面只要涉及到数据库交互的我就不写了全是写一些假数据咱们构造一下就可以那首先第一件事获取安全数据那安全数据如何去做首先获取我们存的U的内幕Posible Connection
[02:36] 打点它有一个方法打点get a primary power symbol这个power symbol它主要目的呢其实就是获取我们唯一的一个 username因为我们现在只存了一个啊因为我们现在只存了一个所以这边获取的是唯一的这么一个安全数据username获取到了那获取到了之后开始查那我这边就不查了查询用户的角色我也不查了这个都比较简单那接着我们来看一下如何去构造返回
[03:06] 那构造返回呢我们准备通过这两个方向来做我们这边不查用户角色也不查用户权信息我们自己构造string permissionprms吧等于new一个release好了那接着呢再去构造一个rosros等于也来new一个就release吧
[03:42] OK那这样一来构造了这么两个那这两个里面我们存的内容究竟存什么呢其实很简单了火米神司打点比如说你当前查询这个人他有两个角色一个叫做肉1再打点add一个叫做肉2好那接下来呢你当前查询这个角色错了上面权限底下角色如果你查询这个权限呢他有比如说呢user-sale比如说你查询这个角色呢有user-update
[04:16] OK那这个我们查询出来的内容之后呢我们开始构造返回那构造返回其实就是通过返回值我们开始构造吧AuthorationInfoInfo等于New一个AuthorationInfo放过来好了那接下来这是一个接口我们还是用的它的实现类Simple开头千万别忘了Simple开头Simple开头好了那我们构造这个太不靠谱了改一下改一下
[04:52] 好那接着来这边呢如何去做呢其实不难比较简单这个认证授权数据授权数据当中的info对象当中它有一个方法打点直接可以set死菌类型的所有权限的一个集合所以把permission设置进去设置权限我们叫做权限的集合哎抱歉是add不是set那还有一个就是设置角色集合info.addros那我们把ros
[05:32] 存进去OK那接着最后returninfo那这样一来呢我当前的这个代码呢就已经都写好了都写好了之后我们就可以做一些简单的测试了那简单测试首先呢我们进行认证登录那进来这方法那存了我们一个Uter name那接下来呢这边是不是就可以叫做获取授权那可以判断一下它是否具有决策一是否具有save方法那好了接下来我们把这个测试也给它了
[06:02] 补充完成好了这边所有都关掉测试这边Ctrl C Ctrl Vcall一个我们的测试类第三个好了那这回呢我们构造的过程当中呢咱们根据的是第三个配置文件构造的那第三个配置文件如果各位有一点点淡忘的话我们可以找到它里面指定了我的自己写到的RemoU被配置到了我们的Security Manager当中所以这样一来我的Security Manager当中其实已经知道了我认证要走哪个方法我授权要走哪个方法
[06:34] 那我们的这个代码部分呢其实都差不多都差不多基本上跟这个逻辑是一样是一模一样的那我们可以执行一下看一下方法好了比如说呢我就传张三那张三一登录你点login那这回点击login的时候他会自动的找到我们的日母域中的我们叫做认证方法
[07:08] 它自动找然后呢根据我们的认证方法里面的用户名领域码是否匹配开始做执行那这一回呢由于有了real那这里面呢去判断我们的授权那授权它做的事情就是自动的去根据我们的real与这中的叫做授权方法它就会自动去找去匹配了好了我们一起执行一把看一下好了张三123456
[07:47] 那这边报了一个错误啊我们一起来看一下往下走No rooms has beenconfiguredwhen all more rooms must be presented toexecuteN好了这个代码呢咱们来看一下究竟哪出问题了这个错误部分呢我们简单的看这边是小配置configuring那我们这个工程呢运行的是第三个配置文件那我们找到第三个配置文件简单的来看一下
[08:20] 抱歉这边是MEN是MEN吧MEN好了这个才是配置那这个我们搞了之后呢接下来再来看一下还是这样那我们当登录成功的时候由于在我们的realmooly当中进行登录如果登录成功去判断是否有肉依是否有save方法那么来看一下这边是不是有肉依是不是有save方法那好了为了让我这个问题更加直观一下我这边打一句话好了执行就是
[08:53] 授权方法吧好了底下呢就给他来一个执行认证方法OK我们再来做一下测试那走OK各位来看先去执行认证方法接着执行授权接着执行授权为什么呢是因为我们这边授权是判断了是不是有肉依是不是还有这个U的C方法呀所以通过这个案例想让各位知道就是我们可以自己进行一个任务
[09:23] 定义它的认证方法定义它的授权方法当你授权的时候它会自动的在你的授权权益信息里面帮你进行构造构造好了之后帮你判断它是否具备当前的这个角色当前这个权限OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Shiro 中自定义 Realm 实现用户认证与授权，并通过测试类验证功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PermissionRealm.java 文件，定义了 setRealmName 方法和 doGetAuthorizationInfo 方法的骨架，注释说明了授权逻辑。
画面 2: 展示 PermissionRealm.java 文件，聚焦在 doGetAuthorizationInfo 方法，准备实现授权逻辑。
画面 3: 在 doGetAuthorizationInfo 方法中，通过 IDE 的自动补全功能，选择获取当前用户 Principal 的方法 getPrimaryPrincipal()。
画面 4: 在 doGetAuthorizationInfo 方法中，通过 IDE 的自动补全功能，选择创建 List<String> 的方法 new ArrayList<>()。
画面 5: 在 doGetAuthorizationInfo 方法中，创建了用于存储权限和角色的 List<String> 对象 perms 和 roles。
画面 6: 在 doGetAuthorizationInfo 方法中，通过 IDE 的自动补全功能，选择创建 SimpleAuthorizationInfo 对象的方法 new SimpleAuthorizationInfo()。
画面 7: 在 doGetAuthorizationInfo 方法中，通过 IDE 的自动补全功能，选择 SimpleAuthorizationInfo 对象的 addStringPermissions 方法。
画面 8: 在 doGetAuthorizationInfo 方法中，通过 IDE 的自动补全功能，选择 SimpleAuthorizationInfo 对象的 addRoles 方法。
画面 9: 在 doGetAuthorizationInfo 方法中，完成授权信息的构造，返回 SimpleAuthorizationInfo 对象。
画面 10: 展示 ShiroTest02.java 文件，通过 IDE 的“Copy Class”功能，将 ShiroTest02 复制到 ShiroTest03。
画面 11: 展示 ShiroTest03.java 文件，初始化 SecurityManager，加载 shiro-test-3.ini 配置文件。
画面 12: 展示 ShiroTest03.java 文件，执行 testLogin 方法，测试登录和权限验证，但测试失败，提示“必须存在一个或多个 realm 才能执行认证尝试”。
画面 13: 展示 ShiroTest03.java 文件，测试失败，提示“无法加载类 org.slf4j.impl.StaticLoggerBinder”。
画面 14: 展示 ShiroTest03.java 文件，测试失败，提示“无法加载类 org.slf4j.impl.StaticLoggerBinder”，但编译成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public class PermissionRealm extends AuthorizingRealm {
    /**
     * 自定义realm名称
     */
    public void setName(String name) {
        super.setName("permissionRealm");
    }
    //授权
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        return null;
    }
    //认证，认证的主要目的，比较用户名和密码是否与数据库中的一致
    //将安全数据存入到shiro进行保管
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        //1.构造upToken
        UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
        //2.获取输入的用户名密码
        String username = upToken.getUsername();
        String password = new String(upToken.getPassword());
        //3.比对数据库中用户密码是否一致（密码可能被加密）
        if("123456".equals(password)) {
            return null;
        }
    }
}
```

画面 2:
```java
//授权
protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
    return null;
}
```

画面 3:
```java
//获取安全数据 username, userId
String username = (String)principalCollection.getPrimaryPrincipal();
```

画面 4:
```java
List<String> perms = new ArrayList<>();
```

画面 5:
```java
//1.获取安全数据 username, userId
String username = (String)principalCollection.getPrimaryPrincipal();
//2.根据id或者名称查询用户
//3.查询该用户的角色和权限信息
List<String> perms = new ArrayList<>();
List<String> roles = new ArrayList<>();
```

画面 6:
```java
//4.构造返回
return null;
```

画面 7:
```java
AuthorizationInfo info = new AuthorizationInfo();
```

画面 8:
```java
info.addStringPermissions(perms);
info.addRoles(roles);
```

画面 9:
```java
//1.构造授权信息
//2.设置角色和权限
SimpleAuthorizationInfo info = new SimpleAuthorizationInfo();
info.addStringPermissions(perms);
info.addRoles(roles);
return info;
```

画面 10:
```java
Copy class cn.itcast.shiro.ShiroTest02
New name: ShiroTest03
Destination package: cn.itcast.shiro
Target destination directory: [shiro_demo]_shiro_demo/src/test/java/cn/itcast/shiro
```

画面 11:
```java
public void init() {
    //1.根据配置文件创建SecurityManagerFactory
    Factory<SecurityManager> factory = new IniSecurityManagerFactory("classpath:shiro-test-3.ini");
    //2.通过工厂获取SecurityManager
    SecurityManager securityManager = factory.getInstance();
    //3.SecurityManager设置到当前线程中
    SecurityUtils.setSecurityManager(securityManager);
}
@Test
public void testLogin() {
    Subject subject = SecurityUtils.getSubject();
    String username = "lisi";
    String password = "123456";
    UsernamePasswordToken token = new UsernamePasswordToken(username, password);
    //执行login方法，完成登录
    subject.login(token);
    //授权，检测当前登录用户是否具有操作权限、是否具有某个角色
    System.out.println(subject.hasRole("role1"));
    System.out.println(subject.isPermitted("user:save"));
}
```

画面 12:
```java
//执行login方法，完成登录
subject.login(token);
//授权，检测当前登录用户是否具有操作权限、是否具有某个角色
System.out.println(subject.hasRole("role1"));
System.out.println(subject.isPermitted("user:save"));
```

画面 13:
```java
//执行login方法，完成登录
subject.login(token);
//授权，检测当前登录用户是否具有操作权限、是否具有某个角色
System.out.println(subject.hasRole("role1"));
System.out.println(subject.isPermitted("user:save"));
```

画面 14:
```java
//执行login方法，完成登录
subject.login(token);
//授权，检测当前登录用户是否具有操作权限、是否具有某个角色
System.out.println(subject.hasRole("role1"));
System.out.println(subject.isPermitted("user:save"));
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

