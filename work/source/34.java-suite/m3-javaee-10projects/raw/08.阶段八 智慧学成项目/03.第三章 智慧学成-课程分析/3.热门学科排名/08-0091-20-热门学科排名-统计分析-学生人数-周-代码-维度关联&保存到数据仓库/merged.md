# 20-热门学科排名-统计分析-学生人数-周-代码-维度关联&保存到数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\20-热门学科排名-统计分析-学生人数-周-代码-维度关联&保存到数据仓库_【海量资源尽在 666java.com】.mp4
- 时长 6分52秒（音频 412s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前边已经获取了本周的数据和上周的数据并且计算了涨幅接下来咱们进行维度数据的关联这里咱们需要对它做一些修改因为这个地方直接是在控制台进行打印的咱们接下来把它创建成一个临时表创建成一个临时表后边咱们使用Spark Circle的时候直接根据临时表进行获取数据这里就叫做BIZ的temp
[00:30] 有了它之后咱们等会使用的时候直接根据这个临时表进行数据的一个获取咱们接下来就是进行circle的编写这里咱们还是要多行数据所以说要用三个码号的这种多行文本的方式首先需要使用slide星把这个数据给查出来查出来之后咱们就是对维度的一个关联了
[00:58] 对维度的关联,这个时候咱们就得回到咱们的文档,这个地方咱们来看咱们的维度有哪些,把它给分割一下窗口。
[01:09] 首先这个地方咱们要关联的是谁?
[01:12] 咱们要关联的是课程分类ID,课程分类ID在这个里边是有的。
[01:18] 好,咱们直接就把它给关联过来,这个地方起一个临时表,叫做A表,因为咱们后边需要维度的关联,所以说起个别名还是方便咱们进行数据的一个存取了。
[01:32] 接下来呢是分类的名称分类名称就是咱们要关联的维度表了这个地方咱们需要关联谁啊需要关联课程分类的这个维度这里呢咱们life的join把它给关联进来这里呢关联的时候咱们来复制一下表明咱们来找到维度库咱们是课程分类的维度这个呢就是它然后呢把它给复制一下
[02:01] 复制完成之后呢这个地方它就是咱们的b表它呢它跟它这个地方呢它们的关联关系还是使用a.categoryid等于b.categoryid就是这一行咱们呢直接把它给复制过来有了它之后咱们前面已经写过了咱们呢分类名称呢就是b.name就是咱们的分类名称这个地方呢
[02:26] 但是在咱们的文档中它不是在咱们文档在咱们数据仓库中它是叫什么的Category Name这个地方就需要起一个别名Category Name有了之后接下来是咱们的User NumberUser Number是在A表中A.UserUser Number接下来是咱们的增幅增幅也在这里这个就直接站一下是咱们A.的增幅接下来就是咱们分区的
[02:56] 咱们分区的数据了分区的数据是什么呀分区是咱们年还有咱们的年中的周这个地方呢在前面咱们已经写过也是直接拿过来这个地方有一个分区的年和周这个代码呢就直接拿过来在这里有了它之后呢咱们就可以直接进行一个复制操作这个地方呢加一个到这复年的话就是咱们第一个
[03:31] 锁引为1的这个数据周的话呢就是他们年终的周呢就是锁引为1的这个数据这个地方呢还需要起一个别名咱们来看一下在咱们的数据仓库中它是什么是YERS接下来呢是O4WAKEO4YERS这个数据封装完了之后呢咱们就可以进行一个输出操作收一下咱们来看咱们这个封装结果是否是正常的走起
[04:03] 这个封装结果呢咱们还需要注意一点咱们这个实体呢它这个类型是什么呀是印太类型的这个增幅呢是一个flot类型的咱们呢要根据这个增幅进行一个数据的一个转换这个地方结果程序让它运行的咱们呢把数据类型做一个转换因为程序已经运行了咱们就可以修改咱们的代码了这个地方呢把它转换成咱们的实体实体名称呢就是它站过来
[04:32] 这个时候就可以根据咱们实体进行一个字段的数据类型的转换这个是一个number是一个inter类型的咱们这个地方是kist cst把它转换成一个inter类型的这个地方asinter它转成inter类型之后它还是有算number这个就不能变
[05:03] 接下来呢把它给转化一下它呢是一个flot类型的as flot这个呢别名不能丢这个转化完成之后咱们就得到了谁啊就得到了咱们这个地方会有一个咱们来看一下它是dataset还是datafarm它是一个dataset这个呢就是咱们有一个learn的一个learn ds有了这个ds之后咱们就可以进行什么呀进行数据的一个保存了
[05:35] 这里保存还是重复的代码咱们直接进行一个服用把它给粘过来就这个粘过来之后呢修改一下咱们的编辑名这个地方呢是learn的ds这个修改完不要忘记咱们还有什么啊咱们的表明要修改这个表明呢咱们来数据仓库进行查看咱们是人们学科的这个呢是用户的是用户的
[06:06] 按周统计就是它咱们学科中用户按周统计咱们来切回来学科用户按周统计切换一下它完成之后呢咱们整个代码就算完成了这里呢前边咱们存上自下啊前边咱们首先是获取日期的区间根据这个日期的区间呢咱们来获取了具体的数据并系上了党服系上完成党服之后呢咱们
[06:39] 对维度进行关联最终呢将数据保存到咱们数据仓库中到此呢咱们代码就完成了好视频呢也就先到这里测试呢交给下一个视频

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark SQL 在 Scala 中编写并执行数据统计分析代码，包括创建外部表、编写 SQL 查询、配置动态分区以及在 Hive 中验证结果。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Scala 代码文件 SubjectLearnNumByWeekBiz.scala，其中包含 SQL 查询语句，用于统计课程分类维度下的用户数和用户占比，并通过 LEFT JOIN 连接两个子查询。代码中包含注释“// 6. 根据模板动态加载数据”和“// 7. 输出结果”。
画面2：展示 PPT 页面，标题为“3.5.1.2.2 APP层数据结构”，内容包括创建外部表的 SQL 语句 CREATE EXTERNAL TABLE ...，以及对应的 Scala case class 定义。
画面3：展示 Scala 代码，其中 SQL 查询语句中包含 LEFT JOIN 子句，连接 learn_biz_tmp 表和 data_dimen.course_category_dim 表。
画面4：展示 Scala 代码，SQL 查询语句中包含 LEFT JOIN 子句，连接 learn_biz_tmp 表和 data_dimen.course_category_dim 表。
画面5：展示 Scala 代码文件 SubjectSalesVolumeByWeekBiz.scala，其中包含 SQL 查询语句，用于统计课程分类维度下的销售额和销售占比，并通过 LEFT JOIN 连接两个子查询。
画面6：展示 Scala 代码，其中 SQL 查询语句中包含 LEFT JOIN 子句，连接 learn_biz_tmp 表和 data_dimen.course_category_dim 表。
画面7：展示 Scala 代码，SQL 查询语句中包含 LEFT JOIN 子句，连接 learn_biz_tmp 表和 data_dimen.course_category_dim 表。
画面8：展示 Terminal 窗口，显示 Spark 应用启动日志，包括 BlockManager、SharedState 等信息。
画面9：展示 Terminal 窗口，显示 Spark 应用执行日志，包括获取表、注册数据库等操作。
画面10：展示 Terminal 窗口，显示 Spark 应用执行结果，包含课程分类维度、课程名称、用户数、用户占比、年份、周数等字段。
画面11：展示 Scala 代码，其中包含配置动态分区的代码，设置 Hive.exec.dynamic.partition.mode 为 nonstrict，以及 write.mode 为 overwrite。
画面12：展示 Hue 界面，其中包含 SQL 查询语句，用于统计课程分类维度下的用户数和用户占比。
画面13：展示 Scala 代码，其中包含获取当前日期的代码，以及 SQL 查询语句。
画面14：展示 Scala 代码，其中包含获取当前日期的代码，以及 SQL 查询语句。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```scala
val current = weeks(0).split(regexp = "\\s")
val last = weeks(1).split(regexp = "\\s")
Spark.sql(
  s"""
    SELECT a.course_category_dim_id, a.user_num,
    ifnull(a.user_num/b.user_num,1.0) as user_percent
    from (
      (SELECT course_category_dim_id, count(user_dim_id) user_num
      FROM data_course.learning_course_fact
      WHERE concat_ws('','years,months,days') BETWEEN '${current(0)}' AND '${current(1)}'
      GROUP BY course_category_dim_id) as a
    LEFT JOIN (
      (SELECT course_category_dim_id, count(user_dim_id) user_num
      FROM data_course.learning_course_fact
      WHERE concat_ws('','years,months,days') BETWEEN '${last(0)}' AND '${last(1)}'
      GROUP BY course_category_dim_id) as b
    on a.course_category_dim_id = b.course_category_dim_id
    """ + """stripMargin).show()
```

