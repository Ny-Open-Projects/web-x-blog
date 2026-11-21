# 15-热门学科排名-统计分析-销售量-周-代码-抽取工具类&测试入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\15-热门学科排名-统计分析-销售量-周-代码-抽取工具类&测试入库_【海量资源尽在 666java.com】.mp4
- 时长 5分14秒（音频 315s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好咱们继续前边呢已经将统计分析的代码编写完成接下来呢就是测试环节就是针对咱们编写的代码进行一个测试但是测试之前呢这个地方为了提高咱们代码的附用性这个地方需要抽取一个工具类抽取工具类的原因是什么呢就是咱们咱们回到代码说咱们这一块呢就是获取周的数据还有计算奖服这个的话咱们其实在这个地方操作和周有关系吗
[00:30] 就是根据上面计算的日期然后根据日期区间进行一个计算进行一个数据的获取然后计算它和周期是没有太大的关系的咱们呢就把这块的代码进行一个抽取抽取完成之后呢咱们后边还有月的一个统计月的一个数据获取月的一个涨幅的一个计算这块代码就是可以附用的咱们呢接下来就是对代码的一个抽取抽取呢咱们是抽取到这个工具类内咱们呢每个
[01:00] 这次这个认为学会排名呢每一个统计分析都有代码一个抽取学生人数的销售量的以及销售额的咱们现在做的是谁啊咱们现在做的是销售量的一个统计咱们呢直接就把这个代码给抽取到这个工具类中以便咱们后取后期咱们统计月的时候好进行一个复用好咱们呢直接把这块代码给粘过来粘过来之后呢这个报销先不管他等会呢咱们使用工具类然后直接进行一个
[01:33] 数据的一个查询这里呢把它给粘过来之后这个时候就行了因为呢Spark它有一个好处是啥呀这个地方是不用直接写返回值的你这个查询结果是啥它就自动把你给返回了返回之后呢咱们直接就是调用这个方法就行这里呢咱们需要将这个方法给引入一下copy这个地方呢引泡它一下引泡它
[02:03] 有了它之后引入了之后咱们这里就可以直接使用这个时候呢它需要的参数咱们把它给提供一下就行了这里需要的参数谁呀需要的参数是咱们的Spark这里呢将Spark给它接下来它需要的谁呀接下来它需要的是当前的周以及呢上周这个因为是之前这个地方已经写好了咱们来对比一下对比一下第一个参数Spark好有第二个参数
[02:36] 是current就是咱们当前的第三个参数是last上头这个有了之后呢这个就OK了咱们这个地方就代码量就比较少了等于一行代码直接把这个数据给查过来然后进行一个转换咱们后期在统计月的时候这个代码就不用写了因为它是根据区间进行一个获取的咱们只用获取月的期间把日期给传过来后面呢就可以直接进行一个使用查询使用然后统计它一个增幅咱们工具类抽取完成之后呢
[03:06] 咱们接下来就是一个测试就是测试咱们使用工具列的方式咱们这里呢数据是否是正常的然后呢还要查看咱们的数据是否能保存到咱们的数据库中就是咱们的数据仓库中这里不是数据库是数据仓库咱们来运行代码咱们来切到咱们的数据仓库数据仓库呢是这个咱们当前是轴这里直接查看它吧右键open不到2
[03:38] 这里呢目前分区里边还没有数据说明数据还没有写成哦这个查看CNN跑它也没有任何数据咱们这里就等待它执行完成好这里呢控制台已经输出了结果说明它已经执行完成这里呢咱们来这里刷新一下来HUE刷新看HUE上是否可以查到数据了走起好HUE呢也正常的查到了数据这个地方呢已经将数据给查清出来
[04:12] 咱们这个地方由于是根据咱们的州进行的一个数据的统计它呢没有办法没有办法就是直接将所有的数据直接给过滤出来因为咱们这个地方Gertrude拜的时候是根据什么呀根据日期区间然后进行的一个Gertrude拜如果统计所有的话它就没有这个州的一个概念了所以说咱们后期在展示的时候咱们后期在展示的时候也就是说你传的日期是多少
[04:42] 传的日期是多少然后你这个地方得到的结果就是哪一周的一个具体的一个数据咱们这个地方测试已经完成咱们认为学科排名销售量周的统计也到此完成通过学习咱们根据咱们的清洗步骤一步步的将数据获取然后计算两幅最终将结果保存到咱们的数据仓库中好咱们视频也留到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark 中编写 SQL 代码，对课程销售数据按周进行统计分析，并将结果写入 Hive 表中，最后在 Hue 中验证数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构和代码目录，当前选中“3.5.1.1.3 工具类”章节，右侧显示 `SubjectSalesVolumeByWeekBiz` 类的代码，包含导入语句和初始化 SparkSession。
画面2：在 `SubjectSalesVolumeByWeekBiz` 类中，展示 `val date_info = "2019-09-25"` 和 `val weeks = getWeekRelativelyInterval(date_info).split(regex = ";")` 的代码，以及 `Spark.sql` 的 SQL 语句，该语句包含 `LEFT JOIN` 和 `WHERE` 条件。
画面3：展示 `SubjectUtils.scala` 文件中的 `def subjectBuyCountSql(Spark: SparkSession, current: Array[String], last: Array[String]): Unit = { }` 方法定义。
画面4：在 `SubjectUtils.scala` 中，展示 `subjectBuyCountSql` 方法的 SQL 语句，包含 `SELECT`、`FROM`、`WHERE` 和 `LEFT JOIN` 子句。
画面5：在 `SubjectUtils.scala` 中，展示 `def subjectLearningSql(Spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame = { }` 方法定义。
画面6：在 `SubjectSalesVolumeByWeekBiz` 类中，展示 `val weekOfYear = getWeekOfYear(current(0)).split(regex = ";")` 和 `val sIdS = Spark.sql` 的代码。
画面7：在 `SubjectUtils.scala` 中，展示 `def subjectLearningSql` 方法的 SQL 语句，包含 `SELECT`、`FROM`、`WHERE` 和 `LEFT JOIN` 子句。
画面8：展示 `subjectBuyCountSql` 方法的完整 SQL 语句，包含 `SELECT`、`FROM`、`WHERE` 和 `LEFT JOIN` 子句。
画面9：在 `SubjectSalesVolumeByWeekBiz` 类中，右键点击代码，弹出菜单，选择“Paste from History”。
画面10：在 `SubjectSalesVolumeByWeekBiz` 类中，执行代码后，终端显示任务提交和成功完成的日志。
画面11：在 `SubjectSalesVolumeByWeekBiz` 类中，终端显示 Hive 表创建和数据写入的日志。
画面12：在 Hue 界面中，显示 `data_subject.subject_sale_week_biz` 表，提示“该表不包含任何数据”。
画面13：在 `SubjectSalesVolumeByWeekBiz` 类中，展示 `Spark.sql` 的代码，用于查询表数据。
画面14：展示开发中查询结果，表格包含列：`course_category_dim_id`、`course_category_name`、`sale_num`、`sale_percent`、`years`、`week_of_year`，并显示了部分数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```scala
package cn.itcast.xc.analysis.subject.salesvolume

import cn.itcast.xc.common.ELTEnvironment
import cn.itcast.xc.entity.SubjectSaleWeekBiz
import cn.itcast.xc.utils.DateUtils.{getWeekNum, getWeekRelativelyInterval}
import cn.itcast.xc.utils.SubjectUtils.subjectBuyCountSql
import org.apache.Spark.sql.SparkSession

object SubjectSalesVolumeByWeekBiz {
  /**
    * 初始化参数
    */
  val Spark: SparkSession = ELTEnvironment.getSparkSession(this.getClass.getSimpleName)
```

