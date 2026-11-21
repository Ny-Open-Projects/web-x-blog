# 19-权限业务接口-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对第二章内容做个回顾和总结

首先我们来看一下第二章的学习目标

在这里我们要去完成权限模块对应的业务接口

从编码上面做具体的实现

我们回顾一下整体的实现讲解步骤是怎样的

首先咱们讲解了核心的接口列表

权限模块所设计的接口点会比较多

在这里我们只是实现了比较重要的核心的权限功能接口

接着咱们讲解了技术这块的具体实现

咱们是采用了SplitData REST以及SplitBoot

两套不同技术去实现对外服务接口

这两套接口具有互补的作用

同时咱们可以掌握更多的技术点

接着咱们要去创建对应的表结构

初始化对应的权限数据

便于下面对整个功能的测试和验证

我们的具体实现先创建对应的实体

接着的话

我们要去创建数据层相关的接口

这里面是包括八个权限模块所设计到的实体

接着的话咱们就要去搭建后台管理服务工程

然后添加对应的依赖

这个依赖的话

咱们是要侧重了解SplitData REST

以及JPA对应的依赖

还有SWOG2

在上面都有对应的注释和说明

JPA

然后SplitData REST

JPA的主线依赖

再往下面

我们从用户的数据层接口做了对应的实现

它要去继承分页和排序的接口

以及JPA的规格接口

按照这种实现方式

咱们也要将其余的六个实体做对应的实现

然后要去编写它的启动类

这样就完成了后台管理工程的搭建配置

接下来就是咱们本章学习的重点

要去实现了全线核心的逻辑接口

这块核心的逻辑接口

设计到的逻辑比较复杂

在这里通过SplitData REST不方便处理

所以我们要去再包装一层

通过自定义接口的形式

在service层做封装

然后以SplitBoot接口的形式提供出去

首先咱们可以看到保存角色全线接口的代码实现

在这里咱们也做了一个详细的讲解

然后的话是下面的分配用户和角色关联关系的接口

这块的代码具体

实现大家也要了解清楚

在整个讲义的内容当中都做了具体的说明

再往下面就是根据角色ID去查找对应的菜单操作信息接口

这个是前端做全线处理所需要用到的接口信息

然后还有角色ID查找对应的菜单信息接口

这两个接口都是通过SplitData REST的形式提供出来的

然后他们是采用了HQAdWord的面向对象的

查询语句做的实现

因为在这里会涉及到表的关联查询

那咱们也是以此为例给大家做了一个讲解和介绍

在实际的业务项目当中可能都会需要使用它

最后咱们是讲解了SplitData REST的高级用法

也是对这块知识进行了一个拓展

提升了大家对SplitData REST的组件的运用

那么在这里会涉及到SplitData REST的冗余查询的实现

然后SplitData REST的返回ID数据的配置和实现

最后就是SplitData REST和QueryDSL的插件集成

QueryDSL插件能够极大的帮助咱们去简化查询实现

可以快速实现了高级查询的条件接口

在这里咱们也对它做了详细的详解

并且通过菜单管理接口做了一个测试和验证

最后咱们再来总结一下

全线模块所设计的功能接口会比较多

在这里咱们只是测重和讲解了全线分配管理所设计到的核心接口

还有很多的接口在这里就不做一一律举

因为的话会占用较多的时间

我们可以通过SplitData REST的快速帮助咱们去实现增伤改查等基本信息接口

对于复杂逻辑的接口可以通过SplitBoot进行实现

通过service层再做一个包装处理

这一章咱们最主要的要掌握了这个组件的实现设计的时间

也就是说全线核心接口的实现

用户角色和菜单的逻辑处理

理解整个全线的分配和处理机制

这一讲就是对DL内容的回顾和总结

