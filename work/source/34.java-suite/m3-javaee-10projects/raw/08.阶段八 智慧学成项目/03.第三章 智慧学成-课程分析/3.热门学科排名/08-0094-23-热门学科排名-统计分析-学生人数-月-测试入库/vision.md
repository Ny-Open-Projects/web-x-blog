# 画面线理解：23-热门学科排名-统计分析-学生人数-月-测试入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\23-热门学科排名-统计分析-学生人数-月-测试入库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:23, 00:29, 00:51, 01:22, 01:33, 01:38, 01:44, 01:49, 01:57, 02:20, 02:29, 02:54, 03:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:27:21

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark 中编写 Scala 代码，读取数据、进行聚合计算，并将结果写入 Hive 表，最后通过 Hue 工具验证数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Scala 代码中定义 SparkSession 和处理日期的逻辑，其中包含注释“// 1. 获取当月的时间区间，例：1号至18号”。
画面 2: 在代码中选中 `subjectLearnMonth`，右键弹出菜单，选择“Run 'SubjectLearnNumByMonth...'”以执行程序。
画面 3: 显示了 Spark 启动日志，包括成功绑定端口、注册 BlockManager、加载 Hive 配置文件等信息。
画面 4: 展示了 Spark SQL 的执行计划（Execution Plan），显示了多个 Catalyst Tree 的节点，如 `TreedNodeApply`、`TreedNodeTransform` 等。
画面 5: 展示了 Spark SQL 代码，包含 `spark.conf.set` 设置动态分区模式、`learnDS.repartition` 设置分区数、`spark.sql` 执行 SQL 语句并 `spark.close` 关闭连接。
画面 6: 显示了 Spark 启动日志，包括加载 Hive 配置、初始化 SparkContext、设置安全权限等。
画面 7: 显示了 Spark 启动日志，包括加载 Hive 配置、初始化 Hive Metastore、注册 StateStoreCoordinator 等。
画面 8: 显示了 Spark 启动日志，包括初始化 Hive Metastore、加载表信息、获取数据库和表的元数据。
画面 9: 展示了 Hue 的 Table Browser 页面，显示了 `data_subject` 数据库下的多个表。
画面 10: 在 Hue 的终端中执行了 SQL 命令 `show tables`，并显示了结果。
画面 11: 在 Hue 的 Table Browser 页面，点击了 `subject_user_month_biz` 表的“Sample”标签页。
画面 12: 在 Hue 的 Table Browser 页面，显示了 `subject_user_month_biz` 表的样本数据，包含课程类别、用户数、用户占比等字段。
画面 13: 展示了 PDF 文档中的“3.5.2.2.2 APP层数据结构”部分，包含创建外部表的 SQL 语句。
画面 14: 与画面 13 相同，PDF 文档中的“3.5.2.2.2 APP层数据结构”部分，包含创建外部表的 SQL 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
import cn.licat.cc.entity.SubjectLearnUserMonthBiz
import cn.licat.cc.utils.DateUtils.{getMonthNow, getMonthRelativelyInterval}
import org.apache.spark.sql.SparkSession

// 获取当月用户人数
object SubjectLearnNumByMonthBiz {
  // Spark session
  val spark: SparkSession = EtlEnvironment.getSparkSession(this.getClass.getSimpleName)
  // 1. 获取当月的时间区间，例：1号至18号
  def main(args: Array[String]): Unit = {
    import spark.implicits._
    val date_info = "2019-11-11"
    val months = getMonthRelativelyInterval(date_info).split(regex = "\\s")
    val current = months(0).split(regex = "\\t")
    val last = months(1).split(regex = "\\t")
    println(months.mkString(";"))
    // 2. 计算当月用户数
    // 3. 计算上月用户数
    // 4. 计算当月用户占比
    // 5. 计算上月用户占比
    // 6. 计算当月用户数
    // 7. 计算上月用户数
    subjectLearnMonth(spark, current, last).createReplaceView(viewName = "learn_biz_month_biz")
  }
}
```

画面 2:
```scala
subjectLearnMonth(spark, current, last)
```

画面 3:
```text
15/11/28 17:18:53 INFO SparkEnv: Registering OutputCommitCoordinator
10/11/28 17:18:53 INFO Utils: Successfully started service SparkUI at http://localhost:4040
10/11/28 17:18:53 INFO Executor: Starting executor driver on host localhost
10/11/28 17:18:53 INFO NettyBlockTransferService: Server created on DESKTOP-LPM4L8:53339
10/11/28 17:18:53 INFO BlockManager: BlockManager created with 1807.5 MB RAM, BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMasterEndpoint: Registered BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: Registered BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 53339, None)
10/11/28 17:18:53 INFO BlockManagerMaster: BlockManagerId(driver, DESKTOP-LPM4L8, 533
