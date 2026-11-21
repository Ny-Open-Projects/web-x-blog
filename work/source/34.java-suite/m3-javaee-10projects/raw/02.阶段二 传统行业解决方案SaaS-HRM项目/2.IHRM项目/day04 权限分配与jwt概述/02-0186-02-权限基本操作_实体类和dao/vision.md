# 画面线理解：02-权限基本操作：实体类和dao

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\02-权限基本操作：实体类和dao_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:40, 00:59, 01:08, 01:19, 01:50, 02:24, 02:36, 03:37, 04:22, 04:50, 05:10, 05:52, 06:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:48:52

1) 这一组画面整体在讲什么（一句话）：
讲解 SaaS-HRM 系统中权限管理模块的后端实现，包括实体类设计、数据库表结构及 DAO 层接口定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 系统桌面，任务栏显示多个应用程序图标，鼠标悬停在 Chrome 浏览器图标上。
画面 2: 展示 PPT 页面，标题为“1.2 后端实现”，子标题“1.2.1 实体类”，内容包含数据库表结构图（菜单表、按钮表、API接口表、权限表）及实体类代码片段。
画面 3: IntelliJ IDEA 开发环境，项目结构显示 `ihrm_parent` 下的 `ihrm_common_model` 模块，选中 `Permission` 类。
画面 4: Windows 资源管理器，路径为 `ihrm/day4/实体类`，选中三个 Java 文件：`Permission.java`、`PermissionMenu.java`、`PermissionPoint.java`。
画面 5: IntelliJ IDEA 中弹出“Copy”对话框，提示文件 `PermissionMenu.java` 已存在，提供“Overwrite”、“Skip”、“Overwrite for all”、“Skip for all”选项。
画面 6: IntelliJ IDEA 编辑器显示 `PermissionMenu.java` 代码，包含 `@Entity`、`@Table(name = "pe_permission_menu")` 注解及类定义。
画面 7: IntelliJ IDEA 编辑器显示 `Permission.java` 代码，包含 `@Entity`、`@Table(name = "pe_permission")` 注解及类定义。
画面 8: IntelliJ IDEA 项目结构视图，选中 `Permission` 类，编辑器显示 `Permission.java` 代码。
画面 9: Microsoft PowerPoint 空白画布，准备绘制流程图。
画面 10: PowerPoint 画布上绘制了“菜单”和“按钮”两个矩形框，中间用箭头连接，箭头指向“按钮”框。
画面 11: IntelliJ IDEA 项目结构视图，选中 `Permission` 类，编辑器显示 `Permission.java` 代码。
画面 12: IntelliJ IDEA 项目结构视图，选中 `resources` 目录。
画面 13: IntelliJ IDEA 编辑器显示 `UserDao.java` 代码，定义了 `UserDao` 接口。
画面 14: IntelliJ IDEA 编辑器显示 `PermissionApiDao.java` 代码，定义了 `PermissionApiDao` 接口。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@Entity
@Table(name = "pe_permission")
public class Permission implements Serializable {
    @Id
    private String id;
    // 权限名称
    private String name;
    // 权限类型 1为菜单 2为功能 3为API
    private Integer type;
    // 权限编码
    private String code;
    // 权限描述
    private String description;
    // 权限ID
    private String pid;
    // 是否禁用
    private Integer enVisible;
}
```
画面 6:
```java
@Entity
@Table(name = "pe_permission_menu")
public class PermissionMenu implements Serializable {
    @Id
    private String id;
    // 显示图标
    private String menuIcon;
    // 父节点ID
    private String menuPid;
}
```
画面 7:
```java
@Entity
@Table(name = "pe_permission")
public class Permission implements Serializable {
    @Id
    private String id;
    // 权限名称
    private String name;
    // 权限类型 1为菜单 2为功能 3为API
    private Integer type;
    // 权限编码
    private String code;
    // 权限描述
    private String description;
    // 权限ID
    private String pid;
    // 是否禁用
    private Integer enVisible;
}
```
画面 13:
```java
package com.ihrm.system.dao;
import com.ihrm.system.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
public interface UserDao extends JpaRepository<User, String>, JpaSpecificationExecutor<User> {
}
```
画面 14:
```java
package com.ihrm.system.dao;
import com.ihrm.system.entity.PermissionApi;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
public interface PermissionApiDao extends JpaRepository<PermissionApi, String>, JpaSpecificationExecutor<PermissionApi> {
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“1.2 后端实现”，子标题“1.2.1 实体类”。架构图包含四个实体框：菜单表、按钮表、API接口表、权限表。箭头从“菜单表”指向“权限表”，从“按钮表”指向“权限表”，从“API接口表”指向“权限表”，表示三者与权限表之间是一对一关系。
画面 10: 流程图包含两个矩形框：“菜单”和“按钮”。从“菜单”框引出一条带箭头的线指向“按钮”框。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
