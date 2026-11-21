# 23-热门学科排名-统计分析-学生人数-月-测试入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\23-热门学科排名-统计分析-学生人数-月-测试入库_【海量资源尽在 666java.com】.mp4
- 时长 3分46秒（音频 226s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 热门学科排名学生人数的统计咱们呢前边是基于周把这个统计分析呢修改成月咱们呢也排查过了这个代码没有发现问题就是在排查过程中没有发现问题接下来呢咱们就是对代码的进行测试进行测试来校验这个结果就是看这个结果是否有问题咱们呢来运行代码看咱们这个代码的流程是否有问题这里呢代码运行中
[00:31] 咱们可以看到这里11月咱们是输的是11号这个地方呢是11月1号到10号的上个月呢就是10号1号到10月10号的这个呢区间是正确的因为咱们是离线分析是分析前天的数据你传这个当天的数据它是取前天这个是对的这个呢这里报错了咱们来看报什么错week over year这个地方的话咱们就是在排查的时候就
[01:02] 排查的不够彻底是不是这个变量忘记修改了m o n把它也给修改成月这个呢就是咱们业务表的一个对应的一个实体就是咱们最终是要保存到咱们按月统计的这个业务表学生人数按月统计的业务表但是呢这个地方排查的时候就忘记了咱们还是使用的按周统计的这个地方修改完成之后呢咱们再次运行咱们的代码这个呢出现这个问题就是咱们排查还不够彻底
[01:37] 修改完成之后呢咱们等待它运行看它的一个运行结果咱们呢切到HUE上来看咱们月的数据这里呢目前还没有任何数据是因为咱们程序还没有运行完成好程序呢已经运行完成咱们可以看到11月相对于10月这个产品经理这个是负增长这两个呢就是一个正增长咱们来HUE上来查看一下数据刷新
[02:11] 然后对数据进行一个再次查看没有出来可能HUE还没有读到咱们再次刷新一下好这里数据已经出来这个地方产品经理负增长2019年然后是11月这个数据和他们控制台里边打印的数据就是一模一样的到此测试完成之后咱们发现这个结果是匹配的也就是说咱们代码就没有任何问题
[02:44] 这个地方还有一个增幅0的说明它10月份也是30亿条这个呢就是这个数字就很奇妙了咱们来切到文档认为学科排名中学生人数按月统计呢咱们是基于周进行的一个修改咱们呢修改完成代码之后刚刚呢也进行了一个相对应的一个测试测试呢中间是有一个忘修改的一个步骤咱们呢经过咱们的测试也已经修正
[03:14] 修正完成之后呢咱们的结果也保存到了数据仓库中到此呢咱们热门学科排名中学生人数按月统计分析这里就完成了通过学习呢你需要掌握将学生人数这个统计分析呢按月统计分析将它这个结果呢通过一系列的统计加分析然后呢将结果保存到数据仓库中好这里呢咱们测试已经完成咱们呢视频就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark 中编写 Scala 代码，读取数据、进行聚合计算，并将结果写入 Hive 表，最后通过 Hue 工具验证数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Scala 代码中定义 SparkSession 和处理日期的逻辑，其中包含注释“// 1. 获取当月的时间区间，例：1号至18号”。
画面 2: 在代码中选中 `subjectLearnMonth`，右键弹出菜单，选择“Run 'SubjectLearnNumByMonth...'”以执行程序。
画面 3: 显示了 Spark 启动日志，包括成功绑定端口、注册 BlockManager、加载 Hive 配置文件等信息。
画面 4: 展示了 Spark SQL 的执行计划（Execution Plan），显示了多个 Catalyst Tree 的节点，如 `TreedNodeApply`、`TreedNodeTransform` 等。
画面 5: 展示了 Spark SQL 代码，包含 `Spark.conf.set` 设置动态分区模式、`learnDS.repartition` 设置分区数、`Spark.sql` 执行 SQL 语句并 `Spark.close` 关闭连接。
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
import org.apache.Spark.sql.SparkSession

// 获取当月用户人数
object SubjectLearnNumByMonthBiz {
  // Spark session
  val Spark: SparkSession = EtlEnvironment.getSparkSession(this.getClass.getSimpleName)
  // 1. 获取当月的时间区间，例：1号至18号
  def main(args: Array[String]): Unit = {
    import Spark.implicits._
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
    subjectLearnMonth(Spark, current, last).createReplaceView(viewName = "learn_biz_month_biz")
  }
}
```

画面 2:
```scala
subjectLearnMonth(Spark, current, last)
```

画面 3:
```text
15/11/28 17:18:53 INFO SparkEnv: Registering OutputCommitCoordinator
10/11/28 17:18:53 INFO Utils: Successfully started Service SparkUI at http://localhost:4040
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

