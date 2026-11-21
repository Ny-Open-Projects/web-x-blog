# day08-2-入门案例-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day08-2-入门案例-功能实现2_【海量资源尽在 666java.com】.mp4
- 时长 11分14秒（音频 675s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才我们把入门案例当中的这一堆最基本的配置把它搞定了这些配置都是咱之前见过的最基本的一个配置接下来我们就该进行sharding-gdbc配置那么这个配置是咱们这一块的重点对不对这块配置有两个特点咱先跟大家介绍一下第一个特点就是配置非常多大家看一下配置带很多对吧一堆一堆的看上去很头疼第二个特点就是
[00:33] 我们使用sharing gdbc主要就是玩它的什么配置换句话说加代码那一块就我们以前的操作数据库的加代码以前该怎么写现在还是怎么写没有变化没有变化只是变化了是什么是配置所以说我们使用sharing gdbc主要玩的就是它这一堆什么配置所以说这是相当两个特点我们需要给大家说一说
[01:03] 那咱接下来就要搞这一堆配置啊这一堆非常多呢我们给他这个拆分成这个若干的这个块啊或者若干的不受首先我们要搞的就是真实数据源的定义定义真实数据然后我们还要定义逻辑数据这个逻辑数据源呢其实就是相当于是什么呀主从对应关系我们要配
[01:41] 然后再接下来我们还要搞什么配置呢我们要搞的就是分库分表测量当然呢我们这里边涉及到几个表的分表测量是不是应该是三个表吧对不对我先写个啊三张表然后接下来还有什么呀绑定表设置是绑定表大概应该是整个配置拆分成这几块吧我们这个讲义看下讲义快速的过一遍我看有没有遗漏啊真实数据员对吧
[02:22] 还有什么呀这个逻辑数据员分库策略对吧然后JS是这几张表的分表策略是不是应该是几张表三张表对不对然后是什么呀绑定表没了下面这个是一个日志的一个输出打印这个他就是把搜索语音给打印到空台吧方便我们调试随着说呢整个销定杠GDBC的配置大家注意我们整体的拆分成这几块咱一块一块来
[02:52] 首先我们看第一块配置叫定义真实数据员啥意思呢咱看看这张图什么叫真实数据员就是真实存在的物理数据库那大家想一下我们前面这个表大家应该都见过了我们是把这些都已经这个搭建好了是不是那你能不能现在告诉我我这台电脑上一共有多少个数据库这个真实存在的物理数据库其实就是我们说的这个这个什么呀对就是这个真实的数据员吧
[03:26] 有几个数据库老师你数一数嘛三个嘛这不是一个对不对这一个然后还有什么呀这一个这一个一共三个嘛不够我告诉你不够不是三个应该是几个对应该有的说对应该是几个六个数据库我还是六个因为我们是不是现在本机是主从架构嘛主数据库和从数据库嘛而且主和从上的这个数据库一样不一样一样
[03:56] 所以一共有几个数据库六个数据库啊六个数据库那我们这应该是定义几个数据员了应该对我们这其实一共是六个的啊这个你千万不要忘记了六个好这个我们搞清楚之后我们看看这个真实数据员具体怎么配置啊咱看看讲这些配置代码我就不再挨个你敲了这个太花时间了我们重在理解那你看首先我们是要做这么一行配置
[04:28] 你看他说的是这个什么呀Data Source是不是数据源Names是不是给这个真实的数据源相当于起个名字我们有六个是不是应该起几个名字六个名字分别是M0 M1 M2 S0 S1 S2大家能看出来这边哪几个是主库哪几个表示存库吗能看出来吗这个M就是Master的意思就是主库对吧S就是Slaver这个单词咱在哪见过呀这个
[04:59] 我们再再再再找找就是哪个单词啊就这这三个啊就是从从属是s开头的对不对所以说呢m大头的这三个是主库啊s开头的这三个是总库一共几个啊一共有六个那有的学员会说老师这就表示把真实数据给定义好了不是啊这只是先起了六个名字而已那我们既然还要针对这六个名字进行配置m0表示哪个数据库啊
[05:29] M1表示数据库哪个数据库对不对S0 S1又分别表示哪个数据库是不是我还得配接下来这些配置大家都比较熟了一看那你就知道是啥意思我给你粘过来一块因为他们这些基本上都是一样我先去粘过来一块给你看看来大家瞅一眼很简单你看我这写的都是什么M0这个M0是不是跟这个名字是对应的保持一致的对不对
[06:02] 那等于说呢这几行代码配的就是名字叫m0的这个数据员相关的一些信息都配了什么信息啊用哪一种连接池这个什么呀驱动对吧价值三号不用解释了不用解释了这不是那个那个ip地址端口号数据库的名字对不对还有账号密码那看到这一配你能告诉我m0这个数据员到底指的是哪个数据库吗到底指的是哪个数据库m0是不是指的是主库当中的
[06:32] StoreDB这个数据库是不是我刚才说M开头就是主库主库当中哪个库对StoreDB3306我们前面说3306是主库3307是从库说这是主库主库当中的谁StoreDB这就是M0那同样的M1 M2 S0 S1 S2是不是都是类似这种配置当然里边像这个这个端口号或者说这个输出的名字是不是会发生变化这代码我们直接看讲一样你看M1 M1你看
[07:02] 数据库的名字就换成了product db1对不对m2就换成了product db2是不是你跟这个表对应一下是不是product db1product db2还有store db然后你再看再往下是s开头s0 s1和什么s2跟上面相比你看是不是端口号变我们重库的端口号是3307对不对那你看s0是store db然后s1是谁product db1s2就是
[07:33] prodark的地边明白什么意思吧其他配置都是一样那这些代码我就直接粘过来了啊只要大家搞明白什么意思就行然后从这开始粘粘过来然后呢还有一部分在这儿呃这里边的话你从pdf讲义粘过来之后呢有些地方这个换行你需要给他去掉这里边是不是给你提示错误啊对不对这个你自己修改一下就行了包括其他地方的这些换行啊你都可以自己改一下
[08:27] 其他的还有这个差不多这一堆大家注意了这一堆就是第一块配置就是真实数据源这个配置一共有六个这块代码虽然多你看一下一堆了对不对但是其实比较好理解那么六个真实的数据源配置好之后呢我们接下来就要配置什么呀逻辑数据源什么叫逻辑数据源呢其实指的就是主从对应关系啥意思呢来咱看看这张表这是我专门给大家这个准备的一张表
[08:59] 就是帮助你理解sharding-gdbc的这一堆什么呀配置的那啥意思呢大家知道我们前面讲过这个从库是不是要从主库那边同步数据是不是那大家看这张图这个左边这边是主库上面的三个数据库是吧右边呢是从库上面的三个什么呀数据库我们是不是从库就是右边要从主库这边要同步数据对吧那
[09:28] 两边各自有三个数据库那他们之间是谁从谁那边同步数据呢就他们之间的对应关系我们是需要指定一下配置一下要不然的话这个框架没那么智能那具体什么意思呢大家也知道S0要从哪同步数据S0是不是要从M0这儿同步数据对吧那么S要从哪同步数据要从M1这个同步数据那S2自然是要从什么呀对M2这个库里边进行数据的同步
[09:59] 说M0 S0是对应关系M1 S1是一个对应关系M2和S2是一个什么呀对应关系这叫主从这个什么呀逻辑上的一个对应关系所以我们需要把这个给配置一下框架它是不可能这么智能的知道这个事情怎么配置呢很简单咱们看一下就这几行代码再复制一下然后再粘过来粘完之后呢大家看一下这个代码呢也比较清晰了你看M0和S0
[10:30] 它俩是不是一对这一对这个对应的数据源叫DS0看见没有M1和S1是一对我凭啥说它俩是一对呢因为它俩都属于哪个数据源逻辑数据源啊叫DS1那M2和S2是一对它俩是对应关系对不对它俩呢这个对应的逻辑数据源的名字叫DS2相当于把那六个库分成了几对啊三对啊分别叫DS0DS1DS2这其实相当于是什么呀逻辑数据源啊
[11:00] 这个每个数据源里边呢是不是都有一个主库和一个从库从库从这个主库里边对进行数据同步这是sharding-gdbc的第二块配置咱就搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

