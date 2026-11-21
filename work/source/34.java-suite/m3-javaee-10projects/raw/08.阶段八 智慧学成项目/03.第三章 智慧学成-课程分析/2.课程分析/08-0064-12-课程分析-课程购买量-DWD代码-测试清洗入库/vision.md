# 画面线理解：12-课程分析-课程购买量-DWD代码-测试清洗入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\12-课程分析-课程购买量-DWD代码-测试清洗入库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 01:03, 01:28, 02:05, 02:32, 02:57, 03:23, 04:06, 04:58, 05:42, 06:17, 06:45, 07:44, 08:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:05:30

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark 中处理课程购买事实表数据，并通过 Hive 和 Nifi 等工具进行数据校验与流转。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- IDE 中展示 Scala 代码，用于将课程购买数据写入 Hive 表。
- 代码片段：
  ```scala
  CourseBuyFact(obj_order_number,
  json.getString("buy_id"),
  time_dim_id, area_id,
  course_obj_price,
  obj_status, obj_user_id,
  ymd(1), ymd(2)
  )
  ```
  ```scala
  val buyDF = spark.createDataFrame(cleanCourseBuy)
  // 配置动态分区
  spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
  buyDF
  .repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
  spark.sql(sql = "select * from data_course.course_buy_fact").show()
  ```

画面2：
- IDE 中展示代码，用于将课程购买数据写入 Hive 表。
- 代码片段：
  ```scala
  buyDF
  .repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
  ```

画面3：
- Hue 界面展示 Hive 表 `course_buy_fact` 的数据样本，包含订单号、商品ID、价格等字段。

画面4：
- IDE 中展示 Scala 代码，用于处理课程维度数据。
- 代码片段：
  ```scala
  var areaMap = Map[String, String]()
  var courseMap = Map[String, String]()
  spark.sql(sql = "SELECT * FROM data_dimen.course_dim").as[CourseDim].collect().map(x => {
    if (x.course_id != null && x.company_id != null) {
      courseMap += (x.course_id.toString -> x.company_id.toString)
    }
    areaMap += (x.city_name -> x.area_id.toString)
  })
  ```

画面5：
- IDE 中展示 Spark 启动日志，显示 Spark 服务在端口 50001 和 4040 上成功启动。

画面6：
- IDE 中展示 Spark 任务执行日志，显示任务因列数不匹配而失败。

画面7：
- Hue 界面展示 Hive 表列表，正在加载中。

画面8：
- Hue 界面展示 Hive 查询编辑器，执行 SQL 查询 `SELECT count(1) FROM course_buy_fact`。

画面9：
- Hue 界面展示查询结果，返回结果为 318。

画面10：
- Hue 界面展示 Table Browser，显示多个数据表。

画面11：
- Nifi 界面展示数据流，包含两个处理节点：一个从 MySQL 到 MySQL，另一个从 MySQL 到 Hive。

画面12：
- IDE 中展示 Spark 代码，用于初始化 Hive 仓库路径和读取数据。
- 代码片段：
  ```scala
  val courseSource = spark.sql(sql = "select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '${date}'").as(CourseOrderSource).collect()
  ```

画面13：
- IDE 中展示 Spark 代码，用于处理课程维度数据。
- 代码片段：
  ```scala
  courseMap += (x.course_id.toString -> x.company_id.toString)
  val date_info = "2019-11-13"
  val courseSource = spark.sql(sql = "select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '${date}'").as(CourseOrderSource).collect()
  ```

画面14：
- PDF 文档页面，展示 DWM 层数据结构，包含课程维度、课程事实表等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
已在上述要点中完整抄录。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- PPT 标题：2.4.2 DWM 层数据，2.4.2.1 DWM 层简介，2.4.2.4 DWM 层数据结构。
- 表格数据：在 PDF 页面中展示课程维度、课程事实表等数据结构。

5) 不要评价画面美观，不要输出与课程无关的内容。
已完成。
