# 14-热门学科排名-统计分析-销售量-周-代码-维度关联&保存到数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\14-热门学科排名-统计分析-销售量-周-代码-维度关联&保存到数据仓库_【海量资源尽在 666java.com】.mp4
- 时长 11分36秒（音频 697s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前面已经获取了上周和上上周的数据并计算了涨幅,接下来就是维度的关联,然后保存数据,咱们开始相关维度的一个关联,这里咱们获取的结果是直接输出的,当然结果咱们还在使用,这里上一层就是这个surfer获取的一个结果是一个ditform,咱们直接给它转换成一个临时表,
[00:29] 这里转换成一个临时表之后,咱们后边就可以写SPA Circle的时候,根据这个临时表进行一个相关代码的一个编写,主要还是一个Circle的编写。
[00:42] 咱们这个地方就叫它的一个BIZ的一个临时表,TMP。
[00:47] 后边咱们就可以直接使用这个临时表,然后进行维度的关联。
[00:52] 咱们来写维度关联的代码。
[00:54] 这里还在使用什么?
[00:55] 还在使用SPA Circle。
[01:00] 还是用多行的方式吧咱们首先还是由于这个地方用了临时表用了临时表之后而且上面呢是没有那个HUE是不支持这个一分钥的函数呢这个地方的代码编写咱们就只能在IDEA里边就是开发工具里边进行编写咱们呢先把它给查出来Solid这里是Solid星是这张表把这张表的数据给查过来之后呢咱们是不是要进行维度的关联呢
[01:31] 维度数据的关联咱们要关联的是谁啊要关联的是课程分类的一个数据这里呢咱们来换个行这里呢直接来进行一个关联它还是起个别名叫做A表吧然后呢咱们要叫left joinjoin呢是咱们的一个课程分类维度这里呢咱们来粘一下课程分类维度课程分类维度是在咱们的维度库里边
[02:02] 课程分类维度这个这个呢路径就是库名加表名比较长直接过来粘一下把它给粘过来粘过来之后呢它呢就是咱们的B表现在的一个B表这里它的一个分类咱们唯一关联的是不是还是还是这个条件啊就是A表的课程分类ID等于B表的课程分类ID这个时候咱们关联条件有了是不是就剩输出字段了咱们输出字段的话咱们得对着咱们的文档来看
[02:34] 这里的输出字段我来给窗口来分割一下吧在这稍微拉大一点再拉长一点好好就这样吧咱们输出字段首先是课程分类的ID课程分类的ID是不是在A表和B表都有啊这里课程分类ID把它给粘一下咱们呢再换个行A的课程分类ID接下来呢分类ID有了是不是分类名称分类名称是不是只有在B表有啊
[03:11] 咱们来看B表的分类名称是叫什么呀它这个地方是应该是直接就是Name这个地方就是直接是Name直接是Name的话咱们B点Name就行了B点Name但是在咱们的在咱们的业务表里边就是APP层那个表里边它叫什么呀它叫Category Name然后呢咱们把别名给清好接下来是谁呀是不是Solar NumberSolar Number的话是不是只有在A表有就是咱们上面一系列操作
[03:41] 他在这里把他给拿过来他拿过来之后接下来是不是咱们的一个销量的一个涨幅涨幅是不是也在币边里也在币边里边这个是币边刚才口误接下来是分区的年和分区的OEQOFYR就是分区中年的年中的周这里年中的周这两个数据咱们现在是不是没有没有的情况下咱们当前周是不是这个数据
[04:14] 当前都是这个数据的情况下咱们是不是要根据当前都进行一个年数据的一个获取啊年中的周的一个数据获取啊咱们在这个地方吧再加个主持获取年中的周获取年中的周这里呢获取年中的周咱们在DataNihil里边有一个get wake number错了control加control加Fget
[04:46] 这个地方呢是有一个测试wkwk number咱们来找到这个方法把它给引入进来在这里copy一下把它给导到咱们这个工程里边impostor有了它之后咱们直接get wk就行了这里呢get wk number它是不是要一个字符顺啊字符顺的话咱们这个地方是不是要取一个周一啊周几都行啊
[05:24] 咱们直接根据咱们当前周直接取当前周的第一天就行这里呢过去完之后咱们看它的返回值是什么它是不是当前的周完了之后它的返回值是年和周中间用一个横杠进行一个分割啊这个时候咱们直接接着进行一个分割split这里呢就是横杠它呢它会有一个变量咱们呢就是weekoveryear就是年中的周
[05:56] 这个时候它是一个数组它这个数组呢前半部分是谁啊前半部分就是年后半部分就是年终的周这个时候呢咱们就可以直接进行一个在这里边进行一个复制操作它呢年就是第一个值然后呢接下来这个豆花上吊它就是年终的周它就是第一个值零值和第一个值这两个写好之后咱们这个地方是不是还要起个边缘了因为它
[06:29] 直接使用变量引入的话它是没有名字的咱们呢把别名给起好起好之后这个时候咱们这个结果写完之后是不是就可以进行一个结果查看了接着收一下这个地方咱们结果查看只是验证啥呀只是为了验证咱们这个代码是否是正确的搜起这里呢让它计算一下稍等然后等它计算完成
[07:12] 这里呢当前周是2019年的第39周就是上面这个日期咱们看结果已经完成咱们想想了这个时候呢你就可以看到到由产品经理这个呢销量是这么多然后呢它的增幅是这么多它的分区是这样的这个地方稍微有一个问题啊咱们这个地方销量它是一个inter类型但是呢它把它给看当成一个什么了
[07:43] 它把它给当成一个flot类型了这个时候呢咱们还需要进它对它进行一个转换就是把它给转换成印刷类型因为咱们的数据结构咱们最终保存的时候是不是有一个学科的一个对应的一个实体啊就是这个对应的一个实体上面如果字段不对的话你实体肯定是不是找不着啊咱们这里把它给粘过来这个地方呢就不是瘦了把它艾子咱们的实体
[08:13] 这就得到了咱们的实体然后导个包这个时候它报了一个错报个错的原因呢是因为咱们隐私转换没有导入这个地方呢把隐私转换给导入这个呢是咱们的隐私转换导入之后它这个包错就没了咱们是不是需要把它给转换成inter类型啊这里用case的然后呢它asinter就行了这个时候
[08:46] 由于咱们使用了函数这个还要需要将它把别名给加上对应的为了保险期间咱们也需要将它给转换因为如果它这个地方如果不是使用了flot或者是它这个地方用的是如果是打保或者其他情况或者是四幅算什么的它也会出问题就是转换实体的时候这个咱们直接使用case把它给转换成flot保险期间就
[09:19] 免得出问题这样写完之后咱们这个程序就没有问题了没有问题这个地方咱们按键完之后它是一个什么dataset它给它一个接收这里是谁这里咱们是课程购买量的一个最终的一个结果这就叫就叫sl的df ds因为它是一个dataset这里咱们
[09:49] 输出完成之后这个地方这个地方就不用输出了这个地方呢咱们就可以直接保存结果保存结果呢还是咱们之前的方式由于都是固定的代码咱们呢就来复制一下这里咱们是分析这个呢咱们在学这个是学习人数这个地方就是学习人数的原始数据咱们来加这个的保存因为保存格式都是一样的你去课程购买量或者课程房量都行
[10:22] 这里咱们是使用学生人数原始数据的信息咱们使用这一块的直接粘这个上面变量需要修改一下这个地方是DS然后它就不需要CREATE了因为咱们上面DS是可以直接使用的直接在这改就行了改完之后这个地方是表明咱们最终需要保存的表明咱们来点数据仓库来看一下这个是和学科相关的咱们现在是销售量
[10:54] 销售量是周的就是这个然后收底片把这个完整的路径给粘过来复制一下这个呢走起这个呢也修改一下修改完成之后呢咱们整个代码的编写就算完成了代码的编写完成咱们的视频呢就先到这里测试呢交给咱们下个视频来进行通过本节的学习呢需要掌握的是就是维度相关维度的关联
[11:25] 以及呢咱们将数据进行一个保存这类保存由于是固定的代码咱们就直接进行一个复制粘贴的一个操作好视频就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Scala 中编写 Spark SQL 代码，对课程销售数据按周进行聚合分析，并展示如何配置 Spark 作业参数和执行结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，当前编辑的是 SubjectSalesVolumeByWeekBiz.scala 文件，其中包含一个 Spark SQL 查询，用于计算课程销售数据的周度汇总，包括科目ID、科目名称、销售额、销售占比、年份、周数等字段，并通过 LEFT JOIN 连接 salesvolume_biz_tmp 表。

