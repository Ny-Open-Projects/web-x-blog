# 11-行情K线数据处理-ShardingJDBC全局序列ID配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着去实现行情服务K线分表的集成配置

之前咱们已经是实现了分库以及分片的设置

这一讲咱们就来实现Druid多数据源集成配置

这里要去修改Druid System Statsource Configuration之前的数据库连接池配置

回到代码当中

打开连接池配置内

去增加ShaddingJetDPC的配置

咱们增加一个方法

Statsource

Shad System Statsource

Druid Statsource注入进来

这个是交易数据库的连接池配置

然后抛出一场

将它声明为Bin

名称叫Shad System Statsource

因为这里只是针对于交易数据源行情表做分辨设置

所以我们要调整

交易数据源配置

这个修改下

叫ShadDruid System Statsource

名称我们要做个区分

跟下面名称要区分开来

Primary的注解

咱们要加到下面的方法配置当中

通过ShaddingJetDPC实现交易数据源的代理

增加注释交易数据源ShaddingJetDPC配置

接下来我们从配置当中做具体实现

ShaddingRuleConfiguration

定义Shadding的Rule配置规则

增加注释说明一下

定义ShaddingJetDPC配置处理规则

然后增加表的配置处理规则

因为只针对于行情表做了一个分辨处理

所以我们要将行情表的分辨处理规则加入进去

要新创建一个方法

这里是分表规则的具体配置

咱们创建一个方法

添加注释

K线

行情表

分表配置处理规则

创建一个Table配置规则

Configuration

设置它的逻辑表名称

也就是原始映射的表名称

ShadstockKline

然后设置实际数据源的节点

也就是分库与分片配置信息

这个是分库信息

这个是三张表

这个是五分钟的K线数据表

这个是三十分钟的K线数据表

这里包住错误

这个方法写错

要改成Set

添加对应的注释

这里是分库规则配置

配置实际的分库与分片信息

如果是要实现多库与多分片概率过去设置呢

给大家演示下

Result

Set

Active

Betanose

如果是有多个分库

比如说分了0 1 2 3个库

那么可以通过表达师将分库信息配置进去

如果是有五个库

在这里改成0到5

这个是从0开始计算到5结束

总共是有六个库

接下来就是配置分片信息

比如说ShadstockKline这张表

它分了0到9

10张表

那么在这里去配置0到9

这样就将多个分库与多个分片信息都同时设置进去

我们这里做的是单个分库处理

有多个分片

分片的话

有一分钟五分钟到三十分钟的三张K线数据表

可以直接写上去

以逗号进行分割就可以

接下来还要将咱们之前所实现的分片规则表

所实现的分片规则配置注入进来

将分片规则设置进去

result.setTable

newStandard

setType

newDataSource

table

这里就将分片的设置信息加入进来

最后要返回result

完成行情K线表的分片设置之后

接着去实现数据源的配置

接着设置默认的数据源名称

因为只有单个库

默认名称就指向DataSource 0

然后要将咱们之前实现的分库信息配置加入进来

加入分库信息配置

创建一个Map对象

DataSource

DataSource Map

给它创建一个有序的Map

将数据源配置加入进来

这个我们要将它注入进去

采用AutoWire的注解

根据名称进行注入

这个名称要跟上面保持一致

在这里调整一下

如果是有多个分库需要配置

存入至DataSource Map当中就可以

比如说

这里还规划了一个DataSource 1号数据库

它的一个数据源连接配置

如果是还有2号数据库

以此类推

做相应的配置

可以针对不同的数据库

设定不同的数据源配置信息

这个就是多个分库的配置

接着还可以配置属性

Mobis

这里添加一个属性

开启Circle的日志打印

然后要返回一个DataSource

Sharding

DataSource Factory

Create DataSource

通过Sharding JDBC去创建一个数据源

将咱们的配置信息加入进去

这里可以看到了

Sharding JDBC Configure

New HashMap

Publish

属性配置

这个是DataSource Map

这里可以将数据源做一个调整

ID的工具它没法正常识别

我们就将它改成Dluid DataSource

这下没有爆出错误提示

咱们回到讲义当中

在这里就完成了Dluid多数据源

和Sharding JDBC的集成配置

这一讲内容就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段为一个关于“**ShardingSphere 分库分表实战**”技术课程的实操部分。讲师正在演示如何在 Spring Boot 项目中，通过 ShardingSphere-JDBC 框架，结合 Druid 数据源，实现对“行情 K 线数据”的分库分表配置。核心内容包括：创建并配置多个 Druid 数据源、定义分片规则（特别是针对 K 线表 `t_trade_stock_kline` 的分片策略）、配置数据源映射关系，并最终通过 `ShardingDataSourceFactory` 创建一个可使用的分片数据源。整个过程是典型的 Java 项目配置代码编写与调试演示。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 编辑器中展示课程大纲，明确当前章节为“3.3 行情K线生成功能”。
*   **00:00:05 - 00:00:15**: 切换到 IntelliJ IDEA，展示项目结构和当前正在编辑的 `DruidSystemDataSourceConfiguration.java` 文件。
*   **00:00:15 - 00:00:30**: 讲师开始编写 `tradeSystemDataSource()` 方法，定义两个数据源：`bizSystemDataSource` 和 `tradeSystemDataSource`，并为交易数据源添加 `@Primary` 注解。
*   **00:00:30 - 00:00:45**: 讲师开始编写 `tradeDruidSystemDataSource()` 方法，用于创建一个包含分片规则的 `ShardingRuleConfiguration`。
*   **00:00:45 - 00:01:00**: 讲师定义分片规则，调用 `getKlineTableRule()` 方法获取针对 `t_trade_stock_kline` 表的分片规则配置。
*   **00:01:00 - 00:01:15**: 讲师在 `getKlineTableRule()` 方法中设置分片键为 `t_trade_stock_kline`，并配置实际数据节点（`ds_0` 和 `ds_1`）。
*   **00:01:15 - 00:01:30**: 讲师继续配置分片规则，为 `ds_0` 和 `ds_1` 分别配置数据源。
*   **00:01:30 - 00:01:45**: 讲师创建 `Map<String, DataSource>` 用于存储多个数据源，并将 `ds_0` 和 `ds_1` 的数据源放入其中。
*   **00:01:45 - 00:02:00**: 讲师配置 `ShardingDataSourceFactory`，传入数据源映射、分片规则和属性（如 `sql.show=true`），并返回最终的分片数据源。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **关键代码片段**

