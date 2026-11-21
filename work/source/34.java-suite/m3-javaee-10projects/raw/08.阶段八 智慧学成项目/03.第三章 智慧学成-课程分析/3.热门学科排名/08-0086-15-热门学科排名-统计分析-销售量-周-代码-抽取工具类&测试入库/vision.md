# 画面线理解：15-热门学科排名-统计分析-销售量-周-代码-抽取工具类&测试入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\15-热门学科排名-统计分析-销售量-周-代码-抽取工具类&测试入库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:53, 01:06, 01:37, 01:53, 02:18, 02:51, 03:06, 03:22, 03:46, 03:50, 03:57, 04:14, 04:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:20:38

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark 中编写 SQL 代码，对课程销售数据按周进行统计分析，并将结果写入 Hive 表中，最后在 Hue 中验证数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构和代码目录，当前选中“3.5.1.1.3 工具类”章节，右侧显示 `SubjectSalesVolumeByWeekBiz` 类的代码，包含导入语句和初始化 SparkSession。
画面2：在 `SubjectSalesVolumeByWeekBiz` 类中，展示 `val date_info = "2019-09-25"` 和 `val weeks = getWeekRelativelyInterval(date_info).split(regex = ";")` 的代码，以及 `spark.sql` 的 SQL 语句，该语句包含 `LEFT JOIN` 和 `WHERE` 条件。
画面3：展示 `SubjectUtils.scala` 文件中的 `def subjectBuyCountSql(spark: SparkSession, current: Array[String], last: Array[String]): Unit = { }` 方法定义。
画面4：在 `SubjectUtils.scala` 中，展示 `subjectBuyCountSql` 方法的 SQL 语句，包含 `SELECT`、`FROM`、`WHERE` 和 `LEFT JOIN` 子句。
画面5：在 `SubjectUtils.scala` 中，展示 `def subjectLearningSql(spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame = { }` 方法定义。
画面6：在 `SubjectSalesVolumeByWeekBiz` 类中，展示 `val weekOfYear = getWeekOfYear(current(0)).split(regex = ";")` 和 `val sIdS = spark.sql` 的代码。
画面7：在 `SubjectUtils.scala` 中，展示 `def subjectLearningSql` 方法的 SQL 语句，包含 `SELECT`、`FROM`、`WHERE` 和 `LEFT JOIN` 子句。
画面8：展示 `subjectBuyCountSql` 方法的完整 SQL 语句，包含 `SELECT`、`FROM`、`WHERE` 和 `LEFT JOIN` 子句。
画面9：在 `SubjectSalesVolumeByWeekBiz` 类中，右键点击代码，弹出菜单，选择“Paste from History”。
画面10：在 `SubjectSalesVolumeByWeekBiz` 类中，执行代码后，终端显示任务提交和成功完成的日志。
画面11：在 `SubjectSalesVolumeByWeekBiz` 类中，终端显示 Hive 表创建和数据写入的日志。
画面12：在 Hue 界面中，显示 `data_subject.subject_sale_week_biz` 表，提示“该表不包含任何数据”。
画面13：在 `SubjectSalesVolumeByWeekBiz` 类中，展示 `spark.sql` 的代码，用于查询表数据。
画面14：展示开发中查询结果，表格包含列：`course_category_dim_id`、`course_category_name`、`sale_num`、`sale_percent`、`years`、`week_of_year`，并显示了部分数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```scala
package cn.itcast.xc.analysis.subject.salesvolume

import cn.itcast.xc.common.ELTEnvironment
import cn.itcast.xc.entity.SubjectSaleWeekBiz
import cn.itcast.xc.utils.DateUtils.{getWeekNum, getWeekRelativelyInterval}
import cn.itcast.xc.utils.SubjectUtils.subjectBuyCountSql
import org.apache.spark.sql.SparkSession

object SubjectSalesVolumeByWeekBiz {
  /**
    * 初始化参数
    */
  val spark: SparkSession = ELTEnvironment.getSparkSession(this.getClass.getSimpleName)
```

