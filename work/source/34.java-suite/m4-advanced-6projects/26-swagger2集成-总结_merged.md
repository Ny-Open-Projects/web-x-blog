# 26-swagger2集成-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对本章内容做个回顾和总结

首先咱们明确本章的学习目标

在这里咱们要掌握三点

第一咱们要掌握SWOG2制定于启动器的工装

以及它的集成配置

接着的话咱们要掌握SWOG2和Splint Data REST的集成支持

最后咱们要掌握SWOG2和SWOG Bootstrap

第三方UI的集成和配置

我们回顾下本章所讲的具体内容有哪些

首先咱们去实现了自定义的SWOG2的启动器

这个是做了一个封装

通过封装它可以在咱们项目当中更方便的去配置和使用

接下来咱们就对后台管理服务

与SWOG2做了一个集成配置

整个配置来讲就比较简单

首先我们把依赖加上去

然后增加SWOG2的属性配置

接着的话就在接口上面增加SWOG2的相关注解说明

在这里我们对相应的一些接口增加了SWOG2的描述说明

那么接着咱们就启动了工程

做了一个测试和验证

这个是原生的UI它的界面的呈现

咱们可以看到这些接口都展示出来了

但是Splint Data REST的接口却不能正常显示

然后我们就讲解了如何去让SWOG去支持Splint Data REST

首先的话咱们要添加对应的SWOG2的描述说明

然后在SWOG2的MIMI user工程当中去增加对应的系统类

最后启动后台管理工程就能够正常展示

在这里发现了报错

这个报错原因是它们的一些版本兼容性方面的问题

那么具体的话要做对应的排除处理

要将其中的源码做一定的修改

才能去适配和支持Splint Data REST的WebMVC

好 再往下面就是对集成SWOG

BotchApp第三方UI界面的支持

然后做了相关的一个配置

通过第三方UI界面整个接口文档呈现起来就更为直观

便于交互和使用

最后咱们就去修改了SplintFox Data REST

让它能够支持API的注解

实现了自定义的接口注释

否则的话按照默认的这个接口英文名称显示非常不直观

好 这个是做了一定的拓展

也是要修改对应的源码

最后咱们再来总结一下

通过SplintBotchStars的自定义封装SWOG2的启动器

它可以便于复用 统一它的配置

这个是它的一个优点

为什么咱们要去自定义封装作为启动器来去集成和使用

在SWOG和Splint Data REST的集成当中

要注意的是默认HOS REST的风格接口

它不会显示出来

也就是说

这个SWOG2的UI接口不会正常显示

但这个不影响咱们的使用

咱们遵循HeadOS的规范去操作就可以了

它只会显示咱们自定义的逻辑接口

也就是在代码工程当中

咱们自定义添加实现的相关接口

如果说咱们在这里添加的一些额外接口

它是可以正常扫描和识别显示出来的

这一点大家要明白

SWOG和SWOG2相比默认的UI界面会更为直观

便于咱们的

实际工程项目中

最好就采用第三方UI界面

去替换它的原生界面

让整个接口文档看起来更为直观

操作起来也更为简便

这个就是对本章内容的回顾与总结

