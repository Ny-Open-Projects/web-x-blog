# 09-热门学科排名-用户选课-DWD代码-测试清洗入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\09-热门学科排名-用户选课-DWD代码-测试清洗入库_【海量资源尽在 666java.com】.mp4
- 时长 7分50秒（音频 470s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,用户选科这个清洗代码咱们已经编写完成,接下来呢就是测试,咱们来切到开发工具进行测试,这个地方呢,咱们再来过一下逻辑,首先呢是关联维度,关联维度之后呢是获取用户表的原始数据,获取完原始数据呢进行维度的封装,封装之后呢就是咱们实时表需要的数据。
[00:26] 封装完试约表的数据之后呢接下来就是向数据仓库中保存这是咱们的保存的一些代码配置了动态分区保存完成之后呢接下来是查看结果查看收保存成功这个地方查看少了一个from就是刚才应该是粘的时候把这个单次给粘掉了查看之后呢咱们最终是关闭资源咱们来运行测试来看咱们的代码是否好使走起
[00:57] 这里呢编译需要一定的时间咱们呢等待它编译然后进行一个计算这里还在编译中好现在已经开始执行了这个地方执行需要的一个时间这个刚要说执行需要的一个时间它就报了一个错这个地方说musturlmustbeset说咱们没有设置url那没有设置url这个地方只可能会是一个原因
[01:37] 咱们就是这个地方忘记改了在集群模式下如果你是配置了集群模式然后在单机启动就是在开发工具中启动它就会报这个错咱们呢改成为咱们是什么呀开发工具启动就行了这个地方把注射给注料或者呢把这个变量改成false就行了好咱们接着运行就是启动的时候在开发工具中启动一定要确定它是被注射料的或者是呢它是false但是你在打包放到集群中
[02:09] 使用的时候这个地方一定要把这个给注射给放开好这个地方已经在执行了咱们等待它执行完成这个计算不知道需要多长时间咱们稍微暂停一下好咱们继续这里已经将结果输出出来就说明了咱们整个计算已经完成这个时候咱们可以来到HUE上再次确认一下咱们的结果咱们来HUE
[02:43] 咱们是用户选客的试试表就是这张表点击simple这个地方刷一下看有没有数据这个地方显示还没有数据咱们看哪个地方出错了再刷一下有可能是HUE还没有读到呢果然咱们又多次刷新了这个数据就出来了咱们分了ID关联成功咱们时间维度为ID关联成功OK分区年月日也是正确的
[03:18] 这个地方测试完成之后咱们代码没有问题但是还要多说一点就是在咱们开发过程中这个地方咱们过滤了什么咱们过滤了日期但是在咱们开发过程中测试的时候后面进行数据统计的时候你只有一天的数据很显眼这个地方是不太合理的因为你只有一天的数据你去测试你就要不停的跑这个代码也就是为了咱们方便测试咱们
[03:46] 是要把这个日期呢过滤给取消掉在咱们生产环境这个代码是正确的但是在咱们现在开发测试为了方便后面咱们的统计分析这个呢咱们把这个日期给过滤给关掉日期给过滤给关掉呢咱们这里就是清洗所有数据也就是说原始数据有多少我就清洗多少咱们在采集的时候也没有采集特别多所以说这个地方清洗呢
[04:16] 也清洗出来不会特别多咱们呢再次执行一下代码让它呢数据库里边多一点就咱们数据仓库中多一点这个时候呢咱们可以查一下咱们现在这个数据仓库中这张表有多少条数据这个地方可以把原来查的这个给删掉slot星form这个地方来个底然后呢这个地方呢就不是星了咱们要统计谁啊要统计现在有多少条数据走起
[04:51] 咱们看这里面执行完没又报错了这个地方咱们看哪报的错get这个地方报了一个错也就是说咱们生成的一个数据呢可能是有一点脏数据脏数据呢造成什么呀课程分类ID获取不到咱们这个程序就报错了为了保证它这个完整性呢咱们这个地方加一个try开始这里呢try这是咱们的获取代码让它呢
[05:25] 在这里边再次进行一个复制上面这个变量就不能是VL的需要改成V2也就可以再次复制这里呢咱们catch一下catch到谁呀catch咱们的变量这里呢casecase完之后这就是咱们咱们的最终的一个可能报的一个异常可能报的一个异常这里呢你可以处理异常其实你还不管的一个异常因为呢咱们是生产的数据
[05:56] 他这个数据呢就是说可能会有这个ID不存在的情况所以说咱们这个地方呢就是不管他就行再次运行这里呢来看这是跑完没他家是有52条数据等咱们这里清洗所有的数据清洗完成之后咱们再来看咱们清洗过的数据有多少这里呢是以12月11月11号为为那个
[06:24] 基础日期怎么进行清洗呢就是这上面这个日期这里呢咱们现在没有过滤任何日期清洗的时候这个结果就会多一点这里还在计算咱们呢还稍微暂停一下因为不知道它要跑多久好咱们继续这里呢它已经计算完成程序跑完之后呢咱们就来咱们的HUE来查看一下咱们现在这个数据是有多少咱们来运行程序
[06:55] 这个地方它数据量已经多的情况下它这个执行呢可能就会慢一点咱们稍微等待一下这个地方是有3958条数据虽然说这个数据还不算多但是呢对于咱们统计统计分析来说它已经有了不同日期的一个数据咱们后边报表展示的时候就可以生成咱们的相对应的报表好咱们切回温暖这里呢咱们通过代码的编写
[07:27] 通过咱们的清洗以及代码的编写,最终咱们也测试完成。
[07:33] 咱们用户选客这个数据清洗就到这里,通过学习咱们需要将原始数据清洗到咱们事实表中,最终为咱们后面的统计分析提供了基础数据。
[07:47] 好,咱们视频就到这里。

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
- 代码中 `Spark.sql` 的 SQL 语句被高亮显示，用于从 `data_course.learning_course_source` 表中查询数据。
- 代码片段：
```scala
Spark.sql("SELECT * FROM data_course.learning_course_source WHERE from_unixtime(choose_time, 'yyyy-MM-dd') = '${date_info}'")
```