那这一讲咱们就讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于“权限模块业务接口实现”的技术讲解，主要聚焦于使用 Spring Data Rest 与 Spring Boot 框架构建后台管理系统的权限功能。课程内容从宏观的模块划分（角色、用户）开始，逐步深入到具体的接口设计、实体类创建、以及核心逻辑的实现。重点讲解了如何通过 Spring Data Rest 快速实现 CRUD 接口，并针对复杂的权限分配逻辑（如角色与权限、用户与角色的关联）进行了详细演示。课程还涉及了 HQL 自定义查询、级联映射以及 Swagger2 的集成，旨在帮助开发者掌握权限模块的核心实现方法。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:30**：课程总览与目标设定。介绍本章将讲解“权限模块业务接口实现”，并列出主要章节：接口列表、技术实现说明、创建表结构、初始化数据、创建实体、创建后台管理工程、权限核心逻辑接口实现。
*   **00:30 - 01:00**：模块划分与接口概览。详细列出“角色模块”和“用户模块”的具体接口，包括增删改查、权限分配、角色查询、用户查询等。
*   **01:00 - 01:30**：技术实现说明。介绍采用 Spring Data Rest 与 Spring Boot 实现对外服务接口，并说明其分页、排序、动态查询等能力。
*   **01:30 - 02:00**：创建实体与基础类。展示 `BaseEntity` 类的定义，包括 `@MappedSuperclass`、`@Id`、`@GeneratedValue` 等注解，以及所有实体类需要继承此基类。
*   **02:00 - 02:30**：创建后台管理工程。展示 `pom.xml` 文件中的依赖配置，包括 Spring Boot Web、Spring Data JPA、Spring Data Rest 和 Jackson。
*   **02:30 - 03:00**：接口定义与 Repository。展示 `AuthorityUserRepository`、`AuthorityRoleRepository` 等六个 Repository 接口的定义，并说明其继承关系。
*   **03:00 - 03:30**：权限核心逻辑接口实现。演示 `savePrivileges` 方法，用于保存角色与权限的关联关系，并处理角色不存在的异常。
*   **03:30 - 04:00**：用户分配角色逻辑。演示 `userAssignRoles` 方法，用于查询用户已分配的角色，并校验用户是否已存在相同机构类型的角色。
*   **04:00 - 04:30**：根据角色ID查询菜单信息。展示 `AuthorityMenuOperationRepository` 接口的定义，以及其中的 `findByRoleId` 方法，使用 HQL 语句实现跨表查询。
*   **04:30 - 05:00**：Spring Data Rest 高级用法。讲解如何通过级联映射实现菜单父级信息的查询，并展示 `AuthorityMenu` 实体类的定义。
*   **05:00 - 05:30**：自定义查询与绑定。演示如何通过 `QuerydslBindings` 自定义 `AuthorityMenu` 实体的查询条件，如模糊查询和忽略大小写。
*   **05:30 - 06:00**：总结。回顾本章核心内容，强调通过 Spring Data Rest 快速实现接口，并掌握用户、角色、菜单的逻辑处理。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **章节结构**：清晰列出了“权限模块业务接口实现”的各个子章节，如“接口列表”、“技术实现说明”、“创建实体”等。
    *   **模块接口列表**：
        *   **角色管理**：增、改、查（支持分页），角色与权限分配接口，根据角色查询权限接口。
        *   **用户管理**：增、改、查（支持分页），重置密码接口，根据用户查找分配角色接口。
    *   **技术实现说明**：明确指出采用 Spring Data Rest 与 Spring Boot 实现接口，支持分页、排序、动态查询。
    *   **总结**：强调了权限模块的核心接口，以及 Spring Data Rest 和 Spring Boot 在实现中的作用。

