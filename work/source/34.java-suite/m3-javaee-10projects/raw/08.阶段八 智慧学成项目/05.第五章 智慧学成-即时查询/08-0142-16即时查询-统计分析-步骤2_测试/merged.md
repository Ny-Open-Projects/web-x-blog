# 16即时查询-统计分析-步骤2：测试

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\16即时查询-统计分析-步骤2：测试_【海量资源尽在 666java.com】.mp4
- 时长 7分50秒（音频 470s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前边呢已经根据步骤二的保存逻辑咱们编写了保存代码接下来呢就是对代码进行测试这里呢代码测试直接在开发工具中运行即可但是呢查询结果呢咱们这里除了在之前呢除了在那个命令中进行一个查看这里呢还引入了web界面的查看这里web界面的查看主要是针对Aleska设置的数据查看
[00:31] 这里alasksearch header可以很友好的在web中进行数据的一个查看搜索这里alasksearch的header容器咱们在编排的时候已经做了相关的编排操作但是它没有开机启动咱们需要将容器启动这里咱们先将alasksearch容器启动
[01:00] 启动完成之后呢,咱们再来开发工具中进行一个代码的测试这里HBase的查看,由于HBase没有外部界面的一个查看咱们呢还是使用这个脚本的方式在命令,在这个控制台中使用命令进行查看咱们来切到终端,来把AlaskaSourceHeader进行一个启动这里呢
[01:26] 我已经登录到服务器而且呢目录切换到了optcdh5.14.0咱们容器编排的命令容器编排的目录这里呢直接使用啊负值错了直接使用这个命令呢进行一个启动好这里呢显示容器已经启动成功咱们来访问这里呢它的端口是9100ok已经呢
[01:59] 访问成功这个时候这个呢是我之前配置过他呢不是显示的这个默认值怎么来切换问答末日情况下呢他这个数据他这个地址呢是localhost的9200但是呢咱们现在服务器上的es呢是在xc-lane这个9200这个段口下咱们来把它给恢复到默认
[02:29] 重新设置一下,local,就是localhost连接之后呢,它就显示未连接,因为这个地址上呢是没有任何进行的,没有任何ES的一个数据的咱们呢,还把这个给恢复回来,rc-live然后进行一个连接连接之后呢,咱们可以在ES中查看到咱们原来的数据这是咱们最开始在咱们技术方案的地方测试了
[03:00] 保存到HBase以及ES中的一个代码的保存这是咱们当时测试的数据可以很清楚的查看到这个查看结果还是非常友好的好接下来咱们对咱们的代码进行测试切了开发工具直接运行这里它运行需要一段时间咱们来观察日志看代码是否报错等然后等待它运行结束
[03:46] 还在计算中根据日志呢咱们可以看到他呢已经啊这个地方已经报错了咱们来看他是报了一个空指针议场第69行第69行读的是谁呀读的是内姆cosname咱们来hue上查看数据这里h这个数据呢hue上的数据也是空的这个地方呢报空指针就不奇怪了在咱们
[04:22] 测试步骤一的时候也解释过这个地方呢为什么是no因为咱们在前端gs买点呢是模拟生产环境虽然说和生产环境流程是一模一样的但是咱们这个数据是不完整的前端gs买点这些数据呢都是生成的这个随机数据使用url随机生成的所以说这个地方获取不到它对应的这个客栋名称以及用户名称咱们呢直接把它给先注释到就行
[04:53] 这个地方ES也是相同的ES它在索引的时候如果是闹纸的它会自动不索引所以说ES这个地方不用管咱们后期会有一个NiFi生产数据NiFi生产数据它是读取的数据库读取的数据库获取的这些数据都是真实数据包括用户ID 客户ID这些都是真实数据它就不会出现闹纸这种情况
[05:21] 咱们来重新测试就是把现在这个结果它只要能有的数据它只要能保存到ES和HBase中就说明咱们这个代码是OK的这里呢咱们来刷新一下ES刚才呢它已经做了一个保存这个地方ES刚才已经保存成功了这个是没有问题的它刚才呢是HBase没有保存成功咱们呢再次等待因为刚才ES是没有报错的
[05:54] 好这次呢代码没有报错说明HBase也保存成功了咱们在这刷新ES呢刚才是保存了两次所以说这个地方呢会有重复的操作重复了这个数据咱们来登录到HBase这个容器使用Docker命令Docker命令参数呢是IT咱们要登录的容器呢是HBase终端呢是BSH
[06:27] 切换到HBase的BIM模组然后使用HBase的脚本然后来查看数据这里咱们可以先查看一下有哪些表这里表是存在的说明它这个地方保存已经成功删除不能删除咱们直接使用输出了咱们直接使用scan命令来查看这张表这个时候你可以看到数据
[07:05] 已经进来这里进来的是客厂ID和DataInfo因为对于咱们现在这个代码来讲的话客厂IDDataInfoUserID这些数据是不为空的咱们来对一下客厂ID12345它一共是五列12345一共是五列客厂ID时间CountTimeUserID是对的
[07:36] 说明了咱们这个代码功能上就没有问题了OK咱们这个代码的测试呢就到这里好视频呢也就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.apache.Hadoop.hbase.client.Put
import org.apache.Hadoop.hbase.io.ImmutableBytesWritable
import org.apache.Spark.sql.SparkSession