画面2：展示 PPT 内容，标题为“3.5.1.1.3 统计分析代码”，左侧是目录结构，右侧是代码示例，包括 Hive 表的存储格式和分区信息，以及 Scala 中的 case class SubjectSaleWeekBiz 的定义。

画面3：展示两个并排的窗口，左侧是 PPT 内容，右侧是代码编辑器，代码中包含 Spark SQL 查询语句，用于从 salesvolume_biz_tmp 表中选择数据并进行 LEFT JOIN 操作。

画面4：展示代码编辑器中的 Spark SQL 查询语句，其中包含对当前日期的处理，使用 getYear()、getWeekOfYear() 等方法提取年份和周数。

画面5：展示代码编辑器中的 DateUtils.scala 文件，其中包含用于处理日期的工具方法，如 getToday()、getYesterday()、getMonthInterval() 等。

画面6：展示代码编辑器中的 DateUtils.scala 文件，鼠标悬停在 getToday() 方法上，弹出上下文菜单，显示可以执行的选项，如 Run、Debug、Create Git、Create Gist 等。

画面7：展示代码编辑器中的 SubjectSalesVolumeByWeekBiz.scala 文件，代码中包含对当前日期的处理，使用 getYear()、getWeekOfYear() 等方法提取年份和周数。

画面8：展示代码运行日志，显示 Spark 作业的启动和初始化过程，包括 BlockManager、Hive metastore、StateStoreCoordinator 等组件的初始化。

