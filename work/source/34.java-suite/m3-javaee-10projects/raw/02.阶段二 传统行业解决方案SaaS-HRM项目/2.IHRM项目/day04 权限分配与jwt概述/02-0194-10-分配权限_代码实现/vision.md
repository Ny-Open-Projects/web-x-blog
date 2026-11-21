# 画面线理解：10-分配权限：代码实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\10-分配权限：代码实现_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:49, 01:51, 02:13, 02:32, 03:36, 04:40, 04:58, 05:35, 07:12, 07:52, 08:17, 08:51, 10:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:54:34

1) 这一组画面整体在讲什么（一句话）：
演示如何在 SaaS-HRM 系统中通过后端 Java 代码实现角色与权限的分配功能，包括前端界面操作、API 文档、控制器与服务层代码编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 HRM 系统的员工列表页面，左侧导航栏选中“员工”，页面显示员工编号、姓名、手机号、部门等信息。
画面 2: 展示 API 文档页面，列出与角色相关的 API 接口，包括 POST /role（添加角色）、GET /role（获取角色列表）、PUT /role/{roleId}（修改角色）、DELETE /role/{roleId}（删除角色）等。
画面 3: 展示前端界面，弹出“为【人事经理】分配权限”的对话框，其中“员工管理”下的“用户删除按钮”、“删除用户角色”、“用户修改按钮”等选项被勾选。
画面 4: 展示 IntelliJ IDEA 中 RoleController.java 的代码，包含添加角色、更新角色、删除角色的注解和方法。
画面 5: 展示 IntelliJ IDEA 中 RoleController.java 的代码，新增了保存权限分配的 PUT /user/assignRoles 接口方法。
画面 6: 展示 IntelliJ IDEA 中 RoleService.java 的代码，包含 assignPerms 方法的注释和部分实现。
画面 7: 展示 IntelliJ IDEA 中 RoleService.java 的代码，光标位于 assignPerms 方法的注释“//3. 设置角色和权限的关系”处，提示“Press Ctrl+空格 to choose the selected...”。
画面 8: 展示 IntelliJ IDEA 中 RoleService.java 的代码，assignPerms 方法中已添加注释“//3. 设置角色和权限的关系”。
画面 9: 展示 IntelliJ IDEA 中 RoleService.java 的代码，assignPerms 方法中已添加注释“//3. 设置角色和权限的关系”，并弹出一个“SaaS-HRM系统API文档 - Google Chrome”窗口。
画面 10: 展示前端界面，弹出“为【人事经理】分配权限”的对话框，所有权限选项均未勾选。
画面 11: 展示 IntelliJ IDEA 中 PermissionDao.java 的代码，定义了继承自 JpaRepository 的接口。
画面 12: 展示 IntelliJ IDEA 中 RoleService.java 的代码，光标位于 assignPerms 方法中，提示“Press Ctrl+空格 to choose the selected...”。
画面 13: 展示 IntelliJ IDEA 中 RoleService.java 的代码，assignPerms 方法中已添加注释“//3. 设置角色和权限的关系”，并添加了权限赋值逻辑。
画面 14: 展示 IntelliJ IDEA 中 RoleService.java 的代码，assignPerms 方法中已添加注释“//3. 设置角色和权限的关系”，并添加了设置角色权限关系和保存角色的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```java
package com.ihrm.system.controller;

import com.ihrm.system.controller;
@RquestMapping("/sys")
public class RoleController extends BaseController{
    @Autowired
    private RoleService roleService;

    //添加角色
    @RequestMapping(value = "/role", method = RequestMethod.POST)
    public Result add(@RequestBody Role role) throws Exception {
        role.setCompanyId(companyId);
        roleService.save(role);
        return Result.SUCCESS();
    }

    //更新角色
    @RequestMapping(value = "/role/{id}", method = RequestMethod.PUT)
    public Result update(@PathVariable(name = "id") String id, @RequestBody Role role) throws Exception {
        roleService.update(role);
        return Result.SUCCESS();
    }

    //删除角色
    @RequestMapping(value = "/role/{id}", method = RequestMethod.DELETE)
    public Result delete(@PathVariable(name = "id") String id) throws Exception {
        roleService.delete(id);
        return Result.SUCCESS();
    }
}
```

画面 5:
```java
//添加角色
@RequestMapping(value = "/role", method = RequestMethod.POST)
public Result add(@RequestBody Role role) throws Exception {
    role.setCompanyId(companyId);
    roleService.save(role);
    return Result.SUCCESS();
}

//更新角色
@RequestMapping(value = "/role/{id}", method = RequestMethod.PUT)
public Result update(@PathVariable(name = "id") String id, @RequestBody Role role) throws Exception {
    roleService.update(role);
    return Result.SUCCESS();
}

//删除角色
@RequestMapping(value = "/role/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(name = "id") String id) throws Exception {
    roleService.delete(id);
    return Result.SUCCESS();
}

//分配权限
@RequestMapping(value = "/user/assignRoles", method = RequestMethod.PUT)
public Result save(@RequestBody Map<String, Object> map) {
    String userId = (String) map.get("id");
    List<String> roleIds = (List<String>) map.get("roleIds");
    userService.assignRoles(userId, roleIds);
    return new Result(ResultCode.SUCCESS);
}
```

画面 6:
```java
@Autowired
private IdWorker idWorker;
@Autowired
private RoleDao roleDao;
@Autowired
private PermissionDao permissionDao;

//分配权限
public void assignPerms(String roleId, List<String> permIds) {
    //1.获取角色对象
    //2.获取角色的权限集合
    //3.设置角色和权限的关系
    //4.更新角色
}

//添加角色
public void save(Role role) {
    //填充其他参数
    role.setId(idWorker.nextId() + "");
    roleDao.save(role);
}

//更新角色
public void update(Role role) {
    //更新角色
    roleDao.save(role);
}
```

画面 7:
```java
//3. 设置角色和权限的关系
//4. 更新角色
```

画面 8:
```java
//3. 设置角色和权限的关系
```

画面 9:
```java
//3. 设置角色和权限的关系
```

画面 11:
```java
package com.ihrm.system.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;

public interface PermissionDao extends JpaRepository<Permission, String>, JpaSpecificationExecutor<Permission> {
}
```

画面 12:
```java
//3. 设置角色和权限的关系
```

画面 13:
```java
//3. 设置角色和权限的关系
Permission permission = permissionDao.findById(permId).get();
List<Permission> apiList = permissionDao.findByTypeAndPid(PermissionConstants.PERMISSION_API, permission.getPid());
perms.addAll(apiList);
perms.add(permission);
```

画面 14:
```java
//3. 设置角色和权限的关系
role.setPermissions(perms);
roleDao.save(role);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
