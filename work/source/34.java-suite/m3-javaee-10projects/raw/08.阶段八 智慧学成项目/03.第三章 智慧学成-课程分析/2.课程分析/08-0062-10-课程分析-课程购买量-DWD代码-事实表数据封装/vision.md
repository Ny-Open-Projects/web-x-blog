# 画面线理解：10-课程分析-课程购买量-DWD代码-事实表数据封装

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\10-课程分析-课程购买量-DWD代码-事实表数据封装_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:19, 02:57, 04:51, 06:33, 08:08, 09:49, 10:37, 11:00, 11:54, 13:30, 14:11, 14:46, 15:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:04:17

1) 这一组画面整体在讲如何使用 Spark SQL 从 Hive 表中读取订单数据，并通过 Scala 代码进行数据转换和映射，最终生成事实表 CourseBuyFact。

2) 按时间顺序列出每张画面的要点：
画面1：展示 IDEA 中的 Scala 代码，定义了用户维度、区域维度和课程维度的映射逻辑，以及从 Hive 表 data_course.course_orders_source 中读取数据的 SQL 语句。
画面2：展示 Hue 界面中 data_course.course_orders_source 表的数据，显示了订单号、价格、状态等字段。
画面3：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面4：展示 IDEA 中的 Scala 代码，定义了 CourseOrdersSource 的数据结构和映射方法。
画面5：展示 IDEA 中的 Scala 代码，定义了 SparkSession 和数据处理的日期信息。
画面6：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面7：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面8：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面9：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面10：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面11：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面12：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面13：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面14：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```scala
def main(args: Array[String]): Unit = {
  import spark.implicits._
  // 用户维度
  var userMap = Map[String, String]()
  spark.sql("select * from data_dimen.user_dim").as[UserDim].collect().map(x => {
    userMap += (x.user_id -> x.id)
  })
  // 区域维度
  var areaMap = Map[String, String]()
  spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDim].collect().map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
  // 课程维度
  var courseMap = Map[String, String]()
  spark.sql("SELECT * FROM data_dimen.course_dim").as[CourseDim].collect().map(x => {
    if (x.course_dim_id != null && x.company_id != null) {
      courseMap += (x.course_dim_id.toString -> x.company_id.toString)
    }
  })
  // 日期信息
  val data_info = "2019-11-13"
  // 读取数据
  spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
}
```

画面2：
```sql
SELECT * FROM data_course.course_orders_source
```

画面3：
```scala
val data_info = "2019-11-13"
val courseSource = spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面4：
```scala
case class CourseOrdersSource(
  order_number: String,
  course_orders_source_price: Float,
  course_orders_source_status: String,
  course_orders_source_order_time: String,
  course_orders_source_order_id: String,
  course_orders_source_user_id: String
)
```

画面5：
```scala
val spark = SparkSession.builder().appName("CourseBuyByHiveToFact").config("spark.sql.catalogImplementation", "hive").getOrCreate()
val sc = spark.sparkContext
val data_info = args(0)
```

画面6：
```scala
val data_info = "2019-11-13"
val courseSource = spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面7：
```scala
val data_info = "2019-11-13"
val courseSource = spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面8：
```scala
val data_info = "2019-11-13"
val courseSource = spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面9：
```scala
val data_info = "2019-11-13"
val courseSource = spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面10：
```scala
val data_info = "2019-11-13"
val courseSource = spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面11：
```scala
val data_info = "2019-11-13"
val courseSource = spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面12：
```scala
val data_info = "2019-11-13"
val courseSource = spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面13：
```scala
val data_info = "2019-11-13"
val courseSource = spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面14：
```scala
val data_info = "2019-11-13"
val courseSource = spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
