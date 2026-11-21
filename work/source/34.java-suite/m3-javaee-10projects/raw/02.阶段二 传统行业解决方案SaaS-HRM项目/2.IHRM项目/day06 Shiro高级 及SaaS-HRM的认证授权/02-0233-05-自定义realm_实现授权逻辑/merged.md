# 05-自定义realm：实现授权逻辑

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\05-自定义realm：实现授权逻辑_【海量资源尽在 ubkz.com】.mp4
- 时长 7分25秒（音频 445s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 好了我们已经完成了自定义REM的认证方法的编写当然了除了认证之外呢还有一个授权的这么一个方法那对于这个授权的方法而言呢其实我们可以把它简单的补充上那对于授权咱们都知道授权它的主要目的其实就是在操作的时候判断用户是否具有我们叫做相应的权限但是呢其权限
[00:33] 但是呢这边有一个问题想跟各位说明如果是要进行操作的时候他必然应该先进行一个认证也就是说你要执行授权我们就是先认证再进行授权好了那接着那先认证我们之前得知了有一个叫做安全数据安全数据那我们的授权方法干嘛呢其实就是根据安全数据我们进行获取用户
[01:03] 具有的叫做所有操作权限OK这个是我们授权它的一个主要的一个逻辑必须你认证也就是刚才我们写的登录的方法那认证好了之后我们存储了一些安全数据在user这里面那我们在上边就可以通过我们的叫做share或取到你存储的安全数据
[01:25] 那安全数据叫用户那用户我们可以根据用户获取用户名获取用户究竟是谁获取用户的数据获取用户的角色获取用户的权限等等那接下来我们就开始把这个授权的这个方法给它补充完整那么在进行授权的过程当中呢这个应该如何去做呢咱们也是先简单的分析一下我们的步骤那对于授权而言首先第一件事干嘛就是去获取叫做以认证的用户数据
[01:56] 数据那获取到了认证数据之后接下来我们就可以根据用户的认证数据去拿到他所有的权限信息用户的叫做权限信息当了我们这个权限信息呢可能给他包含成两个部分一部分呢就是所有角色一部分呢就是所有权限好了那接下来我们把这个方法给他构造完成
[02:30] 首先获取已认证的用户数据那认证的用户数据就是安全数据在哪放着ProSympo叫做Connection我们可以通过ProSympo Connection里面Get Primary ProSympo得到我们唯一的一个安全数据OK打点Get Primary ProSympo这个就是得到唯一的安全数据因为对于我们现在写的这个任务域里面来说只有一个我们只写了一个
[03:03] 所以这边呢我就得到唯一的或者这主要的这个安全数据因为我们刚才只存了一个吧那接下来呢我们这边可以把它强制的转化成我们的注意我们存的是用户所以这边强制转化成user等于强制转型OK那这样一来用户对象已经有了那用户对象已经有了那接着这边呢简单的再说一下我这个用户对象呢和我们这个角色以及权限全部都是配置的是多对多关系那借助SpringDataJPA
[03:37] 它的一些机制呢我们可以得知直接可以通过user获取你所具备的所有角色user打点get rows那接着通过里面的每一个rows打点get permission得到里面的所有权限所以我们不需要再去额外的韩式数据库直接就能获取那我们来看一下如何去构造我们的角色信息和权限信息那我这边呢去准备一个set这边呢我们去准备
[04:06] 我们的直接这个对象吧准备我们的返回值对象好了在SERIO当中呢一般这两个不管是认证还是我们的授权翻回都会返回这么一个INFO对象当然这些全都是接口那这边有个小的技巧告诉各位那返回的全部都是它的实现类全部都是simple开头simpleOK好了接着把这个返回值Ctrl C Ctrl V拷过来INFO等于NEWCtrl C Ctrl V拿过来
[04:36] 好了构造这么一个对象那构造好了之后我们开始fall循环那fall循环我们的user对象那我们这边user点叫做get rows得到每一个角色那接着我们得到每一个角色那我们的所有角色信息其实都是它的一些权限的一些内容或者都是我们需要的一些权限的一些信息那我们这边呢其实就可以打row打点
[05:08] 我们叫做getName咱就来Name吧getName得到角色的他的名称当然了这些内容呢我们可以把它放到一个我们的集合当中去做所以在上面呢我先去定一个set集合当然了这边用set集合此句类型的比如说呢就叫做ros等于new一个hashset那接下来呢我底下就可以ros打点add那这样一来
[05:41] 我所有的角色信息都存放到肉丝这个集合里面了那这边呢除了角色信息之外呢我们可能还有全线的所有信息我这边同样来一set集合比如说呢还是死君类型的这边呢就是perms等于new一个hcset好了上边是所有角色存储所有角色的那底下这个就是存储所有全线
[06:08] 那权限在哪呢注意我们同样的可以再来一个双层循环好了就是肉丝打点get permissions那这回我里面存放的就是打点addperm太长了改的短一点perm打点get好了我们还是跟刚才之前的按一样用code来进行存储标志那这样一来呢其实我全部的循环都已经循环结束一下
[06:40] 以后这个肉丝里面有所有的角色的相关内容这permiss里面有我所有的权限相关的内容那我们把这些内容怎么复制给info其实很简单直接调用info的方法info打点有一个叫做set stream permissions里面是所有的权限好了权限放进去info打点set我们叫做肉丝
[07:06] 好了把肉丝放进去那这样一来那这样一来我们返回info的时候那其实就已经返回了你当前这个已认证用户他所有的角色以及他所有具有权限的这些字符串相应的内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

