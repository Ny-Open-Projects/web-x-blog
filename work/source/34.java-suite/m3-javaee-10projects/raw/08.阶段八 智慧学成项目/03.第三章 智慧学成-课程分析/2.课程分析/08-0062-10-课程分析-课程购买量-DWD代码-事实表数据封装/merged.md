# 10-课程分析-课程购买量-DWD代码-事实表数据封装

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\10-课程分析-课程购买量-DWD代码-事实表数据封装_【海量资源尽在 666java.com】.mp4
- 时长 15分57秒（音频 958s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续。
[00:02] 维度数据获取完成之后,接下来就是要获取原始数据,进行一个数据的清洗操作。
[00:10] 咱们来看原始数据,它的数据库以及它的表明。
[00:14] 咱们是在DataCourse中,原始数据就是这张表,咱们来复制一个表明。
[00:22] 这里由于数据是在Hive中,咱们可以直接使用Spark Circle进行一个获取。
[00:32] 加个注释,这是呢获取原始数据使用呢Spark Circle这里呢是Sled From这个From咱们的订单的一个原始数据但是呢咱们是离线分析是分析昨天的时间这里呢需要一个日期的一个筛选咱们呢在这个地方有一个Data Infer但是我不确定咱们这个数据是有哪天的咱们就来查看一下
[01:13] 咱们这个数据呢是有哪天的数据咱们测试的时候呢先指定日期进行一个查看这个呢是航秒值这个是航秒值它不方便观看咱们可以去买Circle中进行一个查看9月10月11月都有这里呢就选一个日期吧就是2019年11月13号这个是随机选的一个日期2019年
[01:49] 11月13号然后呢接下来就是咱们过滤条件的一个编写这里呢咱们使用vr唯一和时间有关系的呢就是咱们的这个字单订单时间这里呢订单时间呢又不能直接的使用订单时间又不能直接使用咱们呢需要使用Hive提供的一个工具进行一个编写这不是进行一个编写进行一个过滤
[02:19] 这里呢咱们使用的是unixfrom unix timef2o m e f2o m 没有 e然后unixin x time这里呢给它一个括号咱们需要一个原始的一个时间咱们原始时间呢就是order timeor d a time然后呢接下来是它的时间格式这里呢用单引号时间格式呢咱们就是y y i
[02:51] YYYMM-VD这是咱们的一个时间格式转换成之后的时间呢咱们需要和水进行匹配啊咱们是不是要让它等于咱们的DataInfo呀这里加一个$大符号就是咱们的DataInfo有了DataInfo之后呢这个时候咱们过滤时间过滤呢就完成了时间过滤完成之后呢咱们还需要一个操作就是需要把它给转成什么呀
[03:22] 转成咱们后续编好操作的一个格式这里先把它给转成实体转成实体之后再把它给转成一个集合咱们后边用的时候比较方便咱们coscours1咱们cosorderSource数据也是有的ordr提示已经出来了
[03:51] 这个呢实体也是有的转换成它之后呢咱们把它再转换成一个集合C是小写Ccollectcollect转换成它之后呢前边这个就比较长了咱们可以在这加一个换行转换成它之后呢咱们前面需要一个变量来进行一个接收咱们呢这个变量是课程购买量的就是cost咱们接下来是购买量就叫buy
[04:22] 是原数据source档号加上原数据获取之后呢接下来就是咱们筛选条件的一个编写这里呢咱们不是筛选条件啊说错了这里是维度的一个关联咱们进行维度的关联这里呢直接使用map算子给它一个变量这里呢是一个对象就叫object obj在这个里边呢进行维度的一个关联操作
[05:01] 咱们首先是存时间维度时间维度这个地方val然后是时间维度tme dim时间维度的id等于咱们是有一个getdata s72是时间工具类这个由于它不会自动的打包咱们需要来复制一下它全路径然后把它手动给导入进来
[05:31] 这里是咱们的课程购买量手动把它给导入进来import把它粘进来这个时候就可以使用get data st2咱们时间维度是order咱们是order time这个时候order time需要把它给转成一个什么值转换成一个浪形因为咱们需要的一个毫秒值最终需要的毫秒值但是这个地方order time它获取的是啥
[06:01] 它获取的是时间传因为买色后获取过来之后它是一个时间传咱们乘以1000让它变成一个毫秒值变成毫秒值之后咱们接下来的就是咱们的格式咱们的时间维度ID的格式是小写的y y y-mm-dd-h这就是咱们时间维度的ID我来确认一下
[06:29] 咱们前面也写过一次咱们看一下是两个H还是一个H记不太清了时间维度的ID两个H这个时候呢就是如果是9点的话就是09好时间维度ID有了之后呢接下来是啥接下来就是区域维度ID区域维度ID的话咱们其实前面已经有经验了就是在这个地方区域维度ID它呢可能会出现什么情况呢可能会出现
[07:01] 这个IP呢不在咱们的数据仓库中这个时候呢就要加一个try cache了咱们呢首先给它一个变量v2然后呢就叫区域ID给它一个默认值是-1就是说找不到的情况下我就让它是-1接下来呢咱们就是正常的一个编写前边呢已经有一个error map了这里呢通过map呢咱们是使用get的方法get方法呢在使用的时候
[07:33] 咱们是这个地方是有用户的ID咱们呢直接使用IP嗯还在分布着行咱们呢是可以使用IP工具类IPUtils然后呢直接是使用get error的方法然后通过ID来获取它这个程式的名称咱们呢IP呢又是通过咱们的用户的ID来获取的这个地方呢是user
[08:01] 小写的u啊小写的u user map点get了他一个k这个地方呢他是一个opt的还需要一个get这个地方也先把它给写上嗯嗯多了在这呢嗯他get的时候呢是获取的是咱们的用户就是obj点用户的iduser id通过他呢他可以获取到用户的ip有了用户的ip之后呢这个地方咱们就可以进行一个获取获取之后呢他是一个optr的
[08:32] 咱们需要用get获取具体的值但是这个地方可能会有一个什么值可能会有一个异常就是说我这个值在咱们这个IP在咱们的数据仓库中并没有所以说这个地方加一个try catch这里就是case这个异常可以处理也可以不处理咱们因为是知道这种情况的然后异常就不处理然后直接异常也无需要不需要打印这是加个注释
[09:03] 这是时间维度这个呢是区域维度接下来呢还有咱们的公司维度以及咱们的分区年月日这里呢这里呢咱们继续就是分区的年月日最后吧先来写公司公司的维度吧公司维度呢是通过公司的这个map可以获取它呢使用get的是谁啊
[09:41] 咱们来看一下公司维度是课程的ID课程的ID呢咱们课程ID是不是在那个数组里边啊不是数组不是数组是在JSON里边咱们来切过来课程ID是不是在这里边呢所以说咱们还要解析这个JSON解析这个JSON呢获取ITMIDITMID呢就是咱们的课程ID这里呢咱们加个注释
[10:11] 是获取公司维度公司维度公司维度它这个地方是需要的是用户的不是用户的ID课程的ID课程的ID又在json中又在json中json咱们还在写写写json这里使用first的json这里是json大写的json使用part的json然后pass json array
[10:45] s pass json array 得到呢咱们的json数组json数组呢咱们知道这个地方呢是只有一个值的obj.get咱们呢是不是get是点然后是details就是详情这个地方呢get json object咱们呢这个地方只有一个值咱们是确定它只有一个值呢所以说所以是0这个地方呢就得到json的object嗯不能进行变量的这个自动化咱们就手动的写
[11:15] 然后json得到具体的json值之后咱们就可以通过json来获取咱们的什么咱们的课程ID这个地方是get string k得到咱们的课程ID这个它的变量名是叫做itemid把它给粘过来复制一下itemid获取了之后这个地方点get一下get一下
[11:45] 最终呢就得到了谁啊得到了咱们的公司ID有了公司ID之后呢咱们维度相关的数据就完成了接下来呢咱们就是分区年月日分区的数据的获取年月日分区这里呢咱们已经有维度ID了这里呢维度ID是用横杠来分割的咱们呢直接split然后
[12:17] 横杠得到一个YMD的一个数组YMD得到这个之后咱们选012前三个值就行了接下来就是数据的一个封装咱们有一个coscosFETCUUR2SE有一个FETcosH5cosByH5ToFET不是这个咱们应该是有一个cosByBUYFACT
[12:53] 是有这样一个实体了crossback fate没有的话咱们来导看能不能导到OK导入过来了这个实体呢就可以进行直接的封装它是在咱们实体这个包里面是存在的咱们呢根据它的一个数据结构首先呢是订单ID首先呢是订单的订单ID然后课程的ID这一系列的一个封装咱们从第一个开始
[13:26] 订单ID就是obj.otherid,other number第二个就是咱们的客栈ID客栈ID是在json里边的gs.get它还是stringk它是叫做itemID这个数字封装结构比较清晰一点接下来是时间维度的ID就是timeID
[14:00] 接下来呢是记不太清了咱们把这个给打开然后呢把它给切过来时间维度的ID之后呢是区域维度ID区域维度的ID咱们也有了区域维度ID完了之后呢是公司维度ID是comma ID公司维度ID之后呢就是价格价格的话就是obg.press接下来呢是状态obg.stace
[14:33] 接下来呢是用户ID用户ID呢咱们用户ID是在哪获取的用户ID用户ID用户ID直接在OBG里边有OBG.userID有了用户ID之后呢看下一个是啥用户ID接下来就是分区年月日了这就是YMD0嗯这个地方为什么报错了YMD哦这个地方少了一个逗号
[15:16] 我说怎么报错了然后呢最后一个干掉一二好到此呢咱们这个数据的封装就完成了数据封装完成之后呢前边就可以给它一个变量进行一个接收咱们呢就是一个这是一个clean的clean的谁呀cos c o u r s e咱们by到此咱们这个数据的一个清理的一个封装就完成了清理封装完成之后呢
[15:49] 咱们的视频就先到这里后边呢就是一个保存到数据仓库中的一个操作好视频就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark SQL 从 Hive 表中读取订单数据，并通过 Scala 代码进行数据转换和映射，最终生成事实表 CourseBuyFact。