画面2：
```sql
CREATE EXTERNAL TABLE IF NOT EXISTS data_subject.subject_user_week_biz
(course_category_dim_id String,
user_num Int,
user_percent FLOAT)
PARTITIONED BY (years String, week_of_year String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/Hive/external/data_subject/subject_user_week_biz';
```

画面3：
```scala
Spark.sql(
  s"""
    select
    a.course_category_dim_id,
    b.name course_category_name,
    a.user_num,
    a.user_percent,
    ${weekOfYear(0)} years,
    ${weekOfYear(1)} week_of_year
    from learn_biz_tmp a
    left join data_dimen.course_category_dim b
    on a.course_category_dim_id = b.course_category_dim_id
    """ + """stripMargin).show()
```

画面4：
```scala
Spark.sql(
  s"""
    select
    a.course_category_dim_id,
    b.name course_category_name,
    a.user_num,
    a.user_percent,
    ${weekOfYear(0)} years,
    ${weekOfYear(1)} week_of_year
    from learn_biz_tmp a
    left join data_dimen.course_category_dim b
    on a.course_category_dim_id = b.course_category_dim_id
    """ + """stripMargin).show()
```

画面5：
```scala
val date_info = "2019-09-25"
val weeks = getRelativeInterval(date_info).split(regexp = "\\s")
val current = weeks(0).split(regexp = "\\s")
val last = weeks(1).split(regexp = "\\s")
subjectBuyCountSql(spore, current, last).createOrReplaceTempView(viewName = "salesvolume_biz_tmp")
```

