# 11-第三方行情源-交易数据源配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们开始实现GPA的多数据源配置

咱们知道行情表是在交易数据库当中

交易数据库采用的是PostgreSQL

产品和配置表则是放在业务数据库当中

这个是存储在MirrorDB下面

从行情服务的揭露逻辑

数据层它是用到了两个库的数据表

因为它要去加工行情K线数据

另外要去读取行情的产品配置

那么如何去实现GPA的多数据源配置呢

其实有比较多的方案

比较简单的一点是可以采用国内开源的爆米豆

多数据源的主线

这个代码清路性比较低

配置来讲也比较简单

使用比较方便

因为它做了深度的封装

这个是它的原码地址

大家有兴趣可以从中去学习和了解下

但是在这里面

我们使用较为复杂的原始配置

原始配置相比封装的组件

可能会更为复杂一点

但是这样呢

可以让大家更深入的去了解了

多数据源是如何配置

如何去实现的

好

接下来咱们就从代码当中去做具体的实现

打开咱们的代码工程

找到BuzzTalk Code行情服务

我们之前呢

已经搭建和配置好

接着的话呢

我们要去创建对应的包

New Package

这个包名呢

叫ComIDCast

点BuzzTalk

Port

这个是它的一个配置类的实现

咱们给它一个Configure配置包

然后还有其他的一些包

咱们也一并做个实现

CD返回上一层

咱们创建了M2

这个呢

是需要用到的

LockitMQ服务的

然后还有它的数据层

Diffusitly

然后呢

服务层

这个是少不了的

然后呢

是数据源

因为这个要和第三方聚合数据源平台

做一个对接

最后呢

就是它的启动内的包

创建完成之后

咱们刷新下

可以看到的包都已经创建完成

首先咱们要实现JPA多数据源的配置

那么咱们呢

先创建Glue的连接子配置

给它一个名称

叫做LuidSystemDataSourceConfiguration

点击OK

给它加上附件

作为一个配置类

然后下面呢

我们要去配置它的DataSource

因为是有两个数据源

对不对

一个呢

是业务数据源

所以我们要定义一个DataSourceBusinessDataSource

这个呢

就直接Return New

然后咱们是采用Glue1的去实现

所以呢

要将它的数据源呢

创建下

另外一个呢

是交易的数据源

咱们也采用同样的方式

CAD SystemDataSource

咱们给它创建一个新的对象

GlueDataSource

创建完成之后

加上对应的注解以及注释说明

这个是业务数据源

要加上一个注解

它作为一个并对象

注入到视频容器当中

名称呢

我们就叫它copy一下

保持一致

然后呢

它要去读取我们配置文件当中所定义的属性

那么在这里呢

也要通过这个注解做对应的实现

我们也给它一个属性的前缀

统一叫SpinDataSource

然后呢是Bit System

因为另外呢

还会有一个交易的数据源配置

对不对

那咱们呢

让它copy过来

在这里面我们要做一个区分

它就采用CEDSystem

同样的这个bin注解呢

也要扩大进来

名称注意要改变

加上注释说明

它是交易数据源

那么我们还要再加上一个注解

这个注解呢

是要标识你的默认的数据源

微模类

因为咱们后面还需要实现数据层的接口

如果不指定默认的数据源

这个时候呢

数据层接口

它并不知道

先采用哪个数据源

所以呢

咱们要给它加上一个注解

Limit

也就是默认的话呢

优先会查找该数据源进行了数据的操作

这一块呢

就是Druid数据源连接池的配置实现

接着呢

咱们就要去创建了交易数据库的具体配置

回到讲义当中

这块呢

咱们已经创建完成

然后这些注意点呢

刚才也做了说明

下面呢

咱们就要去创建交易数据库的配置

交易数据库里面呢

还要去配置它的扫描信息

JPA的配置信息

像NtManage

然后那个事务管理器

创建完交易数据库的配置之后

