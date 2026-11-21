# 画面线理解：14-ETL-维度数据采集-区域维度原文件数据与实体映射

- 阶段：08.阶段八 智慧学成项目
- 章节：02.第二章 智慧学成-数据仓库与ETL
- 源文件：08.阶段八 智慧学成项目\02.第二章 智慧学成-数据仓库与ETL\14-ETL-维度数据采集-区域维度原文件数据与实体映射_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:21, 00:35, 01:05, 01:42, 01:57, 02:44, 04:30, 05:02, 05:54, 06:18, 06:40, 07:21, 08:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:47:08

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spark 读取区域代码和区域信息文本文件，解析数据并创建 Hive 表。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Scala 代码文件 AreaDimInsert.scala，定义了区域映射类和区域代码类，初始化 SparkSession，并读取 area_code.txt 和 region.txt 文件。
画面 2: 在 Hue 浏览器中查看 area_code.txt 文件内容，显示北京、天津等城市的区域代码。
画面 3: 在 Hue 浏览器中查看 area_code.txt 文件内容，显示河北、山西等省份的区域代码。
画面 4: 在 Scala 代码中，对 area_code.txt 的每一行进行 split 操作，提取省份、城市、区域代码。
画面 5: 在 Scala 代码中，对 area_code.txt 的每一行进行 split 操作，提取省份、城市、区域代码，并对字符串进行 trim 和 split 操作。
画面 6: 在 Scala 代码中，对 area_code.txt 的每一行进行 split 操作，提取省份、城市、区域代码，并对字符串进行 trim 和 split 操作。
画面 7: 在 Scala 代码中，对 area_code.txt 的每一行进行 split 操作，提取省份、城市、区域代码，并对字符串进行 trim 和 split 操作。
画面 8: 在 Scala 代码中，对 area_code.txt 的每一行进行 split 操作，提取省份、城市、区域代码，并对字符串进行 trim 和 split 操作。
画面 9: 在 Scala 代码中，使用 Hive.createDataFrame 创建表 area_code。
画面 10: 在 Scala 代码中，使用 Hive.createDataFrame 创建表 area_code。
画面 11: 在 Hue 浏览器中查看 region.txt 文件内容，显示北京、天津等城市的经纬度信息。
画面 12: 在 Scala 代码中，对 region.txt 的每一行进行 split 操作，提取城市、经纬度信息。
画面 13: 在 Scala 代码中，对 region.txt 的每一行进行 split 操作，提取城市、经纬度信息，并创建临时视图 region_temp。
画面 14: 在 Scala 代码中，对 region.txt 的每一行进行 split 操作，提取城市、经纬度信息，并创建临时视图 region_temp。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
object AreaDimInsert {
  // 省份维度实体
  case class regionMap(sh: String, xian: String, lng: Float, lat: Float)
  // 区域维度实体
  case class areaCodeMap(sheng: String, shengCode: String, shi: String, shiCode: String, xian: String, xianCode: String)
  // 其它Spark session
  val spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
  def main(args: Array[String]): Unit = {
    // 初始化Spark context
    val sc = spark.sparkContext
    val area_code = sc.textFile(path = "/area_code.txt")
    val region = sc.textFile(path = "/region.txt")
  }
}
```

画面 4:
```scala
val area_code = sc.textFile(path = "/area_code.txt")
val region = sc.textFile(path = "/region.txt")
val area = area_code.map(line => {
  val strings = line.split(regexp = "=")
  val sheng = strings(0).trim().split(regexp = ",")
  val shi = strings(1).trim().split(regexp = ",")
  val xian = strings(2).trim().split(regexp = ",")
  areaCodeMap(sheng(0), sheng(1), shi(0), shi(1), xian(0), xian(1))
})
```

画面 9:
```scala
hive.createDataFrame(area).createReplaceTempView(viewName = "area_code")
```

画面 12:
```scala
val region_temp = region.map(line => {
  val strings = line.split(regexp = "=")
  regionMap(strings(0), strings(1), strings(2).toFloat, strings(4).toFloat)
})
```

画面 14:
```scala
hive.createDataFrame(region_temp).createOrReplaceTempView(viewName = "region_temp")
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
