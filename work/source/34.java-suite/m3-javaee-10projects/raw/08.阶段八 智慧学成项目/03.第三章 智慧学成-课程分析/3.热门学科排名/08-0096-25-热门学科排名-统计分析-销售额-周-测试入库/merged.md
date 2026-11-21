# 25-热门学科排名-统计分析-销售额-周-测试入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\25-热门学科排名-统计分析-销售额-周-测试入库_【海量资源尽在 666java.com】.mp4
- 时长 2分55秒（音频 175s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前边呢,咱们已经根据热门学科排名中的销售量按周统计的修改,得到咱们热门学科排名中销售额的按周统计。
[00:12] 代码呢,咱们已经修改好,接下来呢,就是进行测试,这里呢,直接运行代码即可。
[00:20] 这里呢,还在打包编译中,咱们呢,切到HUE,这是咱们热门学科。
[00:27] 销售额的一个按周统计的一个结果数据表就是咱们APP层的一个数据这里呢现在刷新它还没有数据这里还在刷没有数据是因为呢咱们这里还程序还没有执行完成咱们呢就等待这个程序执行完成来验证这个结果这里呢程序还在执行过程中好程序已经执行完成这是呢9月的按9月咱们来计算
[01:01] 是9月的话是第39周和同月相比因为咱们9月之前已经没有数据了这个的话增幅可以看到都是100%的咱们呢把它改成10月让程序跑着咱们呢来HUE再查看一下结果这里呢刷来验证一下这里呢是按周统计的是39周这里已经有数据了咱们呢把数据改成了10月10月的话这里结果还没有出来
[01:32] 咱们呢等待它10月25号这个结果出来咱们再来演讲一下这里呢程序还在计算过程中咱们稍微等待一下这里呢还在运行运行中好结果呢已经出来这是已经是第43周了是10月25号它计算的是第43周的数据咱们来切到HU一场来刷新一下39 43因为39周的话咱们前面是没有数据的你可以看到这个地方增幅都是百分之百
[02:16] 后面呢咱们是有数据的这个增幅就有正增长还有负增长这个数据呢就是一个很正常的一个数据通过测试呢咱们代码可以得到正确的结果咱们呢热门学科排名中销售额按周统计到这里呢代码的编写以及咱们的测试就算完成了通过学习呢你需要将热门学科热门学科中销售额的统计按周统计呢
[02:45] 保存到咱们的数据仓库中为后面业务抱卷系统提供的一个可使用的基础数据好视频就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark 中编写代码，计算并生成一个按周粒度的销售金额汇总表，并通过 Hue 工具验证数据结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Scala 代码文件 `SubjectSalesByWeekBiz.scala` 的内容，其中定义了 Spark 会话和主函数，用于计算销售数据。代码中包含注释说明了数据处理逻辑。
画面 2: 展示了 Spark 应用程序启动的日志，显示 Spark 版本 2.3.3 启动成功，并注册了各种服务。
画面 3: 展示了 Spark 应用程序继续执行的日志，包括初始化 Hive Metastore 和 ObjectStore，以及读取查询结果。
画面 4: 展示了 Spark 应用程序执行过程中的日志，显示了文件源策略、过滤器和分区剪枝等优化信息。
画面 5: 展示了 Spark 应用程序执行完成后的日志，显示 Spark 上下文已停止，内存管理器已关闭。
画面 6: 展示了 Spark 应用程序执行完成后的结果，显示了计算出的销售数据表，包含课程类别、销售金额、百分比、年份和周数。
画面 7: 展示了 Hue Table Browser 界面，显示了 `subject_amount_week_biz` 表的结构和部分数据，年份为 2019，周数为 39。
画面 8: 展示了 Spark 应用程序启动的日志，显示 Hive Metastore 初始化成功，以及读取了 Hive 配置文件。
画面 9: 展示了 Spark 应用程序执行的日志，显示了获取数据库和表信息的过程，包括 `data_subject` 数据库和 `subject_amount_week_biz` 表。
画面 10: 展示了 Spark 应用程序执行的日志，显示了任务调度器初始化、数据读取和任务提交等信息。
画面 11: 展示了 Spark 应用程序执行完成后的结果，显示了计算出的销售数据表，包含课程类别、销售金额、百分比、年份和周数。
画面 12: 展示了 Hue Table Browser 界面，显示了 `subject_amount_week_biz` 表的结构和部分数据，年份为 2019，周数为 43。
画面 13: 展示了 Hue Table Browser 界面，显示了 `subject_amount_week_biz` 表的结构和部分数据，年份为 2019，周数为 48。
画面 14: 展示了课程 PPT 页面，标题为“3.5.3 销售额”，其中包含“3.5.3.1 周”小节，以及创建外部表 `subject_amount_week_biz` 的 SQL 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
import cn.itcast.xc.entity.SubjectAmountWeekBiz, SubjectSalesByWeekBiz
import cn.itcast.xc.utils.DateUtils.getWeeksNum, getWeeksRelativelyInterval
import cn.itcast.xc.utils.SubjectUtils.createReplaceTempView
import org.apache.Spark.sql.SparkSession

