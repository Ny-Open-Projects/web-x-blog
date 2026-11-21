# 画面线理解：19-热门学科排名-统计分析-学生人数-周-代码-获取周区间&获取数据&计算涨幅

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\19-热门学科排名-统计分析-学生人数-周-代码-获取周区间&获取数据&计算涨幅_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:06, 03:31, 05:04, 08:08, 09:48, 11:10, 11:30, 11:51, 12:46, 13:04, 13:32, 14:32, 14:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:23:37

1) 这一组画面整体在讲如何使用 Spark Scala 编写程序，通过 Hive 查询数据，计算并展示不同课程分类下用户数及其占比。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Scala 代码，定义了日期范围，准备计算当前周和上周的数据。
画面2：在 Hue 中查看 Hive 表 data_course.learning_course_fact 的结构。
画面3：在 Hue 中编写并执行一个 Hive 查询，筛选指定日期范围内的数据。
画面4：在 Hue 中执行 Hive 查询，按课程分类维度分组统计用户数。
画面5：在 Hue 中执行 Hive 查询，结果显示课程分类维度和用户数。
画面6：在 Hue 中执行 Hive 查询，结果显示课程分类维度和用户占比。
画面7：在 IntelliJ IDEA 中展示 Scala 代码，计算当前周和上周的用户数。
画面8：在 IntelliJ IDEA 中展示 Scala 代码，执行 Hive 查询并显示结果。
画面9：在 IntelliJ IDEA 中展示 Scala 代码，执行 Hive 查询并显示结果。
画面10：在 IntelliJ IDEA 中展示 Scala 代码，执行 Hive 查询并显示结果。
画面11：在 IntelliJ IDEA 中展示 Scala 代码，执行 Hive 查询并显示结果。
画面12：在 Hue 中查看 Hive 表 data_course.learning_course_fact 的数据。
画面13：在 IntelliJ IDEA 中展示 Scala 代码，执行 Hive 查询并显示结果。
画面14：在 IntelliJ IDEA 中展示 Scala 代码，执行 Hive 查询并显示结果。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
```scala
object SubjectLearnNumByWeekBiz {
  // Spark session
  val spark: SparkSession = {
    val spark = SparkSession.builder()
      .appName("SubjectLearnNumByWeekBiz")
      .config("spark.sql.warehouse.dir", "hdfs://node1:8020/user/hive/warehouse")
      .config("spark.sql.catalogImplementation", "hive")
      .config("spark.sql.hive.metastore.uris", "thrift://node1:9083")
      .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
      .config("spark.sql.adaptive.enabled", "true")
      .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
      .config("spark.sql.adaptive.ad
