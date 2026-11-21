# 12-第三方行情源-业务数据源配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着的话咱们开始实现

业务数据员的配置

上一章节咱们实现了

交易数据员的配置

那么业务数据员跟交易数据员

配置其实基本上差不多

咱们回到代码当中

在这里面我们就直接copy

不再重新逐行去编写

节省下大家的时间

这个就叫做Bit System

和Chat System做个区分

copy完成之后

咱们要做相应的调整

首先的话是它的base package

也就是LibreCity数据层接口的路径

这个我们copy一下

改成业务数据的数据层路径

然后是实体管理器名称

改成Bit开头

事务管理器也是Bit开头

下面就要采用业务数据员

这个名称咱们做一个同名名

改成Bit

下面是实体Play所在的包路径

因为咱们行情服务

还有读取

产品信息的基本数据配置

所以咱们要指向股票产品实体的包路径

将它copy过来

下面持续化单元名称要做个调整

然后是Hypernet属性的配置

这里是采用默认的Hypernet的属性配置信息

咱们还加上一项配置

在这里面先将它的对象拿到

map

string

object

probes

拿到对象之后

咱们还去添加一个属性配置

这个就是Hypernet的方言

我们给它指定一下

因为咱们是采用的不同数据源

所以针对于不同数据的配置

咱们也要指定一下它的方言

Hypernet

Sally

因为咱们业务数据员采用的是MirrorDB

MirrorDB跟MySQL协议是一致的

所以在这里我们就采用MySQL的方言

DenoDB

然后将对象打回出去

For Ops

下面我们再检查一下

Anti-Managed Factors的配置

这个同样改成B字开头

然后下面是事务管理器

改成B字开头

刚才配置了MySQL的方言

接着的话我们还去修改交易数据源的配置

将它的方言信息改成PGSQL

我们来看一下

还是回到刚才的代码

我们直接将它拷贝过来

再做一个修改

这样比较快一点

这里只需要修改这个属性Hypernet

然后我们再去修改这个属性

Direct

将它改成Post-Reset

Direct

这样咱们就完成了业务数据源的配置

咱们回到讲义当中

在这里是可以参考交易数据源的配置信息

然后咱们做一个调整就可以

这个要注意

路径我们要改成了业务数据部的Anti

以及数据层接口的保路径

最后就是它的配置文件

配置文件咱们来看一下

它是如何去配置实现的

首先它要去配置

配置文件

交易数据源

这个是交易数据源的连接配置信息

然后是Druid

它的连接词的配置信息

Druid连接词配置信息

之前咱们也做了讲解

这里就不再赘述

然后下面就是业务数据源的连接配置

这里面的话

它指向的也是Druid的数据源

然后它的驱动类名称

是指向MySQL的驱动包

下面是它的连接配置信息

然后它指向的也是Druid的数据源

同样这里也是Druid的连接词的配置信息

好

在Spring Data Source下面

我们增加了一个层级

也就是Chad System和Business System

这个不同于单个数据源的配置

我们要多了一个层级

对应在Druid System Data Source Config 类当中

我们可以读取到不同的数据源配置

其他的跟单数据源的配置信息都是一样的

这里要注意一下

PG搜索跟ManoDB连接配置信息

连接上它的配置是存在一些差异

相应的数据库驱动架包也要将它导入进来

那咱们回到工程代码当中去检查一下

在BusTalk, Quart,行情服务工程当中

咱们通过ManoHelp插件去检测一下

CostReceive

这个驱动包并没有加入进来

那么咱们把它放在CommonDuo下面

在Home文件下面

我们去增加PG搜索的驱动包

Defenses

主编名称叫org-post-gre-circle

artifact的ID是post-gre-circle

还给它一个版本

motion-post-gre-circle.motion

加上注释

这个是post-gre-circle的客户端

连接驱动图件

好,咱们让它导入一下

再次回到行情服务当中

咱们刷新一下

这个时候就能看到PG搜索的驱动包

那在这里咱们就实现了业务数据上的配置

