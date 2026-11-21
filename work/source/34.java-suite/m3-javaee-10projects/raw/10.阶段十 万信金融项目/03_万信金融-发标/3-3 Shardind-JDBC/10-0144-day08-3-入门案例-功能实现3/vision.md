# 画面线理解：day08-3-入门案例-功能实现3

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day08-3-入门案例-功能实现3_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 01:36, 04:28, 05:31, 06:16, 06:51, 08:22, 09:38, 10:27, 10:58, 11:38, 12:12, 12:44, 13:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:44:20

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Sharding-JDBC 配置文件中定义数据源、分库分表策略（包括主从库规则、分库策略、分表策略、绑定表）以及开启 SQL 日志输出。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了项目结构，当前编辑的是 `application.properties` 文件。
- 配置了两个数据源 ds0 和 ds1，分别指向不同的数据库（product_db_2 和 product.db_2）。
- 配置了主从库规则，ds0 的从库是 ds1，ds1 的从库是 ds2。
- 注释说明了“定义逻辑数据源（主从对应关系）”。

画面 2：
- 继续编辑 `application.properties` 文件。
- 配置了分库策略，使用 `store_info_id` 作为分片列，算法为 `ds${store_info_id % 2 + 1}`。
- 注释说明了“分库策略”和“分表策略”。
- 屏幕下方弹出两个 PPT 页面，内容是关于分库分表的示意图。

画面 3：
- 展示了数据源 ds0 和 ds1 的详细配置，包括驱动、URL、用户名和密码。
- 注释说明了“定义逻辑数据源（主从对应关系）”。

画面 4：
- 继续编辑 `application.properties` 文件。
- 配置了分库策略，使用 `store_info_id` 作为分片列，算法为 `ds${store_info_id % 2 + 1}`。
- 注释说明了“分库策略”和“分表策略”。
- 配置了 `store_info` 表的分表策略，分片列是 `id`，算法为 `store_info`。

画面 5：
- 展示了多个窗口，包括 PPT、代码编辑器和数据库管理工具。
- PPT 页面显示了分库分表的架构图。
- 代码编辑器中配置了 `product_info` 表的分片策略，分片列是 `product_info_id`，算法为 `product_info_id % 2 + 1`。
- 注释说明了“分表策略”。

画面 6：
- 继续编辑 `application.properties` 文件。
- 配置了 `product_info` 表的分片策略，分片列是 `product_info_id`，算法为 `product_info_id % 2 + 1`。
- 配置了 `product_info` 表的主键生成策略，类型为 `SNOWFLAKE`。
- 注释说明了“分表策略”和“设置主键”。

画面 7：
- 继续编辑 `application.properties` 文件。
- 配置了 `product_info` 表的分片策略，分片列是 `product_info_id`，算法为 `product_info_id % 2 + 1`。
- 配置了 `product_info` 表的主键生成策略，类型为 `SNOWFLAKE`。
- 注释说明了“分表策略”和“设置主键”。

画面 8：
- 继续编辑 `application.properties` 文件。
- 配置了 `product_info` 表的分片策略，分片列是 `product_info_id`，算法为 `product_info_id % 2 + 1`。
- 配置了 `product_info` 表的主键生成策略，类型为 `SNOWFLAKE`。
- 注释说明了“分表策略”和“设置主键”。

画面 9：
- 继续编辑 `application.properties` 文件。
- 配置了 `product_info` 表的分片策略，分片列是 `product_info_id`，算法为 `product_info_id % 2 + 1`。
- 配置了 `product_info` 表的主键生成策略，类型为 `SNOWFLAKE`。
- 注释说明了“分表策略”和“设置主键”。

画面 10：
- 继续编辑 `application.properties` 文件。
- 配置了 `product_info` 表的分片策略，分片列是 `product_info_id`，算法为 `product_info_id % 2 + 1`。
- 配置了 `product_info` 表的主键生成策略，类型为 `SNOWFLAKE`。
- 注释说明了“分表策略”和“设置主键”。

