# 28-导入功能代码 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们来看一下我们第九章的最后一部分

最后一部分就是关于我们导入功能代码

下面我们再来简单看一下

前面我们已经看到过这个图

在我们项目第一章的时候就已经看到过

我们TMS中各个微服务之间调用关系是这样的

首先最上面是用户端

咱们这个项目是不是分成了四个端

分别是TMS后台管理端

还有什么呢

TMS手机的会计员端

还有司机端

还有用户端

是这么四个端

然后这四个端的话

那么他们跟我们这个应用层交互

当然这个交互过程会经过网关来处理

然后应用层分别对应的就是PDWebManager

这就是咱们第九章要完成的

就是这块的内容

然后这个是后台系统管理端

还有个PDWebCourier

这个是快递员端

然后这个Customer是用户端

还有Driver

这个就是司机端

然后我们在这个应用层

它会通过Fend去远程调用我们其他的一些组件

其实就是一个一个的微服务

所以我们这个称为服务层

包括我们前面已经完成的PDOMS

还有什么Base User Work等等这些

这些微服务我们都已经完成了

当然有一些我们是在课上去自己编写的

还有一些是代码是直接导入的

因为我们整个项目

其实它的代码量是非常庞大的

对吧

我们不可能把所有的代码全都在课堂上去敲出来

这是不太现实的

而且在我们实际工作当中

其实也都是这一个大型的项目

肯定是团队开发

对吧

每个人只是负责其中的一个部分

所以说这里边

我们有一部分是自己咱们课上来实现的

还有很多是我们直接代码导入的

然后接下来呢

我们

直接导入咱们这个PDWebManager

它属于应用层

对吧

它的定位是应用层

那么这块呢

我都提前已经导进来了

这个代码在哪呢

在我们提供的资料后台管理端

对吧

PDWebManager代码导入

这里边呢

你看resource里边呢

就是咱们这个配置文件

然后呢

Java里边呢

就是我们相应的这个Java代码

这块呢

因为从技术上来说呢

没有什么新的技术内容

所以说呢

我们直接把它导入到我们项目里面来

咱们直接使用就可以了

也就是这块内容呢

我们就不在课堂上去手敲了

咱们可以整体的大概来了解一下这个代码

好

先来看一下这个配置文件跟原先的都是一样的

对吧

没有什么区别

你看都是常规的一些配置

包括我们这个Nux

对吧

作为这个注册中心呢

还有这个服务这个配置中心呢

那么这些常规的配置

包括这个Java的配置中心呢

还有这个Jackson

对吧

它的这个日期的格式化

时间格式化

然后呢

这个是我们导进来的一个什么呢

这是一个启动类

对吧

启动类

然后呢

还有一些VO

对吧

还有一些VO

还有一些工具类

对吧

然后还有一些对于这个Find掉用的一些封装

然后还有一些配置类

当然更多的呢

是我们这个Controller

你可以看到Controller其实非常多

因为什么呢

我们后台系统管理端呢

呃

所涉及到的内容其实还是比较多的

对吧

哎

你比如说这一块

这个是什么呢

组织管理

对吧

组织管理

那么在这一块呢

就是获得组织机构数

对吧

获得详情

然后呢

获取员工详细信息

大家可以看到我们整个这个配置啊

刚才我们也看到了

这里边好像没有关于数据库的配置

对吧

哎

这是为什么呢

咱们可以回过头来来看一下

我们这个应用层啊

就是PDWeb

这个manager

包括其他的Controller

对吧

这些应用层的这些服务啊

他不会直接去操作数据库

那么如果涉及到数据库操作怎么做呢

他其实全都是通过FIN

是不是去调用相应的这些微服务组件

由这些微服务去操作数据库

哎

所以是这么一个关系啊

你看我们这里边也没有Mapper

对吧

也没有这个数据库相关的配置啊

所以这里边呢

会有大量的这种什么呢

FIN调用

你看咱们导进来的这些是不是全都是一些FIN接口

所以说呢

这里边他完成这个组织操作

员工操作

对吧

包括这个保存什么机构作业范围

对吧

这些呢

最终的全都是调用我们这个FIN接口

其实就是通过这种远程调用

对吧

接口调用

然后来实现相应的功能

好

所以这块的话呢

我们就直接导进来

然后直接来使用就可以了

那么大家呢

也可以把这个项目跑起来

