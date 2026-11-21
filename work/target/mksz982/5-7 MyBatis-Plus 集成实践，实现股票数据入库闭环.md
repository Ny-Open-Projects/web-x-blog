# 5-7 MyBatis-Plus 集成实践，实现股票数据入库闭环

## 【学习目标】

学完本节，你应该能够：

- 在最新 Spring Boot 4 下引入 MyBatis-Plus 3.5.14，并正确处理 `mybatis-spring` 版本冲突（排除旧版、单独引新版）；
- 配置 HikariCP 数据源，连接 Docker 中的 MySQL 9；
- 用 `@TableName` + `resultMap` 把 `USStockRss` 实体与 `us_stock_rss` 表映射起来；
- 让 `USStockRssMapper` 继承 `BaseMapper` 白嫖增删改查，并在 `StockService` 中 `insert` 落库；
- 用 `@MapperScan` + 手动 `SqlSessionFactory` 解决 Spring Boot 4 与 MyBatis-Plus 的兼容 gap，打通整条入库闭环。

---

## 【正文】

### 1. 目标：把清洗好的数据落库

前面几节课我们已经把股票新闻清洗得差不多了（标题翻译留到后面章节），现在要把这些数据**保存进数据库**，形成入库闭环。数据库目前是空的，每抓到一批就存一批。这一步用 **MyBatis-Plus** 来做，它在 MyBatis 之上封装了通用 Mapper、分页、代码生成等能力，省去大量样板 XML。

### 2. 引入依赖与排除冲突

在 `pom.xml` 里加上 MyBatis-Plus 的 starter 和 MySQL 驱动。这里有个关键坑：MyBatis-Plus 内部自带的 `mybatis-spring` 版本偏低，和我们用的最新 Spring Boot 4 存在兼容性问题，所以要先把旧的 `mybatis-spring` **排除**掉，再单独引入一个新版本：

```xml
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.5.14</version>
    <exclusions>
        <exclusion>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis-spring</artifactId>
        </exclusion>
    </exclusions>
</dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-spring</artifactId>
    <version>3.0.5</version>
</dependency>
```

要点：`<exclusions>` 把 starter 传递进来的老 `mybatis-spring` 剔除，避免它和新 Spring 体系打架；再显式声明 `3.0.5` 与之匹配。`3.5.14` 是课程验证过的 MyBatis-Plus 版本，`mybatis-spring 3.0.5` 对应 Spring 6 / Boot 3+ 体系，但要注意 Boot 4 仍属较新组合，下面第 7 节会给出因此产生的兼容处理。加完后在 Maven 刷新，把相关依赖都加载进来。

### 3. 配置数据源

把数据源配置粘到 `application.yml`（Spring 配置）里。关键点：

- **URL 地址**：用本地 Docker 容器里的 MySQL；若 MySQL / Docker 在另一台机器，就填那台机器的 IP（内网互通或外网 IP 都行，只要连通）；
- **端口**：课程用的 MySQL 9 映射端口是 `5506`，要改成 `5506`；
- **数据库名（schema）**：改成你自己的库名；
- **用户名 / 密码**：这里都是 `root` / `root`；
- **数据源类型**：默认 `HikariCP`（一位日本开发者写的，速度很快），也可用阿里 Druid 等；
- 字符集 `UTF-8`、SSL 等保持默认。Hikari 连接池参数（池名、最小/最大连接数、自动提交、超时、连接最大生命周期等）建议和讲师保持一致，数据量不用配太大。

> 工程经验：密码明文写在 `application.yml` 仅适合本地。生产应走环境变量或配置中心（如 4-4 节多环境解耦、`982-demo` 的 `${ENV}` 占位），避免密钥入库/入仓。

### 4. 实体与表映射

清洗好的对象是 `USStockRss`，对应的数据库表是 `us_stock_rss`。先给实体加 `@TableName("us_stock_rss")` 建立关联，字段通过 Mapper XML 的 `resultMap` 一一映射：

```java
@Data
@NoArgsConstructor
@AllArgsConstructor
public class USStockRss {
    private String id;
    private String stockCode;
    private String title;
    private String titleZh;
    private String link;
    private LocalDateTime pubDateGmt;
    private LocalDateTime pubDateBj;
    private String tags;
}
```

注意这里属性名是纯驼峰（`stockCode`、`pubDateGmt` 等），与 5-4 节「与列名一致」的版本不同，这正是团队命名约定的差异。无论哪种，关键是和 `resultMap` 对齐。在 `resources/mappers` 下新建 `USStockRssMapper.xml`，定义 `resultMap`，把下划线列映射到驼峰属性：

