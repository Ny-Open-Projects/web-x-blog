# 15-课程分析-课程购买量-DWM代码-保存到数据仓库&测试入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\15-课程分析-课程购买量-DWM代码-保存到数据仓库&测试入库_【海量资源尽在 666java.com】.mp4
- 时长 6分26秒（音频 387s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前边已经使用SparkCircle将咱们需要的结果获取到保存到这个编量中接下来咱们就需要将它持久化到数据仓库中咱们来编写持久化的代码首先还有一个是不要忘记就是一个报错的问题咱们需要将保存代码开启这个动态分区这个如果不配置的话
[00:30] 在保存的时候它会告诉你Hive的动态分区没有开启这个不允许保存这个配置完成之后呢接下来咱们就是具体的一个保存操作了这里呢为了防止小文件过多还是把分区修改为1接下来呢咱们的写入模式还是呢overwrite就是覆盖的模式然后呢
[01:02] 接下来就是咱们指定的表明以色彩银兔表明咱们这个表明还可以偷懒来点复制一下是DataCross下面的这应该是DWM为了保险期间咱们还是来确认一下DWM是对的保存完成之后呢按照惯例咱们还需要来到这里再查看一下咱们来到咱们的使用Spark call
[01:38] 使用Spark circle再进行查看一下查看咱们这个数据库怎么那个数据仓库是否保存成功这里直接售出来把它给打印到控制台上面那个售就把它给住掉就不输出了这里让程序抖起来把注释给加一下这个就是关联维度轻度集合关联维度轻度集合
[02:18] 轻度聚合这里呢是动态分区这里呢是设置分区修改分区这个呢是写入模式指定表明这个呢就是查看结果好度数写完呢咱们这里代码也已经跑完咱们呢还可以来到咱们的数据仓库使用HUE进行一个验证直接呢打开然后呢
[03:07] 这里点击simple进行数据的一个查看这里咱们约束的是9月23号的就是这里日期过滤是过滤的2019年9月23号的在咱们开发过程中咱们一般是使用测试所有的方式在咱们生产环境是需要指定日期进行一个过滤而且这个日期的获取是使用参数的方式获取这里先给它注掉
[03:34] 是使用参数的方式进行一个获取是咱们在生产环境但是呢咱们现在测试环境呢这个日期过滤之后呢你只有一天的数据咱们后边在业务表的一个操作的时候呢你获取的也是只有一天的一个数据所以说呢咱们这个地方把过滤条件给去掉这个呢是还是比较长的咱们呢注掉吧注射掉吧复制一份把这个给注射掉这个呢把过滤条件就给
[04:05] 就是VR之后的条件呢就给它删掉删掉之后呢咱们进行一个运行这个时候呢就会把所有的数据咱们事实表里边有的数据全部给处理了处理完成之后呢再次保存到数据仓库中这里呢咱们使用了使用模式是覆盖如果这个数据原来已经有了直接把用新的把老的给覆盖掉也不用担心数据重复的问题这里呢可以看到
[04:33] 程序呢正在读取根据这个日期呢进行一个读取所有的一个数据读取完成之后呢下面可以看到正在计算的这里是一个计算的一个操作好这个数据呢已经运行完成咱们来数据仓库来看一下还是刷新一下再进行一个查看这个时候呢咱们来看日期数据已经出来了它是2019年11月12号
[05:08] 然后呢这里是墨音是显示100条它是这个地方呢只显示100条咱们还可以使用查询的方式这个呢就可以干掉了把它给聚合一下control一下就是查看一下现在有多少条咱们呢from咱们的是dwm这个时候呢就可以执行了查询咱们当前这个课程购买量这个中间层就是dwm层现在有多少条数据
[05:41] 因为咱们现在的话是把所有的全部给清洗了看一下查询结果这里呢还在计算中3000多条也就是说呢所有的数据呢就是以课程为单位按天进行的一个轻度聚合这里呢有3000多条数据好咱们再切到文档这里呢咱们根据咱们的一个代码的一个编写以及咱们的一个最终的一个测试清洗测试
[06:10] 这里呢数据已经成功的保存到咱们的数据仓库中这里呢是可以看到的保存到数据仓库中之后呢咱们DWM层的一个清洗到这里呢就完成了好视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark SQL 将课程购买事实表按日期维度聚合后写入 Hive 数据仓库，并通过 Hue 查看结果。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Spark SQL 代码，定义了 buyDS DataFrame，包含从 fact 表中按日期维度聚合的销售数据，并使用 LEFT JOIN 连接维度表。
画面2：在代码中添加了设置动态分区模式的配置：Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")。
画面3：在代码中添加了 repartition 设置，并右键弹出菜单，显示可执行的选项。
画面4：在代码中添加了注释，说明使用的是 MySQL 作为底层数据库，并显示了 SparkSession 初始化的日志。
画面5：在代码中添加了写入模式为 overwrite，并显示了 Spark 任务启动和停止的日志。
画面6：在 Hue 的 Table Browser 中查看了 course_buy_dwm 表的数据样本，包含课程维度 ID、公司 ID、类别 ID、销售额等字段。
画面7：在代码中对 buyDS DataFrame 的字段进行了调整，移除了部分字段。
画面8：在代码中对 buyDS DataFrame 的字段进行了调整，移除了部分字段。
画面9：在代码中添加了写入模式为 overwrite，并显示了 Spark 任务启动和停止的日志。
画面10：在 Terminal 中显示了 Spark 任务执行过程中的日志，包括任务启动、完成和数据块传输等信息。
画面11：在 Hue 的 Table Browser 中查看了 course_buy_dwm 表的数据样本，包含课程维度 ID、公司 ID、类别 ID、销售额等字段。
画面12：在 Hue 的 Hive 编辑器中编写了 SQL 查询语句，用于查询 course_buy_dwm 表的数据。
画面13：在 Hue 的 Hive 编辑器中显示了 SQL 查询语句的执行结果，包括执行时间、查询语句和结果数据。
画面14：在 Hue 的 Table Browser 中查看了 course_buy_dwm 表的数据样本，包含课程维度 ID、公司 ID、类别 ID、销售额等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```scala
val buyDS = Spark.sql(
  """
    |SELECT
    |  a.course_dim_id,
    |  b.company_id,
    |  b.at_course_category_dim_id,
    |  a.sales,
    |  a.salesvolume,
    |  a.years, a.months, a.days
    |FROM
    |  (
    |    SELECT
    |      course_dim_id,
    |      sum(price) sales,
    |      count(course_id) salesvolume,
    |      years, months, days
    |    from data_course.course_buy_fact WHERE concat_ws('-', years, months, days) = '${date_info}'
    |    GROUP BY course_dim_id, years, months, days
    |  ) a
    |  LEFT JOIN data_dimen.course_dim b
    |  ON a.course_dim_id = b.course_dim_id
    |""".stripMargin.as(CourseBuyDWM)
)
```

