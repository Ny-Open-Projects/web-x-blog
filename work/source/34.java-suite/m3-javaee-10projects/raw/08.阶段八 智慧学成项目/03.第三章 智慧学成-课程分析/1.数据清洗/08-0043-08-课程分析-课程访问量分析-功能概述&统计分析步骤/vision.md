# 画面线理解：08-课程分析-课程访问量分析-功能概述&统计分析步骤

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\08-课程分析-课程访问量分析-功能概述&统计分析步骤_【海量资源尽在 666java.com】.mp4
- 抽帧：8 帧 @ 02:02, 02:44, 02:47, 03:05, 03:07, 03:21, 03:23, 03:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:53:48

1) 这一组画面整体在讲课程访问量统计分析的APP层数据结构，包括Hive表定义和Scala case class定义。

2) 按时间顺序列出每张画面的要点：
画面1: 展示“1.1.1 统计步骤”和“1.1.2 APP层数据结构”标题，Hive表创建语句和Scala case class定义部分可见。
画面2: 鼠标光标在Hive表创建语句的PARTITIONED BY部分，下方Scala case class定义部分可见。
画面3: 鼠标光标在Scala case class定义的“days: string”字段上。
画面4: 鼠标光标在Scala case class定义的“months”字段上。
画面5: 鼠标光标在Hive表创建语句的“PARTITIONED BY”部分。
画面6: 鼠标光标在“1.1.2 APP层数据结构”标题上。
画面7: 鼠标光标在Hive表创建语句的“PARTITIONED BY”部分。
画面8: 鼠标光标在“1.1.2 APP层数据结构”标题上。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1-8中出现的SQL语句：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_course.course_visit_biz
(date_info String,
count INT)
PARTITIONED BY (years String,months String,days String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/hive/external/data_course/course_visit_biz';

画面1-8中出现的Scala代码：
/**
 * 每天访问量
 */
@paran date_info 日期，格式：yyyy-MM-dd
@paran count 访问次数
@paran years 分年
@paran months 分月
@paran days 分日
case class CourseVisitBiz(date_info: String,
count: Int,
years: String,
months: String,
days: string);