```xml
<resultMap id="BaseResultMap" type="com.itizixi.entity.USStockRss">
    <id column="id" property="id" />
    <result column="stock_code" property="stockCode" />
    <result column="title" property="title" />
    <result column="title_zh" property="titleZh" />
    <result column="link" property="link" />
    <result column="pub_date_gmt" property="pubDateGmt" />
    <result column="pub_date_bj" property="pubDateBj" />
    <result column="tags" property="tags" />
</resultMap>
```

实体属性名和数据库列名不一致时（如 `stock_code` ↔ `stockCode`），一定要在 `resultMap` 里对上，否则映射会错，这是 MyBatis 最常见的「字段为 null」根因。

### 5. Mapper 接口

建 `mapper` 包，新建 `USStockRssMapper` 接口，让它**继承 `BaseMapper<USStockRss>`**。继承之后，增删改查的面向对象方法（按 id 删除、更新、插入 `insert`、查询等）直接白送，不需要自己写实现：

```java
public interface USStockRssMapper extends BaseMapper<USStockRss> {
}
```

`BaseMapper` 已内置 `insert(T)`、`deleteById`、`updateById`、`selectById`、`selectList` 等，本节的落库只需 `insert(stockNews)`。

### 6. 服务层保存

定义 `StockService` 接口，里面放一个 `saveStockNews(USStockRss)` 方法；再写实现类 `RssServiceImpl`（加 `@Service`），把 `USStockRssMapper` 注入进来，调 `mapper.insert(stockNews)` 完成保存：

```java
public interface StockService {
    public void displayRss() throws Exception;
    public List<SyncEntry> fetchRssFeed(String url) throws Exception;
}
```

> 说明：原稿接口里此处写作 `List<SyncEntry>`，与正文 `SyndEntry` 命名不一致（应是笔误），本节为代码守恒保留原貌；真实工程应统一为 `List<SyndEntry>` 并在实现里对齐。

业务实现里把清洗、转换、取标签、保存串起来：

```java
// 处理时区转换
Date gmtDateTemp = entry.getPublishedDate();
LocalDateTime gmtDate = GMTDateConverter.convertGmtToBeijing(gmtDateTemp);
stockNews.setPubDateGmt(gmtDate);
stockNews.setPubDateBj(GMTDateConverter.convertGmtToBeijing(gmtDateTemp));

// 处理标题翻译
stockNews.setTitleZh("");

// 获取标签
List<String> tagsList = StockTitanCrawler.getTags(titleen);
stockNews.setTags(tagsList);

// 保存数据
stockService.saveStockNews(stockNews);
```

记得在定时任务类里把 `StockService` 注入进来，并在清洗完之后调用 `saveStockNews` 把数据存进去。这里 `setTags(tagsList)` 承接 5-6 节的中文标签列表（原稿片段用 `tagsList` 直接 `setTags`，与 5-6 的 `setTagsZh` 命名略有漂移，真实工程应统一）。

### 7. MyBatis-Plus 统一配置与兼容性问题

MyBatis-Plus 还需要一处统一配置：用 `@MapperScan` 指定 Mapper 接口扫描路径（如 `com.itizixi.mapper`），Mapper XML 位置用 `classpath*:mappers/*.xml` 通配；同时配置 ID 生成策略（这里用「非空」策略）。

实际跑起来会遇到两个典型错误：

1. **`USStockRssMapper` 找不到**：多半是 `@MapperScan` 的包路径两边不一致，扫描不到。把地址对齐即可跳转关联。
2. **`StockService` 注入失败 / 找不到 `SqlSessionFactory` 或 `SqlSessionTemplate`**：这是因为 Spring Boot 4 太新、MyBatis-Plus 版本还没完全跟上，存在兼容性 gap。需要我们**手动**补一个配置类，自己创建 `SqlSessionFactory` 并指定 Mapper XML 位置：

```java
@Configuration
@MapperScan("com.itizixi.mapper")
public class MyBatisPlusConfig {
    @Bean
    public SqlSessionFactory sqlSessionFactory(DataSource dataSource) throws Exception {
        MybatisSqlSessionFactoryBean factoryBean = new MybatisSqlSessionFactoryBean();
        factoryBean.setDataSource(dataSource);
        factoryBean.setMapperLocations(
            new PathMatchingResourcePatternResolver()
                .getResources("classpath*:mappers/*.xml")
        );
        return factoryBean.getObject();
    }
}
```

