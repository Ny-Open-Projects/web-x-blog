# 16-权限业务接口-Spring data Rest 冗余查询 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对Splendid REST的高级用法

做一个拓展和延伸

让大家今后在一些复杂的业务场景下面

知道该怎么去处理和实现

首先咱们来看一下

Splendid REST的冗余查询的实现

我们看一下它的一个背景

如果菜单要显示副菜单的编号

以及它对应的名称

我们这个时候该怎么去实现呢

这样它就会用到关联的查询

咱们知道菜单和副菜单

都是保存在菜单表当中

它们是通过Parent ID做映射和关联的

我们可以再去定义一个接口

然后再去封装一个返回对象

这样是可以实现的

但是会比较麻烦

对不对

这样又要增加额外的代码量

Splendid REST它能否支持

它是可以支持的

具体化就是采用极点映射方式进行处理

这个就类似于HiveNet的

一对多多对多等极点方式的处理

咱们看一下具体的实现该怎么去做呢

要做极点映射

就要再创建一个新的无忧对象

不能存在Splendid REST的映射之中

否则返回的对象会自动转换成REST的地址

就如下所示

咱们往下面看它的返回信息

这里可以看到Parent Authentic Menu

就是它的副菜单信息

它将它的副菜单信息也作为一个支援

返回给了客户端

那么这个其实并不是咱们希望暴露出来的接口

对不对

那怎么办呢

我们就需要去新定义一个VU

让Splendid REST找不到匹配的路径接口

那么它就会自动转换成为阶层对象

这个就是请求后的结果

咱们可以看一下

Parent Authentic Menu

它作为阶层对象

将这个信息转换成阶层对象

返回出来了

对不对

里面就可以包含咱们所需要的

像副菜单的编号

副菜单的名称

那下面就没有副菜单的操作地址信息

好

这点大家要明白清楚

因为在JPA的数据层接口当中

咱们任何的接口

它都会有一个什么

对象的注入

关联一个对象

像这个菜单数据层接口

它就会关联菜单的对象

那么如果咱们

不定义一个新的VU

它就会拿到这个对象

当作一个资源提供出来

就不会将它转换为JSON的数据信息

咱们在这个数据包含当中

可以看到

对不对

在这里面的话

是不能显示副菜单的编号

副菜单的名称

那所以我们就需要定义一个新的VU

这样新的VU和它

就不会产生任何的关联关系

也就不会进行对应的地址映射

好

这点明白之后

咱们就从代码层面

对集点映射方式

再做一个具体的讲解

打开autolink menu这个实体

我们看一下它怎么去配置

菜单和副菜单

是一个什么关系

是多对一的关系

所以咱们在这里

采用的是一个menu2one的注解

fagtype是一个一个

并非懒加载

有两种方式

一个是懒加载

就是在用到的时候再去加载处理

一个的话就是比较主动的方式

对不对

初始化的时候就会进行对应的加载处理

下面是NodeFounder

这个注解建议大家要加上去

如果是不加会出现什么问题

当它集点关系找不到匹配的数据时候

就是为闹

它就会抛出一个NodeFounder的异常信息提示

会影响咱们正常业务流程的处理

所以如果咱们没有这种特殊要求

不想阻塞业务的实现

如果没找到

就返回对应的空数据就可以了

不需要去抛出异常

咱们就加上这个注解

如果你需要抛出异常

这个注解可以将它去掉

下面就是比较重要的

它如何去集点和映射对应的数据

就是通过这个注解

上面这个注解是标注为多对一的关联关系

那么具体是怎么去映射

跟哪个列哪个属性去关联

这里就会有一个

就是做了一个具体定义

比如说你的复集菜单的ID

它就通过Parrot的ID去作为关联

那么它要关联什么

关联对应的复集菜单数据的ID

这样就形成了一个映射关系

那么在保存和修改的时候

这部分数据咱们是不需要让它急连去改动的

所以咱们在这里insertable

还有updateable全部将它关闭

就是防止在咱们对菜单数据

进行操作和修改的时候

它会产生急连的数据同时被修改的问题

好这个是Mini2One的一个急连映射的配置

那么1-2-Mini该怎么去配置呢

咱们再找一个实体来举例作为讲解

这个是AuthenticUser

在这下面咱们可以看到

