# 22-简易下单功能-交易服务Mybatis双数据源配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始学习交易服务MyBetis双数据源方案的集成实现

前面的课程当中咱们讲过基于JPA的双数据源方案

在这里我们是采用MyBetis双数据源方案

去实现交易服务的数据神接口的操作

因为交易服务的逻辑不是单纯的增上改查

同时要求有较高的处理性能

MyBetis是一个轻量级的OM框架

在数据处理方面没有过度的封装

所以它整体性能有着较好的表现

接着咱们就来实现多数据源的配置

首先咱们要创建Druid System Data Source

它的数据源配置

回到咱们的代码当中

在Configure目录下面创建一个新的class

删贴进去

这个和之前咱们在行情服务当中

所实现的Druid的数据源

基本上都是没什么差别

咱们可以从代码当中Copy进来

将包导入进去

一个是交易数据源的配置

一个是用于业务数据源

接着咱们对这两个业务数据源做具体实现

回到咱们讲义当中

首先咱们去实现交易数据源的配置

之前做JPA讲解的时候也已经做过介绍

在这里咱们就不再逐行去敲起代码

侧重来讲解它们的实现流程

以及这两者的主要区别

首先咱们创建ChadSystems

ChadSourceConfiguration

NewClass

将代码Copy进来

将相关包导入进去

ChadSource导入进来

咱们重新打开

这个的话并不是代码错误

可以暂时不用去管

咱们看一下它这一块的具体处理流程是怎样的

首先它要加上Configuration注写

然后定义Mapskin

Mapskin是扫描MyBadge的数据层接口

这里咱们要做个替换

Copy

然后这里要去注入CircleSessionTemplate

Circle绘画的操作模板

这个是指向咱们下面的配置

可以看到

ChadSystems Circle Session Template

它会去创建一个新的Circle Session Template

大家注意它的创建是基于ChadSystems Circle Session Factory

咱们可以看到

在这里面定义了对应的

这个Session工厂咱们看一下是如何定义呢

它会去读取ChadSystems Data Source

这个也就是在上面Lui的数据源当中的配置

可以看到定义了交易数据源

那么在这里呢

咱们是要保持一致

然后将交易数据源设置进去

接着呢就要去指定MapResource的支援路径

也就是Map文件的路径信息

在这里咱们要去定义了

做个修改

com.idcast

buzz

确保Map的路径是正确的

上面也有一个路径的配置

这个路径是扫描数据层接口

也就是DAO

下面这个路径就是扫描Map文件

这两者是有区别的

接下来还要去定义Transaction Manager

也就是事务管理器

同样它也要将交易数据源注入进来

最后在交易服务当中

交易数据源是作为主数据源

所以在这里呢

都要加上Primary的读解

作为默认的首选项

这个呢就是交易数据源的具体定义

JPA的属性呢

这里可以不需要

Habitator的话呢也不需要

这些都不需要

接下来咱们再去定义业务数据源

回到讲义当中

创建业务数据源的配置内

New Class

那从讲义当中

咱们再将它copy进来

copy进来之后

先将这些包导入进去

然后加Data Source

包导入进来

这个配置和刚才所讲解的交易数据源配置呢

也基本上是一样的

咱们也将它的路径呢

做个替换

确保这些名称呢

不要产生冲突

大家可以查找检索匹配下

看一下是否存在问题

然后这个呢是Map的文件路径

这个路径呢

咱们是Bus

在这里要做个调整

业务数据源呢

就已经配置完成

接着咱们还去配置文件当中呢

去实现双数据源的配置

打开咱们的工程配置文件

在这里呢

咱们已经配置上了交易数据源

以及呢

业务数据源

这两项配置呢

咱们之前也做过讲解

和JPA的双数据源配置呢

也都是一样的

不需要做任何的调整

区别呢

主要是在于配置内的实现

MyBedis和JPA双数据源配置处理流程呢

基本上是一样的

不同的呢

是他们的细节上的差异

比如说包的扫描路径

Mapscan呢

在这里他要扫描MyBedis的数据层接口

而且呢

还要在这里去配置MyBedis的Map文件

JPA的话呢

只需要配置DAO

也就是Libscytl的路径就可以了

这些细节上的距离差异

大家可以去对比行情服务里面

JPA双数据源的配置

好

咱们回到讲义当中

这一讲

咱们就实现了交易服务

MyBedis双数据源方案的集成配置

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析报告：

