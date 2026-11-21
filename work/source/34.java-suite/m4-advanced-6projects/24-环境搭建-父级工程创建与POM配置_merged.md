# 24-环境搭建-父级工程创建与POM配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

咱们就来创建复级工程

我们看一下复级工程

它主要是管理我们的子服务之间的依赖

它不做具体的业务实现

复级工程主要作用是要集成和配置

十分靠的阿里巴巴的开发环境

在这里会有相关的一些组件

以及构建的具体配置

好 那我们就来做一个实现

打开我们的工程

然后去创建一个project

new project

点击next

在这里要给它一个主题ID

叫come idcast

然后是什么

pass

我们的支流股股

pass stock

它的版本我们按规范来

1.0.0

按照我们项目自身的规范

然后点击next

这个给它一个分割线

不要写在一起

这样要给它分割线

这样看起来更加直观一点

然后这个路径的话

我们放在第一

好 finish

这个时候它提示没有这个目录

没关系

我们点击OK

它会自动进行创建

好 已经创建完成

创建完成了

它会有一个manual的结构

对不对

那我们可以把src目录

把它给删除掉

不需要

因为它不负责业务的实现

最主要就是pum

依赖这一块的基层配置管理

我们将它的一些依赖拨币过来

然后放到我们的pum文件当中

在这里让它导入生效

大家注意

如果是第一次去搭运这个环境

建议大家采用老师的虚拟机

采用老师这个manual虚拟机

因为在这里我们已经下载了

十分靠的阿里巴巴的所有相关的一些依赖

如果说自身的产品

自身去下载构建起来可能会比较慢一点

当然的话也可以自身去下载

对不对

如果说你想快一点

或者说下载不成功的话

就可以采用老师的虚拟机进行一个连接

那么连接的时候

就是maiwen要去指向所对应的虚拟机的地址

这一块我就不做过多的讲解

我们还是侧重我们所要学习的目标和内容

在这里

我们来讲解一下pum的一个依赖

它在这里的话

距离是怎么配置的

首先是properties

它是什么

自定义的属性

能够去实现我们统一的版本的管理

在这里可以看到像是分卡的阿里巴巴的版本

对不对

给了V的一个版本

maiwen编译的maiwen插件

构建等相关的一些版本都在上面

做一个统一的配置管理

这个是自定义的属性

再往下面是depensys

这个是公用的依赖

也就是说

在这里面配置的依赖

子服务就不需要再重新去引用

它会自动去继承

然后获取到对应的maiwen依赖组件

那么再往下面看depensys management

这个是什么

这个是maiwen的一个依赖的管理

在这里大家要注意一下

这个跟这个区别是什么

这个它会立马加载相关的一些依赖到我们工程当中

但在这里它不会首先去加载

它在这里是先做了一个声明

那么什么时候去加载呢

在你指幅模块如果是需要使用的时候

它就会去加载

所以我们可以看到下面的depensys

它做了很明确的定义

对不对

你的group ID artifact ID以及我选版本号是什么

都有一个很明确的标识

好这个是depensys management的一个作用

那么再往下面看的就是build

我们整个工程

这一块该怎么去构建

比如说它的打包之后的名称对不对

然后呢

要设置的resource的资源目录情况

然后还有什么maiwen的编译插件等等

最后呢

是plugin management

这个是什么意思

这个是不是跟这个有点类似呢

一个是depensys management

一个是什么插件的声明对不对

同样的在这里呢

它不会先把这些插件的依赖加入进来

如果说你指幅模块需要就是在具体使用的时候

比如说指幅模块

哎

它也定了这些插件

这样一个插件

那么呢

它就会去根据复集的这个声明查找对应的插件

然后呢

加载到指幅模块当中

是这么一个作用

那这个呢

就是form的一个配置

再往下面的话呢

我们就要去创建

Gateway网关服务以及User服务

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于“Spring Cloud Alibaba”微服务项目工程搭建的入门教程。讲师通过 IntelliJ IDEA 开发工具，演示了如何创建一个名为 `bulls-stock` 的父级 Maven 工程，并配置其核心依赖。主要内容包括：定义统一的版本号、引入 Spring Boot 和 Spring Cloud Alibaba 的依赖、添加 Lombok 插件以简化开发、配置资源目录的过滤规则，以及规划后续要创建的子工程（如 Gateway 和 User 服务）。整个过程旨在为后续的微服务开发建立标准化的项目结构和依赖管理。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面的时间点，以下章节是根据画面内容和逻辑顺序进行的划分：

