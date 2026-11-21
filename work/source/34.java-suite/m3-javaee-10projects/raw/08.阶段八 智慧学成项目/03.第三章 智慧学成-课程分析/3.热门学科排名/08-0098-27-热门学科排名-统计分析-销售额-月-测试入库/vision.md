# 画面线理解：27-热门学科排名-统计分析-销售额-月-测试入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\27-热门学科排名-统计分析-销售额-月-测试入库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:31, 00:43, 00:50, 00:57, 01:19, 01:34, 01:50, 01:59, 02:08, 02:18, 02:30, 02:50, 03:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:31:24

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spark 应用程序如何读取原始数据、按月聚合计算并写入 Hive 表的过程，同时展示在 Hue 中查看结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Spark 代码，定义了日期范围（2019-10-25），并准备了月份数据。代码中包含 SQL 查询语句，用于从原始数据中选择课程类别ID、名称、销售金额、金额占比和年份。
画面 2: 在 Hue 的 Table Browser 中，显示了表 subject_amount_month_biz，但提示“该表不包含任何数据”。
画面 3: Spark 代码执行日志，显示了初始化对象存储、获取所有数据库等操作。
画面 4: Spark 代码执行日志，显示了任务调度、数据广播和任务提交等过程。
画面 5: Spark 代码执行日志，显示了正在读取文件，文件路径为 HDFS 上的原始数据。
画面 6: Spark 代码执行日志，显示了正在读取文件，文件路径为 HDFS 上的原始数据。
画面 7: 在 Hue 的 Table Browser 中，显示了表 subject_amount_month_biz 的样本数据，其中包含销售金额和金额占比等字段。
画面 8: Spark 代码执行日志，显示了获取数据库和表的操作。
画面 9: Spark 代码执行日志，显示了读取文件，文件路径为 HDFS 上的原始数据。
画面 10: Spark 代码执行日志，显示了读取文件，文件路径为 HDFS 上的原始数据。
画面 11: 在 Hue 的 Table Browser 中，显示了表 subject_amount_month_biz 的“Sample”标签页，列出了表的字段和分区信息。
画面 12: 在 Hue 的 Table Browser 中，显示了表 subject_amount_month_biz 的样本数据，其中包含销售金额和金额占比等字段。
画面 13: 在 Hue 的 Table Browser 中，显示了表 subject_amount_month_biz 的样本数据，其中包含销售金额和金额占比等字段。
画面 14: 展示了文档中的 SQL 语句，用于创建外部表 subject_amount_month_biz，包含字段 course_category_dim_id、course_category_name、sale_amount、amount_percent，分区字段为 years 和 month_of_year，存储格式为 PARQUET。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
def main(args: Array[String]): Unit = {
  import spark.implicits._
  // 1. 读取当前月份的日期范围，例：1号至18号
  val date_info = "2019-10-25"
  val months = getMonthRelativeInterval(date_info).split(regex = "\\")
  val current = months(0).split(regex = "\\")
  val last = months(1).split(regex = "\\")
  // 2. 获取本月所有数据
  // 3. 读取上月数据
  // 4. 读取本月数据
  // 5. 计算指标
  subjectBuyAmountSql(spark, current, last, createReplaceTempView, viewName = "sales_biz_month_tmp")
  // 6. 根据维度id获取相关数据
  val monthOfYear = spark.sql("select
  a.course_category_dim_id,
  a.course_category_name,
  b.name as course_name,
  cast(a.sale_amount as float) as amount,
  cast(a.amount_percent as float) as amount_percent,
  a.year,
  a.month
  from sales_biz_month_tmp a
  join dim_course b on a.course_id = b.id
  where a.year = 2019 and a.month = 10
  group by a.course_category_dim_id, a.course_category_name, b.name, a.year, a.month
  order by a.course_category_dim_id, a.course_category_name, b.name, a.year, a.month
  ").collect()
  // 7. 保存结果
  val tmp = spark.sql("select
  a.course_category_dim_id,
  a.course_category_name,
  b.name as course_name,
  cast(a.sale_amount as float) as amount,
  cast(a.amount_percent as float) as amount_percent,
  a.year,
  a.month
  from sales_biz_month_tmp a
  join dim_course b on a.course_id = b.id
  where a.year = 2019 and a.month = 10
  group by a.course_category_dim_id, a.course_category_name, b.name, a.year, a.month
  order by a.course_category_dim_id, a.course_category_name, b.name, a.year, a.month
  ").collect()
```
画面 14:
```sql
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_amount_month_biz
(course_category_dim_id String,
course_category_name String,
sale_amount Int,
amount_percent FLOAT)
PARTITIONED BY (years String, month_of_year String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
LOCATION '/user/hive/external/data_subject/subject_amount_month_biz'
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14:
PPT 标题：3.5.3.2.1 统计分析步骤
表格数据：
| 字段名 | 类型 |
| --- | --- |
| course_category_dim_id | String |
| course_category_name | String |
| sale_amount | Int |
| amount_percent | FLOAT |
| years | String |
| month_of_year | String |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
