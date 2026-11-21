# 01系统集成测试-学习目标&概述

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\01系统集成测试-学习目标&概述_【海量资源尽在 666java.com】.mp4
- 时长 5分19秒（音频 320s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来呢,进行系统集成测试的学习。
[00:04] 咱们呢,首先来看学习目标,也就是说通过学习咱们需要掌握的内容。
[00:12] 第一个,理解系统集成测试的目的。
[00:16] 这里呢,咱们做集成测试的主要目的,就是按照企业生产环境的方式进行项目的一个部署。
[00:27] 第二,能够完成系统的集成测试。
[00:31] 做相应的配置了因为咱们之前的测试虽然说也在Netflix上进行一个调度来执行Spark的相关任务但是日期相关的配置都是写死的这里咱们要按照企业的方式就是把日期是按传递的方式进行一个配置日期动态获取来完成咱们系统的基层测试第三
[00:59] 能够在业务报表系统上展示咱们的测试结果衡量咱们系统测试成功的重要的一个标准就是这个结果可以在业务系统上进行展示因为如果你是测试不OK的话这个结果肯定是不会正常的一个出现的以上就是咱们系统集成测试的主要的一个学习目标接下来咱们来概述一下咱们这个集成测试的一个
[01:29] 整个流程咱们呢通过对智慧学成这个项目的一系列学习咱们呢首先是学习了什么是数据仓库什么是ETL然后呢在ETL当中对咱们课程分析首先是课程法案量这个指标进行了一个离线分析这里呢课程法案量是在咱们课程分析这个功能模块中的
[02:01] 课程分析除了课程访问量以外还有咱们的课程购买量以及热门学科排名这三个指标做完成之后咱们是进行的是实时分析实时分析主要是针对今日的课程访问量今日的新增用户量以及今日的购买量这个实时实时分析然后实时保存到Redis中然后进行一个结果的实时展示
[02:29] 实时分析完成之后呢,咱们做的是离线即时查询,这个即时查询呢,主要是针对海量的日志数据,这个日志数据呢,也算是离线的,因为呢,咱们查询的是统计分析的是昨天的,对这个海量的日志进行一个查询,这个查询呢,就是查询这个日志得到咱们想要的这个结果,咱们做统计分析的时候,主要是关联的相关的维度,然后呢,把这个学习时长,
[02:59] 给统计出来通过咱们一系列的学习呢主要是做了以上的这些功能模块虽然说咱们在这个代码的编写过程中已经做了相关的测试也在咱们的Netfile上做了相关的调度但是呢这个日期代码中的日期呢都是写死的咱们可以切到开发工具来切换到开发工具中来看一下这里呢咱们获取日期处理日期
[03:30] 这些呢都是现在都是写死的这些写死的日期在咱们生产环境肯定是不允许的因为这个日期如果你写死新的数据过来了它肯定还是你程序在调度执行的时候还是按照这个老的日期来的这个肯定是不OK的咱们还先回文档这里呢咱们就需要对代码进行一个修改把所有的和日期参数相关的
[03:59] 都改成咱们的动态获取这里主要就是课程分析离线分析在一块的以及即时查询在一块的因为实时分析这里的数据是实时进来的它没有日期的一个概念它这个日期就是当天你只要数据来了我就进行处理这个修改完成之后咱们代码还需要进行一个重新的打包重新的上传到内饭容器中上传到内饭容器中之后咱们
[04:29] 还要重新配置咱们的NiFi的一个调度这个重新配置呢其实只用做微调就行了因为咱们之前已经对NiFi呢进行了一个完整的配置配置完成之后呢咱们就是进行相关的测试这个测试衡量这个测试成功的指标呢就是咱们这个结果测试结果能够在业务报表系统上进行一个展示好 视频呢就讲到这里咱们呢这个视频主要
[05:02] 就说了咱们系统集成测试的一个学习目标咱们呢要完成的事是什么以及呢对咱们智慧学乘这个项目的一个功能模块进行一个概述也是咱们集成测试的一个概述好 视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

val learnDS = Spark.sql("select * from ${hiveTableName} where date_info = '${date_info}' and learningCourseOnlineId > 0")
```

画面8代码：
```scala
val date_info = "2019-12-11"
val learnSource = sc.textFile(path + s"/user/Hive/external/data_course/learning_course_online_source/${date_info}")
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

