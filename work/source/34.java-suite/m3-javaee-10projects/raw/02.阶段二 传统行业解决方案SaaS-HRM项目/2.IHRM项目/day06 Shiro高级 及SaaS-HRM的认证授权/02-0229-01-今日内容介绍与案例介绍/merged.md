# 01-今日内容介绍与案例介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\01-今日内容介绍与案例介绍_【海量资源尽在 ubkz.com】.mp4
- 时长 6分43秒（音频 403s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 各位朋友大家好今天是我们这个SaaS系统的第六天那在进入我们内容之前呢简单的对今天要学的这些点呢做一个说明对于今天呢我们要做的内容呢相对来说不是很多全部都是围绕在Sherlock以及他在我们web应用当中的一些特点的一些说明那我们首先看的第一块呢是Sherlock如何在我们Spring Boot的工程当中去使用
[00:32] 我们可以写一个简单的案例去看一下在Springboard当中如何整合Shera如何借助Shera的特性完成我们全线相关的一个开发和我们全线相关的一块控制好了在Shera当中它涉及一个比较高级的一个特性就是叫做绘画管理Shera不仅提供我们Java Web
[00:54] 也提供Java SE等等相关的绘画管理所以第二块呢我们来看一下Sheryl当中的绘画究竟是怎么回事以及基于它这个绘画管理我们可能对我们的系统结构或者对我们的系统架构上面又有什么对我们帮助的地方好了那接着前两块我们都搞定了之后接下来呢我们就可以综合的运用我们Sheryl相应的内容去完成我们
[01:20] SaaS人力资源管理系统的第二种认证方式之前我们是结合JWT的方式来做的那我们今天就是使用Sherlock的方式一起来看一下如何去完成好了这个就是我们今天相应的三框内容的一个简单介绍咱们先看第一个就是一个Sherlock在web工程的一个应用当然我讲的是Spring Boot工程的应用那接着就是说呢咱们都知道Sherlock它是一个极其功能强大的这么一个安全框架
[01:49] 那他呢可以对我们的认证授权等等很多的内容他都有一些他都会进行统一的进行管理那现在呢这个sharewell已经越来越广泛的应用在企业当中了那我们之前学习sharewell呢全部都是以最简单的SE简单案例的形式来看了一下sharewell如何做认证如何叫授权如何自定义任务那以及我们看了一下sharewell它整个认证授权它的一个
[02:19] 执行的一个过程那之前的还是着重介绍它的一个执行的一个原理那我们今天呢就是有案例的形式来看一下在我们的应用当中如何去做那首先呢在这边跟各位介绍一下就是说我们这个Spring Boot搭建的这个工程可能有一个简单的案例那这个案例呢其实就是从我们这个SaaS人力资源管理系统当中呢提取出来的一点点内容
[02:42] 我们这边还是一个RBAC的这么一个模型这个模型当中包含了用户包含了角色包含了权限它们之间全部都是多对多关系如果各位还有印象的话和我们SaaS人力自动管系统里面基本上差不多只不过权限表这边少了三个一对一OK好了当然了这些数据库表在今天的资料当中也给各位准备好了我们一起来看一下第六天
[03:11] 资源其中有一个shadowdb那这是我们今天要用到的数据库表里面呢就这么几张表里添加了一些基础的一些数据好了除了这个表之外还有就是为了我们这个学习呢只专注于shadow相关的内容那我把今天的基本的这个工程呢也给各位准备好了里面的工程其实就是一些简单的我们叫做渡曼实体类写了一些简单的do写了一些简单的Service那同样的
[03:39] 这个案例工程也在我们今天这个share案例代码当中我们只需要打开我们的idea好了打开我们的idea那我们之前呢写了一个简单的share account text这么一个工程好了我这边再重新打开一下share account textnew window好了我们要做的事情呢其实很简单只需要把这个工程啊放到我们的工程目录下并且把它引入进来其实就可以了
[04:14] 在这边呢我找到我们的工程的代码地址好了workspace下进去好了在这边我把它拷过来拷过来之后呢在我这边呢直接引入到我当前的这个模块当中其实就可以了fill new model from exciting source好了找到它没问题工程没问题好了next一路next点击finishok其实就可以了好了那这样一来呢我这个基本的案例工程也给各位引进来了
[04:50] 那接下来我们可以简单的来看一下就是这个工程里面的一些基本的代码好了在这边呢我们可以打开首先呢看我们的Domain类就是这么几个实体类当然都比较简单和我们之前SaaS人力资管管理系统里面设计的这些实体类都是一模一样的只不过是在属性和字段上面做了一些简单的增减那除了
[05:16] 我们的笃门类之外呢还有我们的do,do只提供了一个就是我们叫做user do在里面呢是根据用户名查询好了这边刚才忘了简单的提一下了就是在这边用户和角色是一个多对多关系那角色和权限同样也是一个多对多关系我们都是已经配置好的都是配置好的好了那接下来do看过了之后呢还有Service那Service这边呢就是一个user Service当然了都比较简单
[05:45] 通过Find by name查询以及Find all得到所有用户那这个看过了之后呢还有我们叫做ControllerController就是UserController了里面呢很典型的我是用的ResetFood风格的一种编码好了在这边呢-UserPost方法添加好了查询等等这些功能呢我们都没有实现我们主要是看一下要对访问这些方法的要对访问的这些方法做权限的一个控制所以这里面的实现呢我就都没有写
[06:13] 当然了这边还有一个叫做用户登录咱们只是写了一个大致的一个轮廓在里面好了那这些我们都看过了之后当然还有最后一个就是share application这里面写的是一个我们基本一个启动类OK好了这个就是我们的案例的一个代码那我们一会儿呢只是关注于在这个案例的代码上边呢我们去添加share的相关的一些功能完成整个share的一个权限控制其实就可以了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在Spring Boot项目中整合Shiro框架，实现用户认证与授权功能，基于已有的数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT标题页，内容为“第6章 Shiro高级及SaaS-HRM的认证授权”，学习目标包括理解Shiro登录方式、拦截器、自定义realm、会话管理及实现SaaS-HRM中的Shiro认证与授权。
画面2：展示PPT内容“1.1 案例说明”，说明使用Spring Boot构建应用并整合Shiro完成用户认证与授权，并展示“1.1.1 数据库表”部分的架构图。
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