画面5：
val Spark: SparkSession = EtEnvironment.getSparkSession(this.getClass.getSimpleName, esTableName)
def main(args: Array[String]): Unit = {
  import Spark.implicits._
  val hbaseUtils = new HbaseUtils
  val hbaseTableName = "LearningOnlineDetail"
  val hbaseColumnNames = "learning_online_detail"
  hbaseUtils.createTable(hbaseTableName, hbaseColumnNames)
  val jdbcConf = hbaseUtils.getHbaseConf(hbaseTableName)
  val hiveTableName = "data_course.learning_course_online_dhm"
  val date_info = "2019-12-12"
  val sql = "select * from " + hiveTableName + " where data_info = '" + date_info + "' as learning_course_online_dhm"

画面6：
10/12/12 02:12:38 INFO SharedData: Setting Hive.metastore.warehouse.dir to "null" to the value of Spark.sql.warehouse.dir
10/12/12 02:12:38 INFO SharedData: Setting Hive.metastore.path to "file:///D:/code-analysis/xc-Service-search/target/classes/Hive-site.xml" to the value of Spark.sql.warehouse.dir
10/12/12 02:12:38 INFO HiveMetastore: Opening new store with implementation class org.apache.Hadoop.Hive.metastore.ObjectStore
10/12/12 02:12:38 INFO HiveMetastore: Property datanucleus.cache.level2.jpa.pushdown unknown - will be ignored
10/12/12 02:12:38 INFO HiveMetastore: Setting Metastore object pin classes with Hive.metastore.cache.pinclasses to "Table,StorageDescriptor,SchemaInfo,Partition,Database,Type,FieldSchema"
10/12/12 02:12:38 INFO HiveMetastore: The class "org.apache.Hadoop.Hive.metastore.model.FieldSchema" is tagged as "embedded-only" so does not have its own datastore table.
10/12/12 02:12:38 INFO HiveMetastore: The class "org.apache.Hadoop.Hive.metastore.model.Md5" is tagged as "embedded-only" so does not have its own datastore table.
10/12/12 02:12:38 INFO HiveMetastore: The class "org.apache.Hadoop.Hive.metastore.model.Md5" is tagged as "embedded-only" so does not have its own datastore table.
10/12/12 02:12:38 INFO HiveMetastore: Reading in results for query "org.datanucleus.store.rdbms.query.SQLQuery" since the connection used is closing
10/12/12 02:12:38 INFO HiveMetastore: Initialized ObjectStore

画面7：
Caused by: java.lang.NullPointerException
at org.apache.Hadoop.hbase.util.Bytes.toBytes(Bytes.java:525)
at cn.itcast.xc.analysis.search.InstantQueryStep2ToHbaseAndES$.apply(InstantQueryStep2ToHbaseAndES.scala:8)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem.scala:122)
at org.apache.Spark.internal.io.SparkHadoopFilesystem$.apply(SparkHadoopFilesystem

