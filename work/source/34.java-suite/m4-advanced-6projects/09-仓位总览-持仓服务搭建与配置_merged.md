# 09-仓位总览-持仓服务搭建与配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

下面咱们开始去实现持仓服务的搭建和配置

在做实现之前咱们先了解一下

用户下单完成之后

需要去查看仓位的信息

关注行情和仓位信息的变化

这个时候就需要咱们提供用户仓位总览的功能

这又是仓位总览的具体作用

它能够提供行情对仓位信息的变化情况

用户仓位总览

实际上就是查看所有的仓位信息

结合这些信息做一个汇总

包含持仓价格

持仓数量

最新价格

盈亏情况等等

核心逻辑呢

它是要做浮动盈亏的计算

这部分是比较重要

也是整个实现的难点

在下面章节的实现过程当中

咱们会做具体的讲解

那首先我们来搭建持仓服务

咱们回到工程当中

在这里我们创建一个新的模块

New Model

点击Next

名称就叫Bus

Stock Position

负责用户仓位的功能处理

点击Next

点击Finish

好可以看到持仓服务呢

就已经导入进来

接下来咱们创建它的基础包结构

Package

Com

AddCast

点Bus

点Stock

Position

这样基础包呢

咱们就已经创建完成

接下来我们再创建它的纸包

右键Open

In Terminal

创建配置目录Config

创建DAO数据层

Service层

GRBC接口层

系统内

好咱们来刷新一下目录

可以看到呢

这几个整目录就已经创建完成

接下来咱们将工程的依赖添加进去

回到讲义当中

在这里copy工程POM的依赖

粘贴到

POM文件里面

让它导入生效

咱们来看一下它的主要依赖组件

这里呢

添加了SplitBoot的依赖

Narcos服务注射发现依赖

还有公用的数据层主线

服务层主线

工具主线

然后还有咱们的实体依赖

接下来呢

是LockedMQ消息主线的依赖

自动化缓存依赖

然后呢

就是GRBC相关的依赖组件

下面呢

是多环境的版本配置

这里的多环境版本

咱们就配置一个开发环境

做一个简化

工程配置文件的内容

相对会比较多一点

咱们就从已经实现的代码当中

做一个copy

在Resource目录下面

选中工程配置文件

将它粘贴到Resource目录下面

这个端口调整一下

挂单服务呢

是10697

这个持仓服务就改成10698

那咱们再大概看一下

它整体的工程配置

这些呢

是服务的基础配置信息

有Nacos的一些配置

然后呢

是LockitMQ的消费端配置

这个是新的持仓服务

所以呢

Hulu给了一个新的名称

然后下面是双数据源的配置

这个是交易数据源

下面这里呢

是业务数据源

然后就是累计式缓存配置

Spring分布式

Session呢

这里可以不需要

将它去除

下面呢

就是JPA的功能配置

然后就是Habnet的映射配置

再下面呢

就是MyBattis的配置

这里的数据源

咱们是采用MyBattis做的实现

下面呢

就是GRBC服务端的配置信息

确保这个端口是唯一

不要被其他服务占用

然后是现证词的配置

好

这个就是整体的工程配置信息

接下来咱们再将双数据源的配置

引入进来

双数据源配置的集成使用

之前咱们做过讲解

这里呢

就不再进行赘述

主要是这三个配置实现类

那咱们从原本的配置

代码当中拖比进来

在Config目录下面

选中这三个配置类

放置在Config包下面

接下来咱们将这个代码做个修正

JP和Habnet都不需要

因为咱们是基于MyBattis实现的双数据源

然后咱们要检查一下

数据层接口的扫描路径

这里呢是指向Position.do

好

然后是业务数据源

这个是B字的包

数据层接口

目前咱们还没有引入进来

那为了变语

后面核心业务功能的讲解与实现

这里咱们先将DAO数据层接口引入进来

在DAO的目录下面

将这两个包做copy

放置DAO package下面

要注意检查MAP的数据层接口

以及NT实体的路径

好

这些都配置正确

那咱们回到刚才的数据源配置

下面呢

是要检查MAP文件的扫描路径

咱们可以看一下

Bus, Stock, Position, DAO, Bits, Map

好

这个路径是正确的

咱们再看一下交易的数据源配置

这个话呢也是没有问题

咱们再看一下MAP的文件

这个路径扫描的话呢也是正确的

Position,资金服务也需要用到缓存功能

那咱们将缓存的配置代码也加入进来