object SubjectSalesByWeekBiz {
  // Spark session
  val Spark: SparkSession = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)

  def main(args: Array[String]): Unit = {
    import Spark.implicits._

    // 1. 获取三角形的三个边，判断是否能构成三角形
    val date_info = args(0)
    val weeks = getWeeksRelativelyInterval(date_info).split(regex = "\\n")
    val current = weeks(0).split(regex = "\\t")
    val last = weeks(1).split(regex = "\\t")

    // 2. 获取上周和本周的日期
    // 3. 获取上周和本周的销售数据
    subjectMyAmountSql(Spark, current, last).createOrReplaceTempView(viewName = "sales_biz_top")
  }
}
```

画面 2:
```text
using Spark's default logic profile: org/apache/Spark/log4j-defaults.properties
10/11/28 18:06:28 WARN NativeCodeLoader: Unable to load native Hadoop library for your platform. Using built-in Java classes where applicable
10/11/28 18:06:28 INFO SecurityManager: Changing view acls to: hpc
10/11/28 18:06:28 INFO SecurityManager: Changing modify acls to: hpc
10/11/28 18:06:28 INFO SecurityManager: SecurityManager: authentication disabled; users with view permissions: Set(hpc) groups with view permissions: Set()
10/11/28 18:06:28 INFO BlockManagerMaster: BlockManagerMasterEndpoint using org.apache.Spark.storage.DefaultTopologyMapper for getting topology information
10/11/28 18:06:28 INFO BlockManagerMasterEndpoint: Using org.apache.Spark.storage.DefaultTopologyMapper for getting topology information
10/11/28 18:06:28 INFO MemoryStore: MemoryStore started with capacity 1073741824 bytes
10/11/28 18:06:28 INFO SparkEnv: Registering OutputCommitCoordinator
10/11/28 18:06:28 INFO SparkEnv: Registering OutputCommitCoordinator on port 4040.
```

画面 3:
```text
10/11/28 18:06:31 INFO ObjectStore: ObjectStore, initialize called
10/11/28 18:06:31 INFO ObjectStore: integral_jdo_pukdown_unmmap - will be ignored
10/11/28 18:06:31 INFO ObjectStore: property.cache.level.unmmap - will be ignored
10/11/28 18:06:34 INFO ObjectStore: Setting Metastore object pin classes with Hive.metastore.cache.pinototypes=Table,StorageDescriptor,SerializeInfo,Partition,Database,Type,FieldSchema
10/11/28 18:06:34 INFO ObjectStore: The class "org.apache.Hadoop.Hive.metastore.model.MTable" is tagged as "embedded-only" so does not have its own datastore table.
10/11/28 18:06:34 INFO ObjectStore: The class "org.apache.Hadoop.Hive.metastore.model.MFieldSchema" is tagged as "embedded-only" so does not have its own datastore table.
10/11/28 18:06:35 INFO ObjectStore: Reading in results for query "org.apache.Hadoop.Hive.metastore.model.MTable" since the connection used is closing
10/11/28 18:06:35 INFO ObjectStore: Initialized ObjectStore
10/11/28 18:06:35 INFO HiveMetastore: Added admin role in metastore
```

画面 4:
```text
10/11/28 18:06:41 INFO FileSourceStrategy: Post-Scan Filters:
10/11/28 18:06:41 INFO FileSourceStrategy: Pushed Filters:
10/11/28 18:06:41 INFO FileSourceStrategy: Pruning directories with (concat_ws('-', year#18, month#15, days#28) > 2019-09-16), (concat_ws('-', year#18, month#15, days#28) < 2019
10/11/28 18:06:41 INFO FileSourceScanExec: Pushed Filters:
10/11/28 18:06:41 INFO ContextCleaner: Cleaned accumulator 8
10/11/28 18:06:41 INFO ContextCleaner: Cleaned accumulator 4
10/11/28 18:06:41 INFO ContextCleaner: Cleaned accumulator 2
10/11/28 18:06:41 INFO ContextCleaner: Cleaned accumulator 18
10/11/28 18:06:41 INFO PrunedInMemoryFileIndex: Selected 2 partitions out of 2, pruned 0.0% partitions.
```

画面 5:
```text
10/11/28 18:06:45 INFO SparkUI: Stopped Spark web UI at http://DESKTOP-LPN84L1:4040
10/11/2

