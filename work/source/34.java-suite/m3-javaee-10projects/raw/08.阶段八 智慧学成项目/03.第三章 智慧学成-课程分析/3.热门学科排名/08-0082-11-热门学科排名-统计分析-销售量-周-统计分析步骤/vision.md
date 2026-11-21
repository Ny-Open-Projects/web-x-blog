# 画面线理解：11-热门学科排名-统计分析-销售量-周-统计分析步骤

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\11-热门学科排名-统计分析-销售量-周-统计分析步骤_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 02:10, 02:13, 02:23, 02:26, 02:29, 03:02, 03:09, 03:13, 03:19, 03:21, 03:26, 03:27, 03:31, 03:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:17:00

1) 这一组画面整体在讲什么（一句话）：
讲解统计分析步骤中APP层数据表的结构定义及其对应的实体类定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“3.5.1.1 周”章节下的“3.5.1.1.1 统计分析步骤”和“3.5.1.1.2 APP层数据结构”内容，其中APP层数据结构部分显示了CREATE EXTERNAL TABLE语句。
画面2：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面3：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分，下方显示了“对应实体”部分的注释和case class代码。
画面4：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分，下方显示了“对应实体”部分的注释和case class代码。
画面5：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分，下方显示了“对应实体”部分的注释和case class代码。
画面6：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分，下方显示了“对应实体”部分的注释和case class代码。
画面7：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面8：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面9：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面10：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面11：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面12：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面13：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面14：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1-14中出现的SQL语句：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_sale_week_biz
(course_category_dim_id String,
course_category_name String,
sale_num INT,
sale_percent FLOAT)
PARTITIONED BY (years String, week_of_year String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/hive/external/data_subject/subject_sale_week_biz';

画面1-14中出现的case class代码：
/*
热门学科-销量-周
*/
@Param course_category_dim_id 学科id
@Param course_category_name 学科名
@Param sale_num 销售量
@Param sale_percent 张数
@Param years 分区年
@Param week_of_year 分区年中的周
/
case class SubjectSaleweekBiz(course_category_dim_id: String,
course_category_name: String,
sale_num: Int,
sale_percent: Float,
years: String,
)

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
