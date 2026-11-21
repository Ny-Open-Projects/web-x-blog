# 15-权限业务接口-根据角色获取权限信息接口实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着咱们就来实现根据角色ID查找对应的菜单操作信息接口

以及根据角色ID来查找对应的菜单信息数据接口

这两个接口是通过HitOS方式进行的实现

在前端对用户的角色权限做判断的时候

需要去调取和使用

咱们来看一下具体的实现

首先我们看根据角色ID来查找获取对应的菜单数据接口

这个接口不涉及过多的业务规则处理

但是它需要画表查询

我们知道JPA接口的话

一般都是单表进行映射的查询

根据方法名称做对应的色口映射

我们来看一下如何去实现画表查询

在这里我们是通过AUQL语句的方式去实现的自定义查询

我们从代码上面

做具体的实现

public

类似的返回一个数据集合对象

menu operation

方法名称就是vendorby

noid

这里面要存立个参数

参数就是角色ID

类型是long

这里重点是HQL语句的查询实现

我们通过query误解

然后去编写HQL语句

这个呢

跟色口的语法有点类似

但是呢

它是面向对象的查询

所以呢

我们不会看到对应的表都是呢

对象的名称

它要和哪个表进行关联呢

它需要和角色对应的操作关联关系表的进行关联

autority

然后这个是load

operation

然后给它一个别名

这样子叫load

然后呢

我们再做一个拼接

加上对应的条件

loadority.loadid

要等于我们存立的参数

这个参数位置呢

是从1开始

我们用这种方式进行标识

然后呢

还加上它的条件

menu

ority.state

要等于1

接着的话呢

再加上它们的两个表的拼接连接条件

loadoperator

这张表呢

menu

operator

这个呢

就是我们的标识

我们的标识

我们的标识

这个呢

就是自定义hql的实现

我们完成了根据角色ID去获取菜单操作信息

接着的话呢

我们再加上它对应的swork2的注解

swork2这部分注解的运用呢

我们在下面上间呢

可以做详细的讲解

在这里呢

我们可以先直接拖逼过来

这样呢

我们就会需要再加上那个注释

通过这里面的注释说明了

我们就可以知道这个接口的具体作用

接着的话呢

我们再实现下面这个接口

根据角色ID去查找对应的菜单信息

这个呢

也是要用于前端查询展示

大家注意一下

对于关联的查询呢

一般我们将返回的结果集

它是和哪个实体关联

就把方法呢

定义在对应的数据审结果上面

所以呢

在这里我们把这个接口呢

是写在authority menu

reversitory这个接口上面

并没有写在角色的reversitory数据审结果上面

因为呢它的返回结果集呢

就是authority menu

好那咱们呢做一个具体的实现

回到咱们的代码当中

找到authority menu reversitory数据审结果

这里呢我们添加一个方法

它的返回对象呢

也是一个集合

fund by

logid

将参数呢

还没进来

然后呢我们就实现自定义了

AQL的查询

通过credit注解

到stack

菜单对象

from

authority menu

给它一个别名叫menu

它要连接呢

authority

load menu的关联表

load menu

我们给它一个别名叫load menu

然后呢连接一下

这里呢是

加上它的条件

load menu

点load id

这里呢我们采用单位户的形式

去选递对应参数

然后再加上它的条件

space

要等于1

就是有效的数据

然后再拼接一下

这个呢是两方表的连接条件

根据load menu里面的menu id字段

和menu表里面的id字段进行放点

好这样呢

咱们就完成了这个数据层接口的AQL语句的编写

接着呢我们也将它的注释呢

加入进来

这个呢是SW2的

读解说明

好

这样呢咱们就完成了

这两个数据层接口

这两个接口呢

都是前端做全线处理时

所需要用到的

那么我们可以看到

在这里呢

它都是返回一个

集合对象

因为呢它的数据量并不大

并且呢前端是仪式性调用查询

不需要去做

更业处理

一个系统

做的再大最多呢也就

几百个菜单

