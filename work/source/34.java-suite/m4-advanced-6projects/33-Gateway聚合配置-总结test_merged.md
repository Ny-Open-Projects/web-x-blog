# 33-Gateway聚合配置-总结test — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对本章内容做个回顾和总结

首先我们看一下本章的学习目标

在这里咱们要找到三点

第一要实现自定义OS2启动器的封装和配置

接着的话要实现OS2和Swog2的集成使用

最后咱们就要实现聚合文档

Swog2跟SplintColor Gateway的集成使用

那咱们再来回顾一下本章的具体内容

首先咱们对实现说明做了一个讲解

因为之前咱们是实现了基于爱护用户的OS2密码模式的健全

它只能指定一个用户数据源

如果是仍然需要采用密码模式

就需要咱们提供两套认证服务

作为教学演示我们就不同时采用两套认证服务

因为这只是重复性的配置

没有太多技术学习意义

但是咱们还是要保障登录和菜单权限的健全

这些在后面上节还会做具体的讲解

那么本章的话仍然是拿后台管理服务为例

进行了配置和讲解

首先咱们是实现了制定OS2的启动器封装和配置

接着的话咱们就实现了制定OS2启动器和后台管理服务的集成使用

在这里咱们也做了对应的测试和验证

接下来咱们就对Swog2实现了健全的访问

这里有三种解决方案

大家可以根据自己的需要去采用不同的方案来做实现

我们在这里采用的是比较简单易用的第三种方式进行了配置

咱们在下面也做了一个测试和验证

在这里咱们可以看到OS2的健全配置该如何去实现

最后咱们就对Spring Cloud Gateway网关服务做了一个集成配置

实现了续合文档的功能

续合文档的实现

测试是在代码的配置上面

在下面我们要知道如何去扫描不同的Swog服务节点信息

如何去做对应的去从处理

接下来就是在路由方面去做对应的转发配置

然后要去增加一个Conclude层的接口映射

因为咱们可以看到Swog的它的接口地址

其实后面是做了多个路径的访问请求

咱们通过F12刷新页面

可以看到它其实是有多个额架可是请求符合额层的

这个Swog的Conclude的接口一定要增加进去

否则的话就无法去访问和加载对应的Swog服务节点信息

最后咱们做了一个集成和验证

因为咱们的后台管理服务是加了一个后缀路径

所以它真正有效的节点是最后一个路径

这一点咱们要注意一下

咱们也对整个聚合服务文档的有效性做了一个试验

做了一个测试和验证

整体的话测试都能够正常使用

最后咱们再来总结一下

在这里咱们要完成自定义OS2的启动器封装

公用配置的统一处理

以及个性化部分可以读取项目的配置去独立处理

比如说不需要加入健全的URL路径

咱们在工程服务当中去配置EnogyURL属性指定要忽略的接口地址就可以了

接下来咱们就完成了自定义OS2与管理后台服务的集成配置

这个要掌握在实际项目当中具体的使用

SWOG2它也可以去支持OS2的健全处理

有三种解决方案

在上面章节当中咱们就做了介绍

我们可以根据业务需要采用灵活的配置方式做对应的实现

便于整个项目的集成和使用

在SWOG2与Gateway网关服务的集成当中

我们就使用了Gateway的服务接口

必须要做好对应的映射处理

这个咱们在代码配置过程当中也做了详细的讲解

这样的好处就在于咱们就不用在配置文件当中再做特殊的定义和配置

这样Gateway就能根据配置文件当中所配置的路由转发信息

去自动扫描SWOG2文档节点服务信息

就能够实现聚合文档便于咱们的维护和使用

好

最后咱们再来看一下

FQ在整个实现过程当中可能会遇到的一些问题处理

第一点是SWOG2 2.9.2的版本

它不再支持Gawar 18.0版本

其中时候会爆错

这个时候咱们要注意一下

将它的主线升级至20.0版本

将它的依赖做对应的修改

最后如果是大家需要扩展Spring Data REST相关的知识点信息

可以参考网上相关的资料

这里也提供出来一个链接地址

大家有时间的话可以再去研究和学习一下

好

这讲就到此结束

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析。

---

### 1) 视频摘要

