# 16-账户资金总览-工程搭建与配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始去实现资金服务的搭建和配置

资金服务是负责账户资金功能的处理

包含账户总的资金调整

还有资金变动等相关功能

那咱们就来做个实现

在工程当中

我们去创建一个新的模块

右键New Model

点击Next

名称叫Bus

Stock

Finance

点击Next

点击Finish

让它导入生效

工程模块创建完成之后

首先咱们创建它的技术包

New Package

名称叫Com

Add Cast

Bus

Stock

Finance

OK

好

接下来咱们来创建

它的纸包

右键Open in Terminal

创建配置目录

创建DAO数据层

创建GRBC

接口服务层

创建Service

Startup

再创建一个VIO

咱们刷新一下包

好

那这些必要的包呢

就已经创建好

后面咱们会做具体的实现

接下来

咱们加入工程的依赖

从讲义当中做copy

放在最下面

让它导入生效

咱们看一下

主要导入了哪些依赖呢

在这里有Spring Boot的依赖

Marcus服务注册发现的依赖

这些呢就是公用的数据层

服务层组件

然后工具

这个是实体层的依赖

咱们还用到了Lockit MQ

消息对电

因为呢要去监听实时行情数据

接着呢是款存的依赖

这里呢就是GIBC服务相关的依赖

这里要注意一下

咱们还会用到CETA分布式事务依赖

在下单的整个流程当中

订单服务是处理订单相关的信息

资金服务是负责账户资金的管理

他们是在不同的服务下面

这就需要采用到分布式事务

去做对应的实现

CETA的运用

之前咱们也做了讲解

那CETA如何在项目当中去集成运用

在后面的讲解

我们还会做具体的讲解

咱们先将它的依赖引入进来

这里我们要定义它的版本信息

放在我们的附集工程

这个是最上级的工程下面

定义一个属性

叫CETA.WASH

之前讲义采用的版本呢

是比较早期的版本

目前CETA迭代的版本

更新比较快

这里咱们就采用一个相对稳定的版本

0.9.0

把它导入生效

再回到咱们刚才的FOM文件下面

这些依赖定义完成之后

下面是多环境版本的配置信息

然后是Build的

多环境打包的一些配置信息

接下来咱们还去实现工程的服务配置

在这里我们创建配置文件

LiuFile

Boot

Shapes

YAM

这里是Splint

Profiles

因为是多环境版本配置

我们采用的是动态变量

Hackage.Evolution

接着我们定义一个开发环境的版本配置

LiuFile

Boot.Shapes

-DV.YAM

这里配置内容比较多

咱们就从讲义当中做一个copy

找到工程配置信息

在最下面

咱们全部选中

然后粘贴进去

咱们来看一下它的主要配置

从上面开始看起

这下是服务的基本配置

端口

服务名称

下面是LokiMQ

消息的订阅配置

注意它的Global组别

这里不要产生冲突了

下面是双数据源的配置

这个是交易数据源

下面是业务数据源

然后是Ladies

缓存的配置

Splint本不是Session

这个不需要

然后是JPA的功能配置

MyBadis的配置信息

资金服务

在这里是采用MyBadis的双数据源方案

下面是GRBC的服务端配置

然后是现成时的配置信息

工程配置完成之后

咱们就来实现双数据源的配置

双数据源的实现方案

之前咱们是做过讲解

在这里我们就直接从

已实现的代码当中做一个copy

找到咱们的资金服务

它在config的包下面

将这三个配置类copy进来

放在config目录下面

copy进来之后要注意他们的扫描路径

主要就是调整路径的扫描

其他方面是不需要做任何调整

这个是数据层接口的扫描

下面是map文件的扫描

我们要确保这个路径是正确的

finance.do

finance.do

然后地址

目前DAO的数据层接口还没有解决完

没有引入进来

咱们就从已实现的代码当中

将DAO的数据层接口copy进来

放到DAO目录下面

连接OK

