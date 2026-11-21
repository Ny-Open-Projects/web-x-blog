# 画面线理解：15即时查询-统计分析-步骤2：代码

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\15即时查询-统计分析-步骤2：代码_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:31, 01:10, 02:12, 02:40, 03:21, 04:03, 04:21, 05:14, 05:59, 06:29, 07:01, 07:51, 08:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:03:05

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
import spark.sql
val hbaseTableName = "LearningOnlineDetail"
val hbaseColumnFamily = "learning_online_detail"
// 创建HBase表
hbaseUtils.createTable(hbaseTableName, hbaseColumnFamily)
val jdbcConf = hbaseUtils.getJdbcConf(hbaseTableName)
// 查询
val hiveTableName = "data_course.learning_course_online_dwm"
val date_info = "2019-12-12"
spark.sql(s"select * from ${hiveTableName} where date_info = '${date_info}'").as[LearningCourseOnlineDm].collect()
```

画面 2:
```scala
object Save {
  case class Person(id: String, name: String, age: String)
  def main(args: Array[String]): Unit = {
    val esTableame = "demo/doc"
    val spark = EtiEnvironment.getSparkSession(this.getClass.getSimpleName, esTableame)
    import spark.implicits._
    val sc = spark.sparkContext
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
    spark.close()
  }
}
```

画面 3:
无代码或配置。

画面 4:
```scala
val date_info = "2019-12-12"
spark.sql(s"select * from ${hiveTableName} where date_info = '${date_info}'").as[LearningCourseOnlineDm].collect()
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
val learnDS = spark.sql(s"select * from ${hiveTableName} where date_info = '${date_info}'").as[LearningCourseOnlineDm]
```

画面 10:
```scala
val hbaseTableName = "learning_online_detail"
val hiveTableName = "data_course.learning_course_online_dwm"
val date_info = "2019-12-12"
val learnDS = spark.sql(s"select * from ${hiveTableName} where date_info = '${date_info}'").as[LearningCourseOnlineDm]
```

画面 11:
```scala
val hbaseTableName = "learning_online_detail"
val hiveTableName = "data_course.learning_course_online_dwm"
val date_info = "2019-12-12"
val learnDS = spark.sql(s"select * from ${hiveTableName} where date_info = '${date_info}'").as[LearningCourseOnlineDm]
```

画面 12:
```scala
val hbaseTableName = "learning_online_detail"
val hiveTableName = "data_course.learning_course_online_dwm"
val date_info = "2019-12-12"
val learnDS = spark.sql(s"select * from ${hiveTableName} where date_info = '${date_info}'").as[LearningCourseOnlineDm]
```

画面 13:
```scala
object InstantQueryStep2ToHbaseAndES {
  def main(args: Array[String]): Unit = {
    import spark.implicits._
    val spark: SparkSession = EtiEnvironment.getSparkSession(this.getClass.getSimpleName, "learning_online_detail")
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
