# 19-SasSHRM中基于shiro的认证授权：自定义realm-认证

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\19-SasSHRM中基于shiro的认证授权：自定义realm-认证_【海量资源尽在 ubkz.com】.mp4
- 时长 6分13秒（音频 374s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那我们用户进行登录之后调用subject.login那我们都知道要进入到我们自定义room当中去完成认证的这个逻辑那么这个认证的这个room进入哪个呢注意是让它进入到我们系统微服务当中我们刚才写过一个叫做user room是我们当前这个系统里面独用的或者独有的room这个里面我们专注里面的认证方法其实就可以了那接着我们就是说了对于这个认证方法我们如何进行编辑它的一个逻辑是什么样的
[00:32] 首先第一个点就是我们要获取到用户的手机号和密码获取到了之后接着根据我们的手机号手机号查询我们的用户那好了接下来第三件事就是判断用户是否存在判断用户密码是否和输入密码一致好了那接下来第四件事就是构造我们叫做安全数据
[01:02] 并返回好了那接下来就是说呢对于我们这几个逻辑当中有一个啊就是说构造安全数据并返回那我们现在这个系统的安全数据各位觉得各位觉得这个安全数据应该包含什么样的内容就可以了那有的人朋友说user那user当然可以当然可以那么这个user内容呢其实就是我们这个model当中system里面的user对象那各位来看这个user对象里面的内容
[01:34] 好像有点多好像有点多那除了这个优德里面呢它还包含了我们的肉丝角色那这个角色里面还关联了我们叫做权限这个内容确实是有点多了那对于我们的安全数据我们着重考量的其实就是说这个里面应该要包含用户的基本数据以及它的权限信息其实就可以了
[01:58] 因为我们授权主要是为了要到它的全新信息以及用户的一些基本数据比如说用户的ID用户的企业ID用户所属企业的名称等等其实就够了我们这边为了简单是这样的注意我们用户登录成功之后我准备给它构造一个安全数据而这个安全数据就跟我们底下用户详细信息它里面的profile result就跟它保持一致了因为这个profile result我们是
[02:28] 获取用户信息里面的一些内容里面有手机号里面有用户名里面有它的比如说呢公司和公司的ID当然里面还有一个MAP集合肉丝那这个肉丝里面有有菜单权限有按钮权限有我们的API权限那对于我们而言这个更加合适所以我们要要构造的其实就是把它作为安全数据构造出来其实就可以了那我们都知道这个安全数据最终要访问到Redis里面存在到Redis里面我们需要去实现
[02:55] implements两个接口一个叫做serializable好了另一个接口呢我们叫做also catch就是poursimple好了实现also catch poursimple我们实现它的一个方法当然这个方法空方法返回none即可好了这些呢我们都做了一些简单的分析那我们得知到安全书记其实就可以用profile result就可以了好了剩下我们把代码给它搞定即可那搞定这个代码呢这个代码的部分呢
[03:24] 都不难我就从这边呢简单的call一段了我们之前写过的这个逻辑call一段好了Ctrl C Ctrl V call过来好了Ctrl C Ctrl V call一块当然这样是就稍微快一点嘛OK好了那接下来呢我们做一个简单的修改就可以了在这边由于要跟数据库交互at all to whereprivate我们的user Service
[03:57] 那接下来呢就是说我们刚才登录存储的不叫做username我们存储的叫做password存储的叫做mobile那我们的userservice就应该打点叫做find by mobile把mobile传递进去得到我们的用户对象那接下来判断用户不存用户如果不为难那并且用户的密码也匹配那也匹配的话底下我们就开始去构造安全数据了
[04:28] 那我们底下构造安全数据的时候我们的安全数据呢其实是一个profile这么一个对象所以我在这边需要构造出profile等于那那千万别忘了我们这个权限的数据呢在profile里面都有体现并且我们可以根据用户的他的不同的级别构造不同的权限那这个里面的代码其实跟我们这个profile这个方法我们之前写获取用户信息这个方法其实是一样的
[04:57] 所以在这边呢我把它直接Ctrl C靠到这边Ctrl V就可以了如果是一个普通用户从用户里面获取里面的权限如果不是普通用户那这一回我们直接查询权限信息即可那这边呢我们需要注入PrivatePromission ServicePromission ServiceOK底下就可以通过Promission Service直接根据你这个用户的级别去查询他所具备的所有权限
[05:26] OK那接着调用里面我们之前写好的构造方法构造出安全数据result那接下来我们可以返回simpleauthenticationinfo那构造authenticationinfo的构造方法第一个参数用数据第二个密码第三个realme域的名称好了这回呢不写user了我们是result那password没问题类似点get username也没问题OK那这样一来我们就已经把这个认证的逻辑写好了当然了我们这边return non的时候简单的说一下
[05:56] return null返回 null它会抛出异常表示用户名和密码不匹配OK那这样一来我们这个认证的这个逻辑就已经写好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
展示一个基于 Spring Boot 和 Shiro 的用户登录与权限认证系统的核心代码实现，包括控制器、Realm、实体类和响应结果类。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 UserContoller.java 中的 login 方法，用于处理用户登录请求。
- 代码中使用了 @RequestMapping 注解，路径为 "/login"，方法为 POST。
- 代码中使用了 MdsHash 对密码进行加密，调用 SecurityUtils 获取 Subject。
- 代码中使用了 Result 返回登录结果，包含 ResultCode 和 sessionId。

