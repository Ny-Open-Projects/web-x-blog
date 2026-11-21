# 16-OAUTH2生产实践-认证服务搭建 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始编写工程服务的代码

首先咱们要创建一个公用组件服务

这个公用组件服务的作用是干嘛呢

它是为了便于微服务之间

公用功能的一个附用

也就是说我们要减少不必要的重复工作

比如说我们有些工具

像是Skynutils对Skyn的一些处理

如果说你不去做统一封装

每个工程都去写一份Skynutils

这样的话就会有大量的重工性的劳动

那么我们要把它统一封装一下

减少一下不必要的成本

同时的话也可以便于我们去统一组件的一个管理

如果说Skynutils

我们比如说要截取一个受付算的一个方法

我们要做一个修改

比如说从之前的长度我们要更改一下

那么的话我只要修改一个地方就可以了

就不需要每个地方都去做一个维护处理

那咱们来看一下

公用组件包括哪些服务模块呢

在下面的话咱们是分了四个组件服务

有哪四个呢

第一个是Stock Common DAO

它的意思是公用的DAO数据层组件

目的是用来管理数据层的依赖

以及公用的接口

再往下面咱们可以看一下

有Stock Common Service

这个是什么呢

这个是公用的服务层组件

那么再往下面是Stock Common Utils

这个就是公用的一个辅助工具组件

比如说

我们用了一些Stream的工具

日期的工具

还有加密解密工具

统一异常处理等等

那Stock Common Web呢

就是公用的Web层组件

好

这些的话呢

就是我们公用组件的模块

那么还有一个呢

是统一的实体工程

为什么要把实体工程统一起来呢

这个呢

是为了便于我们各个微服务之间的一个引用

如果说我们不同意实体

每个微服模块呢

都会有一份实体

如果说我们其他模块也要对这个实体进行操作

那么你要维护多份吗

如果是维护比较多的这个实体的话呢

我们的开发工作量就会比较多

对不对

所以的话呢

为了便于统一管理

我们呢

把它放在一个工程当中

还有一个好处在于什么呢

如果说你要引用其他的服务工程上的实体

那么其他服务呢

它会有自身的依赖

对不对

这样的话呢

我把实体专门抽取出来

整个依赖的话呢

就会比较好

比较纯净

那么这个就是统一实体的一个工程的作用

它与呢

Stalk Common是同一个层级

在这里呢

为节省一点时间

咱们呢

就不重新去创建和编写对应代码了

我们呢

就直接引用到工程当中

我们可以看一下

Bus Talk Common

下面呢

分了四个组件模范

对不对

DAO

Service

Utils

Web

然后呢

还有Stalk NT

好

那接着的话呢

咱们就要去实现了认证服务的代码编写

那我们首先来看一下认证服务这块的说明

统一认证服务呢

它是实现了Auth2的认证功能

在服务设计上呢

它采用的是增强Token方式

这套流程呢

它会包含Token的扩展

缓存的集成认证

密码模式

加密处理

自动化配置

等等一系列功能

如果咱们学会这套流程的使用呢

就能够利用Splint Security

去处理大部分的业务场景

以及呢

包括JWT的实现

其他的话呢

都比较简单

主要呢

咱们能够掌握这套增强Token的使用

以及呢

集成和配置

好

那咱们呢

就来具体看一下

在下面的话呢

我们数据层产生的是JPA实现

自定义的用户服务接口

然后呢

实现了用户密码模式认证

之前呢

咱们讲了四种模式

对不对

在这里呢

因为咱们要面向的是APP用户

所以呢

这里我们是结合了OS2的密码模式

来实现的统一认证

那咱们看一下

认证服务这一块的工程结构

在这里面的话呢

我们可以看到

有很多的一些包

对不对

这些包的话呢

有Config

有数据层的

有Service层的

还有一些启动配置的

那整个的一个工程依赖呢

我们可以看一下

在这里面的话呢

有OS2的核心组件依赖

然后呢

Splint Security的依赖

自动化的版权依赖

然后呢

在这里面的话呢

通过Splint Boot Start的

它是基于Ladies的一个

返存封装依赖

还有呢

GPA的依赖实现

以及呢

Nagos的服务注册发现依赖

下面的话呢

就是一些公用的

像Utils啊

公用的实体啊

然后那个

下面是连接词的依赖

然后呢

Fleamark Web

这个就是Start Web

因为我们呢

要去实现Web接口

对不对

下面的话呢

就是Tomcat

然后呢

好

再往下面呢

就是打包的一个配置

打包配置当中的话呢

这个是它的一个名称

然后下面是它对应的插件

咱们可以看到

它包括一些

Resource的一些插件

对不对

然后呢

还有我们的一些Java

Java下面的话呢

因为

如果是我们采用MapBetis

下面的话呢

会有一些XML

就是Circle的XML

所以呢

在这里要将对应的XML文件呢

