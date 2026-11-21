# 画面线理解：day08-5-入门案例-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day08-5-入门案例-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 01:07, 02:30, 03:25, 04:32, 05:24, 06:50, 07:57, 08:43, 10:11, 10:50, 11:22, 11:52, 12:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:46:09

1) 这一组画面整体在讲什么（一句话）：
演示 Sharding-JDBC 如何通过商品 ID 的奇偶性实现分库分表，并验证读写分离和数据同步功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT，标题为“2.3.6 测试”，列出测试要点：通过创建商品接口验证分库（store_info_id 奇偶）、分表（product_id 奇偶）、主从数据同步、商品查询接口验证读写分离。
画面 2: 与画面 1 相同，为 PPT 页面。
画面 3: 屏幕空白，无内容。
画面 4: 展示 Swagger UI 的 POST /products 接口，用于添加商品，参数为 productInfo。
画面 5: 展示数据库管理工具，连接到 product_db_1，显示其包含的表：product_info_1, product_info_2, product_descript_1, product_descript_2。
画面 6: 展示 Swagger UI 的响应，成功创建商品，返回状态码 200 和“创建成功！”。
画面 7: 展示数据库管理工具，连接到 product_db_2，显示其包含的表：product_info_1, product_info_2, product_descript_1, product_descript_2。
画面 8: 与画面 1 相同，为 PPT 页面。
画面 9: 展示 IDEA 中的 application.properties 配置文件，配置了分库分表规则，包括 store_info 和 product_info 表的分片策略。
画面 10: 展示数据库管理工具，连接到 product_db_2，显示其包含的表：product_info_1, product_info_2, product_descript_1, product_descript_2。
画面 11: 展示 Swagger UI 的 GET /products 接口，用于查询商品列表。
画面 12: 展示 IDEA 中的 application.properties 配置文件，显示了分库分表的 SQL 执行日志，包括实际执行的 SQL 语句和逻辑 SQL。
画面 13: 展示 IDEA 中的 application.properties 配置文件，显示了分库分表的 SQL 执行日志，包括实际执行的 SQL 语句和逻辑 SQL。
画面 14: 展示 IDEA 中的 application.properties 配置文件，显示了分库分表的 SQL 执行日志，包括实际执行的 SQL 语句和逻辑 SQL。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 9:
spring.shardingsphere.sharding.tables.store_info.actual-data-nodes = ds$->{0}.store_info
spring.shardingsphere.sharding.tables.store_info.table-strategy.inline.algorithm-expression = store_info_id % 2
spring.shardingsphere.sharding.tables.product_info.actual-data-nodes = ds$->{0,1,2}.product_info
spring.shardingsphere.sharding.tables.product_info.table-strategy.inline.algorithm-expression = product_info_id % 2
spring.shardingsphere.sharding.tables.product_info.key-generator.type = SNOWFLAKE
spring.shardingsphere.sharding.tables.product_descript.actual-data-nodes = ds$->{0,1,2}.product_descript
spring.shardingsphere.sharding.tables.product_descript.table-strategy.inline.algorithm-expression = product_descript_id % 2
spring.shardingsphere.sharding.tables.product_descript.key-generator.type = SNOWFLAKE

画面 12:
Actual SQL: s1: insert into product_descript_1 (product_info_id, descrip, store_info_id, id) VALUES (?,?,?,?)
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_descript_d on i.product_info_id = d.product_info_id
Actual SQL: s1: select i.*, d.descrip from product_info_1 inner join product_des
