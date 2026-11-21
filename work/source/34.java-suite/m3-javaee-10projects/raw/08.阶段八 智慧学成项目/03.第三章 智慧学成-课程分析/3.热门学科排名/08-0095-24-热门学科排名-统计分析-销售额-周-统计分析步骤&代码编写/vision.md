# 画面线理解：24-热门学科排名-统计分析-销售额-周-统计分析步骤&代码编写

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\24-热门学科排名-统计分析-销售额-周-统计分析步骤&代码编写_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:40, 01:02, 01:25, 01:38, 02:10, 02:44, 02:57, 03:14, 03:48, 04:11, 04:22, 04:50, 05:11, 05:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:28:20

1) 这一组画面整体在讲如何使用 Spark 编写周粒度销售金额统计程序，涉及数据读取、时间处理、SQL 查询和结果写入。

2) 按时间顺序列出每张画面的要点：
画面1: 展示项目结构，选中 `SubjectSalesByWeekBiz.scala` 文件，准备编写周销售统计代码。
画面2: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义主函数，初始化 SparkSession，解析日期参数。
画面3: 展示 `SubjectUtils.scala` 文件内容，包含 `subjectBuyAmountSql` 函数，定义 SQL 查询语句。
画面4: 切换到 Hive 图形界面，展示 `sales` 数据库下的表结构，包括 `salesvolume`、`salesvolume_biz_tmp` 等。
画面5: 回到代码编辑器，展示 `SubjectUtils.scala` 文件中 `subjectBuyAmountSql` 函数的 SQL 语句。
画面6: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `subjectBuyAmountSql` 函数，创建临时视图 `salesvolume_biz_tmp`。
画面7: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `weekOfYear` 变量，加载 SQL 文件。
画面8: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `SubjectAmountWeekBiz` 案例类，用于封装周销售数据。
画面9: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `SubjectAmountMonthBiz` 案例类，用于封装月销售数据。
画面10: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `SubjectAmountWeekBiz` 案例类，用于封装周销售数据。
画面11: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `SubjectSalesByWeekBiz` 类，包含 `subjectBuyAmountSql` 函数。
画面12: 展示 `SubjectUtils.scala` 文件内容，包含 `subjectBuyAmountSql` 函数，定义 SQL 查询语句。
画面13: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `subjectBuyAmountSql` 函数，创建临时视图 `salesvolume_biz_tmp`。
画面14: 展示 PPT 页面，标题为“3.5.3 销售额”，子标题“3.5.3.1 周”，内容为“3.5.3.1.1 统计分析步骤”，并列出 7 个步骤，其中步骤 7 为“保存结果”，并展示 SQL 创建外部表语句。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面2:
```scala
package cn.itcast.xc.analysis.subject.sales

import cn.itcast.xc.common.fileEnvironment
import cn.itcast.xc.entity.SubjectSaleBiz
import cn.itcast.xc.utils.DateUtils.getWeekNum, getWeekRelativelyInterval
import org.apache.spark.sql.SparkSession

object SubjectSalesByWeekBiz {
  val spark: SparkSession = EtlEnvironment.getSparkSession(this.getClass.getSimpleName)

  def main(args: Array[String]): Unit = {
    import spark.implicits._
    val date_info = args(0)
    val weeks = getWeekRelativelyInterval(date_info).split(regex = "-")
    val current = weeks(0).split(regex = "-")
    val last = weeks(1).split(regex = "-")
  }
}
```

画面3:
```scala
def subjectBuyAmountSql(spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame = {
  spark.sql(
    """
      SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num,
      ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
      FROM (SELECT course_category_dim_id, sum(salesvolume) sale_num
      FROM data_course.course_buy_dim
      WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
      GROUP BY course_category_dim_id) as a
      LEFT JOIN (
      SELECT course_category_dim_id, sum(salesvolume) sale_num
      FROM data_course.course_buy_dim
      WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
      GROUP BY course_category_dim_id) as b
      ON a.course_category_dim_id = b.course_category_dim_id
    """.stripMargin
  )
}
```

画面4:
```sql
SELECT a.course_category_dim_id, course_buy_dim_id, a.sale_num sale_num,
ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
FROM (SELECT course_category_dim_id, sum(salesvolume) sale_num
FROM data_course.course_buy_dim
WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
GROUP BY course_category_dim_id) as a
LEFT JOIN (
SELECT course_category_dim_id, sum(salesvolume) sale_num
FROM data_course.course_buy_dim
WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
GROUP BY course_category_dim_id) as b
ON a.course_category_dim_id = b.course_category_dim_id
```

画面6:
```scala
subjectBuyAmountSql(spark, current, last).createReplaceTempView(viewName = "salesvolume_biz_tmp")
```

画面7:
```scala
val weekOfYear = getWeekNum(current(0)).split(regex = "-")
val sids = spark.sql(
  """
    select
      a.course_category_dim_id,
      b.name course_category_name,
      cast(a.sale_num as float) sale_amount,
      cast(a.sale_percent as float) amount_percent,
      ${weekOfYear(0)} week_of_year
    from salesvolume_biz_tmp a
    left join data_dimen.course_category_dim b
    on a.course_category_dim_id = b.course_category_dim_id
  """.stripMargin
)
```

画面8:
```scala
case class SubjectAmountWeekBiz(course_category_dim_id: String,
  course_category_name: String,
  sale_amount: Float,
  amount_percent: Float,
  years: String,
  week_of_year: String)
```

画面9:
```scala
case class SubjectAmountMonthBiz(course_category_dim_id: String,
  course_category_name: String,
  sale_amount: Float,
  amount_percent: Float,
  years: String,
  month_of_year: String)
```

画面10:
```scala
case class SubjectAmountWeekBiz(course_category_dim_id: String,
  course_category_name: String,
  sale_amount: Float,
  amount_percent: Float,
  years: String,
  week_of_year: String)
```

画面11:
```scala
val date_info = args(0)
val weeks = getWeekRelativelyInterval(date_info).split(regex = "-")
val current = weeks(0).split(regex = "-")
val last = weeks(1).split(regex = "-")
```

画面12:
```scala
SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num,
ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
FROM (SELECT course_category_dim_id, sum(salesvolume) sale_num
FROM data_course.course_buy_dim
WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
GROUP BY course_category_dim_id) as a
LEFT JOIN (
SELECT course_category_dim_id, sum(salesvolume) sale_num
FROM data_course.course_buy_dim
WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
GROUP BY course_category_dim_id) as b
ON a.course_category_dim_id = b.course_category_dim_id
```

画面13:
```scala
subjectBuyAmountSql(spark, current, last).createReplaceTempView(viewName = "salesvolume_biz_tmp")
```

画面14:
```sql
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_amount_week_biz
(course_category_dim_id String,
course_category_name string,
sale_amount Float,
amount_percent Float)
PARTITIONED BY (years string, week_of_year string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面14:
标题: 3.5.3 销售额
子标题: 3.5.3.1 周
子子标题: 3.5.3.1.1 统计分析步骤
内容:
1. 获取当前周的时间区间，例如：上周1至上周5
2. 获取上周的时间区间，例如：上周1至上周5
3. 获取本周的数据
4. 获取上周的数据
5. 计算增幅
6. 根据维度id获取相关数据
7. 保存结果
表格数据:
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_amount_week_biz
(course_category_dim_id String,
course_category_name string,
sale_amount Float,
amount_percent Float)
PARTITIONED BY (years string, week_of_year string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'

5) 无
