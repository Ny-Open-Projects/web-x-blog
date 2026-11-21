# 画面线理解：04-自定义realm：实现认证逻辑

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\04-自定义realm：实现认证逻辑_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:17, 00:43, 00:48, 00:58, 01:11, 01:24, 01:27, 01:32, 01:47, 02:11, 02:18, 03:15, 03:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:28:43

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中编写 Shiro 自定义 Realm 的 `doGetAuthenticationInfo` 方法，实现用户认证逻辑，包括获取用户名、密码、查询用户数据、校验密码并返回认证信息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 编写 `doGetAuthenticationInfo` 方法的开头，注释说明方法作用，准备获取用户名和密码。
画面 2: 代码编辑器中光标位于 `String username =` 后，准备输入变量名。
画面 3: 输入 `String username =`，并开始编写获取用户名的逻辑。
画面 4: 输入 `String password =`，并开始编写获取密码的逻辑。
画面 5: 输入 `String password = new String( upToken.getPassword());`，完成密码获取。
画面 6: 输入 `User user = userService.findByName(username);`，准备查询用户数据。
画面 7: 输入 `if (user != null && user.getPassword().equals(password)) {`，开始校验用户名和密码。
画面 8: 输入 `SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(user, user.getPassword(), this.getName());`，创建认证信息对象。
画面 9: 输入 `SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(user, user.getPassword(), this.getName());`，完成认证信息对象的创建。
画面 10: 输入 `SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(user, user.getPassword(), this.getName());`，完成认证信息对象的创建。
画面 11: 输入 `SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(user, user.getPassword(), this.getName());`，完成认证信息对象的创建。
画面 12: 输入 `SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(user, user.getPassword(), this.getName());`，完成认证信息对象的创建。
画面 13: 输入 `SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(user, user.getPassword(), this.getName());`，完成认证信息对象的创建。
画面 14: 输入 `SimpleAuthenticationInfo info = new SimpleAuthenticationInfo(user, user.getPassword(), this.getName());`，完成认证信息对象的创建。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
protected AuthenticationInfo doGetAuthenticationInfo(PrincipalCollection principalCollection) {
    return null;
}
```

画面 2:
```java
//1.获取登录的用户名密码
//2.根据用户名查询数据库
//3.判断用户是否存在或者密码是否一致
//4.如果一致返回安全数据
//5.不一致，返回null（抛出异常）
return null;
```

画面 3:
```java
protected AuthenticationInfo doGetAuthenticationInfo(PrincipalCollection principalCollection) {
    return null;
}
```

画面 4:
```java
//1.获取登录的用户名密码
//2.根据用户名查询数据库
//3.判断用户是否存在或者密码是否一致
//4.如果一致返回安全数据
//5.不一致，返回null（抛出异常）
return null;
```

画面 5:
```java
//1.获取登录的用户名密码
//2.根据用户名查询数据库
//3.判断用户是否存在或者密码是否一致
//4.如果一致返回安全数据
//5.不一致，返回null（抛出异常）
return null;
```

画面 6:
```java
//1.获取登录的用户名密码
//2.根据用户名查询数据库
//3.判断用户是否存在或者密码是否一致
//4.如果一致返回安全数据
//5.不一致，返回null（抛出异常）
return null;
```

画面 7:
```java
//1.获取登录的用户名密码
//2.根据用户名查询数据库
//3.判断用户是否存在或者密码是否一致
//4.如果一致返回安全数据
//5.不一致，返回null（抛出异常）
return null;
```

画面 8:
```java
//1.获取登录的用户名密码
//2.根据用户名查询数据库
//3.判断用户是否存在或者密码是否一致
//4.如果一致返回安全数据
//5.不一致，返回null（抛出异常）
return null;
```

画面 9:
```java
//1.获取登录的用户名密码
//2.根据用户名查询数据库
//3.判断用户是否存在或者密码是否一致
//4.如果一致返回安全数据
//5.不一致，返回null（抛出异常）
return null;
```

画面 10:
```java
//1.获取登录的用户名密码
//2.根据用户名查询数据库
//3.判断用户是否存在或者密码是否一致
//4.如果一致返回安全数据
//5.不一致，返回null（抛出异常）
return null;
```

画面 11:
```java
//1.获取登录的用户名密码
//2.根据用户名查询数据库
//3.判断用户是否存在或者密码是否一致
//4.如果一致返回安全数据
//5.不一致，返回null（抛出异常）
return null;
```

画面 12:
```java
//1.获取登录的用户名密码
//2.根据用户名查询数据库
//3.判断用户是否存在或者密码是否一致
//4.如果一致返回安全数据
//5.不一致，返回null（抛出异常）
return null;
```

画面 13:
```java
//1.获取登录的用户名密码
//2.根据用户名查询数据库
//3.判断用户是否存在或者密码是否一致
//4.如果一致返回安全数据
//5.不一致，返回null（抛出异常）
return null;
```

画面 14:
```java
//1.获取登录的用户名密码
//2.根据用户名查询数据库
//3.判断用户是否存在或者密码是否一致
//4.如果一致返回安全数据
//5.不一致，返回null（抛出异常）
return null;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
