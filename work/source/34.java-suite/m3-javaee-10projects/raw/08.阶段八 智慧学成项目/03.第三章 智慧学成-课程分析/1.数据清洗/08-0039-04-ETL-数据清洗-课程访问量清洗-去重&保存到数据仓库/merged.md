# 04-ETL-数据清洗-课程访问量清洗-去重&保存到数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\04-ETL-数据清洗-课程访问量清洗-去重&保存到数据仓库_【海量资源尽在 666java.com】.mp4
- 时长 10分28秒（音频 628s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来呢进行去虫的操作咱们这里呢这个就可以关掉了把这个菜单给转出来加个注释进行去虫进行去虫去虫的话咱们来看一下文档上去虫规则是什么呀根据它来去虫以天为单位的话咱们这个地方是不是每天的缓量了
[00:31] 其实这个DataInfo这个地方已经把这个天自动帮咱们过滤了过滤完了之后呢这个地方咱们直接进行去虫记录这里呢是根据Session以及咱们的IP加上课程ID进行一个去虫这里呢去虫使用Galaxy ProBi进行进行操作Galaxy ProBi呢这个地方还是需要一个变量因为咱们需要在里边写表达式变量呢其实就对应的是咱们这个对象
[01:03] cause we did it for it这个对象由于是他去重的也就是说他们三个只要是加起来只要是相同的就说明这个地方要忽略的一点是时间不管是什么时间只要是他这俩是这三个加起来是相同的就说明是重复的数据所以呢咱们这个地方就采用最原始的办法这个地方是session加上咱们的根据这个来写根据咱们这个
[01:37] 我这个上面这个去重的这个顺序来行然后另外一个是咱们的客厂ID其实呢这三个值的顺序是没有影响的这三个值的顺序是没有影响的你不管是谁在前谁在后都行Graphy Y完了之后呢得到是就是聚合后的值聚合后的值呢咱们最终要保存哪一个呢因为你
[02:08] 得到了之后它是有比如说有重复了它的session id和这个是有重复的它只是把它给拿出来了但是并没有进行一个选择信号操作我就是我需要哪个值我不需要哪个值咱们这里使用map进行一个过滤map进行过滤这个地方还叫x就行这个地方由于需要那个需要计算使用大块来进行一个计算
[02:40] 这个大括号应该是不需要的因为外层有了大括号这个就不需要了X呢这个地方我要求的值是啥呀我要求的是X因为咱们是进行一个去虫的过滤去虫的它的第二个值就是咱们的一个什么值呀就是一个个数值这个值呢进行一个排序就是mini by进行一个最小值的一个排序这个排完之后咱们取的是哪一个对着这个
[03:14] 这个来说假如说这个地方有重复的了我把它给粘出来假如说这个地方有重复的了我这一条有多行这条有多行为了区分我这个地方稍微来个换行这个时间呢是不是越大说明你访问的访问的时间是越晚越大访问的时间越晚咱们这个地方用mini呢mini by的意思就是说我只要时间小的
[03:44] 也就是说你什么时间来我这访问呢我是不是就要你这个什么时间小的呀这个地方呢咱们就用mini by就是取最小的就是你第一时间访问这个时间才算真的但是你后面同一个同一次绘画你又进行刷新了是后面的纸进行刷新的我后面的纸丢失我以先进来的这个纸为准这样所以说就用这个mini by这个时候呢咱们mini by的条件是什么呀
[04:14] 就是咱们的VZ time通过这个通过这个一个计算咱们就可以拿得到通过这个计算咱们就可以拿得到谁了就可以拿得到已经去虫之后的值去虫之后的值拿到之后其实它对于咱们来说这个地方已经结束了就是这些步骤已经结束了这个结束完了之后呢咱们就是进行一个保存操作这个呢把注释给简单的加一下
[04:49] 这个是首先进行的是分组加到这里边吧根据这三项进行分组分组完了之后呢这个组里边取访问时间最小的就是保留访问时间最早的值这个地方就是一个过滤最终呢这个地方就是得到了谁啊这个就换成一行吧得到了咱们
[05:38] 去重之后的值这个时候呢就是一个咱们去重之后的值就是VD这个地方其实还是在清洗操作如果还是清洗操作呢这个地方其实咱们这个变量可以不要这个变量其实可以不要让它继续点点完之后上面最终是不是得到一个VD的可怜呢这个是可以继续点的诶 站错了这个是继续点的点完之后最终
[06:08] 得到咱们清洗完的数据清洗完之后的数据呢咱们接下来进行一个保存操作加个注释进行进行保存进行保存这个时候呢咱们使用的是DataForm进行保存的使用呢Spark将数据转成DataForm这里先就是使用Crate的方式得到呢一个DataForm这个出不来出不来的话咱们就
[06:48] 手动到写这个地方呢变成了Dithomb就叫VitaDF这个时候呢就使用那个DF进行一个保存进行保存这个是加上转换为DF加上注释转换为DF转成DF之后呢进行保存到Hive保存到Hive之后呢为了防止小文件过多咱们把分区
[07:23] 咱们把分区改成改成一个这是阿姨他他这个时候呢把分区改成一分区改成一之后呢咱们进行一个写操作就是rat这里使用的model呢因为咱们是以天位单位进行分分析呢这里model直接是overrat就是直接是覆盖的因为咱们这里使用overrat的一个原因是啥呢w r i t e
[07:54] 使用overwrap一个原因是如果前面清晰可能有问题然后这边使用overwrap再次直接把它给覆盖掉就是全量清晰覆盖完了之后就直接就是最新的结果就是咱们需要的结果insert into这个时候它是一个保存到指定的表明咱们来看一下表明是啥切到咱们的HUE表明的话这个是在课程的课程的这个
[08:28] 库种,课程库,然后咱们是cosvdatacosvdata.feta,就这个,把这个给粘过来,这就是咱们保存的数据库名加表名保存完了之后呢接下来你要看是不是保存成功了,是不是咱们进行一个查询Spark.circle进行一个查询,这个时候呢少了一个语句,slash 行,直接
[09:05] 进行查询所有这个还不算完事咱们一定要把资源给关掉资源关闭资源这里咱们打开了两个资源一个是sc的这里就把它给停掉一个是Spark的Spark的就是cow子资源关了之后这个时候呢咱们程序已经写完把注释给补上这个呢就是进行保存指定表这个呢是
[09:53] 写入模式写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写写�

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Scala 编写 Spark 代码，对课程访问日志数据进行清洗、分组聚合，并最终写入 Hive 表。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 Scala 代码中对原始数据进行过滤（排除机器人）和按时间、区域、公司维度解析的逻辑。
画面 2: 展示了项目结构，并在文档中显示了“4.4.2 数据清洗分析”章节，其中包含一个清洗后字段映射表，列出了原始字段与清洗后字段的对应关系。
画面 3: 展示了代码中对数据进行 groupBy 和 map 操作，用于生成访问事实表的主键。
画面 4: 展示了 Hue 平台中访问日志文件的预览，显示了原始数据格式。
画面 5: 展示了代码中对数据进行 groupBy 和 map 操作，用于生成访问事实表的主键。
画面 6: 展示了代码中对数据进行 groupBy 和 map 操作，用于生成访问事实表的主键。
画面 7: 展示了代码中对数据进行 groupBy 和 map 操作，用于生成访问事实表的主键。
画面 8: 展示了代码中对数据进行 groupBy 和 map 操作，用于生成访问事实表的主键。
画面 9: 展示了代码中创建 DataFrame 并准备写入 Hive 表。
画面 10: 展示了代码中调用 repartition 方法对 DataFrame 进行分区。
画面 11: 展示了 Hue 平台中访问日志文件的预览，显示了原始数据格式。
画面 12: 展示了代码中创建 SparkSession 的上下文。
画面 13: 展示了代码中调用 writeInto 方法将 DataFrame 写入 Hive 表，并显示了 SQL 查询语句。
画面 14: 展示了代码中调用 writeInto 方法将 DataFrame 写入 Hive 表，并显示了 SQL 查询语句。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 1:
```scala
// 过滤机器人
.filter(arr => {
  !arr(5).contains("Robot")
})
// 平拆维度
.map(tmp => {
  // 格式化时间维度
  val time_dim = getDateTimeStr(tmp(6).tolog, pattern = "yyyy-MM-dd HH")
  // 格式化区域维度
  val area_dim = areaMap.get(getArea(tmp(3))).get
  // 格式化公司维度
  val com_dim = comMap.get(tmp(0)).get
  val ymd = time_dim.split("-")
  CourseVisitFact(getId(), tmp(0), time_dim, area_dim, com_dim, tmp(2), tmp(3), tmp(5), tmp(6).tolog, ymd(0), ymd(1), ymd(2))
})
```