这里边咱们是不是也已经加了Swagger

对吧

也已经加了Swagger

所以这个接口呢

我们其实都能看到

大家自己启动起来之后呢

也都能看到这些接口

我现在呢

可以让大家来看一下我们线上的提前已经部署好的

对吧

这个接口

其实跟我们这份代码是一样的

只不过是我们研发的时候提前已经部署好了

你看这是相应的接口

这是客户端

对吧

然后呢

这是快递员端

这个是司机端

然后还有就是后台管理端

对吧

这个是我们线上部署的

你可以看到这里边这个通过这个Swagger文档了

你也能看到这里边的这个功能是不是非常多

有个人中心

对吧

然后呢

什么位置查询

然后公共信息

还有什么司机作业单

取派件任务等等这些

那么

这些呢

全都是对应的是什么呢

就是咱们导进来的这个controller

那么最终呢

是不是给我们这个通过接口的方式来开放的吧

就是我们导进来的这一堆controller

所以说呢

整个这个后台系统管理端啊

它的功能其实非常多

对吧

但是难度并不是很难

全都是一些fin接口调用啊

主要呢

就是一些这个业务方面的代码

这是关于我们最后这一块直接啊

咱们这块呢

就不在课堂上去开发了

我们直接导到我们项目里面来直接使用就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频为一个关于“品达物流TMS系统”后台管理端开发的技术课程，主要演示了如何在 IntelliJ IDEA 中导入并运行一个已有的 Spring Boot 项目，并配置其核心功能。课程内容聚焦于“pd-web-manager”模块，详细讲解了其启动配置（`bootstrap-dev.yml`）、主程序入口（`WebManagerApplication.java`）、控制器层（`AgencyController.java`）的业务逻辑（如分页查询、保存机构范围），以及如何通过 Swagger2 配置并生成 API 文档。整个过程旨在帮助开发者快速上手并理解该微服务架构中后台管理模块的代码结构和核心功能点。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，展示 IntelliJ IDEA 的启动界面，项目结构清晰可见，当前选中的是 `pd-web-manager` 模块。
*   **00:00:05 - 00:00:15**：进入 `bootstrap-dev.yml` 配置文件，展示项目的基础配置，如 `server.addr`、`spring.application.name` 和 `spring.profiles.active`。
*   **00:00:15 - 00:00:30**：查看 `WebManagerApplication.java` 主类，重点讲解了 `@EnableSwagger2` 注解用于开启 Swagger 文档功能，并演示了 `Jackson2ObjectMapperBuilderCustomizer` 用于解决 `LocalDateTime` 类型在 JSON 序列化和反序列化时的格式问题。
*   **00:00:30 - 00:00:45**：进入 `AgencyController.java`，讲解了 `@ApiImplicitParams` 注解用于定义分页和机构ID等请求参数，以及 `PageResponse` 对象的封装。
*   **00:00:45 - 00:01:00**：继续讲解 `AgencyController` 中的 `findUserByPage` 方法，展示了如何从远程服务获取数据并进行对象转换。
*   **00:01:00 - 00:01:15**：讲解 `saveAgencyScope` 方法，演示了如何将前端传来的 `AreaVo` 列表转换为 `AgencyScopeDto` 列表，并通过 Feign 客户端批量保存到远程服务。
*   **00:01:15 - 00:01:30**：展示 `SwaggerConfig.java` 的配置代码，重点是 `Docket` 的创建和 `select()` 方法用于指定扫描的包路径。
*   **00:01:30 - 00:01:45**：在浏览器中访问 `http://localhost:8186/pd-oms/swagger-ui.html`，成功加载并展示了 Swagger UI 界面，验证了 Swagger 配置的有效性。
*   **00:01:45 - 00:02:00**：回到 IDEA，再次查看 `SwaggerConfig.java`，确认 `basePackages` 的配置值。
*   **00:02:00 - 00:02:15**：展示 Typora 文档，其中包含一个架构图，说明了 TMS 系统中各个微服务（如 `pd-web-manager`, `pd-web-courier`, `pd-web-driver`）通过网关和 Feign 调用后端服务（如 `pd-base`, `pd-user`, `pd-druid` 等）的调用关系。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **Typora 文档**：标题为“4. 导入功能代码”，内容包含一个架构图，图中展示了用户端、应用层和微服务层的调用关系。图中明确指出，可以直接将“后台管理端（pd-web-manager）”的代码导入项目中。

