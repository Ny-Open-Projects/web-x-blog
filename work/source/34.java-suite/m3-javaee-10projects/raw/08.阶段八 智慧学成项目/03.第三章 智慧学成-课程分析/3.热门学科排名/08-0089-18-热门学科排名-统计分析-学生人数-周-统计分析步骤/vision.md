# 画面线理解：18-热门学科排名-统计分析-学生人数-周-统计分析步骤

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\18-热门学科排名-统计分析-学生人数-周-统计分析步骤_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:53, 01:55, 01:57, 01:59, 02:02, 02:23, 02:25, 02:38, 02:39, 02:41, 02:42, 02:48, 02:49, 02:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:22:33

1) 这一组画面整体在讲什么（一句话）：
讲解学生人数统计分析的步骤和APP层数据表结构，包括Hive表定义和Scala实体类定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“3.5.2.1.1 统计分析步骤”列表，包含7个步骤，其中第1步为“获取当前周的时间区间，例：周1 至 周5”，第2步为“获取上周的相同时间区间，例：上周1 至 上周5”，第3步为“获取本周的数据”，第4步为“获取上周的数据”，第5步为“计算增幅”，第6步为“根据维度id获取相关数据”，第7步为“保存结果”。同时展示“3.5.2.1.2 APP层数据结构”的Hive表创建语句。
画面2：与画面1内容相同，仅光标位置不同。
画面3：与画面1内容相同，仅光标位置不同。
画面4：展示“3.5.2.1.2 APP层数据结构”的Hive表创建语句，并在下方新增“对应实体：”部分，显示注释“//热门课程-学生人数(选课)-周”，以及字段注释，如“@param course_category_dim_id 课程分类id”、“@param course_category_name 课程分类名”、“@param user_num 用户数”、“@param user_percent 比例”、“@param years 分区年”、“@param week_of_year 分区年中的周”。
画面5：与画面4内容相同，仅光标位置不同。
画面6：与画面4内容相同，仅光标位置不同。
画面7：与画面4内容相同，仅光标位置不同。
画面8：与画面4内容相同，仅光标位置不同。
画面9：展示“3.5.2.1.1 统计分析步骤”列表，光标位于第1步“获取当前周的时间区间，例：周1 至 周5”。
画面10：与画面9内容相同，仅光标位置不同。
画面11：与画面9内容相同，仅光标位置不同。
画面12：与画面9内容相同，仅光标位置不同。
画面13：与画面4内容相同，仅光标位置不同。
画面14：与画面4内容相同，仅光标位置不同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1-3：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_user_week_biz
(course_category_dim_id String,
course_category_name String,
user_num Int,
user_percent FLOAT)
PARTITIONED BY (years String, week_of_year String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/hive/external/data_subject/subject_user_week_biz';

画面4-8,13-14：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_user_week_biz
(course_category_dim_id String,
course_category_name String,
user_num Int,
user_percent FLOAT)
PARTITIONED BY (years String, week_of_year String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/hive/external/data_subject/subject_user_week_biz';

对应实体：
/*
热门课程-学生人数(选课)-周
*/
@param course_category_dim_id 课程分类id
@param course_category_name 课程分类名
@param user_num 用户数
@param user_percent 比例
@param years 分区年
@param week_of_year 分区年中的周

case class SubjectLearnUserWeekBiz(course_category_dim_id: String,
course_category_name: String,
user_num: Int,
user_percent: Float,
years: String,
week_of_year: String)

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
