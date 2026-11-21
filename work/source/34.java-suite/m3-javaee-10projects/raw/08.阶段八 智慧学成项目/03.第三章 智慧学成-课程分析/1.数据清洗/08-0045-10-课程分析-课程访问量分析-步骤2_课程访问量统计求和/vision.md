# 画面线理解：10-课程分析-课程访问量分析-步骤2：课程访问量统计求和

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\10-课程分析-课程访问量分析-步骤2：课程访问量统计求和_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:50, 01:33, 02:19, 03:31, 03:50, 04:01, 04:13, 04:27, 04:36, 05:30, 05:42, 05:56, 06:10, 06:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:54:45

1) 这一组画面整体在讲如何使用 Spark SQL 从 Hive 表中按日期维度聚合课程访问量，并将结果展示出来。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Scala 代码，定义 SparkSession，设置日期变量，构建 SQL 查询语句，准备从 Hive 表 data_course.course_visit_fact 中按日期维度聚合访问量。
画面2：展示 PPT 内容，标题为“1.1.2 APP层数据结构”，包含 Hive 表创建语句（CREATE EXTERNAL TABLE）和对应的 Scala 案例类定义（case class CourseVisitBiz）。
画面3：展示 PPT 内容，标题为“1.1.3 编写代码”，展示 Scala 案例类定义（case class CourseVisitBiz）。
画面4：在 Scala 代码中，右键选中变量 visitDF，弹出菜单选择“Generate...”并点击“Generate Scala Code”。
画面5：展示 Hue 界面，显示 Hive 表 data_course.course_visit_fact 的数据，按日期分区展示。
画面6：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面7：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面8：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面9：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面10：展示 PPT 内容，标题为“1.1.3 编写代码”，展示 Scala 案例类定义（case class CourseVisitBiz）。
画面11：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面12：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面13：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面14：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```scala
object CourseVisitProcessByDay {
  def main(args: Array[String]): Unit = {
    val spark: SparkSession = SparkSession.builder()
      .appName("CourseVisitProcessByDay")
      .config("spark.sql.warehouse.dir", "hdfs://node1:8020/user/hive/warehouse")
      .config("spark.sql.catalogImplementation", "hive")
      .enableHiveSupport()
      .getOrCreate()

    val date_info = "2020-11-11"
    val visitDF = spark.sql(s"select concat_ws('-',years,months,days) as date_info from data_course.course_visit_fact where concat_ws('-',years,months,days) = '$date_info'")
    // 2. 查询
    // 3. 展示
    // 4. 关闭资源
    spark.close()
  }
}
```

画面2：
```sql
CREATE EXTERNAL TABLE IF NOT EXISTS data_course.course_visit_biz (
  date_info String,
  count INT
)
PARTITIONED BY (years String, months String, days String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
LOCATION '/user/hive/external/data_course/course_visit_biz';
```

画面3：
```scala
case class CourseVisitBiz(date_info: String,
  count: Int,
  years: String,
  months: String,
  days: String)
```

画面6：
```scala
val visitCount = visitDF.groupBy(col = "date_info").count()
visitCount.show()
```

画面10：
```scala
package cn.itcast.xc.analysis.visit
```

画面11：
```scala
val visitCount = visitDF.groupBy(col = "date_info", cols = "years", "months", "days").count()
visitCount.show()
```

画面12：
```scala
val visitCount = visitDF.groupBy(col = "date_info", cols = "years", "months", "days").count()
visitCount.show()
```

画面13：
```scala
val visitCount = visitDF.groupBy(col = "date_info", cols = "years", "months", "days").count()
visitCount.show()
```

画面14：
```scala
val visitCount = visitDF.groupBy(col = "date_info", cols = "years", "months", "days").count()
visitCount.show()
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面2：
标题：1.1.2 APP层数据结构
内容：
- Hive 表创建语句（CREATE EXTERNAL TABLE）
- 对应实体类（case class CourseVisitBiz）定义

画面3：
标题：1.1.3 编写代码
内容：
- Scala 案例类定义（case class CourseVisitBiz）

画面10：
标题：1.1.3 编写代码
内容：
- Scala 包声明（package cn.itcast.xc.analysis.visit）

5) 无
