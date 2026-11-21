# 画面线理解：day08-2-入门案例-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day08-2-入门案例-功能实现2_【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:03, 00:29, 02:21, 02:45, 03:25, 05:01, 06:03, 06:49, 07:16, 07:40, 07:56, 08:24, 10:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:43:24

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中配置 Sharding-JDBC 实现数据库分库分表，包括数据源配置、分片策略和绑定表配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示项目结构，聚焦于 application.properties 文件，高亮显示 mybatis 配置项，用于将下划线命名映射为驼峰命名的实体属性。
画面 2: 展示分片策略配置，定义 store_info 表和 product_info 表的分片策略，使用 store_info_id 和 product_info_id 作为分片键，分片算法为取模。
画面 3: 展示数据源配置，定义了 6 个数据源（m0 到 s2），分别连接到不同的 MySQL 数据库。
画面 4: 展示分库分表的架构图，说明如何将数据分散到不同的数据库和表中。
画面 5: 展示 application.properties 文件，高亮显示定义实体属性映射的配置项。
画面 6: 展示数据源配置，定义了 s2 数据源连接到 product_db_2 数据库。
画面 7: 展示数据源配置，高亮显示 m0 数据源连接到 store_db_0 数据库。
画面 8: 展示项目结构，聚焦于 application.properties 文件，高亮显示数据源配置。
画面 9: 展示分库分表的架构图，说明如何将数据分散到不同的数据库和表中。
画面 10: 展示数据源配置，定义了 m0 到 s2 数据源。
画面 11: 展示分片策略配置，定义 store_info 表和 product_info 表的分片策略。
画面 12: 展示数据源配置，定义了 s0 到 s2 数据源。
画面 13: 展示数据源配置，高亮显示 s2 数据源连接到 product_db_2 数据库。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```properties
spring.main.allow-bean-definition-overriding=true
# 将带有下划线的字段映射为驼峰格式的实体类属性
mybatis.configuration.map-underscore-to-camel-case = true
```

画面 2:
```properties
# store_info分表策略，确定分配到的store_info真实表
spring.shardingsphere.sharding.tables.store_info.actual-data-nodes = ds$->{0..2}.store_info
spring.shardingsphere.sharding.tables.store_info.table-strategy.inline.sharding-column = id
spring.shardingsphere.sharding.tables.store_info.table-strategy.inline.algorithm-expression = store_info
# product_info分表策略，分布在ds1,ds2的product_info表，分片策略为product_info_id % 21，product_info_id取模后加1
spring.shardingsphere.sharding.tables.product_info.actual-data-nodes = ds$->{1..2}.product_info
spring.shardingsphere.sharding.tables.product_info.table-strategy.inline.sharding-column = product_info_id
spring.shardingsphere.sharding.tables.product_info.table-strategy.inline.algorithm-expression = product_info_id % 21
spring.shardingsphere.sharding.tables.product_info.key-generator.type = SNOWFLAKE
```

画面 3:
```properties
# 定义数据源
spring.shardingsphere.datasource.names = m0,m1,m2,s0,s1,s2
spring.shardingsphere.datasource.m0.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m0.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m0.url = jdbc:mysql://localhost:3306/store_db?useUnicode=true
spring.shardingsphere.datasource.m0.username = root
spring.shardingsphere.datasource.m0.password = 123
spring.shardingsphere.datasource.m1.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m1.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m1.url = jdbc:mysql://localhost:3306/product_db_1?useUnicode=true
spring.shardingsphere.datasource.m1.username = root
spring.shardingsphere.datasource.m1.password = 123
spring.shardingsphere.datasource.m2.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m2.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m2.url = jdbc:mysql://localhost:3306/product_db_2?useUnicode=true
spring.shardingsphere.datasource.m2.username = root
spring.shardingsphere.datasource.m2.password = 123
```

画面 4:
```properties
# 设置product_info,product_descript为绑定表，这两张表中的分片键名字必须一致
spring.shardingsphere.sharding.binding-tables = product_info,product_descript
```

画面 5:
```properties
# 定义实体属性映射
spring.shardingsphere.props.sql.show = true
```

画面 6:
```properties
# 主库从库规则数据源定义 ds0/store_db ds1/product_db_1 ds2/product_db_2
spring.shardingsphere.sharding.master-slave-rules.ds0.master-data-source-name = m0
spring.shardingsphere.sharding.master-slave-rules.ds1.master-data-source-name = m1
spring.shardingsphere.sharding.master-slave-rules.ds2.master-data-source-name = m2
```

画面 7:
```properties
spring.shardingsphere.datasource.m0.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m0.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m0.url = jdbc:mysql://localhost:3306/store_db?useUnicode=true
spring.shardingsphere.datasource.m0.username = root
spring.shardingsphere.datasource.m0.password = 123
```

画面 8:
```properties
spring.shardingsphere.datasource.names = m0,m1,m2,s0,s1,s2
spring.shardingsphere.datasource.m0.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m0.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m0.url = jdbc:mysql://localhost:3306/store_db?useUnicode=true
spring.shardingsphere.datasource.m0.username = root
spring.shardingsphere.datasource.m0.password = 123
spring.shardingsphere.datasource.m1.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m1.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m1.url = jdbc:mysql://localhost:3306/product_db_1?useUnicode=true
spring.shardingsphere.datasource.m1.username = root
spring.shardingsphere.datasource.m1.password = 123
spring.shardingsphere.datasource.m2.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m2.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m2.url = jdbc:mysql://localhost:3306/product_db_2?useUnicode=true
spring.shardingsphere.datasource.m2.username = root
spring.shardingsphere.datasource.m2.password = 123
```

画面 9:
```properties
# 设置product_info,product_descript为绑定表，这两张表中的分片键名字必须一致
spring.shardingsphere.sharding.binding-tables = product_info,product_descript
```

画面 10:
```properties
spring.shardingsphere.datasource.names = m0,m1,m2,s0,s1,s2
spring.shardingsphere.datasource.m0.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m0.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m0.url = jdbc:mysql://localhost:3306/store_db?useUnicode=true
spring.shardingsphere.datasource.m0.username = root
spring.shardingsphere.datasource.m0.password = 123
spring.shardingsphere.datasource.m1.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m1.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m1.url = jdbc:mysql://localhost:3306/product_db_1?useUnicode=true
spring.shardingsphere.datasource.m1.username = root
spring.shardingsphere.datasource.m1.password = 123
spring.shardingsphere.datasource.m2.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m2.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m2.url = jdbc:mysql://localhost:3306/product_db_2?useUnicode=true
spring.shardingsphere.datasource.m2.username = root
spring.shardingsphere.datasource.m2.password = 123
```

画面 11:
```properties
# store_info分表策略，确定分配到的store_info真实表
spring.shardingsphere.sharding.tables.store_info.actual-data
