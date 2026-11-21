# 04即时查询-技术方案-代码演示-保存-测试

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\04即时查询-技术方案-代码演示-保存-测试_【海量资源尽在 666java.com】.mp4
- 时长 2分52秒（音频 172s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续前边已经编写了保存的HBase以及所有的Alaska测试的代码咱们接下来对代码进行测试直接在开发工具中运行即可这里代码正在运行咱们来登录到HBase容器中进行结果查看这里使用Dock命令exec参数是-it参数
[00:32] 我们要登录的容器是HBase容器终端是BSH咱们来切到HBase的BMU使用HBase命令这里咱们需要采用的参数是SHARE参数就是得到HBase的SHARE得到它之后咱们就等待咱们这个程序执行完成好这里已经执行完成执行完成之后咱们就可以进行一个
[01:09] 数据到查看list 它这个时候咱们可以看到咱们的table呢Demo这个table已经创建好了咱们来查看它这个数据这个时候你已经可以看到A1这个列就是咱们的Rookie它呢一共有两个这个行一共有两个列它的列呢分别是NameName和Age下边呢也是一样的都是有Name和Age
[01:39] 这说明HBase咱们已经保存成功了接下来呢来查看Elexic Search是否保存成功这里呢查看Elexic Search是否保存成功咱们在代码中有一个咱们在文档中有一个链接咱们来点击这个链接进行一个查看好我已经点击过了按照Ctrl键点击即可这个时候呢访问咱们ES的9200端口然后呢传递的是
[02:10] 这个API search API然后呢它就得到了当前HBase这个ES中所有的数据这里呢咱们可以看到一共有三个这三个数据呢就是咱们在代码中准备的这三条数据这三条数据咱们HBase呢和Alaska search都已经测试成功说明呢咱们使用代码保存是没有问题的接下来呢
[02:42] 咱们进行使用代码查询的这个操作使用代码进行查询的操作咱们交给下一个视频好本视频就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spark 将数据写入 HBase，并通过 EsSparkSQL 将数据同步到 Elasticsearch，最终在浏览器中查询验证数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- IDE 中显示 Scala 代码，定义了 HBase 表名和数据写入逻辑。
- 代码中包含 HBase 表名 "demo_coll" 和数据数组。
- 代码末尾调用 .saveAsHadoopDataset(jobConf)。

画面2：
- 代码中 HBase 表名被修改为 "demo_coll"。
- 代码逻辑与画面1相同。

画面3：
- IDE 中代码未变化，但终端窗口显示 Spark 任务执行日志。
- 日志显示任务成功完成，输出路径为 /demo/doc。

画面4：
- 终端窗口中执行了停止 HBase 服务的脚本：./shutdown_regionserver.rb。
- 任务执行成功，退出码为 0。

画面5：
- 终端窗口中显示 Spark 任务执行日志。
- 日志显示任务成功完成，输出路径为 /demo/doc。

画面6：
- 终端窗口中执行了 HBase Shell 命令：scan 'demo'。
- 输出显示表中包含三行数据，列名为 column-demo_collage，值为不同字符串。

画面7：
- 终端窗口中执行了 HBase Shell 命令：scan 'demo'。
- 输出显示表中包含三行数据，列名为 column-demo_collage，值为不同字符串。

画面8：
- 终端窗口中执行了 HBase Shell 命令：scan 'demo'。
- 输出显示表中包含三行数据，列名为 column-demo_collage，值为不同字符串。

画面9：
- 终端窗口中显示 Spark 任务执行日志。
- 日志显示任务成功完成，输出路径为 /demo/doc。

画面10：
- PPT 页面标题为 "1.2.1 代码演示"。
- 代码部分包含 package、import 语句和 case class Person。
- 代码中定义了 val esTableName = "demo/doc" 和 val hbaseTableName = "demo"。

画面11：
- 浏览器中显示 Elasticsearch 查询结果。
- 查询结果包含索引 "demo"、类型 "_type"、文档 ID、_score、_source 等字段。
- _source 字段包含 name 和 age 字段，值分别为 "王五" 和 "21岁"。

画面12：
- IDE 中显示 Scala 代码，定义了 HBase 表名和数据写入逻辑。
- 代码中包含 HBase 表名 "demo_coll" 和数据数组。
- 代码末尾调用 .saveAsHadoopDataset(jobConf)。

画面13：
- IDE 中显示 Scala 代码，定义了 HBase 表名和数据写入逻辑。
- 代码中包含 HBase 表名 "demo_coll" 和数据数组。
- 代码末尾调用 .saveAsHadoopDataset(jobConf)。

