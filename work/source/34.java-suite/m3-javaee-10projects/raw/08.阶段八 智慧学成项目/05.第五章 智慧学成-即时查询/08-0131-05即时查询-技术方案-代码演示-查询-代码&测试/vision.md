# 画面线理解：05即时查询-技术方案-代码演示-查询-代码&测试

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\05即时查询-技术方案-代码演示-查询-代码&测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:26, 02:48, 04:06, 05:16, 06:17, 08:17, 10:34, 13:27, 14:40, 15:43, 17:26, 19:09, 19:38, 20:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:55:49

1) 这一组画面整体在讲如何使用 Spark 分析数据并写入 HBase 的技术实现过程。

2) 按时间顺序列出每张画面的要点：
画面1: 展示技术方案文档，包含数据源、数据仓库、数据采集、数据清洗、HBase 表、Elasticsearch 表等模块的流程图。
画面2: 编写 Spark Scala 代码，创建 SparkSession，定义查询语句，准备数据。
画面3: 在 Spark 代码中，使用 collect().map() 对数据进行处理，将结果转换为字符串。
画面4: Spark 任务执行日志，显示任务成功完成。
画面5: 在 Spark 代码中，将处理后的数据存入 ArrayBuffer。
画面6: 切换到 HBaseUtils.scala 文件，准备创建 HBase 表。
画面7: 在 HBaseUtils.scala 中，配置 HBase 的连接参数，包括 zookeeper 地址和端口。
画面8: 在 HBaseUtils.scala 中，定义 getRowKeyList 方法，用于获取 HBase 表中指定行键的数据。
画面9: 在 HBaseUtils.scala 中，继续完善 getRowKeyList 方法，处理 HBase 表的列族和单元格数据。
画面10: 在 HBaseUtils.scala 中，继续完善 getRowKeyList 方法，处理 HBase 表的列族和单元格数据。
画面11: 在 HBaseUtils.scala 中，继续完善 getRowKeyList 方法，处理 HBase 表的列族和单元格数据。
画面12: 在 Query.scala 中，创建 HBaseUtils 实例，并调用 getRowKeyList 方法获取数据。
画面13: Spark 任务执行日志，显示任务成功完成，并打印出查询结果。
画面14: Spark 任务执行日志，显示任务成功完成，并打印出查询结果。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面2:
package cn.itaast.xc.analysis.demo
import cn.itaast.xc.analysis.common.fileEnvironment
object Query {
  def main(args: Array[String]): Unit = {
    // cs 语句
    val csTable = "demo/doc"
    // Master 表名
    val masterTableName = "demo"
    val spark = ETEnvironment.getSparkSession(this.getClass.getSimpleName, csTableName)
    val sc = spark.sparkContext
    val query = {
      ("query":("match":("name":"王五")))
    }
    sc.parallelize(query).collect().foreach(println)
    spark.close()
  }
}

画面3:
val rdd = sc.cRDD(csTableName, query)
rdd.collect().map(p => {
  rowkeys = p._2.get("id").get.toString
})
spark.close()

画面4:
val rowkeys = new ArrayBuffer[String]()
rdd.collect().map(p => {
  rowkeys += p._2.get("id").get.toString
})
spark.close()

画面6:
def createTable(tableName: String, columnName: String): Unit = {
  if (!HBaseAdmin.tableExists(tableName)) {
    val tableDescriptor = new HTableDescriptor(tableName)
    tableDescriptor.addFamily(new HColumnDescriptor(columnName))
    hbaseAdmin.createTable(tableDescriptor)
  }
}

画面7:
def getTableConfig = {
  val conf = HBaseConfiguration.create()
  conf.set(HConstants.ZOOKEEPER_QUORUM, "xc_online_ik")
  conf.set(HConstants.ZOOKEEPER_PORT, "2181")
  conf
}

画面8:
def getRowKeyList(baseTableName: String, rowkeys: ArrayBuffer[String]): Unit = {
  import scala.collection.JavaConverters._
  val table = connection.getHTable(baseTableName)
  var keyBuffer = ArrayBuffer[String]()
  for (rowkey <- rowkeys) {
    keyBuffer += new Get(rowkey).addColumn(family, qualifier).toString
  }
  val results = table.get(keyBuffer.asJava)
  var resultBuffer = ArrayBuffer[String]()
  for (result <- results) {
    val tmpBuffer = ArrayBuffer[String]()
    for (kv <- result.rawCells()) {
      val va = Bytes.toString(CellUtil.cloneValue(kv))
      tmpBuffer += va
    }
    resultBuffer += tmpBuffer.mkString(" ")
  }
}

画面12:
val hbaseUtils = new HBaseUtils
val result = hbaseUtils.getRowKeyList(hbaseTableName, rowkeys)
println(result.mkString(""))

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1: 架构图中，数据源指向数据仓库，数据仓库指向数据采集，数据采集指向数据清洗，数据清洗指向 HBase 表和 Elasticsearch 表。

5) 不涉及评价画面美观，不输出与课程无关的内容。
