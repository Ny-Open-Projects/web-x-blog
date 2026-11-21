# 10-权限业务接口-实体创建 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着去创建对应的表结构以及相关的实体

首先咱们要导入已经整理的Circle

这个在资料当中已经提供出来

咱们将ChadstockCircle这个脚本文件导入到数据库当中

让它创建T-Ausley开头的相关的表

创建完成表之后咱们要初始化对应的数据

为了便于查询等相关的一些功能验证

咱们会初始化一定的数据

那么直接导入已经整理的Circle

也是Chadstock这个文件

只要导入进去之后

它不仅会初始化对应的表结构

还会创建一些数据

咱们可以随便打开一张T-Ausley Menu这张表

在这里如果是可以看到对应的菜单数据

那么说明整个脚本的话

执行导入都是OK的

好,接着咱们就要去创建对应的实体

那么这个实体

我们可以通过MyBedisGenerate的工程去生成

但是呢

每个实体我们还做些调整和修改

要加上GPA相关的注解

以及后面咱们SWG2集成使用的时候

要用到的相关注解

就是生成了文档的描述和说明

咱们将权限相关的八个实体创建好之后

就是放在咱们的Stock Entity的工程下面

在这里

我已经将这些代码放置了Stock Entity工程下面

咱们可以看一下Ausley开头这些表

这个是Menu表

那么我们可以看到它报错了

对不对

这个为什么报错了

因为在这里用到了SWG2相关的注解

我们要给这些实体加上对应的文档说明

那么我们也要在PoM下面去增加对应的依赖

这个依赖

我们把SWG2的依赖加上去就可以了

好

这里Copy进去

只要添加一个依赖就可以了

这个就是SWG2相关的依赖说明

这个是它的版本SWGVoLCH

我们将这个数据加进去

然后它的属性加入到复集工程当中

把它放在Properties表现下面

这个版本我们就选用2.9.2

回到代码当中

我们让它导入真相

Conclude

看一下能不能找到

依赖的话已经找到

我们再回到实体当中

那么就没有再报错了

对不对

如果是我们要在实体上面增加注解说明

我们要采用API的这个注解

然后在Value上面给它具体的描述就可以

我们可以看到每个实体上面

我们都给加了一个API注解

对不对

因为在黑图OS接口当中

我们要提供相关的操作说明

所以我们要把这个注释加入进去

然后接着的话可以看到

是JPA相关的注解

这个是它的映射N体

然后是它映射所对应的表明

这个Data是Longboard的注解

它会帮我们生成Get和Set的方法

我们可以看到BaseN体下面

BaseN体是我们的主体

N体是这些所有实体的附类

那么它在这里封装了供应的属性

就比如说ID

然后这个是ID的生成策略

这个是唯一标识

上面这个Map的Superclass代表它是一个附类

大家要将这八个实体

1 2 3 4 5 6 7 8

OS里开头的这八个实体

创建到咱们的StockN体工程下面

要加上对应的注解说明

好检查OK

没有问题之后

接下来咱们就可以从接口上面做具体的代码实现

咱们可以看到这两个实体当中

还有一个API Model的注解对不对

这个Model的注解是什么意思

API Model是用于返回对象的描述说明

API的话

一般是用于接口的描述说明

咱们在这里是一个实体对不对

因为这个是采用Servin DataList的HitOS的高阶形态

所以提供的数据层接口

它就能够实现对外的一个访问

这个实现起来

相比之前的SplitBoot的接口来讲的话

少了Conclude层

也不需要Service层

可以直接通过JPA

就是数据层去提供对应的接口

这个在下面章节当中

咱们去实现的时候

还会做一个讲解和说明

好

那在这里就对全线相关实体的创建

以及表结构数据的导入和创建

