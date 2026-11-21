# 画面线理解：11-分配权限，分配角色：测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\11-分配权限，分配角色：测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:23, 00:28, 00:46, 01:00, 01:06, 01:12, 01:28, 01:44, 01:50, 02:12, 02:23, 02:46, 02:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:55:03

1) 这一组画面整体在讲什么（一句话）：
演示在 HRM 系统中，通过前端界面分配员工角色，并在后端代码和数据库中验证该功能的实现过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中，查看并修改 RoleController.java 文件，其中包含一个 PUT 请求映射方法，用于处理分配角色的逻辑。
画面 2: 在终端中运行 Spring Boot 应用，显示启动日志，确认应用成功启动。
画面 3: 在终端中，因在 RoleController 中重复定义了 save 方法，导致 Spring Boot 启动失败并抛出 Ambiguous mapping 异常。
画面 4: 在 HRM 系统前端界面，显示“角色管理”页面，包含角色列表和操作按钮。
画面 5: 在 IntelliJ IDEA 中，将 RoleController.java 文件中的 save 方法的请求路径从 "/user/assignroles" 修改为 "/role/assignPerm"。
画面 6: 在 HRM 系统前端界面，点击“员工”菜单项，进入员工列表页面。
画面 7: 在 HRM 系统前端界面，显示员工列表，包含员工编号、姓名、手机号、工号、聘用形式、部门等信息。
画面 8: 在 HRM 系统前端界面，点击某员工的“分配角色”按钮，弹出“分配角色”对话框，其中“人事经理”和“系统管理员”角色被选中。
画面 9: 在 SQLyog 数据库工具中，执行 SQL 查询语句，查询用户与角色的关联表（user_role）。
画面 10: 在 HRM 系统前端界面，点击“分配角色”对话框中的“提交”按钮，完成角色分配。
画面 11: 在 SQLyog 数据库工具中，执行 SQL 查询语句，查询角色与权限的关联表（role_permission）。
画面 12: 在 SQLyog 数据库工具中，执行 SQL 查询语句，查询权限表（permission）。
画面 13: 在 HRM 系统前端界面，点击“员工”菜单项，进入员工列表页面。
画面 14: 在 HRM 系统前端界面，点击某员工的“分配角色”按钮，弹出“分配角色”对话框，其中“人事经理”角色被选中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@RestController
@RequestMapping("/sys")
public class RoleController extends BaseController {
    @Autowired
    private RoleService roleService;

    /**
     * 分配权限
     */
    @RequestMapping(value = "/user/assignroles", method = RequestMethod.PUT)
    public Result save(@RequestBody Map<String,Object> map) {
        //1.获取角色id
        String roleId = (String) map.get("id");
        //2.获取权限的id列表
        List<String> permIds = (List<String>) map.get("permIds");
        //3.调用service完成权限分配
        roleService.assignPerms(roleId, permIds);
        return new Result(ResultCode.SUCCESS);
    }
```

画面 5:
```java
@RequestMapping(value = "/role/assignPerm", method = RequestMethod.PUT)
public Result save(@RequestBody Map<String,Object> map) {
    //1.获取角色id
    String roleId = (String) map.get("id");
    //2.获取权限的id列表
    List<String> permIds = (List<String>) map.get("permIds");
    //3.调用service完成权限分配
    roleService.assignPerms(roleId, permIds);
    return new Result(ResultCode.SUCCESS);
}
```

画面 9:
```sql
SELECT u.id, u.name, p.code, p.type, p.permission_code, p.permission_description, p.permission_url
FROM user_role ur
JOIN user u ON ur.user_id = u.id
JOIN role r ON ur.role_id = r.id
JOIN permission p ON r.id = p.role_id
WHERE u.id = 1 AND r.id = 1 AND p.id = 1
```

画面 11:
```sql
SELECT r.id, p.permission_id
FROM role r
JOIN role_permission rp ON r.id = rp.role_id
JOIN permission p ON rp.permission_id = p.id
WHERE r.id = 1
```

画面 12:
```sql
SELECT id, permission_code, permission_description, permission_url
FROM permission
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
