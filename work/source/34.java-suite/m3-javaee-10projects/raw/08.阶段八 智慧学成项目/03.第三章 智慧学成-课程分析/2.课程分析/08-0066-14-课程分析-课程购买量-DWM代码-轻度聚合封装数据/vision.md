# 画面线理解：14-课程分析-课程购买量-DWM代码-轻度聚合封装数据

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\14-课程分析-课程购买量-DWM代码-轻度聚合封装数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:59, 01:22, 05:40, 08:06, 10:37, 12:22, 12:58, 14:18, 15:07, 15:27, 16:06, 16:24, 17:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:06:39

1) 这一组画面整体在讲如何通过 Spark 编程将课程购买事实表（course_buy_fact）数据清洗并聚合，生成 DWM 层的课程销售事实表（course_dim_id, salesvolume, years, months, days）。

2) 按时间顺序列出每张画面的要点：
画面1：展示 DWM 层数据结构，包含课程维度、公司维度、课程分类维度、销售金额、年、月、日等字段。
画面2：在 Spark 编程环境中，编写 CourseBuyProcessToDWM.scala 代码，初始化 SparkSession。
画面3：在 Spark 编程环境中，编写 CourseBuyProcessToDWM.scala 代码，定义数据清洗逻辑。
画面4：在 Hive 查询界面，执行 SQL 查询，展示清洗后的课程销售数据。
画面5：在 Spark 编程环境中，编写 CourseBuyProcessToDWM.scala 代码，定义数据清洗逻辑。
画面6：在 Hive 查询界面，执行 SQL 查询，展示清洗后的课程销售数据。
画面7：在 Hive 查询界面，执行 SQL 查询，展示清洗后的课程销售数据。
画面8：在 Sublime Text 编辑器中，编写 Spark 配置文件，定义 Spark 应用的参数。
画面9：在 IntelliJ IDEA 中，编写 CourseBuyProcessToDWM.scala 代码，定义数据清洗逻辑。
画面10：在 IntelliJ IDEA 中，运行 CourseBuyProcessToDWM.scala 代码，执行数据清洗。
画面11：在 IntelliJ IDEA 中，运行 CourseBuyProcessToDWM.scala 代码，执行数据清洗。
画面12：在 IntelliJ IDEA 中，运行 CourseBuyProcessToDWM.scala 代码，执行数据清洗。
画面13：在 IntelliJ IDEA 中，运行 CourseBuyProcessToDWM.scala 代码，执行数据清洗。
画面14：在 IntelliJ IDEA 中，编写 CourseBuyProcessToDWM.scala 代码，定义数据清洗逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```scala
package org.xc.service.offline
import org.apache.spark.sql.SparkSession

object CourseBuyProcessToDWM {
  val spark: SparkSession = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
  def main(args: Array[String]): Unit = {
    import spark.implicits._
    val date_info = "2019-09-23"
    spark.close()
  }
}
```

画面5：
```scala
val date_info = "2019-09-23"
val buyDS = spark.sql(
  """
    |SELECT
    |  a.course_dim_id,
    |  a.company_id, a.course_category_dim_id,
    |  a.sales,
    |  a.salesvolume,
    |  a.years, a.months, a.days
    |FROM (
    |  SELECT
    |    course_dim_id,
    |    sum(price) sales,
    |    count(course_id) salesvolume,
    |    years, months, days
    |  from data.course.course_buy_fact
    |  GROUP BY course_dim_id, years, months, days
    |) a
    |LEFT JOIN data.dimen.course_dim b
    |ON a.course_dim_id = b.course_dim_id
    |""".stripMargin
)
```

画面8：
```text
# source server
# x client host
127.0.0.1
# localhost
localhost
192.168.5.6 xc-online
192.168.5.6 xc-online-hadoop
192.168.5.6 xc-online-spark
192.168.5.6 xc-online-yapi
192.168.5.6 xc-online-redis
192.168.5.6 xc-online-zk
192.168.5.6 xc-online-hbase
```

画面9：
```scala
object CourseBuyProcessToDWM {
  val spark: SparkSession = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
  def main(args: Array[String]): Unit = {
    import spark.implicits._
    val date_info = "2019-09-23"
    val buyDS = spark.sql(
      """
        |SELECT
        |  a.course_dim_id,
        |  a.company_id, a.course_category_dim_id,
        |  a.sales,
        |  a.salesvolume,
        |  a.years, a.months, a.days
        |FROM (
        |  SELECT
        |    course_dim_id,
        |    sum(price) sales,
        |    count(course_id) salesvolume,
        |    years, months, days
        |  from data.course.course_buy_fact
        |  GROUP BY course_dim_id, years, months, days
        |) a
        |LEFT JOIN data.dimen.course_dim b
        |ON a.course_dim_id = b.course_dim_id
        |""".stripMargin
    )
  }
}
```

画面10：
```scala
val date_info = "2019-09-23"
val buyDS = spark.sql(
  """
    |SELECT
    |  a.course_dim_id,
    |  a.company_id, a.course_category_dim_id,
    |  a.sales,
    |  a.salesvolume,
    |  a.years, a.months, a.days
    |FROM (
    |  SELECT
    |    course_dim_id,
    |    sum(price) sales,
    |    count(course_id) salesvolume,
    |    years, months, days
    |  from data.course.course_buy_fact
    |  GROUP BY course_dim_id, years, months, days
    |) a
    |LEFT JOIN data.dimen.course_dim b
    |ON a.course_dim_id = b.course_dim_id
    |""".stripMargin
)
```

画面14：
```scala
SELECT
  a.course_dim_id,
  a.company_id, a.course_category_dim_id,
  a.sales,
  a.salesvolume,
  a.years, a.months, a.days
FROM (
  SELECT
    course_dim_id,
    sum(price) sales,
    count(course_id) salesvolume,
    years, months, days
  from data.course.course_buy_fact
  GROUP BY course_dim_id, years, months, days
) a
LEFT JOIN data.dimen.course_dim b
ON a.course_dim_id = b.course_dim_id
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“2.4.2.2 DWM层数据结构”，表格数据如下：
| DWM层数据字段 | 事实表 (DWD) 字段 | 字段说明 |
| --- | --- | --- |
| course_dim_id | course_dim_id | 课程id |
| company_dim_id | company_dim_id | 公司id |
| course_category_dim_id | course_dim_id | 课程分类id |
| sales | price | 课程销售额 |
| salesvolume | course_dim_id | 课程销量(购买量) |
| years | years | 分区年 |
| months | months | 分区月 |
| days | days | 分区日 |

画面5：PPT 标题为“2.4.2.3 数据清洗分析”，表格数据如下：
| 清洗字段 | 清洗说明 | 清洗后字段名 |
| --- | --- | --- |
| 关联课程分类id |  |  |

5) 不要评价画面美观，不要输出与课程无关的内容。
