# 画面线理解：11-分配权限，分配角色：页面回显

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\11-分配权限，分配角色：页面回显_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:25, 02:32, 03:27, 05:05, 05:53, 07:04, 07:54, 08:30, 09:36, 10:38, 11:16, 12:20, 13:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:55:56

1) 这一组画面整体在讲什么（一句话）：
演示如何在 HRM 系统中为员工分配角色权限，涉及前端 Vue 代码、后端 Java 代码及数据库模型设计。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 HRM 系统的“员工”页面，弹出“分配角色”对话框，用户正在为员工“zhangsan1”选择角色，鼠标悬停在“确定”按钮上。
画面 2: HRM 系统“员工”列表页，显示员工信息，包括姓名、手机号、工号、转正时间、部门等字段。
画面 3: Visual Studio Code 编辑器中打开 `addRole.vue` 文件，展示前端 Vue 代码，其中包含 `toAssignPrem(id)` 方法，用于处理分配权限的逻辑。
画面 4: 多窗口分屏画面，展示 HRM 系统前端、后端代码（IntelliJ IDEA）、数据库设计工具（PowerDesigner、SQLyog）等开发环境。
画面 5: IntelliJ IDEA 中打开 `UserResult.java` 文件，展示后端 Java 类定义，包含 `private String workingCity;` 等字段。
画面 6: IntelliJ IDEA 中 `UserResult.java` 文件，展示 `UserResult(UserUser)` 构造函数，其中包含 `BeanUtils.copyProperties(user, target_this);` 代码。
画面 7: IntelliJ IDEA 中 `UserResult.java` 文件，展示构造函数内部的 `for (Role role : user.getRoles()) { this.roleIds.add(role.getId()); }` 代码。
画面 8: IntelliJ IDEA 中 `UserResult.java` 文件，展示类的顶部导入语句和 `@RequestMapping` 注解。
画面 9: HRM 系统“分配角色”对话框，用户已勾选“人事经理”、“系统管理员”、“人事专员”角色，鼠标悬停在“确定”按钮上。
画面 10: IntelliJ IDEA 中打开 `RoleResult.java` 文件，展示后端 Java 类定义，包含 `private List<String> p;` 字段。
画面 11: IntelliJ IDEA 中打开 `RoleController.java` 文件，展示控制器类，包含 `@RequestMapping(value = "/role/{id}", method = RequestMethod.GET)` 和 `@RequestMapping(value = "/role/list", method = RequestMethod.GET)` 注解。
画面 12: Visual Studio Code 编辑器中打开 `role-list.vue` 文件，展示前端 Vue 代码，包含 `import {list, add, update, remove, detail, assignPrem} from '@/api/base/role';` 导入语句。
画面 13: 浏览器开发者工具的“Network”标签页，显示正在记录网络活动。
画面 14: HRM 系统“角色管理”页面，弹出“为【新资专员】分配权限”对话框，列出多个权限选项，鼠标悬停在“取消”按钮上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```vue
<div slot="footer" class="dialog footer">
  <el-button type="primary" @click="createData">提交</el-button>
  <el-button @click="roleFormVisible=false">取消</el-button>
</div>
```
```javascript
import {findUser} from "@/api/base/users";
import {assignRole, detail} from "@/api/base/users";
export default {
  data () {
    return {
      roleFormVisible: false,
      formBase: {},
      checkedRoles: [],
      rules: []
    };
  },
  methods: {
    toAssignPrem(id) {
      detail({id: id}).then(res => {
        this.checkedRoles = res.data.data.roleIds;
      });
    }
  }
};
```
画面 5:
```java
package com.ihrm.domain.system.response;

public class UserResult implements Serializable {
```
画面 6:
```java
private String workingCity;
private Date correctionTime;
private Integer inServiceStatus;
private String departmentName;
private List<String> roleIds;
```
画面 7:
```java
public UserResult(User user) {
  BeanUtils.copyProperties(user, target_this);
  for (Role role : user.getRoles()) {
    this.roleIds.add(role.getId());
  }
}
```
画面 8:
```java
package com.ihrm.domain.system.response;
import com.ihrm.domain.system.Role;
import com.ihrm.domain.system.User;
import org.springframework.beans.BeanUtils;
import javax.persistence.Id;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
```
画面 10:
```java
private List<String> p;
```
画面 11:
```java
@RequestMapping(value = "/role/{id}", method = RequestMethod.GET)
public Result findRoleById(@PathVariable(name = "id") String id) throws Exception {
  Role role = roleService.findById(id);
  RoleResult roleResult = new RoleResult(role);
  return new Result(ResultCode.SUCCESS, roleResult);
}

@RequestMapping(value = "/role", method = RequestMethod.GET)
public Result findRole(@RequestParam(name = "company_id") String companyId, Pageable pageable) throws Exception {
  Page<Role> pr = new PageResult<>(roleService.findByPage(companyId, pageable));
  return new Result(ResultCode.SUCCESS, pr);
}

@RequestMapping(value = "/role/list", method = RequestMethod.GET)
public Result findAll() throws Exception {
  List<Role> roleList = roleService.findAll(companyId);
  return new Result(ResultCode.SUCCESS, roleList);
}
```
画面 12:
```vue
<el-tree
  :data="roleList"
  :props="defaultCheckedKeys"
  show-checkbox
  node-key="id"
  ref="tree"
  :default-checked-keys="checkedNodes"
  :default-expand-all="true"
  :expand-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :
