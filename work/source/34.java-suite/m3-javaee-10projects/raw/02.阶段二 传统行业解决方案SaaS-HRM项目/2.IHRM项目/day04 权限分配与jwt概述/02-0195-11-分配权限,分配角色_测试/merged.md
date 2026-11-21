# 11-分配权限，分配角色：测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\11-分配权限，分配角色：测试_【海量资源尽在 ubkz.com】.mp4
- 时长 3分8秒（音频 189s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 分配角色分配权限的这些代码我们都写好了之后接下来我们就可以一起来启动一下测试一下我们当前的这个代码究竟有没有问题好了这边直接重启我们的服务就可以了好了这边开始启动大家耐心等待一下抱歉这边报了一个错误我们来看一下说There is already已经存在的这么一个请求
[00:40] 这边找到了我们分配权限的时候访问的应该是肉这个请求下的这个连接下的肉的sign p r e mok ctrl c拿过来ctrl vok抱歉这个有点粗心了咱们再启动一下好了这边的程序让它去启动我们直接打开页面来看一下究竟这几个功能呢好不好用啊刷新一下看一下
[01:12] 服务器OK好了这边员工的信息已经出现了右边已经把分配角色的按钮给各位绑定上了我们今天的页面全部都提供好了分配角色点击进来之后好了这边有当前的所有的角色的一些内容好了我随便点两个各位跟我一起来看一下目前我们角色和用户数据库表里面一共有这么多条记录123456这记录是不是有点多
[01:40] 我删两条吧好了删除两条记录那接着呢我随便分配一个看一下能不能分配成功好了多了四条走明显的看到这个记录肯定是多了别管多了几条肯定是有了那好了这个呢我们看过了其实分配员工分配角色是没有问题的接下来就是分配权限那分配权限找到角色这边我们随便找一个分配权限
[02:07] 那分配权限呢我这边都勾选上都勾选上都勾选上都勾选都勾选那接着我们找到权限到角色中间表有这么多条数据刷新一把这么多条好了接着我点确定这边操作成功我刷新数据库会发现这回内容就比较多了OK那这个其实侧面证明了其实我们已经完成了分配权限分配角色的这个操作但是呢我们这个代码呢还是有一点点问题不够理想不够理想的点在什么地方
[02:36] 是这样的比如说呢刚才我已经对薪资专员分配了权限那我一点你没发现他应该最好有一个回显的这么一个过程包含呢员工这边他同样存在这个问题那各位来看我们刚才呢其实对张森这个员工也分配了角色那我打开之后呢他内容什么都没有这什么都没有所以就是说目前呢已经完成了分配权限分配角色的这个操作但是最好还给他把我们
[03:05] 这些回写的内容也给它添加上才好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
        //3.调用Service完成权限分配
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
    //3.调用Service完成权限分配
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

