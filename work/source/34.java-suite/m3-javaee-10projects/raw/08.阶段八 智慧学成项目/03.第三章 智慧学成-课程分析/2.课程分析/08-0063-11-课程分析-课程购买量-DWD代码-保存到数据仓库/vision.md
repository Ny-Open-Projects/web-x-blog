# 画面线理解：11-课程分析-课程购买量-DWD代码-保存到数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\11-课程分析-课程购买量-DWD代码-保存到数据仓库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:27, 00:29, 01:07, 01:10, 01:15, 01:41, 01:54, 02:05, 02:09, 02:15, 03:45, 03:48, 04:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:04:59

1) 这一组画面整体在讲如何使用 Spark SQL 和 DataFrame API 对课程购买和访问数据进行清洗、转换和写入事实表。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了课程购买事实表的 Scala 代码，包含从 JSON 提取数据、解析时间戳、构造 CourseBuyFact 对象并写入数据。
画面2: 代码中对时间戳进行拆分，构造 CourseBuyFact 对象，并调用 spark.createDataFrame。
画面3: 代码中定义了课程购买数据源的 SQL 查询，用于从数据库中提取数据。
画面4: 代码中调用 spark.createDataFrame，传入 CourseBuy 对象，并设置 Spark 配置。
画面5: 代码中调用 spark.createDataFrame，传入 CourseBuy 对象，并设置 Spark 配置。
画面6: 代码中调用 spark.createDataFrame，传入 CourseBuy 对象，并设置 Spark 配置。
画面7: IDE 中打开搜索框，准备搜索代码或类。
画面8: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。
画面9: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。
画面10: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。
画面11: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。
画面12: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。
画面13: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。
画面14: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```scala
try {
  areaMap.get(implicit getAreaMap.get(obj.user_id).get).get
} catch {
  case _ =>
}
// 公司维度
val json = JSON.parseArray(obj.details).getJSONObject(index = 8)
val con2d = courseMap.get(json.getString(key = "item_id")).get
// 年月日维度
val ymd = time_dim_id.split(regex = "-")
CourseBuyFact(obj.order_number,
  json.getString(key = "item_id"),
  time_dim_id, areaId,
  con2d, obj.price,
  obj.status, obj.user_id,
  ymd(0), ymd(1), ymd(2)
)
```

画面2:
```scala
// 年月日维度
val ymd = time_dim_id.split(regex = "-")
CourseBuyFact(obj.order_number,
  json.getString(key = "item_id"),
  time_dim_id, areaId,
  con2d, obj.price,
  obj.status, obj.user_id,
  ymd(0), ymd(1), ymd(2)
)
```

画面3:
```scala
val courseBuySource = courseSource.map(obj => {
  val time_dim_id = getDateTimeStr(obj.order_time, long = 1000, pattern = "yyyy-MM-dd HH")
  // 年月日维度
  val ymd = time_dim_id.split(regex = "-")
  CourseBuyFact(obj.order_number,
    json.getString(key = "item_id"),
    time_dim_id, areaId,
    con2d, obj.price,
    obj.status, obj.user_id,
    ymd(0), ymd(1), ymd(2)
  )
})
```

画面4:
```scala
spark.createDataFrame(CleanCourseBuy)
```

画面5:
```scala
spark.createDataFrame(CleanCourseBuy)
```

画面6:
```scala
spark.createDataFrame(CleanCourseBuy)
```

画面7:
无代码。

画面8:
```scala
val buyOF = spark.createDataFrame(CleanCourseBuy)
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
buyOF.repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
spark.sql(sqlText = "select * from data_course.course_buy_fact").show()
```

画面9:
```scala
val buyOF = spark.createDataFrame(CleanCourseBuy)
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
buyOF.repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
spark.sql(sqlText = "select * from data_course.course_buy_fact").show()
```

画面10:
```scala
val buyOF = spark.createDataFrame(CleanCourseBuy)
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
buyOF.repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
spark.sql(sqlText = "select * from data_course.course_buy_fact").show()
```

画面11:
```scala
val buyOF = spark.createDataFrame(CleanCourseBuy)
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
buyOF.repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
spark.sql(sqlText = "select * from data_course.course_buy_fact").show()
```

画面12:
```scala
val buyOF = spark.createDataFrame(CleanCourseBuy)
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
buyOF.repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
spark.sql(sqlText = "select * from data_course.course_buy_fact").show()
```

画面13:
```scala
val data_info = "2019-11-11"
val cleanCourseBuy = courseSource.map(obj => {
  val time_dim_id = getDateTimeStr(obj.order_time, long = 1000, pattern = "yyyy-MM-dd HH")
  // 年月日维度
  val ymd = time_dim_id.split(regex = "-")
  CourseBuyFact(obj.order_number,
    json.getString(key = "item_id"),
    time_dim_id, areaId,
    con2d, obj.price,
    obj.status, obj.user_id,
    ymd(0), ymd(1), ymd(2)
  )
})
```

画面14:
```scala
val buyOF = spark.createDataFrame(CleanCourseBuy)
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
buyOF.repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
spark.sql(sqlText = "select * from data_course.course_buy_fact").show()
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
