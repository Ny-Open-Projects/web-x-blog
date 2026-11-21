# 画面线理解：25-热门学科排名-统计分析-销售额-周-测试入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\25-热门学科排名-统计分析-销售额-周-测试入库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:37, 00:44, 00:49, 00:55, 01:04, 01:26, 01:37, 01:44, 01:49, 01:55, 02:06, 02:17, 02:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:29:29

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
import org.apache.spark.sql.SparkSession

object SubjectSalesByWeekBiz {
  // spark session
  val spark: SparkSession = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)

  def main(args: Array[String]): Unit = {
    import spark.implicits._

    // 1. 获取三角形的三个边，判断是否能构成三角形
    val date_info = args(0)
    val weeks = getWeeksRelativelyInterval(date_info).split(regex = "\\n")
    val current = weeks(0).split(regex = "\\t")
    val last = weeks(1).split(regex = "\\t")

    // 2. 获取上周和本周的日期
    // 3. 获取上周和本周的销售数据
    subjectMyAmountSql(spark, current, last).createOrReplaceTempView(viewName = "sales_biz_top")
  }
}
```

画面 2:
```text
using Spark's default logic profile: org/apache/spark/log4j-defaults.properties
10/11/28 18:06:28 WARN NativeCodeLoader: Unable to load native hadoop library for your platform. Using built-in Java classes where applicable
10/11/28 18:06:28 INFO SecurityManager: Changing view acls to: hpc
10/11/28 18:06:28 INFO SecurityManager: Changing modify acls to: hpc
10/11/28 18:06:28 INFO SecurityManager: SecurityManager: authentication disabled; users with view permissions: Set(hpc) groups with view permissions: Set()
10/11/28 18:06:28 INFO BlockManagerMaster: BlockManagerMasterEndpoint using org.apache.spark.storage.DefaultTopologyMapper for getting topology information
10/11/28 18:06:28 INFO BlockManagerMasterEndpoint: Using org.apache.spark.storage.DefaultTopologyMapper for getting topology information
10/11/28 18:06:28 INFO MemoryStore: MemoryStore started with capacity 1073741824 bytes
10/11/28 18:06:28 INFO SparkEnv: Registering OutputCommitCoordinator
10/11/28 18:06:28 INFO SparkEnv: Registering OutputCommitCoordinator on port 4040.
```

画面 3:
```text
10/11/28 18:06:31 INFO ObjectStore: ObjectStore, initialize called
10/11/28 18:06:31 INFO ObjectStore: integral_jdo_pukdown_unmmap - will be ignored
10/11/28 18:06:31 INFO ObjectStore: property.cache.level.unmmap - will be ignored
10/11/28 18:06:34 INFO ObjectStore: Setting Metastore object pin classes with hive.metastore.cache.pinototypes=Table,StorageDescriptor,SerializeInfo,Partition,Database,Type,FieldSchema
10/11/28 18:06:34 INFO ObjectStore: The class "org.apache.hadoop.hive.metastore.model.MTable" is tagged as "embedded-only" so does not have its own datastore table.
10/11/28 18:06:34 INFO ObjectStore: The class "org.apache.hadoop.hive.metastore.model.MFieldSchema" is tagged as "embedded-only" so does not have its own datastore table.
10/11/28 18:06:35 INFO ObjectStore: Reading in results for query "org.apache.hadoop.hive.metastore.model.MTable" since the connection used is closing
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
