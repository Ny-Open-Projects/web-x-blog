# 画面线理解：day08-4-入门案例-功能实现4

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day08-4-入门案例-功能实现4_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:18, 00:54, 01:20, 01:29, 01:48, 02:06, 02:35, 04:00, 04:57, 05:21, 05:54, 06:09, 06:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:45:14

1) 这一组画面整体在讲如何通过 Sharding-JDBC 配置实现商品信息表（product_info）和商品描述表（product_description）的分库分表，并展示对应的 Java Mapper 接口定义。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 application.properties 中配置了主库（ds0）和从库（ds1, ds2）的数据库连接信息，以及分库分表规则的初始设置。
画面2: 展示 application.properties 中为 product_info 表配置了分片策略，包括分片键、分片算法、数据源映射和主键生成器。
画面3: 展示 application.properties 中为 product_description 表配置了分片策略，包括分片键、分片算法、数据源映射和主键生成器，并配置了绑定表。
画面4: 展示 ProductDao.java 中定义了插入 product_info 和 product_description 表的 SQL 语句，以及查询两个表关联数据的 SQL 语句。
画面5: 展示数据库架构图，包含 STORE_DB 和 PRODUCT_DB_2 两个数据库，每个数据库下有多个表，表之间通过外键关联。
画面6: 展示 ProductDao.java 中的 insertProductDescription 方法，用于插入 product_description 表数据。
画面7: 展示 ProductDao.java 中的 selectProductList 方法，用于查询 product_info 和 product_description 表关联数据。
画面8: 展示 ProductDao.java 中的 insertProductInfo 方法，用于插入 product_info 表数据。
画面9: 展示 ProductDao.java 中的 insertProductDescription 方法，用于插入 product_description 表数据。
画面10: 展示 ProductDao.java 中的 insertProductDescription 方法，用于插入 product_description 表数据。
画面11: 展示 ProductDao.java 中的 insertProductDescription 方法，用于插入 product_description 表数据。
画面12: 展示 application.properties 中配置了 product_info 和 product_description 表的绑定关系。
画面13: 展示 ProductDao.java 中的 insertProductDescription 方法，用于插入 product_description 表数据。
画面14: 展示 ProductDao.java 中的 selectProductList 方法，用于查询 product_info 和 product_description 表关联数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```properties
spring.shardingsphere.datasource.ds0.url = jdbc:mysql://localhost:3307/product_db_2?useUnicode=true
spring.shardingsphere.datasource.ds0.username = root
spring.shardingsphere.datasource.ds0.password = 123
# 主库从库通过数据源定义 ds0, ds1, ds2 分别对应 product_db_2, product_db_1, product_db_2
spring.shardingsphere.sharding.master-slave-rules.ds0.master-data-source-name=ds0
spring.shardingsphere.sharding.master-slave-rules.ds0.slave-data-source-names=ds1
spring.shardingsphere.sharding.master-slave-rules.ds1.master-data-source-name=ds1
spring.shardingsphere.sharding.master-slave-rules.ds1.slave-data-source-names=ds0
spring.shardingsphere.sharding.master-slave-rules.ds2.master-data-source-name=ds2
spring.shardingsphere.sharding.master-slave-rules.ds2.slave-data-source-names=ds0
# 分库策略，以 store_info_id 为分片键，分片策略为 ds0, ds1, ds2
spring.shardingsphere.sharding.default-database-strategy.inline.sharding-column = store_info_id
spring.shardingsphere.sharding.default-database-strategy.inline.algorithm-expression = ds${store_info_id % 2}
# store_info 分表策略，固定分配到 store_info 表
spring.shardingsphere.sharding.tables.store_info.actual-data-nodes = ds${0..2}.store_info
spring.shardingsphere.sharding.tables.store_info.table-strategy.inline.sharding-column = store_info_id
spring.shardingsphere.sharding.tables.store_info.table-strategy.inline.algorithm-expression = ds${store_info_id % 2}
spring.shardingsphere.sharding.tables.store_info.key-generator.type = SNOWFLAKE
```

