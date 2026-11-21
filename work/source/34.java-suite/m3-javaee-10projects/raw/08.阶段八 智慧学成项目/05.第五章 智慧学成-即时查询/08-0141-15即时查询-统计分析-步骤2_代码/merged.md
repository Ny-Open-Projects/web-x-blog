# 15即时查询-统计分析-步骤2：代码

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\15即时查询-统计分析-步骤2：代码_【海量资源尽在 666java.com】.mp4
- 时长 8分14秒（音频 494s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前面呢,咱们已经分析了统计分析步骤的保存逻辑,接下来呢,咱们就根据这个逻辑进行代码的编写来切到开发工具,开发工具中呢,已经准备好了咱们的基础代码,这里呢,基础代码来源于咱们在技术方案的时候进行的一个HBase和ES的一个测试,这里呢,
[00:26] 主要是测试了HBase和ES的一个保存把数据呢通过这里创建的模拟数据保存在HBase和ES中咱们就使用了这里的基础代码因为代码都是一样的咱们直接来了一个复用唯一不一样的就是咱们的表名还有咱们的列名这里呢表名和列名也已经定义好直接使用咱们来进行代码的一个编写首先呢第一步就是根据
[00:56] 这个日期获取数据仓库中的数据咱们呢首先需要一个日期这里呢data info这个日期呢咱们需要来到HUE上来查看咱们哪天的数据比较多这里可以看到是12号这个数据比较多咱们的这个data info就定于为这天好然后呢就是Spark circle的一个编写这里呢直接select型from咱们的表的话就是咱们
[01:32] Hive中的这个表是这个咱们直接使用Hive中的这个表使用变量的方式把它给传进来接着咱们的查询条件就是具体的日期这里也是data infoNFO它等于咱们这个地方也是使用变量传递的方式等于咱们的data info查完之后咱们这个地方得到是什么得到是一个df
[02:00] 但是这个地方保存的时候它需要的是谁它是不是需要一个dataset咱们把它给转换成咱们的一个实体转换成实体就变成了一个dataset这里是learn-cos-online-dm这个中间表就是咱们这里数据仓库中中间表对应的一个实体就是它这里有相应的注射转换为它之后它就是一个dataset咱们
[02:30] 使用变量进行接收这里呢ds数据有了之后咱们保存到es中咱们前边也有现成的代码这里呢就直接复用保存es这里呢它已经是一个ds了所以说就不需要转换咱们直接把learn ds给它消息了好咱们保存到es中呢就这一步就完成了接下来是保存hbase保存hbase呢咱们前边其实也已经写过了
[03:02] 主要的一个操作是什么把这个数RDD的数据进行一个put的转换进行put转换之后使用Hadoop的提供的保存到HBase的方法就是HadoopsalesHadoopDNSET这个方法它可以直接将数据保存到HBase中这里咱们把它给拿过来这里需要的是一个RDD咱们前面是一个什么是一个DS咱们DS使用
[03:32] 点rdd直接可以把它转换成rdd转换成rdd之后呢这里转换成rdd之后咱们进行相应的配置就行了首先呢是列的一个配置这个呢叫做obj因为它这个对象这个呢就是咱们的line calls online id就是咱们的rokey接下来呢就是根据咱们这个对象呢进行一个数据的一个
[04:06] 封装这个时候呢我把它给配置一下这是OBG点这个呢先把它给删了咱们呢有多少等会呢用多少首先呢是第一列站错位置了接下来呢是第二列接下来呢是第三列这个呢都是体力活没有什么技术含量就使用比较原始的方法进行一个复制单贴
[04:48] user nameuser namelearn timelearn timelearn timelearn countlearn count然后最后一个呢是data変号好这里呢咱们已经把这个数据给准备好准备好之后呢它就保存到hbs保存到hbs呢咱们的一个任务就算完成了咱们来再过一下那代码首先呢是查新数据接下来呢是
[05:17] 数据索引到ES这个地方呢是索引ES是指索引查新的资料移入K咱们这个地方索引的是谁啊是不是索引了所有啊这个地方索引所有的情况下也就是说咱们这个逻辑是不符合咱们文档中这个逻辑的这个地方呢就需要做一个修改这个修改呢咱们放到最后咱们来看第三步这个任务是否是正确的将数据呢保存到一次倍次
[05:49] 这个保存是完整的,咱们需要把所有的字段都给保存了这里呢,HBase的colorma1指令在上面定义着HBase的表明这个地方定义着,咱们呢,C5也就是说咱们第三步的保存代码是OK的,然而第二步呢咱们保存的所有按正常来按照咱们那个文档中的这个逻辑呢,咱们是保存这个查询字段按照生产环境,就是咱们正常情况下的生产环境也是只保存查询字段
[06:16] 所以说呢,咱们这个地方要把这个DS进行一个处理这里呢,直接MAP也是叫做OBG吧对它进行一个操作咱们呢,其实是在咱们的这个实体中呢已经有了一个learning cause online ES index这个实体呢,就是咱们保存到ES中所有自乱的一个实体
[06:45] 咱们首先要索引的是谁首先要索引的就是Rokey这里的Rokey就是咱们对象的ID和他是对应的咱们进行一个复制obg.我复制一下一会可以直接用是learnid接下来咱们索引的是cosname接下来咱们索引的是videonamevideoname之后是username以及咱们的data info
[07:15] 这是咱们所以的字段所以的字段之后呢它这个其实得到的一个结果还是ds这个呢起一个变量接受一下是learn ds但是呢就不能叫ds的因为前面咱们是不是已经有一个ds了它呢是往es中所以呢咱们呢就叫learn esok这里呢就符合了咱们这里保存逻辑中的这个代码呢就符合了咱们保存逻辑
[07:47] 好到此呢咱们步骤二的代码编写就完成了通过代码的编写呢需要掌握根据日期存数据仓库中获取数据然后呢再根据咱们查询的一个字段和周K所用到ES中一定要根据字段进行处理接下来呢是完整的数据保存到Espace好步骤二代码的编写就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark 读取 Hive 表数据，转换为自定义对象，并写入 HBase 表。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 Scala 代码文件 InstantQueryStep2ToHbaseAndES.scala，其中定义了 HBase 表名和 Hive 表名，准备创建 HBase 表。
画面 2: 展示了 Scala 代码文件 Save.scala，定义了 Person 案例类，并创建了 SparkSession、HBase 表和数据。
画面 3: 展示了 Hue 界面，显示了 Hive 表 learning_course_online_dwm 的数据，其中包含学习记录。
画面 4: 展示了 InstantQueryStep2ToHbaseAndES.scala 代码，设置了日期参数并执行了 Spark SQL 查询。
画面 5: 展示了 Save.scala 代码，定义了 HBase 表名和列名，并创建了 HBase 表。
画面 6: 展示了 Save.scala 代码，定义了 Person 案例类，并创建了 SparkSession、HBase 表和数据。
画面 7: 展示了 Course.scala 代码，定义了 LearningCourseOnlineDm 案例类，用于表示学习课程数据。
画面 8: 展示了 Course.scala 代码，定义了 LearningCourseOnlineDm 案例类，并展示了其字段。
画面 9: 展示了 InstantQueryStep2ToHbaseAndES.scala 代码，定义了 Hive 表名和 HBase 表名。
画面 10: 展示了 InstantQueryStep2ToHbaseAndES.scala 代码，定义了 Hive 表名和 HBase 表名。
画面 11: 展示了 InstantQueryStep2ToHbaseAndES.scala 代码，定义了 Hive 表名和 HBase 表名。
画面 12: 展示了 InstantQueryStep2ToHbaseAndES.scala 代码，定义了 Hive 表名和 HBase 表名。
画面 13: 展示了 InstantQueryStep2ToHbaseAndES.scala 代码，定义了 Hive 表名和 HBase 表名。
画面 14: 展示了 InstantQueryStep2ToHbaseAndES.scala 代码，定义了 Hive 表名和 HBase 表名。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
import Spark.sql
val hbaseTableName = "LearningOnlineDetail"
val hbaseColumnFamily = "learning_online_detail"
// 创建HBase表
hbaseUtils.createTable(hbaseTableName, hbaseColumnFamily)
val jdbcConf = hbaseUtils.getJdbcConf(hbaseTableName)
// 查询
val hiveTableName = "data_course.learning_course_online_dwm"
val date_info = "2019-12-12"
Spark.sql(s"select * from ${hiveTableName} where date_info = '${date_info}'").as[LearningCourseOnlineDm].collect()
```

画面 2:
```scala
object Save {
  case class Person(id: String, name: String, age: String)
  def main(args: Array[String]): Unit = {
    val esTableame = "demo/doc"
    val Spark = EtiEnvironment.getSparkSession(this.getClass.getSimpleName, esTableame)
    import Spark.implicits._
    val sc = Spark.sparkContext
    val hbaseTableName = "demo"
    val hbaseColumnFamily = "demo_col1"
    val hbaseUtils = new HbaseUtils
    hbaseUtils.createTable(hbaseTableName, hbaseColumnFamily)
    val jdbcConf = hbaseUtils.getJdbcConf(hbaseTableName)
    val rdd = sc.parallelize(Array(Person("a1", "张三", "30岁"), Person("a2", "李四", "29岁"), Person("a3", "王五", "21岁")))
    // 写入HBase
    rdd.map(p => {
      val put = new Put(Bytes.toBytes(p.id))
      put.addColumn(Bytes.toBytes(hbaseColumnFamily), Bytes.toBytes("name"), Bytes.toBytes(p.name))
      put.addColumn(Bytes.toBytes(hbaseColumnFamily), Bytes.toBytes("age"), Bytes.toBytes(p.age))
      put
    }).saveAsHadoopDataset(jdbcConf)
    Spark.close()
  }
}
```

画面 3:
无代码或配置。

画面 4:
```scala
val date_info = "2019-12-12"
Spark.sql(s"select * from ${hiveTableName} where date_info = '${date_info}'").as[LearningCourseOnlineDm].collect()
```

画面 5:
```scala
val hbaseUtils = new HbaseUtils
hbaseUtils.createTable(hbaseTableName, hbaseColumnFamily)
val jdbcConf = hbaseUtils.getJdbcConf(hbaseTableName)
val rdd = sc.parallelize(Array(Person("a1", "张三", "30岁"), Person("a2", "李四", "29岁"), Person("a3", "王五", "21岁")))
```

画面 6:
```scala
val put = new Put(Bytes.toBytes(obj.learning_course_online_id))
put.addColumn(Bytes.toBytes(hbaseColumnFamily), Bytes.toBytes("course_id"), Bytes.toBytes(obj.course_id))
put.addColumn(Bytes.toBytes(hbaseColumnFamily), Bytes.toBytes("course_name"), Bytes.toBytes(obj.course_name))
put.addColumn(Bytes.toBytes(hbaseColumnFamily), Bytes.toBytes("video_name"), Bytes.toBytes(obj.video_name))
put.addColumn(Bytes.toBytes(hbaseColumnFamily), Bytes.toBytes("user_id"), Bytes.toBytes(obj.user_id))
put.addColumn(Bytes.toBytes(hbaseColumnFamily), Bytes.toBytes("user_name"), Bytes.toBytes(obj.user_name))
put.addColumn(Bytes.toBytes(hbaseColumnFamily), Bytes.toBytes("learn_time"), Bytes.toBytes(obj.learn_time))
put.addColumn(Bytes.toBytes(hbaseColumnFamily), Bytes.toBytes("learn_count"), Bytes.toBytes(obj.learn_count))
put.addColumn(Bytes.toBytes(hbaseColumnFamily), Bytes.toBytes("date_info"), Bytes.toBytes(obj.date_info))
```

画面 7:
```scala
case class LearningCourseOnlineDm(
  learning_course_online_id: String,
  course_id: String,
  course_name: String,
  video_name: String,
  user_id: String,
  user_name: String,
  learn_time: String,
  learn_count: String,
  date_info: String
)
```

画面 8:
```scala
case class LearningCourseOnlineDm(
  learning_course_online_id: String,
  course_id: String,
  course_name: String,
  video_name: String,
  user_id: String,
  user_name: String,
  learn_time: String,
  learn_count: String,
  date_info: String
)
```

画面 9:
```scala
val hbaseTableName = "learning_online_detail"
val hiveTableName = "data_course.learning_course_online_dwm"
val date_info = "2019-12-12"
val learnDS = Spark.sql(s"select * from ${hiveTableName} where date_info = '${date_info}'").as[LearningCourseOnlineDm]
```

画面 10:
```scala
val hbaseTableName = "learning_online_detail"
val hiveTableName = "data_course.learning_course_online_dwm"
val date_info = "2019-12-12"
val learnDS = Spark.sql(s"select * from ${hiveTableName} where date_info = '${date_info}'").as[LearningCourseOnlineDm]
```

画面 11:
```scala
val hbaseTableName = "learning_online_detail"
val hiveTableName = "data_course.learning_course_online_dwm"
val date_info = "2019-12-12"
val learnDS = Spark.sql(s"select * from ${hiveTableName} where date_info = '${date_info}'").as[LearningCourseOnlineDm]
```

画面 12:
```scala
val hbaseTableName = "learning_online_detail"
val hiveTableName = "data_course.learning_course_online_dwm"
val date_info = "2019-12-12"
val learnDS = Spark.sql(s"select * from ${hiveTableName} where date_info = '${date_info}'").as[LearningCourseOnlineDm]
```

画面 13:
```scala
object InstantQueryStep2ToHbaseAndES {
  def main(args: Array[String]): Unit = {
    import Spark.implicits._
    val Spark: SparkSession = EtiEnvironment.getSparkSession(this.getClass.getSimpleName, "learning_online_detail")
    val hbaseUtils = new HbaseUtils
    val hbaseTableName = "learning_online_detail"
    val hbaseColumnFamily = "learning_online_detail"
    // 创建HBase表
    hbaseUtils.createTable(hbaseTableName, hbaseColumnFamily)
    val jdbcConf = hbaseUtils.getJdbcConf(hbaseTableName)
  }
}
```

画面 14:
```scala
learnDS.rdd.map(obj => {
  val put = new Put(Bytes.toBytes(obj.learning_course_online_id))
  put.addColumn(Bytes.toBytes(hbaseColumnFamily), Bytes.toBytes("course_id"), Bytes.toBytes(obj.course_id))
  put.addColumn(Bytes.toBytes(hbaseColumnFamily), Bytes.toBytes("course_name"), Bytes.to

