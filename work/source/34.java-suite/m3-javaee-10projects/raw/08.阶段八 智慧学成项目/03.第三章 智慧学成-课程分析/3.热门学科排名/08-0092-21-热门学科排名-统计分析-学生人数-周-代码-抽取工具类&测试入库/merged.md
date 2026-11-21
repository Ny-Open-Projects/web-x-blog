# 21-热门学科排名-统计分析-学生人数-周-代码-抽取工具类&测试入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\21-热门学科排名-统计分析-学生人数-周-代码-抽取工具类&测试入库_【海量资源尽在 666java.com】.mp4
- 时长 5分31秒（音频 331s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前边呢,咱们已经将代码写完,接下来呢,就是咱们的一个测试环节,但是呢,在测试开始之前,咱们呢,需要对工具类进行一个抽取,不知道大家是否还记得,咱们在热门学科排名中的销售量的一个统计分析的时候,咱们对销售量进行的一个抽取,当时呢,就说了,咱们会对学生人数还有销售额都会做工具类的一个抽取。
[00:28] 这里呢,咱们现在已经到了这个学生人数的一个统计,接下来呢,就是对学生人数的一个工具类的一个抽取。
[00:37] 这个地方咱们还是再多说一嘴,因为这个日期呢,和周其实没有太大的关系,咱们只是在上面根据咱们的日期获取了周的一个区间,获取周的一个区间之后呢,周的开始时间和周的结束时间,这都是具体的一个日期。
[00:55] 但是并没有体现到周咱们月呢也是一样的所以说这段代码就能构成一个附用咱们周的时候传周的日期期间月的时候传月的日期期间相同的道理都能根据这个日期期间呢来获取数据进行一个增幅的一个就是涨幅的一个计算咱们呢就把这段代码进行一个工具类的一个抽取这个呢少复制了一个这个呢直接把它给粘过来
[01:27] 这个完成之后呢咱们这个工具类其实呢就算已经抽取好了因为这些参数咱们前面是准备好的准备好了这个地方呢你只用对它进行一个代码过来进行一个调用就行了因为咱们测试过这张代码是OK的这个呢咱们对它进行一个调用这个地方是中文的括号改成英文的这个呢需要一个打包操作咱们呢把它给复制一下
[01:58] 导进来这个时候他需要的参数咱们给他就行了首先呢第一个是斯巴克第二个呢是当前周的区间他是一个数组接下来呢是上一周的区间也是一个数组就是咱们的拉斯塔给他完成之后呢咱们这个就是调用工具列的方式来获取咱们的周的数据还有计算奖服就完成了咱们后期使用月的时候也是相同的方式这个完成之后呢咱们
[02:31] 就可以对代码进行一个测试了咱们右键运行代码这里呢咱们使用HUE也进行一个查看咱们来切到HUE的这个数据视图这个时候呢来查看咱们的数据目前表中还没有任何数据咱们来切回开发工具这里呢是因为还没有执行完成所以说咱们没有数据等待它执行完成这里呢执行需要一定的时间我把这个视频呢稍微暂停一下
[03:03] 好咱们继续这里呢已经控制台输出了结果说明咱们程序已经运行完成咱们来咱们呢一起右翼来查看一下数据刷新还没有咱们再次刷新这个地方没有数据可能就是数据还没有查询过来好这里呢数据已经过来这个时候呢咱们已经看到第40周2019年的第40周这里呢它的涨幅都是100%都是1.0
[03:36] 咱们的number这些都有数据咱们这个地方之前就是前面在测试的时候就是选的是日期选的是10月1日这个日期10月1号这个日期咱们当时就是为了测试咱们抽取的工具类中的衣服闹是否好使接下来咱们把日期给修改一下改成咱们的11月11号这个时候数据多一点咱们再来看咱们的一个结果走起
[04:06] 这个呢它执行还是需要一定的时间咱们再稍微暂停一下好咱们继续这里呢已经根据咱们新传的日期11月份不是11月份啊11月11号这个日期呢计算了它当前周和上上周的一个就是具体的数据以及它的涨幅这里呢控制台已经打印出来结果咱们来HUE刷一下刷新咱们来切到新跑这个地方呢
[04:36] 上面是咱们40周的一个数据下边呢就是咱们45周的一个数据这个数据呢已经保存在数据库里边而且呢这个数据相对于前面的数据呢数据量多了一点这个涨幅呢也有改变好咱们来切到文档到此呢咱们学生人数认为学科排名中的学生人数按周统计咱们已经完成从咱们的获取时间开始到最终的保存结果咱们最终也测试完成
[05:07] 这里呢通过学习你需要掌握根据咱们的这个视频将热门学科排名中学生人数按周进行统计并且呢能将咱们的这个统计后的结果保存到数据仓库中好咱们按周统计呢就到此结束视频呢也到底到这里就结束

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark 中编写 SQL 代码，通过动态分区和模板替换生成数据表，并在 Hive 中查看结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Scala 代码，定义了 `weekOfYear`、`learnDS`，并编写了 SQL 查询语句，包含 `LEFT JOIN` 和 `cast` 函数，用于计算用户占比和年周数。
画面2：展示 Scala 代码，定义了 `subjectLearnCountSql` 函数，编写了嵌套的 SQL 查询，用于计算课程类别维度下的销售金额和用户数。
画面3：展示 Scala 代码，定义了 `subjectLearnSql` 函数，编写了 SQL 查询，包含 `LEFT JOIN` 和 `WHERE` 条件，用于计算用户占比和年周数。
画面4：展示 Scala 代码，定义了 `subjectLearnSql` 函数，编写了 SQL 查询，包含 `LEFT JOIN` 和 `WHERE` 条件，用于计算用户占比和年周数。
画面5：展示 Scala 代码，定义了 `subjectLearnSql` 函数，编写了 SQL 查询，包含 `LEFT JOIN` 和 `WHERE` 条件，用于计算用户占比和年周数。
画面6：展示 Scala 代码，定义了 `subjectLearnSql` 函数，编写了 SQL 查询，包含 `LEFT JOIN` 和 `WHERE` 条件，用于计算用户占比和年周数。
画面7：展示 Scala 代码，定义了 `subjectLearnSql` 函数，编写了 SQL 查询，包含 `LEFT JOIN` 和 `WHERE` 条件，用于计算用户占比和年周数。
画面8：展示终端窗口，显示 Spark 应用程序提交成功，日志显示 Spark 版本和安全权限设置。
画面9：展示 Hue 界面，显示 `subject_user_week_biz` 表，提示“该表不包含任何数据”。
画面10：展示终端窗口，显示 Spark SQL 查询结果，包含课程类别、用户数、用户占比和年周数。
画面11：展示终端窗口，显示 Spark 任务执行日志，包括任务提交、执行和完成状态。
画面12：展示终端窗口，显示 Spark SQL 查询结果，包含课程类别、用户数、用户占比和年周数。
画面13：展示 Hue 界面，显示 `subject_user_week_biz` 表的数据，包含课程类别、用户数、用户占比和年周数。
画面14：展示文档页面，显示 `SubjectLearnUserWeekBiz` 的 Scala 类定义和相关代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```scala
val weekOfYear = getMonthNum(current(8)).split(regex = "-")
val learnDS = Spark.sql(
  """
    |select
    |  a.course_category_dim_id,
    |  b.name course_category_name,
    |  cast(a.user_num as int) user_num,
    |  cast(a.user_percent as float) user_percent,
    |  ${weekOfYear(0)} years,
    |  ${weekOfYear(1)} week_of_year
    |from learn_biz_tmp a
    |left join data_dimen.course_category_dim b
    |on a.course_category_dim_id = b.course_category_dim_id
    |""".stripMargin
)
```