copy完成之后

同样咱们要做一个检查

确保他们的配置路径是正确的

这个是DAO

这个是实体

好

这些放到实体都没有问题

数据层接口的运用

在后面实现核心业务功能的时候

咱们还会做介绍

如果是涉及到比较复杂的数据层操作接口

咱们还会做具体的讲解

好

双数据源信息配置完成之后

接着咱们再去配置缓存信息

为节省时间

这部分代码就不再去敲写

我们直接从已实现代码当中做一个copy

放在config目录下面

检查一下

好

这个是ladis template模板接口的配置

下面是ladis的使用配置

在这里设置了一个默认的超时时设置

在这里设置了一个默认的超时时设置

时间视为24小时

必要的主件集成配置完成之后

最后咱们再去实现它的启动内

右键new java class

名称叫stock

binance

application

创建启动方法

sprint

application

点乱

指向当前内

传递axe参数

添加必要的注册

解写

是零boot

Enable discovery client

这个是服务注册发现

Enable transaction management

这是开启事务管理器

Compend scan

扫描咱们的基础保证

comm.idcast

好

那这里呢

咱们就实现了资金服务的搭建

以及它的必要组件的集成配置

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于一个名为“ bulls-stock-finance ”的股票资金服务的搭建与配置。讲师通过 IntelliJ IDEA 开发环境，详细演示了如何创建一个 Spring Boot 项目，集成 Nacos 服务发现、Redis 缓存、RocketMQ 消息队列和 gRPC 通信等主流微服务组件。课程重点在于配置文件的编写，包括 `pom.xml` 依赖管理、`bootstrap-dev.yml` 环境配置，以及如何通过 MyBatis-Plus 进行数据库映射。同时，讲师也介绍了账户资金总览功能的计算公式，为后续的业务逻辑实现打下基础。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示项目结构和 PPT 大纲，介绍本节内容为“资金服务的搭建与配置”。
*   **00:06 - 00:15**: 在 IntelliJ IDEA 中创建并配置 `bulls-stock-finance` 项目，展示 `pom.xml` 文件的初始结构。
*   **00:16 - 00:25**: 编辑 `pom.xml`，添加 Spring Cloud Alibaba Nacos Discovery 依赖，用于服务注册与发现。
*   **00:26 - 00:35**: 继续编辑 `pom.xml`，添加公共数据组件依赖。
*   **00:36 - 00:45**: 编辑 `pom.xml`，添加 RocketMQ、缓存（Redis）和 gRPC 等组件的依赖。
*   **00:46 - 00:55**: 展示 `pom.xml` 中的 `<build>` 配置，包括 `spring-boot-maven-plugin` 插件，用于打包和运行。
*   **00:56 - 01:05**: 展示 `bootstrap-dev.yml` 配置文件，设置服务端口、应用名称、Nacos 服务发现地址等。
*   **01:06 - 01:15**: 展示 `bootstrap-dev.yml` 中的 Redis 配置，包括连接地址、密码和端口。
*   **01:16 - 01:25**: 展示 `bootstrap-dev.yml` 中的 JPA 和 Hibernate 配置。
*   **01:26 - 01:35**: 展示 `TradeDealMapper.xml` 文件，演示 MyBatis-Plus 的 XML 映射文件结构。
*   **01:36 - 01:45**: 展示 `RedisConfiguration.java` 文件，演示如何配置 `RedisTemplate` 和 `CacheManager`。
*   **01:46 - 01:55**: 展示 `StockFinanceApplication.java` 的主类，演示 Spring Boot 应用的启动方式。
*   **01:56 - 02:05**: 展示 PPT 内容，介绍“账户资金总览功能计算公式介绍”，并列出四个核心计算公式。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.1 资金服务的搭建与配置”。
    *   **章节标题**: “3.2 账户资金总览功能计算公式介绍”。
    *   **计算公式**:
        1.  **用户总资产**: `总资产 = 总市值 + 可用资金`。
        2.  **总市值**: `总市值 = Σ (股票最新价 * 持仓股数)`。
        3.  **持仓盈亏**: `持仓盈亏 = Σ (现价 - 持仓成本价) * 持仓股数`。
        4.  **当日持仓盈亏**: `原持仓量 = 当前仓位总数 + 当日卖出数量 - 当日买入数量`。
        5.  **当日持仓盈亏**: `当日持仓盈亏 = 原持仓量 * (最新价格 - 昨日收盘价)`。