本视频课程主要讲解如何将自定义的 OAuth2 认证服务与 Swagger2 API 文档工具集成，并通过 Spring Cloud Gateway 实现统一的 API 网关管理。课程内容围绕一个名为 `bulls-stock` 的交易系统展开，重点在于解决 Swagger2 在 OAuth2 保护的资源下无法正常访问的问题。讲师通过修改配置、编写自定义的 Swagger2 启动器和控制器，实现了在 Gateway 网关中动态加载并访问多个后端服务的 Swagger 文档，同时解决了 Swagger2 与 OAuth2 集成时的常见配置问题。课程最后还包含了一个 FAQ，提醒用户注意 Swagger2.9.2 版本对 Guava 18.0 的兼容性问题。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:15**：课程开场，展示文档大纲，介绍本章目标：实现 OAuth2 与 Swagger2 的集成，并与 Spring Cloud Gateway 集成。
*   **00:00:15 - 00:00:30**：讲解自定义 OAuth2 启动器的封装，以及如何将其与后台管理服务集成。
*   **00:00:30 - 00:00:45**：介绍 Swagger2 实现鉴权访问的三种方案，并引出本课程将采用最简单的方法。
*   **00:00:45 - 00:01:00**：演示如何在 Swagger UI 中手动添加 Bearer Token 进行调试。
*   **00:01:00 - 00:01:15**：讲解如何通过自定义 `StockSwaggerProvider` 类来动态获取所有 Swagger 资源。
*   **00:01:15 - 00:01:30**：展示如何创建 `StockSwaggerController` 控制器，用于提供 Swagger2 的资源。
*   **00:01:30 - 00:01:45**：演示如何通过 Gateway 网关访问 Nacos 注册中心中不同服务的 Swagger 文档。
*   **00:01:45 - 00:02:00**：课程总结，强调了自定义 OAuth2 启动器、Swagger2 鉴权和 Gateway 集成的实现方式。
*   **00:02:00 - 00:02:15**：FAQ 部分，讲解 Swagger2.9.2 版本不支持 Guava 18.0 的问题及解决方案。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **目标**：实现自定义 OAuth2 启动器、实现 OAuth2 与 Swagger2 的集成、实现 Swagger2 与 Spring Cloud Gateway 的集成。
    *   **步骤**：自定义 OAuth2 启动器、集成后台管理服务、实现 Swagger2 鉴权访问、集成功能验证。
    *   **总结**：完成自定义 OAuth2 启动器的封装，公用配置统一处理，个性化部分可以读取项目的配置独立处理；完成自定义 OAuth2 与后台管理服务的集成配置；Swagger2 也可以支持 OAuth2 鉴权，采用灵活的配置方式，便于使用；与 Gateway 集成中，实现 Swagger2 服务接口，做好映射，不用在配置文件中作特殊处理。
    *   **FAQ**：Swagger2.9.2 版本不再支持 guava18.0 版本，启动会报错。

*   **代码关键内容**：

    *   **Maven 依赖**：
        ```xml
        <!-- OAuth2 认证自定义启动依赖 -->
        <dependency>
            <groupId>com.itcast.trade.stock.starter</groupId>
            <artifactId>bulls-stock-starter-oauth2</artifactId>
            <version>${project.stock.version}</version>
        </dependency>
        ```

    *   **Swagger2 鉴权配置**：
        ```java
        @Autowired
        public StockSwaggerProvider(RouteLocator routeLocator) {
            this.routeLocator = routeLocator;
        }

        @Override
        public List<SwaggerResource> get() {
            List<SwaggerResource> resources = new ArrayList<>();
            List<String> routeHosts = new ArrayList<>();
            // ... 其他逻辑
        }
        ```

    *   **Swagger2 控制器**：
        ```java
        @RestController
        @RequestMapping("/swagger-resources")
        public class StockSwaggerController {
            @Autowired(required = false)
            private SecurityConfiguration securityConfiguration;
            @Autowired(required = false)
            private UiConfiguration uiConfiguration;
            private final SwaggerResourcesProvider swaggerResources;

            @GetMapping("/configuration/ui")
            public Mono<ResponseEntity<UiConfiguration>> uiConfiguration() {
                return Mono.just(new ResponseEntity<>(
                    Optional.ofNullable(uiConfiguration).orElse(UiConfigurationBuilder.builder().build()), HttpStatus.OK));
            }

            @GetMapping("")
            public Mono<ResponseEntity> swaggerResources() {
                // ... 逻辑
            }
        }
        ```

    *   **解决 Swagger2.9.2 与 Guava 18.0 兼容性问题**：
        ```xml
        <dependency>
            <groupId>com.google.guava</groupId>
            <artifactId>guava</artifactId>
            <version>20.0</version>
        </dependency>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：Swagger2 鉴权访问问题演示**
    *   **描述**：讲师在 Swagger UI 中尝试访问一个受 OAuth2 保护的接口，但返回了 401 错误。他解释了有三种解决方案：直接在 Swagger 中申请 token、自定义全局参数、全局预置参数。讲师选择第三种方法，因为它最简单。

*   **场景二：手动添加 Token 并成功访问**
    *   **描述**：讲师在 Swagger UI 的 “Authorize” 标签页中，手动输入了之前申请的 Bearer Token。他点击“Authorize”按钮后，再次调用接口，成功返回了数据，证明了手动添加 Token 的方法有效。

*   **场景三：自定义 Swagger2 启动器与控制器**
    *   **描述**：讲师编写了 `StockSwaggerProvider` 类，用于动态获取所有 Swagger 资源。然后，他创建了 `StockSwaggerController` 控制器，通过 `@GetMapping("/configuration/ui")` 和 `@GetMapping("")` 两个方法，向 Swagger UI 提供配置和资源信息。

*   **场景四：通过 Gateway 网关访问多个服务的 Swagger 文档**
    *   **描述**：讲师在 Swagger UI 中选择“选择新加入的后台管理服务，带 admin 路径”。他演示了如何通过 Gateway 网关访问 Nacos 注册中心中不同服务的 Swagger 文档。他强调，选择服务时，要根据配置的 context-path 来选择，例如选择 `admin` 路径的服务。

*   **场景五：FAQ 问题演示**
    *   **描述**：讲师展示了 Swagger2.9.2 版本不支持 Guava 18.0 的错误信息。他提供了解决方案，即将 Guava 依赖的版本从 18.0 升级到 20.0。他同时提到了 Spring Data REST 扩展的配置问题，需要修改相关配置。
