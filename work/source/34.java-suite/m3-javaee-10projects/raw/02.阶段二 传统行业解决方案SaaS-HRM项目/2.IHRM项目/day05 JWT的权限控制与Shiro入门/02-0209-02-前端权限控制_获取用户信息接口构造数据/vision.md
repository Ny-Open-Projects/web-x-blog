# 画面线理解：02-前端权限控制：获取用户信息接口构造数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\02-前端权限控制：获取用户信息接口构造数据_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 02:13, 04:37, 06:36, 07:15, 07:36, 07:56, 08:57, 09:34, 10:16, 10:55, 11:25, 11:54, 12:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:09:15

1) 这一组画面整体在讲什么（一句话）：
实现基于 Shiro 的用户权限控制，通过修改 UserController 中的 profile 方法，根据用户角色（saasAdmin、coAdmin、企业用户）动态返回不同的权限信息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程目录结构，当前章节为“1.2 服务端代码实现”，内容是修改 FrameController 的 profile 方法以添加权限信息。
画面 2: 在 IntelliJ IDEA 中打开 UserController.java，展示 profile 方法的初始代码，包括获取 Authorization 头、解析 JWT、根据用户 ID 查询用户信息。
画面 3: 代码编辑器中，对 profile 方法进行修改，添加了根据用户级别判断权限的逻辑。
画面 4: 在代码中添加了对用户级别（saasAdmin、coAdmin、企业用户）的判断逻辑，使用 if-else 结构。
画面 5: 展示了代码中对用户级别判断的完整逻辑，包括对不同角色返回不同权限的处理。
画面 6: 切换到 PermissionController.java，展示 assignRoles 方法，用于分配角色。
画面 7: 在 UserController.java 中，对 profile 方法的权限判断逻辑进行修改，使用 permissionService.find 方法。
画面 8: 展示了 PermissionService 类的代码，包含 find 方法的实现。
画面 9: 在 UserController.java 中，对 profile 方法的权限判断逻辑进行修改，使用 permissionService.find 方法。
画面 10: 在 UserController.java 中，对 profile 方法的权限判断逻辑进行修改，使用 permissionService.find 方法。
画面 11: 切换到 ProfileResult.java，展示 ProfileResult 类的构造方法，用于封装用户权限信息。
画面 12: 展示 ProfileResult 类的构造方法，用于封装用户权限信息。
画面 13: 在 UserController.java 中，对 profile 方法的权限判断逻辑进行修改，使用 permissionService.find 方法。
画面 14: 在 UserController.java 中，对 profile 方法的权限判断逻辑进行修改，使用 permissionService.find 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
1.2 服务端代码实现
对系统微服务的FrameController的profile方法（获取用户信息接口）进行修改，添加权限信息
```

画面 2:
```java
@RequestMapping(value = "/profile", method = RequestMethod.POST)
public Result profile(HttpServletRequest request) throws Exception {
    //获取个人信息
    String authorization = request.getHeader("Authorization");
    if(StringUtils.isEmpty(authorization)) {
        throw new CommonException(ResultCode.UNAUTHENTICATED);
    }
    //2.当携带Bearer令牌
    String token = authorization.replace("Bearer ", "");
    //3.解析token
    Claims claims = jwtUtils.parseJwt(token);
    String userid = claims.getId();
    User user = userService.findById(userid);
    ProfileResult result = new ProfileResult(user);
    return new Result(ResultCode.SUCCESS,result);
}
```

画面 3:
```java
//从请求头中获取token数据
// 1.获取请求头信息，名称-Authorization
// 2.携带Bearer令牌
// 3.解析token
// 4.获取claims
String authorization = request.getHeader("Authorization");
if(StringUtils.isEmpty(authorization)) {
    throw new CommonException(ResultCode.UNAUTHENTICATED);
}
//2.当携带Bearer令牌
String token = authorization.replace("Bearer ", "");
//3.解析token
Claims claims = jwtUtils.parseJwt(token);
String userid = claims.getId();
User user = userService.findById(userid);
ProfileResult result = new ProfileResult(user);
return new Result(ResultCode.SUCCESS,result);
```

画面 4:
```java
if("saasAdmin".equals(user.getLevel())) {
    //1.saas平台管理员具有所有权限
} else if("coAdmin".equals(user.getLevel())) {
    //2.企业管理员具有所有企业权限
} else {
    //3.企业用户具有当前角色的权限
}
```

画面 5:
```java
if("saasAdmin".equals(user.getLevel())) {
    //1.saas平台管理员具有所有权限
} else if("coAdmin".equals(user.getLevel())) {
    //2.企业管理员具有所有企业权限
} else {
    //3.企业用户具有当前角色的权限
}
```

画面 6:
```java
package com.ihrm.system.controller;