*   **代码关键内容**：
    *   **`BaseEntity` 类**：
        ```java
        @MappedSuperclass
        public class BaseEntity implements Serializable {
            @Id
            @GeneratedValue(strategy = GenerationType.IDENTITY)
            private Long id;
            public Long getId() { return id; }
            public void setId(Long id) { this.id = id; }
        }
        ```
        *   说明：所有实体类必须继承此基类，实现 `Serializable` 接口，并使用 `@Id` 和 `@GeneratedValue` 注解定义主键。
    *   **`pom.xml` 依赖配置**：
        ```xml
        <!-- Spring Boot 依赖 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!-- Spring Data JPA 依赖 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <!-- Spring Data Rest 实现组件 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-rest</artifactId>
        </dependency>
        <!-- 增加 Jackson 的 Hibernate 类型支持 -->
        <dependency>
            <groupId>com.fasterxml.jackson.datatype</groupId>
            <artifactId>jackson-datatype-hibernate5</artifactId>
        </dependency>
        ```
    *   **`AuthorityMenuOperationRepository` 接口**：
        ```java
        @RepositoryRestResource(path = "/authorityMenuOperation")
        public interface AuthorityMenuOperationRepository extends
            PagingAndSortingRepository<AuthorityMenuOperation, Long>,
            JpaSpecificationExecutor<AuthorityMenuOperation> {
            @ApiOperation(value = "根据角色ID查找对应的菜单操作信息")
            @ApiImplicitParams({
                @ApiImplicitParam(value = "角色ID", name = "roleId", dataType = "string", required = true)
            })
            @Query("select menuOpt from AuthorityMenuOperation menuOpt, AuthorityRoleOperation roleOpt " +
                "where roleOpt.roleId = ?1 and menuOpt.status = 1 and roleOpt.operationId = menuOpt.id")
            public List<AuthorityMenuOperation> findByRoleId(@Param("roleId") Long roleId);
        }
        ```
        *   说明：使用 `@RepositoryRestResource` 注解定义 REST 接口，使用 `@Query` 注解定义 HQL 查询语句，实现跨表查询。
    *   **`AuthorityMenu` 实体类**：
        ```java
        @Entity
        @Table(name = "t_authority_menu")
        @Data
        public class AuthorityMenu extends BaseEntity {
            @ManyToOne(fetch = FetchType.EAGER)
            @JoinColumn(name = "parentId", referencedColumnName = "id")
            @Insertable(false)
            @Updatable(false)
            private ParentAuthorityMenuVo parentAuthorityMenu;
        }
        ```
        *   说明：定义了菜单实体，并通过 `@ManyToOne` 注解与父级菜单关联，使用 `@Insertable(false)` 和 `@Updatable(false)` 注解防止在插入或更新时自动处理该字段。
    *   **`QuerydslBindings` 自定义查询**：
        ```java
        @Override
        default public void customize(QuerydslBindings bindings, QAuthorityMenu menu) {
            bindings.bind(menu.menuName).first(StringExpression::contains);
            bindings.bind(menu.menuCode).first(StringExpression::equalsIgnoreCase);
        }
        ```
        *   说明：通过 `QuerydslBindings` 自定义 `AuthorityMenu` 实体的查询条件，支持模糊查询和忽略大小写。

---

### 4) 关键场景与演示描述

*   **场景一：权限模块接口概览**（00:30）
    *   **描述**：讲师在 PPT 上展示“角色模块”和“用户模块”的接口列表，清晰地列出了每个模块需要实现的接口，如“角色与权限分配接口”、“根据用户查找分配角色接口”等，为后续开发提供明确的指导。

*   **场景二：实体类设计与继承**（01:30）
    *   **描述**：讲师在代码编辑器中展示 `BaseEntity` 类的定义，强调所有实体类必须继承此基类，并使用 `@MappedSuperclass` 注解。通过高亮显示 `@Id` 和 `@GeneratedValue` 注解，说明了主键的定义方式。

*   **场景三：HQL 自定义查询**（04:00）
    *   **描述**：讲师在代码编辑器中展示 `AuthorityMenuOperationRepository` 接口的定义，重点讲解 `@Query` 注解的使用。通过
