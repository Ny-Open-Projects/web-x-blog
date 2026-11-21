# 画面线理解：16即时查询-统计分析-步骤2：测试

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\16即时查询-统计分析-步骤2：测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:11, 01:41, 02:41, 03:20, 03:49, 04:03, 04:53, 05:08, 05:32, 05:49, 06:05, 07:19, 07:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:04:05

1) 这一组画面整体在讲如何使用 Spark 将 Hive 表数据写入 HBase 和 Elasticsearch。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程文档“3.2 步骤2: 保存到es, hbase”的“3.2.2 代码”部分，代码文件为 InstantQueryStep2ToHbaseAndES.scala，包含 SparkSession 初始化和 HBase 表创建的导入语句。
画面2：展示 HBase 中表 learning_online_detail 的数据，显示其大小和列信息，下方有“3.2.4 使用hbase注意事项”标题。
画面3：展示 Xshell 远程连接终端界面，路径为 /opt/cdh5.14.0s。
画面4：展示 Elasticsearch 的 Hue 界面，地址为 http://xc-online:9100，页面显示“集群概览”和“连接”按钮。
画面5：展示 IntelliJ IDEA 编辑器中 InstantQueryStep2ToHbaseAndES.scala 文件内容，包含 SparkSession 初始化、HBase 表名和列名定义、以及 Hive 表查询语句。
画面6：展示 IntelliJ IDEA 的运行日志，显示 Spark 会话初始化、Hive 元数据初始化、以及连接 MySQL 的信息。
画面7：展示 IntelliJ IDEA 的运行日志，显示 Spark 任务执行失败，错误原因为 java.lang.NullPointerException。
画面8：展示 IntelliJ IDEA 编辑器中 InstantQueryStep2ToHbaseAndES.scala 文件内容，显示 HBase 表创建和数据写入的代码。
画面9：展示课程文档“3.3 Nifi生产数据”的“3.3.1 生产数据脚本”部分，脚本内容包含 Python 代码，用于生成模拟数据。
画面10：展示 IntelliJ IDEA 的运行日志，显示 Spark 服务启动成功，端口为 9000。
画面11：展示 IntelliJ IDEA 的运行日志，显示 Hive 元数据初始化完成，以及创建了 admin 角色。
画面12：展示 Elasticsearch 的 Hue 界面，显示表 learning_online_detail 的数据，包含多个文档，字段包括 learning_course_online_id、date_info、id、name、age。
画面13：展示 IntelliJ IDEA 编辑器中 InstantQueryStep2ToHbaseAndES.scala 文件内容，显示数据写入 HBase 的代码，包含 .put() 方法和 .saveAsHadoopDataset() 方法。
画面14：展示课程文档“3.3 Nifi生产数据”的“3.3.1 生产数据脚本”部分，脚本内容与画面9相同。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
package cn.itcast.xc.analysis.search
import cn.itcast.xc.analysis.common.EtEnvironment
import cn.itcast.xc.entity.{LearningCourseOnlineDm, LearningCourseOnlineIndex}
import cn.itcast.xc.utils.HbaseUtils
import org.apache.hadoop.hbase.client.Put
import org.apache.hadoop.hbase.io.ImmutableBytesWritable
import org.apache.spark.sql.SparkSession

画面5：
val spark: SparkSession = EtEnvironment.getSparkSession(this.getClass.getSimpleName, esTableName)
def main(args: Array[String]): Unit = {
  import spark.implicits._
  val hbaseUtils = new HbaseUtils
  val hbaseTableName = "LearningOnlineDetail"
  val hbaseColumnNames = "learning_online_detail"
  hbaseUtils.createTable(hbaseTableName, hbaseColumnNames)
  val jdbcConf = hbaseUtils.getHbaseConf(hbaseTableName)
  val hiveTableName = "data_course.learning_course_online_dhm"
  val date_info = "2019-12-12"
  val sql = "select * from " + hiveTableName + " where data_info = '" + date_info + "' as learning_course_online_dhm"

画面6：
10/12/12 02:12:38 INFO SharedData: Setting hive.metastore.warehouse.dir to "null" to the value of spark.sql.warehouse.dir
10/12/12 02:12:38 INFO SharedData: Setting hive.metastore.path to "file:///D:/code-analysis/xc-service-search/target/classes/hive-site.xml" to the value of spark.sql.warehouse.dir
10/12/12 02:12:38 INFO HiveMetastore: Opening new store with implementation class org.apache.hadoop.hive.metastore.ObjectStore
10/12/12 02:12:38 INFO HiveMetastore: Property datanucleus.cache.level2.jpa.pushdown unknown - will be ignored
10/12/12 02:12:38 INFO HiveMetastore: Setting Metastore object pin classes with hive.metastore.cache.pinclasses to "Table,StorageDescriptor,SchemaInfo,Partition,Database,Type,FieldSchema"
10/12/12 02:12:38 INFO HiveMetastore: The class "org.apache.hadoop.hive.metastore.model.FieldSchema" is tagged as "embedded-only" so does not have its own datastore table.
10/12/12 02:12:38 INFO HiveMetastore: The class "org.apache.hadoop.hive.metastore.model.Md5" is tagged as "embedded-only" so does not have its own datastore table.
10/12/12 02:12:38 INFO HiveMetastore: The class "org.apache.hadoop.hive.metastore.model.Md5" is tagged as "embedded-only" so does not have its own datastore table.
10/12/12 02:12:38 INFO HiveMetastore: Reading in results for query "org.datanucleus.store.rdbms.query.SQLQuery" since the connection used is closing
10/12/12 02:12:38 INFO HiveMetastore: Initialized ObjectStore

画面7：
Caused by: java.lang.NullPointerException
at org.apache.hadoop.hbase.util.Bytes.toBytes(Bytes.java:525)
at cn.itcast.xc.analysis.search.InstantQueryStep2ToHbaseAndES$.apply(InstantQueryStep2ToHbaseAndES.scala:8)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem
