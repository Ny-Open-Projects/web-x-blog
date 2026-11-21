# 02-权限基本操作：实体类和dao

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\02-权限基本操作：实体类和dao_【海量资源尽在 ubkz.com】.mp4
- 时长 6分4秒（音频 364s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 简单的看了一下我们这个权限管理的需求其实就是对这几张表的一个基本增长改查的这么一个操作那接下来呢我们回到讲义那我们都知道这张表之间呢都是一个一对一关系那我这个一对一关系其实是使用共享主见的形式来做的那也就是说API这边的ID和我们权限如果有关系的话那权限的ID就是API ID同理按钮和权限菜单和权限
[00:32] 他们的ID是不是应该都是保持一致的这么一个情况啊OK那这些呢我们都说过了之后呢接下来接下来我们就可以在我们的后端或者在我们的Java后台去完成基本权限的这个操作了那么完成权限的这个操作其实跟之前的套路基本上都是一模一样的首先搞这个实体类那我们的实体类呢其实在昨天写代码的时候呢已经把相应的实体类给它copy到
[01:01] 我的这个操我的这个代码当中了当然如果你不放心的话我在今天的资源当中也把这些实体类给各位准备好了Ctrl C把它放到我们系统管理的哎实体类模块下OKall right全部all right那好了我们简单的来看一下这几个实体类那首先呢API点到哪一个算哪个API里面有相应的一些API下的资源的一些配置属性
[01:32] 比如说当前请求的这个APM是我们访问的后台的一个链接那API URL指的是API的URL地址链接是什么请求呢方式有很多get,pull,delete等等当然还有一个API level这是我们的一个预留字段目前也没使用那接下来呢还有一个就是我们的menu就是菜单那对于一个菜单来说它可能有自己主件它可以有自己的ID等等它的icont还有这个排序号就是因为菜单呢它可能有顺序的
[02:01] 那接着还有一个pontpont呢这边我们把它叫做一个权限点其实我们这边可以把它简单的理解成就是我们就是我们页面当中的一个按钮这个里面有当前这个按钮的class也就是样式是什么它的icon还有它的状态好了那接着我们回过头来看permission它代表的是我们真正的权限那这个权限当中有ID不多说了有权限名称那这个权限名称比如说呢就是我们的
[02:30] 如果对应的菜单而言菜单里面你会发现没有名称我其实把它抽取到了permission那如果是菜单的话这个代表的就是菜单名如果代表的是权限点那代表的就是按钮名如果代表的API那就是API的名称这个都好理解都好理解好了那接下来还有tap因为我们说过了那这个权限它既能代表API又能代表菜单又能代表按钮那通过一个tap类型来进行区分
[02:57] 当然这边还有一个code这个code呢指的是我们的权限编码这个权限编码呢是比较重要的一个配置是因为我们之后要做权限控制的时候不管是前端的菜单还是后端的API甚至是我们按钮的那些配置全部都是根据code进行比较看一下你当前这个人有没有当前的这个权限编码如果有就让你过如果没有就给你拦截处理
[03:26] OK那接下来呢还有一个权限描述不多说了PID我们之前都知道对一个菜单而言或者对于一个按钮而言以一个这边一张图形的声简单的说一下那比如说呢左边的代表的是我的一列菜单代表的是一个一个的菜单那我点击这个菜单会进入到真正的一个页面
[03:55] 那这个页面当中是不是又可以有很多的我们叫做按钮所以大家就应该要得知了一个菜单下可能对应一个按钮那他们之间必然有这么一个从属关系那比如说呢还有你这个菜单下呢可能访问进来可能要访问一些API这边叫API那同样的你按钮这边是不是同样的可能点击按钮触发事件也要调用我们后台的一个API接口
[04:33] 所以这个就比较明确了所以这个就比较明确了就是说我们这个权限它是有一个上下级关系的菜单下有按钮那这个按钮它是不是就属于菜单它的一个子的一个权限OK那这个我们就说清了所以来了一个PID它指的是我付权限的ID究竟是什么我付菜单究竟是什么OK还有一个EnterpriseVisibleVisible指的是我们的可见性可见状态
[05:04] OK那这样一来我基本的几个实体类就已经跟各位都说清楚了那实体类我们都已经写好了之后呢接下来就根据我们的作业套路其实都是一样的写好实体类那接着我们开始写DU那对于DU呢其实跟我们之前配置企业配置用户或者配置我们昨天的角色基本上都是一模一样的很简单写一个接口继承
[05:33] GPA repository继承GPA specification executor这些代码呢都比较简单所以在今天的资源当中呢我也给各位准备好了这四个DO接口Ctrl C注意这些呢全部都属于我们系统管理这个V服务下的所以把这个内容呢全部都call到system DO下即可Ctrl VOK全部都call过来了那这样一来我基本的实体类基本的DO就已经都搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

