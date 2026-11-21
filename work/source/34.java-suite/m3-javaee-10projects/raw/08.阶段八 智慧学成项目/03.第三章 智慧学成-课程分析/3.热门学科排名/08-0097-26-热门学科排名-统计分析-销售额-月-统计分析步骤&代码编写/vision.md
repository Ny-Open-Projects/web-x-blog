# 画面线理解：26-热门学科排名-统计分析-销售额-月-统计分析步骤&代码编写

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\26-热门学科排名-统计分析-销售额-月-统计分析步骤&代码编写_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:27, 00:46, 01:12, 02:02, 02:23, 02:50, 03:07, 03:16, 03:35, 03:56, 04:13, 04:30, 04:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:30:37

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spark 编写月度销售数据统计分析代码，包括数据表结构定义、Spark SQL 查询和动态分区写入。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档，说明月度统计分析步骤，包括获取当月、上月、本月数据，计算维度，根据维度获取相关数据，保存结果。并展示APP层数据结构的SQL代码：CREATE EXTERNAL TABLE IF NOT EXISTS data_subject.subject_amount_month_biz (course_category_dim_id string, course_category.name string, sale_amount int, amount_percent (FLOAT), month_of_year String) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'。

画面2：展示IDE中SubjectSalesByWeekBiz.scala文件，代码中定义了获取当前周的日期范围，创建临时视图，以及查询语句，其中包含SQL：select a.course_category_dim_id, b.name course_category_name, cast(a.sale_amount as float) sale_amount, cast(a.amount_percent as float) amount_percent, (weekOfYear(1)) week_of_year from sales.biz_week_top a left join data_dimen.course_category_dim b on a.course_category_dim_id = b.course_category_dim_id ***.stripMargin().as(SubjectAmountBiz)。

画面3：展示IDE中SubjectSalesByMonthBiz.scala文件，代码中定义了获取当前月的日期范围，创建临时视图，以及查询语句，其中包含SQL：select a.course_category_dim_id, b.name course_category_name, cast(a.sale_amount as float) sale_amount, cast(a.amount_percent as float) amount_percent, (monthOfYear(1)) month_of_year from sales.biz_month_top a left join data_dimen.course_category_dim b on a.course_category_dim_id = b.course_category_dim_id ***.stripMargin().as(SubjectAmountBiz)。

画面4：展示IDE中SubjectSalesByMonthBiz.scala文件，代码中定义了获取当前月的日期范围，创建临时视图，以及查询语句，其中包含SQL：select a.course_category_dim_id, b.name course_category_name, cast(a.sale_amount as float) sale_amount, cast(a.amount_percent as float) amount_percent, (monthOfYear(1)) month_of_year from sales.biz_month_top a left join data_dimen.course_category_dim b on a.course_category_dim_id = b.course_category_dim_id ***.stripMargin().as(SubjectAmountBiz)。

画面5：展示IDE中SubjectSalesByMonthBiz.scala文件，代码中定义了获取当前月的日期范围，创建临时视图，以及查询语句，其中包含SQL：select a.course_category_dim_id, b.name course_category_name, cast(a.sale_amount as float) sale_amount, cast(a.amount_percent as float) amount_percent, (monthOfYear(1)) month_of_year from sales.biz_month_top a left join data_dimen.course_category_dim b on a.course_category_dim_id = b.course_category_dim_id ***.stripMargin().as(SubjectAmountBiz)。

画面6：展示IDE中SubjectSalesByMonthBiz.scala文件，代码中定义了获取当前月的日期范围，创建临时视图，以及查询语句，其中包含SQL：select a.course_category_dim_id, b.name course_category_name, cast(a.sale_amount as float) sale_amount, cast(a.amount_percent as float) amount_percent, (monthOfYear(1)) month_of_year from sales.biz_month_top a left join data_dimen.course_category_dim b on a.course_category_dim_id = b.course_category_dim_id ***.stripMargin().as(SubjectAmountBiz)。

画面7：展示IDE中SubjectSalesByMonthBiz.scala文件，代码中定义了获取当前月的日期范围，创建临时视图，以及查询语句，其中包含SQL：select a.course_category_dim_id, b.name course_category_name, cast(a.sale_amount as float) sale_amount, cast(a.amount_percent as float) amount_percent, (monthOfYear(1)) month_of_year from sales.biz_month_top a left join data_dimen.course_category_dim b on a.course_category_dim_id = b.course_category_dim_id ***.stripMargin().as(SubjectAmountBiz)。

