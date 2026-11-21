# 画面线理解：19-SasSHRM中基于shiro的认证授权：自定义realm-认证

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\19-SasSHRM中基于shiro的认证授权：自定义realm-认证_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 01:27, 01:35, 02:11, 02:24, 02:58, 03:09, 03:33, 03:44, 03:55, 04:51, 05:12, 05:20, 06:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:39:23

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
