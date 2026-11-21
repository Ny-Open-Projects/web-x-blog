# 画面线理解：11-课程分析-课程访问量分析-步骤3：课程访问量统计结果保存数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\11-课程分析-课程访问量分析-步骤3：课程访问量统计结果保存数据仓库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:38, 02:32, 02:59, 03:39, 03:50, 04:26, 05:22, 05:55, 06:08, 06:28, 06:45, 07:22, 07:39, 08:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:55:19

1) 这一组画面整体在讲如何使用 Spark 读取 Hive 表数据、进行分组聚合，并将结果写入 Hive 表，同时展示了在 Hive 中查看数据的过程。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Hive 表结构定义（CREATE EXTERNAL TABLE）和对应的 Scala 案例类（case class CourseVisitBiz）。
画面2：展示 Spark 代码，定义了日期变量、读取 Hive 表、分组聚合，并准备写入数据。
画面3：在 Spark 代码中设置动态分区模式（spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")）。
画面4：执行 Spark 任务，终端显示任务启动和执行日志。
画面5：Spark 任务执行中，终端显示任务状态和日志。
画面6：Spark 任务执行完成，终端显示任务成功完成。
画面7：Spark 任务执行完成，终端显示任务成功完成。
画面8：Spark 任务执行完成，终端显示任务成功完成。
画面9：Spark 任务执行完成，终端显示任务成功完成。
画面10：Spark 任务执行完成，终端显示任务成功完成。
画面11：切换到 Hive 的 Hue 编辑器界面，准备执行 SQL 查询。
画面12：在 Spark 代码中执行了 Hive 表的分区替换操作。
画面13：在 Hue 编辑器中执行了 SQL 查询（select count() from data_course.course_visit_biz）。
画面14：展示课程大纲，内容为“1.1 课程访问量统计分析”下的“1.1.1 统计步骤”和“1.1.2 APP层数据结构”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面1：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_course.course_visit_biz
(date_info String,
count INT)
PARTITIONED BY (years String,months String,days String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/hive/external/data_course/course_visit_biz';

对应实体：
/**
 * 每天访问量
 * @param date_info 日期，格式：yyyy-MM-dd
 * @param count 访问次数
 * @param years 分区年
 * @param months 分区月
 * @param days 分区日
 */
case class CourseVisitBiz(date_info: String,
count: Int,
years: String,
months: String,
days: String)

画面2：
val spark: SparkSession = ETLEnvironment.getSparkSession(this.getClass.getClassLoader)
def main(args: Array[String]): Unit = {
  val date_info = "2019-11-11"
  val visitCount = visitDF.groupBy(col = "date_info", cols = "years", "months", "days").count()
  visitCount.show()
}

画面3：
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")

画面4：
// 3. 存储到数据表（业务表中）
visitCount.selectExpr(exprs = "date_info", "count", "years", "months", "days")
.write.mode(saveMode = "overwrite")
.insertInto(tableName = "data_course.course_visit_biz")

画面5：
// 3. 存储到数据表（业务表中）
visitCount.selectExpr(exprs = "date_info", "count", "years", "months", "days")
.write.mode(saveMode = "overwrite")
.insertInto(tableName = "data_course.course_visit_biz")

画面6：
// 4. 天然查询
spark.sql("select * from data_course.course_visit_biz").show()

画面7：
// 4. 天然查询
spark.sql("select * from data_course.course_visit_biz").show()

画面8：
// 4. 天然查询
spark.sql("select * from data_course.course_visit_biz").show()

画面9：
// 4. 天然查询
spark.sql("select * from data_course.course_visit_biz").show()

画面10：
// 4. 天然查询
spark.sql("select * from data_course.course_visit_biz").show()

画面11：
（无代码）

画面12：
// 1. 替换分区
spark.sql("replace partition with '2019-11-11' partition by (years, months, days) from data_course.course_visit_biz")

画面13：
select count() from data_course.course_visit_biz

画面14：
（无代码）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：
标题：1.1.2 APP层数据结构
内容：数据结构定义（CREATE EXTERNAL TABLE）和对应的 Scala 案例类（case class CourseVisitBiz）。

画面14：
标题：1.1 课程访问量统计分析
子标题：1.1.1 统计步骤
内容：1. 读取课程访问量事实表数据；2. 以天为单位求和；3. 将结果保存到课程访问量外表。
子标题：1.1.2 APP层数据结构
内容：数据结构定义（CREATE EXTERNAL TABLE）和对应的 Scala 案例类（case class CourseVisitBiz）。

5) 不要评价画面美观，不要输出与课程无关的内容。