画面 2:
```markdown
| 清洗前字段 | 清洗后字段 | 清洗后字段名 |
| --- | --- | --- |
| course_id | 课程ID | course_dim_id |
| company_id | 公司ID | company_dim_id |
| visit_time | 访问时间 | visit_time |
```

画面 3:
```scala
visitClean.groupBy(x => {
  x.client_sessionid + x.client_ip + x.course_dim_id
}).map {
  x =>
  x._2.minBy {
    _._visit_time
  }
}
```

画面 4:
```
8fcd04a49f1c01d8a8b3eac806071c
8377f6fa8db83ec1925887cf03249968
192.168.1.56 56d1ba61b16
0.3994.78 Safari/5.36 1572861998051
```

画面 5:
```scala
visitClean.groupBy(x => {
  x.client_sessionid + x.client_ip + x.course_dim_id
}).map {
  x =>
  x._2.minBy {
    _._visit_time
  }
}
```

画面 6:
```scala
visitClean.groupBy(x => {
  x.client_sessionid + x.client_ip + x.course_dim_id
}).map {
  x =>
  x._2.minBy {
    _._visit_time
  }
}
```

画面 7:
```scala
visitClean.groupBy(x => {
  x.client_sessionid + x.client_ip + x.course_dim_id
}).map {
  x =>
  x._2.minBy {
    _._visit_time
  }
}
```

