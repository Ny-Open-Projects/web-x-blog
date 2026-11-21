# 02系统集成测试-代码重新打包-代码修改

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\02系统集成测试-代码重新打包-代码修改_【海量资源尽在 666java.com】.mp4
- 时长 11分24秒（音频 684s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前边已经概述了咱们系统的集生测试,这里系统的集生测试主要目的是能够按照企业的生产环境的方式进行项目的部署并测试。
[00:14] 这里要符合企业的生产环境,首先咱们需要对代码进行一个配置,因为在代码中咱们之前的日期传递都是直接写死的,这个写死的话就是硬编码。
[00:29] 在企业的真正的一个部署过程中日期肯定是动态的一个获取然后根据获取的日期来进行数据的清洗统计分析接下来呢咱们对代码进行重新打包要做的事呢也是把代码修改为使用参数传递的方式来获取这个日期这个代码的重新打包重新打包呢一共是分为三步第一步呢就是对
[00:58] 清洗程序的一个修改清洗程序修改完成之后呢是对统计分析程序修改统计分析程序修改完成之后呢是对Netfile调度进行修改咱们呢文档中是以课程访问为例的这里步骤一和步骤二是咱们在开发工具中进行修改步骤三呢是在Netfile上进行修改但是这个地方呢咱们需要注意一点是Netfile的配置咱们在
[01:26] 原码中已经配置好,现在的调度呢,就是可以直接使用的,这个地方呢,步骤三,咱们了解一下几何,咱们来切到NiFi,进行这个NiFi调度配置的一个参数的一个查看,这里呢,咱们最后做的是及时查询,就以及时查询为例,这里是咱们数据清洗,统计分析的调度程序,这两个呢,是咱们真正的一个调度脚本,就是调度处理器,然后执行咱们的调度脚本,
[01:58] 咱们右键选择config第一个参数呢就是传递的日期咱们可以点击看一下这里呢获取今天的时间就是获取此时此刻的时间就是程序在调度的时候它是什么时间调度的就获取什么时间的那个具体的时间然后呢它减去一个毫秒值这个毫秒值呢就是一天的一个时间得到昨天的时间得到昨天的时间之后呢把它给
[02:27] 隔次化成YYYMM-DD的方式咱们这里即时查询呢它是也是对历史数据进行一个数据的清洗然后呢把它给持续化到HB4和Aleska色彩上面这里呢也是获取昨天的时间相同咱们离线查询也是一样的咱们以看成购买量为例找到它的一个调度这里是统计分析程序的调度咱们呢
[02:57] 真正的调度这个地方有两个,咱们来随机找一个,卡住一个,在这个地方呢,可以看到相同的一个配置,好,咱们来切回文档,这里呢,在代码中,咱们主要是对步骤一和步骤二进行配置,咱们来切到开发工具,咱们还是以咱们最后开发这个先修改,然后呢,再修改咱们前面开发的,
[03:29] 咱们后边开发的这个就是最近开发这个呢是即时查询即时查询然后是实时分析然后是离线分析但是实时分析呢是没有这个时间参数这个概念的咱们呢即时查询修改完成之后直接修改离线分析即可咱们接下来对代码进行修改这里呢这个包下面四上相下挨个修改这个呢是咱们
[03:58] 这个传递的这个原来代码中写死的这个参数这个时间参数在这里进行一个传递接下来呢咱们就把它给修改成程序运行的时候使用参数传递的方式但是这个地方呢有一个问题这个地方是写的是1当时呢咱们在编写这个代码的时候是这样描述的就是说
[04:23] 传递是7的时候呢是第一个参数然后就写了1但是呢咱们这个地方是数组数组在接收数据的时候第一个参数它的索引是谁啊索引是0当时呢就是为了咱们这个好理解是随手写了一个1但是在咱们数组在获取数据的时候一定要注意数组的索引是从0开始的这个修改完成之后呢咱们这个程序就算修改OK了咱们把这行给复制了
[04:54] 接下来呢把它给关了咱们修改第二个这里呢也是那个写死的咱们来使用传递的方式OK这个地方呢代码中过滤这个日期因为是根据你传来的参数然后进行日期的过滤下边这一行呢是查询所有的也就是在咱们测试的时候是查询所有但是在咱们生产环境呢是你传过来的日期是多少然后就过滤到哪一天的好
[05:28] 这个呢修改完成咱们即时查询呢一共就两个程序修改OK之后咱们进行理解分析的代码修改理解分析的话就相对来说比较多了课程访问量课程购买量日文学科排名咱们呢就是防止修改修改的时候不知道哪个已经修改了哪个未修改咱们就自伤向下挨个修改就行这里呢找到咱们的DataInfo
[05:59] 这个地方呢还是咱们就是随手写了这个1让它变成正确的就是使用索引0来进行参数的接收这个地方呢下边是用的这个查询所有的方式获取这个数据进行清洗但是咱们在生产环境你获取所有显然是不合适的咱们呢把上面的这个放开也就是咱们在写代码的时候呢已经考虑到了咱们这个过滤日期的这种情况
[06:27] 把这个代码给放开就行了咱们来检查其他地方有没有和日期相关的这个地方呢只有这一个位置修改完成之后咱们进行下一个的修改这个地方的修改呢它是方便测试不过滤的时间这个呢是直接在circle里边的把下边这个给注释掉把上边这个注释给放开放开之后呢这个地方可以看到它是不是在这写死的它在这里边写死的情况下咱们是不是要改成
[07:00] 参数传递的方式这个地方要是英文的咱们把参数给传过来参数传过来之后下边都是直接保存了就没有和日期相关的了就OK了这个代码的修改就OK接下来是第三个这个也是一样的也是一个在serve中修改下边呢是测试的测试的时候查清所有上边呢是过滤日期的把这个给注料
[07:37] 改成咱们用参数获取的方式OK修改完成接下来呢是人们修改排名的人们修改排名一共是这么多日期的上面的注掉这个呢是他的查询参数把上面的给放开OK修改完成下一个切换掉把写死的参数给注射掉看一下切到位置没有发现然后咱们继续下一个这个
[08:24] 切换掉把原来写死的日期给注释掉好修改完成接下来呢是销售量的注释掉好这个呢修改就OK下一个注释掉OK下一个把这个写死的日期给注释掉把咱们复制的给粘进来OK下一个这个注释掉复制的粘过来
[09:12] 因为咱们这个日期呢都是在开头的也就是说你直接在开头进行一个修改就行这个参数是正确的这个注释掉OK这个呢是确认是OK的咱们进行下一个参数0参数0日期的过滤日期的过滤这个呢咱们批量生产环境的时候它呢是生成大量的一个数据它那个日期呢是随机的咱们在这个
[09:48] SPARK进行计算的时候也使用了filter算子进行过滤咱们这个地方呢生成数据这个过滤就不再做因为咱们在生产环境的时候咱们在测试生产环境的时候咱们采集的时候只有一天的数据实际采集只有一天的数据但是咱们呢也是采用NiFi生产的方式进行一个生产让这个原始数据多一点这个地方呢就不过滤就行了咱们到试试表没有过滤但是呢咱们在
[10:17] 咱们到统计分析程序这个地方是有过滤的也就是前边你这个程序不管你多少数据到我这个地方它就是正常的了所以说呢这个测试的时候你可以选择过滤也可以选择不过滤这个地方呢就不过滤了到此呢咱们这个程序就修改完成了修改完成之后呢咱们需要给代码重新打包这里呢使用mywin先把它clean一下clean完成之后呢
[10:47] 点击package让它打包即可咱们来切回问答这里呢到代码的一个打包咱们呢所有的配置就说明已经配置好了打包呢需要一定的时间这里呢咱们下一个视频进行代码的一个上传把这个炸不是代码把这个jar 包上传到内饭人去就是对大包的一个上传然后呢咱们对咱们这个任务调度这个程序呢
[11:18] 进行一个相关的讲解这个视频呢就到这里好视频到此为止

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
val Spark: SparkSession = ETLEnvironment.getSparkSession(this.getClass.getSimpleName, _sTableName = null)
val date_info = args(0)
val learnSource = sc.textFile(path = s"/user/Hive/external/data_course/learning_course_online_source/${date_info}")
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