一个User下面会关联多个角色

对不对

所以用户和角色

它就可以采用1-2-Mini的一个配置

那么咱们可以看到

它所对应的实体就是新定义的vivo

AuthenticUserNodeVivo

然后是它的GDN配置关系

在这里面的话采用2

对应的话就是所有的操作类型

开局Type仍然是采用1个

下面就是刚才所讲的注解

基本上都是一样的

然后这个是JoinClient

它们的列属性的映射配置

这个是通过AuthenticUserNode表的UserX

和User表里面的ID进行的关联

好

这个就是一对多的配置处理

这一讲就是对SplintDataList

冗余查询实现的配置

做了具体的讲解和介绍

那这讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于 **Spring Data REST** 的高级用法，具体聚焦于如何实现 **“级联查询”**（或称“嵌套查询”）。讲师通过一个“权限菜单”（`AuthorityMenu`）实体的示例，说明了当需要在返回的菜单对象中包含其父菜单的信息时，Spring Data REST 默认不支持直接返回关联对象。为了解决这个问题，讲师提出并演示了使用 **“级联映射”** 的方案：即定义一个独立的 **VO（Value Object，值对象）** 来承载父菜单的数据，然后在实体类中使用 `@ManyToOne` 和 `@JoinColumn` 映射关系。这样，当 Spring Data REST 无法找到对应的 REST 路径时，它会自动将该 VO 对象转换为一个 JSON 对象，并包含指向父菜单的 `href` 链接，从而实现“级联”效果。视频中还展示了相关的 Java 代码、数据库表结构以及最终返回的 JSON 数据结构。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各帧的时间戳，以下章节是根据画面内容和逻辑顺序进行的结构化梳理：

*   **00:00 - 00:05**: **章节标题与问题引入**。画面显示标题“3.8 Spring Data Rest 高级用法（拓展）”，并提出核心问题：“如果菜单要显示父菜单的编号和名称，该如何实现？”。讲师指出，直接定义接口和返回对象比较麻烦，但可以考虑采用“级联映射”方式。
*   **00:05 - 00:15**: **实体类设计与级联映射**。讲师展示 `AuthorityMenu` 实体类的代码，其中使用 `@ManyToOne(fetch = FetchType.EAGER)` 和 `@JoinColumn` 映射父菜单关系，并定义了一个私有属性 `private ParentAuthorityMenuVo parentAuthorityMenu;`。
*   **00:15 - 00:25**: **VO 对象的必要性与自动转换**。讲师强调，必须定义一个新的 VO 对象（`ParentAuthorityMenuVo`），并且该 VO 不能存在于 Spring Data REST 的默认映射中。否则，Spring Data REST 会自动将该 VO 转换为一个 JSON 对象，并包含 `href` 链接。
*   **00:25 - 00:35**: **JSON 响应结构演示**。讲师展示了最终返回的 JSON 数据结构，其中包含了父菜单的 `parentId`、`menuName` 等信息，并通过 `parentAuthorityMenu` 字段包含一个 `href` 链接，指向父菜单的 REST 路径。
*   **00:35 - 00:45**: **代码实现与调试**。讲师切换到 IDE，展示了 `AuthorityMenuRepository` 接口的代码，其中包含了 `@RepositoryRestResource` 注解和 `customizeQuerydslBindings` 方法，用于自定义查询条件。
*   **00:45 - 00:55**: **数据结构与关联关系**。讲师展示了 `AuthorityUser` 实体类的代码，其中定义了 `@OneToMany` 关联 `AuthorityUserRoleVo`，并使用 `@JoinColumn` 映射 `userId`。
*   **00:55 - 01:05**: **总结与关键点回顾**。讲师再次强调了“级联映射”的核心思想：通过定义 VO 对象和使用 `@ManyToOne` 映射，可以实现 Spring Data REST 中的“级联”效果。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文本内容**:
    *   标题：“3.8 Spring Data Rest 高级用法（拓展）”。
    *   核心问题：“如果菜单要显示父菜单的编号和名称，该如何实现？我们再定义接口和返回对象是可以实现，但比较麻烦，spring data rest 能否支持？可以采用级联映射方式处理。”
    *   关键提示：“注意，此时我们要定义一个新的VO对象，不能存在Spring Data Rest的映射之中，否则返回的对象，会自动转换成rest地址”。