---

### 1) 视频摘要

本视频片段是关于“交易服务 MyBatis 双数据源方案实现”的教学内容。讲师旨在指导学员如何在 Spring Boot 项目中，为交易服务配置两个独立的数据库连接（业务数据库和交易数据库），并使用 MyBatis 框架分别管理它们。核心内容包括创建两个数据源配置类（`DruidSystemDataSourceConfiguration` 和 `TradeSystemDataSourceConfiguration`），配置对应的 `SqlSessionFactory`、`TransactionManager` 和 `SqlSessionTemplate`，并使用 `@Qualifier` 注解来区分不同数据源。视频中也展示了如何在 `application.yml` 配置文件中定义两个数据源的连接信息，并通过 `@MapperScan` 注解指定不同的 Mapper 扫描路径。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 文档中定位到本节内容“3.9 交易服务 MyBatis 双数据源方案实现”，并简要说明本节将采用 MyBatis 方案，而非之前的 JPA 方案。
*   **00:00:05 - 00:00:15**: 讲师开始讲解第一个步骤：“创建多数据源配置”，并展示 `DruidSystemDataSourceConfiguration` 类的代码框架。
*   **00:00:15 - 00:00:30**: 讲师在 `DruidSystemDataSourceConfiguration` 类中编写了业务数据源的配置方法，使用 `@ConfigurationProperties` 注解绑定 `spring.datasource.bizsystem` 配置项。
*   **00:00:30 - 00:00:45**: 讲师讲解交易数据源的配置，使用 `@Bean` 和 `@Primary` 注解，并绑定 `spring.datasource.tradesystem` 配置项。
*   **00:00:45 - 00:01:00**: 讲师继续在 `DruidSystemDataSourceConfiguration` 类中配置 `SqlSessionTemplate` 和 `DataSourceTransactionManager`，并使用 `@Qualifier` 注解指定数据源。
*   **00:01:00 - 00:01:15**: 讲师切换到 `TradeSystemDataSourceConfiguration` 类，讲解其配置逻辑，包括 `SqlSessionFactory`、`TransactionManager` 和 `SqlSessionTemplate`。
*   **00:01:15 - 00:01:30**: 讲师在 `TradeSystemDataSourceConfiguration` 类中编写了 `SqlSessionFactory` 的配置代码，使用 `@Qualifier` 注解指定数据源。
*   **00:01:30 - 00:01:45**: 讲师继续在 `TradeSystemDataSourceConfiguration` 类中编写 `TransactionManager` 和 `SqlSessionTemplate` 的配置代码。
*   **00:01:45 - 00:02:00**: 讲师切换到 `BizSystemDataSourceConfiguration` 类，讲解其配置逻辑，包括 `SqlSessionFactory`、`TransactionManager` 和 `SqlSessionTemplate`。
*   **00:02:00 - 00:02:15**: 讲师在 `BizSystemDataSourceConfiguration` 类中编写了 `SqlSessionFactory` 的配置代码，使用 `@Qualifier` 注解指定数据源。
*   **00:02:15 - 00:02:30**: 讲师继续在 `BizSystemDataSourceConfiguration` 类中编写 `TransactionManager` 和 `SqlSessionTemplate` 的配置代码。
*   **00:02:30 - 00:02:45**: 讲师在 `application.yml` 配置文件中展示了如何配置两个数据源的连接信息，包括 `url`、`username`、`password` 和连接池参数。
*   **00:02:45 - 00:03:00**: 讲师在 Typora 文档中总结了本节内容，强调了 `@Primary` 注解的作用和 `@MapperScan` 注解的使用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: `3.9 交易服务 MyBatis 双数据源方案实现`
    *   **关键说明**: “前面课程讲过基于 JPA 的双数据源方案，这里我们采用 MyBatis 的双数据源方案，因为交易服务的逻辑不是单纯的增删改查，同时要求较高的处理性能。”
    *   **步骤说明**:
        1.  创建多数据源配置
        2.  交易数据源配置
        3.  业务数据源配置
    *   **关键注解说明**: `@Primary` 注解用于指定默认数据源，`@Qualifier` 注解用于区分不同数据源。

