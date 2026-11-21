# 画面线理解：07-权限基本操作：测试权限的操作

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\07-权限基本操作：测试权限的操作_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:43, 00:54, 01:05, 01:20, 01:58, 02:19, 02:58, 03:15, 03:49, 04:29, 04:54, 05:02, 05:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:52:43

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Vue.js 和 Java 的 SaaS 人力资源管理系统中权限管理模块的前后端代码实现与前端界面操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：桌面环境，显示“黑马程序员”和“博学谷”两个机构的标志。
画面2：文件资源管理器中显示项目根目录，选中了“module-permissions”文件夹，同时预览了“src”目录下的文件结构。
画面3：Notepad++ 编辑器中显示了“users.js”文件内容，其中定义了多个与用户相关的 API 请求方法。
画面4：文件资源管理器中显示“api”文件夹，选中了“permissions.js”文件。
画面5：Visual Studio Code 编辑器中显示“main.js”文件，导入了多个模块并注册了 Vue 实例，底部显示应用已成功编译并在本地运行。
画面6：IntelliJ IDEA 中显示 Java 代码，具体为“PermissionService.java”中的删除权限方法，包含对不同权限类型的判断和删除操作。
画面7：IntelliJ IDEA 中显示“PermissionController.java”中的删除权限方法，包含对不同权限类型的判断和删除操作。
画面8：浏览器中显示 HRM 系统的“权限管理”页面，列出了多个菜单项及其权限标识。
画面9：浏览器中显示“权限管理”页面，选中了“test”权限项并点击“编辑”按钮。
画面10：浏览器中显示“权限管理”页面，选中了“权限菜单1”并点击“编辑”按钮。
画面11：浏览器中弹出“编辑权限”对话框，包含“权限名称”、“权限标识”、“权限描述”、“企业可见”、“按钮样式”、“按钮icon”、“按钮状态”等字段。
画面12：浏览器中弹出“编辑权限”对话框，切换到“API权限列表”标签页，包含“权限名称”、“权限标识”、“权限描述”、“企业可见”、“API请求地址”、“API请求方式”、“API类型”等字段。
画面13：浏览器中显示“API权限列表”弹窗，列出了“查看部门”权限项及其操作按钮。
画面14：浏览器中显示“API权限列表”弹窗，列出了“查看部门”权限项及其操作按钮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```javascript
import {createAPI} from '@/utils/request'

export const list = data => createAPI('/sys/user', 'get', data)
export const simple = data => createAPI('/sys/user/simple', 'get', data)
export const add = data => createAPI('/sys/user', 'post', data)
export const update = data => createAPI('/sys/user/${data.id}', 'put', data)
export const remove = data => createAPI('/sys/user/${data.id}', 'delete', data)
export const detail = data => createAPI('/sys/user/${data.id}', 'get', data)
export const assignRoles = data => createAPI('/sys/user/assignRoles', 'put', data)
```

画面5：
```javascript
import 'font-awesome/css/font-awesome.css'
import '@/mock' // 模拟数据
import dashboard from '@/module-dashboard' // 图表
import demo from '@/module-demo' // 高级
import saasClients from '@/module-saas-clients' // 企业客户
import departments from '@/module-departments' // 部门
import employees from '@/module-employees' // 员工
import settings from '@/module-settings' // 设置

import tools from '@/utils/common.js'
Vue.prototype.Stools = tools

Vue.use(dashboard, store)
Vue.use(demo, store)
Vue.use(saasClients, store)
Vue.use(departments, store)
Vue.use(employees, store)
Vue.use(settings, store)
```

画面6：
```java
return permissionDao.findAll(spec);
```

画面6：
```java
public void deleteById(String id) throws Exception {
    // 1.通过传递的权限id获取权限
    Permission permission = permissionDao.findById(id).get();
    // 2.根据权限类型不同的处理
    int type = permission.getPermissionType();
    switch (type) {
        case PermissionConstants.PERMISSION_MENU:
            permissionMenuDao.deleteById(id);
            break;
        case PermissionConstants.PERMISSION_POINT:
            permissionPointDao.deleteById(id);
            break;
        case PermissionConstants.PERMISSION_API:
            permissionApiDao.deleteById(id);
            break;
    }
}
```

画面7：
```java
@GetMapping(value = "/permission/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(value = "id") String id) throws Exception {
    Map map = permissionService.findById(id);
    return new Result(ResultCode.SUCCESS, map);
}
```

画面7：
```java
@DeleteMapping(value = "/permission/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(value = "id") String id) throws Exception {
    permissionService.deleteById(id);
    return new Result(ResultCode.SUCCESS);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