画面2：
```scala
val date_info = "2019-09-25"
val weeks = getWeekRelativelyInterval(date_info).split(regex = ";")
val current = weeks(0).split(regex = ";")
val last = weeks(1).split(regex = ";")

Spark.sql(
  s"""
     |SELECT a.course_category_dim_id, course_category_dim_id, a.sale_sum sale_num,
     |ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
     |FROM (
     |(SELECT course_category_dim_id, sum(salesvolume) sale_num
     |FROM data_course.course_buy_dwm
     |WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
     |GROUP BY course_category_dim_id) as a
     |LEFT JOIN (
     |(SELECT course_category_dim_id, sum(salesvolume) sale_num
     |FROM data_course.course_buy_dwm
     |WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
     |GROUP BY course_category_dim_id) as b
     |ON a.course_category_dim_id = b.course_category_dim_id
     |""".stripMargin
)
```

画面3：
```scala
def subjectBuyCountSql(Spark: SparkSession, current: Array[String], last: Array[String]): Unit = {
  // todo
}
```

画面4：
```scala
def subjectBuyCountSql(Spark: SparkSession, current: Array[String], last: Array[String]): Unit = {
  Spark.sql(
    s"""
       |SELECT a.course_category_dim_id, course_category_dim_id, a.sale_sum sale_num,
       |ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
       |FROM (
       |(SELECT course_category_dim_id, sum(salesvolume) sale_num
       |FROM data_course.course_buy_dwm
       |WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
       |GROUP BY course_category_dim_id) as a
       |LEFT JOIN (
       |(SELECT course_category_dim_id, sum(salesvolume) sale_num
       |FROM data_course.course_buy_dwm
       |WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
       |GROUP BY course_category_dim_id) as b
       |ON a.course_category_dim_id = b.course_category_dim_id
       |""".stripMargin
  )
}
```