要那个打包加入进去

好

这些呢

就是整体的一个POM依赖的一个配置

那咱们呢

就来创建一下Shared Auth这个工程

咱们右键New Model

这里呢

选中MapBet模板

然后点击Next

下面的话呢

我们给它一个模块名称

叫Shared Auth

点击Next

将名称改一下

然后点击Finish

这时候呢

我们就创建一个Auth的认证服务

将它导入生效

这里呢

我们把它禁止忽略

好

这个创建完成之后呢

我们要将依赖导入进来

对不对

那我们呢

将这个依赖拖背过来

咱们先将复集工程的依赖属性配置呢

加入进去

这里面的话呢

有三个版本的配置信息

把它放在它的复集工程

把Stalk下面

那我们放在Properties标签下面

好

加入进去

加入完成之后呢

咱们就要去加入它对应的依赖

这个依赖呢

我们也把它全选

然后copy过来

把它呢

放在我们的BuzzTalk

BuzzShared Auth下面

然后呢

直接粘贴

让它导入生效

这一块呢

就是Auth认证服务的依赖

这些依赖呢

刚才咱们是做了讲解和介绍

最主要的话呢

咱们要了解

要将那个Auth2的核心组件依赖呢

加入进来

还有SplitSecurity

因为呢

是基于这个

这两个组件呢

SplitSecurity

加上Auth2

实现了统一认证

那我们呢

再将对应的启动包

先创建一下

New Package

给它报名

com.idcast.buzz.stock

然后呢

shared.auth

下面的话呢

我们再创建一个包

make dir

然后startup

然后呢

这个名称拼写错了

我们重新刷新一下

也啊

让他们这个删除

他们呢改用一个命令

rds

然后呢

创建

startup

再刷新一下

好

这个名称呢

注意不要拼写错误了

咱们创建启动内

cast

然后呢

shared

auth

创建

application

这个呢是它的启动内名称

我们将代码呢

直接引入过来

好

从讲解当中呢

拨不进来

上面部分呢

是对应的注解

下面的话呢

是它的启动方法

那注解在这里呢

我们来看一下

首先呢

这是一个实名簿的程序

对不对

然后要开启什么

nucleus的服务注册发现

然后是它的组件的扫描

这个呢

因为我们是基于JPG的实现

所以呢

要将anti-scan

就是实体的扫描

以及呢

JPG的数据层的扫描

一定要指定对应的路径

然后呢

咱们在这里会用到缓存

就是基于os2的一个认证

会那个集成缓存的一个使用

所以呢

我们也将缓存开启

好

再往下面呢

咱们来看一下

接着的话呢

就是要创建对应的实体

实体的话呢

要创建一个用户

对不对

因为呢

咱们是通过密码模式进行认证

所以呢

你的用户是不是要传递对应的用户币呢

所以呢

是不是要传递对应的用户编号

以及用户密码呢

是吧

所以呢

我们这个用户呢

就是负责对应的一个关系映射

也就是说

作为呢

用户的一个基础信息

咱们来看一下

在bus.togg.anti下面

那咱们来看一下

这个chad user

对应呢

会有他的属性

然后有用户编号

用户名称

密码

对不对

其他的话呢

就是用户的一些基本资料

等等信息

最主要的话呢

我们一定要保证好

他有一个名称

以及呢

对应的

用户的一个属性

的密码

好

这个呢

是用户的一个实体

那这个jpg实体呢

咱们要去开启

n体

这个注解

这个呢

要清楚

好

然后呢

table的一个表名称的映射

我们采用的是

自动转换处理

可以呢

不用再加

crumian的

就是属性列的

这种指定映射

因为这样加起来

又会很麻烦

对吧

因为咱们呢

开启自动转换

就可以了

好

在这里呢

就是对认证服务的

一个工程的搭建

一些基础性的配置

再往下面呢

咱们就会实现了

它对应的数据层方法

以及呢

os2的一个集成配置

那这一讲呢

