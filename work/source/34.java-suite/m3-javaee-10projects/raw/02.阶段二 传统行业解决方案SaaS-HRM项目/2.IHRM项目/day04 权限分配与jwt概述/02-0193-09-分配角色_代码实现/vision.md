# 画面线理解：09-分配角色：代码实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\09-分配角色：代码实现_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:53, 01:17, 01:43, 02:47, 03:11, 03:42, 04:26, 05:05, 05:28, 05:42, 06:02, 06:40, 07:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:53:52

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现用户与角色的分配功能，包括控制器层、服务层和数据访问层的代码编写与调试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PermissionController.java 文件，包含 findAll 和 findById 两个 GET 请求方法，用于查询权限列表和单个权限。
画面2：展示 API 文档页面，列出 /user、/user/assignRoles、/login、/profile 等接口，用于用户管理。
画面3：展示 UserController.java 文件，包含 save 方法，用于保存用户信息。
画面4：展示 API 文档页面，显示 /user/assignRoles 接口的请求体和响应体结构。
画面5：展示 UserController.java 文件，正在编写 assignRoles 方法的 PUT 请求处理逻辑。
画面6：展示 UserController.java 文件，继续编写 assignRoles 方法，准备调用服务层。
画面7：展示 UserController.java 文件，完成 assignRoles 方法的 PUT 请求处理逻辑。
画面8：展示 UserService.java 文件，正在编写 assignRoles 方法，用于处理用户角色分配逻辑。
画面9：展示 UserService.java 文件，正在编写 findUserById 方法，用于根据用户 ID 查询用户信息。
画面10：展示 UserService.java 文件，正在导入 Role 类，用于处理角色对象。
画面11：展示 UserService.java 文件，完成 findUserById 方法的实现。
画面12：展示 UserService.java 文件，完成 assignRoles 方法的实现，包括获取用户、创建角色集合、遍历角色 ID 并查询角色对象。
画面13：展示 UserService.java 文件，完成 assignRoles 方法的实现，包括将角色对象添加到用户的角色集合中。
画面14：展示 RoleService.java 文件，显示其包路径和导入的依赖类。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@RequestMapping(value = "/permission", method = RequestMethod.GET)
public Result findAll(@RequestParam Map map) {
    List<Permission> list = permissionService.findAll(map);
    return new Result(ResultCode.SUCCESS,list);
}

//根据ID查询
@RequestMapping(value = "/permission/{id}", method = RequestMethod.GET)
public Map map = permissionService.findById(id);
return new Result(ResultCode.SUCCESS,map);
```

画面3：
```java
@RequestMapping(value = "/user", method = RequestMethod.POST)
public Result save(@RequestBody User user) {
    //1.设置公司ID
    user.setCompanyId(companyId);
    //2.设置公司名称
    user.setCompanyName(companyName);
    //3.调用service保存企业
    userService.save(user);
}
```

画面5：
```java
@RequestMapping(value = "/user/assignRoles", method = RequestMethod.PUT)
public Result save(@RequestBody Map<String,Object> map) {
    //1.获取用户ID
    String userId = (String) map.get("id");
    //2.获取角色ID列表
    List<String> roleIds = (List<String>) map.get("roleIds");
    //3.调用service完成角色分配
    userService.assignRoles(userId,roleIds);
    return new Result(ResultCode.SUCCESS);
}
```

画面8：
```java
if(!StringUtils.isEmpty(map.get("hosDept"))){
    if("0".equals(String) map.get("hosDept")){
        list.add(criteriaBuilder.isNull(root.get("departmentId")));
    }else{
        list.add(criteriaBuilder.equal(root.get("departmentId"),map.get("hosDept")));
    }
}
return criteriaBuilder.and(list.toArray(new Predicate[list.size()]));
```

画面9：
```java
public void assignRoles(String userId,List<String> roleIds) {
    //1.根据ID查询用户
    User user = userDao.findById(userId).get();
    //2.设置用户的角色集合
    Set<Role> roles = new HashSet<>();
    //3.遍历角色ID
    for (String roleId : roleIds) {
        //4.查询角色对象
        Role role = roleDao.findById(roleId).get();
        //5.添加到角色集合
        roles.add(role);
    }
    //6.更新用户
    user.setRoles(roles);
    //7.保存用户
    userDao.save(user);
}
```

画面14：
```java
package com.ihrm.system.service;
import com.ihrm.common.utils.IdWorker;
import com.ihrm.system.dao.PermissionDao;
import com.ihrm.system.domain.Permission;
import com.ihrm.system.domain.Role;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.*;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
