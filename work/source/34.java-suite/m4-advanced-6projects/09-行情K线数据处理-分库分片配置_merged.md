# 09-行情K线数据处理-分库分片配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

下面开始学习行情服务K线分表Sharding JDBC的集成配置

在做集成配置之前咱们先思考下

如何在多数据源当中实现Sharding JDBC的集成配置

之前行情服务咱们采用的是基于JPA的多数据源的配置

交易服务采用的是基于MyBetis的多数据源配置

在多数据源的情况下

集成Sharding JDBC会不会碰上问题

如何去实现单库分片的配置

那接下来我们做个实现

首先要去增加POM的依赖配置

Copy

在行情代理服务POM文件下面

增加Sharding JDBC的依赖

让它导入生效

咱们还要定义Sharding JDBC的版本

将它定义在2G的工程下面

Propice标签里面

版本是3.1.0

让它导入生效

回到刚才的配置

Ctrl可以看到依赖已经添加成功

接下来回到讲义当中

然后我们要增加分库分片的规则设施

这里采用的是单库分片配置

如果是大家需要多库分片

也可以依此作为参照

在这里大家要注意一下

有些SaaS平台

一些数据表

他们是动态去创建的

比如说他们在SaaS上面

新开了一个公司

那么对应它会在数据源当中

创建该公司所对应的表

但是Sharding JDBC

它只是一个路由代理主线

并非Sharding JDBC不能实现

它的核心职能是作为数据源的路由代理

所以官方不建议去操纵

或者是修改数据库

不能去执行DML语句

如果大家需要去动态创建表

那么需要预先建立好

比如说可以通过后台管理功能

去提供相关的菜单操作

或者去通过初始化语句

实现表的动态创建

接着我们就来做分库分片的具体配置

上面这部分是分库的配置

下面这部分是分片的配置

那咱们来做一个具体实现

回到代码当中

创建表的动态创建表

创建表的动态创建表

创建一个宝

在config目录下面

new package

创建专门优于分表配置的宝

sharing

首先去实现分库的配置

创建一个class

名称叫datasource

alg

它要去实现sharing JDBC的接口

传递分库的类型

将接口重写

加上描述

这个接口添加注释

这个是分库配置信息

下面可以看到有两个阐述

一个是collection

一个是sharing value

collection里面包含的是分库信息

sharing value里面包含的就是分片信息

如果咱们要实现多个分库配置

那么每个库下面呢

就要配置不同的分片

咱们可以来画一下

比如说这里面有两个分库

数据库1

这个呢是二号数据库

下面呢有不同的分片

比如说有四个分片

这是订单表

一号分片

订单表

二号分片

这是三号分片

四号分片

如果只是单库

那么数据库的1

对应的就是所有订单表的信息

如果是做了分库处理

那么就要做一个配置划分

比如说订单表1归属数据库1

订单表2也归属数据库1

那么订单表3和订单表4归属数据库2

它们的配置对应关系是怎么去识别和处理呢

就是咱们刚才所写的这段配置代码

那这里面的collection就是咱们的分库信息

比如说有两个数据库

那么collection里面呢

就有数据库1以及数据库2的信息

那么shorting value里面呢

就是所有的订单表的分片信息

从一号到四号分片

在这里既然咱们是采用单个数据库

所以就可以给它返回一个固定的默认值

那就固定返回0号数据库

如果是要做多个分库的设置

那么就要拿到shorting value

然后和collection做一个匹配关联

如果这个shorting它是属于某一个数据库

那么就返回对应的数据库信息

这个呢就是分库的一个配置

在这里是单固处理

我们默认返回0号数据库就可以了

接下来还要去实现分片配置

我们再创建一个类

这个名称呢

我们叫datasource table lg

分片它要实现对应的接口

这个是分表的字段类型

重写它的配置

上面添加日字注解

添加描述

添加打印日字

提示已经进入该方法

去执行对应的逻辑

将参数打印出来

然后是shorting value的参数

行情这一块该如何去分表的

咱们回到讲习当中

查看行情服务k线分表方案

这里我们就分三张表

一张是以1分钟为k线的行情表

另外是5分钟和30分钟的k线表

咱们回到代码当中

首先要去定义table的名称

从shorting value里面获取

拿到table名称

它默认了就是tchat的storekline

并不包含后缀

它是一个原始的表信息

我给了table name

那么我们就需要做一个拼接处理

外层加上check catch补货

打印异常日字

抛出异常

