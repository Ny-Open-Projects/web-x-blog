# 18-权限业务接口-Spring Data Rest与queryDS — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们来讲解SplitDataList的以及QueryDSL的集成去实现了高级的查询。

在查询使用过程当中,我们经常会遇到各种查询条件或者是举择查询。

如果是针对每个条件都去新增一个接口,实现起来会非常麻烦。

这个是一个查询的失利。

这个接口地址是去查询账户预警通知模板信息。

咱们可以看到,在这里默认是提供可以支持分页的查询,以及排序的查询处理。

但是在这后面,它并不支持自定义的条件查询。

比如说这个预警模板里面,咱们想根据它的内容或者标题做一个过滤查询,这个是无法支持的。

那么如果咱们有这种需要,

是不是还得再去看一看?

那再去开一个接口就会比较麻烦,对不对?

咱们来看一下有没有比较好的方法能够去实现呢?

这个时候就可以采用咱们之前所提过的QueryDSL的这个主线,去帮助咱们快速实现。

QueryDSL会根据咱们在SplitDataRest中定义的实体,然后生成用于查询的类,会重新生成一个类,它会以Q开头。

我们在对应的LibSyto类当中去进行。

我们在这些数据中,我们可以分析到一个多个数据的缺点。

那么我们可以透过这些数据去进行高级的查询。

这样就能支持这个实体当中任意的属性去实现它的条件查询。

不管是单个属性还是多个属性都可以进行支持。

QueryDSL还包含比较丰富的功能,比如像模糊查询、时间范围查询,在下面我们可以看到它对应的实践。

咱们只要将这个规则配置到。

代码当中就可以了

这个呢

就是实践段查询的具体规则配置

上面呢

就是模糊查询的设定

还有比较丰富的条件配置

比如说忽略大小写等等

大家有兴趣呢

可以再去拓展研究

在这里呢

我们以Authry Menu Libsitly

作为实例进行讲解

咱们找到Authry Menu Libsitly

这个数据层接口

我们可以看到

它这一块的具体代码配置实现

首先要去继承Query DSL的接口

这里面呢

有两个接口

因为呢

咱们要实现自定义的查询规则配置

那下面呢

就要去重写对应的方法

这里面就是具体的配置规则

比如说模糊查询

忽略大小写的配置

这两段配置呢

它的意思就是说

菜单名称

它要支持模糊查询

菜单的编号呢

它是要支持完全匹配

但是呢

可以忽略大小写

我们可以看到它的参数呢

是以Q开头的Authry Menu的生成的实体信息

这一块的生成配置呢

咱们之前也做了介绍

它是在SpaStalk N体工程下面

要增加对应的Query DSL的编译查写

这里面呢

是它构建时候所需要用到的查写信息

上面呢

是Query DSL的查写依赖信息

如果咱们新加了数据层

或者是对数据层查询条件做了调整

或者是新增了一些查询属性

那么呢

我们要去重新生成Query DSL的映射实体

可以呢

在Maven试图上面去找到呢

SpaStalk N体

然后呢

重新去clean打包

好

大家要注意就是对实体的条件修改

无论你是新增还是删除

或者是调整它的属性名称

或者是新加了的数据属性

我们可以在这里呢

我们可以在这里呢

加了实体

不要忘记呢

去重新呢

通过Query DSL插件呢

构建整个实体工程

生成了最新的映射代码

那咱们呢

再回到讲义当中来看一下

具体的调用实现呢

可以通过Postman

在上面呢

去验证整个结果

那为了大家更直观的去了解

Query DSL插件的功能呢

咱们就来给大家做一个演示

咱们首先呢

启动SpaStalk Admin User图工程

找到它的启动内

右键乱运行

观察它的启动输出日志

确保呢

服务是正常启动

好

服务呢

启动完成

端口是10691

接着的话呢

咱们就来做一个测试验证

就以全线菜单为例

进行测试讲解

咱们首先直接发出一个请求

