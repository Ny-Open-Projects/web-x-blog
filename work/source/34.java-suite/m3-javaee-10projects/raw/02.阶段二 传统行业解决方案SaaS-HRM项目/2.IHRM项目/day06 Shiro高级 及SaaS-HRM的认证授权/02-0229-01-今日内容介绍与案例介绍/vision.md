# 画面线理解：01-今日内容介绍与案例介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\01-今日内容介绍与案例介绍_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:45, 02:33, 03:02, 03:17, 03:28, 03:52, 04:04, 04:26, 04:38, 04:48, 05:09, 05:38, 05:55, 06:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:26:49

1) 这一组画面整体在讲什么（一句话）：
讲解如何在SpringBoot项目中整合Shiro框架，实现用户认证与授权功能，基于已有的数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT标题页，内容为“第6章 Shiro高级及SaaS-HRM的认证授权”，学习目标包括理解Shiro登录方式、拦截器、自定义realm、会话管理及实现SaaS-HRM中的Shiro认证与授权。
画面2：展示PPT内容“1.1 案例说明”，说明使用SpringBoot构建应用并整合Shiro完成用户认证与授权，并展示“1.1.1 数据库表”部分的架构图。
画面3：展示PPT“1.1.1 数据库表”部分的架构图，包含用户表、角色表、权限表、用户关联角色表、角色权限表及其关联关系。
画面4：展示Notepad++编辑器中的SQL脚本，包含插入权限记录、创建pe_role表结构、插入角色记录、创建pe_role_permission表结构。
画面5：展示PPT“1.1.2 基本工程结构”，说明导入资料中准备的基本工程代码，实现了基本用户角色权限操作，只需添加Shiro相关代码即可。
画面6：展示IntelliJ IDEA中打开项目时的弹窗，询问新项目是打开在当前窗口还是新窗口。
画面7：展示IntelliJ IDEA中打开的Shiro源码文件，显示`doSingleRealmAuthentication`和`doMultiRealmAuthentication`方法的代码。
画面8：展示IntelliJ IDEA中打开的Shiro源码文件，显示`doSingleRealmAuthentication`和`doMultiRealmAuthentication`方法的代码，光标在`while`循环处。
画面9：展示IntelliJ IDEA中“Select File or Directory to Import”对话框，路径为`E:\workspace\idea\shiro-test`，选中`shiro_springboot`模块。
画面10：展示IntelliJ IDEA中“Split Vertically”等选项的右键菜单。
画面11：展示IntelliJ IDEA中`User.java`类的代码，包含@Entity、@Table注解，以及与Role的@ManyToMany关联。
画面12：展示IntelliJ IDEA中`Role.java`类的代码，包含@Entity、@Table注解，以及与User和Permission的@ManyToMany关联。
画面13：展示IntelliJ IDEA中`UserController.java`类的代码，包含add、find、update、delete、login等方法。
画面14：展示PPT“1.1.2 基本工程结构”和“1.2 整合Shiro”部分，说明导入资料中准备的基本工程代码，只需添加Shiro相关代码即可。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4 SQL：
-- Records of pe_permission
INSERT INTO `pe_permission` VALUES ('1', '添加用户', 'user-add', null);
INSERT INTO `pe_permission` VALUES ('2', '查询用户', 'user-find', null);
INSERT INTO `pe_permission` VALUES ('3', '更新用户', 'user-update', null);
INSERT INTO `pe_permission` VALUES ('4', '删除用户', 'user-delete', null);