给出一个long time exception

将错误信息抛出去

那咱们来做具体的分析

分表配置

分表规则配置实际上是根据周期类型

来映射不同的表

周期类型具体包括哪些值呢

它就包含1分钟

5分钟和30分钟

周期类型我们采用integer

那么要定义一个integer对象

那么要定义一个integer对象

做相应的判断

这个定义的是周期常量

定义的是不同的k线时间周期

单位是秒

那60秒是代表1分钟

300秒代表的是5分钟

回到刚才的代码

60就代表1分钟

知道1分钟的周期

那么表的名称拼接

后面就要跟上后缀为1

接下来再判断5分钟的周期

5分钟是300秒

table name做个拼接

然后是30分钟的判断

global consistence

30分钟是1800秒

30分钟周期

table name

table name在前面已经拼接了下滑线

最终组成的名称拼接30

就是咱们讲义当中

tchat stockinan下滑线-30

再回到代码当中

最后

如果超出咱们的规则

要抛出一个异常

not match

将type打印一下

再打印一个日志提示性的代码

种艺ость

飞货名词

配备剧象

网络

公式

信号

地址

电源

线上

饰素

检测

类型

任 Sexual

该模型

一个

使用

这个

是流星

恒星

下

那现在

这个

就是 vous

Terre

像 je

可能

不

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“bulls-stock-quote”的Java项目，重点讲解如何在该系统中集成并配置 **Sharding-JDBC** 数据库分库分表中间件，以实现对K线数据的水平分片。讲师通过IDEA开发环境，逐步演示了如何添加Sharding-JDBC的Maven依赖、编写自定义的分片算法（`DataSourceTableAlg`），以及如何配置多个数据源（如Druid）。视频内容旨在为开发者提供一个完整的、基于Sharding-JDBC的分库分表解决方案，特别适用于金融行情数据的存储场景。同时，视频也提到了Sharding-JDBC的一些技术限制，如不支持某些SQL语法。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开场，展示PPT大纲，明确本节主题为“3.2 行情服务K线分表 ShardingJDBC集成配置”。
*   **00:00:05 - 00:00:15**: 讲解第一步，增加Maven依赖。屏幕显示了 `sharding-jdbc-core` 的依赖配置代码，并指出其版本为 `3.1.0`。
*   **00:00:15 - 00:00:30**: 讲解第二步，增加分库分片规则。屏幕显示了 `DataSourceAlg` 类的代码，这是一个实现 `PreciseShardingAlgorithm<String>` 接口的分片算法，用于根据字符串（如股票代码）进行分片。
*   **00:00:30 - 00:00:45**: 切换到IDEA开发环境，展示项目结构。讲师在 `bulls-stock-quote` 项目中，右键点击 `src/main/java/com.icast.bulls.stock.quote/config` 目录，准备创建新的分片算法类。
*   **00:00:45 - 00:01:00**: 讲解如何创建新的分片算法类。屏幕显示了 `DataSourceTableAlg` 类的代码，这是一个实现 `PreciseShardingAlgorithm<Integer>` 接口的类，用于根据整数（如K线周期）进行分片。
*   **00:01:00 - 00:01:15**: 讲解分片算法的核心逻辑。屏幕显示了 `doSharding` 方法的代码，其中通过 `preciseShardingValue.getValue()` 获取分片键（周期类型），并根据其值（如 `KLINE_PERIOD_60`、`KLINE_PERIOD_300`）来决定数据应插入到哪个表中。
*   **00:01:15 - 00:01:30**: 讲解分片算法的异常处理。屏幕显示了 `catch` 块中的代码，当分片规则不匹配时，抛出 `Not Match Table Rule` 异常。
*   **00:01:30 - 00:01:45**: 讲解Sharding-JDBC的限制。屏幕显示了PPT内容，列出了Sharding-JDBC不支持的SQL特性，如不支持 `HAVING`、`OR`、`UNION`、`INSERT ... VALUES` 多行数据等。
*   **00:01:45 - 00:02:00**: 讲解Druid多数据源集成配置。屏幕显示了 `DruidSystemDataSourceConfiguration` 类的代码，用于配置名为 `bizSystemDataSource` 的数据源。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT内容**:
    *   **章节标题**: “3.2 行情服务K线分表 ShardingJDBC集成配置”。
    *   **问题**: “如何在多数据源中实现sharding-jdbc的集成配置？如何实现单库分片的配置？”
    *   **Sharding-JDBC限制**: 一个列表，包含不支持的SQL特性，如 `HAVING`、`OR`、`UNION`、`INSERT ... VALUES`、`DISTINCT`、`SELECT LAST_INSERT_ID()`、`CASE WHEN` 等。
    *   **分片方案**: “根据行情周期条件，生成不同时间周期的K线数据”。