画面 11：
- 继续编辑 `application.properties` 文件。
- 配置了 `product_info` 表的分片策略，分片列是 `product_info_id`，算法为 `product_info_id % 2 + 1`。
- 配置了 `product_info` 表的主键生成策略，类型为 `SNOWFLAKE`。
- 注释说明了“分表策略”和“设置主键”。

画面 12：
- 继续编辑 `application.properties` 文件。
- 配置了 `product_info` 表的分片策略，分片列是 `product_info_id`，算法为 `product_info_id % 2 + 1`。
- 配置了 `product_info` 表的主键生成策略，类型为 `SNOWFLAKE`。
- 注释说明了“分表策略”和“设置主键”。

画面 13：
- 展示了 PPT 页面，内容是关于 Sharding-JDBC 的配置。
- 屏幕下方弹出一个 PPT 页面，内容是关于分库分表的架构图。
- 代码编辑器中配置了数据源 ds0 和 ds1 的详细信息。

画面 14：
- 继续编辑 `application.properties` 文件。
- 配置了 `product_info` 表的分片策略，分片列是 `product_info_id`，算法为 `product_info_id % 2 + 1`。
- 配置了 `product_info` 表的主键生成策略，类型为 `SNOWFLAKE`。
- 注释说明了“分表策略”和“设置主键”。
- 配置了 `product_info` 和 `product_descript` 表的绑定关系。
- 配置了 SQL 日志输出开关 `spring.shardingsphere.props.sql-show=true`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```
spring.shardingsphere.datasource.ds0.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.ds0.url = jdbc:mysql://localhost:3307/product_db_2?useUnicode=true
spring.shardingsphere.datasource.ds0.username = root
spring.shardingsphere.datasource.ds0.password = 123

# 定义逻辑数据源（主从对应关系）
spring.shardingsphere.sharding.master-slave-rules.ds0.master-data-source-name=ds0
spring.shardingsphere.sharding.master-slave-rules.ds0.slave-data-source-names=ds1
spring.shardingsphere.sharding.master-slave-rules.ds1.master-data-source-name=ds1
spring.shardingsphere.sharding.master-slave-rules.ds1.slave-data-source-names=ds2
```

画面 2：
```
# 分库策略
spring.shardingsphere.sharding.default-database-strategy.inline.sharding-column = store_info_id
spring.shardingsphere.sharding.default-database-strategy.inline.algorithm-expression = ds${store_info_id % 2 + 1}

# 分表策略 - 表
spring.shardingsphere.sharding.tables.store_info.actual-data-nodes = ds${0}.store_info
spring.shardingsphere.sharding.tables.store_info.table-strategy.inline.sharding-column = id
spring.shardingsphere.sharding.tables.store_info.table-strategy.inline.algorithm-expression = store_info
```

画面 3：
```
spring.shardingsphere.datasource.ds0.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.ds0.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.ds0.url = jdbc:mysql://localhost:3307/store_db?useUnicode=true
spring.shardingsphere.datasource.ds0.username = root
spring.shardingsphere.datasource.ds0.password = 123

spring.shardingsphere.datasource.ds1.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.ds1.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.ds1.url = jdbc:mysql://localhost:3307/product_db_2?useUnicode=true
spring.shardingsphere.datasource.ds1.username = root
spring.shardingsphere.datasource.ds1.password = 123
```

画面 4：
```
# 分库策略
spring.shardingsphere.sharding.default-database-strategy.inline.sharding-column = store_info_id
spring.shardingsphere.sharding.default-database-strategy.inline.algorithm-expression = ds${store_info_id % 2 + 1}

# 分表策略 - 表
spring.shardingsphere.sharding.tables.store_info.actual-data-nodes = ds${0}.store_info
spring.shardingsphere.sharding.tables.store_info.table-strategy.inline.sh