画面2：
```scala
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")
```

画面3：
```scala
buyDS.repartition(numPartitions = 1)
```

画面4：
```scala
// 配置动态分区模式
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")
```

画面5：
```scala
// 配置动态分区模式
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")

buyDS.repartition(numPartitions = 1)
// 写入模式
.write.mode("overwrite")
.insertInto tableName = "data_course.course_buy_dwm"
```

画面6：
```sql
SELECT
  a.course_dim_id,
  b.company_id,
  b.at_course_category_dim_id,
  a.sales,
  a.salesvolume,
  a.years, a.months, a.days
FROM
  (
    SELECT
      course_dim_id,
      sum(price) sales,
      count(course_id) salesvolume,
      years, months, days
    from data_course.course_buy_fact WHERE concat_ws('-', years, months, days) = '${date_info}'
    GROUP BY course_dim_id, years, months, days
  ) a
  LEFT JOIN data_dimen.course_dim b
  ON a.course_dim_id = b.course_dim_id
```

画面7：
```scala
val buyDS = Spark.sql(
  """
    |SELECT
    |  a.course_dim_id,
    |  b.company_id,
    |  b.at_course_category_dim_id,
    |  a.sales,
    |  a.salesvolume,
    |  a.years, a.months, a.days
    |FROM
    |  (
    |    SELECT
    |      course_dim_id,
    |      sum(price) sales,
    |      count(course_id) salesvolume,
    |      years, months, days
    |    from data_course.course_buy_fact WHERE concat_ws('-', years, months, days) = '${date_info}'
    |    GROUP BY course_dim_id, years, months, days
    |  ) a
    |  LEFT JOIN data_dimen.course_dim b
    |  ON a.course_dim_id = b.course_dim_id
    |""".stripMargin.as(CourseBuyDWM)
)
```