-- Table structure for pe_role
DROP TABLE IF EXISTS `pe_role`;
CREATE TABLE `pe_role` (
  `id` varchar(4) NOT NULL COMMENT '主键ID',
  `name` varchar(40) DEFAULT NULL COMMENT '权限名称',
  `description` varchar(255) DEFAULT NULL COMMENT '说明',
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_k3berrf7gqlfn58g5f2yvog4li` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Records of pe_role
INSERT INTO `pe_role` VALUES ('1', '系统管理员', '系统日常维护');
INSERT INTO `pe_role` VALUES ('2', '普通员工', '普通操作权限');

-- Table structure for pe_role_permission
DROP TABLE IF EXISTS `pe_role_permission`;
CREATE TABLE `pe_role_permission` (
  `role_id` varchar(4) NOT NULL,
  `permission_id` varchar(4) NOT NULL,
  KEY `FK_role_permission` (`role_id`),
  KEY `FK_permission_role` (`permission_id`),
  CONSTRAINT `FK_role_permission` FOREIGN KEY (`role_id`) REFERENCES `pe_role` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_permission_role` FOREIGN KEY (`permission_id`) REFERENCES `pe_permission` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

画面11 Java代码：
@Entity
@Table(name = "pe_user")
public class User implements Serializable {
    private static final long serialVersionUID = 4297464181893970382L;
    @Id
    private String id;
    private String username;
    private String password;
    @ManyToMany(fetch = FetchType.EAGER)
    @JoinTable(name = "pe_user_role", joinColumns = {@JoinColumn(name = "user_id", referencedColumnName = "id")},
            inverseJoinColumns = {@JoinColumn(name = "role_id", referencedColumnName = "id")})
    private Set<Role> roles = new HashSet<>();

画面12 Java代码：
@Entity
@Table(name = "pe_role")
public class Role implements Serializable {
    private static final long serialVersionUID = 594829328797158219L;
    @Id
    private String id;
    private String name;
    private String description;
    //角色与用户 多对多
    @ManyToMany(fetch = FetchType.EAGER)
    @JoinTable(name = "pe_user_role",
            joinColumns = {@JoinColumn(name = "role_id", referencedColumnName = "id")},
            inverseJoinColumns = {@JoinColumn(name = "user_id", referencedColumnName = "id")})
    private Set<User> users = new HashSet<>();
    //角色与权限 多对多
    @ManyToMany(fetch = FetchType.EAGER)
    @JoinTable(name = "pe_role_permission",
            joinColumns = {@JoinColumn(name = "role_id", referencedColumnName = "id")},
            inverseJoinColumns = {@JoinColumn(name = "permission_id", referencedColumnName = "id")})
    private Set<Permission> permissions = new HashSet<>();

画面13 Java代码：
@RestController
public class UserController {
    @Autowired
    private UserService userService;
    //添加
    @RequestMapping(value = "/user", method = RequestMethod.POST)
    public String add() { return "添加用户成功"; }
    //查询
    @RequestMapping(value = "/user", method = RequestMethod.GET)
    public String find() { return "查询用户成功"; }
    //更新
    @RequestMapping(value = "/user/{id}", method = RequestMethod.PUT)
    public String update(String id) { return "更新用户成功"; }
    //删除
    @RequestMapping(value = "/user/{id}", method = RequestMethod.DELETE)
    public String delete() { return "删除用户成功"; }
    //用户登录
    @RequestMapping(value = "/user/login", method = RequestMethod.POST)
    public String login(String username, String password) {
        System.out.println("用户登录");
        return "登录成功";
    }

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2 PPT标题：“1.1 案例说明”，内容：“使用springBoot构建应用程序，整合shiro框架完成用户认证与授权。”
画面3 PPT标题：“1.1.1 数据库表”，架构图包含：
- 用户表（用户ID、用户名、用户密码）
- 角色表（角色ID、角色名、角色描述）
- 权限表（权限ID、权限标识、权限描述）
- 用户关联角色表（用户ID、角色ID）
- 角色权限表（角色ID、权限ID）
- 关联关系：用户表通过`FK_US_USER`指向用户关联角色表，角色表通过`FK_US_ROLE`指向用户关联角色表，权限表通过`FK_US_PERMISSION`指向角色权限表，用户关联角色表通过`FK_US_ROLE`指向角色表，角色权限表通过`FK_US_PERMISSION`指向权限表。
画面5 PPT标题：“1.1.2 基本工程结构”，内容：“导入资料中准备的基本工程代码，此工程中实现了基本用户角色权限的操作，我们只需要在此工程中添加Shiro相关的操作代码即可。”
画面14 PPT标题：“1.1.2 基本工程结构”和“1.2 整合Shiro”，内容：“导入资料中准备的基本工程代码，此工程中实现了基本用户角色权限的操作，我们只需要在此工程中添加Shiro相关的操作代码即可。”

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
