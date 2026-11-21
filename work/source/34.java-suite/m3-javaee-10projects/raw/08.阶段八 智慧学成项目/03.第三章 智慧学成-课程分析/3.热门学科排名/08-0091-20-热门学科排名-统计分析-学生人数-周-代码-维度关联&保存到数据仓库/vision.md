# 画面线理解：20-热门学科排名-统计分析-学生人数-周-代码-维度关联&保存到数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\20-热门学科排名-统计分析-学生人数-周-代码-维度关联&保存到数据仓库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 01:03, 01:19, 02:32, 03:11, 03:45, 04:02, 04:22, 04:32, 05:17, 05:41, 05:58, 06:28, 06:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:24:36

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
画面11：展示 Scala 代码，其中包含配置动态分区的代码，设置 hive.exec.dynamic.partition.mode 为 nonstrict，以及 write.mode 为 overwrite。
画面12：展示 Hue 界面，其中包含 SQL 查询语句，用于统计课程分类维度下的用户数和用户占比。
画面13：展示 Scala 代码，其中包含获取当前日期的代码，以及 SQL 查询语句。
画面14：展示 Scala 代码，其中包含获取当前日期的代码，以及 SQL 查询语句。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```scala
val current = weeks(0).split(regexp = "\\s")
val last = weeks(1).split(regexp = "\\s")
spark.sql(
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
location '/user/hive/external/data_subject/subject_user_week_biz';
```

画面3：
```scala
spark.sql(
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
spark.sql(
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
spark.sql(
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
spark.sql(
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
19/11/29 16:29:59 INFO SharedState: loading hive config file: file:/D:/code/xc-analysis/xc-service-offline/target/classes/hive-site.xml
19/11/29 16:29:59 INFO SharedState: Setting hive.metastore.warehouse.dir to the value of spark.sql.warehouse.dir
Warehouse path is 'file:/D:/code/xc-analysis/spark-warehouse'
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
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
spark.conf.set("spark.sql.parquet.writeLegacyFormat", "true")
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.advisoryPartitionSizeInBytes
