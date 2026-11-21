# 画面线理解：09-热门学科排名-用户选课-DWD代码-测试清洗入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\09-热门学科排名-用户选课-DWD代码-测试清洗入库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:21, 00:51, 01:18, 02:06, 02:41, 03:24, 04:10, 04:58, 05:41, 06:12, 06:27, 06:36, 07:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:16:08

1) 这一组画面整体在讲什么（一句话）：
演示一个 Scala Spark 应用程序如何从数据源读取课程学习事实数据，进行转换和写入 Hive 表的过程，并展示其运行日志和结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- IDE 界面显示 Scala 代码文件 `UserLearnSourceToFact.scala`。
- 代码内容：从 `data_course_learning_course_source` 表读取数据，转换为 `learning_course_fact` 表结构，并写入 Hive 表 `data_course.learning_course_fact`。
- 代码片段：
```scala
val catId = courseMap.get(obj.course_id).get
val timeId = getDateTime(obj.choose_time, long = 1000, pattern = "yyyy-MM-dd HH")
val ymd = timeId.split(regexp = "")
LearningCourseFact(
  obj.learning_course_id, catId, obj.course_id, obj.user_id, timeId, obj.status, ymd(0), ymd(1), ymd(2)
)
```

画面 2:
- 代码中 `spark.sql` 的 SQL 语句被高亮显示，用于从 `data_course.learning_course_source` 表中查询数据。
- 代码片段：
```scala
spark.sql("SELECT * FROM data_course.learning_course_source WHERE from_unixtime(choose_time, 'yyyy-MM-dd') = '${date_info}'")
```

画面 3:
- 代码中 `spark.conf.set` 设置了 Hive 动态分区模式。
- 代码片段：
```scala
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
```

画面 4:
- IDE 的 Run 窗口显示程序成功运行，耗时 16 秒。
- 日志显示：`Build completed successfully in 16 s 227 ms`

画面 5:
- IDE 显示 `application.properties` 文件内容。
- 代码片段：
```properties
# Spark 配置
spark.sql.adaptive.enabled=true
spark.sql.adaptive.coalescePartitions.enabled=true
```

画面 6:
- HUE 界面显示 Hive 数据库 `data_course` 中的表 `learning_course_dim` 和 `learning_course_fact`。
- 表 `learning_course_dim` 的部分数据列：`course_dim_id`, `course_id`, `user_id`, `time_id`, `status`, `years`, `months`, `days`。

画面 7:
- IDE 显示 `application.properties` 文件内容。
- 代码片段：
```properties
# Spark 配置
spark.sql.adaptive.enabled=true
spark.sql.adaptive.coalescePartitions.enabled=true
```

画面 8:
- 代码中 `spark.sql` 的 SQL 语句被高亮显示，用于从 `data_course.learning_course_source` 表中查询数据。
- 代码片段：
```scala
val learnSource = spark.sql(s"SELECT * from data_course.learning_course_source WHERE from_unixtime(choose_time, 'yyyy-MM-dd') = '${date_info}'")
```

画面 9:
- IDE 的 Run 窗口显示程序运行失败，抛出 `NoSuchElementException: None.get` 异常。
- 异常堆栈信息：
```scala
Exception in thread "main" java.util.NoSuchElementException: None.get
at scala.None$.get (Option.scala:347)
at cn.ictas.xc.analysis.subject.learn.UserLearnSourceToFact$$anonfun$1.apply (UserLearnSourceToFact.scala:37)
at cn.ictas.xc.analysis.subject.learn.UserLearnSourceToFact$$anonfun$1.apply (UserLearnSourceToFact.scala:35)
at scala.collection.TraversableLike$WithFilter.apply (TraversableLike.scala:224)
at scala.collection.TraversableLike$WithFilter.apply (TraversableLike.scala:224)
at scala.collection.mutable.ArrayOpsRef.foreach (ArrayOps.scala:160)
at scala.collection.TraversableLike$WithFilter.foreach (TraversableLike.scala:224)
at cn.ictas.xc.analysis.subject.learn.UserLearnSourceToFact.main (UserLearnSourceToFact.scala:55)
```

画面 10:
- 代码中 `try-catch` 块被高亮显示，用于处理 `NoSuchElementException` 异常。
- 代码片段：
```scala
try {
  catId = courseMap.get(obj.course_id).get
} catch {
  case _ =>
}
```

画面 11:
- IDE 的 Run 窗口显示程序运行失败，抛出 `NoSuchElementException: None.get` 异常。
- 异常堆栈信息：
```scala
Exception in thread "main" java.util.NoSuchElementException: None.get
at scala.None$.get (Option.scala:347)
at cn.ictas.xc.analysis.subject.learn.UserLearnSourceToFact$$anonfun$1.apply (UserLearnSourceToFact.scala:37)
at cn.ictas.xc.analysis.subject.learn.UserLearnSourceToFact$$anonfun$1.apply (UserLearnSourceToFact.scala:35)
at scala.collection.TraversableLike$WithFilter.apply (TraversableLike.scala:224)
at scala.collection.TraversableLike$WithFilter.apply (TraversableLike.scala:224)
at scala.collection.mutable.ArrayOpsRef.foreach (ArrayOps.scala:160)
at scala.collection.TraversableLike$WithFilter.foreach (TraversableLike.scala:224)
at cn.ictas.xc.analysis.subject.learn.UserLearnSourceToFact.main (UserLearnSourceToFact.scala:55)
```

画面 12:
- IDE 的 Run 窗口显示程序运行日志，显示任务正在执行。
- 日志信息：
```text
19/11/28 16:28:54 INFO DAGScheduler: Submitting TaskSet 2 (2 partitions, 0.0 KB) to 1 executor(s) for stage 1
19/11/28 16:28:54 INFO BlockManagerMasterEndpoint: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMasterEndpoint: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.10:4040
19/11/28 16:28:54 INFO BlockManagerMaster: Registering BlockManager with ID: 10.0.0.