Ladies Configuration

放在Configure Package下面

Ladies的集成配置

之前咱们也做过讲解

在这里呢

要开启缓存的注解

然后定义Ladies Tempo里的模板操作接口

下面是Ladies的使用配置

在这里呢

配置了它的一个默认操作时间

最后咱们再去创建它的启动类

6件6

DAO Class

Stock, Position, Application

定义启动方法

Strength, Application, 演络

此下方向类

Position, Class

增加注解

Spin Boot, Application

Enable

Discovering Client

最后呢就是包的扫描

Base, Packages

指向基准目录

Com.idcast

好,在这里呢

咱们就完成了

持仓服务的搭建

以及必要的组件集成配置

为下面核心功能的实现

做好准备

好

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于一个名为“bulls-stock”的股票交易系统中“持仓服务”（stock-position service）的实现教程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何搭建和配置一个独立的持仓服务模块。主要内容包括：创建新的 Maven 项目 `bulls-stock-position`，配置其 `pom.xml` 文件以引入必要的依赖（如 gRPC、Spring Boot、MyBatis、Redis 等），设置多环境配置（`bootstrap-dev.yml`），配置数据源（`TradeSystemDataSourceConfiguration.java`）和缓存（`RedisConfiguration.java`），并最终启动服务。整个过程旨在构建一个能够处理用户持仓信息、计算盈亏并支持高并发的后端服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师在 Typora 文档中展示了课程大纲，当前章节为“3.1 持仓服务的搭建与配置”，并简要说明了服务的核心功能是提供仓位服务和处理强平等逻辑。
*   **00:05 - 00:15**: 讲师在 IntelliJ IDEA 中创建了名为 `bulls-stock-position` 的新 Maven 项目，并在 `pom.xml` 中配置了父项目和基本的 `artifactId`。
*   **00:15 - 00:25**: 讲师在 `pom.xml` 中添加了 `dependencies` 部分，引入了 `bulls-stock-starter-grpc` 和 `bulls-stock-starter` 等依赖，并配置了 `profiles` 用于多环境管理。
*   **00:25 - 00:35**: 讲师展示了 `bootstrap-dev.yml` 配置文件，其中包含了服务端口、Nacos 注册中心地址、RocketMQ 消费者配置等。
*   **00:35 - 00:45**: 讲师继续编辑 `bootstrap-dev.yml`，配置了 MyBatis、gRPC 服务端口、线程池参数等。
*   **00:45 - 00:55**: 讲师在项目中创建了 `config` 文件夹，并展示了其中的 `TradeSystemDataSourceConfiguration.java` 和 `RedisConfiguration.java` 等配置类。
*   **00:55 - 01:05**: 讲师详细讲解了 `TradeSystemDataSourceConfiguration.java` 中的 `@Configuration` 注解和 `@Primary` 注解，以及如何配置数据源和 `SqlSessionFactory`。
*   **01:05 - 01:15**: 讲师讲解了 `RedisConfiguration.java` 中的 `@Bean` 方法，用于创建 `RedisTemplate` 和 `CacheManager`，并设置了默认的缓存过期时间。
*   **01:15 - 01:25**: 讲师在 `StockPositionApplication.java` 主类中调用 `SpringApplication.run(...)` 方法启动服务。
*   **01:25 - 01:35**: 讲师在 Typora 文档中再次强调了本节的核心内容，即“3.1 持仓服务的搭建与配置”。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **核心目标**: 搭建一个独立的持仓服务，提供仓位信息查询、处理强平等核心功能。
    *   **服务结构**: 服务包含 `dao`、`service`、`grpc`、`config`、`startup` 等模块。
    *   **依赖管理**: 使用 Maven 管理依赖，引入 `bulls-stock-starter-grpc`、`bulls-stock-starter`、`mybatis-spring-boot-starter`、`spring-boot-starter-data-redis` 等。
    *   **配置文件**: 使用 `bootstrap-dev.yml` 进行多环境配置，包含服务端口、Nacos、RocketMQ 等配置。
    *   **数据源配置**: `TradeSystemDataSourceConfiguration.java` 用于配置数据库连接。
    *   **缓存配置**: `RedisConfiguration.java` 用于配置 Redis 缓存，包括 `RedisTemplate` 和 `CacheManager`。

