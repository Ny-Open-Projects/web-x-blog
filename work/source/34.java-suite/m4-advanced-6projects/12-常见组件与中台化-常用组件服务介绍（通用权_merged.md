# 12-常见组件与中台化-常用组件服务介绍（通用权 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看我们这个通用权限系统介绍,刚才呢,我们是演示了一下,如何把我们这个通用权限系统是不是把它运行起来,然后接下来呢,我们就来看一下如何使用我们这个通用权限系统,咱们是分成这么两个方面,一个是作为新项目开发,在这种情况下,我们如何使用通用权限系统,还有就是什么呢,我已经有了项目了,对吧,已有的项目如何集成,

好,咱们先来看,作为新项目开发,作为新项目开发的话呢,那其实相对来说比较简单,就是什么呢,我们直接在我们当前这个Maven工程的基础之上来进行开发,也就是把我们这个通用权限系统把它当成一个开发的交手架,对吧,然后在它的基础之上来开发我们相应的业务功能就可以了,这是比较简单的一种开发方式,

好,接下来呢,我们先把这个服务呢给停掉,因为我们要开发代码,所以先把服务给停掉,停掉之后呢,咱们这个地方呢,我就不再去手敲了,然后呢,我们这些操作呢,我直接从讲义上来复制,因为重点不在于怎么去这个操作,怎么去这个敲代码,而是什么呢,给大家演示一下,如果是新项目开发,大概是一个什么样的处理流程,在大家注意看这些关键点,对吧,那么需要我们做哪些事情,好,

好,比如说呢,我们在这儿呢,我就开发一个商品管理,对吧,当然这个就简单来一个增伤改查就可以了,因为我们重点呢,还不是真的去开发这个服务,而是为大家演示一下,如何基于通用权益系统来开发新业务,对吧,所以我们就以商品服务为例啊,给大家来演示一下,而我这个商品呢,很显然它可能也是需要有自己的数据库的,对吧,所以我们在这儿呢,就来创建一个数据库,比如说就叫PD Goose,

然后呢,

在数据库里面来创建这么一张表,叫做PD Goose Info,对吧,具体这个表的结构呢,就是这么一个结构,大家按照这个结构来创建就可以了,好,这一步呢,就是创建数据库环境,好,这一步呢,我就不再具体去操作了,咱们直接来看一下就可以了,因为我这儿呢,其实已经创建好了,所以你在你本地呢,来创建这个数据库就可以了,你看我在这儿已经创建好了,叫做PD什么呢,

Goose,

然后在这个库里面呢,创建了这么一张表,这个Andlog,大家可以忽略它,不用它,然后呢,我们直接用这个,叫做PD Goose Info,对吧,这个叫做商品信息表,商品信息表,然后这里边呢,有这么一些字段,按照要求,跟我们这个保持一致,大家可以自行来创建一下,好,这是把这个数据库还有表是不是创建出来,创建出来之后呢,我们就可以在我们这个通用权限系统的基础之上来创建我们这个商品信息表,好,

好,

放进来一个model,对吧,

好,

直接next,

咱们这个呢,就叫PD Goose,

商品,

然后next,

就一样,把这个横线给它加上,

这个地方呢,应该是放在哪呢,放在我们这个PD App下边,好,所以这个路径呢,给它检查一下,应该没啥问题,然后呢,我们直接完成,好,那这样的话,我们这个PD Goose是不是就已经创建了,好,

好,

创建好了之后还需要在它下面来创建两个子模块

一个叫做PDGooseEntity

咱们先来创建一下

New一个Model叫做PDGooseEntity

它是在哪呢

就在我们这个PDGoose下面

这个层次关系我们就按这个来完成

这是我们的实体这个模块

然后我们再来创建一个什么呢

PDGooseServer

作为我们这个商品服务

所以还是选中它

然后来New一个Model

新的一个Maven模块

Next

同样是在这个PDGoose下面来创建

所以这个目录层次就是这样的

这样的话我们把这三个Maven工程是不是都创建好了

当然严格来说应该叫做Maven模块

它是Model

然后创建好之后我们来看

需要进行相应的配置

比如说我在这个PDGooseEntity里边需要来导入什么呢

导入一些这个坐标

导入一些坐标

然后我们就把这个Dependency这块拿过来就行了

因为其他的这些地方呢

咱们应该是自动就已经生成了

Entity这边你看它就已经弄好了

所以我们直接把这块给它补全

PDTools Common

还有这个什么呢

这其实是SWAG文档

所以依赖的这个

就是MyBed Plus

把这块呢

给它完善好

然后呢

我们在这里边呢

来创建一个什么呢

商品实体类对吧

商品实体类

这个呢

我就不去敲了

咱们直接来复制进来就可以了

叫做GooseInfo

先把这个包来创建一下吧

这个包比较深

很显然应该是在我们这个Entity这个模块里面是不是来创建这个包结构

好

我们在这儿来创建这个包结构

然后呢

在这个包里边来创建什么呢