画面9：展示代码运行日志，显示 Spark 作业执行过程中的 Hive 表操作，包括 get database、get table 等操作。

画面10：展示代码运行日志，显示 Spark 作业执行完成后的结果，包括课程科目ID、科目名称、销售额、销售占比、年份、周数等字段的数据。

画面11：展示代码编辑器中的 SubjectSalesVolumeByWeekBiz.scala 文件，代码中包含 SparkSession 的创建和导入的包，如 Spark.implicits._

画面12：展示代码编辑器中的 UserLearnSourceOfact.scala 文件，代码中包含 Spark SQL 查询语句，用于从 data_course.learning_course_fact 表中选择数据。

画面13：展示代码编辑器中的 UserLearnSourceOfact.scala 文件，代码中包含 Spark SQL 查询语句，用于从 data_course.learning_course_fact 表中选择数据。

画面14：展示代码编辑器中的 SubjectSalesVolumeByWeekBiz.scala 文件，代码中包含 Spark SQL 查询语句，用于从 data_subject.subject_sale_week_biz 表中选择数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```scala
Spark.sql(
  """
    |SELECT a.course_category_dim_id course_category.dim_id, a.sale_num sale_num,
    |       ifnull(a.sale_num-b.sale_num/b.sale_num, 1.0) sale_percent
    |FROM (
    |  SELECT course_category_dim_id, sum(salesvolume) sale_num
    |  FROM data_course.course_buy_dim
    |  WHERE concat_ws( '-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
    |  GROUP BY course_category_dim_id
    |) as a
    |LEFT JOIN (
    |  SELECT course_category_dim_id, sum(salesvolume) sale_num
    |  FROM data_course.course_buy_dim
    |  WHERE concat_ws( '-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
    |  GROUP BY course_category_dim_id
    |) as b
    |ON a.course_category_dim_id = b.course_category_dim_id
    |""".stripMargin).show()
```

画面2：
```sql
STORED AS PARQUET
location '/user/Hive/external/data_subject/subject_sale_week_biz'
```

```scala
case class SubjectSaleWeekBiz(course_category_dim_id: String,
                              course_category_name: String,
                              sale_num: Int,
                              sale_percent: Float,
                              years: String,
                              week_of_year: String)
```

画面3：
```scala
SELECT a.course_category_dim_id, b.name course_category_name,
       a.sale_num, a.sale_percent, a.years, a.week_of_year
FROM salesvolume_biz_tmp a
LEFT JOIN data_dimen.course_category_dim b
ON a.course_category_dim_id = b.course_category_dim_id
```

画面4：
```scala
val weekOfYear = getWeekOfYear(current(0)).split( regex = "-")
```

画面5：
```scala
val date_info = "2019-07-18"
println(getMonthRelativeInterval(date_info, "yyyy-MM-dd"))
```

画面6：
```scala
val today = getToday()
println(today)
```

画面7：
```scala
val weekOfYear = getWeekOfYear(current(0)).split( regex = "-")
```

画面8：
```scala
19/11/28 11:17:04 INFO BlockManagerMaster: Registered BlockManager DESKTOP-DESKTOP-58625 with 3867.5 MB RAM, BlockManagerId(driver, DESKTOP-LPH4L8, 58625, None)
19/11/28 11:17:04 INFO BlockManagerMaster: Registered BlockManager BlockManagerId(driver, DESKTOP-LPH4L8, 58625, None)
19/11/28 11:17:04 INFO SharedState: loading Hive config file: file:/D:/code/xc-analysis/xc-Service-offline/target/classes/Hive-site.xml
19/11/28 11:17:04 INFO HiveMetastore: Setting Hive.metastore.warehouse.dir ('/m111') to the value of Spark.sql.warehouse.dir
19/11/28 11:17:05 INFO HiveMetastore: Warehouse path is: file:/D:/code/xc-analysis/Spark-warehouse
19/11/28 11:17:05 INFO StateStoreCoordinatorRef: Registered StateStoreCoordinator endpoint
```

画面9：
```scala
19/11/28 11:17:12 INFO HiveMetastore: get database: data_course
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table: db-data_course tbl-course_buy_dim
19/11/28 11:17:12 INFO HiveMetastore: get table:

