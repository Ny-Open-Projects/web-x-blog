# 14-SEATA集成运用-挂单服务集成配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来咱们接着去改造挂单服务

让它集成支持SATA主线

回到工程当中

我们先将SATA的配置文件信息做一个copy

把它放在挂单服务的资源目录下面

Resource

三点进去

一个是Registry Configure

一个是File Configure

这里面的内容都已经配置好

咱们不需要做任何调整

直接copy引入进来就可以

接着要检查挂单服务的Home文件依赖

是否增加了SATA的主线

好 在这里并没有

我们去copy过来

在旧从资金服务里面

将SATA的主线复制

把它放在Pending的Home文件下面

让它导入生效

导入完成之后

接着我们去增加SATA的配置类

选中SATA Configuration

把它放在

Pending的Configure包下面

同样这里也不需要做任何调整

接着的话我们就去修改

数据源的集成配置

在这里我们也去增加SATA的

代理数据源配置信息

咱们就从资金服务当中

引用进来

放在Glue的System Data Source Configuration下面

确保业务数据源名称是正确的

好

接着的话我们就去修改业务数据源的配置

将BizSystemData Source配置到

BizSystemData Source做一个替换

改成BizProxyData Source

然后去修改TransactionManager里面的参数

将这个Data Source也改成SATA的代理数据源

好

那挂单服务的SATA集成配置就已经实现完成

整体实现比较简单

大家按讲义当中的步骤去实现就可以

好

这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于“分布式事务”技术栈的实战教学，主要演示如何在 Spring Boot 项目中集成 Seata 分布式事务管理器。课程内容围绕一个名为 `bulls-stock-pending` 的子项目展开，详细讲解了如何通过修改 `pom.xml` 文件添加 Seata 依赖，以及如何在配置类中定义数据源代理和事务管理器。视频通过 IntelliJ IDEA 开发环境，展示了从项目结构、依赖管理到核心配置类的编写过程，旨在帮助开发者快速搭建一个支持分布式事务的微服务架构。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 开场，展示项目结构，当前在 `bulls-stock-finance` 模块中，准备为 `bulls-stock-pending` 模块配置分布式事务。
*   **00:03 - 00:08**: 切换到 `bulls-stock-pending` 模块，展示其 `pom.xml` 文件，重点是添加 Seata 依赖。
*   **00:08 - 00:14**: 在 `pom.xml` 中添加 Seata 的 Maven 依赖，`groupId` 为 `io.seata`，`artifactId` 为 `seata-all`。
*   **00:14 - 00:20**: 展示 `bulls-stock-pending` 模块的 `src/main/java` 目录结构，准备创建新的配置类。
*   **00:20 - 00:25**: 从 `bulls-stock-finance` 模块中复制 `SeataConfiguration` 类，粘贴到 `bulls-stock-pending` 模块中。
*   **00:25 - 00:30**: 在 `bulls-stock-pending` 模块的 `config` 包下创建 `SeataConfiguration` 类。
*   **00:30 - 00:35**: 在 `SeataConfiguration` 类中，定义 `bizSystemDataSource` 和 `tradeSystemDataSource` 两个数据源。
*   **00:35 - 00:40**: 定义 `bizProxyDataSource`，它是一个 `DataSourceProxy`，用于代理 `bizSystemDataSource`。
*   **00:40 - 00:45**: 定义 `bizSystemTransactionManager`，它是一个 `PlatformTransactionManager`，用于管理事务。
*   **00:45 - 00:50**: 定义 `bizSystemSqlSessionFactory`，它是一个 `SqlSessionFactory`，用于创建 SQL 会话。
*   **00:50 - 00:55**: 定义 `bizSystemSqlSessionTemplate`，它是一个 `SqlSessionTemplate`，用于执行 SQL 操作。
*   **00:55 - 01:00**: 总结，强调通过以上配置，`bulls-stock-pending` 模块现在支持了 Seata 分布式事务。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **目标**: 配置分布式事务。
    *   **步骤**: 1. 工程配置修改；2. 依赖支持；3. 增加配置类。
    *   **依赖支持**: 修改 `pom.xml`，增加 Seata 依赖。
    *   **增加配置类**: 新增 `com.ictast.trade.stock.deal.config.SeataConfiguration`，直接从交易服务中复制，无需修改。

*   **代码关键内容**:
    *   **Maven 依赖 (pom.xml)**:
        ```xml
        <!-- Seata 分布式事务依赖 -->
        <dependency>
            <groupId>io.seata</groupId>
            <artifactId>seata-all</artifactId>
            <version>${seata.version}</version>
        </dependency>
        ```
    *   **配置类 (SeataConfiguration.java)**:
        ```java
        @Configuration
        public class SeataConfiguration {
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

            @Bean("bizProxyDataSource")
            public DataSourceProxy bizProxyDataSource(@Qualifier("bizSystemDataSource") DataSource bizSystemDataSource) {
                return new DataSourceProxy(bizSystemDataSource);
            }

            @Bean("bizSystemTransactionManager")
            @Primary
            @Transactional
            public PlatformTransactionManager bizSystemTransactionManager(@Qualifier("bizProxyDataSource") DataSource dataSource) {
                return new DataSourceTransactionManager(dataSource);
            }

            @Bean("bizSystemSqlSessionFactory")
            @Primary
            public SqlSessionFactory bizSystemSqlSessionFactory(@Qualifier("bizSystemTransactionManager") PlatformTransactionManager transactionManager,
                                                               @Qualifier("bizSystemDataSource") DataSource dataSource) throws Exception {
                return new SqlSessionFactoryBean().setDataSource(dataSource).build();
            }

            @Bean("bizSystemSqlSessionTemplate")
            @Primary
            public SqlSessionTemplate bizSystemSqlSessionTemplate(@Qualifier("bizSystemSqlSessionFactory") SqlSessionFactory sqlSessionFactory) {
                return new SqlSessionTemplate(sqlSessionFactory);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与依赖管理**
    *   **描述**: 视频首先展示了 `bulls-stock-finance` 和 `bulls-stock-pending` 两个模块的项目结构。通过在 `bulls-stock-pending` 模块的 `pom.xml` 文件中添加 Seata 依赖，为后续的分布式事务配置做准备。

*   **场景二：配置类的创建与复制**
    *   **描述**: 在 `bulls-stock-pending` 模块中，通过 IntelliJ IDEA 的“复制类”功能，将 `bulls-stock-finance` 模块中的 `SeataConfiguration` 类复制到 `bulls-stock-pending` 模块的 `config` 包下。这一步骤是为了快速搭建一个与交易服务一致的分布式事务配置。

*   **场景三：数据源与事务管理器的配置**
    *   **描述**: 在 `SeataConfiguration` 类中，通过 `@Bean` 注解定义了多个数据源和事务管理器。其中，`bizSystemDataSource` 和 `tradeSystemDataSource` 是两个不同的数据源，`bizProxyDataSource` 是一个代理数据源，用于在 Seata 中管理事务。`bizSystemTransactionManager` 是一个事务管理器，用于管理事务的提交和回滚。`bizSystemSqlSessionFactory` 和 `bizSystemSqlSessionTemplate` 是用于创建和执行 SQL 会话的工厂和模板。

*   **场景四：配置类的最终效果**
    *   **描述**: 视频最后展示了 `SeataConfiguration` 类的完整代码，强调了通过这些配置，`bulls-stock-pending` 模块现在可以支持 Seata 分布式事务，从而实现跨服务的数据一致性。