画面 2：
- 展示 UserRealm.java 文件，这是 Shiro 的认证 Realm。
- 代码中定义了 doGetAuthenticationInfo 方法，用于获取用户认证信息。
- 代码中使用了 UserRealm extends IrmRealm，继承自 IrmRealm。
- 代码中使用了 import org.apache.shiro.authc.AuthenticationException; 等导入语句。

画面 3：
- 展示 User.java 文件，这是用户实体类。
- 代码中定义了多个私有属性，如 password、enableState、createTime、companyId、companyName、departmentId、timeOfEntry、formOfEmployment。
- 代码中使用了注释说明属性含义。

画面 4：
- 展示 UserContoller.java 中的 login 方法，与画面 1 类似。
- 代码中使用了 MdsHash 对密码进行加密，调用 SecurityUtils 获取 Subject。
- 代码中使用了 Result 返回登录结果，包含 ResultCode 和 sessionId。

画面 5：
- 展示 ProfileResult.java 文件，这是用户信息响应结果类。
- 代码中定义了私有属性，如 mobile、username、companyId、roles。
- 代码中使用了 @Setter 和 @Getter 注解，用于自动生成 getter 和 setter 方法。
- 代码中定义了构造方法，用于初始化属性。

画面 6：
- 展示 ProfileResult.java 文件，与画面 5 类似。
- 代码中定义了私有属性，如 mobile、username、companyId、roles。
- 代码中使用了 @Setter 和 @Getter 注解，用于自动生成 getter 和 setter 方法。
- 代码中定义了构造方法，用于初始化属性。

画面 7：
- 展示 ProfileResult.java 文件，与画面 5 和 6 类似。
- 代码中定义了构造方法，用于初始化属性。
- 代码中使用了 for 循环，遍历 Permission 列表，根据类型添加到 menus 或 aps 集合中。

画面 8：
- 展示 UserRealm.java 文件，与画面 2 类似。
- 代码中定义了 doGetAuthenticationInfo 方法，用于获取用户认证信息。
- 代码中使用了 UserRealm extends IrmRealm，继承自 IrmRealm。
- 代码中使用了 import org.apache.shiro.authc.AuthenticationException; 等导入语句。

画面 9：
- 展示 UserRealm.java 文件，与画面 2 和 8 类似。
- 代码中定义了 doGetAuthenticationInfo 方法，用于获取用户认证信息。
- 代码中使用了 UserRealm extends IrmRealm，继承自 IrmRealm。
- 代码中使用了 import org.apache.shiro.authc.AuthenticationException; 等导入语句。

画面 10：
- 展示 UserRealm.java 文件，与画面 2、8 和 9 类似。
- 代码中定义了 doGetAuthenticationInfo 方法，用于获取用户认证信息。
- 代码中使用了 UserRealm extends IrmRealm，继承自 IrmRealm。
- 代码中使用了 import org.apache.shiro.authc.AuthenticationException; 等导入语句。

画面 11：
- 展示 UserContoller.java 中的 profile 方法，用于处理用户信息查询请求。
- 代码中使用了 @RequestMapping 注解，路径为 "/profile"，方法为 POST。
- 代码中使用了 HttpServletRequest 获取用户 ID。
- 代码中使用了 userService.findBId 方法获取用户信息。
- 代码中使用了 ProfileResult 类返回用户信息。

画面 12：
- 展示 UserRealm.java 文件，与画面 2、8、9 和 10 类似。
- 代码中定义了 doGetAuthenticationInfo 方法，用于获取用户认证信息。
- 代码中使用了 UserRealm extends IrmRealm，继承自 IrmRealm。
- 代码中使用了 import org.apache.shiro.authc.AuthenticationException; 等导入语句。

画面 13：
- 展示 UserRealm.java 文件，与画面 2、8、9、10 和 12 类似。
- 代码中定义了 doGetAuthenticationInfo 方法，用于获取用户认证信息。
- 代码中使用了 UserRealm extends IrmRealm，继承自 IrmRealm。
- 代码中使用了 import org.apache.shiro.authc.AuthenticationException; 等导入语句。

画面 14：
- 展示 UserRealm.java 文件，与画面 2、8、9、10、12 和 13 类似。
- 代码中定义了 doGetAuthenticationInfo 方法，用于获取用户认证信息。
- 代码中使用了 UserRealm extends IrmRealm，继承自 IrmRealm。
- 代码中使用了 import org.apache.shiro.authc.AuthenticationException; 等导入语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```java
@RequestMapping(value="/login",method = RequestMethod.POST)
public Result login(@RequestBody Map<String,String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    try {
        //1.构造登录小样 UsernamePasswordToken
        password = new MdsHash(password,mobile, hashIterations: 3).toString(); //1.密码、盐、加密次数
        UsernamePasswordToken upToken = new UsernamePasswordToken(mobile,password);
        //2.获取 Subject
        Subject subject = SecurityUtils.getSubject();
        //3.调用登录方法，进入 realm 完成认证
        subject.login(upToken);
        //4.获取 sessionId
        String sessionId = (String)subject.getSession().getId();
        //5.登录成功，返回结果
        return new Result(ResultCode.SUCCESS,sessionId);
    }catch (Exception e) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    }
}
```

画面 2：
```java
package com.ihrm.system.shiro.realm;
import com.ihrm.common.shiro.realm.IrmRealm;
import org.apache.shiro.authc.AuthenticationException;
import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.authc.SimpleAuthenticationInfo;
import org.apache.shiro.authc.UnknownAccountException;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.authz.SimpleAuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;
import org.apache.shiro.subject.Subject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org