以及整个工程配置文件当中多数据的配置

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频是关于一个名为“bulls-stock”的Java项目中，如何配置和管理多个数据库（特别是交易数据库和业务数据库）的实战教程。讲师通过 IntelliJ IDEA 开发环境，详细演示了如何使用 Spring Boot 的 `@Configuration` 类来配置 JPA 的数据源和事务管理器，并通过 `bootstrap-dev.yml` 文件配置 Druid 数据源。视频重点在于展示如何为不同的数据源（如 `bizSystem` 和 `tradeSystem`）创建独立的配置类，以及如何在配置文件中为它们指定不同的数据库连接参数和包扫描路径。同时，讲师也展示了如何解决 Maven 依赖冲突，并配置 Druid 数据源的监控和连接池参数。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，讲师在 PPT 上展示课程大纲，明确本节内容是“JPA 多数据源配置”。
*   **00:00:05 - 00:00:15**：讲师在 IDEA 中打开 `BizSystemDataSourceConfiguration.java` 文件，展示如何为业务数据库配置 `@EnableTransactionManagement` 和 `@EnableJpaRepositories`，并指定 `basePackages` 为业务包路径。
*   **00:00:15 - 00:00:30**：讲师切换到 `TradeSystemDataSourceConfiguration.java` 文件，展示如何为交易数据库配置类似的注解，并将 `basePackages` 设置为交易包路径。
*   **00:00:30 - 00:00:45**：讲师在 `BizSystemDataSourceConfiguration` 中，演示如何通过 `@Autowired` 注入 `HibernateProperties` 和 `JpaProperties`，并编写 `getVendorProperties` 方法来动态设置 Hibernate 的方言（`hibernate.dialect`）。
*   **00:00:45 - 00:01:00**：讲师在 `TradeSystemDataSourceConfiguration` 中，同样演示了注入属性和设置方言，但使用了不同的数据库连接参数。
*   **00:01:00 - 00:01:15**：讲师在 PPT 上展示 `bootstrap-dev.yml` 文件，讲解如何配置 Druid 数据源，包括 `type`、`driver-class-name`、`url`、`username` 和 `password`。
*   **00:01:15 - 00:01:30**：讲师在 PPT 上展示 Druid 数据源的详细配置项，如 `maxActive`、`maxWait`、`validationQuery`、`poolPreparedStatements` 等。
*   **00:01:30 - 00:01:45**：讲师在 IDEA 中打开 `pom.xml` 文件，演示如何解决 Druid 监控组件与其它日志框架的冲突，通过添加 `slf4j-log4j12` 依赖。
*   **00:01:45 - 00:02:00**：讲师在 `pom.xml` 中添加 `postgresql` 依赖，并设置版本号。
*   **00:02:00 - 00:02:15**：讲师在 PPT 上再次展示 `bootstrap-dev.yml` 文件，强调配置文件中 `datasource` 的 `type` 和 `driver-class-name` 配置。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   课程大纲：包含“目标”、“步骤”、“实现”等部分，其中“实现”部分下有“3.3 JPA多数据源配置”。
    *   `bootstrap-dev.yml` 文件配置示例：
        ```yaml
        spring:
          datasource:
            tradesystem:
              type: com.alibaba.druid.pool.DruidDataSource
              driver-class-name: org.postgresql.Driver
              username: office
              password: 654321
              url: jdbc:postgresql://192.168.19.150:5432/trade_stock
        ```
    *   Druid 数据源配置项：
        ```yaml
        druid:
          # 连接池的配置信息
          # 初始化大小，最小，最大
          initial-size: 5
          min-idle: 5
          maxActive: 20
          # 配置获取连接等待超时的时间
          maxWait: 60000
          # 配置间隔多久才进行一次检测，检测需要关闭的空闲连接，单位是毫秒
          timeBetweenEvictionRunsMillis: 60000
          # 配置一个连接在池中最小生存的时间，单位是毫秒
          minEvictableIdleTimeMillis: 300000
          validationQuery: SELECT 1
          testWhileIdle: true
          testOnBorrow: false
          testOnReturn: false
          # 打开PSCache，并且指定每个连接上PSCache的大小
          poolPreparedStatements: true
          maxPoolPreparedStatementPerConnectionSize: 20
          # 配置监控拦截的filters，去掉后监控界面sql无法统计，'wall'用于防火
          filters: stat,wall,log4j
          # 通过connectProperties属性来打开mergeSql功能，慢SQL记录
          connectionProperties: druid.stat.mergesql=true;druid.stat.slowSqlMillis=5000
        ```

