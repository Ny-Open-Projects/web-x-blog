# 画面线理解：13即时查询-统计分析-步骤1：代码-测试

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\13即时查询-统计分析-步骤1：代码-测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:20, 00:32, 00:41, 00:48, 01:29, 02:07, 02:18, 02:31, 02:46, 03:00, 03:15, 03:33, 03:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:01:42

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spark SQL 读取 Hive 分区表数据，通过自定义 UDF 处理时间字段，并将结果写入 Hive 表。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Scala 代码，定义 SparkSession，读取本地文件路径，创建 DataFrame 并注册 UDF。
画面 2: 展示 Spark SQL 查询语句，包含 group by、join、left join 等操作。
画面 3: 展示 Spark 应用启动日志，包括 BlockManager、HiveMetastore、SparkContext 等初始化信息。
画面 4: 展示 Spark 任务执行日志，显示任务提交、分区信息和执行状态。
画面 5: 展示 Spark 读取文件的详细日志，包括文件路径和读取时间。
画面 6: 展示 Spark SQL 查询结果，包含学习课程 ID、用户 ID、学习时长、日期等字段。
画面 7: 展示代码中设置 Hive 动态分区模式，并写入 Hive 表。
画面 8: 展示 Spark 启动日志，包括 Hive 客户端、数据库连接等信息。
画面 9: 展示 Hue 平台的 Table Browser 界面，显示表结构。
画面 10: 展示 Hue 平台的分区列表，显示不同日期分区。
画面 11: 展示 Spark SQL 查询结果，包含学习课程 ID、用户 ID、学习时长、日期等字段。
画面 12: 展示 Hue 平台的分区列表，显示不同日期分区。
画面 13: 展示 Spark SQL 查询结果，包含学习课程 ID、用户 ID、学习时长、日期等字段。
画面 14: 展示 PPT 页面，标题为“3.2 步骤2: 保存到 es, hbase”，子标题为“3.2.1 保存逻辑”，并展示部分 SQL 代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
object InstantQueryStepTolive {
  // 1. 获取 SparkSession
  val spark: SparkSession = ELEnvironment.getSparkSession(this.getClass.getSimpleName, eTableName = null)
  // 2. 获取 SparkContext
  val sc = spark.sparkContext
  // 3. 读取日期参数
  val date_info = "2019-12-11"
  val learnSource = sc.textFile(path = s"/user/hive/external/data_course/learning_course_online_source/${date_info}")
  val learnSourceRDD = learnSource.map(split regex = ".*", arr = {
    UserLearnOnline(arr(0), arr(1), arr(2), arr(3), arr(4), arr(5), arr(6), arr(7), arr(8), arr(9), arr(10), arr(11), arr(12), arr(13), arr(14), arr(15), arr(16), arr(17), arr(18), arr(19), arr(20), arr(21), arr(22), arr(23), arr(24), arr(25), arr(26), arr(27), arr(28), arr(29), arr(30), arr(31), arr(32), arr(33), arr(34), arr(35), arr(36), arr(37), arr(38), arr(39), arr(40), arr(41), arr(42), arr(43), arr(44), arr(45), arr(46), arr(47), arr(48), arr(49), arr(50), arr(51), arr(52), arr(53), arr(54), arr(55), arr(56), arr(57), arr(58), arr(59), arr(60), arr(61), arr(62), arr(63), arr(64), arr(65), arr(66), arr(67), arr(68), arr(69), arr(70), arr(71), arr(72), arr(73), arr(74), arr(75), arr(76), arr(77), arr(78), arr(79), arr(80), arr(81), arr(82), arr(83), arr(84), arr(85), arr(86), arr(87), arr(88), arr(89), arr(90), arr(91), arr(92), arr(93), arr(94), arr(95), arr(96), arr(97), arr(98), arr(99), arr(100), arr(101), arr(102), arr(103), arr(104), arr(105), arr(106), arr(107), arr(108), arr(109), arr(110), arr(111), arr(112), arr(113), arr(114), arr(115), arr(116), arr(117), arr(118), arr(119), arr(120), arr(121), arr(122), arr(123), arr(124), arr(125), arr(126), arr(127), arr(128), arr(129), arr(130), arr(131), arr(132), arr(133), arr(134), arr(135), arr(136), arr(137), arr(138), arr(139), arr(140), arr(141), arr(142), arr(143), arr(144), arr(145), arr(146), arr(147), arr(148), arr(149), arr(150), arr(151), arr(152), arr(153), arr(154), arr(155), arr(156), arr(157), arr(158), arr(159), arr(160), arr(161), arr(162), arr(163), arr(164), arr(165), arr(166), arr(167), arr(168), arr(169), arr(170), arr(171), arr(172), arr(173), arr(174), arr(175), arr(176), arr(177), arr(178), arr(179), arr(180), arr(181), arr(182), arr(183), arr(184), arr(185), arr(186), arr(187), arr(188), arr(189), arr(190), arr(191), arr(192), arr(193), arr(194), arr(195), arr(196), arr(197), arr(198), arr(199), arr(200), arr(201), arr(202), arr(203), arr(204), arr(205), arr(206), arr(207), arr(208), arr(209), arr(210), arr(211), arr(212), arr(213), arr(214), arr(215), arr(216), arr(217), arr(218), arr(219), arr(220), arr(221), arr(222), arr(223), arr(224), arr(225), arr(226), arr(227), arr(228), arr(229), arr(230), arr(231), arr(232), arr(233), arr(234), arr(235), arr(236), arr(237), arr(238), arr(239), arr(240), arr(241), arr(242), arr(243), arr(244), arr(245), arr(246), arr(247), arr(248), arr(249), arr(250), arr(251), arr(252), arr(2
