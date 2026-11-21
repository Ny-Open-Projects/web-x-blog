# 22-环境搭建-准备 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们开始学习支流股开发环境的搭建

在搭建之前呢

先要做好准备工作

准备工作有哪些呢

首先你必须要具备Idea开发工具

要在本地上面安装好

能够正常运行

第二呢

你必须要有JDK 1.8以上的版本

然后Maven这一块呢

要采用3.5加以上的版本

Marcos呢

我们建议大家采用1.0.1的一个版本

因为是当时讲义编写当中呢

最新的应用版本

目前呢

可能会产生一些更新和变化

我们建议大家呢

还是按照讲义当中的版本来

避免呢

学习过程当中出现一些

不可一致的错误

那接下来我们再安装两个Idea插件

在Idea的Marketplace里面呢

我们要去搜索Maven Help跟Lompk

两个插件

这两个插件是干什么作用呢

Maven Help

它能够去帮助我们分析

整个工程的项目依赖的情况

那么我们现在来看看

比如说我要去查到一个MVC的价包依赖

它有没有产生冲突

对吧

它在这里面的话呢

有没有产生问题

比如说我搜索SplitBoot

好

这个时候呢

我就可以看到

有哪些组件呢

会引用SplitBoot

是不是整个程序非常清晰

然后呢

他们引用的这个版本后呢

都可以帮我们立即出来

这样呢

如果是出现Maven冲突的时候呢

能够极大的帮助我们

简化这一块排查的工作量

那另外一个呢

Lompk这个插件

这个插件呢

是干嘛用呢

它可以帮助我们

快速生成对应的代码

比如说

在这里面的话呢

我要去

有很多的属性

我要去生成get和set的方法

这样呢

每次去生成

而且每次追加起来呢

都比较麻烦

那么有没有比较方便的方式

有

就直接通过Lompk的

Data的这个组件

能够呢

快速生成get set的方法

这个呢

就是为什么会采用Lompk

当然了

它不仅仅是有这一个功能

比如说一些日志的

我们经常要写

Private

然后呢

Static

然后呢

Static

Final

对不对

然后Log Factory

在这里面的话呢

去找到对应的一个Log

然后呢

去

每次呢

都要去

创建这样一个Log

会非常麻烦

这个呢

有没有比较方便的方法

有

就通过Log4J2

在这里面的话

也是Lompk提供出来的

它在这里呢

就可以直接去

使用了

Log的一个插件阻力

比如说我在这里面的话呢

已经过来对Log

然后呢

点

Wall

因为呢

它这里是一个Static的方法

对不对

我们呢

可以来给大家测试一下

Public

Void Test

然后呢

我们将这个Log

看一下

是不是已经有了

对不对

非常方便

好

这个呢

是为什么要采用这个

Lompk这个插件

让我们看一下

具体是怎么安装呢

在我们的

File

然后呢

Setting

我们去搜索

Parking

P-L-U-G-I-N

P-L-U-G-I-N

好

可以看到

Plugin的菜单

对不对

在这里呢

有Markit

上面呢

有三个标签

对不对

一个是Marketplace

就是我们的市场

比如说你要搜索Lompk

那在这里呢

输入搜索就可以

因为这个是国外的网站

搜索起来呢

会有些慢

那么Install是已经安装好的插件

我们可以看一下Lompk

对不对

已经安装完成了

那么还有什么

Maven Help

是不是都已经帮我们安装好了

对不对

这个呢

我们建议大家

要先安装好

Update是说可以更新的一些插件

好

那这一块呢

就是那个环境的一个准备工作

这一讲呢