*   **代码关键内容**:

    *   **实体类 `AuthorityMenu`**:
        ```java
        @Entity
        @Table(name="t_authority_menu")
        @Data
        public class AuthorityMenu extends BaseEntity {
            ...
            @ManyToOne(fetch = FetchType.EAGER)
            @JoinColumn(name = "parentId", referencedColumnName="id",
                insertable = false, updatable = false)
            private ParentAuthorityMenuVo parentAuthorityMenu;
        }
        ```

    *   **VO 对象 `ParentAuthorityMenuVo`** (虽然未直接展示，但其存在是关键)。
        ```json
        {
            "parentId": 1,
            "institutionTypeId": "COMPANY",
            "menuCode": "SysAdmin",
            "menuName": "用户管理",
            "menuUri": "/sys/admin",
            "menuLevel": 0,
            "operationSecurity": 1,
            "menuIco": "table",
            "status": 1,
            "isopen": 0,
            "isshow": 1,
            "componentSrc": "/sysAdmin/index",
            "parentAuthorityMenu": {
                "href": "http://127.0.0.1:10691/admin/authorityMenu/2/parentAuthorityMenu"
            },
            "_links": {
                "self": {
                    "href": "http://127.0.0.1:10691/admin/authorityMenu/2"
                },
                "authorityMenu": {
                    "href": "http://127.0.0.1:10691/admin/authorityMenu/2"
                }
            }
        }
        ```

    *   **Repository 接口 `AuthorityMenuRepository`**:
        ```java
        @RepositoryRestResource(path = "/authorityMenu")
        public interface AuthorityMenuRepository extends QuerydslPredicateExecutor<AuthorityMenu>, PagingAndSortingRepository<AuthorityMenu, Long>, JpaRepository<AuthorityMenu, Long> {
            @Override
            default public void customizeQuerydslBindings(bindings, AuthorityMenu menu) {
                bindings.bind(menu.menuName).first(StringExpression::contains); // 模糊查询
                bindings.bind(menu.menuCode).first(StringExpression::equalsIgnoreCase); // 忽略大小写
            }
        }
        ```

    *   **`FetchType` 枚举**:
        ```java
        public enum FetchType {
            LAZY,
            EAGER;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：问题提出与方案选择 (00:00-00:05)**
    *   讲师在 PPT 上展示标题“3.8 Spring Data Rest 高级用法（拓展）”，并提出一个实际开发中常见的需求：在菜单列表中显示父菜单的编号和名称。
    *   讲师分析了两种方案：一是直接定义接口和返回对象，但认为“比较麻烦”；二是采用“级联映射”方式，认为这是“可以支持”的方案。

*   **场景二：实体类设计与级联映射 (00:05-00:15)**
    *   讲师在 IDE 中展示 `AuthorityMenu` 实体类的代码。
    *   重点演示了 `@ManyToOne` 注解的使用，其中 `fetch = FetchType.EAGER` 表示立即加载关联对象。
    *   通过 `@JoinColumn` 注解，将 `parentId` 字段与数据库中的 `id` 字段关联。
    *   讲师强调，为了实现级联效果，需要在实体类中定义一个私有属性 `parentAuthorityMenu`，其类型为 `ParentAuthorityMenuVo`。

*   **场景三：VO 对象的必要性与自动转换 (00:15-00:25)**
    *   讲师在 PPT 上强调：“注意，此时我们要定义一个新的VO对象，不能存在Spring Data Rest的映射之中”。
    *   讲师解释，如果 VO 对象存在于 Spring Data REST 的默认映射中，系统会尝试将其转换为 REST 路径，这会导致错误。
    *   讲师指出，Spring Data REST 会自动将该 VO 对象转换为一个 JSON 对象，并包含 `href` 链接。

*   **场景四：JSON 响应结构演示 (00:25-00:35)**
    *   讲师在 PPT 上展示最终返回的 JSON 数据结构。
    *   该结构包含父菜单的详细信息（如 `parentId`, `menuName` 等），并通过 `parentAuthorityMenu` 字段包含一个 `href` 链接。
    *   该 `href` 链接指向父菜单的 REST 路径，实现了“级联”效果。

*   **场景五：代码实现与调试 (00:35-00:45)**
    *   讲师切换