创建咱们这个GooseInfo

创建咱们这个GooseInfo

这是我们这个实体类

来一个类

这个类呢

我也不敲了

直接啊

把整个代码拿过来

好

整个覆盖一下就可以了

然后呢

我们可以来看一下

它这边呢

是不是通过这个TableName对吧

进行了一个映射

它映射的呢

就是我们刚才看见的这个PDGooseInfo

也就是我们这个什么呢

商品这张表对吧

包括这里边这些属性呢

跟字段呢

都是对应好的

大家直接照着我们讲页上来操作就可以了

这个提前都是整理好的

好

然后接下来呢

我们再来创建一个什么呢

DTO啊

数据传输对象对吧

在我们进行这个接口调用的时候呢

会使用到这个传输对象

先把这个包结构呢

给它来创建一下

DTO

然后呢

我们这个就叫做什么

GooseInfoPageDTO

好

是这么一个

数据传输对象

好

然后呢

具体这里边这个代码呢

我们就直接把它拿过来

然后呢

你看这个DTO呢

它其实继承了这个GooseInfo

然后呢

又扩展出来了自己这么两个属性

对吧

都是时间

好

然后接下来呢

是不是

再来创建这么几个啊

一个叫做GooseInfoSave

也就是我们保存的时候呢

通过这个对象来传输

还有更新的时候呢

通过这个对象来传输

对吧

这是各种各样的DTO

也就是我们分的呢

其实呢

其实还是比较细的

它其实是直接继承了什么呢

直接继承了我们这个GooseInfo

这样的话

我们这个分类呢

就非常明确了

对吧

那么传输的时候呢

我们就使用DTO对象来传输

更新的时候呢

也是使用这个DTO对象

直接把讲义上这个抄过来

它其实直接继承了它就可以

继承我们这个实体类

直接来引入一下

OK

按照我们讲义上来操作一下就可以了

到这儿的话呢

我们这个什么呢

Entity

也就是我们创建的GooseEntity

这个实体模块呢

就已经搞定了

一会儿呢

我们再来开发一下什么呢

咱们这个PDGooseServer

当然这个地方呢

也是啊

我们不再去手敲代码

直接从我们讲义上

把代码拷过来就可以了

一会儿呢

我们再来操作这个PDGooseServer

这个模块

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于“常见组件与中台化”系列教程的一部分，具体聚焦于“2.1.4 使用说明”下的“2.1.4.1 新项目开发”子章节。课程内容旨在指导开发者如何基于一个已有的“品达通用权限系统”快速搭建和开发新的业务模块，以实现中台化架构。讲师通过一个“商品服务”的案例，演示了从环境搭建、数据库建模、创建实体类和DTO类等基础开发步骤。整个过程使用了 IntelliJ IDEA、Navicat Premium 和 Typora 等开发工具，并涉及 Spring Boot、MyBatis-Plus、Nacos 等主流技术栈。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: **课程引入与项目背景**
    *   展示了项目结构 `pinda-authority`，并强调本节将基于此通用权限系统进行新业务开发。
*   **00:05 - 00:15**: **环境搭建与配置中心**
    *   展示了 `application-dev.properties` 和 `application-test.properties` 文件，详细说明了如何通过 Nacos 配置中心为不同环境（开发、测试）配置数据库地址和命名空间。
*   **00:15 - 00:25**: **数据库环境搭建**
    *   在 Navicat Premium 中展示了 `pd_goods` 数据库的表结构设计，重点是 `pd_goods_info` 表，包含了商品名称、条码、品牌、分类等字段。
*   **00:25 - 00:35**: **创建新项目**
    *   在 IntelliJ IDEA 中演示了使用 Spring Initializr 创建新模块 `pd-goods`，并配置了 Maven 依赖。
*   **00:35 - 00:45**: **项目结构与 POM 文件**
    *   展示了 `pd-goods` 模块的 `pom.xml` 文件，明确了其父项目为 `pinda-authority`，并配置了 `1.0.0-SNAPSHOT` 版本。
*   **00:45 - 00:55**: **创建实体类 (Entity)**
    *   在 `GoodsInfo.java` 文件中，定义了商品实体类，使用了 `@TableName` 注解指定数据库表名，并包含了 `name`, `barCode`, `brandId` 等字段。
*   **00:55 - 01:05**: **创建 DTO 类**
    *   在 `GoodsInfoSaveDTO.java` 文件中，定义了用于数据传输的 DTO 类，它继承自 `GoodsInfo`，用于封装商品保存时的请求数据。
*   **01:05 - 01:15**: **多窗口开发环境展示**
    *   展示了多窗口并行开发的场景，包括 IDEA、Navicat、Typora 和 Chrome 浏览器，体现了现代开发中多工具协同工作的模式。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: `2.1.4 使用说明` -> `2.1.4.1 新项目开发` -> `2.1.4.1.2 后端业务功能开发`。
    *   **核心概念**: “基于通用权限系统快速开发新业务”。
    *   **数据库表**: `pd_goods_info`，字段包括 `code`, `name`, `bar_code`, `brand_id`, `one_category_id`, `price`, `average_cost` 等。
    *   **配置中心**: `Nacos`，用于管理不同环境（`dev`, `test`）的配置，如数据库 IP、端口、命名空间。