2) 按时间顺序列出每张画面的要点：
画面1：展示 IDEA 中的 Scala 代码，定义了用户维度、区域维度和课程维度的映射逻辑，以及从 Hive 表 data_course.course_orders_source 中读取数据的 SQL 语句。
画面2：展示 Hue 界面中 data_course.course_orders_source 表的数据，显示了订单号、价格、状态等字段。
画面3：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面4：展示 IDEA 中的 Scala 代码，定义了 CourseOrdersSource 的数据结构和映射方法。
画面5：展示 IDEA 中的 Scala 代码，定义了 SparkSession 和数据处理的日期信息。
画面6：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面7：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面8：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面9：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面10：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面11：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面12：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面13：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。
画面14：展示 IDEA 中的 Scala 代码，定义了数据处理的日期信息和 SQL 查询语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```scala
def main(args: Array[String]): Unit = {
  import Spark.implicits._
  // 用户维度
  var userMap = Map[String, String]()
  Spark.sql("select * from data_dimen.user_dim").as[UserDim].collect().map(x => {
    userMap += (x.user_id -> x.id)
  })
  // 区域维度
  var areaMap = Map[String, String]()
  Spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDim].collect().map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
  // 课程维度
  var courseMap = Map[String, String]()
  Spark.sql("SELECT * FROM data_dimen.course_dim").as[CourseDim].collect().map(x => {
    if (x.course_dim_id != null && x.company_id != null) {
      courseMap += (x.course_dim_id.toString -> x.company_id.toString)
    }
  })
  // 日期信息
  val data_info = "2019-11-13"
  // 读取数据
  Spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
}
```

