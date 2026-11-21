# 11-课程分析-课程购买量-DWD代码-保存到数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\11-课程分析-课程购买量-DWD代码-保存到数据仓库_【海量资源尽在 666java.com】.mp4
- 时长 4分7秒（音频 247s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 咱们继续40秒的封装40秒数据的封装呢已经完成接下来呢就是保存到数据仓库中这里呢我把这个也关了这个呢少了一个注释给加上就是封装维度数呃封装40秒数据40秒数据这个呢稍微有点长看着还是比较丑的给它稍微格次化一下这样呢就数据就稍微美观了一点接着呢咱们就使用这个
[00:33] 清洗后的试试表这个变量咱们呢把它给保存到咱们的数据仓库中但是呢具体的保存之前呢咱们还需要一个操作就是把它给转成一个DataForm因为呢DataForm呢方便咱们的一个保存CREATECREATEDataForm这个又写错了这个不是用它CREATE的这个呢转换成DataForm呢要需要使用Spark
[01:05] 我说怎么点不出来呢carry to datafarm这里呢把它丢给他刚才呢按错快捷键了就是把它单过来之后呢然后直接跳到这来了这是按错快捷键的一个操作这个时候呢给他一个变量他就是呢by然后是df因为呢他是一个datafarmf大写吧有了这个值之后呢加个变量吧加个注释吧就是转换成df转换为
[01:40] df方便方便保存找完它之后呢咱们就可以保存操作了但是还有一点不要忘了咱们已经呢遇到过一个措施保存的时候呢使用Spark代码直接保存的时候呢它需要把hi5的动态分区给开起来就是允许hi5的动态分区咱们呢来找一下hi5动态分区的代码带过来
[02:10] 将来之后呢这个就可以关掉了咱们呢允许害物的一个动态分区允许动态分区之后呢接下来咱们就可以进行相应的一个保存操作这里呢直接进行一个保存操作首先呢把它的分区改为一个因为呢这样的话就不会有那个小文件不会有很多小文件接下来呢是咱们的写入模式写入模式呢还是咱们的
[02:40] overwrite就是覆盖Writ overwriteWrit写反了写入模式完了之后呢就是咱们指定咱们要写入的表明insert into这个表明呢其实还是稍微有点长的咱们来一起写它data cost然后呢是cost c u r s ebuy这是咱们可能购买量相关的然后放到f act
[03:18] 保存完之后呢咱们还有一条不要忘了就是我不确定我这个保存是真的成功了还是假成功了然后呢进行一个查询这里呢就是查询这张表slide 星from这张表然后呢售一下就是在空台进行一个打印写完之后呢咱们代码自始至终还没有进行一个测试接下来呢就是
[03:51] 进行测试的一个工作进行测试呢咱们交到交给下一个视频好咱们呢保存以上呢就是保存到咱们数据仓库中的一个代码代码编写完成之后呢咱们视频就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark SQL 和 DataFrame API 对课程购买和访问数据进行清洗、转换和写入事实表。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了课程购买事实表的 Scala 代码，包含从 JSON 提取数据、解析时间戳、构造 CourseBuyFact 对象并写入数据。
画面2: 代码中对时间戳进行拆分，构造 CourseBuyFact 对象，并调用 Spark.createDataFrame。
画面3: 代码中定义了课程购买数据源的 SQL 查询，用于从数据库中提取数据。
画面4: 代码中调用 Spark.createDataFrame，传入 CourseBuy 对象，并设置 Spark 配置。
画面5: 代码中调用 Spark.createDataFrame，传入 CourseBuy 对象，并设置 Spark 配置。
画面6: 代码中调用 Spark.createDataFrame，传入 CourseBuy 对象，并设置 Spark 配置。
画面7: IDE 中打开搜索框，准备搜索代码或类。
画面8: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。
画面9: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。
画面10: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。
画面11: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。
画面12: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。
画面13: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。
画面14: 展示了课程访问事实表的 Scala 代码，包含从数据库中提取数据、构造 VisitSourceTotal 对象并写入数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```scala
try {
  areaMap.get(implicit getAreaMap.get(obj.user_id).get).get
} catch {
  case _ =>
}
// 公司维度
val json = JSON.parseArray(obj.details).getJSONObject(index = 8)
val con2d = courseMap.get(json.getString(key = "item_id")).get
// 年月日维度
val ymd = time_dim_id.split(regex = "-")
CourseBuyFact(obj.order_number,
  json.getString(key = "item_id"),
  time_dim_id, areaId,
  con2d, obj.price,
  obj.status, obj.user_id,
  ymd(0), ymd(1), ymd(2)
)
```

画面2:
```scala
// 年月日维度
val ymd = time_dim_id.split(regex = "-")
CourseBuyFact(obj.order_number,
  json.getString(key = "item_id"),
  time_dim_id, areaId,
  con2d, obj.price,
  obj.status, obj.user_id,
  ymd(0), ymd(1), ymd(2)
)
```

画面3:
```scala
val courseBuySource = courseSource.map(obj => {
  val time_dim_id = getDateTimeStr(obj.order_time, long = 1000, pattern = "yyyy-MM-dd HH")
  // 年月日维度
  val ymd = time_dim_id.split(regex = "-")
  CourseBuyFact(obj.order_number,
    json.getString(key = "item_id"),
    time_dim_id, areaId,
    con2d, obj.price,
    obj.status, obj.user_id,
    ymd(0), ymd(1), ymd(2)
  )
})
```

画面4:
```scala
Spark.createDataFrame(CleanCourseBuy)
```

画面5:
```scala
Spark.createDataFrame(CleanCourseBuy)
```

画面6:
```scala
Spark.createDataFrame(CleanCourseBuy)
```

画面7:
无代码。

画面8:
```scala
val buyOF = Spark.createDataFrame(CleanCourseBuy)
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")
buyOF.repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
Spark.sql(sqlText = "select * from data_course.course_buy_fact").show()
```

画面9:
```scala
val buyOF = Spark.createDataFrame(CleanCourseBuy)
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")
buyOF.repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
Spark.sql(sqlText = "select * from data_course.course_buy_fact").show()
```

画面10:
```scala
val buyOF = Spark.createDataFrame(CleanCourseBuy)
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")
buyOF.repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
Spark.sql(sqlText = "select * from data_course.course_buy_fact").show()
```

画面11:
```scala
val buyOF = Spark.createDataFrame(CleanCourseBuy)
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")
buyOF.repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
Spark.sql(sqlText = "select * from data_course.course_buy_fact").show()
```

画面12:
```scala
val buyOF = Spark.createDataFrame(CleanCourseBuy)
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")
buyOF.repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
Spark.sql(sqlText = "select * from data_course.course_buy_fact").show()
```

画面13:
```scala
val data_info = "2019-11-11"
val cleanCourseBuy = courseSource.map(obj => {
  val time_dim_id = getDateTimeStr(obj.order_time, long = 1000, pattern = "yyyy-MM-dd HH")
  // 年月日维度
  val ymd = time_dim_id.split(regex = "-")
  CourseBuyFact(obj.order_number,
    json.getString(key = "item_id"),
    time_dim_id, areaId,
    con2d, obj.price,
    obj.status, obj.user_id,
    ymd(0), ymd(1), ymd(2)
  )
})
```

画面14:
```scala
val buyOF = Spark.createDataFrame(CleanCourseBuy)
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")
buyOF.repartition(numPartitions = 1)
  .write.mode(saveMode = "overwrite")
  .insertInto(tableName = "data_course.course_buy_fact")
Spark.sql(sqlText = "select * from data_course.course_buy_fact").show()
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

