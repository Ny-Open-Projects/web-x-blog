# 画面线理解：03即时查询-技术方案-代码演示-保存-代码

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\03即时查询-技术方案-代码演示-保存-代码_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:52, 01:21, 03:20, 04:37, 06:18, 07:27, 08:30, 09:11, 09:54, 11:39, 12:41, 13:30, 15:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:54:16

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spark 结合 HBase 和 Elasticsearch 实现数据的实时分析与存储。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示技术方案架构图，包含“实时查询”、“数据采集”、“数据仓库”、“数据分析”、“查询接口”等模块，以及“HBase 数据”和“Elasticsearch 数据”两个数据存储模块，数据流向从“实时查询”经“数据采集”到“数据仓库”，再分发至“HBase 数据”和“Elasticsearch 数据”，最终由“查询接口”调用。
画面2：展示 Scala 代码，定义了 SparkSession 和 HBase 表名、列名，准备数据。
画面3：继续展示 Scala 代码，初始化 HBaseUtils 并创建 HBase 表。
画面4：展示 HBaseConfiguration 配置，设置 ZK 地址和端口。
画面5：展示 HBaseUtils 的 createTable 方法，用于创建 HBase 表。
画面6：展示 HBaseConfiguration 的 getConf 方法，用于获取配置。
画面7：展示 HBaseUtils 的 createTable 方法，用于创建 HBase 表。
画面8：展示 Scala 代码，导入 Elasticsearch 的相关类型。
画面9：展示 Scala 代码，使用 EsSparkSQL 将 Spark 数据写入 Elasticsearch。
画面10：展示 Elasticsearch 的配置，设置节点、端口、索引等。
画面11：展示 HBase 客户端的源码，导入相关包。
画面12：展示 HBase Put 操作的代码，添加列。
画面13：展示 HBase Put 操作的代码，添加列。
画面14：展示 HBase Put 操作的代码，添加列并保存。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
1. 采集相关数据及相关的维度存储到数据仓库
2. 使用Spark统计分析相关数据，结果存储到数据仓库
3. 把统计结果保存到Hbase，使用ES索引查询字段及RowKey
4. 业务使用时，在ES中查询RowKey，根据RowKey在Hbase查询数据

画面2：
object Save {
  case class Person(id: String, name: String, age: String)
  def main(args: Array[String]): Unit = {
    val esTableName = "demo/doc"
    val spark = t1Environment.getSparkSession(this.getClass.getSimpleName, esTableName)
    import spark.implicits._
    val hbaseTableName = "demo"
    val hbaseColumnName = "demo_col1"
    val hbaseUtils = new HbaseUtils
    hbaseUtils.createTable(hbaseTableName, hbaseColumnName)
    val jobConf = hbaseUtils.getJobConf(hbaseTableName)
    val rdd = sc.parallelize(Array(Person("a1", "张三", "38岁"), Person("a2", "李四", "29岁"), Person("a3", "王五", "21岁")))
    // todo @HBase - es
    spark.close()
  }
}

画面3：
object Save {
  case class Person(id: String, name: String, age: String)
  def main(args: Array[String]): Unit = {
    val esTableName = "demo/doc"
    val spark = t1Environment.getSparkSession(this.getClass.getSimpleName, esTableName)
    import spark.implicits._
    val hbaseTableName = "demo"
    val hbaseColumnName = "demo_col1"
    val hbaseUtils = new HbaseUtils
    hbaseUtils.createTable(hbaseTableName, hbaseColumnName)
    val jobConf = hbaseUtils.getJobConf(hbaseTableName)
    val rdd = sc.parallelize(Array(Person("a1", "张三", "38岁"), Person("a2", "李四", "29岁"), Person("a3", "王五", "21岁")))
    // todo @HBase - es
    spark.close()
  }
}

画面4：
val conf = HBaseConfiguration.create()
conf.set(Constants.ZOOKEEPER_QUORUM, "xc-online-rk")
conf.set(Constants.ZOOKEEPER_CLIENT_PORT, "2181")
conf

画面5：
def createTable(tableName: String, columnName: String): Unit = {
  if (!HBaseAdmin.tableExists(tableName)) {
    val tableDescriptor = new HTableDescriptor(TableName.valueOf(tableName))
    tableDescriptor.addFamily(new HColumnDescriptor(columnName))
    hbaseAdmin.createTable(tableDescriptor)
  }
}

画面6：
def getConf(tableName: String): Unit = {
  val conf = HBaseConfiguration.create()
  conf.set(Constants.ZOOKEEPER_QUORUM, "xc-online-rk")
  conf.set(Constants.ZOOKEEPER_CLIENT_PORT, "2181")
  conf
}

画面7：
object Save {
  case class Person(id: String, name: String, age: String)
  def main(args: Array[String]): Unit = {
    val esTableName = "demo/doc"
    val spark = t1Environment.getSparkSession(this.getClass.getSimpleName, esTableName)
    import spark.implicits._
    val hbaseTableName = "demo"
    val hbaseColumnName = "demo_col1"
    val hbaseUtils = new HbaseUtils
    hbaseUtils.createTable(hbaseTableName, hbaseColumnName)
    val jobConf = hbaseUtils.getJobConf(hbaseTableName)
    val rdd = sc.parallelize(Array(Person("a1", "张三", "38岁"), Person("a2", "李四", "29岁"), Person("a3", "王五", "21岁")))
    // todo @HBase - es
    spark.close()
  }
}

画面8：
import org.elasticsearch.spark.sql._
import org.elasticsearch.spark._
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.EsSparkSQL_type
import org.elasticsearch.spark.sql.E