画面 8:
```scala
visitClean.groupBy(x => {
  x.client_sessionid + x.client_ip + x.course_dim_id
}).map {
  x =>
  x._2.minBy {
    _._visit_time
  }
}
```

画面 9:
```scala
val visitDF = Spark.createDataFrame(visitClean)
```

画面 10:
```scala
visitDF.repartition(1)
```

画面 11:
```
8fcd04a49f1c01d8a8b3eac806071c
8377f6fa8db83ec1925887cf03249968
192.168.1.56 56d1ba61b16
0.3994.78 Safari/5.36 1572861998051
```

画面 12:
```scala
val Spark = SparkSession.builder()
  .appName("course_visit_analysis")
  .config("Spark.sql.warehouse.dir", "hdfs://nameservice1:8020/user/Hive/warehouse")
  .config("Spark.serializer", "org.apache.Spark.serializer.KryoSerializer")
  .config("Spark.sql.adaptive.enabled", "true")
  .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
  .config("Spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
  .config("Spark.sql.adaptive.enabled", "true")
  .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
  .config("Spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
  .config("Spark.sql.adaptive.enabled", "true")
  .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
  .config("Spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
  .getOrCreate()
```

画面 13:
```scala
visitDF.write.mode("overwrite").insertInto("data_course.course_visit_fact")
```

画面 14:
```scala
sql("select * from data_course.course_visit_fact")
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 2: PPT 标题为“4.4.2 数据清洗分析”，其中包含一个表格，列出了清洗前字段、清洗后字段和清洗后字段名。
画面 12: 展示了 SparkSession 的构建配置，包括应用名称、仓库目录、序列化器、自适应查询优化等配置项。

5) 无。

