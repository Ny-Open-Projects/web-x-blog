# 画面线理解：01系统集成测试-学习目标&概述

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\01系统集成测试-学习目标&概述_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 00:59, 01:39, 02:19, 02:59, 03:22, 03:26, 03:30, 03:33, 03:38, 03:39, 03:51, 04:19, 04:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:08:40

1) 这一组画面整体在讲什么（一句话）：
讲解系统集成测试中代码重新打包的步骤，重点演示如何修改Spark程序中的日期参数。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT，标题为“6 系统集成测试”，学习目标包括理解测试目的、能够完成测试、能够在业务系统上展示结果。正文说明集成测试覆盖课程分析、实时分析、即时查询等模块。
画面2：同画面1，光标在“实时分析”后。
画面3：同画面1，光标在“实时分析”后。
画面4：同画面1，光标在“实时分析”后。
画面5：同画面1，光标在“实时分析”后。
画面6：切换到IDEA编辑器，显示Scala代码文件`InstantQueryStep1Online.scala`，代码中定义了HBase表名、Hive表名、日期参数`val date_info = "2019-12-12"`，并创建了SparkSession和DataFrame。
画面7：同画面6，光标在`val date_info = "2019-12-12"`行。
画面8：同画面6，光标在`val date_info = "2019-12-11"`行。
画面9：同画面6，光标在`val date_info = "2019-12-11"`行。
画面10：同画面6，光标在`val date_info = "2019-12-11"`行。
画面11：同画面6，光标在`val date_info = "2019-12-11"`行。
画面12：切换回PPT，光标在“实时分析”后。
画面13：同画面12，光标在“实时分析”后。
画面14：同画面12，光标在“实时分析”后。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6代码：
```scala
val hbaseTableName = "learning_online_detail"
val hbaseColumnNames = "learning_online_detail"

// 自动创建表
hbaseUtils.createTable(hbaseTableName, hbaseColumnNames)
val jobConf = hbaseUtils.getJobConf(hbaseTableName)

// 表
val hiveTableName = "data_course.learning_course_online_dat"

val date_info = "2019-12-12"

val learnDS = spark.sql("select * from ${hiveTableName} where date_info = '${date_info}' and learningCourseOnlineId > 0")
```

画面8代码：
```scala
val date_info = "2019-12-11"
val learnSource = sc.textFile(path + s"/user/hive/external/data_course/learning_course_online_source/${date_info}")
val learnSourceRDD = learnSource.map(_ split("\t")).map(arr => {
  learnOnlineId = arr(0).toLong,
  arr(1).toLong,
  arr(2).toLong,
  arr(3).toLong,
  arr(4).toLong,
  arr(5).toLong,
  arr(6).toLong,
  arr(7).toLong,
  arr(8).toLong,
  arr(9).toLong,
  arr(10).toLong,
  arr(11).toLong,
  arr(12).toLong,
  arr(13).toLong,
  arr(14).toLong,
  arr(15).toLong,
  arr(16).toLong,
  arr(17).toLong,
  arr(18).toLong,
  arr(19).toLong,
  arr(20).toLong,
  arr(21).toLong,
  arr(22).toLong,
  arr(23).toLong,
  arr(24).toLong,
  arr(25).toLong,
  arr(26).toLong,
  arr(27).toLong,
  arr(28).toLong,
  arr(29).toLong,
  arr(30).toLong,
  arr(31).toLong,
  arr(32).toLong,
  arr(33).toLong,
  arr(34).toLong,
  arr(35).toLong,
  arr(36).toLong,
  arr(37).toLong,
  arr(38).toLong,
  arr(39).toLong,
  arr(40).toLong,
  arr(41).toLong,
  arr(42).toLong,
  arr(43).toLong,
  arr(44).toLong,
  arr(45).toLong,
  arr(46).toLong,
  arr(47).toLong,
  arr(48).toLong,
  arr(49).toLong,
  arr(50).toLong,
  arr(51).toLong,
  arr(52).toLong,
  arr(53).toLong,
  arr(54).toLong,
  arr(55).toLong,
  arr(56).toLong,
  arr(57).toLong,
  arr(58).toLong,
  arr(59).toLong,
  arr(60).toLong,
  arr(61).toLong,
  arr(62).toLong,
  arr(63).toLong,
  arr(64).toLong,
  arr(65).toLong,
  arr(66).toLong,
  arr(67).toLong,
  arr(68).toLong,
  arr(69).toLong,
  arr(70).toLong,
  arr(71).toLong,
  arr(72).toLong,
  arr(73).toLong,
  arr(74).toLong,
  arr(75).toLong,
  arr(76).toLong,
  arr(77).toLong,
  arr(78).toLong,
  arr(79).toLong,
  arr(80).toLong,
  arr(81).toLong,
  arr(82).toLong,
  arr(83).toLong,
  arr(84).toLong,
  arr(85).toLong,
  arr(86).toLong,
  arr(87).toLong,
  arr(88).toLong,
  arr(89).toLong,
  arr(90).toLong,
  arr(91).toLong,
  arr(92).toLong,
  arr(93).toLong,
  arr(94).toLong,
  arr(95).toLong,
  arr(96).toLong,
  arr(97).toLong,
  arr(98).toLong,
  arr(99).toLong,
  arr(100).toLong,
  arr(101).toLong,
  arr(102).toLong,
  arr(103).toLong,
  arr(104).toLong,
  arr(105).toLong,
  arr(106).toLong,
  arr(107).toLong,
  arr(108).toLong,
  arr(109).toLong,
  arr(110).toLong,
  arr(111).toLong,
  arr(112).toLong,
  arr(113).toLong,
  arr(114).toLong,
  arr(115).toLong,
  arr(116).toLong,
  arr(117).toLong,
  arr(118).toLong,
  arr(119).toLong,
  arr(120).toLong,
  arr(121).toLong,
  arr(122).toLong,
  arr(123).toLong,
  arr(124).toLong,
  arr(125).toLong,
  arr(126).toLong,
  arr(127).toLong,
  arr(128).toLong,
  arr(129).toLong,
  arr(130).toLong,
  arr(131).toLong,
  arr(132).toLong,
  arr(133).toLong,
  arr(134).toLong,
  arr(135).toLong,
  arr(136).toLong,
  arr(137).toLong,
  arr(138).toLong,
  arr(139).toLong,
  arr(140).toLong,
  arr(141).toLong,
  arr(142).toLong,
  arr(143).toLong,
  arr(144).toLong,
  arr(145).toLong,
  arr(146).toLong,
  arr(147).toLong,