画面2：
```scala
val date_info = "2019-09-25"
val weeks = getWeekRelativelyInterval(date_info).split(regex = ";")
val current = weeks(0).split(regex = ";")
val last = weeks(1).split(regex = ";")

spark.sql(
  s"""
     |SELECT a.course_category_dim_id, course_category_dim_id, a.sale_sum sale_num,
     |ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
     |FROM (
     |(SELECT course_category_dim_id, sum(salesvolume) sale_num
     |FROM data_course.course_buy_dwm
     |WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
     |GROUP BY course_category_dim_id) as a
     |LEFT JOIN (
     |(SELECT course_category_dim_id, sum(salesvolume) sale_num
     |FROM data_course.course_buy_dwm
     |WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
     |GROUP BY course_category_dim_id) as b
     |ON a.course_category_dim_id = b.course_category_dim_id
     |""".stripMargin
)
```

画面3：
```scala
def subjectBuyCountSql(spark: SparkSession, current: Array[String], last: Array[String]): Unit = {
  // todo
}
```

画面4：
```scala
def subjectBuyCountSql(spark: SparkSession, current: Array[String], last: Array[String]): Unit = {
  spark.sql(
    s"""
       |SELECT a.course_category_dim_id, course_category_dim_id, a.sale_sum sale_num,
       |ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
       |FROM (
       |(SELECT course_category_dim_id, sum(salesvolume) sale_num
       |FROM data_course.course_buy_dwm
       |WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
       |GROUP BY course_category_dim_id) as a
       |LEFT JOIN (
       |(SELECT course_category_dim_id, sum(salesvolume) sale_num
       |FROM data_course.course_buy_dwm
       |WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
       |GROUP BY course_category_dim_id) as b
       |ON a.course_category_dim_id = b.course_category_dim_id
       |""".stripMargin
  )
}
```

画面5：
```scala
def subjectLearningSql(spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame = {
  // todo
}
```

画面6：
```scala
val weekOfYear = getWeekOfYear(current(0)).split(regex = ";")
val sIdS = spark.sql
```

画面7：
```scala
def subjectLearningSql(spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame = {
  spark.sql(
    s"""
       |SELECT a.course_category_dim_id, course_category_dim_id, a.sale_sum sale_num,
       |ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
       |FROM (
       |(SELECT course_category_dim_id, sum(salesvolume) sale_num
       |FROM data_course.course_buy_dwm
       |WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
       |GROUP BY course_category_dim_id) as a
       |LEFT JOIN (
       |(SELECT course_category_dim_id, sum(salesvolume) sale_num
       |FROM data_course.course_buy_dwm
       |WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
       |GROUP BY course_category_dim_id) as b
       |ON a.course_category_dim_id = b.course_category_dim_id
       |""".stripMargin
  )
}
```

画面8：
```scala
def subjectBuyCountSql(spark: SparkSession, current: Array[String], last: Array[String]) = {
  spark.sql(
    s"""
       |SELECT a.course_category_dim_id, course_category_dim_id, a.sale_sum sale_num,
       |ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
       |FROM (
       |(SELECT course_category_dim_id, sum(salesvolume) sale_num
       |FROM data_course.course_buy_dwm
       |WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
       |GROUP BY course_category_dim_id) as a
       |LEFT JOIN (
       |(SELECT course_category_dim_id, sum(salesvolume) sale_num
       |FROM data_course.course_buy_dwm
       |WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
       |GROUP BY course_category_dim_id) as b
       |ON a.course_category_dim_id = b.course_category_dim_id
       |""".stripMargin
  )
}
```

画面9：
无代码内容，仅显示右键菜单。

画面10：
```scala
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
sIdS.repartition(numPartitions = 3)
write.mode = "overwrite"
.writeInto(tableName = "data_subject.subject_sale_week_biz")
spark.sql(sqlText = "select * from data_subject.subject_sale_week_biz").show()
```

画面11：
```scala
spark.conf
