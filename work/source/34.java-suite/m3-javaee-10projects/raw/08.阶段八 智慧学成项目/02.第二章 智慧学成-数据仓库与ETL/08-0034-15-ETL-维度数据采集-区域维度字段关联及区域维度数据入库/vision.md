# 画面线理解：15-ETL-维度数据采集-区域维度字段关联及区域维度数据入库

- 阶段：08.阶段八 智慧学成项目
- 章节：02.第二章 智慧学成-数据仓库与ETL
- 源文件：08.阶段八 智慧学成项目\02.第二章 智慧学成-数据仓库与ETL\15-ETL-维度数据采集-区域维度字段关联及区域维度数据入库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:53, 04:18, 06:44, 08:30, 09:28, 11:03, 12:24, 13:09, 14:06, 14:50, 15:22, 15:54, 16:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:48:02

1) 这一组画面整体在讲如何使用 Spark SQL 和 Hive 创建区域维度表，通过读取区域编码和区域名称文件，转换并生成最终的维度表。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Scala 代码，定义了读取区域编码文件和区域名称文件的逻辑，并创建了两个临时视图（area_code 和 region_temp）。
画面2：展示 Hue 的 Table Browser 界面，显示了 data_dimen 数据库下的 area_dim 表结构，包含 9 个字段。
画面3：展示 Scala 代码，定义了 region_temp 的转换逻辑，并创建了 region 视图。
画面4：展示 Scala 代码，定义了最终的 Hive SQL 查询语句，用于连接 area_code 和 region_temp 表。
画面5：展示 Scala 代码，定义了读取区域编码文件和区域名称文件的逻辑，并创建了两个临时视图（area_code 和 region_temp）。
画面6：展示 Scala 代码，定义了最终的 Hive SQL 查询语句，用于连接 area_code 和 region_temp 表。
画面7：展示 Hue 的 File Browser 界面，显示了 /user/hive/external/data_dimen 目录下的多个维度表文件夹。
画面8：展示 Scala 代码，定义了最终的 Hive SQL 查询语句，并设置了输出路径和表名，最后关闭 SparkSession。
画面9：展示 Scala 代码，定义了最终的 Hive SQL 查询语句，并设置了输出路径和表名，最后关闭 SparkSession。
画面10：展示 Scala 代码，定义了最终的 Hive SQL 查询语句，并设置了输出路径和表名，最后关闭 SparkSession。
画面11：展示 Scala 代码，定义了最终的 Hive SQL 查询语句，并设置了输出路径和表名，最后关闭 SparkSession。
画面12：展示 Scala 代码，定义了最终的 Hive SQL 查询语句，并设置了输出路径和表名，最后关闭 SparkSession。
画面13：展示 Hue 的 Table Browser 界面，显示了 data_dimen 数据库下的 area_dim 表数据，包含多个字段的值。
画面14：展示 PDF 文档，内容为“3.2.7 区域维度代码”，说明区域维度表由区域经度和区域编码两个数据合并而成，并展示了区域维度数据的目录结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```scala
val hive = spark.sqlContext
val area_code = sc.textFile(path = "area_code.txt")
val region = sc.textFile(path = "region.txt")

// 区域编码转实体
val area_code_map = area_code.map(line => {
  val strings = line.split(regex = ",")
  val sheng = strings(0).trim().split(regex = "")
  val shi = strings(1).trim().split(regex = "")
  val xian = strings(2).trim().split(regex = "")
  areaCodeMap(sheng(0), sheng(1), shi(0), shi(1), xian(0), xian(1))
})

// 转换为临时表
hive.createDataFrame(area_code_map).createReplaceTempView(viewName = "area_code")

// 区域名称转实体
val region_temp = region.map(line => {
  val strings = line.split(regex = ",")
  regionMap(strings(0), strings(1), strings(2), strings(3).toFloat, strings(4).toFloat)
})

// 转换为临时表
hive.createDataFrame(region_temp).createReplaceTempView(viewName = "region_temp")

// 根据region_temp生成最终表
val result = hive.sql(sqlText = "select row_number() over(order by sheng), * from region_temp")
result.createReplaceTempView(viewName = "region")
```

画面3：
```scala
val region_temp = region.map(line => {
  val strings = line.split(regex = ",")
  regionMap(strings(0), strings(1), strings(2), strings(3).toFloat, strings(4).toFloat)
})

// 转换为临时表
hive.createDataFrame(region_temp).createReplaceTempView(viewName = "region_temp")

// 根据region_temp生成最终表
val result = hive.sql(sqlText = "select row_number() over(order by sheng), * from region_temp")
result.createReplaceTempView(viewName = "region")
```

画面4：
```scala
hive.sql(
  """select *
    from region a
    left join area_code b
    on a.xian = b.xian and a.shi = b.shi
    order by a.id
    """ + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """""" + """"""
