# 画面线理解：14-热门学科排名-统计分析-销售量-周-代码-维度关联&保存到数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\14-热门学科排名-统计分析-销售量-周-代码-维度关联&保存到数据仓库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 02:32, 02:50, 03:43, 04:46, 05:04, 06:03, 07:01, 07:15, 07:46, 08:31, 10:12, 10:46, 11:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:19:39

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

画面11：展示代码编辑器中的 SubjectSalesVolumeByWeekBiz.scala 文件，代码中包含 SparkSession 的创建和导入的包，如 spark.implicits._

画面12：展示代码编辑器中的 UserLearnSourceOfact.scala 文件，代码中包含 Spark SQL 查询语句，用于从 data_course.learning_course_fact 表中选择数据。

画面13：展示代码编辑器中的 UserLearnSourceOfact.scala 文件，代码中包含 Spark SQL 查询语句，用于从 data_course.learning_course_fact 表中选择数据。

画面14：展示代码编辑器中的 SubjectSalesVolumeByWeekBiz.scala 文件，代码中包含 Spark SQL 查询语句，用于从 data_subject.subject_sale_week_biz 表中选择数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```scala
spark.sql(
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
location '/user/hive/external/data_subject/subject_sale_week_biz'
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
19/11/28 11:17:04 INFO SharedState: loading hive config file: file:/D:/code/xc-analysis/xc-service-offline/target/classes/hive-site.xml
19/11/28 11:17:04 INFO HiveMetastore: Setting hive.metastore.warehouse.dir ('/m111') to the value of spark.sql.warehouse.dir
19/11/28 11:17:05 INFO HiveMetastore: Warehouse path is: file:/D:/code/xc-analysis/spark-warehouse
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
