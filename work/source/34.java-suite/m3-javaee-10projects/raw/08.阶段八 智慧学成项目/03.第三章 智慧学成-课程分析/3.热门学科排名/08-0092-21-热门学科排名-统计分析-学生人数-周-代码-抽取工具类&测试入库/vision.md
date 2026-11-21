# 画面线理解：21-热门学科排名-统计分析-学生人数-周-代码-抽取工具类&测试入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\21-热门学科排名-统计分析-学生人数-周-代码-抽取工具类&测试入库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:24, 00:45, 01:24, 01:40, 02:06, 02:31, 02:57, 03:11, 03:40, 03:54, 04:15, 04:35, 04:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:25:34

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark 中编写 SQL 代码，通过动态分区和模板替换生成数据表，并在 Hive 中查看结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Scala 代码，定义了 `weekOfYear`、`learnDS`，并编写了 SQL 查询语句，包含 `LEFT JOIN` 和 `cast` 函数，用于计算用户占比和年周数。
画面2：展示 Scala 代码，定义了 `subjectLearnCountSql` 函数，编写了嵌套的 SQL 查询，用于计算课程类别维度下的销售金额和用户数。
画面3：展示 Scala 代码，定义了 `subjectLearnSql` 函数，编写了 SQL 查询，包含 `LEFT JOIN` 和 `WHERE` 条件，用于计算用户占比和年周数。
画面4：展示 Scala 代码，定义了 `subjectLearnSql` 函数，编写了 SQL 查询，包含 `LEFT JOIN` 和 `WHERE` 条件，用于计算用户占比和年周数。
画面5：展示 Scala 代码，定义了 `subjectLearnSql` 函数，编写了 SQL 查询，包含 `LEFT JOIN` 和 `WHERE` 条件，用于计算用户占比和年周数。
画面6：展示 Scala 代码，定义了 `subjectLearnSql` 函数，编写了 SQL 查询，包含 `LEFT JOIN` 和 `WHERE` 条件，用于计算用户占比和年周数。
画面7：展示 Scala 代码，定义了 `subjectLearnSql` 函数，编写了 SQL 查询，包含 `LEFT JOIN` 和 `WHERE` 条件，用于计算用户占比和年周数。
画面8：展示终端窗口，显示 Spark 应用程序提交成功，日志显示 Spark 版本和安全权限设置。
画面9：展示 Hue 界面，显示 `subject_user_week_biz` 表，提示“该表不包含任何数据”。
画面10：展示终端窗口，显示 Spark SQL 查询结果，包含课程类别、用户数、用户占比和年周数。
画面11：展示终端窗口，显示 Spark 任务执行日志，包括任务提交、执行和完成状态。
画面12：展示终端窗口，显示 Spark SQL 查询结果，包含课程类别、用户数、用户占比和年周数。
画面13：展示 Hue 界面，显示 `subject_user_week_biz` 表的数据，包含课程类别、用户数、用户占比和年周数。
画面14：展示文档页面，显示 `SubjectLearnUserWeekBiz` 的 Scala 类定义和相关代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```scala
val weekOfYear = getMonthNum(current(8)).split(regex = "-")
val learnDS = spark.sql(
  """
    |select
    |  a.course_category_dim_id,
    |  b.name course_category_name,
    |  cast(a.user_num as int) user_num,
    |  cast(a.user_percent as float) user_percent,
    |  ${weekOfYear(0)} years,
    |  ${weekOfYear(1)} week_of_year
    |from learn_biz_tmp a
    |left join data_dimen.course_category_dim b
    |on a.course_category_dim_id = b.course_category_dim_id
    |""".stripMargin
)
```

画面2：
```scala
def subjectLearnCountSql(spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame = {
  spark.sql(
    """
      |SELECT a.course_category_dim_id, a.sale_num sale_num,
      |       ifnull(a.user_num/b.sale_num, 1.0) sale_percent
      |FROM (
      |  SELECT a.course_category_dim_id, sum(sale_volume) sale_num
      |  FROM data_course.course_buy_dim
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${current(0)}' AND '${current(1)}'
      |  GROUP BY course_category_dim_id
      |) a
      |LEFT JOIN (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.course_buy_dim
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${last(0)}' AND '${last(1)}'
      |  GROUP BY course_category_dim_id
      |) b
      |ON a.course_category_dim_id = b.course_category_dim_id
      |""".stripMargin
  )
}
```

画面3：
```scala
val subjectLearnSql = (spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame => {
  spark.sql(
    """
      |SELECT a.course_category_dim_id, a.user_num,
      |       ifnull(a.user_num/b.user_num, 1.0) as user_percent
      |FROM (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${current(0)}' AND '${current(1)}'
      |  GROUP BY course_category_dim_id
      |) a
      |LEFT JOIN (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${last(0)}' AND '${last(1)}'
      |  GROUP BY course_category_dim_id
      |) b
      |ON a.course_category_dim_id = b.course_category_dim_id
      |""".stripMargin
  )
}
```

画面4：
```scala
val subjectLearnSql = (spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame => {
  spark.sql(
    """
      |SELECT a.course_category_dim_id, a.user_num,
      |       ifnull(a.user_num/b.user_num, 1.0) as user_percent
      |FROM (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${current(0)}' AND '${current(1)}'
      |  GROUP BY course_category_dim_id
      |) a
      |LEFT JOIN (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${last(0)}' AND '${last(1)}'
      |  GROUP BY course_category_dim_id
      |) b
      |ON a.course_category_dim_id = b.course_category_dim_id
      |""".stripMargin
  )
}
```

画面5：
```scala
val subjectLearnSql = (spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame => {
  spark.sql(
    """
      |SELECT a.course_category_dim_id, a.user_num,
      |       ifnull(a.user_num/b.user_num, 1.0) as user_percent
      |FROM (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${current(0)}' AND '${current(1)}'
      |  GROUP BY course_category_dim_id
      |) a
      |LEFT JOIN (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${last(0)}' AND '${last(1)}'
      |  GROUP BY course_category_dim_id
      |) b
      |ON a.course_category_dim_id = b.course_category_dim_id
      |""".stripMargin
  )
}
```

画面6：
```scala
val subjectLearnSql = (spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame => {
  spark.sql(
    """
      |SELECT a.course_category_dim_id, a.user_num,
      |       ifnull(a.user_num/b.user_num, 1.0) as user_percent
      |FROM (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${current(0)}' AND '${current(1)}'
      |  GROUP BY course_category_dim_id
      |) a
      |LEFT JOIN (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${last(0)}' AND '${last(1)}'
      |  GROUP BY course_category_dim_id
      |) b
      |ON a.course_category_dim_id = b.course_category_dim_id
      |""".stripMargin
  )
}
```

画面7：
```scala
val subjectLearnSql = (spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame => {
  spark.sql(
    """
      |SELECT a.course_category_dim_id, a.user_num,
      |       ifnull(a.user_num/b.user_num,