*   **代码内容**：
    *   `BizSystemDataSourceConfiguration.java`：
        ```java
        @Configuration
        @EnableTransactionManagement
        @EnableJpaRepositories(
            basePackages = "com.itcast.bulls.stock.quote.repository.biz",
            entityManagerFactoryRef = "bizEntityManagerFactory",
            transactionManagerRef = "bizTransactionManager"
        )
        public class BizSystemDataSourceConfiguration {
            @Autowired
            private HibernateProperties hibernateProperties;
            @Autowired
            private JpaProperties jpaProperties;
            @Bean
            public LocalContainerEntityManagerFactoryBean tradeEntityManagerFactoryBean(EntityManagerFactoryBuilder builder) {
                return builder
                    .dataSource(bizSystemDataSource)
                    .properties(getVendorProperties(bizSystemDataSource))
                    .packages("com.itcast.bulls.stock.entity.quote")
                    .persistenceUnit("bizPersistentUnit")
                    .build();
            }
            private Map<String, Object> getVendorProperties(DataSource dataSource) {
                Map<String, Object> props = hibernateProperties.determineHibernateProperties(jpaProperties, dataSource);
                props.put("hibernate.dialect", "org.hibernate.dialect.MySQL5InnoDBDialect");
                return props;
            }
        }
        ```
    *   `TradeSystemDataSourceConfiguration.java`：
        ```java
        @Configuration
        @EnableTransactionManagement
        @EnableJpaRepositories(
            basePackages = "com.itcast.bulls.stock.quote.repository.trade",
            entityManagerFactoryRef = "tradeEntityManagerFactory",
            transactionManagerRef = "tradeTransactionManager"
        )
        public class TradeSystemDataSourceConfiguration {
            @Autowired
            private HibernateProperties hibernateProperties;
            @Autowired
            private JpaProperties jpaProperties;
            @Bean
            public LocalContainerEntityManagerFactoryBean tradeEntityManagerFactoryBean(EntityManagerFactoryBuilder builder) {
                return builder
                    .dataSource(tradeSystemDataSource)
                    .properties(getVendorProperties(tradeSystemDataSource))
                    .packages("com.itcast.bulls.stock.entity.trade")
                    .persistenceUnit("tradePersistentUnit")
                    .build();
            }
            private Map<String, Object> getVendorProperties(DataSource dataSource) {
                Map<String, Object> props = hibernateProperties.determineHibernateProperties(jpaProperties, dataSource);
                props.put("hibernate.dialect", "org.hibernate.dialect.PostgreSQL95Dialect");
                return props;
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：配置业务数据库（BizSystem）**：
    *   讲师在 IDEA 中打开 `BizSystemDataSourceConfiguration.java` 文件。
    *   他使用 `@Configuration`、`@EnableTransactionManagement` 和 `@EnableJpaRepositories` 注解来启用事务和 JPA 功能。
    *   他通过 `basePackages` 指定扫描的包路径为 `com.itcast.bulls.stock.quote.repository.biz`。
    *   他通过 `entityManagerFactoryRef` 和 `transactionManagerRef` 指定对应的 Bean 名称。
    *   他编写了 `getVendorProperties` 方法，用于动态设置 Hibernate 的方言，这里设置为 `MySQL5InnoDBDialect`。

*   **场景二：配置交易数据库（TradeSystem）**：
    *   讲师切换到 `TradeSystemDataSourceConfiguration.java` 文件。
    *   他同样使用 `@Configuration`、`@EnableTransactionManagement` 和 `@EnableJpaRepositories` 注解。
    *   他将 `basePackages` 设置为 `com.itcast.bulls.stock.quote.repository.trade`。
    *   他将 `entityManagerFactoryRef` 和 `transactionManagerRef` 设置为 `tradeEntityManagerFactory` 和