在这里可以看到

全线菜单的所有数据信息

我们系统当中的

所有的菜单数据呢

在这里呢

都可以通过接口返回出来

然后呢

之前咱们所讲的

SpringData冗余查询呢

在这里呢

也可以实现

对不对

将它的副菜单信息呢

都全部呈现出来

那咱们的重点呢

是来去验证了

这个条件查询能否正常生效

如果是不加QualityDSL的话呢

你后面跟任何的查询条件呢

都是无法生效的

那现在呢

咱们就来做一个测试

以Menu URI属性作为条件来查询

后面的话呢

跟咱们普通参数传递是一样的

那我们看一下它的一个运行结果

查询完成之后呢

可以看到在这里呢

它就返回了一条业务数据

对不对

这个业务数据的话呢

它的Menu URI也是-SYS

这条数据Menu URI呢

跟这个呢是匹配

这条数据的Menu URI呢

咱们可以看到是匹配正确的

对不对

这样呢

咱们就实现了QualityDSL的条件

如果说你还想根据其他条件呢

这个呢都可以在后面进行拼接

比如说Menu Name

好

在这里呢

就是对Supreme Data REST和QualityDSL

集成实现高级查询的配置讲解

那这讲呢

咱们先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于 **Spring Data REST 与 QueryDSL 集成** 的技术教程，旨在解决在 RESTful API 开发中，为应对复杂的查询条件（如模糊查询、精确匹配、时间范围查询等）而频繁创建多个接口的繁琐问题。讲师通过一个名为 `stock-admin-user` 的项目，演示了如何通过引入 QueryDSL 依赖，并在 Repository 接口中继承 QueryDSL 提供的接口（如 `QuerydslPredicateExecutor`），来自动生成强大的查询能力。视频中还展示了如何在 Postman 中调用这些动态生成的接口，并通过 `customize` 方法自定义查询规则，从而实现灵活、高效的高级查询功能。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，讲师在 Typora 编辑器中展示课程大纲，定位到“3.8 Spring Data Rest 高级用法（拓展）”章节。
*   **00:00:05 - 00:00:15**：讲师介绍本节核心内容：使用 QueryDSL 来简化 Spring Data REST 中的复杂查询。
*   **00:00:15 - 00:00:30**：讲师在 IDE 中展示如何为 `stock-entity` 项目添加 QueryDSL 依赖，包括 `querydsl-jpa` 和 `querydsl-apt`。
*   **00:00:30 - 00:00:45**：讲师在 `stock-admin-user` 项目中，展示如何在 `AuthorityMenuRepository` 接口中继承 `QuerydslPredicateExecutor` 等接口。
*   **00:00:45 - 00:01:00**：讲师演示如何在 `customize` 方法中，通过 `bindings.bind(...).first(...)` 来定义模糊查询和忽略大小写的精确查询。
*   **00:01:00 - 00:01:15**：讲师在 Postman 中演示如何调用接口，通过 `menuName` 和 `menuCode` 参数进行查询。
*   **00:01:15 - 00:01:30**：讲师演示如何通过 `createTime` 参数进行时间范围查询。
*   **00:01:30 - 00:01:45**：讲师展示项目启动日志，确认服务已成功启动。
*   **00:01:45 - 00:02:00**：讲师在 Postman 中展示接口调用结果，验证查询功能。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   标题：“3. Spring data rest 与 QueryDSL 集成实现高级查询”。
    *   核心观点：“QueryDSL 会根据我们在 Spring Data Rest 中定义的实体，生成用于查询的类（以 Q 开头）”。
    *   操作步骤：“修改 stock-entity 工程，增加依赖配置”。
    *   操作步骤：“修改 stock-admin-user 的接口，以 AuthorityMenuRepository 为例”。

*   **关键代码**：

    **1. Maven 依赖配置 (在 `pom.xml` 中)**

    ```xml
    <!-- QueryDSL 插件 -->
    <dependency>
        <groupId>com.querydsl</groupId>
        <artifactId>querydsl-jpa</artifactId>
    </dependency>
    <dependency>
        <groupId>com.querydsl</groupId>
        <artifactId>querydsl-apt</artifactId>
    </dependency>
    ```

    **2. Repository 接口定义 (在 `AuthorityMenuRepository.java` 中)**

    ```java
    @RepositoryRestResource(path = "/authorityMenu")
    public interface AuthorityMenuRepository extends
            QuerydslPredicateExecutor<AuthorityMenu>,
            QuerydslBinderCustomizer<QAuthorityMenu>,
            PagingAndSortingRepository<AuthorityMenu, Long>,
            JpaSpecificationExecutor<AuthorityMenu> {

        @Override
        default public void customize(QuerydslBindings bindings, QAuthorityMenu menu) {
            bindings.bind(menu.menuName).first(StringExpression::contains); // 模糊查询
            bindings.bind(menu.menuCode).first(StringExpression::equalsIgnoreCase); // 忽略大小写
        }
    }
    ```

    **3. 时间范围查询示例 (在 `customize` 方法中)**

    ```java
    bindings.bind(menu.createTime).first((path, createTime) ->
        path.between(createTime, new Date())); // 时间段查询
    ```

*   **关键图表/演示**：

    *   **Postman 接口调用演示**：
        *   **模糊查询**：`GET http://127.0.0.1:10691/admin/authorityMenu?menuName=xxx`
        *   **精确查询**：`GET http://127.0.0.1:10691/admin/authorityMenu?menuCode=xxx`
        *   **时间范围查询**：`GET http://127.0.0.1:10691/admin/authorityMenu?createTime=2020-04-27T17:49:00.000+08:00&createTime=2020-04-27T17:50:00.000+08:00`

---

### 4) 关键场景与演示描述

*   **场景一：引入 QueryDSL 依赖**
    *   **描述**：讲师在 `stock-entity` 项目的 `pom.xml` 文件中，添加了 `querydsl-jpa` 和 `querydsl-apt` 两个 Maven 依赖。这是实现 QueryDSL 功能的基础步骤。

*   **场景二：定义 Repository 接口**
    *   **描述**：讲师在 `stock-admin-user` 项目中，创建或修改 `AuthorityMenuRepository` 接口。该接口继承了 `QuerydslPredicateExecutor`、`QuerydslBinderCustomizer`、`PagingAndSortingRepository` 和 `JpaSpecificationExecutor` 等接口，以获得 QueryDSL 的查询能力。

*   **场景三：自定义查询规则**
    *   **描述**：讲师在 `AuthorityMenuRepository` 接口的 `customize` 方法中，通过 `bindings.bind(...).first(...)` 来定义查询规则。例如，对 `menuName` 字段进行模糊查询（`contains`），对 `menuCode` 字段进行忽略大小写的精确查询（`equalsIgnoreCase`）。

*   **场景四：Postman 调用接口**
    *   **描述**：讲师使用 Postman 工具，向服务端发送 GET 请求。通过在 URL 参数中传入 `menuName`、`menuCode` 等参数，验证了 QueryDSL 生成的查询功能。例如，传入 `menuName=xxx` 可以查询出所有菜单名称包含 "xxx" 的记录。

*   **场景五：时间范围查询**
    *   **描述**：讲师在 `customize` 方法中添加了对 `createTime` 字段的时间范围查询规则。在 Postman 中，通过传入 `createTime` 参数（如 `2020-04-27T17:49:00.000+08:00` 和 `2020-04-27T17:50:00.000+08:00`），成功查询出了在指定时间范围内的记录。

*   **场景六：项目启动与验证**
    *   **描述**：讲师在 IDE 中运行 `StockAdminUserApplication`，查看控制台日志，确认服务已成功启动（端口 10691）。随后，通过 Postman 发送请求，成功获取了查询结果，验证了整个流程的正确性。
