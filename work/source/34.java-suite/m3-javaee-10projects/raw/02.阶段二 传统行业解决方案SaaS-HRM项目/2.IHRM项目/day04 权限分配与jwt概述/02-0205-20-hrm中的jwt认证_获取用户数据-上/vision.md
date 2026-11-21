# 画面线理解：20-hrm中的jwt认证：获取用户数据-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\20-hrm中的jwt认证：获取用户数据-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：13 帧 @ 00:08, 01:41, 02:32, 03:44, 04:26, 05:12, 05:53, 06:16, 06:36, 07:33, 08:13, 09:02, 09:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:01:56

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的 HRM 系统中用户登录和获取用户权限信息的后端代码实现过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示登录接口返回的 JSON 数据结构，包含 code、message、data 字段，data 中包含 mobile、username、company、menus、points、apis 等信息。
画面2：展示 API 文档中登录接口的响应示例，结构与画面1一致。
画面3：展示 UserContoller.java 中的 login 方法，接收 mobile 和 password，调用 userService.findUserByMobile 查询用户，验证密码，成功则生成 JWT token 并返回。
画面4：展示 UserContoller.java 中的 profile 方法，接收 userId，调用 userService.findById 查询用户，返回 ProfileResult 对象。
画面5：展示 ProfileResult.java 类的定义，包含 mobile、username、company、roles 字段。
画面6：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。
画面7：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。
画面8：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。
画面9：展示多个开发工具窗口的切换，包括 IDEA、Postman、SQLyog、PowerDesigner 等。
画面10：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。
画面11：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。
画面12：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。
画面13：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
{
  "code": 0,
  "message": "string",
  "data": {
    "mobile": "string",
    "username": "string",
    "company": "string",
    "menus": [
      "string"
    ],
    "points": [
      "string"
    ],
    "apis": [
      "string"
    ]
  }
}

画面3：
@RequestMapping(value = "/login", method = RequestMethod.POST)
public Result login(@RequestBody Map<String, String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    User user = userService.findUserByMobile(mobile);
    if (user == null || !user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    } else {
        Map<String, Object> map = new HashMap<>();
        map.put("companyName", user.getCompanyName());
        map.put("username", user.getUsername());
        String token = jwtUtils.createJwt(user.getId(), user.getUsername(), map);
        return new Result(ResultCode.SUCCESS, token);
    }
}

画面4：
@RequestMapping(value = "/profile", method = RequestMethod.POST)
public Result profile() {
    String userId = "1";
    User user = userService.findById(userId);
}

画面5：
package com.ihrm.domain.system;

public class ProfileResult {
    private String mobile;
    private String username;
    private String company;
    private Map<String, Object> roles;
}

画面6：
package com.ihrm.domain.system;

import lombok.Getter;
import lombok.Setter;
import java.util.Map;

@Getter
@Setter
public class ProfileResult {
    private String mobile;
    private String username;
    private String company;
    private Map<String, Object> roles;
}

画面10：
public ProfileResult(User user) {
    this.mobile = user.getMobile();
    this.username = user.getUsername();
    this.company = user.getCompanyName();
    Set<Role> roles = user.getRoles();
    Set<String> menus = new HashSet<>();
    Set<String> points = new HashSet<>();
    Set<String> apis = new HashSet<>();
    for (Role role : roles) {
        Set<Permission> perms = role.getPermissions();
        for (Permission perm : perms) {
            String code = perm.getCode();
            if (perm.getPerType() == 1) {
                menus.add(code);
            } else if (perm.getPerType() == 2) {
                points.add(code);
            } else {
                apis.add(code);
            }
        }
    }
    this.roles.put("menus", menus);
    this.roles.put("points", points);
    this.roles.put("apis", apis);
}

画面13：
public ProfileResult(User user) {
    this.mobile = user.getMobile();
    this.username = user.getUsername();
    this.company = user.getCompanyName();
    Set<Role> roles = user.getRoles();
    Set<String> menus = new HashSet<>();
    Set<String> points = new HashSet<>();
    Set<String> apis = new HashSet<>();
    for (Role role : roles) {
        Set<Permission> perms = role.getPermissions();
        for (Permission perm : perms) {
            String code = perm.getCode();
            if (perm.getPerType() == 1) {
                menus.add(code);
            } else if (perm.getPerType() == 2) {
                points.add(code);
            } else {
                apis.add(code);
            }
        }
    }
    this.roles.put("menus", menus);
    this.roles.put("points", points);
    this.roles.put("apis", apis);
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