这讲咱们就讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频课程聚焦于 **Spring Boot 项目中 Swagger2 的深度集成与优化**。讲师通过一个名为 `stock-starter-swagger` 的工程，演示了如何自定义 Swagger2 启动器，使其能够无缝集成 Spring Data Rest 接口，并解决默认 HATEOAS 风格接口在 Swagger UI 中不显示的问题。课程内容涵盖了自定义启动器、集成 Spring Data Rest、使用 Swagger-Bootstrap-UI 界面，以及对实体类进行注解配置等核心步骤。最终目标是实现一个配置统一、接口展示完整、界面友好的 API 文档系统。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: **课程总览与目标介绍**。讲师在 PPT 上展示了本章（第3章）的核心目标：掌握 Swagger2 自定义启动器、与 Spring Data Rest 的集成、以及与 Swagger-Bootstrap-UI 的集成。
*   **00:05 - 00:15**: **自定义 Swagger2 启动器**。讲师在代码编辑器中展示了 `AutoSwaggerConfiguration` 类的 `@Configuration` 注解和 `@Bean` 方法，用于创建自定义的 Swagger2 启动器。
*   **00:15 - 00:25**: **集成 Spring Data Rest**。讲师演示了如何在 `pom.xml` 中添加 `springfox-data-rest` 依赖，并指出需要修改 Spring Data Rest 的源码以适配 Swagger2。
*   **00:25 - 00:35**: **实体类注解配置**。讲师展示了如何在实体类 `AuthorityMenu` 上添加 `@Api` 注解来定义接口的描述，并在关联实体 `AuthorityUserRole` 上使用 `@ApiModel` 和 `@ApiModelProperty` 注解来定义字段。
*   **00:35 - 00:45**: **Swagger UI 界面展示**。讲师启动服务后，展示了 Swagger UI 界面，其中包含了自定义的接口和实体信息。
*   **00:45 - 00:55**: **总结与注意事项**。讲师在 PPT 上总结了本章内容，并强调了在 Swagger 与 Spring Data Rest 集成中，HATEOAS 风格的接口默认不会显示，只有自定义的接口才会被展示。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **第3章 Swagger2集成使用**：目标包括“掌握Swagger2自定义启动器封装与集成配置”、“掌握Swagger2与Spring Data Rest的集成支持”、“掌握Swagger2与Swagger bootstrap-ui的集成”。
    *   **总结**：通过 Spring Boot Starter 自定义封装 Swagger2 启动器，便于复用、统一配置；在 Swagger 与 Spring Data Rest 集成中，要注意的是默认 hteoas rest 风格接口不会显示，只会显示自定义的接口；swagger-bootstrap-ui 相比默认的 ui 界面更为直观，便于查看。

*   **代码内容**:
    *   **自定义启动器配置**：
        ```java
        @Configuration
        public class AutoSwaggerConfiguration {
            @Bean
            public Docket api() {
                return new Docket(DocumentationType.SWAGGER_2)
                        .apiInfo(apiInfo())
                        .select()
                        .apis(RequestHandlerSelectors.basePackage("com.ictast.stock.starter.swagger"))
                        .paths(PathSelectors.any())
                        .build();
            }
        }
        ```
    *   **实体类注解**：
        ```java
        @Api(value = "HATEOAS接口-菜单管理(AuthorityMenu)")
        @Entity
        @Table(name="t_authority_menu")
        @Data
        public class AuthorityMenu extends BaseEntity {
            // ...
        }

        @ApiModel("AuthorityUserRole(用户与角色关联表)")
        public class AuthorityUserRole extends BaseEntity{
            @ApiModelProperty(value = "用户ID", example = "1")
            private Long userId;
            // ...
        }
        ```
    *   **Spring Data Rest 仓库方法**：
        ```java
        @ApiOperation(value = "根据角色ID查找对应的菜单信息")
        @ApiImplicitParam(value = "角色ID", name = "roleId", dataType = "string", required = true)
        @Query("select menu from AuthorityMenu menu, AuthorityRoleMenu roleMenu " +
                "where menu.roleId = ?1 and menu.status = 1 and roleMenu.roleId = ?1 and roleMenu.menuId = menu.id")
        public List<AuthorityMenu> findByRoleId(@Param("roleId") Long roleId);
        ```

---

### 4) 关键场景与演示描述

*   **场景一：自定义启动器配置**。讲师在 Typora 编辑器中展示了 `AutoSwaggerConfiguration` 类的代码，通过 `@Configuration` 注解和 `@Bean` 方法，创建了一个自定义的 Swagger2 启动器，用于统一配置和管理 API 文档。
*   **场景二：集成 Spring Data Rest**。讲师在 PPT 上演示了如何在 `pom.xml` 中添加 `springfox-data-rest` 依赖，并在代码编辑器中展示了需要修改的 Spring Data Rest 源码类，如 `EntityServicesProvider`，以适配 Swagger2。
*   **场景三：实体类注解配置**。讲师在代码编辑器中展示了如何在实体类 `AuthorityMenu` 和 `AuthorityUserRole` 上添加 Swagger 注解，如 `@Api`、`@ApiModel` 和 `@ApiModelProperty`，以定义接口和字段的描述信息。
*   **场景四：Swagger UI 界面展示**。讲师启动服务后，展示了 Swagger UI 界面，其中包含了自定义的接口和实体信息，如 `AuthorityMenu` 和 `AuthorityUserRole`，并演示了如何查看接口的详细信息。
*   **场景五：总结与注意事项**。讲师在 PPT 上总结了本章内容，并强调了在 Swagger 与 Spring Data Rest 集成中，HATEOAS 风格的接口默认不会显示，只有自定义的接口才会被展示，以确保 API 文档的完整性和准确性。