画面2:
```properties
# product_info 分表策略，分片键为 product_info_id，分片策略为 ds${product_info_id % 2}，分片算法为取模算法
spring.shardingsphere.sharding.tables.product_info.actual-data-nodes = ds${0..2}.product_info
spring.shardingsphere.sharding.tables.product_info.table-strategy.inline.sharding-column = product_info_id
spring.shardingsphere.sharding.tables.product_info.table-strategy.inline.algorithm-expression = ds${product_info_id % 2}
spring.shardingsphere.sharding.tables.product_info.key-generator.type = SNOWFLAKE
```

画面3:
```properties
# product_description 分表策略，分片键为 product_description_id，分片策略为 ds${product_description_id % 2}，分片算法为取模算法
spring.shardingsphere.sharding.tables.product_description.actual-data-nodes = ds${0..2}.product_description
spring.shardingsphere.sharding.tables.product_description.table-strategy.inline.sharding-column = product_description_id
spring.shardingsphere.sharding.tables.product_description.table-strategy.inline.algorithm-expression = ds${product_description_id % 2}
spring.shardingsphere.sharding.tables.product_description.key-generator.type = SNOWFLAKE
# 设置 product_info, product_description 为绑定表，这两张表中的分片键名字必须一致
spring.shardingsphere.sharding.binding-tables = product_info,product_description
# 打开 sql 输出日志
spring.shardingsphere.props.sql-show = true
```

画面4:
```java
@Mapper
@Component
public interface ProductDao {

    @Insert("insert into product_info(store_info_id,product_name,spec,region_code,price,image_url) value(#(storeInfoId),#(productName),#(spec),#(regionCode),#(price),#(imageUrl))")
    int insertProductInfo(ProductInfo productInfo);

    @Insert("insert into product_description(product_info_id,describe,store_info_id) value(#(productInfoId),#(describe),#(storeInfoId))")
    @Options(useGeneratedKeys = true, keyProperty = "id", keyColumn = "id")
    int insertProductDescription(ProductDescription productDescription);

    @Select("select i.*, d.describe from product_info i inner join product_description d on i.product_info_id = d.product_info_id")
    List<ProductInfo> selectProductList();
}
```

画面6:
```java
@Insert("insert into product_description(product_info_id,describe,store_info_id) value(#(productInfoId),#(describe),#(storeInfoId))")
@Options(useGeneratedKeys = true, keyProperty = "id", keyColumn = "id")
int insertProductDescription(ProductDescription productDescription);
```

画面7:
```java
@Select("select i.*, d.describe from product_info i inner join product_description d on i.product_info_id = d.product_info_id")
List<ProductInfo> selectProductList();
```

画面8:
```java
@Insert("insert into product_info(store_info_id,product_name,spec,region_code,price,image_url) value(#(storeInfoId),#(productName),#(spec),#(regionCode),#(price),#(imageUrl))")
int insertProductInfo(ProductInfo productInfo);
```

画面9:
```java
@Insert("insert into product_description(product_info_id,describe,store_info_id) value(#(productInfoId),#(describe),#(storeInfoId))")
@Options(useGeneratedKeys = true, keyProperty = "id", keyColumn = "id")
int insertProductDescription(ProductDescription productDescription);
```

画面10:
```java
@Insert("insert into product_description(product_info_id,describe,store_info_id) value(#(productInfoId),#(describe),#(storeInfoId))")
@Options(useGeneratedKeys = true, keyProperty = "id", keyColumn = "id")
int insertProductDescription(ProductDescription productDescription);
```

画面11:
```java
@Insert("insert into product_description(product_info_id,describe,store_info_id) value(#(productInfoId),#(describe),#(storeInfoId))")
@Options(useGeneratedKeys = true, keyProperty = "id", keyColumn = "id")
int insertProductDescription(ProductDescription productDescription);
```

画面12:
```properties
# 设置 product_info, product_description 为绑定表，这两张表中的分片键名字必须一致
spring.shardingsphere.sharding.binding-tables = product_info,product_description
```

画面13:
```java
@Insert("insert into product_description(product_info_id,describe,store_info_id) value(#(productInfoId),#(describe),#(storeInfoId))")
@Options(useGeneratedKeys = true, keyProperty = "id", keyColumn = "id")
int insertProductDescription(ProductDescription productDescription);
```

画面14:
```java
@Select("select i.*, d.describe from product_info i inner join product_description d on i.product_info_id = d.product_info_id")
List<ProductInfo> selectProductList();
```

4) 出现的 PPT 标题、架构图/
