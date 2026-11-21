# 10-行情K线数据处理-Druid多数据源与Shardin — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来开始实现全局序列ID的配置

ShoutingJDBC它不支持自身序列

如果每个表都采用自己的自身序列

它就会出现一个问题

也就是ID会容易出现重复的情况

每个表都有自己的自身序列

ShoutingJDBC通过分片设置

那么不同表的话

这些自身序列就会产生对应的冲突

所以我们需要采用前面所讲到的全局序列方案

去生成唯一的表组件的ID

这里通过JPG对数据层进行操作

所以我们需要去除GenerateValue这个注解

不要让它自动生成唯一ID

交易数据源采用的是PostGridCircle

数据库属性是采用小写

所以我们要在实体上面加上映射

否则Circle处理的时候不能识别

会爆出错误

好

那么我们就来修改

实体的相关配置

回到代码当中

打开ChadstockKlan这个实体

这里我们已经去除了它的负类BaseN体

可以看到

那么直接在这里去定义它的ID

采用ID注解就可以

不需要再采用之前的GenerateValue这个注解

然后我们回到代码

可以看到每个属性都会配置它的列属性的映射

最后我们再来复杂它的列属性的映射

注意PGCircle里面的表属性是采用小写

那么在配置映射的时候

全部要采用小写

如果说你发起的是一个驼峰的命名进行查询

比如说Stalk这里有个大写

那么PGCircle它执行的时候是无法正常识别

会爆出错误

这个是由于ShardingJDBC

在针对PGCircle做适配的时候

没有帮我们进行Circle的自动转换

这是因为ShardingJDBC在进行Circle映射处理的时候

没有帮我们进行Circle的自动转换

这是因为ShardingJDBC在进行Circle映射处理的时候

没有帮我们进行Circle映射处理的时候

没有针对PGCircle做大小写的转换适配

所以这里我们要注意一下

采用Chromium去直接映射它的属性

这样ShardingJDBC发送过去的Circle语句

就是咱们这里所定义的属性名称

配置完实体之后

接下来我们还要去修改它的全局ID配置

这个配置是在Ladies Configuration当中

去增加全局ID的生成器

咱们把它copy进来

回到代码当中

找到Ladies Configuration

在行情服务工程下面

加入到上面

添加对应的包

Spring Framework下面

然后要去添加属性配置

在工程配置的最下面

添加Snowflake的雪花算法的配置

Snowflake

加上说明

这个是全局ID的配置

全局唯一ID分布式标识的配置

然后是Work ID

Data Center ID

确保它们的值是唯一就可以

好

配置完成之后

我们回到讲义当中

以上配置完成之后

那数据层接口该怎么去调用和实现呢

这里就是它所需要修改的地方

保存的数据层接口还是不变

只需要通过全局唯一ID

设置它的ID值就可以

好

因为K线生成的处理逻辑

目前还没有实现

所以这一块暂时不用调整

在讲解行情服务K线生成处理逻辑的时候

咱们再做具体的完善

好

下面是Sharding JDBC的参考文档

如果大家想更详细的了解Sharding JDBC

可以参考对应的文档资料

这个是官方所提供出来的参考文档

上面呢

有更详细

更全面的说明

好

这一讲就是对Sharding JDBC全局序列ID的配置实现

那这一讲内容

咱们先讲到这里

好

谢谢大家的观看

我们下期再见

拜拜

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段为一个关于“行情K线数据处理”的技术课程，主要讲解如何在使用 ShardingJDBC 进行数据库分库分表时，解决因各分表使用独立自增主键而导致的 ID 冲突问题。讲师通过代码演示，阐述了采用全局唯一 ID 生成方案（如 Snowflake）的必要性，并展示了如何在 Spring Boot 项目中集成 Redis 作为 ID 生成器，以及如何在实体类和业务逻辑中应用该方案。核心内容包括：ShardingJDBC 的分库分表配置、全局 ID 生成器的实现、以及在 K 线数据持久化时注入并使用全局 ID。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师在 Typora 文档中定位到“第2章 行情K线数据的处理”下的“4. 全局序列ID配置”章节，引出本节主题。
*   **00:05 - 00:15**: 讲师解释 ShardingJDBC 不支持自增序列，若每个分表都使用自增主键，会导致 ID 冲突。因此，必须采用全局序列方案。
*   **00:15 - 00:25**: 讲师指出，为避免冲突，需要通过 PA（Proxy Agent）对数据库层进行操作，并强调需要移除 `@GeneratedValue(strategy = GenerationType.IDENTITY)` 注解。
*   **00:25 - 00:35**: 讲师提到，由于数据库是 PostgreSQL，且属性名采用小写，需要添加映射，否则会报 `java.lang.IndexOutOfBoundsException` 异常。
*   **00:35 - 00:45**: 讲师展示并解释了 `DataSourceTableAlg()` 的配置代码，用于定义分表策略。
*   **00:45 - 00:55**: 讲师切换到 IntelliJ IDEA，展示实体类 `TradeStockKline` 的代码，其中包含 `@Table(name="t_trade_stock_kline")` 和 `@Id` 注解。
*   **00:55 - 01:05**: 讲师在 IDEA 中滚动查看实体类的字段，包括 `stockId`, `stockCode`, `stockName`, `priceOpen` 等。
*   **01:05 - 01:15**: 讲师回到 Typora，展示如何在 `RedisConfiguration` 类中配置 Snowflake 的 `workerId` 和 `datacenterId`。
*   **01:15 - 01:25**: 讲师在 IDEA 中展示 `RedisConfiguration` 类的完整代码，包括 `@EnableCaching` 注解和 `redisTemplate` 的配置。
*   **01:25 - 01:35**: 讲师展示 `RedisConfiguration` 中的 `globalIDGenerator()` 方法，该方法根据 `workerId` 和 `datacenterId` 创建并返回一个 `GlobalIDGenerator` 实例。
*   **01:35 - 01:45**: 讲师展示 `bootstrap-dev.yml` 配置文件，其中包含数据库连接、Web 配置、登录凭证等信息。
*   **01:45 - 01:55**: 讲师回到 Typora，展示在 `StockQuoteServiceImpl` 类中注入 `GlobalIDGenerator` 的代码。
*   **01:55 - 02:05**: 讲师展示在 `StockQuoteServiceImpl` 中，如何在保存 K 线数据时调用 `globalIDGenerator.nextId()` 来生成全局唯一 ID。
*   **02:05 - 02:15**: 讲师在 Typora 中展示 ShardingJDBC 的官方文档链接，作为后续学习的参考。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 文本内容**:
    *   **章节标题**: “4. 全局序列ID配置”
    *   **核心问题**: “ShardingJDBC 不支持自增序列...会出现ID重复的情况”
    *   **解决方案**: “采用前面所讲到的全局序列方案，生成唯一的ID”
    *   **技术要点**: “需要去除@GeneratedValue(strategy = GenerationType.IDENTITY)”
    *   **异常信息**: `java.lang.IndexOutOfBoundsException: Index: 0, Size: 0`
    *   **配置代码**: `result.setTableShardingStrategyConfig(new StandardShardingStrategyConfiguration("dataType", new DataSourceTableAlg()));`
    *   **配置文件**: `bootstrap-dev.yml` 中的 `login-username` 和 `login-password`。
    *   **文档链接**: `https://shardingsphere.apache.org/document/current/en/overview/`

