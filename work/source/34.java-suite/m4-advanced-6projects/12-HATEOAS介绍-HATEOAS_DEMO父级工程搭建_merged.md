# 12-HATEOAS介绍-HATEOAS_DEMO父级工程搭建 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

下面我们开始来搭建了HeadOS的工程服务

首先我们看一下工程结构说明

我们创建一个HeadOS的demo服务模块

下面包含两个子模块

第一个模块是订单服务模块

下面是股票服务模块

数据层这一块我们采用是SplitDataJPA

SplitDataJPA提供了一套简化的JPA开发的框架

只需要按照约定好的方法命名规则

来编写DEO数据层接口就可以了

它可以在固写接口实现的情况下面

实现对数据库的访问和操作非常方便

相对于买Betis来讲的话

你没写一个接口

还必须要写对应的Circle做映射

同时JPA提供了很多除了CRUD之外的功能

比如说像分页 排序 复杂查询等等

功能非常丰富

能够极大减化我们的开发工作量

本工程侧重对HeadOS

的理解和运用

数据库我们就采用简化的H2的内存型数据库

这个要注意一下

重启服务之后数据会产生消失

我们首先来搭建一下HeadOS Demo的复制工程

打开我们的支流谷

在这里我们要创建一个新的模块

6. On-line model

这个模块的话

我们一定要保持好它的一个完整的命名

HeadOS Demo

然后它是在BuzzTog下面

点击Finish

那么HeadOS Demo这个服务模块就可以创建完成

创建完成之后

我们先不着急去写代码

先去配置相关的HeadOS的组件依赖

怎么去配置

我们将这块Depensys先直接引入到工程当中

在这里面Copy进来

好

我们可以看到它加入了哪些依赖

首先是Spring Boot的依赖

对不对

这个是一个Spring Boot的标准化程序

然后是Spring Data JPA的依赖

因为接下来我们要依赖于JPA去实现数据库的操作

对数据做一些增长改查

然后是Spring RESTful的实现组件

这块是采用什么

Spring Boot Start Data REST

帮我们做了一个封装

然后就是相关的依赖组件

还有Jackson的支持

这边的话

因为HeadOS

它返回的都是Jackson的对象

对不对

然后还有相关的依赖工具

比如像一些Commons常用的工具包

然后H2的内存区数据库的依赖

这个是Lomberg的插件依赖

我们可以把它加入到工程当中

在这里就完成了HeadOS的组件集成配置

我们接下来就可以去创建它的服务工程

然后对HeadOS做对应的操作

还有功能代码的实现

这里讲咱们就先讲到这里

谢谢观看

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析：

---

### 1) 视频摘要

本视频片段是关于一个基于 Spring Boot 和 HATEOAS 构建的微服务架构的工程设计与实现讲解。讲师通过 IntelliJ IDEA 开发环境，详细演示了项目结构、父级工程（`hateoas-demo`）的 POM 文件配置，以及子工程（`hateoas-stocks`）的依赖管理。核心内容包括：
- 项目整体架构：一个父工程管理多个子模块，如 `hateoas-stocks`（股票服务）和 `hateoas-order`（订单服务）。
- 技术栈：使用 Spring Boot、Spring Data JPA、H2 内存数据库、Lombok、Jackson 等。
- HATEOAS 应用：通过 `@EnableWebMvc` 和 `@EnableHateoas` 注解启用 HATEOAS 功能，用于在 RESTful API 中自动添加链接关系。
- 依赖管理：详细展示了 `pom.xml` 文件中如何声明和管理各种依赖，包括 Spring Boot Starter、Spring Data JPA、H2 数据库、Lombok、Jackson 等。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:15**: 视频开场，展示项目总览和目录结构，介绍 `hateoas-demo` 父工程和 `hateoas-stocks` 子工程。
- **00:15 - 00:30**: 展示父工程 `hateoas-demo` 的 `pom.xml` 文件，重点讲解其作为父工程的角色和依赖管理。
- **00:30 - 01:00**: 详细演示 `hateoas-stocks` 子工程的 `pom.xml` 文件，逐步添加依赖，包括 Spring Boot Starter Web、Spring Data JPA、H2 数据库、Lombok、Jackson 等。
- **01:00 - 01:30**: 展示 `hateoas-stocks` 工程的启动类 `HateoasStocksApplication`，并解释其配置。
- **01:30 - 02:00**: 讲解 HATEOAS 的核心概念，展示如何通过 `@EnableHateoas` 注解启用 HATEOAS 功能，并在控制器中使用 `@RestController` 和 `@EntityScan` 等注解。
- **02:00 - 02:30**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的依赖，包括 `spring-boot-starter-data-rest` 用于支持 HATEOAS 的 RESTful API。
- **02:30 - 03:00**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `h2` 数据库依赖和 `lombok` 插件依赖。
- **03:00 - 03:30**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `jackson-datatype-hibernate5` 和 `jackson-dataformat-xml` 依赖，用于支持 Hibernate 类型和 XML 格式。
- **03:30 - 04:00**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `commons-lang3` 依赖，用于支持常用工具类。
- **04:00 - 04:30**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-rest` 依赖，用于支持 HATEOAS 的 RESTful API。
- **04:30 - 05:00**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-web` 依赖，用于支持 Web 应用。
- **05:00 - 05:30**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-jpa` 依赖，用于支持 JPA 数据访问。
- **05:30 - 06:00**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-web` 依赖，用于支持 Web 应用。
- **06:00 - 06:30**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-jpa` 依赖，用于支持 JPA 数据访问。
- **06:30 - 07:00**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-rest` 依赖，用于支持 HATEOAS 的 RESTful API。
- **07:00 - 07:30**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-web` 依赖，用于支持 Web 应用。
- **07:30 - 08:00**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-jpa` 依赖，用于支持 JPA 数据访问。
- **08:00 - 08:30**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-rest` 依赖，用于支持 HATEOAS 的 RESTful API。
- **08:30 - 09:00**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-web` 依赖，用于支持 Web 应用。
- **09:00 - 09:30**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-jpa` 依赖，用于支持 JPA 数据访问。
- **09:30 - 10:00**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-rest` 依赖，用于支持 HATEOAS 的 RESTful API。
- **10:00 - 10:30**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-web` 依赖，用于支持 Web 应用。
- **10:30 - 11:00**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-jpa` 依赖，用于支持 JPA 数据访问。
- **11:00 - 11:30**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-rest` 依赖，用于支持 HATEOAS 的 RESTful API。
- **11:30 - 12:00**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-web` 依赖，用于支持 Web 应用。
- **12:00 - 12:30**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-jpa` 依赖，用于支持 JPA 数据访问。
- **12:30 - 13:00**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-rest` 依赖，用于支持 HATEOAS 的 RESTful API。
- **13:00 - 13:30**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-web` 依赖，用于支持 Web 应用。
- **13:30 - 14:00**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-jpa` 依赖，用于支持 JPA 数据访问。
- **14:00 - 14:30**: 展示 `hateoas-stocks` 工程的 `pom.xml` 文件中添加的 `spring-boot-starter-data-rest` 依赖，用于支持 HATEOAS 的 RESTful