*   **代码关键内容**：
    *   **`bootstrap-dev.yml`**：
        ```yaml
        server:
          addr: 68.79.63.42:8848
        spring:
          application:
            name: pd-web-manager
            profiles: dev
        ```
    *   **`WebManagerApplication.java`**：
        ```java
        @EnableSwagger2
        @SpringBootApplication
        public class WebManagerApplication {
            @Bean
            public Jackson2ObjectMapperBuilderCustomizer jackson2ObjectMapperBuilderCustomizer() {
                return builder -> builder
                    .serializerByType(LocalDateTime.class, new LocalDateTimeSerializer(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")))
                    .deserializerByType(LocalDateTime.class, new LocalDateTimeDeserializer(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")));
            }
        }
        ```
    *   **`AgencyController.java`**：
        ```java
        @ApiImplicitParams({
            @ApiImplicitParam(name = "page", value = "页码", required = true, example = "1"),
            @ApiImplicitParam(name = "pageSize", value = "页尺寸", required = true, example = "10"),
            @ApiImplicitParam(name = "agencyId", value = "机构id", required = true, example = "1")
        })
        @GetMapping("/user/page")
        public PageResponse<SysUserVo> findUserByPage(@RequestParam("page") Integer page, @RequestParam("pageSize") Integer pageSize, @RequestParam("agencyId") String agencyId) {
            R<Page> result = userApi.page(page.longValue(), pageSize.longValue(), agencyId);
            if (result.getSuccess() && result.getData() != null) {
                List<SysUserVo> voList = userApi.getRecords().stream().map(user -> BeanUtil.copyProperties(user, SysUserVo.class)).collect(Collectors.toList());
                return PageResponse.<SysUserVo>builder().items(voList).page(page).pageSize(pageSize).build();
            }
            return PageResponse.<SysUserVo>builder().items(new ArrayList<>()).page(page).pageSize(pageSize).build();
        }
        ```
    *   **`SwaggerConfig.java`**：
        ```java
        @Configuration
        @EnableSwagger2
        public class SwaggerConfig extends WebMvcConfigurationSupport {
            @Bean
            public Docket createRestApi() {
                return new Docket(DocumentationType.SWAGGER_2)
                    .apiInfo(apiInfo())
                    .select()
                    .apis(RequestHandlerSelectors.basePackages("com.iteima.pinda.controller"))
                    .build();
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与配置**：演示者首先在 IntelliJ IDEA 中打开项目，导航至 `pd-web-manager` 模块，并查看其 `bootstrap-dev.yml` 配置文件，确认了服务端口、应用名称和激活的配置文件。
*   **场景二：主程序与 Swagger 配置**：演示者打开 `WebManagerApplication.java`，重点讲解了 `@EnableSwagger2` 注解的作用，并通过 `Jackson2ObjectMapperBuilderCustomizer` 自定义了 `LocalDateTime` 类型的序列化和反序列化格式，解决了前端显示和后端接收时的格式问题。
*   **场景三：控制器层业务逻辑**：演示者进入 `AgencyController.java`，详细讲解了 `findUserByPage` 方法的实现。通过 `@ApiImplicitParams` 注解定义了分页和机构ID参数，并展示了如何使用 `BeanUtil.copyProperties` 进行对象属性拷贝，以及如何使用 `PageResponse` 对象封装分页数据。
*   **场景四：保存机构范围功能**：演示者讲解了 `saveAgencyScope` 方法，展示了如何将前端传来的 `AreaVo` 列表通过 `Stream` 流式处理转换为 `AgencyScopeDto` 列表，并使用 `batchSaveAgencyScope` 方法通过 Feign 客户端批量保存到远程服务。
*   **场景五：Swagger 文档验证**：演示者在 IDEA 中确认了 `SwaggerConfig.java` 中 `basePackages` 的配置，然后在浏览器中访问 `http://localhost:8186/pd-oms/swagger-ui.html`，成功加载了 Swagger UI 界面，验证了 API 文档的生成和配置正确性。
*   **场景六：系统架构展示**：最后，演示者切换到 Typora 文档，展示了一个系统架构图，清晰地说明了 TMS 系统中各个微服务之间的调用关系，强调了 `pd-web-manager` 模块作为后台管理端的角色。