*   **数据源配置类 (`DruidSystemDataSourceConfiguration.java`)**

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

        @Bean(name = "tradeDruidSystemDataSource")
        public DataSource tradeDruidSystemDataSource(@Autowired DataSource tradeDruidDataSource) throws Exception {
            ShardingRuleConfiguration shardJdbcConfig = new ShardingRuleConfiguration();
            shardJdbcConfig.getRuleConfigs().add(getKlineTableRule());
            shardJdbcConfig.setDefaultDataSourceName("ds_0");

            Map<String, DataSource> dataSourceMap = new LinkedHashMap<>();
            dataSourceMap.put("ds_0", tradeDruidDataSource);
            dataSourceMap.put("ds_1", tradeDruidDataSource);

            Properties properties = new Properties();
            properties.put("sql.show", true);

            return ShardingDataSourceFactory.createDataSource(dataSourceMap, shardJdbcConfig, new HashMap<>());
        }

        private TableRuleConfiguration getKlineTableRule() {
            TableRuleConfiguration result = new TableRuleConfiguration();
            result.setLogicTable("t_trade_stock_kline");
            result.setActualDataNodes("ds_0.t_trade_stock_kline, ds_1.t_trade_stock_kline");
            return result;
        }
    }
    ```

*   **分片规则配置 (`ShardingRuleConfiguration`)**

    ```java
    ShardingRuleConfiguration shardJdbcConfig = new ShardingRuleConfiguration();
    shardJdbcConfig.getRuleConfigs().add(getKlineTableRule());
    shardJdbcConfig.setDefaultDataSourceName("ds_0");
    ```

*   **分片键与数据节点配置**

    ```java
    result.setLogicTable("t_trade_stock_kline");
    result.setActualDataNodes("ds_0.t_trade_stock_kline, ds_1.t_trade_stock_kline");
    ```

#### **关键概念**

*   **分片策略 (Sharding Strategy)**: 用于定义如何将数据分片到不同的数据节点。
*   **分片规则 (Sharding Rule)**: 包含分片策略和数据节点映射的配置。
*   **数据源映射 (DataSource Map)**: 将逻辑数据源（如 `ds_0`, `ds_1`）映射到实际的物理数据源。
*   **ShardingDataSourceFactory**: 用于根据配置创建最终的分片数据源。

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与配置文件定位**
    *   **描述**: 讲师首先在 IDE 中展示了项目结构，定位到 `config` 包下的 `DruidSystemDataSourceConfiguration.java` 文件，这是本次演示的核心配置文件。

*   **场景二：创建多个 Druid 数据源**
    *   **描述**: 讲师编写了两个 `@Bean` 方法，分别创建了 `bizSystemDataSource` 和 `tradeSystemDataSource`，并为交易数据源添加了 `@Primary` 注解，使其成为默认数据源。

*   **场景三：定义分片规则**
    *   **描述**: 讲师创建了 `tradeDruidSystemDataSource()` 方法，用于配置分片规则。他调用了 `getKlineTableRule()` 方法，该方法定义了逻辑表 `t_trade_stock_kline` 的分片规则，并配置了实际数据节点 `ds_0` 和 `ds_1`。

*   **场景四：配置数据源映射**
    *   **描述**: 讲师创建了一个 `Map<String, DataSource>`，将逻辑数据源 `ds_0` 和 `ds_1` 映射到实际的 Druid 数据源。这是分片数据源创建的关键步骤。

*   **场景五：创建分片数据源**
    *   **描述**: 讲师使用 `ShardingDataSourceFactory.createDataSource(dataSourceMap, shardJdbcConfig, new HashMap<>())` 方法，传入数据源映射、分片规则和属性，最终创建了一个可使用的分片数据源，并将其作为 `@Bean` 返回，供应用程序使用。

*   **场景六：调试与错误处理**
    *   **描述**: 在编写过程中，讲师遇到了编译错误（如 `Expression expected`），并进行了相应的代码修正，例如调整 `Map` 的初始化和赋值方式，确保代码能够正确编译和运行。

---

以上是根据视频画面进行的详细技术分析。讲师通过代码演示，清晰地展示了如何在 Spring Boot 项目中集成 ShardingSphere-JDBC 来实现分库分表功能。
