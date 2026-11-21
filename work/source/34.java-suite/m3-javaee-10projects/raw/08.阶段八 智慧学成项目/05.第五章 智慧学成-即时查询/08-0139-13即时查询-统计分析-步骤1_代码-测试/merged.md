# 13即时查询-统计分析-步骤1：代码-测试

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\13即时查询-统计分析-步骤1：代码-测试_【海量资源尽在 666java.com】.mp4
- 时长 3分51秒（音频 231s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前边已经编写了即时查询步骤一的代码代码的功能主要就是关联相关维度以及统计学习时长这里咱们写了一个比较长的circle这个circle还没有进行验证咱们直接运行代码这里运行代码一方面是验证circle另一方面是验证咱们的一个结果程序不报错就说明程序的逻辑
[00:29] 是没有问题的,包括我们这个src是没有问题的另外一个验证的就是验证结果结果正确说明功能才算完整这里呢程序正在运行中,咱们等待它运行结束可以看到这里呢已经运行完成根据这个结果来看的话和内幕相关的都没有结果这个是正常的因为呢咱们在前端买点的时候这些各种ID就是课程ID
[01:04] UseID以及咱们的SessionID这些呢都是随机生成的因为咱们学生在线那个web前端是一个静态页面没有真实的数据所以说这个地方拿数据的时候拿不到它是正确的但是DataInfo的话这个地方可以看到它是51914这个很明显是不对的咱们呢这个地方现在的话咱们这个时间是多少是201912-11
[01:34] 但是这个出现了这么大的一个年份主要的原因呢就是咱们在咱们这个日期格式化这个地方这个地方特要求的是时间说但是呢咱们那个learn time钱财获取的时候它是毫秒值的这个地方呢需要除以1000咱们来重新运行这个地方呢咱们是使用的是overwrite也就是重新运行之后呢它会把原来的结果给覆盖掉原来结果覆盖但是
[02:06] 还会有一个问题因为咱们这个地方呢DataInfo进行覆盖的时候它一个很大的问题就是咱们新产生的时间咱们新产生的时间是正确的时间原来的时间是错误的时间咱们来HUE刷新一下错误的时间呢是不会被覆盖掉的这里已经出现了部分数据这是正确的时间刷新一下看一下这还是错误的结果
[02:42] 这些错误的结果呢咱们等会儿使用HOE可以手动把它给删除这里正确的结果因为咱们这个地方随机生成的时间呢并没有对日期进行一个特别的一个过滤它呢生成的时间这就有12和13的这个呢是正常的咱们到目前为止呢咱们这个结果就OK了但是由于前边咱们
[03:12] 没有把这个时间圈给处理它呢出现了部分就是垃圾数据这个呢咱们可以直接把它分区给删掉就行了把这个错误的分区给删掉删掉完成之后呢删掉完成之后咱们数据仓库中有的数据就是正常的数据好测试呢就到这里咱们呢切个切回温的咱们这里呢中间表的一个代码的一个编写
[03:44] 而且这里测试也是OK的视频就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  val Spark: SparkSession = ELEnvironment.getSparkSession(this.getClass.getSimpleName, eTableName = null)
  // 2. 获取 SparkContext
  val sc = Spark.sparkContext
  // 3. 读取日期参数
  val date_info = "2019-12-11"
  val learnSource = sc.textFile(path = s"/user/Hive/external/data_course/learning_course_online_source/${date_info}")
  val learnSourceRDD = learnSource.map(split regex = ".*", arr = {
    UserLearnOnline(arr(0), arr(1), arr(2), arr(3), arr(4), arr(5), arr(6), arr(7), arr(8), arr(9), arr(10), arr(11), arr(12), arr(13), arr(14), arr(15), arr(16), arr(17), arr(18), arr(19), arr(20), arr(21), arr(22), arr(23), arr(24), arr(25), arr(26), arr(27), arr(28), arr(29), arr(30), arr(31), arr(32), arr(33), arr(34), arr(35), arr(36), arr(37), arr(38), arr(39), arr(40), arr(41), arr(42), arr(43), arr(44), arr(45), arr(46), arr(47), arr(48), arr(49), arr(50), arr(51), arr(52), arr(53), arr(54), arr(55), arr(56), arr(57), arr(58), arr(59), arr(60), arr(61), arr(62), arr(63), arr(64), arr(65), arr(66), arr(67), arr(68), arr(69), arr(70), arr(71), arr(72), arr(73), arr(74), arr(75), arr(76), arr(77), arr(78), arr(79), arr(80), arr(81), arr(82), arr(83), arr(84), arr(85), arr(86), arr(87), arr(88), arr(89), arr(90), arr(91), arr(92), arr(93), arr(94), arr(95), arr(96), arr(97), arr(98), arr(99), arr(100), arr(101), arr(102), arr(103), arr(104), arr(105), arr(106), arr(107), arr(108), arr(109), arr(110), arr(111), arr(112), arr(113), arr(114), arr(115), arr(116), arr(117), arr(118), arr(119), arr(120), arr(121), arr(122), arr(123), arr(124), arr(125), arr(126), arr(127), arr(128), arr(129), arr(130), arr(131), arr(132), arr(133), arr(134), arr(135), arr(136), arr(137), arr(138), arr(139), arr(140), arr(141), arr(142), arr(143), arr(144), arr(145), arr(146), arr(147), arr(148), arr(149), arr(150), arr(151), arr(152), arr(153), arr(154), arr(155), arr(156), arr(157), arr(158), arr(159), arr(160), arr(161), arr(162), arr(163), arr(164), arr(165), arr(166), arr(167), arr(168), arr(169), arr(170), arr(171), arr(172), arr(173), arr(174), arr(175), arr(176), arr(177), arr(178), arr(179), arr(180), arr(181), arr(182), arr(183), arr(184), arr(185), arr(186), arr(187), arr(188), arr(189), arr(190), arr(191), arr(192), arr(193), arr(194), arr(195), arr(196), arr(197), arr(198), arr(199), arr(200), arr(201), arr(202), arr(203), arr(204), arr(205), arr(206), arr(207), arr(208), arr(209), arr(210), arr(211), arr(212), arr(213), arr(214), arr(215), arr(216), arr(217), arr(218), arr(219), arr(220), arr(221), arr(222), arr(223), arr(224), arr(225), arr(226), arr(227), arr(228), arr(229), arr(230), arr(231), arr(232), arr(233), arr(234), arr(235), arr(236), arr(237), arr(238), arr(239), arr(240), arr(241), arr(242), arr(243), arr(244), arr(245), arr(246), arr(247), arr(248), arr(249), arr(250), arr(251), arr(252), arr(2

