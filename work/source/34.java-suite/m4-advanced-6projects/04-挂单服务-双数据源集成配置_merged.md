# 04-挂单服务-双数据源集成配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始实现挂单服务双数据源的配置

挂单需要处理生成交易订单

还有持仓等相关信息

这个时候就需要订阅多个数据源来做对应的实现

关于JPA的双数据源配置

以及MyBuddy时的双数据源配置

咱们前面章节都已经做过讲解

在这里我们就从已经实现的源码当中

copy这三个配置文件

打开我们已实现的源码

在这里我们选中Business

Droid

以及Pure System Data Source Configuration

将它copy到我们的Pending工程下面的Config目录

copy完成之后咱们看一下整个配置的实现

首先咱们打开Droid的配置内

这里是采用MyBuddy时的双数据源实现方案

和咱们之前在交易服务当中

讲解的MyBuddy时

双数据源配置基本上都是一样的

在这里要定义两个数据源

一个是业务数据源

一个是交易数据源

然后加上Primary的注解

标识交易数据源

作为整个工程服务的默认数据源

接着的话就是配置业务数据源

在配置的时候

我们要注意Mapscan的扫描路径

确保整个路径的配置是正确的

接下来还要配置Map文件的扫描路径

这些信息不要配置错误

如果路径配置有问题

是不能够正常启动

下面是定义了事务管理器

然后这里定义了CircleSession

Template的模板接口

下面就是交易数据源的定义

交易数据源是作为工程的默认数据源

在这里要加上Primary的注解

接下来咱们再将底层的

DEO数据层接口Copy进来

在DEO目录下面

咱们将B字目录和缺的目录Copy进来

放在DEO下面

注意

DEO的路径以及实体的路径要配置正确

这里面是提供了基础必要的数据层操作接口

在后面咱们实现限价委托挂单的处理流程当中

是需要使用到

这里用到的数据层接口

和交易服务里面试驾下单所用到的数据层接口

基本上都是类似的

这里咱们就不再一一编写

直接引用进来就可以

接下来就是确保工程配置文件当中

加入了双数据源的配置

我们在这里可以看到

这里是定义了两个数据源

一个是交易数据源

另外一个是业务数据源

这两个数据源都是采用得路易的连接词

这些就是不同数据源的它的连接配置信息

不同数据源的连接配置信息要做相应的调整

好

那咱们回到讲义当中

在这里呢

咱们就实现了挂单服务双数据源的集成配置

为后面的限价委托挂单的处理做好基础

好

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频是关于“交易系统”中“挂单服务”模块的开发教程，具体聚焦于**双数据源配置**。讲师通过演示如何在 Spring Boot 项目中配置两个独立的数据库连接（业务系统数据库 `bizsystem` 和交易系统数据库 `tradesystem`），并使用 Druid 数据源连接池进行管理。核心内容包括：从现有项目中拷贝配置类、在 `bootstrap-dev.yml` 中定义两个数据源的配置、使用 `@Qualifier` 注解区分不同数据源、以及为每个数据源配置对应的 `SqlSessionFactory` 和 `SqlSessionTemplate`。整个过程旨在实现服务在处理挂单时能同时访问两个不同的数据库。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开场，讲师在 Typora 中展示课程大纲，明确本节主题为“3.2 挂单服务双数据源配置”。
*   **00:05 - 00:15**: 讲师说明挂单服务需要处理订单和持仓信息，因此需要订阅多个数据源。并指出需要修改三个配置类文件。
*   **00:15 - 00:30**: 讲师在 IDE 中打开项目，展示 `bulls-stock-pending` 模块的结构，并演示如何从 `src/main/java/com/itcast/bulls/stock/pending/config` 目录中拷贝 `BizSystemDataSourceConfiguration.java`、`DruidSystemDataSourceConfiguration.java` 和 `TradeSystemDataSourceConfiguration.java` 三个文件。
*   **00:30 - 00:45**: 讲师在 `bootstrap-dev.yml` 配置文件中添加两个数据源的配置，分别为 `bizsystem` 和 `tradesystem`，并指定其驱动、URL、用户名和密码。
*   **00:45 - 01:00**: 讲师展示 `DruidSystemDataSourceConfiguration.java` 的代码，其中使用 `@Bean` 注解定义了两个数据源，通过 `@ConfigurationProperties` 注解绑定配置文件中的属性，并使用 `@Primary` 注解标记 `tradeSystemDataSource` 为默认数据源。
*   **01:00 - 01:15**: 讲师展示 `TradeSystemDataSourceConfiguration.java` 的代码，其中使用 `@Autowired` 和 `@Qualifier("tradeSystemDataSource")` 注解注入 `tradeSystemDataSource`，并创建了对应的 `SqlSessionFactory`。
*   **01:15 - 01:30**: 讲师展示 `TradeSystemDataSourceConfiguration.java` 中的 `SqlSessionTemplate` 配置，同样使用 `@Qualifier` 注解指定数据源。
*   **01:30 - 01:45**: 讲师展示 `StockUserDao` 接口，其中定义了根据用户账号或账户获取用户对象的方法。
*   **01:45 - 02:00**: 讲师展示 `bootstrap-dev.yml` 文件中的 `server.port` 配置，将其设置为 `19998`。
*   **02:00 - 02:15**: 讲师展示 `bootstrap-dev.yml` 文件中的 `bizsystem` 数据源配置，包括驱动、URL、用户名和密码。
*   **02:15 - 02:30**: 讲师展示 `bootstrap-dev.yml` 文件中的 `tradesystem` 数据源配置，包括驱动、URL、用户名和密码。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: `3.2 挂单服务双数据源配置`
    *   **关键步骤**:
        1.  参考前面所讲的多数据源配置，从已实现的源码中拷贝三个文件作为相应修改：`BizSystemDataSourceConfiguration`, `DruidSystemDataSourceConfiguration`, `TradeSystemDataSourceConfiguration`。
        2.  在 `bootstrap-dev.yml` 中添加多数据源配置。

