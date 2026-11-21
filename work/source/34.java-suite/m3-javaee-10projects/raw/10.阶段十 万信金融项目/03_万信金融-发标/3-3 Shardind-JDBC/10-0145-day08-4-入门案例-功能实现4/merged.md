# day08-4-入门案例-功能实现4

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day08-4-入门案例-功能实现4_【海量资源尽在 666java.com】.mp4
- 时长 6分25秒（音频 386s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们把入门案例当中这一堆配置啊全部给大家讲一讲这里边的话重点就是看跟什么呀sharding gun gdbc 有关的这些配置啊的确是非常多因为咱这里边是主同架构嘛啊所以说库也比较多表也比较多我整个下来这个配置代码非常多而且这一块呢是非常细心的一个活这个代码你也不用敲啊你可以直接粘过去拿用但是这里边有些地方呢这个数据你得改改比如说这个招商密码
[00:30] 你不一定跟忘了一样吧对不对包括这个端口号啊等等等等啊所以你一定要细心啊必须非常非常细心那配置搞完之后咱进来是不是应该是编写加代码来实现比如说这个增删改查这些功能对不对但是呢这些功能都非常简单而且我们前面给大家说过啊在使用sharding干gdbc的时候呢其实主要玩的是不是就是这个配置加代码跟以往都是一样
[00:59] 所以你看这里边control了呀DOO呀实体内呀要层代码我就不再挨个给人家讲了啊人家下去可以自己看一下那这里边呢我们重点看一看这个持久层的这俩接口就行因为咱这个现在研究的毕竟是这个数据库操作嘛咱把这个持久层就是道层的这个代码咱打开看一看就行了你看我们这个product的道它主要是操作哪个表的你应该能猜出来吧
[01:28] 他肯定是操作操作这个商品信息还有商品描述这个商品表对不对他这里边呢定义了三个方法咱瞅一瞅啊一个是往product info表里边插入数据就这个商品信息表一个是你看这个名字啊一个是往这个商品描述这个表里边来插入数据这俩都是保存最后一个你看名字应该能看出来这是一个什么呀查询就查询这个商品列表啊我们就这三个方案就够了
[01:58] 这个这这两个不是增杉改下当中的增嘛这个就是增杉改下当中的什么呀查询啊这个那由于我们使用的是mybattis所以说这里边的sql语句我们在自己编写一下这个我就不再过多说了啊这个大家比较熟那这里边有个细节需要强调就是这个配置前面我们在讲这个sharing-gdbc的配置的时候我们说过啊咱们product info呀还有这个呃productdescript描述啊这两张表里边是不是主见都是采用什么呀
[02:31] 对雪花算法来自动生成是不是所以说呢这两个表的主件的值我们需要提供吗我们不需要提供你说我们相当于是由雪花算法是不是生成啊对不对所以这样呢我们应该加这种配置就是告诉my balance那就是我这个两张表里边的主件是自动生成的你不用管啊你不用管所以这个地方要给处然后还要告诉他这个我的主件的字段名是谁这两张表
[03:02] 主件的字段名是谁以及它对应的实体类当中的属性名是谁这个你就照着写就行了啊也就是细心一点别写错啊主要是给大家强调这个配置是用来就是让my balance知道啊我们两张表的这两个主件是由雪花算法来生成咱不用管啊给值的时候你看我可没给啊你看看这个搜索语句我这里边给主件复制了吗没有啊你看product info
[03:32] prodactinfo里边主件叫productinfo idea你看我这里边出现这个字段了没有没有我就没管他我刚才说了他有他是有雪花算法生成的咱们不用管而且这个配置还可以起到另外一个作用就是他会把生成的主件的值作为返还值干什么呀返回了你看我这个方案是不是有一个硬的类型的返还值对不对可以把雪花算法生成的主件的值给返回了你可以拿着用一下对不对然后下面这是一个多表观点查询是不是商品信息表
[04:03] 和这个什么呀商品描述啊这两张表一个一个什么关联查询那这呢我要提醒大家注意啊你看我们在做增加改查的时候这个搜捕语句跟之前写的有区别吗有区别没有感觉上没区别是吧你确定没区别吗大家看好啊我选中的这些地方你看这个这个还有这俩地方这几个地方是不是表名啊是表的名字不是是不是
[04:36] 你确定咱们的数据库里边不管是主库还是存库里边有这样的表吗有吗你再瞅瞅啊咱们的表名里边都带着-1-2-1-2的呀是不是这才是真实的表明但是你看你在写搜索语的时候这有没有-1-2没有啊语法的确是一样但是你要注意这个表名这叫什么名这叫逻辑名有印象吗对我们写的都是逻辑名啊搜索语里边一定要写逻辑名
[05:07] 逻辑表逻辑表逻辑表逻辑表逻辑表就是这种名字是不带什么-1-0-2这种东西带有-0-1-2的这是真实表的表而我们现在写词录语写的是逻辑表的表那有的学生说老师你这写了一个逻辑表的表明它都不是真实存在的一个表这能实现自然改善吗可以我们这就应该写逻辑表的表明然后呢由sharding-gdbc根据什么呀
[05:38] 根据这一套配置来决定最终这个数据应该是插入到product info1还是product info2明白什么意思吧所以这你只能写逻辑表的表明不能写真实表的表明然后由7b gdbc啊根据这个配置就分表分枯的这个策略嘛让他来决定到底最终是往哪个真实的表里边干什么呀插入数据说这个地方
[06:04] 这个细节给大家强调一下写的都是逻辑的表明不是真实的表明这个一定要注意那么至于这个Controller Service实体内非常简单大家下去自己打开看一看就OK了我就不再过头说了咱就是把do层主要是这块在哪给大家强调一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