画面8：
```scala
val buyDS = Spark.sql(
  """
    |SELECT
    |  a.course_dim_id,
    |  b.company_id,
    |  b.at_course_category_dim_id,
    |  a.sales,
    |  a.salesvolume,
    |  a.years, a.months, a.days
    |FROM
    |  (
    |    SELECT
    |      course_dim_id,
    |      sum(price) sales,
    |      count(course_id) salesvolume,
    |      years, months, days
    |    from data_course.course_buy_fact WHERE concat_ws('-', years, months, days) = '${date_info}'
    |    GROUP BY course_dim_id, years, months, days
    |  ) a
    |  LEFT JOIN data_dimen.course_dim b
    |  ON a.course_dim_id = b.course_dim_id
    |""".stripMargin.as(CourseBuyDWM)
)
```

画面9：
```scala
// 配置动态分区模式
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")

buyDS.repartition(numPartitions = 1)
// 写入模式
.write.mode("overwrite")
.insertInto tableName = "data_course.course_buy_dwm"
```

画面10：
```scala
INFO  TaskManager: Running task 138.0 in stage 3.0 (TD 104)
INFO  TaskManager: Finished task 138.0 in stage 3.0 (TD 104)
INFO  TaskManager: Starting task 131.0 in stage 3.0 (TD 104)
INFO  TaskManager: Finished task 131.0 in stage 3.0 (TD 104)
INFO  TaskManager: Starting task 132.0 in stage 3.0 (TD 104)
INFO  TaskManager: Finished task 132.0 in stage 3.0 (TD 104)
INFO  TaskManager: Starting task 135.0 in stage 3.0 (TD 104)
INFO  TaskManager: Finished task 135.0 in stage 3.0 (TD 104)
INFO  TaskManager: Starting task 134.0 in stage 3.0 (TD 104)
INFO  TaskManager: Finished task 134.0 in stage 3.0 (TD 104)
INFO  TaskManager: Starting task 133.0 in stage 3.0 (TD 104)
INFO  TaskManager: Finished task 133.0 in stage 3.0 (TD 104)
```

画面11：
```sql
SELECT
  a.course_dim_id,
  b.company_id,
  b.at_course_category_dim_id,
  a.sales,
  a.salesvolume,
  a.years, a.months, a.days
FROM
  (
    SELECT
      course_dim_id,
      sum(price) sales,
      count(course_id) salesvolume,
      years, months, days
    from data_course.course_buy_fact WHERE concat_ws('-', years, months, days) = '${date_info}'
    GROUP BY course_dim_id, years, months, days
  ) a
  LEFT JOIN data_dimen.course_dim b
  ON a.course_dim_id = b.course_dim_id
```

画面12：
```sql
SELECT
  a.course_dim_id,
  b.company_id,
  b.at_course_category_dim_id,
  a.sales,
  a.salesvolume,
  a.years, a.months, a.days
FROM
  (
    SELECT
      course_dim_id,
      sum(price) sales,
      count(course_id) salesvolume,
      years, months, days
    from data_course.course_buy_fact WHERE concat_ws('-', years, months, days) = '${date_info}'
    GROUP BY course_dim_id, years, months, days
  ) a
  LEFT

