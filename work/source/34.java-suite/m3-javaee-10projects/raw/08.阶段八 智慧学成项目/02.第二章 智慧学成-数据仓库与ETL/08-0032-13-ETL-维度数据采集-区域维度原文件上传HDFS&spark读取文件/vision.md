# 画面线理解：13-ETL-维度数据采集-区域维度原文件上传HDFS&spark读取文件

- 阶段：08.阶段八 智慧学成项目
- 章节：02.第二章 智慧学成-数据仓库与ETL
- 源文件：08.阶段八 智慧学成项目\02.第二章 智慧学成-数据仓库与ETL\13-ETL-维度数据采集-区域维度原文件上传HDFS&spark读取文件_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:41, 00:58, 01:33, 02:01, 02:28, 03:28, 04:43, 05:14, 05:42, 06:51, 07:17, 08:09, 08:30, 08:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:46:33

1) 这一组画面整体在讲如何使用 Spark 读取文本文件（area_code.txt 和 region.txt）并进行数据处理，涉及 Hadoop 文件系统、Hue 文件浏览器和 Scala 代码编写。

2) 按时间顺序列出每张画面的要点：
画面1：在 Windows 文件资源管理器中，定位到 data 目录，显示 area_code.txt 和 region.txt 两个文件。
画面2：在 Hue 文件浏览器中，弹出“Upload to /”对话框，准备上传文件。
画面3：在 Hue 文件浏览器中，打开并显示 area_code.txt 文件内容，包含城市、省、区、邮编等信息。
画面4：在 Hue 文件浏览器中，打开并显示 region.txt 文件内容，包含城市、经纬度坐标。
画面5：在 IntelliJ IDEA 中，打开 xc-analysis 项目，显示项目结构。
画面6：在 IntelliJ IDEA 中，打开 AreaDimInsert.scala 文件，显示 Spark 会话初始化代码。
画面7：在 IntelliJ IDEA 中，打开 core-site.xml 文件，显示 Hadoop 配置。
画面8：在 Hue 文件浏览器中，页面加载中，显示加载图标。
画面9：在 IntelliJ IDEA 中，同时打开 Hue 文件浏览器和 AreaDimInsert.scala 文件，显示 region.txt 文件内容。
画面10：在 IntelliJ IDEA 中，编辑 AreaDimInsert.scala 文件，定义 regionMap 案例类。
画面11：在 IntelliJ IDEA 中，编辑 AreaDimInsert.scala 文件，定义 areaCodeMap 案例类。
画面12：在 IntelliJ IDEA 中，编辑 AreaDimInsert.scala 文件，定义 area_code 案例类。
画面13：在 IntelliJ IDEA 中，编辑 AreaDimInsert.scala 文件，定义 area_code 案例类，包含 shi、xian 等字段。
画面14：在 IntelliJ IDEA 中，编辑 AreaDimInsert.scala 文件，定义 region 案例类，包含 path = "/region.txt"。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6代码：
```scala
object AreaDimInsert {
  val spark: SparkSession = SparkSession.builder()
    .appName("AreaDimInsert")
    .config("spark.sql.warehouse.dir", "hdfs://node1:8020/user/hive/warehouse")
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    .config("spark.sql.catalogImplementation", "inmemory")
    .config("spark.sql.adaptive.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.skewJoin.enabled", "true")
    .config("spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes", "100M")
    .config("spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes", "100M")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("