*   **代码关键内容**:
    *   **`pom.xml` 依赖**:
        ```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <!-- 服务注册发现依赖 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>

        <!-- 公用数据组件依赖 -->
        <dependency>
            <groupId>com.itcast.trade</groupId>
            <artifactId>bulls-stock-common</artifactId>
            <version>1.0.0</version>
        </dependency>
        ```
    *   **`bootstrap-dev.yml` 配置**:
        ```yaml
        server:
          port: 10699
        spring:
          application:
            name: stock-finance
          cloud:
            nacos:
              discovery:
                server-addr: 127.0.0.1:8848
        redis:
          host: 127.0.0.1
          password: 6379
          port: 6379
        jpa:
          properties:
            hibernate:
              use_jdbc_metadata_defaults: false
        ```
    *   **`TradeDealMapper.xml` 映射文件**:
        ```xml
        <resultMap id="BaseResultMap" type="com.itcast.bulls.stock.finance.trade.TradeDeal">
            <id column="id" property="id" jdbcType="BIGINT"/>
            <result column="tradeOrderd" property="tradeOrderd" jdbcType="BIGINT"/>
            ...
        </resultMap>
        ```
    *   **`RedisConfiguration.java` 配置类**:
        ```java
        @Configuration
        public class RedisConfiguration {
            @Bean
            public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory redisConnectionFactory) {
                RedisTemplate<String, Object> redisTemplate = new RedisTemplate<>();
                redisTemplate.setKeySerializer(new StringRedisSerializer());
                redisTemplate.setConnectionFactory(redisConnectionFactory);
                return redisTemplate;
            }

            @Bean
            public CacheManager cacheManager(RedisConnectionFactory redisConnectionFactory) {
                Duration expiration = Duration.ofSeconds(3600 * 24);
                return RedisCacheManager.builder(RedisCacheConfiguration.defaultCacheConfig())
                        .entryTtl(expiration).build();
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目创建与依赖管理**:
    讲师在 IntelliJ IDEA 中创建了 `bulls-stock-finance` 项目，并逐步在 `pom.xml` 中添加了 Spring Boot Web、Nacos 服务发现、Redis、RocketMQ 和 gRPC 等依赖。通过鼠标点击和键盘操作，演示了如何在 Maven 中管理项目依赖。

*   **场景二：配置文件编写**:
    讲师打开了 `bootstrap-dev.yml` 文件，逐行讲解了服务端口、应用名称、Nacos 地址、Redis 配置和 JPA 配置等关键参数。通过高亮和滚动，引导观众关注配置细节。

*   **场景三：数据访问层配置**:
    讲师展示了 `TradeDealMapper.xml` 文件，解释了 MyBatis-Plus 的 XML 映射文件结构，包括 `resultMap` 和 `resultMap` 中的字段映射关系。

*   **场景四：缓存与服务配置**:
    讲师展示了 `RedisConfiguration.java` 文件，演示了如何通过 Spring 的 `@Configuration` 注解配置 `RedisTemplate` 和 `CacheManager`，并设置了缓存的默认过期时间为 24 小时。

*   **场景五：启动类与公式介绍**:
    讲师展示了 `StockFinanceApplication.java` 的主类，演示了 Spring Boot 应用的启动方式。随后，讲师切换到 PPT，详细介绍了账户资金总览功能的四个核心计算公式，为后续的业务逻辑实现提供了理论基础。
