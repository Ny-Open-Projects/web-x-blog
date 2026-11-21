# 04-自定义realm：实现认证逻辑

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\04-自定义realm：实现认证逻辑_【海量资源尽在 ubkz.com】.mp4
- 时长 3分29秒（音频 210s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们已经把步骤全部都分析出来了那接来的事情其实就比较简单了首先我们这个用户名码全部是存放在我们的token当中那我们这边需要做一个强制的一个转型把我们这个authentication token转号文我们叫做user name and password tokenok好了我这边就叫做习惯了up token等于这边做一个向下的全转型强制转型ctrl c拿过来ctrl vok好那接来呢
[00:34] 通过我们的up token可以得到用户名得到密码死菌类型的pass username等于up token打点get username好了那接下来死菌类型的我们叫做password等于up token打点我们叫做get password当然了这个password我们知道了是一个插着字符串的形式所以这边呢我需要new一个我们叫做死菌OK这样一来就已经转化好了那转化好了之后根据用户名
[01:04] 查询我们叫做数据库那根据用户名查询数据库呢这个比较简单直接就是user Service打点find by name我们把user name传递过去OK这样一来我们可以得到一个用户对象那接下来呢我们就需要做一个判断if user不等于now并且我们叫做user.getpassword需要点
[01:35] ECOS你传递过来的password这个不就是在做别角你是否为空或者密码是否一致那这个必须同时满足才可以OK那好了那这个就进入到我们判断的部分如果一致返回安全数据如果不一致返回NOW好了那接下来中间部分代码我们应该怎么去写呢其实比较简单我们需要返回返回值叫做else indication info那它呢其实也是一个抽象的这么一个
[02:05] 我们叫做接口那我们用它的一个实现类其实就可以了那这个实现类它的习惯其实就是它的自己的套路啊就是前面加simplesimple authenticationinfo比如说我就叫做info等于new一个ok那当然了这个对象呢它可以借助一些构造方法来做它的构造方法三个参数那这三个参数呢首先第一个就是我们的安全数据第二个就是我们的密码第三个就是我们的realme realme
[02:38] 域名称安全数据呢叫做安全数据安全数据那对于安全数据我们一般存的就是用户对象当然你想存放其他内容也可以比如说你自己有用户角色的一些相关的集合或者你自己想构造的一个对象都能往里存好了那么存的就放userOK好了第二个参数呢一般指的是你的密码所以我这边user.getpassword
[03:09] 好了接着第三个参数第三个参数呢就是我们当前用名用域的名称那好了我这边类似打点get name因为set name往里面存了值了我们get name直接获取过来其实就可以了OK那这样一来呢我们这个认证的方法其实也已经写好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

