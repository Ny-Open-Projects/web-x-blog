# 画面线理解：15-课程分析-课程购买量-DWM代码-保存到数据仓库&测试入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\15-课程分析-课程购买量-DWM代码-保存到数据仓库&测试入库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:32, 01:53, 02:06, 02:22, 03:09, 03:50, 04:11, 04:22, 04:43, 04:54, 05:16, 05:44, 06:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:07:30

1) 这一组画面整体在讲如何使用 Spark SQL 将课程购买事实表按日期维度聚合后写入 Hive 数据仓库，并通过 Hue 查看结果。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Spark SQL 代码，定义了 buyDS DataFrame，包含从 fact 表中按日期维度聚合的销售数据，并使用 LEFT JOIN 连接维度表。
画面2：在代码中添加了设置动态分区模式的配置：spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")。
画面3：在代码中添加了 repartition 设置，并右键弹出菜单，显示可执行的选项。
画面4：在代码中添加了注释，说明使用的是 MySQL 作为底层数据库，并显示了 SparkSession 初始化的日志。
画面5：在代码中添加了写入模式为 overwrite，并显示了 Spark 任务启动和停止的日志。
画面6：在 Hue 的 Table Browser 中查看了 course_buy_dwm 表的数据样本，包含课程维度 ID、公司 ID、类别 ID、销售额等字段。
画面7：在代码中对 buyDS DataFrame 的字段进行了调整，移除了部分字段。
画面8：在代码中对 buyDS DataFrame 的字段进行了调整，移除了部分字段。
画面9：在代码中添加了写入模式为 overwrite，并显示了 Spark 任务启动和停止的日志。
画面10：在 Terminal 中显示了 Spark 任务执行过程中的日志，包括任务启动、完成和数据块传输等信息。
画面11：在 Hue 的 Table Browser 中查看了 course_buy_dwm 表的数据样本，包含课程维度 ID、公司 ID、类别 ID、销售额等字段。
画面12：在 Hue 的 Hive 编辑器中编写了 SQL 查询语句，用于查询 course_buy_dwm 表的数据。
画面13：在 Hue 的 Hive 编辑器中显示了 SQL 查询语句的执行结果，包括执行时间、查询语句和结果数据。
画面14：在 Hue 的 Table Browser 中查看了 course_buy_dwm 表的数据样本，包含课程维度 ID、公司 ID、类别 ID、销售额等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```scala
val buyDS = spark.sql(
  """
    |SELECT
    |  a.course_dim_id,
    |  b.company_id,
    |  b.at_course_category_dim_id,
    |  a.sales,
    |  a.salesvolume,
    |  a.years, a.months, a.days
    |FROM
    |  (
    |    SELECT
    |      course_dim_id,
    |      sum(price) sales,
    |      count(course_id) salesvolume,
    |      years, months, days
    |    from data_course.course_buy_fact WHERE concat_ws('-', years, months, days) = '${date_info}'
    |    GROUP BY course_dim_id, years, months, days
    |  ) a
    |  LEFT JOIN data_dimen.course_dim b
    |  ON a.course_dim_id = b.course_dim_id
    |""".stripMargin.as(CourseBuyDWM)
)
```

画面2：
```scala
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
```

画面3：
```scala
buyDS.repartition(numPartitions = 1)
```

画面4：
```scala
// 配置动态分区模式
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
```

画面5：
```scala
// 配置动态分区模式
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")

buyDS.repartition(numPartitions = 1)
// 写入模式
.write.mode("overwrite")
.insertInto tableName = "data_course.course_buy_dwm"
```

画面6：
```sql
SELECT
  a.course_dim_id,
  b.company_id,
  b.at_course_category_dim_id,
  a.sales,
  a.salesvolume,
  a.years, a.months, a.days
FROM
  (
    SELECT
      course_dim_id,
      sum(price) sales,
      count(course_id) salesvolume,
      years, months, days
    from data_course.course_buy_fact WHERE concat_ws('-', years, months, days) = '${date_info}'
    GROUP BY course_dim_id, years, months, days
  ) a
  LEFT JOIN data_dimen.course_dim b
  ON a.course_dim_id = b.course_dim_id
```

