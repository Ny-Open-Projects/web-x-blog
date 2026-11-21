# 画面线理解：16-热门学科排名-统计分析-销售量-月-统计分析步骤及代码编写

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\16-热门学科排名-统计分析-销售量-月-统计分析步骤及代码编写_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:27, 01:37, 02:19, 02:53, 03:18, 04:33, 05:22, 05:45, 06:09, 06:41, 07:28, 07:56, 08:20, 08:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:21:13

1) 这一组画面整体在讲如何使用 Spark 编写月度销售数据统计分析程序，包括数据表结构定义、SQL 查询语句和 Scala 代码实现。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程文档中“3.5.1.2 APP层数据结构”的 SQL 代码，定义了 `data_subject.subject_sale_month.biz` 表。
画面2：展示 `SubjectSalesVolumeByWeekBiz.scala` 文件，包含获取当前周数据的 Scala 代码。
画面3：展示课程文档中“3.5.1.2 月”章节的分析步骤和数据结构。
画面4：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含获取月度数据的 SQL 查询语句和写入操作。
画面5：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含获取月度数据的 Scala 代码。
画面6：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含获取月度数据的 SQL 查询语句。
画面7：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含写入数据和查看结果的 Spark 操作代码。
画面8：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含获取月度数据的 Scala 代码。
画面9：展示 `DateUtils.scala` 文件，包含 `getMonthRelativeInterval` 方法的实现，用于计算月份间隔。
画面10：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含获取月度数据的 Scala 代码。
画面11：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含写入数据和查看结果的 Spark 操作代码。
画面12：展示 `Subject.scala` 文件，定义了 `SubjectSaleMonthBiz` 和 `SubjectSaleMonthWith` 两个 case class。
画面13：展示课程文档中“3.5.1.2.3 统计分析代码”的 Scala 代码，包含导入包和类定义。
画面14：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含获取月度数据的 Scala 代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_sale_month.biz
(course_category_dim_id String,
course_category_name String,
sale_num INT,
sale_percent FLOAT)
PARTITIONED BY (Years String, month_of_year String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
Location "/user/hive/external/data_subject/subject_sale_month_biz"

画面4：
val sld5 = spark.sql(
  """
    |select
    |a.course_category_dim_id,
    |b.name course_category_name,
    |cast(a.sale_num as int) sale_num,
    |cast(a.sale_percent as float) sale_percent,
    |$monthOfYear(0) years,
    |$monthOfYear(1) month_of_year
    |from salesvolume_biz tmp a
    |left join data_dimen.course_category_dim b
    |on a.course_category_dim_id = b.course_category_dim_id
    |""".stripMargin).as[SubjectSaleMonthBiz]

画面7：
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
sld5.repartition(numPartitions = 1)
sld5.write.mode(saveMode = "overwrite")
sld5.insertInto(tableName = "data_subject.subject_sale_month_biz")
spark.sql("select * from data_subject.subject_sale_month_biz").show()
spark.close()

画面12：
case class SubjectSaleMonthBiz(course_category_dim_id: String,
  course_category_name: String,
  sale_num: Int,
  sale_percent: Float,
  years: String,
  month_of_year: String)

画面13：
package cn.itcast.xc.analysis.subject.salesvolume
import cn.itcast.xc.common.EtlEnvironment
import cn.itcast.xc.entity.SubjectSaleMonthBiz
import cn.itcast.xc.utils.DateUtils.{getMonthNum, getMonthRelativeInterval}
import cn.itcast.xc.utils.SubjectUtils.subjectBuyCountSql
import org.apache.spark.sql.SparkSession

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题“3.5.1.2 APP层数据结构”，内容包含 SQL 代码。
画面3：PPT标题“3.5.1.2 月”，内容包含分析步骤和数据结构。
画面13：PPT标题“3.5.1.2.3 统计分析代码”，内容包含 Scala 代码。

5) 不要评价画面美观，不要输出与课程无关的内容。