咱们先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于“OAuth2生产实践”的第2章，主要讲解如何构建一个认证服务（`trade-auth`）。课程内容围绕一个微服务架构展开，首先介绍了项目中“公用组件”（`stock-common`）的结构和作用，随后重点讲解了认证服务的工程结构、依赖配置、启动类以及数据层设计。课程强调了使用 Spring Cloud OAuth2、Spring Security 和 JPA 等技术栈，并通过 IDEA 开发环境进行演示，旨在帮助学习者掌握如何从零开始搭建一个具备用户认证功能的微服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: **课程引入与目标**。讲师介绍了本章的目标是实现一个认证服务，并简要回顾了之前章节中“公用组件”的概念。
*   **00:15 - 00:45**: **公用组件 (stock-common)**。讲解了 `stock-common` 模块的结构，包括 `dao`、`service`、`utils` 和 `web` 四个子模块，并介绍了 `stock-entity` 模块作为统一的实体工程。
*   **00:45 - 01:15**: **认证服务 (trade-auth) 服务说明**。详细说明了认证服务将实现 OAuth2 认证功能，采用增强 token 方式，并会集成 Spring Security 处理大部分业务场景，包括 JWT 的实现。
*   **01:15 - 01:45**: **工程依赖配置**。在 POM 文件中配置了 OAuth2 的核心依赖（`spring-cloud-starter-oauth2`）和 Spring Security 依赖。
*   **01:45 - 02:15**: **工程依赖配置（续）**。继续配置了 Web 模块依赖（`spring-boot-starter-web`）和 Tomcat 容器依赖（`spring-boot-starter-tomcat`）。
*   **02:15 - 02:45**: **父级工程依赖属性配置**。在父级 POM 文件中定义了版本号，如 `spring-cloud-starter.version` 和 `druid.version`，以便子模块继承。
*   **02:45 - 03:15**: **认证服务工程结构**。在 IDEA 中展示了 `trade-auth` 项目的目录结构，包括 `src/main/java` 和 `src/main/resources`。
*   **03:15 - 03:45**: **启动类 (TradeAuthApplication)**。展示了 `TradeAuthApplication` 启动类的代码，其中使用了 `@SpringBootApplication`、`@EnableDiscoveryClient`、`@ComponentScan`、`@EntityScan` 和 `@EnableJpaRepositories` 等注解。
*   **03:45 - 04:15**: **数据层设计**。讲解了 JPA 实体类需要开启 `@Entity`、`@Table` 和 `@Id` 注解，并采用自动转换处理，无需手动添加 `@Column` 注解。
*   **04:15 - 04:45**: **数据层接口 (TradeUserRepository)**。展示了用户信息数据层接口 `TradeUserRepository` 的注释和定义。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **3.3 公用组件 (stock-common)**: 描述了其作用是便于微服务之间公用功能的复用，并展示了其目录结构，包括 `stock-common-dao`、`stock-common-service`、`stock-common-utils` 和 `stock-common-web`。
    *   **3.4 认证服务 (trade-auth)**: 说明了服务将实现 OAuth2 功能，并展示了其工程结构，包括 `src/main/java` 和 `src/main/resources`。
    *   **4. 启动类 (TradeAuthApplication)**: 展示了启动类的代码和注解。
    *   **6. 数据层**：说明了 JPA 实体类的注解要求和数据层接口的定义。

*   **代码关键内容**:
    *   **POM.XML 文件 - OAuth2 依赖**:
        ```xml
        <!-- OAuth2 的核心组件 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-oauth2</artifactId>
            <version>${spring-cloud-starter.version}</version>
        </dependency>
        ```
    *   **POM.XML 文件 - Spring Security 依赖**:
        ```xml
        <!-- Spring Security 依赖 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-security</artifactId>
            <version>${spring-cloud-starter.version}</version>
        </dependency>
        ```
    *   **POM.XML 文件 - Web 模块依赖**:
        ```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        ```
    *   **POM.XML 文件 - Tomcat 容器依赖**:
        ```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-tomcat</artifactId>
        </dependency>
        ```
    *   **父级 POM.XML 文件 - 版本属性配置**:
        ```xml
        <properties>
            <spring-cloud-starter.version>2.1.1.RELEASE</spring-cloud-starter.version>
            <druid.version>1.1.18</druid.version>
            <project.stock.version>1.0.0</project.stock.version>
        </properties>
        ```
    *   **TradeAuthApplication 启动类**:
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        @ComponentScan(basePackages = {"com.itcast"})
        @EntityScan(basePackages = {"com.itcast"})
        @EnableJpaRepositories(basePackages = {"com.itcast"})
        @EnableCaching
        public class TradeAuthApplication {
            public static void main(String[] args) {
                SpringApplication.run(TradeAuthApplication.class, args);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示**。讲师在 Typora 中展示 `stock-common` 模块的目录结构，强调其作为公用组件的作用。
*   **场景二：认证服务工程结构**。讲师在 IDEA 中展示 `trade-auth` 项目的目录结构，包括 `src/main/java` 和 `src/main/resources`。
*   **场景三：依赖配置演示**。讲师在 IDEA 中打开 `pom.xml` 文件，逐行讲解并高亮显示了 OAuth2、Spring Security、Web 和 Tomcat 的依赖配置。
*   **场景四：启动类代码演示**。讲师在 IDEA 中展示 `TradeAuthApplication` 启动类的代码，重点讲解了 `@SpringBootApplication`、`@EnableDiscoveryClient`、`@ComponentScan`、`@EntityScan` 和 `@EnableJpaRepositories` 等注解的作用。
*   **场景五：数据层设计演示**。讲师在 Typora 中讲解了 JPA 实体类的注解要求，并展示了 `TradeUserRepository` 接口的注释和定义。
