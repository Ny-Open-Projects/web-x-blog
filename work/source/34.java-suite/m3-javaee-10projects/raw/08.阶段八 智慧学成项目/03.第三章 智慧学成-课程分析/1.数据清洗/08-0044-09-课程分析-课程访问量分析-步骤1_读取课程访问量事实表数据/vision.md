# 画面线理解：09-课程分析-课程访问量分析-步骤1：读取课程访问量事实表数据

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\09-课程分析-课程访问量分析-步骤1：读取课程访问量事实表数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:37, 02:09, 04:11, 04:20, 05:12, 05:17, 05:26, 05:34, 05:43, 05:58, 06:17, 07:27, 07:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:54:12

1) 这一组画面整体在讲如何在 Spark 中编写代码，根据日期分区查询 Hive 表中的课程访问事实数据，并展示数据在 Hue 和 Sublime Text 中的查看过程。

2) 按时间顺序列出每张画面的要点：
画面1：在 IntelliJ IDEA 中打开 Scala 文件 CourseVisitProcessByDay.scala，显示 SparkSession 的初始化代码和 main 方法的框架。
画面2：在 IDEA 中选中 main 方法的代码块，准备进行编辑或调试。
画面3：在 IDEA 中，光标位于 main 方法内，弹出 SparkSession 的成员方法列表，准备调用相关方法。
画面4：切换到 Hue 的 Table Browser，显示数据库 data_course。
画面5：在 Hue 中查看 data_course 数据库下的表 course_visit_fact 的列结构。
画面6：在 IDEA 中编写 SQL 查询语句，使用 spark.sql 方法查询 data_course.visit_fact 表，条件为 date_info = '2019 11 10'。
画面7：在 Hue 中查看 course_visit_fact 表的数据，显示部分记录，其中 time_dim_id 为 '2019-11-09-10'。
画面8：在 Hue 中切换到 Details 标签页，查看表的详细信息。
画面9：在 Hue 中切换到 Sample 标签页，查看表的样本数据，显示 client_ip、client_sessionid、client_type、visit_time 等字段。
画面10：在 Hue 中切换到多个窗口的视图，显示了 Table Browser、Sublime Text、IDEA、Docker 等工具的界面。
画面11：在 Sublime Text 中打开一个文本文件，内容为日期相关的数据，包括 '2019-11-09-10'、'1573266878000'、'2019 11 09'。
画面12：在 Sublime Text 中，光标在 '2019 11 09' 后，准备进行编辑。
画面13：在 IDEA 中，光标位于 SQL 查询语句中，准备修改或添加代码。
画面14：在 IDEA 中，光标位于 SQL 查询语句中，弹出提示框，提示“该包围块是冗余的...（Ctrl+I）”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1-3：
```scala
package cn.itcast.xc.analysis

import cn.itcast.xc.common.FilEnvironment
import org.apache.spark.sql.SparkSession

/**
 * 课程访问量统计分析
 */
object CourseVisitProcessByDay {
  // Spark session
  val spark: SparkSession = FilEnvironment.getSparkSession(this.getClass.getSimpleName)

  def main(args: Array[String]): Unit = {
  }
}
```

画面6：
```scala
spark.sql(s"select * from data_course.visit_fact where concat_ws('-',${date_info})")
```

画面13-14：
```scala
val date_info = "2019 11 10"
spark.sql(s"select * from data_course.visit_fact where concat_ws('-',${date_info})")
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无 PPT 标题、架构图/流程图或表格数据。

5) 无其他内容。