import com.ihrm.common.constant.PermissionConstants;
import com.ihrm.common.domain.Permission;
import com.ihrm.system.dao.PermissionDao;
import com.ihrm.system.service.PermissionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * 权限控制器
 */
@RestController
@RequestMapping("/permission")
public class PermissionController {

    @Autowired
    private JwtUtils jwtUtils;

    @RequestMapping(value = "/user/assignRoles", method = RequestMethod.PUT)
    public Result assignRoles(@RequestBody Map<String, Object> map) {
        String userId = (String) map.get("id");
        //获取角色的id列表
        List<String> roleIds = (List<String>) map.get("roleIds");
        //根据用户id和角色id，更新用户角色
        permissionService.assignRoles(userId, roleIds);
        return new Result(ResultCode.SUCCESS);
    }
}
```

画面 7:
```java
if("saasAdmin".equals(user.getLevel())) {
    //1.saas平台管理员具有所有权限
} else if("coAdmin".equals(user.getLevel())) {
    //2.企业管理员具有所有企业权限
} else {
    //3.企业用户具有当前角色的权限
}
```

画面 8:
```java
//1.获取用户信息
String userid = claims.getId();
User user = userService.findById(userid);
ProfileResult result = null;
if("saasAdmin".equals(user.getLevel())) {
    //1.saas平台管理员具有所有权限
    Map map = new HashMap();
    List<Permission> list = permissionService.findAll(map);
    result = new ProfileResult(user, list);
} else if("coAdmin".equals(user.getLevel())) {
    //2.企业管理员具有所有企业权限
    Map map = new HashMap();
    List<Permission> list = permissionService.findAll(map);
    result = new ProfileResult(user, list);
} else {
    //3.企业用户具有当前角色的权限
    List<Permission> list = permissionService.findAll(map);
    result = new ProfileResult(user, list);
}
return new Result(ResultCode.SUCCESS,result);
```

画面 9:
```java
String userid = claims.getId();
User user = userService.findById(userid);
ProfileResult result = null;
if("saasAdmin".equals(user.getLevel())) {
    //1.saas平台管理员具有所有权限
    Map map = new HashMap();
    List<Permission> list = permissionService.findAll(map);
    result = new ProfileResult(user, list);
} else if("coAdmin".equals(user.getLevel())) {
    //2.企业管理员具有所有企业权限
    Map map = new HashMap();
    List<Permission> list = permissionService.findAll(map);
    result = new ProfileResult(user, list);
} else {
    //3.企业用户具有当前角色的权限
    List<Permission> list = permissionService.findAll(map);
    result = new ProfileResult(user, list);
}
return new Result(ResultCode.SUCCESS,result);
```

画面 10:
```java
String userid = claims.getId();
User user = userService.findById(userid);
ProfileResult result = null;
if("saasAdmin".equals(user.getLevel())) {
    //1.saas平台管理员具有所有权限
    Map map = new HashMap();
    List<Permission> list = permissionService.findAll(map);
    result = new ProfileResult(user, list);
} else if("coAdmin".equals(user.getLevel())) {
    //2.企业管理员具有所有企业权限
    Map map = new HashMap();
    List<Permission> list = permissionService.findAll(map);
    result = new ProfileResult(user, list);
} else {
    //3.企业用户具有当前角色的权限
    List<Permission> list = permissionService.findAll(map);
    result = new ProfileResult(user, list);
}
return new Result(ResultCode.SUCCESS,result);
```

画面 11:
```java
import xxx

@Getter
@Setter
public class ProfileResult {
    private String mobile;
    private String username;
    private String company;
    private Map<String,Object> roles = new HashMap<>();
    //封装用户
    public ProfileResult(User user) {
        this.mobile = user.getMobile();
        this.username = user.getUsername();
        this.company = user.getCompany();
        Set<String> menus = new HashSet<>();
        Set<String> points = new HashSet<>();
        Set<String> spis = new HashSet<>();
        for (Role role : roles) {
            Set<Permission> perms = role.getPermissions();
            for (Permission perm : perms) {
                //封装权限信息
                menus.add(perm.getMenu());
                points.add(perm.getPoint());
                spis.add(perm.getSpis());
            }
        }
    }
}
```

画面 12:
```java
public ProfileResult(User user, List<Permission> list) {
    this.mobile = user.getMobile();
    this.username = user.getUsername();
    this.company = user.getCompany();
    Set<String> menus = new HashSet<>();
    Set<String> points = new HashSet<>();
    Set<String> spis = new HashSet<>();
    for (Permission permission : list) {
        menus.add(permission.get