画面5：
```scala
def subjectLearningSql(Spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame = {
  // todo
}
```

画面6：
```scala
val weekOfYear = getWeekOfYear(current(0)).split(regex = ";")
val sIdS = Spark.sql
```

画面7：
```scala
def subjectLearningSql(Spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame = {
  Spark.sql(
    s"""
       |SELECT a.course_category_dim_id, course_category_dim_id, a.sale_sum sale_num,
       |ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
       |FROM (
       |(SELECT course_category_dim_id, sum(salesvolume) sale_num
       |FROM data_course.course_buy_dwm
       |WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
       |GROUP BY course_category_dim_id) as a
       |LEFT JOIN (
       |(SELECT course_category_dim_id, sum(salesvolume) sale_num
       |FROM data_course.course_buy_dwm
       |WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
       |GROUP BY course_category_dim_id) as b
       |ON a.course_category_dim_id = b.course_category_dim_id
       |""".stripMargin
  )
}
```

画面8：
```scala
def subjectBuyCountSql(Spark: SparkSession, current: Array[String], last: Array[String]) = {
  Spark.sql(
    s"""
       |SELECT a.course_category_dim_id, course_category_dim_id, a.sale_sum sale_num,
       |ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
       |FROM (
       |(SELECT course_category_dim_id, sum(salesvolume) sale_num
       |FROM data_course.course_buy_dwm
       |WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
       |GROUP BY course_category_dim_id) as a
       |LEFT JOIN (
       |(SELECT course_category_dim_id, sum(salesvolume) sale_num
       |FROM data_course.course_buy_dwm
       |WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
       |GROUP BY course_category_dim_id) as b
       |ON a.course_category_dim_id = b.course_category_dim_id
       |""".stripMargin
  )
}
```

画面9：
无代码内容，仅显示右键菜单。

画面10：
```scala
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")
sIdS.repartition(numPartitions = 3)
write.mode = "overwrite"
.writeInto(tableName = "data_subject.subject_sale_week_biz")
Spark.sql(sqlText = "select * from data_subject.subject_sale_week_biz").show()
```

画面11：
```scala
Spark.conf