那这一讲

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个基于 Spring Boot 的权限管理系统开发教程的第 3 章“Swagger2集成使用”中的“技术实现说明”部分。讲师正在演示如何通过 MyBatis-Generator 工具自动生成数据库表对应的 Java 实体类（Entity），并为这些实体类添加 Swagger2 注解以实现 API 文档自动生成。视频重点展示了如何创建与权限相关的 8 个核心实体类（如 `AuthorityMenu`, `AuthorityUserRole` 等），并为它们添加 `@Api`, `@Entity`, `@Table` 等注解。同时，讲师也讲解了 `BaseEntity` 基础类的定义，以及如何在 `pom.xml` 中配置 Swagger2 依赖。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开始，展示课程大纲，当前位于“3.5 创建实体”章节。
*   **00:00:05 - 00:00:15**: 展示数据库表 `t_authority_menu` 的数据，用于验证初始化数据。
*   **00:00:15 - 00:00:30**: 在 IDE 中展示项目结构，突出显示需要创建的 8 个实体类。
*   **00:00:30 - 00:00:45**: 编辑 `AuthorityMenu.java` 文件，添加 `@Api` 和 `@Entity` 注解。
*   **00:00:45 - 00:01:00**: 展示 `BaseEntity` 类的定义，强调其作为所有实体的基类。
*   **00:01:00 - 00:01:15**: 编辑 `pom.xml` 文件，添加 Swagger2 依赖。
*   **00:01:15 - 00:01:30**: 编辑 `AuthorityMenuOperation.java` 文件，添加 `@Entity` 和 `@Table` 注解。
*   **00:01:30 - 00:01:45**: 编辑 `AuthorityUserRole.java` 文件，添加 `@ApiModel` 和 `@ApiModelProperty` 注解。
*   **00:01:45 - 00:02:00**: 总结本节内容，强调实体类的创建和注解的添加。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.5 创建实体”。
    *   **关键文字**: “将权限相关的8个实体创建好: AuthorityMenu, AuthorityMenuOperation, AuthorityNoLimitUri, AuthorityRole, AuthorityRoleMenu, AuthorityRoleOperation, AuthorityUser, AuthorityUserRole。”
    *   **关键文字**: “BaseEntity基础实体类: `@MappedSuperclass public class BaseEntity implements Serializable { @Id @GeneratedValue(strategy = GenerationType.IDENTITY) private Long id; }`”。
    *   **关键文字**: “stock-entity的POM依赖: `<!-- swagger2 依赖 --> <dependency> ... </dependency>`”。

*   **代码示例**:
    *   **`AuthorityMenu.java`**:
        ```java
        @Api(value = "HATEOAS接口--菜单管理(AuthorityMenu)")
        @Entity
        @Table(name = "t_authority_menu")
        public class AuthorityMenu extends BaseEntity {
            private static final long serialVersionUID = -1L;
        }
        ```
    *   **`BaseEntity.java`**:
        ```java
        @MappedSuperclass
        public class BaseEntity implements Serializable {
            @Id
            @GeneratedValue(strategy = GenerationType.IDENTITY)
            private Long id;
        }
        ```
    *   **`pom.xml` (Swagger2 依赖)**:
        ```xml
        <!-- swagger2 依赖 -->
        <dependency>
            <groupId>io.springfox</groupId>
            <artifactId>springfox-swagger2</artifactId>
            <version>${swagger.version}</version>
        </dependency>
        ```
    *   **`AuthorityMenuOperation.java`**:
        ```java
        @Api(value = "HATEOAS接口--菜单操作管理(AuthorityMenuOperation)")
        @Entity
        @Table(name = "t_authority_menu_operation")
        public class AuthorityMenuOperation extends BaseEntity {
            // 自定义菜单id
        }
        ```
    *   **`AuthorityUserRole.java`**:
        ```java
        @Api(value = "HATEOAS接口--用户与角色关联管理(AuthorityUserRole)")
        @Entity
        @Table(name = "t_authority_user_role")
        @ApiModel("AuthorityUserRole(用户与角色关联表)")
        public class AuthorityUserRole extends BaseEntity {
            @ApiModelProperty(value = "用户ID", example = "1")
            private Long userId;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：数据库数据验证 (00:00:05)**
    *   **描述**: 讲师在 Navicat Premium 数据库管理工具中打开 `t_authority_menu` 表，展示其数据内容，以验证之前导入的初始化数据是否成功。

*   **场景二：实体类创建与注解 (00:00:30 - 00:01:45)**
    *   **描述**: 讲师在 IntelliJ IDEA 中，依次打开并编辑 `AuthorityMenu.java`, `AuthorityMenuOperation.java`, `AuthorityUserRole.java` 等文件。
    *   **操作**: 在每个实体类的顶部添加 `@Api` 注解用于 Swagger2 文档描述，添加 `@Entity` 注解用于 JPA 映射，添加 `@Table` 注解指定对应的数据库表名。
    *   **操作**: 在 `AuthorityUserRole.java` 中，使用 `@ApiModel` 和 `@ApiModelProperty` 注解来为实体类添加模型描述和字段注释，以便在 Swagger2 文档中更清晰地展示。

*   **场景三：基础实体类与依赖配置 (00:00:45 - 00:01:15)**
    *   **描述**: 讲师在 PPT 上展示了 `BaseEntity` 的定义，强调其作为所有实体类的基类，包含 `@MappedSuperclass` 注解和 `@Id`、`@GeneratedValue` 注解。
    *   **操作**: 在 `pom.xml` 文件中，讲师添加了 Swagger2 的 Maven 依赖，并将版本号 `${swagger.version}` 设置为占位符，以便后续统一管理。

*   **场景四：项目结构与文件管理 (00:00:15 - 00:00:30)**
    *   **描述**: 讲师在 IDE 中展示了项目结构，通过鼠标选中并高亮显示了需要创建的 8 个实体类，为后续的代码编写做准备。
