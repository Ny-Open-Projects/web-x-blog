# 画面线理解：03-权限基本操作：api介绍和基本service与controller

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\03-权限基本操作：api介绍和基本service与controller_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:51, 01:05, 01:43, 02:47, 03:31, 03:55, 04:18, 04:32, 05:06, 05:44, 06:15, 06:54, 07:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:49:42

1) 这一组画面整体在讲什么（一句话）：
演示一个权限管理模块的前后端实现，包括API文档、实体类、控制器和Service层的代码编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示API文档，显示权限模块的POST、GET、PUT、DELETE四个接口，以及Models部分的Permission和PermissionList。
画面2：IDEA中展示项目结构，当前选中的是`PermissionApiDao.java`，代码为`public interface PermissionApiDao extends JpaRepository<PermissionApi, String>, JpaSpecification`。
画面3：IDEA中展示`PermissionPoint.java`实体类代码，包含注解`@Entity`、`@Table`，以及字段`id`、`pointClass`、`pointIcon`、`pointStatus`。
画面4：API文档中展示GET /permission接口的参数，包括type、pid、entVisible三个必填参数。
画面5：API文档中展示GET /permission接口的响应示例，JSON结构包含code、message、data字段，data中包含id、description、type等字段。
画面6：API文档中展示DELETE /permission/{permissionId}接口的参数，仅包含permissionId。
画面7：IDEA中展示`PermissionPoint.java`实体类代码，光标在`pointStatus`字段上。
画面8：IDEA中展示`UserController.java`控制器代码，包含保存用户和查询企业列表的两个方法。
画面9：IDEA中展示`PermissionController.java`控制器代码，包含保存权限的POST方法。
画面10：IDEA中展示`PermissionController.java`控制器代码，包含查询权限列表的GET方法。
画面11：IDEA中展示`PermissionController.java`控制器代码，包含根据ID查询权限的GET方法。
画面12：IDEA中展示`PermissionService.java`服务类代码，光标在`@Autowired`注解上，下方有自动补全建议。
画面13：IDEA中展示`PermissionService.java`服务类代码，光标在`public void save(Permission permission)`方法内，正在设置权限ID。
画面14：IDEA中展示`PermissionService.java`服务类代码，光标在`public void deleteById(String id)`方法内，正在执行删除操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
package com.ihrm.system.dao;

import ...

/**
 * 企业数据访问接口
 */
public interface PermissionApiDao extends JpaRepository<PermissionApi, String>, JpaSpecification
```

画面3：
```java
@Entity
@Table(name = "pe_permission_point")
public class PermissionPoint implements Serializable {
    private static final long serialVersionUID = -1087411490113957485L;

    // 主键
    @Id
    private String id;

    // 权限代码
    private String pointClass;
    private String pointIcon;
    private String pointStatus;
}
```

画面8：
```java
@RestController
public class UserController {
    @Autowired
    private UserService userService;

    @RequestMapping(value = "/user", method = RequestMethod.POST)
    public Result save(@RequestBody User user) {
        user.setCompanyId(companyId);
        user.setCompanyName(companyName);
        // 保存用户
        userService.save(user);
        // 返回结果
        return new Result(ResultCode.SUCCESS);
    }

    @RequestMapping(value = "/user", method = RequestMethod.GET)
    public Result findAll(int page, int size, @RequestParam Map map) {
        map.put("companyId", companyId);
        // 返回结果
        return new Result(ResultCode.SUCCESS);
    }
}
```

画面9：
```java
import java.util.Map;

// 1. 解决跨域
@CrossOrigin
// 2. 设置访问路径
@RestController
@RequestMapping(value = "/sys")
public class PermissionController {
    // 保存
    @RequestMapping(value = "/permission", method = RequestMethod.POST)
    public Result save(@RequestBody User user) {
        // 保存权限
        return new Result(ResultCode.SUCCESS);
    }
}
```

画面10：
```java
// 查询列表
@RequestMapping(value = "/permission", method = RequestMethod.GET)
public Result findAll(int page, int size, @RequestParam Map map) {
    return new Result(ResultCode.SUCCESS, pageResult);
}
```

画面11：
```java
// 根据ID查询
@RequestMapping(value = "/permission/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(value = "id") String id) {
    User user = userService.findById(id);
    return new Result(ResultCode.SUCCESS, user);
}
```

画面12：
```java
@Service
public class PermissionService {
    @Autowired
    private PermissionDao permissionDao;
    @Autowired
    private PermissionMenuDao permissionMenuDao;
    @Autowired
    private PermissionPointDao permissionPointDao;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi
