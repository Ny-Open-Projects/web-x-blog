# 11-权限业务接口-后台管理工程搭建配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们去创建后台管理工程

我们在振留股服务工程当中

去新建一个模块

New Model

点击Next

名称叫做Bus Stock Alumin User

拨比一下,点击Next

将名称粘贴,然后Finish

这样我们就创建了后台管理服务工程

导入生效

接着咱们将它的包做一个创建

New Package

Com.idcast.tread

Stock

它的模块名称

然后它下面要创建哪些包呢

我们先把它创建好

Make DIR

一个是Configure,配置目录

Make DIR,然后是Controller

这个是Split Boot的接入程

然后是Vivo City

这个是JPA的数据程

还有Service程

咱们的启动路口

好,这些包创建完成了

咱们刷新一下

那整个包结构呢就已经创建完成

接着呢,咱们将POM的依赖呢加入进来

在讲义当中

我们将这些依赖呢

全部选中,套用进来

好,那我们来看一下具体包括哪些依赖呢

让它导入生效

在上面呢

我们先来看看这个Split Boot的依赖

然后呢,Data JPA的组件依赖

因为在这里呢

咱们要去实现增三改差的结构

就是通过了Split Data JPA这个组件呢

帮助咱们去实现的

接着的话呢

是Split RESTful的组件依赖

因为咱们是采用Split Data REST的黑头OS的高级形态

所以这个RESTful的组件依赖呢

咱们也必须将它呢加入进来

下面呢就是JSON的组件支持

然后呢是Apache Common的一些工具

就像一些Stream的操作啊

接着换的是NuX的服务注册发现依赖

然后是数据层的组件依赖

实体的依赖

公用的web层的依赖

好,主要呢就是这些依赖的组件

这里呢咱们重点了解

是对Data REST的组件依赖

还有JPA的依赖

后面SWOG2的集成

以及OS2的集成相关的依赖呢

咱们后面在讲解的时候呢

再加入进去

依赖添加完成之后呢

咱们就可以开始通过Splint Bootlet REST

去实现了用户数据层的接口

那咱们在repoC2里包下面呢

去NuX创建一个接口

BitFace

这个接口名称呢我们就叫

authorit user repoC2里

点击OK

我们看一下该如何去实现呢

首先呢它要去继承分页和排序的接口

agent under sorting repoC2里

这个范围呢要传入它对应的实体

因为呢它是用户层的数据接口

所以咱们要将那个用户的实体呢

加入进来

然后是它的主页

还继承什么接口呢

因为它是JPA的规范

JPA的这个接口呢

咱们也要把它加入进来

接着的话呢我们要给它一个访问路径

这个访问路径呢通过内部C2里

REST resource呢去配置

Path呢人用authorit user

这样呢咱们就实现了一个用户数据层的接口

它的整个实现来讲呢也是非常简单

只要呢去继承两个接口就可以了

一个呢是配几份的sorting

这个呢可以支持分页

排序等相关的查询

接着的话呢是实现JPA的接口规范

然后呢就加上它对应的读解

可以看到呢这样就非常简单对不对

不像咱们之前写conclude成接口

要去呢先在conclude上面定义好接口

然后呢service层上面

再写业务实现

最后的话呢再定义数据层接口

在这里我们可以看到

Split data REST的它是以对象为支援

它的目的是要消除繁杂的CURD增伤改查的代码

减少程序员的重复劳动

让咱们更多的精力呢

能专注于核心业务功能的实现上面

接下来呢咱们还去实现其他的全线数据层接口

每个实体呢它一般都会映射一个数据层接口

可以去实现它的增伤改查的操作

我们可以将其余6个实体呢都做对应的实现

那么为了减便期限呢

我们就将原码都copy过来

接口保留

后面用到的时候呢咱们再做具体的讲解

那我们呢将已经实现的代码

可以将它呢copy过来

刚才呢咱们实现了U者对不对

接着呢咱们将其他的接口呢copy到工程当中来

把它呢复制到repoxy图里这个包下面

咱们可以检查一下在这里呢出现了错误

这个错误呢是因为咱们没有加入query dsl的组件依赖

query dsl呢是可以实现jpa的高级查询

这个在后面章节当中呢咱们会做详细的介绍

那咱们呢先把这个错误解决掉

咱们把这个依赖加入进去

找到query dsl

将它的插件依赖呢

还有它的构件依赖

加入到anti的工程当中

把stack anti放到pump文件下面

这个依赖的话呢我们把它放在dependencies标签下面

这里报错了

因为这个标签位置没有配置正确

咱们也加上bargains

好让它导入生效

导入生效完成之后呢咱们回过头来看

在这里还是会报错对不对呢

因为呢query dsl呢

它要去编译构件一遍

生成对应的代码

在这里是以q开头的

那咱们呢找到bargains anti

在maven的视图下面

进行一个打包

clean package

整理装

咱们看一下具体错误

它说呢这个版本的话呢

没有配置正确不支持

那咱们呢去修改一下

让咱们的工程的话呢改成1.8

这里改成1.8

sdk呢也改成1.8

然后barstock anti

这里检查一下它的jtk版本是不是8系列的

好咱们就连开

咱们再重新去打包

好这个时候呢可以看下

就已经构建成功了对不对

那咱们再回过头来看一下barstock的meanuser

数据层接口

在这里就不再报错了

好至于这一块的具体作用

我们呢在下面上节

讲到supreme data loss高级用法的时候呢

再做详细的讲解

这些数据层接口的具体作用呢

咱们在业务代码编写用到的时候呢

再做具体的讲解

好咱们回到讲义当中

创建完后台管理工程之后呢

我们看一下接着还要去创建它的启动内

stock admin user application

再启动包下面new class

代码呢我们就直接拷贝过来

注意一下它的注解

在这里它需要用到哪些注解呢

因为呢我们会采用jpa相关的接口

所以呢jpa的注解必须要开启

还有它的事务jpa的操作方法呢

必须要依存于事务

这个consection manager的注解呢

大家要记得加上去

然后呢我们要指定它的扫描路径

实体的扫描路径

jpa数据层的扫描路径

这个就是咱们supreme boot

service的扫描路径

然后呢是服务的注册发现

这个呢是supreme boot的注册

这样呢咱们就完成了

后台管理服务工程的搭建

以及呢它数据层接口的实现和配置

好那这讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于一个名为 `bulls-stock` 的微服务项目中，**权限管理后台模块（`stock-admin-user`）的开发**。讲师主要讲解了如何使用 **Spring Data REST** 来实现后台管理接口，并重点演示了如何通过 **QueryDSL** 进行复杂的动态查询。课程内容包括：创建工程结构、定义数据实体、编写数据访问层接口（Repository）、集成 Swagger2 以及使用 QueryDSL 进行高级查询。整个过程是典型的 Spring Boot 项目开发流程，强调了接口设计、数据模型和查询能力。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:01:30**：课程介绍与工程创建。讲师首先展示了项目结构，然后在 IDEA 中创建了 `bulls-stock-admin-user` 工程，并配置了 `pom.xml` 文件。
*   **00:01:30 - 00:03:00**：添加 Spring Data REST 依赖。讲师在 `pom.xml` 中添加了 `spring-boot-starter-data-rest` 依赖，并引入了 `jackson-dataformat-xml` 以支持 XML 格式。
*   **00:03:00 - 00:04:30**：定义数据实体与 Repository 接口。讲师创建了 `AuthorityUser` 实体类，并定义了 `AuthorityUserRepository` 接口，继承自 `PagingAndSortingRepository` 和 `JpaSpecificationExecutor`。
*   **00:04:30 - 00:06:00**：实现复杂查询。讲师演示了如何使用 `@QuerydslPredicate` 注解和 `QuerydslBindings` 来实现基于 `menuName` 和 `menuCode` 的动态查询。
*   **00:06:00 - 00:07:30**：集成 Swagger2。讲师在 `pom.xml` 中添加了 `springfox-swagger2` 和 `springfox-swagger-ui` 依赖，并配置了 Swagger2。
*   **00:07:30 - 00:09:00**：项目构建与运行。讲师执行了 Maven 的 `clean package` 命令，成功构建了项目，并展示了 `StockAdminUserApplication` 的启动类。
*   **00:09:00 - 00:10:30**：总结与展望。讲师回顾了本节内容，并预告了后续将讲解权限核心逻辑接口的实现。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **章节标题**：`3.6 创建后台管理工程 (stock-admin-user)`，`3.7 权限核心逻辑接口实现 (重要)`，`3.8 Spring Data Rest 高级用法 (拓展)`。
    *   **技术说明**：`@RepositoryRestResource` 注解可以对外实现 REST 接口；`PagingAndSortingRepository` 支持分页与排序功能；`JpaSpecificationExecutor` 支持复杂的动态查询。
    *   **代码结构图**：展示了 `stock-admin-user` 工程的目录结构，包括 `src/main/java`、`src/main/resources` 等。

*   **关键代码**：

    *   **`pom.xml` 依赖配置**：
        ```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-rest</artifactId>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.datatype</groupId>
            <artifactId>jackson-datatype-hibernate5</artifactId>
            <version>2.9.8</version>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.dataformat</groupId>
            <artifactId>jackson-dataformat-xml</artifactId>
            <version>2.9.0</version>
        </dependency>
        <dependency>
            <groupId>io.springfox</groupId>
            <artifactId>springfox-swagger2</artifactId>
            <version>${swagger.version}</version>
        </dependency>
        <dependency>
            <groupId>com.querydsl</groupId>
            <artifactId>querydsl-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>com.querydsl</groupId>
            <artifactId>querydsl-apt</artifactId>
        </dependency>
        ```

    *   **`AuthorityUserRepository.java` 接口**：
        ```java
        @RepositoryRestResource(path = "/authorityUser")
        public interface AuthorityUserRepository extends PagingAndSortingRepository<AuthorityUser, Long>,
                JpaSpecificationExecutor<AuthorityUser> {
        }
        ```

    *   **`AuthorityMenuRepository.java` 中的 QueryDSL 配置**：
        ```java
        @Override
        default public void customize(QuerydslBindings bindings) {
            bindings.bind(menu.menuName).first(StringEx.class);
            bindings.bind(menu.menuCode).first(StringEx.class);
        }
        ```

    *   **`StockAdminUserApplication.java` 启动类**：
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        @ComponentScan(basePackages = {"com.itcast"})
        @EntityScan(basePackages = {"com.itcast"})
        @EnableJpaRepositories(basePackages = {"com.itcast"})
        @EnableTransactionManagement
        public class StockAdminUserApplication {
            public static void main(String[] args) {
                SpringApplication.run(StockAdminUserApplication.class, args);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：工程创建与依赖管理**（00:00:00 - 00:03:00）
    *   讲师在 IDEA 中创建了一个名为 `bulls-stock-admin-user` 的 Spring Boot 项目。
    *   通过在 `pom.xml` 中添加 `spring-boot-starter-data-rest` 依赖，为项目引入了 RESTful API 支持。
    *   为了支持 JSON 和 XML 格式的数据传输，讲师添加了 `jackson-datatype-hibernate5` 和 `jackson-dataformat-xml` 依赖。

*   **场景二：定义数据实体与 Repository 接口**（00:03:00 - 00:06:00）
    *   讲师创建了 `AuthorityUser` 实体类，并使用 `@Entity` 和 `@Table` 注解进行配置。
    *   讲师定义了 `AuthorityUserRepository` 接口，并使用 `@RepositoryRestResource` 注解将其暴露为 REST 接口。
    *   接口继承了 `PagingAndSortingRepository` 和 `JpaSpecificationExecutor`，前者用于分页和排序，后者用于复杂的动态查询。

*   **场景三：实现复杂查询（QueryDSL）**（00:06:00 - 00:09:00）
    *   讲师在 `AuthorityMenuRepository` 中使用 `@QuerydslPredicate` 注解和 `QuerydslBindings` 来实现动态查询。
    *   通过 `bindings.bind(menu.menuName).first(StringEx.class);` 等语句，讲师实现了根据菜单名称和编码进行查询的功能。
    *   讲师执行了 Maven 的 `clean package` 命令，成功构建了项目，并展示了 `StockAdminUserApplication` 的启动类。

*   **场景四：集成 Swagger2**（00:07:30 - 00:09:00）
    *   讲师在 `pom.xml` 中添加了 `springfox-swagger2` 和 `springfox-swagger-ui` 依赖。
    *   讲师配置了 Swagger2，以便在项目运行时可以通过浏览器访问 API 文档。

*   **场景五：项目构建与运行**（00:09:00 - 00:10:30）
    *   讲师执行了 Maven 的 `clean package` 命令，成功构建了项目。
    *   讲师展示了 `StockAdminUserApplication` 的启动类，并说明了如何通过 `@EnableDiscoveryClient` 和 `@ComponentScan` 等注解来支持服务发现和组件扫描。

---

以上是根据视频画面进行的结构化分析。希望对您有所帮助！