画面2：
```sql
SELECT * FROM data_course.course_orders_source
```

画面3：
```scala
val data_info = "2019-11-13"
val courseSource = Spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面4：
```scala
case class CourseOrdersSource(
  order_number: String,
  course_orders_source_price: Float,
  course_orders_source_status: String,
  course_orders_source_order_time: String,
  course_orders_source_order_id: String,
  course_orders_source_user_id: String
)
```

画面5：
```scala
val Spark = SparkSession.builder().appName("CourseBuyByHiveToFact").config("Spark.sql.catalogImplementation", "Hive").getOrCreate()
val sc = Spark.sparkContext
val data_info = args(0)
```

画面6：
```scala
val data_info = "2019-11-13"
val courseSource = Spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面7：
```scala
val data_info = "2019-11-13"
val courseSource = Spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面8：
```scala
val data_info = "2019-11-13"
val courseSource = Spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面9：
```scala
val data_info = "2019-11-13"
val courseSource = Spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面10：
```scala
val data_info = "2019-11-13"
val courseSource = Spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面11：
```scala
val data_info = "2019-11-13"
val courseSource = Spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面12：
```scala
val data_info = "2019-11-13"
val courseSource = Spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面13：
```scala
val data_info = "2019-11-13"
val courseSource = Spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

画面14：
```scala
val data_info = "2019-11-13"
val courseSource = Spark.sql("select * from data_course.course_orders_source where from_unixtime(order_time, 'yyyy-MM-dd') = '" + data_info + "'")
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