画面2：
```scala
def subjectLearnCountSql(Spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame = {
  Spark.sql(
    """
      |SELECT a.course_category_dim_id, a.sale_num sale_num,
      |       ifnull(a.user_num/b.sale_num, 1.0) sale_percent
      |FROM (
      |  SELECT a.course_category_dim_id, sum(sale_volume) sale_num
      |  FROM data_course.course_buy_dim
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${current(0)}' AND '${current(1)}'
      |  GROUP BY course_category_dim_id
      |) a
      |LEFT JOIN (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.course_buy_dim
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${last(0)}' AND '${last(1)}'
      |  GROUP BY course_category_dim_id
      |) b
      |ON a.course_category_dim_id = b.course_category_dim_id
      |""".stripMargin
  )
}
```

画面3：
```scala
val subjectLearnSql = (Spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame => {
  Spark.sql(
    """
      |SELECT a.course_category_dim_id, a.user_num,
      |       ifnull(a.user_num/b.user_num, 1.0) as user_percent
      |FROM (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${current(0)}' AND '${current(1)}'
      |  GROUP BY course_category_dim_id
      |) a
      |LEFT JOIN (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${last(0)}' AND '${last(1)}'
      |  GROUP BY course_category_dim_id
      |) b
      |ON a.course_category_dim_id = b.course_category_dim_id
      |""".stripMargin
  )
}
```

画面4：
```scala
val subjectLearnSql = (Spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame => {
  Spark.sql(
    """
      |SELECT a.course_category_dim_id, a.user_num,
      |       ifnull(a.user_num/b.user_num, 1.0) as user_percent
      |FROM (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${current(0)}' AND '${current(1)}'
      |  GROUP BY course_category_dim_id
      |) a
      |LEFT JOIN (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${last(0)}' AND '${last(1)}'
      |  GROUP BY course_category_dim_id
      |) b
      |ON a.course_category_dim_id = b.course_category_dim_id
      |""".stripMargin
  )
}
```

画面5：
```scala
val subjectLearnSql = (Spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame => {
  Spark.sql(
    """
      |SELECT a.course_category_dim_id, a.user_num,
      |       ifnull(a.user_num/b.user_num, 1.0) as user_percent
      |FROM (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${current(0)}' AND '${current(1)}'
      |  GROUP BY course_category_dim_id
      |) a
      |LEFT JOIN (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${last(0)}' AND '${last(1)}'
      |  GROUP BY course_category_dim_id
      |) b
      |ON a.course_category_dim_id = b.course_category_dim_id
      |""".stripMargin
  )
}
```

画面6：
```scala
val subjectLearnSql = (Spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame => {
  Spark.sql(
    """
      |SELECT a.course_category_dim_id, a.user_num,
      |       ifnull(a.user_num/b.user_num, 1.0) as user_percent
      |FROM (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${current(0)}' AND '${current(1)}'
      |  GROUP BY course_category_dim_id
      |) a
      |LEFT JOIN (
      |  SELECT course_category_dim_id, count(user_dim_id) user_num
      |  FROM data_course.learning_course_fact
      |  WHERE concat_ws('-',years,months, days) BETWEEN '${last(0)}' AND '${last(1)}'
      |  GROUP BY course_category_dim_id
      |) b
      |ON a.course_category_dim_id = b.course_category_dim_id
      |""".stripMargin
  )
}
```

画面7：
```scala
val subjectLearnSql = (Spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame => {
  Spark.sql(
    """
      |SELECT a.course_category_dim_id, a.user_num,
      |       ifnull(a.user_num/b.user_num,