对不对

而且这些数据呢并非用于

界面的呈现和查看

它是用于全线逻辑的

控制和处理

所以呢咱们不需要做

分页的处理

如果说有特殊需求要做分页处理呢

咱们呢就不用

采用这种方式

可以呢再去通过

自定义的数据层接口再做一层包装

去实现了分页的查询功能

当然

我们在这里实现了

VibroC图里

我们在这里实现了

VibroC图里

使用DataLess

这个接口呢

它都可以支持分页

还有排序的

功能处理

这些呢是对于

单个数据表的查询

也就是说咱们这个数据层接口

所映射的实体数据的查询

如果是要采用这种据文的方式呢

进行查询呢

咱们呢还去通过

包装的方式再做一层实现

这个就根据咱们的需要

去灵活处理

好这一讲呢就是对角色ID

查找对应的菜单信息接口

以及呢根据角色ID

查找对应的

菜单操作信息接口的实现

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个基于 Spring Boot 的后台管理系统权限模块开发教程。讲师正在讲解如何通过自定义的 HQL 查询语句，实现根据角色 ID 查询其对应的菜单操作信息的功能。核心内容包括：
- **接口定义**：使用 `@RepositoryRestResource` 注解定义 REST 接口，并通过 `@ApiImplicitParams` 注解为接口参数添加 Swagger2 文档说明。
- **数据访问层**：在 `AuthorityMenuOperationRepository` 接口中，使用 `@Query` 注解编写 HQL 查询语句，实现跨表关联查询。
- **技术要点**：强调 HQL 是面向对象的查询语言，避免了直接使用表名和列名，简化了实体映射过程。
- **后续内容预告**：视频最后提到了“3.8 Spring Data Rest 高级用法（拓展）”，暗示接下来会讲解如何集成 Swagger2 以自动生成 API 文档。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，讲师在 Typora 编辑器中展示课程大纲，当前章节为“3.7 权限核心逻辑接口实现（重要）”。
*   **00:00:05 - 00:00:15**：讲师在 Typora 中讲解“根据角色ID查找对应的菜单操作信息接口”，并指出该接口需要通过 HQL 实现跨表查询。
*   **00:00:15 - 00:00:25**：讲师切换到 IntelliJ IDEA，展示项目结构，并定位到 `AuthorityMenuOperationRepository` 接口文件。
*   **00:00:25 - 00:00:35**：讲师在 IDEA 中编辑 `AuthorityMenuOperationRepository` 接口，编写 `findByRoleId` 方法，并添加 `@Query` 注解。
*   **00:00:35 - 00:00:45**：讲师在 IDEA 中编写 HQL 查询语句，通过 `roleOpt.roleId = ?1` 和 `menuOpt.id = roleOpt.operationId` 实现关联查询。
*   **00:00:45 - 00:00:55**：讲师在 Typora 中总结 HQL 的优势，并引出下一个知识点“3.8 Spring Data Rest 高级用法（拓展）”。
*   **00:00:55 - 00:01:05**：讲师在 Typora 中展示“3.8 Spring Data Rest 高级用法（拓展）”章节，预告接下来将讲解 Swagger2 的集成。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **章节标题**：`3.7 权限核心逻辑接口实现（重要）` 和 `3.8 Spring Data Rest 高级用法（拓展）`。
    *   **接口说明**：`根据角色ID查找对应的菜单操作信息接口`。
    *   **技术要点**：`HQL是面向对象的查询语句，注意不能直接使用表名与列名，参数通过占位符引用。通过HQL实现简单方便，不需要再做实体映射，它能够自动对结果集进行映射关联处理。`