还要去创建业务数据源的配置

那咱们就从代码当中做个实现

六,创建一个新的配置类

名称的话呢

叫TradeSystemDataSource

Configuration

首先咱们加上数解

一个是Configuration

接着的话呢

因为咱们是通过JPA实现的

所以呢

我们要开启JPA的事务管理器

Enable JPA的数据层扫描信息

LibreSatalyst

这里要扫描它的数据层接口

要将数据层的路径配置进去

我们就从代码中先copy进来

除了这个LibreSatalyst的奥明的配置呢

还有实体管理器以及事务管理器的配置

这两个呢

咱们在下面代码当中呢

就会做具体的实现

咱们可以先把它的名称先配置进去

这个路径呢

咱们要修改一下

因为路径已经发生了调整

我们要创建两个子宝

Open in Terminal

一个是Biz

这个呢

是业务数据源

还有一个是Chad交易数据源

那咱们将路径修改一下

Copy Deflux

这个不要搞错了

它是交易数据源配置

所以呢

要扫描交易的数据路径

接下来咱们就看一下交易数据源的配置该怎么去实现了

首先咱们要去定一个Applet

Properties

因为JPA的它其实就是基于Applet实现了

让它注入进来

off-wide

然后呢

咱们还定一个JPA的Properties

也要将它注入进来

注入完成之后

接着就要注入咱们刚才所配置的Glue的数据源

Credit System

Data Source

off-wide

这里我们采用别名方式

第一个图件

注意这个名称不能配置错误

咱们还是从这里面copy进来

在Deluid配置内当中

我们找到交易数据源

配置完成之后

接着我们就要配置

EntityManager

Public

Docu

Container

AntiManager

AntiManager Backup Bin

这个呢是交易的AntiManager

它的一个参数

AntiManager

Fatulate

Builder

将Builder作为参数

然后Return

Builder.

这个名称呢

咱们要保持一致

然后是Data Source

将交易的数据源注入进来

接着System

Data Source

就是这上面所定义的

然后Properties

这里面的Properties呢

咱们还去定义一个方法

Private Map String Object

Get Render Properties

将Data Source注入进去

Map导入下

Return

这个作用呢

是读取AppNet的数据配置信息

比如说AppNet

它会映射不同的数据库

然后不同的数据库呢

它有不同的一些语法

这些的话呢

就叫做方言

所以在这里呢

咱们要加上相应的配置

配置完成之后呢

咱们就将它的属性呢

设置进去

Data Source

这个Data Source呢

就是Shared System Data Source

然后呢

我们要定义它的实体的上面路径

实体呢

就在咱们的Stock Anti功能下面

将这个路径Copy出来

接着还要去设置下

它的持续化单元

Positive Unit

这个单元名称呢

我们叫Shared Persistent Unit

最后呢

叫Build构建一下

这些信息配置完成之后呢

咱们还要去定义

它的Anti-Manager Fetching

然后它的名称是叫做

Shared Anti-Manager Fetching

将上面

Anti-Manager Fetching Build呢

作为参数

接着咱们就要创建它的对象

直接呢

从Anti-Manager Fetching的Bin当中呢

去获取Anti-Manager Fetching

Get Object

因为咱们呢

在上面做了一个配置

对不对

它就会将这里面的配置信息呢

输入进去

然后呢

返回出Anti-Manager Fetching的对象

这里就不需要Nu

它指向呢

就是刚才所定义的方法

为什么要配置Anti-Manager Fetching呢

咱们回到讲义当中

在这里我们来了解一下

Anti-Manager Fetching呢

它其实类似于

Hyphenated Session Fetching

也类似于呢

MyBetis的Circle Session Fetching

总之在执行操作之前呢

我们一定要获取一个Anti-Manager

这个呢是JPA所必须依赖的一个组件

这就类似于Hyphenated Session

好

咱们将它的注释呢

拷贝进来