画面8：展示IDE中SubjectSalesByMonthBiz.scala文件，代码中定义了获取当前月的日期范围，创建临时视图，以及查询语句，其中包含SQL：select a.course_category_dim_id, b.name course_category_name, cast(a.sale_amount as float) sale_amount, cast(a.amount_percent as float) amount_percent, (monthOfYear(1)) month_of_year from sales.biz_month_top a left join data_dimen.course_category_dim b on a.course_category_dim_id = b.course_category_dim_id ***.stripMargin().as(SubjectAmountBiz)。

画面9：展示IDE中SubjectSalesByMonthBiz.scala文件，代码中定义了获取当前月的日期范围，创建临时视图，以及查询语句，其中包含SQL：select a.course_category_dim_id, b.name course_category_name, cast(a.sale_amount as float) sale_amount, cast(a.amount_percent as float) amount_percent, (monthOfYear(1)) month_of_year from sales.biz_month_top a left join data_dimen.course_category_dim b on a.course_category_dim_id = b.course_category_dim_id ***.stripMargin().as(SubjectAmountBiz)。

画面10：展示IDE中SubjectSalesByMonthBiz.scala文件，代码中定义了获取当前月的日期范围，创建临时视图，以及查询语句，其中包含SQL：select a.course_category_dim_id, b.name course_category_name, cast(a.sale_amount as float) sale_amount, cast(a.amount_percent as float) amount_percent, (monthOfYear(1)) month_of_year from sales.biz_month_top a left join data_dimen.course_category_dim b on a.course_category_dim_id = b.course_category_dim_id ***.stripMargin().as(SubjectAmountBiz)。

画面11：展示IDE中SubjectSalesByMonthBiz.scala文件，代码中定义了获取当前月的日期范围，创建临时视图，以及查询语句，其中包含SQL：select a.course_category_dim_id, b.name course_category_name, cast(a.sale_amount as float) sale_amount, cast(a.amount_percent as float) amount_percent, (monthOfYear(1)) month_of_year from sales.biz_month_top a left join data_dimen.course_category_dim b on a.course_category_dim_id = b.course_category_dim_id ***.stripMargin().as(SubjectAmountBiz)。

画面12：展示IDE中SubjectSalesByMonthBiz.scala文件，代码中定义了获取当前月的日期范围，创建临时视图，以及查询语句，其中包含SQL：select a.course_category_dim_id, b.name course_category_name, cast(a.sale_amount as float) sale_amount, cast(a.amount_percent as float) amount_percent, (monthOfYear(1)) month_of_year from sales.biz_month_top a left join data_dimen.course_category_dim b on a.course_category_dim_id = b.course_category_dim_id ***.stripMargin().as(SubjectAmountBiz)。

画面13：展示IDE中SubjectSalesByMonthBiz.scala文件，代码中定义了获取当前月的日期范围，创建临时视图，以及查询语句，其中包含SQL：select a.course_category_dim_id, b.name course_category_name, cast(a.sale_amount as float) sale_amount, cast(a.amount_percent as float) amount_percent, (monthOfYear(1)) month_of_year from sales.biz_month_top a left join data_dimen.course_category_dim b on a.course_category_dim_id = b.course_category_dim_id ***.stripMargin().as(SubjectAmountBiz)。

画面14：展示IDE中SubjectSalesByMonthBiz.scala文件，代码中定义了获取当前月的日期范围，创建临时视图，以及查询语句，其中包含SQL：select a.course_category_dim_id, b.name course_category_name, cast(a.sale_amount as float) sale_amount, cast(a.amount_percent as float) amount_percent, (monthOfYear(1)) month_of_year from sales.biz_month_top a left join data_dimen.course_category_dim b on a.course_category_dim_id = b.course_category_dim_id ***.stripMargin().as(SubjectAmountBiz)。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_amount_month_biz
(course_category_dim_id string,
course_category.name string,
sale_amount int,
amount_percent (FLOAT),
month_of_year String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'

画面2：
val s105 = spark.sql(
"""
select
a.course_category_dim_id,
b.name course_category_name,
cast(a.sale_amount as float) sale_amount,
cast(a.amount_percent as float) amount_percent,
(monthOfYear(1)) month_of_year
from sales.biz_week_top a
left join data_dimen.course_category_dim b
on a.course_category_dim_id = b.course_category_dim_id
""".stripMargin().as(SubjectAmountBiz)

画面3：
val s105 = spark.sql(
"""
select
a.course_category_dim_id,
b.name course_category_name,
cast(a.sale_amount as float) sale_amount,
cast(a.amount_percent as float) amount_percent,
(monthOfYear(1)) month_of_year
from sales.biz_month_top a
left join data_dimen.course_category_dim b
on a.course_category_dim_id = b.course_category_dim_id
""".stripMargin().as(SubjectAmountBiz)

画面4：
val s105 = spark.sql(
"""
select
a.course_category_dim_id,
b.name