画面14：
- IDE 中显示 Scala 代码，定义了 HBase 表名和数据写入逻辑。
- 代码中包含 HBase 表名 "demo_coll" 和数据数组。
- 代码末尾调用 .saveAsHadoopDataset(jobConf)。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```scala
val hbaseTableName = "demo_coll"
val hbaseColumnNames = "demo_coll"
val jobConf = HbaseUtils.getJobConf(hbaseTableName)
val rdd = sc.parallelize(Array(Person("a1", "张三", "30岁"), Person("a2", "李四", "28岁"), Person("a3", "王五", "21岁")))
EsSparkSQL.saveToEs(Spark.createDataset(rdd), esTableName)
rdd.map(p => {
  val put = new Put(Bytes.toBytes(p.id))
  put.addColumn(Bytes.toBytes(hbaseColumnNames), Bytes.toBytes("name"), Bytes.toBytes(p.name))
  put.addColumn(Bytes.toBytes(hbaseColumnNames), Bytes.toBytes("age"), Bytes.toBytes(p.age))
  (new ImmutableBytesWritable(), put)
}).saveAsHadoopDataset(jobConf)
```

画面2：
```scala
val hbaseTableName = "demo_coll"
```

画面3：
```scala
val Spark = EtlEnvironment.getSparkSession(this.getClass.getSimpleName, esTableName)
import Spark.implicits._
val sc = Spark.sparkContext
val hbaseTableName = "demo"
val hbaseColumnNames = "demo_coll"
```

画面4：
```bash
./shutdown_regionserver.rb
```

画面5：
```scala
val Spark = EtlEnvironment.getSparkSession(this.getClass.getSimpleName, esTableName)
import Spark.implicits._
val sc = Spark.sparkContext
val hbaseTableName = "demo"
val hbaseColumnNames = "demo_coll"
```

画面6：
```bash
scan 'demo'
```

画面7：
```bash
scan 'demo'
```

画面8：
```bash
scan 'demo'
```

画面9：
```scala
val Spark = EtlEnvironment.getSparkSession(this.getClass.getSimpleName, esTableName)
import Spark.implicits._
val sc = Spark.sparkContext
val hbaseTableName = "demo"
val hbaseColumnNames = "demo_coll"
```

画面10：
```scala
package cn.itcast.xc.analysis.demo
import cn.itcast.xc.analysis.common.EtEnvironment
import cn.itcast.xc.utils.HbaseUtils
import org.apache.Hadoop.hbase.client.Put
import org.apache.Hadoop.hbase.io.ImmutableBytesWritable
import org.apache.Hadoop.hbase.util.Bytes
import org.Elasticsearch.Spark.sql.EsSparkSQL
/*
 * @author
 * @date
 */
object Save {
  case class Person(id: String, name: String, age: String)
  def main(args: Array[String]): Unit = {
    // es 表名
    val esTableName = "demo/doc"
    val Spark = EtlEnvironment.getSparkSession(this.getClass.getSimpleName, esTableName)
    import Spark.implicits._
    val sc = Spark.sparkContext
    // hbase 表名
    val hbaseTableName = "demo"
  }
}
```

画面11：
```json
{
  "took": 45,
  "timed_out": false,
  "shards": {
    "total": 10,
    "successful": 10,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 3,
    "max_score": 1.0,
    "hits": [
      {
        "_index": "demo",
        "_type": "doc",
        "_id": "9409a860a89479832641",
        "_score": 1.0,
        "_source": {
          "id": "a1",
          "name": "张三",
          "age": "30岁"
        }
      },
      {
        "_index": "demo",
        "_type": "doc",
        "_id": "9409a860a89479832641",
        "_score": 1.0,
        "_source": {
          "id": "a2",
          "name": "李四",
          "age": "28岁"
        }
      },
      {
        "_index": "demo",
        "_type": "doc",
        "_id": "9409a860a89479832641",
        "_score": 1.0,
        "_source": {
          "id": "a3",
          "name": "王五",
          "age": "21岁"
        }
      }
    ]
  }
}
```

画面12：
```scala
val hbaseTableName = "demo_coll"
```

画面13：
```scala
val hbaseTableName = "demo_coll"
```

画面14：
```scala
val hbaseTableName = "demo_coll"
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面10：
- PPT 标题：1.2.1 代码演示
- 代码部分包含 package、import 语句和 case class Person。
- 代码中定义了 val esTableName = "demo/doc" 和 val hbaseTableName = "demo"。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

