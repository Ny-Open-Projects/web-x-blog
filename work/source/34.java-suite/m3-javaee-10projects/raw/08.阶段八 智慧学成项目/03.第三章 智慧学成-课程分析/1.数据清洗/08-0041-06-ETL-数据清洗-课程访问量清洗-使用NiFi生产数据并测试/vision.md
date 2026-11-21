# 画面线理解：06-ETL-数据清洗-课程访问量清洗-使用NiFi生产数据并测试

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\06-ETL-数据清洗-课程访问量清洗-使用NiFi生产数据并测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:51, 02:56, 04:11, 04:31, 05:26, 06:23, 06:58, 08:01, 09:55, 12:33, 13:33, 14:52, 15:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:53:11

1) 这一组画面整体在讲如何通过 NiFi 流程生成模拟数据并写入 HDFS，同时展示 Spark 代码对数据进行清洗和写入 Hive 的过程。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 NiFi 调用流程图，包含 QueryDatabaseTable → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → ReplaceText → ExecuteScript → PutHDFS。
画面2: NiFi 界面，显示“课程访问量流程”流程组。
画面3: NiFi 界面，显示流程中各处理器的运行状态和数据量。
画面4: IntelliJ IDEA 中的 Spark 代码，定义了输入路径和 SparkContext。
画面5: IntelliJ IDEA 中的 Spark 代码，显示了读取的数据内容。
画面6: IntelliJ IDEA 中的 Spark 代码，显示了时间维度处理逻辑。
画面7: IntelliJ IDEA 中的 Spark 代码，显示了数据写入 Hive 的日志。
画面8: IntelliJ IDEA 中的 Spark 代码，显示了时间维度处理逻辑。
画面9: Hue 文件浏览器界面，弹出确认删除文件的对话框。
画面10: IntelliJ IDEA 中的 Spark 代码，显示了数据过滤和填充逻辑。
画面11: Hue 查询界面，显示了表结构和查询历史。
画面12: 本地终端界面，显示了 Spark 作业的执行日志。
画面13: Hue 查询界面，显示了 SQL 查询语句。
画面14: 文档页面，标题为“5.6 再次测试清洗代码”，并提示参考“文档 4.4.4 测试章节”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4:
```scala
val sc = spark.sparkContext
val date_info = "2019-11-07"
val input = sc.textFile(path = s"/user/hive/external/data_course/visit_source/${date_info}")
```

画面5:
```scala
1121.248.185.185 185.4040866 45v1 446
151.256.1.115 1.4040866 45v1 446
134.8.1.1 1.4040866 45v1 446
137.138.43.21 1.4040866 45v1 446
187.17.138.186 1.4040866 45v1 446
112.117.79.89 1.4040866 45v1 446
```

画面6:
```scala
val time_dim = getDateTime(tmp).toLong * 1000, pattern = "yyyy-MM-dd HH"
var area_dim = "-1"
try {
  area_dim = areaMap.get(getArea(tmp(3))).get
} catch {
  case e => e.printStackTrace()
}
```

画面7:
```scala
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,06]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,07]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,08]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,09]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,10]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,11]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,12]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,13]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,14]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,15]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,16]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,17]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,18]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,19]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,20]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,21]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,22]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,23]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,24]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,25]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,26]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,27]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,28]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,29]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,11,30]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,01]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,02]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,03]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,04]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,05]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,06]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,07]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,08]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,09]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,10]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,11]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,12]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,13]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,14]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,15]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,16]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,17]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,12,18]
INFO HiveMetastore: get partition with auth: db-data_course tbl-course_visit_fact [2019,