画面6：
```scala
Spark.sql(
  s"""
    select
    a.course_category_dim_id,
    b.name course_category_name,
    a.user_num,
    a.user_percent,
    ${weekOfYear(0)} years,
    ${weekOfYear(1)} week_of_year
    from learn_biz_tmp a
    left join data_dimen.course_category_dim b
    on a.course_category_dim_id = b.course_category_dim_id
    """ + """stripMargin).show()
```

画面7：
```scala
Spark.sql(
  s"""
    select
    a.course_category_dim_id,
    b.name course_category_name,
    a.user_num,
    a.user_percent,
    ${weekOfYear(0)} years,
    ${weekOfYear(1)} week_of_year
    from learn_biz_tmp a
    left join data_dimen.course_category_dim b
    on a.course_category_dim_id = b.course_category_dim_id
    """ + """stripMargin).show()
```

画面8：
```text
19/11/29 16:29:59 INFO BlockManagerMaster: Registering BlockManager BlockManagerId(driver, DESKTOP-LPR46L8, 52785, None)
19/11/29 16:29:59 INFO BlockManagerMaster: Registering BlockManager BlockManagerId(driver, DESKTOP-LPR46L8, 52785, None)
19/11/29 16:29:59 INFO BlockManagerMaster: Initialized BlockManager: BlockManagerId(driver, DESKTOP-LPR46L8, 52785, None)
19/11/29 16:29:59 INFO SharedState: loading Hive config file: file:/D:/code/xc-analysis/xc-Service-offline/target/classes/Hive-site.xml
19/11/29 16:29:59 INFO SharedState: Setting Hive.metastore.warehouse.dir to the value of Spark.sql.warehouse.dir
Warehouse path is 'file:/D:/code/xc-analysis/Spark-warehouse'
```

画面9：
```text
19/11/29 16:30:00 INFO Hive: get table: db-data_dimen tbl-course_category_dim
19/11/29 16:30:00 INFO Hive: get table: db-data_dimen tbl-course_category_dim
19/11/29 16:30:00 INFO Hive: get_database: db-data_dimen
19/11/29 16:30:00 INFO Hive: get_table: db-data_course tbl-learning_course_fact
19/11/29 16:30:00 INFO Hive: get_table: db-data_course tbl-learning_course_fact
19/11/29 16:30:00 INFO Hive: get_table: db-data_course tbl-learning_course_fact
19/11/29 16:30:00 INFO Hive: get_partitions: db-data_course tbl-learning_course_fact
```

画面10：
```text
course_category_dim_id | course_category_name | user_num | user_percent | week_of_year
1-12 | 产品开发 | 3 | 1.0 | 48
```

画面11：
```scala
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")
Spark.conf.set("Spark.sql.parquet.writeLegacyFormat", "true")
Spark.conf.set("Spark.sql.adaptive.enabled", "true")
Spark.conf.set("Spark.sql.adaptive.coalescePartitions.enabled", "true")
Spark.conf.set("Spark.sql.adaptive.advisoryPartitionSizeInBytes