*   **代码关键内容**:
    *   **Nacos 配置文件 (`application-dev.properties`)**:
        ```properties
        # 当前环境
        <profile>dev</profile>
        # Nacos 配置中心地址
        <pom.nacos.ip>127.0.0.1</pom.nacos.ip>
        <pom.nacos.port>8848</pom.nacos.port>
        # Nacos 命名空间（必须使用 ID，不能使用名称）
        <pom.nacos.namespace>301c574e-a440-42c4-b717-d3379057f6a4</pom.nacos.namespace>
        ```
    *   **实体类代码 (`GoodsInfo.java`)**:
        ```java
        package com.ithema.pinda_goods.entity;
        import com.baomidou.mybatisplus.annotation.TableName;
        import com.ithema.pinda_base.entity.Entity;
        import lombok.*;
        import java.time.LocalDateTime;

        @Data
        @AllArgsConstructor
        @NoArgsConstructor
        @ToString(callSuper = true)
        @EqualsAndHashCode(callSuper = true)
        @TableName("pd_goods_info")
        public class GoodsInfo {
            private String name;
            private String barCode;
            private Integer brandId;
            private Integer oneCategoryId;
            private Integer twoCategoryId;
            private Integer threeCategoryId;
            private BigDecimal price;
            private BigDecimal averageCost;
            private LocalDateTime productionDate;
            private Integer shelfLife;
            private String descrip;
        }
        ```
    *   **DTO 类代码 (`GoodsInfoSaveDTO.java`)**:
        ```java
        package com.ithema.pinda_goods.dto;
        import com.ithema.pinda_goods.entity.GoodsInfo;
        import lombok.*;
        import java.time.LocalDateTime;

        @Data
        @AllArgsConstructor
        @NoArgsConstructor
        @ToString(callSuper = true)
        @EqualsAndHashCode(callSuper = true)
        public class GoodsInfoSaveDTO extends GoodsInfo {
            // 可以在此添加仅用于 DTO 的字段，如创建时间等
        }
        ```
    *   **POM 文件 (`pom.xml`)**:
        ```xml
        <parent>
            <artifactId>pinda-authority</artifactId>
            <groupId>com.ithema</groupId>
            <version>1.0.0</version>
        </parent>
        <modelVersion>4.0.0</modelVersion>
        <artifactId>pd-goods</artifactId>
        <description>接口服务实体块</description>
        <dependencies>
            <dependency>
                <groupId>io.springfox</groupId>
                <artifactId>springfox-core</artifactId>
            </dependency>
            <dependency>
                <groupId>com.baomidou</groupId>
                <artifactId>mybatis-plus</artifactId>
            </dependency>
        </dependencies>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境配置与 Nacos 配置中心**
    *   **描述**: 讲师在 IDEA 中打开 `application-dev.properties` 文件，详细讲解了如何通过 Nacos 配置中心为开发环境配置数据库连接信息。重点强调了 `pom.nacos.ip`、`pom.nacos.port` 和 `pom.nacos.namespace` 等关键配置项，并指出命名空间必须使用 ID，不能使用名称。

*   **场景二：数据库建模与表结构设计**
    *   **描述**: 讲师切换到 Navicat Premium，展示了 `pd_goods` 数据库的表结构设计。通过 `Table Design` 界面，清晰地展示了 `pd_goods_info` 表的字段及其数据类型，如 `name` (varchar)、`price` (decimal)、`productionDate` (datetime) 等，为后续的实体类开发提供了数据模型依据。

*   **场景三：创建新项目与依赖管理**
    *   **描述**: 讲师在 IDEA 中使用 Spring Initializr 创建新模块 `pd-goods`，并配置了 Maven 依赖。通过 `pom.xml` 文件，展示了如何继承父项目 `pinda-authority`，并引入 `springfox-core` 和 `mybatis-plus` 等核心依赖，为项目打下基础。

*   **场景四：实体类与 DTO 类开发**
    *   **描述**: 讲师在 IDEA 中创建了 `GoodsInfo.java` 实体类，使用 `@TableName` 注解指定数据库表名，并定义了商品相关的字段。随后，创建了 `GoodsInfoSaveDTO.java` 类，使其继承自 `GoodsInfo`，用于封装前端传来的商品保存数据，体现了面向对象和数据传输分层的设计思想。

*   **场景五：多窗口并行开发**
    *   **描述**: 讲师展示了在开发过程中，如何同时打开多个窗口，如 IDEA（代码编辑）、Navicat（数据库管理）、Typora（文档编写）和 Chrome（查看文档或接口文档）。这种多窗口并行开发模式，极大地提高了开发效率，是现代软件开发的常见实践。