等后续 MyBatis-Plus 兼容性跟上后，该配置类甚至可以删掉。它的本质是用 `MybatisSqlSessionFactoryBean` 手动装配 `SqlSessionFactory`，把数据源与 Mapper XML 位置显式绑死，绕开自动配置在新 Boot 下失效的问题。

### 8. 运行验证

重启应用，定时任务正常执行，控制台能看到打印输出。去数据库看：一开始 0 条，刷新后数据不断累积，`id`、`stockCode`、`title`、各时间字段、`tags` 都在（中文标题 `titleZh` 暂时为空，留待翻译章节）。一次全量抓取就有上百条记录写进库，入库闭环跑通。

整条「感知 → 清洗 → 落库」链路至此闭合：

```mermaid
flowchart LR
    A[StockTitan RSS] --> B[fetchRssFeed 抓取]
    B --> C[displayRss 清洗映射]
    C --> D[getTags 标签/中文]
    D --> E[stockNews 实体]
    E --> F[StockService.saveStockNews]
    F --> G[USStockRssMapper.insert]
    G --> H[(us_stock_rss 表)]
    H --> I[下游: 翻译/防重/风险判定]
```

---

## 【易错点 / 面试题】

1. **MyBatis-Plus 启动报 `mybatis-spring` 类找不到或方法不兼容。**
   答：starter 自带的 `mybatis-spring` 版本与 Spring Boot 4 不匹配。按本节在 starter 里 `<exclusions>` 剔除旧版，再单独引匹配的 `3.0.5`。面试常考「依赖冲突怎么排查」，`mvn dependency:tree` 看传递依赖、用 exclusion 或 dependencyManagement 锁版本。

2. **`StockService` 注入失败，提示找不到 `SqlSessionFactory`。**
   答：Boot 4 下 MyBatis-Plus 自动配置可能未生效，需如本节手写 `MyBatisPlusConfig`，`@MapperScan` 指定扫描包，并 `setMapperLocations` 指向 XML。注意 `@MapperScan` 的包必须与 Mapper 接口所在包一致。

3. **字段落库后为 null，但对象里明明有值。**
   答：几乎都是 `resultMap` 的 `column ↔ property` 没对齐（如下划线 `stock_code` 没映射到 `stockCode`），或实体属性名与列名约定冲突。逐一核对 `resultMap` 是最快路径；也可开启 MyBatis 日志看最终 SQL 的赋值列。

4. **面试官问：MyBatis-Plus 的 `BaseMapper` 为什么能白送 CRUD？**
   答：`BaseMapper<T>` 在容器启动时由 MyBatis-Plus 通过反射 + 泛型 `T` 的 `@TableName`/`@TableId` 等注解，动态生成对应 Mapper 代理与 SQL 模板，把通用增删改查固化进代理对象，业务只需声明接口继承即可，无需写 XML/实现。

5. **HikariCP 为什么是默认连接池？**
   答：HikariCP 以极简设计与高性能著称（号称最快的 Java 连接池），Spring Boot 默认集成。生产关注 `maximum-pool-size`、`connection-timeout`、`max-lifetime` 三项，避免连接泄漏或老化连接被数据库侧断开。

---

## 【小结】

本节把前面所有清洗成果落进 `us_stock_rss` 表，闭环正式成立。三个工程要点，排除 `mybatis-spring` 旧版解决 Boot 4 冲突、用 `resultMap` 桥接下划线列与驼峰属性、手写 `MyBatisPlusConfig` 补 `SqlSessionFactory` 兼容 gap，是把 MyBatis-Plus 跑在新栈上的关键经验。

从架构看，`us_stock_rss` 表是整条链路的「数据底座」：上游 RSS 接入（5-2）→ 定时抓取（5-3）→ 清洗映射（5-4）→ 标签抓取与中文化（5-5/5-6）→ 落库（本节）。这张表正是下游风险判定的输入源。课程配套工程 `982-demo` 中，`RiskEvaluationService`（`982-demo/src/main/java/com/riskbot/service/RiskEvaluationService.java`）所消费的「感知数据」，与 `us_stock_rss` 扮演的是同一角色，区别在 982-demo 感知的是行情 tick（`QuoteProvider` 抽象、MySQL 持久化），本课感知的是资讯条目。理解本节落库闭环，就掌握了「外部杂乱数据 → 稳定库表」的最后一块拼图，为后续防重（5-8/5-9）与翻译（7-x）提供了可依赖的持久层。