咱们先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段为一个关于 Spring Boot 项目工程搭建与配置的教程。讲师首先介绍了项目开发的环境准备要求，包括开发工具（IntelliJ IDEA）、Java 版本（JDK 1.8+）、Maven 版本（3.5+）和 Nacos 服务（1.0.1）。随后，重点演示了如何在 IntelliJ IDEA 中安装并配置必要的插件（Maven Helper 和 Lombok），并讲解了如何修改 Nacos 的配置文件以实现无密码登录。视频的后半部分，讲师深入到项目代码层面，展示了如何在 `SwaggerProperties` 配置类中定义 Swagger 的基础路径、排除路径和标题等属性，并通过 `@Value` 注解实现配置的外部化管理。整个过程旨在为后续的微服务开发搭建一个标准化、可配置的开发环境。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:01:30**：环境搭建准备。讲师在 Markdown 文档中列出开发环境要求：IDEA、JDK 1.8+、MAVEN 3.5+、NACOS 1.0.1，并强调了版本号的规范。
*   **00:01:30 - 00:03:00**：安装 IDEA 插件。讲师在 IDEA 中打开插件市场，搜索并安装 “Maven Helper” 和 “Lombok” 插件。
*   **00:03:00 - 00:04:30**：配置 Nacos 无密码登录。讲师在 Markdown 文档中展示并讲解了需要在 `application.properties` 文件中添加的配置项，包括 `spring.security.enabled=false`、`management.security=false`、`security.basic.enabled=false` 和 `nacos.security.ignore.urls=/**`。
*   **00:04:30 - 00:06:00**：代码层面的 Swagger 配置。讲师在 IDEA 中打开 `SwaggerProperties.java` 文件，讲解了如何定义 Swagger 的基础包路径、排除路径和标题等属性，并使用 `@Value` 注解进行配置管理。
*   **00:06:00 - 00:07:30**：代码细节与注解。讲师继续在 `SwaggerProperties.java` 中添加了 `@Data`、`@NoArgsConstructor` 和 `@Value` 注解，并展示了 `AuthorizationScope` 类的定义。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **版本号规范**：主版本号代表产品方向改变，次版本号代表功能或技术调整，修订号代表修复 BUG。
    *   **编写规范**：类名与方法名采用驼峰命名法，接口以 `I` 开头，实现类以 `Impl` 结尾。例如：用户接口为 `IUserService`，用户实现类为 `IUserServiceImp`。
    *   **环境搭建要求**：IDEA、JDK 1.8+、MAVEN 3.5+、NACOS 1.0.1。
    *   **Nacos 无密码登录配置**：
        ```properties
        spring.security.enabled=false
        management.security=false
        security.basic.enabled=false
        nacos.security.ignore.urls=/**
        ```
    *   **Swagger 配置类 `SwaggerProperties.java`**：
        ```java
        @Data
        @NoArgsConstructor
        public class SwaggerProperties {
            @Value("${swagger.enabled}")
            private Boolean enabled;
            private String basePackage = "";
            private List<String> basePath = new ArrayList<>();
            private List<String> excludePath = new ArrayList<>();
            @Value("${swagger.title}")
            private String title;
        }
        ```

*   **图表 / 代码**：
    *   **项目结构图**：在 IDEA 中展示了 `stock-starter-swagger` 和 `stock-starter-validator` 等模块的项目结构。
    *   **依赖分析图**：在 IDEA 中展示了项目依赖关系，包括 `spring-boot-actuator` 和 `spring-boot-starter-web` 等。
    *   **插件市场截图**：展示了在 IDEA 插件市场中搜索并安装 “Maven Helper” 和 “Lombok” 插件的界面。

---

### 4) 关键场景与演示描述

*   **场景一：环境准备与插件安装**。
    *   **演示**：讲师首先在 Markdown 文档中列出开发环境要求，然后在 IDEA 中打开插件市场，搜索并安装 “Maven Helper” 和 “Lombok” 插件。他强调了这些插件在项目开发中的重要性。

*   **场景二：Nacos 无密码登录配置**。
    *   **演示**：讲师在 Markdown 文档中展示并讲解了需要在 `application.properties` 文件中添加的配置项，包括 `spring.security.enabled=false`、`management.security=false`、`security.basic.enabled=false` 和 `nacos.security.ignore.urls=/**`。他解释了这些配置的作用是关闭 Nacos 的安全验证，以便于开发和测试。

*   **场景三：Swagger 配置类开发**。
    *   **演示**：讲师在 IDEA 中打开 `SwaggerProperties.java` 文件，讲解了如何定义 Swagger 的基础包路径、排除路径和标题等属性，并使用 `@Value` 注解进行配置管理。他展示了如何在类中添加 `@Data`、`@NoArgsConstructor` 和 `@Value` 注解，并定义了 `AuthorizationScope` 类。

*   **场景四：代码细节与注解**。
    *   **演示**：讲师在 `SwaggerProperties.java` 中添加了 `@Data`、`@NoArgsConstructor` 和 `@Value` 注解，并展示了 `AuthorizationScope` 类的定义。他解释了这些注解的作用，例如 `@Data` 用于自动生成 getter 和 setter 方法，`@NoArgsConstructor` 用于生成无参构造函数，`@Value` 用于从配置文件中注入值。

---

以上是根据视频画面进行的结构化技术课程分析。