*   **代码关键内容**:
    *   **`DruidSystemDataSourceConfiguration.java`**:
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
    *   **`TradeSystemDataSourceConfiguration.java`**:
        ```java
        @Configuration
        @MapperScan("com.itcast.bulls.stock.pending.dao.trade")
        public class TradeSystemDataSourceConfiguration {
            @Autowired
            @Qualifier("tradeSystemDataSource")
            private DataSource tradeSystemDataSource;

            @Bean(name = "tradeSystemSqlSessionFactory")
            @Primary
            public SqlSessionFactory tradeSystemSqlSessionFactory(@Qualifier("tradeSystemDataSource") DataSource dataSource) throws Exception {
                SqlSessionFactoryBean bean = new SqlSessionFactoryBean();
                bean.setDataSource(dataSource);
                bean.setMapperLocations(new PathMatchingResourcePatternResolver().getResources("classpath:/com/itcast/bulls/stock/pending/mapper/*.xml"));
                return bean.getObject();
            }

            @Bean(name = "tradeSystemSqlSessionTemplate")
            @Primary
            public SqlSessionTemplate tradeSystemSqlSessionTemplate(@Qualifier("tradeSystemSqlSessionFactory") SqlSessionFactory sqlSessionFactory) {
                return new SqlSessionTemplate(sqlSessionFactory);
            }
        }
        ```
    *   **`bootstrap-dev.yml`**:
        ```yaml
        # bizsystem 数据源配置
        bizsystem:
          type: com.alibaba.druid.pool.DruidDataSource
          driver-class-name: com.mysql.cj.jdbc.Driver
          username: root
          password: 654321
          url: jdbc:mysql://192.168.19.150:3306/trade_stock?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true&failOverReadOnly=false&maxAllowedPacket=64M

        # tradesystem 数据源配置
        tradesystem:
          type: com.alibaba.druid.pool.DruidDataSource
          driver-class-name: org.postgresql.Driver
          username: office
          password: 654321
          url: jdbc:postgresql://192.168.19.150:5432/trade_stock
          druid:
            initial-size: 5
            max-active: 20
            maxWait: 60000
            timeBetweenEvictionRunsMills: 60000
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与文件拷贝** (00:15 - 00:30)
    *   讲师在 IDE 中打开项目，展示 `bulls-stock-pending` 模块的目录结构。
    *   讲师在 `src/main/java/com/itcast/bulls/stock/pending/config` 目录中选中三个配置文件，并演示如何将它们拷贝到当前项目中。

*   **场景二：配置文件修改** (00:30 - 02:30)
    *   讲师在 `bootstrap-dev.yml` 文件中添加两个数据源的配置。
    *   讲师分别展示了 `bizsystem` 和 `tradesystem` 数据源的详细配置，包括驱动、URL、用户名和密码。
    *   讲师展示了 `DruidSystemDataSourceConfiguration.java` 中的代码，其中使用 `@ConfigurationProperties` 注解绑定配置文件中的属性，并使用 `@Primary` 注解标记 `tradeSystemDataSource` 为默认数据源。
    *   讲师展示了 `TradeSystemDataSourceConfiguration.java` 中的代码，其中使用 `@Autowired` 和 `@Qualifier` 注解注入 `tradeSystemDataSource`，并创建了对应的 `SqlSessionFactory` 和 `SqlSessionTemplate`。

*   **场景三：数据访问层配置** (01:30 - 01:45)
    *   讲师展示了 `StockUserDao` 接口，其中定义了根据用户账号或账户获取用户对象的方法。
    *   讲师展示了 `TradeSystemDataSourceConfiguration.java` 中的 `SqlSessionTemplate` 配置，同样使用 `@Qualifier` 注解指定数据源。

*   **场景四：服务端口配置** (01:45 - 02:00)
    *   讲师展示了 `bootstrap-dev.yml` 文件中的 `server.port` 配置，将其设置为 `19998`。

*   **场景五：IDE 操作演示** (00:30 - 00:45)
    *   讲师在 IDE 中打开 `DruidSystemDataSourceConfiguration.java` 文件，展示其代码。
    *   讲师在 IDE 中打开 `TradeSystemDataSourceConfiguration.java` 文件，展示其代码。
    *