画面 3:
- 代码中 `Spark.conf.set` 设置了 Hive 动态分区模式。
- 代码片段：
```scala
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")
```

画面 4:
- IDE 的 Run 窗口显示程序成功运行，耗时 16 秒。
- 日志显示：`Build completed successfully in 16 s 227 ms`

画面 5:
- IDE 显示 `application.properties` 文件内容。
- 代码片段：
```properties
# Spark 配置
Spark.sql.adaptive.enabled=true
Spark.sql.adaptive.coalescePartitions.enabled=true
```

画面 6:
- HUE 界面显示 Hive 数据库 `data_course` 中的表 `learning_course_dim` 和 `learning_course_fact`。
- 表 `learning_course_dim` 的部分数据列：`course_dim_id`, `course_id`, `user_id`, `time_id`, `status`, `years`, `months`, `days`。

画面 7:
- IDE 显示 `application.properties` 文件内容。
- 代码片段：
```properties
# Spark 配置
Spark.sql.adaptive.enabled=true
Spark.sql.adaptive.coalescePartitions.enabled=true
```

画面 8:
- 代码中 `Spark.sql` 的 SQL 语句被高亮显示，用于从 `data_course.learning_course_source` 表中查询数据。
- 代码片段：
```scala
val learnSource = Spark.sql(s"SELECT * from data_course.learning_course_source WHERE from_unixtime(choose_time, 'yyyy-MM-dd') = '${date_info}'")
```

画面 9:
- IDE 的 Run 窗口显示程序运行失败，抛出 `NoSuchElementException: None.get` 异常。
- 异常堆栈信息：
```scala
Exception in Thread "main" java.util.NoSuchElementException: None.get
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
Exception in Thread "main" java.util.NoSuchElementException: None.get
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