*   **00:00 - 00:05**: **课程引入与工程目标**。讲师在 Markdown 文档中说明本节目标是“创建父级工程”，并强调将引入 Spring Cloud Alibaba 依赖。
*   **00:05 - 00:15**: **配置父工程的 POM 文件**。在 IntelliJ IDEA 中打开 `pom.xml` 文件，开始配置 `<properties>` 区域，定义了 `spring.cloud.alibaba.version`、`spring-cloud-gateway.version`、`spring-boot.version` 等关键版本号。
*   **00:15 - 00:25**: **添加 Spring Boot 依赖**。在 `<dependencyManagement>` 区域中，添加了 Spring Boot 的 `spring-boot-dependencies` 依赖，用于管理 Spring Boot 的版本。
*   **00:25 - 00:35**: **添加 Spring Cloud Alibaba 依赖**。在 `<dependencyManagement>` 区域中，添加了 `spring-cloud-alibaba-dependencies` 依赖，用于管理 Spring Cloud Alibaba 的版本。
*   **00:35 - 00:45**: **添加 Lombok 插件**。在 `<dependencies>` 区域中，添加了 Lombok 插件，用于简化 Java Bean 的 Getter、Setter 等方法的编写。
*   **00:45 - 00:55**: **配置资源目录**。在 `<build>` 区域中，配置了 `resources` 节点，设置了 `src/main/resources` 为资源目录，并开启 `filtering`（过滤）功能。
*   **00:55 - 01:05**: **规划子工程**。讲师在 Markdown 文档中提到，接下来将创建两个子工程：`stock-gateway`（网关服务）和 `user`（用户服务）。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **章节标题**：`3. 工程搭建`，`4. 小结`，`第2章 工程规范与环境搭建`。
    *   **核心目标**：创建父级工程 `bulls-stock`，引入 Spring Cloud Alibaba 依赖。
    *   **技术选型**：Spring Boot 2.1.6.RELEASE，Spring Cloud Alibaba 2.1.1.RELEASE，Spring Cloud Gateway 2.1.2.RELEASE。

*   **关键代码片段**：

    *   **父工程 `pom.xml` 中的 `<properties>` 配置**：
        ```xml
        <properties>
            <spring.cloud.alibaba.version>2.1.1.RELEASE</spring.cloud.alibaba.version>
            <spring-cloud-gateway.version>2.1.2.RELEASE</spring-cloud-gateway.version>
            <spring-boot.version>2.1.6.RELEASE</spring-boot.version>
            <maven.compiler.source>1.8</maven.compiler.source>
            <maven.compiler.target>1.8</maven.compiler.target>
            <maven.compiler.plugin.version>3.8.0</maven.compiler.plugin.version>
            <maven-jar-plugin.version>3.1.0</maven-jar-plugin.version>
        </properties>
        ```

    *   **父工程 `pom.xml` 中的 `<dependencyManagement>` 配置**：
        ```xml
        <dependencyManagement>
            <dependencies>
                <!-- Spring Boot 组件 -->
                <dependency>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-dependencies</artifactId>
                    <version>${spring-boot.version}</version>
                    <type>pom</type>
                    <scope>import</scope>
                </dependency>

                <!-- Spring Cloud Alibaba 依赖组件 -->
                <dependency>
                    <groupId>com.alibaba.cloud</groupId>
                    <artifactId>spring-cloud-alibaba-dependencies</artifactId>
                    <version>${spring.cloud.alibaba.version}</version>
                    <type>pom</type>
                    <scope>import</scope>
                </dependency>

                <!-- Spring Cloud 普通依赖组件 -->
                <dependency>
                    <groupId>org.springframework.cloud</groupId>
                    <artifactId>spring-cloud-commons-dependencies</artifactId>
                    <version>${spring.cloud.alibaba.version}</version>
                    <type>pom</type>
                    <scope>import</scope>
                </dependency>
            </dependencies>
        </dependencyManagement>
        ```

    *   **父工程 `pom.xml` 中的 `<dependencies>` 配置**：
        ```xml
        <dependencies>
            <!-- Lombok 插件，简化开发代码 -->
            <dependency>
                <groupId>org.projectlombok</groupId>
                <artifactId>lombok</artifactId>
                <optional>true</optional>
            </dependency>
        </dependencies>
        ```

    *   **父工程 `pom.xml` 中的 `<build>` 配置**：
        ```xml
        <build>
            <finalName>${project.name}</finalName>
            <!-- 设置 resources 资源目录 -->
            <resources>
                <resource>
                    <directory>src/main/resources</directory>
                    <filtering>true</filtering>
                </resource>
                <resource>
                    <directory>src/main/java</directory>
                </resource>
            </resources>
        </build>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建父级工程**。
    *   讲师在 IntelliJ IDEA 中点击“New Project”按钮，弹出“New Project”对话框。
    *   在“Project name”中输入 `bulls-stock`，在“Project location”中指定路径 `D:\IntelliJ_Workspace\courses\day1\bulls-stock`。
    *   系统提示“Directory Does Not Exist”，讲师点击“Finish”按钮，IDEA 会自动创建该目录。

*   **场景二：编辑 `pom.xml` 文件**。
    *   讲师在 IntelliJ IDEA 中打开 `bulls-stock` 工程的 `pom.xml` 文件。
    *   通过鼠标选中并高亮显示 `<properties>` 区域，逐一添加并配置了各个版本号。
    *   在 `<dependencyManagement>` 区域，依次添加了 Spring Boot 和 Spring Cloud Alibaba 的依赖。
    *   在 `<dependencies>` 区域，添加了 Lombok 插件。
    *   在 `<build>` 区域，配置了资源目录和过滤规则。

*   **场景三：规划子工程**。
    *   讲师在 Markdown 文档中提到，接下来将创建两个子工程：`stock-gateway` 和 `user`。
    *   在 IntelliJ IDEA 的项目结构中，可以看到 `bulls-stock` 工程下已创建了 `stock-gateway` 和 `user` 文件夹，用于存放子工程的代码。

以上是根据视频画面内容进行的结构化分析。