*   **代码关键内容**:

    **1. `DruidSystemDataSourceConfiguration` 类 (业务数据源配置)**

    ```java
    @Configuration
    public class DruidSystemDataSourceConfiguration {

        @Bean(name = "bizSystemDataSource")
        @ConfigurationProperties(prefix = "spring.datasource.bizsystem")
        public DataSource bizSystemDataSource() {
            return new DruidDataSource();
        }

        @Bean(name = "tradeSystemDataSource")
        @Primary
        @ConfigurationProperties(prefix = "spring.datasource.tradesystem")
        public DataSource tradeSystemDataSource() {
            return new DruidDataSource();
        }
    }
    ```

    **2. `TradeSystemDataSourceConfiguration` 类 (交易数据源配置)**

    ```java
    @Configuration
    @MapperScan(basePackages = "com.itcast.trade.stock.deal.dao.trade",
            sqlSessionTemplateRef = "tradeSystemSqlSessionTemplate")
    public class TradeSystemDataSourceConfiguration {

        @Bean(name = "tradeSystemSqlSessionFactory")
        @Primary
        @Qualifier("tradeSystemDataSource")
        public SqlSessionFactory tradeSystemSqlSessionFactory(@Qualifier("tradeSystemDataSource") DataSource dataSource) throws Exception {
            SqlSessionFactoryBean bean = new SqlSessionFactoryBean();
            bean.setDataSource(dataSource);
            bean.setMapperLocations(new PathMatchingResourcePatternResolver().getResources("classpath:/com/itcast/trade/stock/deal/mapper/*.xml"));
            return bean.getObject();
        }

        @Bean(name = "tradeSystemTransactionManager")
        @Primary
        @Qualifier("tradeSystemDataSource")
        public DataSourceTransactionManager tradeSystemTransactionManager(@Qualifier("tradeSystemDataSource") DataSource dataSource) {
            return new DataSourceTransactionManager(dataSource);
        }

        @Bean(name = "tradeSystemSqlSessionTemplate")
        @Primary
        @Qualifier("tradeSystemDataSource")
        public SqlSessionTemplate tradeSystemSqlSessionTemplate(@Qualifier("tradeSystemSqlSessionFactory") SqlSessionFactory sqlSessionFactory) {
            return new SqlSessionTemplate(sqlSessionFactory);
        }
    }
    ```

    **3. `BizSystemDataSourceConfiguration` 类 (业务数据源配置)**

    ```java
    @Configuration
    @MapperScan(basePackages = "com.itcast.trade.stock.deal.dao.biz",
            sqlSessionTemplateRef = "bizSystemSqlSessionTemplate")
    public class BizSystemDataSourceConfiguration {

        @Bean(name = "bizSystemSqlSessionFactory")
        @Primary
        @Qualifier("bizSystemDataSource")
        public SqlSessionFactory bizSystemSqlSessionFactory(@Qualifier("bizSystemDataSource") DataSource dataSource) throws Exception {
            SqlSessionFactoryBean bean = new SqlSessionFactoryBean();
            bean.setDataSource(dataSource);
            bean.setMapperLocations(new PathMatchingResourcePatternResolver().getResources("classpath:/com/itcast/trade/stock/deal/mapper/*.xml"));
            return bean.getObject();
        }

        @Bean(name = "bizSystemTransactionManager")
        @Primary
        @Qualifier("bizSystemDataSource")
        public DataSourceTransactionManager bizSystemTransactionManager(@Qualifier("bizSystemDataSource") DataSource dataSource) {
            return new DataSourceTransactionManager(dataSource);
        }

        @Bean(name = "bizSystemSqlSessionTemplate")
        @Primary
        @Qualifier("bizSystemDataSource")
        public SqlSessionTemplate bizSystemSqlSessionTemplate(@Qualifier("bizSystemSqlSessionFactory") SqlSessionFactory sqlSessionFactory) {
            return new SqlSessionTemplate(sqlSessionFactory);
        }
    }
    ```

    **4. `application.yml` 配置文件 (数据源配置)**

    ```yaml
    datasource:
      tradesystem:
        type: com.alibaba.druid.pool.DruidDataSource
        driver-class-name: org.postgresql.Driver
        username: office
        password: 654321
        url: jdbc:postgresql://192.168.19.150:5432/trade_stock
        druid:
          # 连接池的配置信息
          initial-size: 5
          min-idle: 5
          max-active: 20
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 项目结构与配置文件展示**
    *   讲师首先展示了项目结构，包括 `bulls-stock-deal` 项目下的 `src/main/java` 和 `src/main/resources` 目录。
    *   讲师在 `resources` 目录下打开了
