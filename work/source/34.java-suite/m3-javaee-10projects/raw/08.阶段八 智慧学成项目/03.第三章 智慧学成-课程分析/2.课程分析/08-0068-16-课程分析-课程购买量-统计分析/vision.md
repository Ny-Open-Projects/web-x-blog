# 画面线理解：16-课程分析-课程购买量-统计分析

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\16-课程分析-课程购买量-统计分析_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:31, 01:55, 05:05, 05:58, 07:33, 07:55, 08:31, 09:35, 10:03, 10:52, 11:42, 12:10, 12:28, 13:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:08:22

1) 这一组画面整体在讲如何通过Spark程序处理课程购买事实表数据，生成按日期维度聚合的业务指标，并将结果写入目标表。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程统计分析章节，重点是APP层数据结构，包含Hive外部表定义和对应实体类的注释。
画面2：继续展示APP层数据结构，显示了Scala中CourseBuyBiz类的定义，包含字段映射。
画面3：在Hue界面编写并执行Hive SQL，查询课程购买事实表数据，按年月日分组聚合销售额。
画面4：在Hue界面修改Hive SQL，增加WHERE条件，限定查询日期为'2019-09-26'。
画面5：在IDEA中展示Spark程序代码，包含SparkSession初始化、SQL查询语句和结果写入逻辑。
画面6：在IDEA中运行Spark程序，控制台输出SparkSession创建和数据库连接信息。
画面7：在IDEA中运行Spark程序，控制台报错：Cannot up cast 'count' from double to int，提示类型转换失败。
画面8：在IDEA中修改Spark SQL，将count字段的类型从double改为int。
画面9：在IDEA中运行修改后的Spark程序，控制台显示成功执行并输出结果。
画面10：在IDEA中修改Spark程序，设置动态分区模式为“nonstrict”，并添加写入模式为“overwrite”。
画面11：在IDEA中运行修改后的Spark程序，控制台显示成功执行并输出结果。
画面12：在IDEA中修改Spark程序，设置动态分区模式为“nonstrict”，并添加写入模式为“overwrite”。
画面13：在Hue界面查看course_buy_biz表，显示该表无数据。
画面14：展示课程统计分析章节的测试部分，包含运行方法和部分运行结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_course.course_buy_biz
(date_info String,
count INT)
PARTITIONED BY (years String,months String,days String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/hive/external/data_course/course_buy_biz';

对应实体：
/**
 * 每天购买量
 * @param date_info 日期，格式：yyyy-MM-dd
 * @param count 购买量
 * @param years 分年
 * @param months 分月
 * @param days 分日
 */
case class CourseBuyBiz(date_info: String,
count: Int,
years: String,
months: String,
days: String)

画面3：
SELECT
concat_ws('','years, months, days') as date_info,
sum(salesvolume) as count,
years, months, days
FROM data_course.course_buy_dwm
GROUP BY years, months, days

画面4：
SELECT
concat_ws('','years, months, days') as date_info,
sum(salesvolume) as count,
years, months, days
FROM data_course.course_buy_dwm
WHERE concat_ws('','years, months, days') = '2019-09-26'
GROUP BY years, months, days

画面5：
object CourseBuyProcessByBiz {
  // Spark session
  val spark: SparkSession = FileEnvironment.getSparkSession(this.getClass.getSimpleName)

  def main(args: Array[String]): Unit = {
    import spark.implicits._

    val buyDS = spark.sql(
      """
        |SELECT
        |concat_ws('','years, months, days') as date_info,
        |sum(salesvolume) as count,
        |years, months, days
        |FROM data_course.course_buy_dwm
        |WHERE concat_ws('','years, months, days') = '2019-09-26'
        |GROUP BY years, months, days
        |""".stripMargin).as(CourseBuyBiz)
    buyDS.show()
    spark.close()
  }
}

画面6：
val spark: SparkSession = FileEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  import spark.implicits._

  val buyDS = spark.sql(
    """
      |SELECT
      |concat_ws('','years, months, days') as date_info,
      |sum(salesvolume) as count,
      |years, months, days
      |FROM data_course.course_buy_dwm
      |WHERE concat_ws('','years, months, days') = '2019-09-26'
      |GROUP BY years, months, days
      |""".stripMargin).as(CourseBuyBiz)
  buyDS.show()
  spark.close()
}

画面7：
val buyDS = spark.sql(
  """
    |SELECT
    |concat_ws('','years, months, days') as date_info,
    |sum(salesvolume) as count,
    |years, months, days
    |FROM data_course.course_buy_dwm
    |WHERE concat_ws('','years, months, days') = '2019-09-26'
    |GROUP BY years, months, days
    |""".stripMargin).as(CourseBuyBiz)
buyDS.show()
spark.close()

画面8：
val buyDS = spark.sql(
  """
    |SELECT
    |concat_ws('','years, months, days') as date_info,
    |cast(sum(salesvolume) as int) count,
    |years, months, days
    |FROM data_course.course_buy_dwm
    |WHERE concat_ws('','years, months, days') = '2019-09-26'
    |GROUP BY years, months, days
    |""".stripMargin).as(CourseBuyBiz)
buyDS.show()
spark.close()

画面9：
val buyDS = spark.sql(
  """
    |SELECT
    |concat_ws('','years, months, days') as date_info,
    |cast(sum(salesvolume) as int) count,
    |years, months, days
    |FROM data_course.course_buy_dwm
    |WHERE concat_ws('','years, months, days') = '2019-09-26'
    |GROUP BY years, months, days
    |""".stripMargin).as(CourseBuyBiz)
buyDS.show()
spark.close()

画面10：
// 配置动态分区模式
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
buyDS
  .write
  .mode("overwrite")
  .insertInto("data_course.course_buy_fact")
  .show()

画面11：
val buyDS = spark.sql(
  """
    |SELECT
    |concat_ws('','years, months, days') as date_info,
    |cast(sum(salesvolume) as int) count,
    |years, months, days
    |FROM data_course.course_buy_dwm
    |WHERE concat_ws('','years, months, days') = '2019-09-26'
    |GROUP BY years, months, days
    |""".stripMargin).as(CourseBuyBiz)
buyDS.show()
spark.close()

画面12：
val buyDS = spark.sql(
  """
    |SELECT
    |concat_ws('','years, months, days') as date_info,
    |cast(sum(salesvolume) as int) count,
    |years, months, days
    |FROM data_course.course_buy_dwm
    |WHERE concat_ws('','years, months, days') = '2019-09-26'
    |GROUP BY years, months, days
    |""".stripMargin).as(CourseBuyBiz)
buyDS.show()
spark.close()

画面14：
def main(args: Array[String]): Unit = {
  // Run 'CourseBuyProcessByBiz' Ctrl+Shift+F10
  // Debug 'CourseBuyProcessByBiz'
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“2.5 统计分析”，子标题“2.5.1 统计步骤”和“2.5.2 APP层数据结构”。
画面14：PPT标题为“2.5.4 测试”，包含运行方法和部分运行结果表格。
表格数据：
| date_info | count | years | months | days |
| --- | --- | --- | --- | --- |
| 2017-09-30 | 123 | 2017 | 09 | 30 |
| 2017-10-01 | 129 | 2017 | 10 | 01 |
| 2017-10-02 | 137 | 2017 | 10 | 02 |
| 2017-10-03 | 144 | 2017 | 10 | 03 |
| 2017-10-04 | 139 | 2017 | 10 | 04 |
| 2017-10-05 | 149 | 2
