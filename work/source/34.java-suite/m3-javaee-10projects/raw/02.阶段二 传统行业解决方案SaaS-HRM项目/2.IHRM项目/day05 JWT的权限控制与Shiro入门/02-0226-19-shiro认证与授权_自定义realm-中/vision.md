# 画面线理解：19-shiro认证与授权：自定义realm-中

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\19-shiro认证与授权：自定义realm-中_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:39, 03:16, 03:21, 03:29, 04:12, 04:26, 04:53, 04:55, 05:23, 05:29, 06:12, 06:16, 06:21, 06:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:19:40

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中编写并调试 Shiro 自定义 Realm 的 `doGetAuthenticationInfo` 方法，实现用户认证逻辑，包括获取用户名密码、比对、成功时返回认证信息、失败时抛出异常。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 编辑器显示 `PermissionRealm.java` 文件，其中 `doGetAuthenticationInfo` 方法的初始代码为 `return null;`。
- 代码注释说明：认证目的、参数、安全数据存入 Shiro、失败时返回 null。
- 画面底部显示测试通过信息。

画面 2：
- 代码编辑器中，光标位于 `doGetAuthenticationInfo` 方法内，正在输入 `String` 类型的变量声明。
- IDE 提示选择类型或输入点号。
- 画面底部显示测试通过信息。

画面 3：
- 代码编辑器中，光标位于 `doGetAuthenticationInfo` 方法内，正在输入 `String` 类型的变量声明。
- IDE 提示选择类型或输入点号。
- 画面底部显示测试通过信息。

画面 4：
- 代码编辑器中，光标位于 `doGetAuthenticationInfo` 方法内，正在输入 `String` 类型的变量声明。
- IDE 提示选择类型或输入点号。
- 画面底部显示测试通过信息。

画面 5：
- 代码编辑器中，光标位于 `doGetAuthenticationInfo` 方法内，正在输入 `String` 类型的变量声明。
- IDE 提示选择类型或输入点号。
- 画面底部显示测试通过信息。

画面 6：
- 代码编辑器中，光标位于 `doGetAuthenticationInfo` 方法内，正在输入 `String` 类型的变量声明。
- IDE 提示选择类型或输入点号。
- 画面底部显示测试通过信息。

画面 7：
- 代码编辑器中，光标位于 `doGetAuthenticationInfo` 方法内，正在输入 `String` 类型的变量声明。
- IDE 提示选择类型或输入点号。
- 画面底部显示测试通过信息。

画面 8：
- 代码编辑器中，光标位于 `doGetAuthenticationInfo` 方法内，正在输入 `String` 类型的变量声明。
- IDE 提示选择类型或输入点号。
- 画面底部显示测试通过信息。

画面 9：
- 代码编辑器中，光标位于 `doGetAuthenticationInfo` 方法内，正在输入 `String` 类型的变量声明。
- IDE 提示选择类型或输入点号。
- 画面底部显示测试通过信息。

画面 10：
- 代码编辑器中，光标位于 `doGetAuthenticationInfo` 方法内，正在输入 `String` 类型的变量声明。
- IDE 提示选择类型或输入点号。
- 画面底部显示测试通过信息。

画面 11：
- 代码编辑器中，光标位于 `doGetAuthenticationInfo` 方法内，正在输入 `String` 类型的变量声明。
- IDE 提示选择类型或输入点号。
- 画面底部显示测试通过信息。

画面 12：
- 代码编辑器中，光标位于 `doGetAuthenticationInfo` 方法内，正在输入 `String` 类型的变量声明。
- IDE 提示选择类型或输入点号。
- 画面底部显示测试通过信息。

画面 13：
- 代码编辑器中，光标位于 `doGetAuthenticationInfo` 方法内，正在输入 `String` 类型的变量声明。
- IDE 提示选择类型或输入点号。
- 画面底部显示测试通过信息。

画面 14：
- 代码编辑器中，光标位于 `doGetAuthenticationInfo` 方法内，正在输入 `String` 类型的变量声明。
- IDE 提示选择类型或输入点号。
- 画面底部显示测试通过信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```java
public class PermissionRealm extends AuthorizingRealm {
    /**
     * 自定义realm名称
     */
    public void setRealmName(String name) {
        super.setRealmName("permissionRealm");
    }

    //授权
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        return null;
    }

    //认证，认证的主要目的，比对用户名和密码是否与数据库中的一致
    //有安全数据存入到shiro进行传递
    //参数：authenticationToken登录构造的usernamepasswordtoken
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        return null;
    }
}
```

画面 4：
```java
//1.获取用户输入的用户名密码
UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
String username = upToken.getUsername();
String password = new String(upToken.getPassword());
//4.比对密码和数据库中的密码是否一致（密码可能需要加密）
//5.如果成功，向shiro存入安全数据
//6.失败，抛出异常或返回null
```

画面 8：
```java
//1.获取用户输入的用户名密码
UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
String username = upToken.getUsername();
String password = new String(upToken.getPassword());
//4.比对密码和数据库中的密码是否一致（密码可能需要加密）
//5.如果成功，向shiro存入安全数据
//6.失败，抛出异常或返回null
```

画面 11：
```java
//1.获取用户输入的用户名密码
UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
String username = upToken.getUsername();
String password = new String(upToken.getPassword());
//4.比对密码和数据库中的密码是否一致（密码可能需要加密）
//5.如果成功，向shiro存入安全数据
//6.失败，抛出异常或返回null
```

画面 12：
```java
//1.获取用户输入的用户名密码
UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
String username = upToken.getUsername();
String password = new String(upToken.getPassword());
//4.比对密码和数据库中的密码是否一致（密码可能需要加密）
//5.如果成功，向shiro存入安全数据
//6.失败，抛出异常或返回null
```

画面 13：
```java
//1.获取用户输入的用户名密码
UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
String username = upToken.getUsername();
String password = new String(upToken.getPassword());
//4.比对密码和数据库中的密码是否一致（密码可能需要加密）
//5.如果成功，向shiro存入安全数据
//6.失败，抛出异常或返回null
```

画面 14：
```java
//1.获取用户输入的用户名密码
UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
String username = upToken.getUsername();
String password = new String(upToken.getPassword());
//4.比对密码和数据库中的密码是否一致（密码可能需要加密）
//5.如果成功，向shiro存入安全数据
//6.失败，抛出异常或返回null
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