最后呢

咱们还要去配置事务管理器

Platform

Consection

Manage

Cred

Consection

Manage

将Anti-Manager Fetching

Build了个位参数

然后Return NU

JPA

Consection Manage

将Cred

Anti

Manage

这个方法的返回结果呢

设置进去

这个呢就是配置了一个事务管理器

Name

将名称注入进去

加上对应的说明

配置事务管理器

这一块呢就是交易

它的数据源的具体配置

咱们将这个名称呢

这个前缀改成统一的Cred开头的

然后上面呢

Cred Anti-Manage Fetching

它指向的就是这个

我们所配置的方法

然后这个Cred Consection Manage呢

跟在这里面的配置并也是一致的

好

在这里呢咱们就完成了

JPA多数据源配置当中的

交易数据源的配置实现

那这一讲呢咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于在 Spring Boot 2.x 项目中实现 JPA 多数据源配置的教程。讲师旨在通过一个较为复杂的配置方案（基于 Druid + JPA），帮助学习者深入理解多数据源的底层原理和实现细节。视频内容主要围绕如何配置两个不同的数据源（一个用于业务数据库，一个用于交易数据库），并为每个数据源分别配置其对应的 `EntityManagerFactory` 和 `PlatformTransactionManager`，以实现独立的事务管理。讲师通过在 IDE 中逐步编写和修改配置代码，演示了如何使用 `@ConfigurationProperties` 注解、`@Qualifier` 注解、以及 `LocalContainerEntityManagerFactoryBean` 和 `PlatformTransactionManager` 等核心 Spring JPA 组件来完成配置。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:15**：开场，讲师在 PPT 上介绍本节内容，即“3.3 JPA多数据源配置”，并说明将采用基于 Druid + JPA + Spring Boot 2.x 的复杂方案。
*   **00:00:15 - 00:00:30**：讲师在 IDE 中打开 `DruidSystemDataSourceConfiguration.java` 文件，准备编写第一个数据源的配置。
*   **00:00:30 - 00:01:00**：讲师在 `DruidSystemDataSourceConfiguration` 类中，使用 `@ConfigurationProperties` 注解定义一个名为 `bizSystemDataSource` 的数据源 Bean，并演示了如何通过 `@Bean` 方法返回它。
*   **00:01:00 - 00:01:30**：讲师切换到 `TradeSystemDataSourceConfiguration.java` 文件，开始为交易系统配置第二个数据源。
*   **00:01:30 - 00:02:00**：讲师在 `TradeSystemDataSourceConfiguration` 中，使用 `@Qualifier` 注解为 `tradeSystemDataSource` 数据源指定一个别名，并创建了 `LocalContainerEntityManagerFactoryBean` 的 Bean。
*   **00:02:00 - 00:02:30**：讲师编写 `tradeEntityManagerFactoryBean` 的配置，通过 `EntityManagerFactoryBuilder` 来构建 `EntityManagerFactory`，并调用 `properties()` 方法传入数据源属性。
*   **00:02:30 - 00:03:00**：讲师继续编写 `tradeEntityManagerFactoryBean`，调用 `getVendorProperties` 方法获取数据库厂商特定的属性，并将其传递给 `EntityManagerFactoryBuilder`。
*   **00:03:00 - 00:03:30**：讲师在 `TradeSystemDataSourceConfiguration` 中，使用 `@EnableJpaRepositories` 注解配置 JPA 仓库，指定 `basePackages` 和 `entityManagerFactoryRef`。
*   **00:03:30 - 00:04:00**：讲师编写 `tradeTransactionManager` 的配置，使用 `@Bean` 注解创建一个 `PlatformTransactionManager` Bean，并将其与 `tradeEntityManagerFactoryBean` 关联。
*   **00:04:00 - 00:04:30**：讲师在 PPT 上总结，强调了 `EntityManagerFactory` 和 `PlatformTransactionManager` 在 JPA 多数据源配置中的核心作用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 关键内容**：
    *   **章节标题**：`3.3 JPA多数据源配置`。
    *   **核心概念**：`EntityManagerFactory` 类似于 Hibernate 的 `SessionFactory` 和 MyBatis 的 `SqlSessionFactory`。
    *   **配置目标**：为每个数据源配置独立的 `EntityManagerFactory` 和 `PlatformTransactionManager`。
    *   **代码结构**：展示了 `DruidSystemDataSourceConfiguration` 和 `TradeSystemDataSourceConfiguration` 两个配置类的结构。

