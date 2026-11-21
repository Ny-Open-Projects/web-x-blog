# 画面线理解：20-shiro认证与授权：自定义realm-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\20-shiro认证与授权：自定义realm-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:10, 02:45, 03:13, 03:31, 03:50, 04:33, 05:29, 05:46, 06:08, 06:33, 08:05, 08:31, 09:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:20:20

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
