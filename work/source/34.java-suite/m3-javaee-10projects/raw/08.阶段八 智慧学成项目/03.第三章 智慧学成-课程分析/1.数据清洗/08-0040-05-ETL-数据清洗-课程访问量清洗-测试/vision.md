# 画面线理解：05-ETL-数据清洗-课程访问量清洗-测试

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\05-ETL-数据清洗-课程访问量清洗-测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:18, 02:41, 03:15, 04:43, 05:15, 06:16, 07:36, 08:46, 09:06, 10:04, 10:53, 11:34, 12:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:52:17

1) 这一组画面整体在讲如何使用 Spark 编写一个将用户访问日志数据转换为事实表的 ETL 任务，并展示其在 IDE 中的编写、调试和在 Hive 中的执行过程。

2) 按时间顺序列出每张画面的要点：
画面1：在 IntelliJ IDEA 中展示 Scala 代码，定义 SparkSession，读取数据并进行维度映射，设置日期变量和输入路径。
画面2：Hue 文件浏览器界面，正在加载文件，显示加载中状态。
画面3：IntelliJ IDEA 中，运行程序，显示启动命令和终端输出。
画面4：IntelliJ IDEA 的终端，显示 Spark 应用程序启动日志，包括 SparkContext 启动、BlockManager 启动等。
画面5：IntelliJ IDEA 的终端，显示 Spark 初始化日志，包括 Hive Metastore 初始化、Hive 配置加载等。
画面6：IntelliJ IDEA 中，代码编辑器显示 Spark 任务执行日志，包括任务调度、执行器启动等。
画面7：IntelliJ IDEA 中，代码编辑器显示 Spark 任务执行日志，包括任务创建、执行器运行等。
画面8：IntelliJ IDEA 中，打开一个命令行窗口，显示 Spark 任务执行日志。
画面9：IntelliJ IDEA 中，终端显示 Spark 初始化日志。
画面10：IntelliJ IDEA 中，代码编辑器显示 Spark 任务执行日志，包括数据写入 Hive 表。
画面11：IntelliJ IDEA 中，终端显示 Spark 任务执行日志，包括 OutputCommitCoordinator 停止、SparkContext 停止等。
画面12：IntelliJ IDEA 中，终端显示 Spark 任务执行日志，包括 Hive Metastore 操作日志。
画面13：PPT 页面，展示课程大纲，其中包含“2.2.3 数据存储”章节，列出字段及其含义。
画面14：IntelliJ IDEA 中，代码编辑器显示 Spark 任务执行日志，包括任务完成、数据展示。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
```scala
val spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  import spark.implicits._
  // 获取维度映射
  var areaMap = Map[String, String]()
  spark.sql("SELECT * FROM data_dimen_area_dim").as(AreaDimen).map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
  var compMap = Map[String, String]()
  spark.sql("SELECT * FROM data_dimen_course_dim").as(CourseDimen).map(x => {
    compMap += (x.course_dim_id -> x.company_id)
  })
  val sc = spark.sparkContext
  val date_info = "2019-11-04"
  // 读取数据
  val input = sc.textFile(path = s"/user/hive/external/data/course_visit_source/${date_info}")
  val visitClean = input
  // 数据清洗
  .map(_.split(" "))
  .filter(x => {
    x(0) != "null"
  })
```

画面3：
```bash
D:\devtools\Java\jdk1.8.0_221\bin\java.exe ...
```

画面4：
```scala
at org.apache.spark.sql.execution.SQLExecution.withNewExecutionId
at org.apache.spark.sql.DataFrameWriter.run
at org.apache.spark.sql.DataFrameWriter.insertInto
at cn.licks.xc.analysis.VisitSourceToFact.main(VisitSourceToFact.scala:387)
```

画面5：
```scala
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
```

画面6：
```scala
val area_dim = areaMap.get(getAreaId).get
val com_dim = compMap.get(getCompId).get
val ymd = time_dim.split(regexp = "-")
CourseVisitFact(visitId, tmp(0), tmp(1), tmp(2), tmp(3), tmp(4), tmp(5), tmp(6), tmp(7), tmp(8), tmp(9), tmp(10), tmp(11), tmp(12), tmp(13), tmp(14), tmp(15), tmp(16), tmp(17), tmp(18), tmp(19), tmp(20), tmp(21), tmp(22), tmp(23), tmp(24), tmp(25), tmp(26), tmp(27), tmp(28), tmp(29), tmp(30), tmp(31), tmp(32), tmp(33), tmp(34), tmp(35), tmp(36), tmp(37), tmp(38), tmp(39), tmp(40), tmp(41), tmp(42), tmp(43), tmp(44), tmp(45), tmp(46), tmp(47), tmp(48), tmp(49), tmp(50), tmp(51), tmp(52), tmp(53), tmp(54), tmp(55), tmp(56), tmp(57), tmp(58), tmp(59), tmp(60), tmp(61), tmp(62), tmp(63), tmp(64), tmp(65), tmp(66), tmp(67), tmp(68), tmp(69), tmp(70), tmp(71), tmp(72), tmp(73), tmp(74), tmp(75), tmp(76), tmp(77), tmp(78), tmp(79), tmp(80), tmp(81), tmp(82), tmp(83), tmp(84), tmp(85), tmp(86), tmp(87), tmp(88), tmp(89), tmp(90), tmp(91), tmp(92), tmp(93), tmp(94), tmp(95), tmp(96), tmp(97), tmp(98), tmp(99), tmp(100), tmp(101), tmp(102), tmp(103), tmp(104), tmp(105), tmp(106), tmp(107), tmp(108), tmp(109), tmp(110), tmp(111), tmp(112), tmp(113), tmp(114), tmp(115), tmp(116), tmp(117), tmp(118), tmp(119), tmp(120), tmp(121), tmp(122), tmp(123), tmp(124), tmp(125), tmp(126), tmp(127), tmp(128), tmp(129), tmp(130), tmp(131), tmp(132), tmp(133), tmp(134), tmp(135), tmp(136), tmp(137), tmp(138), tmp(139), tmp(140), tmp(141), tmp(142), tmp(143), tmp(144), tmp(145), tmp(146), tmp(147), tmp(148), tmp(149), tmp(150), tmp(151), tmp(152), tmp(153), tmp(154), tmp(155), tmp(156), tmp(157), tmp(158), tmp(159), tmp(160), tmp(161), tmp(162), tmp(163), tmp(164), tmp(165), tmp(166), tmp(167), tmp(168), tmp(169), tmp(170), tmp(171), tmp(172), tmp(173), tmp(174), tmp(175), tmp(176), tmp(177), tmp(178), tmp(179), tmp(180), tmp(181), tmp(182), tmp(183), tmp(184), tmp(185), tmp(186), tmp(187), tmp(188), tmp(189), tmp(190), tmp(191), tmp(192), tmp(193), tmp(194), tmp(195), tmp(196), tmp(197), tmp(198), tmp(199), tmp(200), tmp(201), tmp(202), tmp(203), tmp(204), tmp(205), tmp(206), tmp(207), tmp(208), tmp(209), tmp(210), tmp(211), tmp(212), tmp(213), tmp(