*   **代码关键内容**：

    *   **`DruidSystemDataSourceConfiguration.java`**：
        ```java
        @Configuration
        public class DruidSystemDataSourceConfiguration {
            @Bean
            @ConfigurationProperties(prefix = "biz.datasource")
            public DataSource bizSystemDataSource() {
                // ... 配置代码
            }
        }
        ```

    *   **`TradeSystemDataSourceConfiguration.java`**：
        ```java
        @Configuration
        @EnableJpaRepositories(
            basePackages = "com.ictast.trade.quote.repository.biz",
            entityManagerFactoryRef = "bizEntityManagerFactory",
            transactionManagerRef = "bizTransactionManager"
        )
        public class TradeSystemDataSourceConfiguration {
            @Qualifier("tradeSystemDataSource")
            private DataSource tradeSystemDataSource;

            @Bean
            public LocalContainerEntityManagerFactoryBean tradeEntityManagerFactoryBean(EntityManagerFactoryBuilder builder) {
                return builder
                    .dataSource(tradeSystemDataSource)
                    .properties(getVendorProperties(tradeSystemDataSource))
                    .packages("com.ictast.trade.quote.entity")
                    .persistenceUnit("tradePersistentUnit")
                    .build();
            }

            @Bean
            public PlatformTransactionManager tradeTransactionManager(EntityManagerFactoryBuilder builder) {
                // ... 配置代码
            }
        }
        ```

    *   **`getVendorProperties` 方法**：
        ```java
        private Map<String, Object> getVendorProperties(DataSource dataSource) {
            return hibernateProperties.determineHibernateProperties(jpaProperties.getProperties(), new HibernateSettings());
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建第一个数据源配置**
    *   **描述**：讲师在 IDE 中打开 `DruidSystemDataSourceConfiguration.java` 文件，通过 `@ConfigurationProperties` 注解将 `biz.datasource` 配置属性绑定到 `DataSource` Bean 上，实现了第一个数据源的配置。

*   **场景二：配置第二个数据源**
    *   **描述**：讲师切换到 `TradeSystemDataSourceConfiguration.java` 文件，使用 `@Qualifier` 注解为 `tradeSystemDataSource` 数据源指定一个别名，并创建了 `LocalContainerEntityManagerFactoryBean` 的 Bean。

*   **场景三：配置 `EntityManagerFactory`**
    *   **描述**：讲师在 `TradeSystemDataSourceConfiguration` 中，通过 `EntityManagerFactoryBuilder` 构建 `EntityManagerFactory`，并调用 `properties()` 方法传入数据源属性，同时通过 `packages()` 方法指定实体类的包路径。

*   **场景四：配置 `PlatformTransactionManager`**
    *   **描述**：讲师在 `TradeSystemDataSourceConfiguration` 中，使用 `@EnableJpaRepositories` 注解配置 JPA 仓库，并创建了 `PlatformTransactionManager` Bean，将其与 `tradeEntityManagerFactoryBean` 关联，以实现独立的事务管理。

*   **场景五：总结与强调**
    *   **描述**：讲师在 PPT 上总结了本节内容，强调了 `EntityManagerFactory` 和 `PlatformTransactionManager` 在 JPA 多数据源配置中的核心作用，并指出通过这种方式可以实现对不同数据源的独立操作和事务管理。