*   **关键代码片段**:

    *   **Maven `pom.xml` 配置**:
        ```xml
        <parent>
            <artifactId>bulls-stock</artifactId>
            <groupId>com.itcast.trade</groupId>
            <version>1.0.0</version>
        </parent>

        <dependencies>
            <dependency>
                <groupId>com.itcast.trade</groupId>
                <artifactId>bulls-stock-starter-grpc</artifactId>
                <version>${project.stock.version}</version>
            </dependency>
            <dependency>
                <groupId>com.itcast.trade</groupId>
                <artifactId>bulls-stock-starter</artifactId>
                <version>${project.stock.version}</version>
            </dependency>
        </dependencies>

        <profiles>
            <profile>
                <id>dev</id>
                <activation>
                    <activeByDefault>true</activeByDefault>
                </activation>
            </profile>
        </profiles>
        ```

    *   **`bootstrap-dev.yml` 配置**:
        ```yaml
        server:
          port: 10698
        spring:
          application:
            name: stock-position
          cloud:
            nacos:
              server-addr: 127.0.0.1:8848
          config:
            server-addr: 127.0.0.1:8848
        # RocketMQ 消费端配置
        stream:
          bindings:
            quote:
              consumer:
                concurrency: 10
                maxAttempts: 1
                content-type: application/json
                destination: application:quote
        ```

    *   **`TradeSystemDataSourceConfiguration.java`**:
        ```java
        @Configuration
        @MapperScan(basePackages = "com.itcast.bulls.stock.pdpition.dao.trade", sqlSessionTemplateRef = "tradeSystemSqlSessionFactory")
        public class TradeSystemDataSourceConfiguration {
            @Autowired
            @Qualifier("tradeSystemDataSource")
            private DataSource tradeSystemDataSource;

            @Bean(name = "tradeSystemSqlSessionFactory")
            @Primary
            public SqlSessionFactory tradeSystemSqlSessionFactory(Qualifier tradeSystemDataSource) {
                SqlSessionFactoryBean bean = new SqlSessionFactoryBean();
                bean.setDataSource(tradeSystemDataSource);
                bean.setMapperLocations(new PathMatchingResourcePatternResolver().getResources(locationPat));
                return bean.getObject();
            }
        }
        ```

    *   **`RedisConfiguration.java`**:
        ```java
        @Configuration
        public class RedisConfiguration {
            @Bean
            public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory redisConnectionFactory) {
                RedisTemplate<String, Object> redisTemplate = new RedisTemplate<>();
                redisTemplate.setConnectionFactory(redisConnectionFactory);
                return redisTemplate;
            }

            @Bean
            public CacheManager cacheManager(RedisConnectionFactory redisConnectionFactory) {
                Duration expiration = Duration.ofSeconds(3600 * 24);
                return RedisCacheManager.builder(redisConnectionFactory)
                        .cacheDefaults(RedisCacheConfiguration.defaultCacheConfig().entryTtl(expiration))
                        .build();
            }
        }
        ```

    *   **`StockPositionApplication.java` 启动类**:
        ```java
        @SpringBootApplication
        public class StockPositionApplication {
            public static void main(String[] args) {
                SpringApplication.run(StockPositionApplication.class, args);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目创建与依赖管理**
    *   **描述**: 讲师在 IntelliJ IDEA 中创建了一个名为 `bulls-stock-position` 的新 Maven 项目。随后，他打开了 `pom.xml` 文件，演示了如何配置父项目和添加必要的依赖项，如 `bulls-stock-starter-grpc` 和 `bulls-stock-starter`，并配置了 `profiles` 以支持多环境部署。

*   **场景二：配置文件编辑**
    *   **描述**: 讲师打开了 `bootstrap-dev.yml` 文件，详细讲解了其中的配置项，包括服务端口、Nacos 注册中心地址、RocketMQ 消费者配置等。他特别强调了 `spring.cloud.nacos.server-addr` 和 `spring.cloud.config.server-addr` 的设置。

*   **场景三：数据源与缓存配置**
    *   **描述**: 讲师在项目中创建了 `config` 文件夹，并展示了 `TradeSystemDataSourceConfiguration.java` 和 `RedisConfiguration.java`。在 `TradeSystemDataSourceConfiguration.java` 中，他演示了如何使用 `@Configuration` 和 `@MapperScan` 注解来配置数据源和 MyBatis 的 `SqlSessionFactory`。在 `RedisConfiguration.java` 中，他演示了如何创建 `RedisTemplate` 和 `CacheManager`，并设置了默认的缓存过期时间。

*   **场景四：服务启动**
    *   **描述**: 讲师在 `StockPositionApplication.java
