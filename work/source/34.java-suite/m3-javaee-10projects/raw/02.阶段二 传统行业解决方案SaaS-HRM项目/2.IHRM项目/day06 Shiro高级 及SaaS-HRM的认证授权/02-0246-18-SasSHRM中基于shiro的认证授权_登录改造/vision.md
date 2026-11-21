# 画面线理解：18-SasSHRM中基于shiro的认证授权：登录改造

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\18-SasSHRM中基于shiro的认证授权：登录改造_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:19, 00:34, 01:59, 02:29, 03:48, 04:23, 04:49, 05:19, 05:56, 06:14, 07:02, 07:27, 07:55, 08:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:38:33

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中使用 Shiro 框架实现用户登录认证，包括 JWT 和 Shiro 两种方式的对比、登录逻辑代码实现、以及相关配置和工具的使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了 PPT 页面，对比 JWT 和 Shiro 的认证授权方式。
- JWT 方式：前端调用服务 → 系统微服务 → 生成 token → 返回 token 信息 → 企业微服务 → 解析 token → 校验操作权限。
- Shiro 方式：前端调用服务 → 系统微服务 → 获取企业信息（含 sessionid）→ 企业微服务 → 获取安全数据 → Shiro 会话管理 → Redis 服务。
- PPT 右下角列出四个步骤：1. 搭建环境；2. 登录改造；3. 自定义 realm；4. 自定义会话管理器。

画面 2:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 3:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 4:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 5:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 6:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 7:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 8:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 9:
- 展示了项目结构，选中了 ihrm_system 模块。
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 10:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 11:
- 展示了 UserService.java 文件中 save 方法的代码片段。
- 代码逻辑：设置用户属性（id、password、enableState、deptId）→ 调用 dao 保存用户。

画面 12:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 13:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 14:
- 展示了 Windows 桌面，多个窗口并列显示，包括 IntelliJ IDEA、Redis Desktop Manager、SQLyog Ultimate、PDF 文档等。
- 窗口标题显示为“ihm_parent [E:\workspace...]”、“shiro-test [E:\workspace...]”、“JWT与Shiro认证授权对比”等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
//登录失败
if(user == null || user.getPassword().equals(password)) {
    return new Result(ResultCode.MOBILEORPASSWORDERROR);
}
else {
    //登录成功
    //api权限字符串
    StringBuilder sb = new StringBuilder();
    for (Role role : user.getRoles()) {
        for (Permission perm : role.getPermissions()) {
            if(perm.getTypes() == PermissionConstants.PERMISSION_API) {
                sb.append(perm.getCode()).append(",");
            }
        }
    }
    //构建token
    Map<String, Object> map = new HashMap<>();
    map.put("apis", sb.toString()); //api权限字符串
    map.put("companyId", user.getCompanyId());
    map.put("username", user.getUsername());
    String token = JwtUtil.createJwt(user.getUsername(), map);
    return new Result(ResultCode.SUCCESS, token);
}
```

画面 3:
```java
@RequestMapping(value="/login",method = RequestMethod.POST)
public Result login(@RequestBody Map<String,String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    //1.将登录令牌
    //2.获取subject，进入realm完成认证
    //3.获取sessionid
    //4.获取sessionid
    //5.构造返回结果
    User user = userService.findByMobile(mobile);
    if(user == null || user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    }else {
        //登录成功
        //api权限字符串
        StringBuilder sb = new StringBuilder();
        for (Role role : user.getRoles()) {
            for (Permission perm : role.getPermissions()) {
                if(perm.getTypes() == PermissionConstants.PERMISSION_API) {
                    sb.append(perm.getCode()).append(",");
                }
            }
        }
    }
}
```

画面 4:
```java
@RequestMapping(value="/login",method = RequestMethod.POST)
public Result login(@RequestBody Map<String,String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    //1.将登录令牌
    //2.获取subject，进入realm完成认证
    //3.获取sessionid
    //4.获取sessionid
    //5.构造返回结果
    User user = userService.findByMobile(mobile);
    if(user == null || user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    }else {
        //登录成功
        //api权限字符串
        StringBuilder sb = new StringBuilder();
        for (Role role : user.getRoles()) {
            for (Permission perm : role.getPermissions()) {
                if(perm.getTypes() == PermissionConstants.PERMISSION_API) {
                    sb.append(perm.getCode()).append(",");
                }
            }
        }
    }
}
```

画面 5:
```java
@RequestMapping(value="/login",method = RequestMethod.POST)
public Result login(@RequestBody Map<String,String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    //1.将登录令牌
    //2.获取subject，进入realm完成认证
    //3.获取sessionid
    //4.获取sessionid
    //5.构造返回结果
    User user = userService.findByMobile(mobile);
    if(user == null || user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    }else {
        //登录成功
        //api权限字符串
        StringBuilder sb = new StringBuilder();
        for (Role role : user.getRoles()) {
            for (Permission perm : role.getPermissions()) {
                if(perm.getTypes() == PermissionConstants.PERMISSION_API) {
                    sb.append(perm.getCode()).append(",");
                }
            }
        }
    }
}
```

画面 6:
```java
@RequestMapping(value="/login",method = RequestMethod.POST)
public Result login(@RequestBody Map<String,String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    //1.将登录令牌
    //2.获取subject，进入realm完成认证
    //3.获取sessionid
    //4.获取sessionid
    //5.构造返回结果
    User user = userService.findByMobile(mobile);
    if(user == null || user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    }else {
        //登录成功
        //api权限字符串
        StringBuilder sb = new StringBuilder();
        for (Role role : user.getRoles()) {
            for (Permission perm : role.getPermissions()) {
                if(perm.getTypes() == PermissionConstants.PERMISSION_API) {
                    sb.append(perm.getCode()).append(",");
                }
            }
        }
    }
}
```

画面 7:
```java
@RequestMapping(value="/login",method = RequestMethod.POST)
public Result login(@RequestBody Map<String,String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    //1.将登录令牌
    //2.获取subject，进入realm完成认证
    //3.获取sessionid
    //4.获取sessionid
    //5.构造返回结果
    User user = userService.findByMobile(mobile);
    if(user == null || user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    }else {
        //登录成功
        //
