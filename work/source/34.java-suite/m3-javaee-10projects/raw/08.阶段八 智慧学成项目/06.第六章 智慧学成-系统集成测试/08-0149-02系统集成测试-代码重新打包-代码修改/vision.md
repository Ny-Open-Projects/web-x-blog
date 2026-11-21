# 画面线理解：02系统集成测试-代码重新打包-代码修改

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\02系统集成测试-代码重新打包-代码修改_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:22, 03:06, 04:46, 06:07, 06:44, 07:22, 08:05, 08:36, 09:10, 09:44, 10:24, 10:48, 11:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:09:40

1) 这一组画面整体在讲什么（一句话）：
演示如何在课程项目中进行代码重构、打包，并配置NIFI任务调度以实现系统集成测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“6 系统集成测试”章节，学习目标包括理解集成测试目的、能够完成集成测试、能够在业务报表系统上展示测试结果。正文介绍集成测试主要模块：调度分析、实时分析、即刻时间，并说明代码修改主要以课程分析（离线）和实时分析为例进行演示。
画面2：展示IDE中“CourseInProcessToFact”类的代码，其中包含Spark SQL语句和数据处理逻辑。同时显示NIFI的“Configure Processor”窗口，配置了Command Path为“/opt/script/course_visit.sh”，Command Arguments为“$BinowToNumber($minua(84400000))format(yyyy-MM-dd)”，并设置Working Directory为“/opt/nifi/script”。
画面3：展示NIFI的“Configure Processor”窗口，配置了Command Arguments为“$BinowToNumber($minua(84400000))format(yyyy-MM-dd)”，Command Path为“/opt/script/course_visit.sh”，Working Directory为“/opt/nifi/script”，并设置Max Attribute Length为“256”。
画面4：展示IDE中“InstantQueryStepToFlow”类的代码，包含SparkSession初始化、日期参数设置、数据源读取和写入逻辑。
画面5：展示IDE中“CourseBuyToFact”类的代码，包含Spark SQL语句和数据处理逻辑，其中使用了“course_buy”表的数据。
画面6：展示IDE中“CourseBuyProcessByBiz.scala”类的代码，包含Spark SQL语句和数据处理逻辑，其中使用了“course_buy”表的数据。
画面7：展示IDE中“CourseBuyProcessToDW.scala”类的代码，包含Spark SQL语句和数据处理逻辑，其中使用了“course_buy”表的数据。
画面8：展示IDE中“UserLearnSourceToFact”类的代码，包含Spark SQL语句和数据处理逻辑，其中使用了“learning_course”表的数据。
画面9：展示IDE中“SubjectSalesVolumeByMonthBiz.scala”类的代码，包含Spark SQL语句和数据处理逻辑，其中使用了“sales_volume”表的数据。
画面10：展示IDE中“SubjectLearnNumByWeekBiz.scala”类的代码，包含Spark SQL语句和数据处理逻辑，其中使用了“learn”表的数据。
画面11：展示IDE中“VisitSourceToFact.scala”类的代码，包含Spark SQL语句和数据处理逻辑，其中使用了“visit”表的数据。
画面12：展示IDE中“VisitSourceToFact”类的代码，包含Spark SQL语句和数据处理逻辑，其中使用了“visit”表的数据。
画面13：展示IDE中“xc-analysis”项目的Maven插件面板，显示了“package”、“verify”、“install”等生命周期阶段。
画面14：展示课程文档“6 系统集成测试”章节，说明打包完成后将新的jar包上传到NIFI容器中，配置NIFI任务调度策略。同时展示NIFI的“Configure Scheduler”窗口，设置“Scheduling Strategy”为“Timer driven”，“Run Schedule”为“6000 sec”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
代码：
val spark: SparkSession = ETLEnvironment.getSparkSession(this.getClass.getSimpleName, _sTableName = null)
val date_info = args(0)
val learnSource = sc.textFile(path = s"/user/hive/external/data_course/learning_course_online_source/${date_info}")
val learnSourceDF = learnSource.map(x => {
  val x = x.split("\t")
  val course_id = x(0).toLong
  val user_id = x(1).toLong
  val course_name = x(2)
  val course_price = x(3).toDouble
  val course_type = x(4)
  val course_time = x(5).toLong
  val course_status = x(6)
  val course_create_time = x(7)
  val course_update_time = x(8)
  val course_delete_time = x(9)
  val course_source = x(10)
  val course_source_id = x(11)
  val course_source_type = x(12)
  val course_source_name = x(13)
  val course_source_url = x(14)
  val course_source_desc = x(15)
  val course_source_tag = x(16)
  val course_source_status = x(17)
  val course_source_create_time = x(18)
  val course_source_update_time = x(19)
  val course_source_delete_time = x(20)
  val course_source_source = x(21)
  val course_source_source_id = x(22)
  val course_source_source_type = x(23)
  val course_source_source_name = x(24)
  val course_source_source_url = x(25)
  val course_source_source_desc = x(26)
  val course_source_source_tag = x(27)
  val course_source_source_status = x(28)
  val course_source_source_create_time = x(29)
  val course_source_source_update_time = x(30)
  val course_source_source_delete_time = x(31)
  val course_source_source_source = x(32)
  val course_source_source_source_id = x(33)
  val course_source_source_source_type = x(34)
  val course_source_source_source_name = x(35)
  val course_source_source_source_url = x(36)
  val course_source_source_source_desc = x(37)
  val course_source_source_source_tag = x(38)
  val course_source_source_source_status = x(39)
  val course_source_source_source_create_time = x(40)
  val course_source_source_source_update_time = x(41)
  val course_source_source_source_delete_time = x(42)
  val course_source_source_source_source = x(43)
  val course_source_source_source_source_id = x(44)
  val course_source_source_source_source_type = x(45)
  val course_source_source_source_source_name = x(46)
  val course_source_source_source_source_url = x(47)
  val course_source_source_source_source_desc = x(48)
  val course_source_source_source_source_tag = x(49)
  val course_source_source_source_source_status = x(50)
  val course_source_source_source_source_create_time = x(51)
  val course_source_source_source_source_update_time = x(52)
  val course_source_source_source_source_delete_time = x(53)
  val course_source_source_source_source_source = x(54)
  val course_source_source_source_source_source_id = x(55)
  val course_source_source_source_source_source_type = x(56)
  val course_source_source_source_source_source_name = x(57)
  val course_source_source_source_source_source_url = x(58)
  val course_source_source_source_source_source_desc = x(59)
  val course_source_source_source_source_source_tag = x(60)
  val course_source_source_source_source_source_status = x(61)
  val course_source_source_source_source_source_create_time = x(62)
  val course_source_source_source_source_source_update_time = x(63)
  val course_source_source_source_source_source_delete_time = x(64)
  val course_source_source_source_source_source_source = x(65)
  val course_source_source_source_source_source_source_id = x(66)
  val course_source_source_source_source_source_source_type = x(67)
  val course_source_source_source_source_source_source_name = x(68)
  val course_source_source_source_source_source_source_url = x(69)
  val course_source_source_source_source_source_source_desc = x(70)
  val course_source_source_source_source_source_source_tag = x(71)
  val course_source_source_source_source_source_source_status = x(72)
  val course_source_source_source_source_source_source_create_time = x(73)
  val course_source_source_source_source_source_source_update_time = x(74)
  val course_source_source_source_source_source_source_delete_time = x(75)
  val course_source_source_source_source_source_source_source = x(76)
  val course_source_source_source_source_source_source_source_id = x(77)
  val course_source_source_source_source_source_source_source_type = x(78)
  val course_source_source_source_source_source_source_source_name = x(79)
  val course_source_source_source_source_source_source_source_url = x(80)
  val course_source_source_source_source_source_source_source_desc = x(81)
  val course_source_source_source_source_source_source_source_tag = x(82)
  val course_source_source_source_source_source_source_source_status = x(83)
  val course_source_source_source_source_source_source_source_create_time = x(84)
  val course_source_source_source_source_source_source_source_update_time = x(85)
  val course_source
