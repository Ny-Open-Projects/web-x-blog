# 19-shiro认证与授权：自定义realm-中

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\19-shiro认证与授权：自定义realm-中_【海量资源尽在 ubkz.com】.mp4
- 时长 6分31秒（音频 392s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了接下来呢我们关注的就是这个任务里面当中的两个方法首先呢我们先写认证方法那么先来明白一下认证的主要目的其实是干嘛我们刚才知道认证就是用户登录其实它主要做的事情就是比较用户名和密码是否与数据库中的一致那如果比较成功的话它就会存将我们的安全数据存入到
[00:31] share还进行保管好了那接下来保管那接下来呢我们关注的就是这个认证的这个方法那认证的方法由于这边说过了要比较用户名利码是否和数据会一致因为这个用户名利码是不是用户传递过来的那这个用户名利码在哪呢注意各位如果你够细心的话你会发到你这边有一个token那这个token呢指的是认证token那如果还有印象的话我们之前是不是写了一个叫做yodename password token那玩意儿不就是它的一个实现吗
[01:04] 所以对于我们来说你在登录的时候user name password token那我们这边就可以把它转化过来所以这边有一个参数那这个参数指的就是我们登录构造的user name password token所以对于我们来说很简单我们这边先做一个强制转型转化成user name password token那这边简单写一下步骤啊第一个构造
[01:38] UP token 我写UP token了写的简单一点UP token好了UV token有了之后接着获取你输入的用户名密码好了接着第三件事我们可以根据用户名查询数据库好了接着第四件事我们就是开始比较密码和数据库中的
[02:05] 密码是否一致当然了这边的也有一点点细节问题就是这个密码可能需要加密好了这个加密的过程我们这边就因为是一个简单的案例就是全部都从简了就不再写了好了第五个如果成功向shadow存入安全数据好了第六个如果失败
[02:35] 那如果失败呢我们可以做一个简单粗炮的抛出异常也好当然了你不想抛出异常返回NOW也行或返回NOW都可以那好了我们一个一个来看首先构造UP Token那UP Token呢比较简单了由NIMPASO的Token写到上边就叫UP Token好了做一个强制转型把接口向上转型向下转型转现成我们的实现类好了接下来获取用户密码获取用户密码比较简单死去类型的
[03:17] user name等于up token打点get username死菌类型的我们叫做password等于注意new一个死菌因为在这个up token当中啊它里面是把密码以chart数组的形式给我们获取过来的所以get password得的是一个chart数组所以我这边做一个简单的转型给它转化成user name password好了接下来呢数据库查询啊查询数据库密码那查询数据库密码
[03:44] 我这个就不太好说因为我们现在没有数据库所以我这边做一个简单的比较就行了if我查询数据库我就省略了咱们之后正式系统肯定是要查询的我们这边呢就为了测试啊所以我这边呢跟第三步第四步我就给它合并到一起了我在这边呢直接比较你输的密码如果它等于123456.ecos你输的密码我就认为搞定了所以我这个用户密码我就不查数据库了行吧
[04:19] 我这边直接就是默认用户名码123456我进比较这样一来如果比较成功那我要做什么else如果比较失败我就可以抛出异常好那接着呢我们开始给它完成如果成功的话我刚才说过了第三第四步其实是我们省略的做法是正式启动肯定根据用户名去查查完了之后再比较所以我这边为了简单呢我就直接比较123456了好了那接下来接下来
[04:49] 那如果说失败的话我们这边可以选择性的抛出一个异常死肉new一个比如说叫做rentime exception里面可以加点内容比如说用户名用户名或密码失败用户名或密码错误好那接下来如果成功那成功的话就是想方设法的往里面存数据那存数据怎么办这个数据在哪我们需要构造一个叫做认证的这么一个数据info那这个认证数据呢我们一般用的是它的这也是一个接口我们用的是它的一个时间类
[05:23] simple authentication authenticationinfo好了info等于new一个simple authenticationinfo那么new的过程可以选择它的构造方法那这个构造方法里面可以传递这么三个参数那第一个参数安全数据第二个参数密码第三个数据就是你当前任务域的名称第一个参数指的是我们的安全数据你想存什么你就写什么你想存用户对象你就构造用户对象你想存用户名你就写用户名
[05:56] 好了第二个参数一般是我的密码好了第三个参数就是当前Rail密域的名称OK那接着我们这边为了简单呢我就把当前登录成功的这个密码用户名放到这边了密码呢我就放password了好了第三个RailGetName咱们写了setName放进去GetName就能获取到这个是它附内里面的提供的一些方法OK那接着最后returnInfo那这样一来我已经把认证的方法写好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

