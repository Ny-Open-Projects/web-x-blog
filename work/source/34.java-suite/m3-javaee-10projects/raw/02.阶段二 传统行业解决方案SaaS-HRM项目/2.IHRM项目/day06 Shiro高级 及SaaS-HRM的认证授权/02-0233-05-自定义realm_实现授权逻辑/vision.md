# 画面线理解：05-自定义realm：实现授权逻辑

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\05-自定义realm：实现授权逻辑_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:13, 01:19, 03:07, 03:21, 03:39, 04:31, 05:08, 05:25, 05:36, 05:54, 06:17, 06:41, 07:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:29:34

1) 这一组画面整体在讲什么（一句话）：
在 Shiro 框架中，自定义 Realm 实现用户认证与授权逻辑，重点是构建 `doGetAuthorizationInfo` 方法以获取用户角色和权限信息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `CustomRealm.java` 中 `doGetAuthenticationInfo` 方法的实现，包含获取用户名、密码、调用 `userService.findByUsername` 查询用户、MD5 加密比对密码、创建 `SimpleAuthenticationInfo` 对象。
画面2：光标在 `doGetAuthorizationInfo` 方法的 `return null;` 行，方法体为空。
画面3：光标在 `doGetAuthorizationInfo` 方法的 `return null;` 行，方法体为空。
画面4：在 `doGetAuthorizationInfo` 方法中，调用 `principalCollection.getPrimaryPrincipal()` 获取用户对象。
画面5：在 `doGetAuthorizationInfo` 方法中，尝试将 `getPrimaryPrincipal()` 的返回值强制转换为 `User` 类型，IDE 提示类型不匹配。
画面6：展示 `UserController.java` 中 `login` 方法，通过 `SecurityUtils.getSubject()` 获取 Subject，调用 `subject.login(upToken)` 进行登录。
画面7：在 `doGetAuthorizationInfo` 方法中，尝试创建 `SimpleAuthorizationInfo` 对象，但 IDE 报错“Cannot resolve symbol 'SimpleAuthorizationInfo'”。
画面8：在 `doGetAuthorizationInfo` 方法中，光标在 `principalCollection` 的 `getPrimaryPrincipal()` 方法调用处，IDE 显示 `User` 类的 `toString()` 方法。
画面9：在 `doGetAuthorizationInfo` 方法中，将 `principalCollection.getPrimaryPrincipal()` 强制转换为 `User` 类型，并创建 `SimpleAuthorizationInfo` 对象。
画面10：在 `doGetAuthorizationInfo` 方法中，光标在 `Set<String> roles = new HashSet<>();` 行，IDE 显示 `Set` 接口的方法。
画面11：在 `doGetAuthorizationInfo` 方法中，光标在 `Set<String> perms = new HashSet<>();` 行，IDE 显示 `Set` 接口的方法。
画面12：在 `doGetAuthorizationInfo` 方法中，光标在 `roles.add(role.getName());` 行，IDE 显示 `Set` 接口的 `add` 方法。
画面13：在 `doGetAuthorizationInfo` 方法中，光标在 `perms.add(perm.getcode());` 行，IDE 显示 `Set` 接口的 `add` 方法。
画面14：在 `doGetAuthorizationInfo` 方法中，光标在 `info.setObjectPermissions(perms);` 行，IDE 显示 `SimpleAuthorizationInfo` 类的 `setObjectPermissions` 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
    return null;
}

/**
 * 认证方法
 * 参数：传递的用户名密码
 */
protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
    UsernamePasswordToken upToken = (UsernamePasswordToken) authenticationToken;
    String username = upToken.getUsername();
    String password = new String(upToken.getPassword());
    //1.根据用户名查询用户
    User user = userService.findByName(username);
    //2.判断用户是否存在或者密码是否一致
    //密码加密，md5加密shiro以及提供了好了
    //111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