*   **代码关键内容**:
    *   **实体类 `TradeStockKline`**:
        ```java
        @Entity
        @Table(name = "t_trade_stock_kline")
        public class TradeStockKline implements Serializable {
            @Id
            @ApiModelProperty(hidden = true)
            private Long id;
            @Column(name = "stockid")
            private Long stockId;
            @Column(name = "stockcode")
            private String stockCode;
            @Column(name = "stockname")
            private String stockName;
            @Column(name = "priceopen")
            private Long priceOpen;
            @Column(name = "datatype")
            private Integer dataType;
        }
        ```
    *   **配置类 `RedisConfiguration`**:
        ```java
        @Configuration
        @EnableCaching
        public class RedisConfiguration extends CachingConfigurerSupport {
            @Value("${snowflake.workerId}")
            private Long workerId;
            @Value("${snowflake.datacenterId}")
            private Long datacenterId;

            @Bean
            public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory factory) {
                RedisTemplate<String, Object> redisTemplate = new RedisTemplate<String, Object>();
                redisTemplate.setKeySerializer(new StringRedisSerializer());
                redisTemplate.setConnectionFactory(factory);
                return redisTemplate;
            }

            @Bean
            public GlobalIDGenerator globalIDGenerator() {
                if (null == workerId || null == datacenterId) {
                    return new GlobalIDGenerator();
                }
                return new GlobalIDGenerator(workerId, datacenterId);
            }
        }
        ```
    *   **业务逻辑 `StockQuoteServiceImpl`**:
        ```java
        @Autowired
        private GlobalIDGenerator globalIDGenerator;

        // 在保存K线数据时
        kline.setId(globalIDGenerator.nextId());
        tradeStockKlineRepository.save(kline);
        ```

---

### 4) 关键场景与演示描述

*   **场景一：问题提出与方案选择 (00:00-00:15)**
    *   讲师在 Typora 文档中定位到“全局序列ID配置”章节。
    *   通过文字描述，明确指出 ShardingJDBC 的分库分表特性与自增主键冲突的问题。
    *   强调必须采用“全局序列方案”来生成唯一的 ID。

*   **场景二：技术实现与配置 (00:15-01:35)**
    *   讲师展示如何通过 `DataSourceTableAlg()` 配置分表策略。
    *   切换到 IntelliJ IDEA，展示 `TradeStockKline` 实体类的代码，说明其字段映射。
    *   回到 Typora，展示 `RedisConfiguration` 类的代码，说明如何通过 Spring 的 `@Value` 注解注入 Snowflake 的配置参数。
    *   在 IDEA 中展示 `RedisConfiguration` 的完整代码，包括 `redisTemplate` 和 `globalIDGenerator` 的配置。
    *   展示 `globalIDGenerator()` 方法，说明其根据配置参数创建 ID 生成器实例。

*   **场景三：业务集成与应用 (01:35-02:05)**
    *   讲师展示 `bootstrap-dev.yml` 配置文件，说明项目的基础配置。
    *   回到 Typora，展示在 `StockQuoteServiceImpl` 中如何注入 `GlobalIDGenerator`。
    *   展示在业务逻辑中调用 `nextId()` 方法生成 ID 并赋值给 K 线对象。
    *   最后，讲师提供了 ShardingJDBC 的官方文档链接，鼓励学员深入学习。

---

以上是根据视频画面进行的结构化技术分析。