*   **代码关键内容**：

    **1. `AuthorityMenuOperationRepository` 接口定义 (HQL 查询)**

    ```java
    @RepositoryRestResource(path = "/authorityMenuOperation")
    public interface AuthorityMenuOperationRepository extends
            PagingAndSortingRepository<AuthorityMenuOperation, Long>,
            JpaSpecificationExecutor<AuthorityMenuOperation> {

        @ApiOperation(value = "根据角色ID查找对应的菜单操作信息")
        @ApiImplicitParams({
            @ApiImplicitParam(value = "角色ID", name = "roleId",
                    dataType = "string", required = true)
        })
        @Query("select menuOpt from AuthorityMenuOperation menuOpt, AuthorityRoleOperation roleOpt " +
                "where roleOpt.roleId = ?1 and menuOpt.status = 1 " +
                "and roleOpt.operationId = menuOpt.id")
        public List<AuthorityMenuOperation> findByRoleId(@Param("roleId") Long roleId);
    }
    ```

    **2. `AuthorityMenuRepository` 接口定义 (另一个 HQL 查询)**

    ```java
    @ApiImplicitParams({
        @ApiImplicitParam(value = "机构预置类型编号", name = "institutionTypeId", dataType = "string")
    })
    public List<AuthorityMenu> findByInstitutionTypeId(@Param("institutionTypeId") String institutionTypeId);

    @ApiImplicitParams({
        @ApiImplicitParam(value = "角色ID", name = "roleId", dataType = "string", required = true)
    })
    @Query("select menu from AuthorityMenu menu, AuthorityRoleMenu roleMenu " +
            "where roleMenu.roleId = ?1 and menu.status = 1 " +
            "and roleMenu.menuId = menu.id")
    public List<AuthorityMenu> findByRoleId(@Param("roleId") Long roleId);
    ```

*   **图表/演示**：
    *   **IDEA 项目结构图**：展示了 `repository` 包下的多个 Repository 接口，如 `AuthorityMenuOperationRepository`、`AuthorityRoleRepository` 等。
    *   **代码编辑过程**：通过光标移动和代码高亮，演示了如何编写和修改 HQL 查询语句。

---

### 4) 关键场景与演示描述

*   **场景一：接口定义与 HQL 查询**
    *   **描述**：讲师在 Typora 中首先介绍了 `AuthorityMenuOperationRepository` 接口的功能和实现方式。随后，他切换到 IntelliJ IDEA，在代码编辑器中实际编写了 `@Query` 注解的 HQL 查询语句。该语句通过 `roleOpt.roleId` 和 `menuOpt.id` 进行关联，查询出满足条件的菜单操作信息。
    *   **技术点**：强调了 HQL 的优势，即无需手动处理实体映射，Spring Data JPA 会自动将查询结果映射到 `AuthorityMenuOperation` 对象。

*   **场景二：跨表关联查询的实现**
    *   **描述**：讲师在 IDEA 中演示了如何通过 `@Query` 注解编写 HQL 语句来实现跨表查询。他首先定义了查询的两个实体 `AuthorityMenuOperation` 和 `AuthorityRoleOperation`，然后通过 `where` 子句设置关联条件。
    *   **技术点**：展示了如何使用 `?1` 占位符来接收方法参数 `roleId`，并说明了 HQL 语句的语法结构。

*   **场景三：Swagger2 文档集成预告**
    *   **描述**：在讲解完 HQL 查询后，讲师在 Typora 中切换到“3.8 Spring Data Rest 高级用法（拓展）”章节，并提到接下来会讲解如何集成 Swagger2。
    *   **技术点**：预告了后续内容，即如何通过 `@ApiImplicitParams` 和 `@ApiOperation` 注解为接口生成 Swagger2 文档，方便前端调用和接口测试。

*   **场景四：IDEA 中的代码补全与编辑**
    *   **描述**：讲师在 IDEA 中对 `AuthorityMenuRepository` 接口进行编辑，通过鼠标悬停和快捷键（如 `Ctrl+Shift+Space`）触发代码补全，展示了 `@Query` 注解的使用和 HQL 语句的编写过程。
    *   **技术点**：演示了 IDE 的智能提示功能，帮助开发者快速编写和调试代码。

---

以上是根据视频画面进行的结构化技术课程分析，涵盖了视频的主要内容、技术要点和演示过程。
