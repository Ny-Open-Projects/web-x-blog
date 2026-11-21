# 画面线理解：04-ETL-数据清洗-课程访问量清洗-去重&保存到数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\04-ETL-数据清洗-课程访问量清洗-去重&保存到数据仓库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:28, 02:24, 03:19, 04:07, 04:40, 05:48, 06:08, 07:03, 07:27, 08:19, 08:52, 09:30, 10:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:51:25

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
val visitDF = spark.createDataFrame(visitClean)
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
val spark = SparkSession.builder()
  .appName("course_visit_analysis")
  .config("spark.sql.warehouse.dir", "hdfs://nameservice1:8020/user/hive/warehouse")
  .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
  .config("spark.sql.adaptive.enabled", "true")
  .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
  .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
  .config("spark.sql.adaptive.enabled", "true")
  .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
  .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
  .config("spark.sql.adaptive.enabled", "true")
  .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
  .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")
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