画面7：
```scala
val buyDS = spark.sql(
  """
    |SELECT
    |  a.course_dim_id,
    |  b.company_id,
    |  b.at_course_category_dim_id,
    |  a.sales,
    |  a.salesvolume,
    |  a.years, a.months, a.days
    |FROM
    |  (
    |    SELECT
    |      course_dim_id,
    |      sum(price) sales,
    |      count(course_id) salesvolume,
    |      years, months, days
    |    from data_course.course_buy_fact WHERE concat_ws('-', years, months, days) = '${date_info}'
    |    GROUP BY course_dim_id, years, months, days
    |  ) a
    |  LEFT JOIN data_dimen.course_dim b
    |  ON a.course_dim_id = b.course_dim_id
    |""".stripMargin.as(CourseBuyDWM)
)
```

画面8：
```scala
val buyDS = spark.sql(
  """
    |SELECT
    |  a.course_dim_id,
    |  b.company_id,
    |  b.at_course_category_dim_id,
    |  a.sales,
    |  a.salesvolume,
    |  a.years, a.months, a.days
    |FROM
    |  (
    |    SELECT
    |      course_dim_id,
    |      sum(price) sales,
    |      count(course_id) salesvolume,
    |      years, months, days
    |    from data_course.course_buy_fact WHERE concat_ws('-', years, months, days) = '${date_info}'
    |    GROUP BY course_dim_id, years, months, days
    |  ) a
    |  LEFT JOIN data_dimen.course_dim b
    |  ON a.course_dim_id = b.course_dim_id
    |""".stripMargin.as(CourseBuyDWM)
)
```

画面9：
```scala
// 配置动态分区模式
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")

buyDS.repartition(numPartitions = 1)
// 写入模式
.write.mode("overwrite")
.insertInto tableName = "data_course.course_buy_dwm"
```

画面10：
```scala
INFO  TaskManager: Running task 138.0 in stage 3.0 (TD 104)
INFO  TaskManager: Finished task 138.0 in stage 3.0 (TD 104)
INFO  TaskManager: Starting task 131.0 in stage 3.0 (TD 104)
INFO  TaskManager: Finished task 131.0 in stage 3.0 (TD 104)
INFO  TaskManager: Starting task 132.0 in stage 3.0 (TD 104)
INFO  TaskManager: Finished task 132.0 in stage 3.0 (TD 104)
INFO  TaskManager: Starting task 135.0 in stage 3.0 (TD 104)
INFO  TaskManager: Finished task 135.0 in stage 3.0 (TD 104)
INFO  TaskManager: Starting task 134.0 in stage 3.0 (TD 104)
INFO  TaskManager: Finished task 134.0 in stage 3.0 (TD 104)
INFO  TaskManager: Starting task 133.0 in stage 3.0 (TD 104)
INFO  TaskManager: Finished task 133.0 in stage 3.0 (TD 104)
```

画面11：
```sql
SELECT
  a.course_dim_id,
  b.company_id,
  b.at_course_category_dim_id,
  a.sales,
  a.salesvolume,
  a.years, a.months, a.days
FROM
  (
    SELECT
      course_dim_id,
      sum(price) sales,
      count(course_id) salesvolume,
      years, months, days
    from data_course.course_buy_fact WHERE concat_ws('-', years, months, days) = '${date_info}'
    GROUP BY course_dim_id, years, months, days
  ) a
  LEFT JOIN data_dimen.course_dim b
  ON a.course_dim_id = b.course_dim_id
```

画面12：
```sql
SELECT
  a.course_dim_id,
  b.company_id,
  b.at_course_category_dim_id,
  a.sales,
  a.salesvolume,
  a.years, a.months, a.days
FROM
  (
    SELECT
      course_dim_id,
      sum(price) sales,
      count(course_id) salesvolume,
      years, months, days
    from data_course.course_buy_fact WHERE concat_ws('-', years, months, days) = '${date_info}'
    GROUP BY course_dim_id, years, months, days
  ) a
  LEFT
