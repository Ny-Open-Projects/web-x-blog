# day08-3-入门案例-功能实现3

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day08-3-入门案例-功能实现3_【海量资源尽在 666java.com】.mp4
- 时长 13分26秒（音频 806s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们把前两块的配置搞定了接下来开始进行分库分表的配置那咱首先要进行的就是什么呀分库分库呢这一块呢大家看这个表还是要看这个表啊你比如说我举个例子来回顾一下比如我要插入一行数据要插入一行数据啊那首先我们要考虑的就是这行数据你是要存到哪个库里边就是你要存到product db1
[00:30] 还是存到product db2对不对先确定存到哪个库里边然后再确定存到具体哪张表里边所以说我们应该先配置分库策略分库策略怎么配大家还有印象吗我们以前提过是根据什么来进行这个分库的根据什么根据这个所属的店铺就是店铺的ID根据这个值它是基数还是
[01:00] 偶数来决定我要插入的这张数据是放到dbe里边还是放到dbr里边这就是分库策略具体怎么配置呢咱进来看一看这个代码往下走就是这一块这一块配置的就是分库策略我们粘过来咱一起看一看这个配置代码都比较长好我们先看分库策略首先你要告诉他你要根据哪个字段进行分库
[01:35] 我们刚才说了是不是就是这个谁啊这个所属的这个店铺这个字段这个字段的名字它其实就叫store下滑线info下滑线id来大家查一下这个表啊我们应该随便打开一个就行了是不是你看啊这里边是不是有一个store下滑线info下滑线id对吧就是根据它的值来决定是存到db1还是存到什么呀db2那具体的这个策略配置就是这一块
[02:07] 看清楚了啊是这一块就是我们要拿着这个字段的值对不对让他除以二这不就判断他是基础还是偶数吗那为什么还要加一下一呢哎这个细节大家一定要注意到啊那你看整个这其实又相当于一个表达式什么意思呢你可以把这理解成是一个站位符这个dollar符号站位符这个站位符将来的值是从这获取就是这个大拐号里边它最终的结果是多少
[02:37] 这个结果会放到这那大家想一下这个表演式的最终的结果会是几种情况你看一个数字除以2就是求奇数偶数它的值要么是0要么是1再加上1之后呢要么是1要么是2也就是说呢其实这最终的结果要么是DS1要么是DS2DS1DS2你看这DS1和什么呀对DS2
[03:09] 那你现在是否明白这为什么要加1呢为什么呀因为我们将来在存数据的时候我是不是要往M1或者说什么呀M2里边来存而M1和M2对应的逻辑数据员的名字是DS1和DS2有没有这个0啊没有就是它要么是1要么是什么呀要么是2那你这边要是只是除以2的话它的结果要么是0要么是1
[03:37] 而我们想要的是要么是一要么是什么呀二所以说加一下一就变成一或者说什么呀二你认识什么意思吧哎这是分库错了那举个例子啊举个例子你比如说我们刚才说了我这边呢要插入一行数据对不对那插入数据的时候呢比如说我这个数据里边就是那个store就是这个所属店铺的ID如果是六举个例子啊如果是六然后咱看这个结果会怎么着啊六的话
[04:07] 6除以2能除进吗那余数应该是减00加1是1对吧那有时候这就变成了什么DS1那一旦是DS1的话这行数据最终就会存到什么呀M1这个库里那么M1这个库是哪个库呢你往上找啊M1这个库比如这个库嘛我们就存到了相当于存到了什么呀Product DBE这个数据库里你认为啥意思吧这是什么策略对分库策略
[04:33] 那接下来就是分表策略分表策略的话它一共涉及到几张表三张表三张表咱一个一个来吧首先说的就是这个storeinfo它的这个分表策略我先把代码转过来这个分表策略太简单了我想说它最简单了因为它就没进行水平拆分嘛是不是咱前面不是说过吗就说呢我们这个storeinfo这个表我们要进行这个水平拆分不需要所以我们是固定的
[05:05] 固定分配档分配到DS0你看这DS这是排成战刃服然后你看我们前面大拐号里边这还是一个表还是要运算这次我们就不再运算直接写死成什么0就是DS0里边的库DS0是谁DS0不就是它吗M0就是谁你往上看M0M0不就是store db是不是相当于这是写死因为它不分表它不分表所以这直接就这么一写就行
[05:35] 下面这个什么分库的字段呢包括这个表还是这个也基本上是固定了啊ID这个就是那个store info那个表的逻辑名啊因为我们这不分表了说这就直接这样写了也不需要写什么什么啊这个表啊事说这张表的话我们基本上其实是没分表那我们接下来重点看的是product db啊那里边那些表就这两张表上面精英表和什么上面表书表这两张表我们是要进行这个
[06:06] 分表那我们看一看先看product info它的这个分表测量我先把这块代码粘过来看这代码都很多其实都比较好理解而且有些代码是不是都是重复的或者说基本上都是一样的来咱看一看好大家看一下product info它一共是不是涉及到两张表一个product info1一个product info2这个应该大家知道是咋回事了
[06:40] 因为它是不是有个DS1和DS2你看DS1和什么DS2因为咱是主同架构千万不要忘了咱是主同架构然后这里边它的首先你要定义什么叫数据节点什么叫数据节点大家看一下这个图什么叫数据节点看这个图的话也不太容易看数据节点其实你看这儿
[07:10] DS0 DS1和DS2啥意思呢这个数据节点其实指的就是这个你看好了我在这给你说一下就行就是DS1你看这其实是一个取式范围就是要么一要么二其实就是DS1里边的product info1这张表或者说是DS1里边的product info2这张表或者说是DS2里边的product info1这个表或者说是DS2里边的product info2这张表明白吧
[07:41] 这就是数据节点其实说白了就是到底有几张表就是有几张product infer表大家告诉我一共有几个这个product infer表一共有几个一共有四个是不是你看这个咱这个图看这个图我俩说一共四个你数一数呗自己会数吗你看商品信息一商品信息二商品信息一商品信息二不就是四张表对不对分别是在DSE和DS2上面
[08:09] 所以这个其实相当于它的全名是DS1.商品1对吧DS2.商品2这是DS2.商品1这是DS2.商品2相当于四张表我们把它称为四个数据节点然后我们这个分表策略是怎么分的是根据哪个字段来分的我们是不是就是当时我们提到我是不是根据商品的ID对不对就是主件进行身份它的字段名叫Product Info ID我们可以去表里边瞅一瞅是不是有它主件Product Info ID
[08:40] 然后具体的分秒测量跟上面这个分库测量是一样的就是拿这个主间的值除以2然后再让它干什么呀加1为什么加1呢因为我们的表明你看我们的表明是不是要么1要么2有没有0啊没有0要么1要么2所以说你需要加一下1然后呢它的结果就变成要么1要么什么2所以说最终的这个地方的结果就是product下滑线info下滑线1或者说product下滑线info下滑线什么2对不对
[09:10] 正好跟我们的这个表明是什么呀对应上然后这一块是配置主件的生成策略啊这个其实就是雪花算法的那个固定的这个取值算法的名字啊snowflake对不对雪花算法我们前面提到往类似于uid也可以生成这个不重复的这个主件的值啊这是这个固定写法啊雪花算法的这个名字这是什么呀product的infobel的分表策略那么还有这个分表策略就是哪个表就是这个生命描述表
[09:39] 那么他的分秒策略其实跟刚才这个商品新一秒分秒策略基本上是一样的我们把这个代码给他粘过来就行了策略都一样我们粘过来粘过来之后呢稍微做一下调整好差不多就是这个样子你看一样不一样啊这是不是他也是一共几张表四张表吗你在这数一数是不是1234分别是ds0商品秒数1ds0商品秒数2
[10:13] 和DS1商品描述1和DS2商品描述1和DS2商品描述2吧你看这搞了一个组合跟刚才一样分秒策略是不是也是商品ID对不对这个也是磨上2让它加上这为啥不加1了是我在这要加1一样的我就再说了下面是不是也是主件的什么生成策略也是采用了什么选项算法所以我就不再说了但你要注意主件的名字变了
[10:44] 你看这个product descript1这里边来这个主线的名字叫id是叫id所以你这要写成id也是小还算了所以这是这个什么呀这三张表的分表策略我们就配置好配置好之后呢最后我们就指示一下配置什么呀对绑定表绑定表你还有印象吗咱们前面是在哪讲的这些名词概念呀绑定表是在是不是读写分离这个地方
[11:17] 是在对在这儿绑定表有印象吗咱到时讲的是按照某个分片规则一致的这个什么主表和子表这个比如我们以前说的商品信息和这个商品描述它就是一个什么样绑定关系表对不对所以你需要把他俩之间的这个关系给设置一下那具体怎么设置呢咱看一下看一下他刚才那个是在这儿配置的对不对
[11:48] 我们找一找其实应该就一行一行一个配置对不对你看这里边不就是表明吧prodak下个音和和prodak的下个线descript那你要注意我这写的是逻辑表明不是物理表明不是真实表明因为咱的真实表明是不是后边都带着什么-1-2我这可不带我这是逻辑表明这概念你应该还有印象我们前面应该还是在这你看这不是逻辑表是不是你看真实表都是-0-1对吧
[12:24] 我们的逻辑表明就是把这个数字这一块给去掉我们写的是逻辑的这个表明啊这个大家一定要注意的这是设置什么呀绑定表那这个绑定表搞定之后我们看一看咱这一块的配置啊先定杠gdbc相关配置是不是全部搞完我们检查一下是不是全部搞完对不对最后这个日打印我们就不再说了啊他就往控制台打印一下搜据区变用我们将来这个啊进行一些调试的
[12:56] 所以这是咱们整个sharing-gdb的配置最终呢我们看到这个代码的确非常多但是其实这里边重复的相似的是比较多所以说呢其实也没有那么大家想象的那么那么麻烦这些配置呢我个人的建议是你不用从头到尾去给他敲一遍重在理解只要能看懂这是最关键的理解看懂这是最关键的所以这一块的这个关于sharing-gdb的这个配置呢我们就说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