*   **代码内容**:
    *   **Maven依赖**:
        ```xml
        <!-- sharding-jdbc 依赖 -->
        <dependency>
            <groupId>io.shardingsphere</groupId>
            <artifactId>sharding-jdbc-core</artifactId>
            <version>${sharding.jdbc.version}</version>
        </dependency>
        ```
    *   **分片算法 `DataSourceAlg`**:
        ```java
        public class DataSourceAlg implements PreciseShardingAlgorithm<String> {
            @Override
            public String doSharding(Collection<String> collection, PreciseShardingValue<String> value) {
                return null;
            }
        }
        ```
    *   **分片算法 `DataSourceTableAlg`**:
        ```java
        public class DataSourceTableAlg implements PreciseShardingAlgorithm<Integer> {
            @Override
            public String doSharding(Collection<String> collection, PreciseShardingValue<Integer> preciseShardingValue) {
                String tableName = preciseShardingValue.getLogicTableName() + "_";
                Integer type = preciseShardingValue.getValue();
                if (type.equals(GlobalConstants.KLINE_PERIOD_60)) {
                    tableName = tableName + "1";
                } else if (type.equals(GlobalConstants.KLINE_PERIOD_300)) {
                    tableName = tableName + "300";
                } else if (type.equals(GlobalConstants.KLINE_PERIOD_1440)) {
                    tableName = tableName + "1440";
                } else {
                    throw new Exception("Not Match Table Rule, type: " + type);
                }
                return tableName;
            }
        }
        ```
    *   **Druid数据源配置 `DruidSystemDataSourceConfiguration`**:
        ```java
        @Configuration
        public class DruidSystemDataSourceConfiguration {
            @Bean(name = "bizSystemDataSource")
            @ConfigurationProperties(prefix = "spring.datasource.bizsystem")
            public DataSource bizSystemDataSource() {
                return new DruidDataSource();
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：添加Sharding-JDBC依赖** (00:00:05)
    *   **描述**: 讲师在PPT上展示如何在项目的 `pom.xml` 文件中添加Sharding-JDBC的Maven依赖。他强调了使用的版本是 `3.1.0`，并指出这是实现分库分表的基础。

*   **场景二：创建分片算法类** (00:00:30)
    *   **描述**: 讲师在IDEA中，通过右键菜单在 `config` 包下创建了一个新的Java类 `DataSourceTableAlg`。他展示了如何实现 `PreciseShardingAlgorithm<Integer>` 接口，该接口用于根据整数类型的分片键（如K线周期）来决定数据应插入到哪个表中。

*   **场景三：编写分片逻辑** (00:01:00)
    *   **描述**: 讲师在 `DataSourceTableAlg` 类中编写了核心的 `doSharding` 方法。他通过 `preciseShardingValue.getValue()` 获取分片键的值，并根据该值与预定义的常量（如 `KLINE_PERIOD_60`、`KLINE_PERIOD_300`）进行比较，从而决定最终的表名。例如，如果分片键是60分钟周期，则表名会加上后缀“1”。

*   **场景四：异常处理** (00:01:15)
    *   **描述**: 讲师在 `doSharding` 方法中添加了 `try-catch` 块。当分片规则不匹配时（例如，传入的周期类型不在预定义的常量中），他会抛出一个 `Exception`，并附带错误信息“Not Match Table Rule, type: [类型]”，以便于调试和日志记录。

*   **场景五：展示Sharding-JDBC限制** (00:01:30)
    *   **描述**: 讲师切换到PPT，展示了一个列表，详细说明了Sharding-JDBC不支持的SQL特性。这有助于开发者在设计SQL语句时避免使用不被支持的功能，从而确保应用的兼容性。

*   **场景六：配置Druid数据源** (00:01:45)
    *   **描述**: 讲师在PPT上展示了一个名为 `DruidSystemDataSourceConfiguration` 的配置类。该类使用 `@Configuration` 注解，通过 `@Bean` 注解定义了一个名为 `bizSystemDataSource` 的数据源，并使用 `@ConfigurationProperties` 注解绑定配置文件中的属性。这为Sharding-JDBC提供了底层的数据源支持。
