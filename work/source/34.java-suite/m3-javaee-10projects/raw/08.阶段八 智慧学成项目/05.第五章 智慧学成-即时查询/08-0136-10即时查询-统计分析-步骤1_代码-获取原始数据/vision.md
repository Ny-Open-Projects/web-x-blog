# 画面线理解：10即时查询-统计分析-步骤1：代码-获取原始数据

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\10即时查询-统计分析-步骤1：代码-获取原始数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:34, 00:50, 01:13, 01:29, 02:37, 03:13, 03:19, 03:46, 04:13, 04:37, 04:48, 05:46, 06:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:58:45

1) 这一组画面整体在讲如何使用 Spark 读取 HDFS 上的用户学习行为原始数据，并将其转换为结构化的 DataFrame，最终写入 Hive 表中。

2) 按时间顺序列出每张画面的要点：
画面1: 显示 Scala 代码，定义 SparkSession，读取 HDFS 数据并写入 Hive 表，设置 Hive 参数。
画面2: 代码中高亮显示写入 Hive 表的 SQL 语句 `insertInto("s${tableLame}")`。
画面3: 代码中高亮显示 SparkSession 的创建语句 `val sc = spark.sparkContext`。
画面4: 代码中高亮显示 SparkSession 的创建语句 `val sc = spark.sparkContext`。
画面5: 显示 Hue 文件浏览器界面，展示 HDFS 上的目录结构，其中包含多个事实表文件夹。
画面6: 代码中高亮显示读取 HDFS 数据的路径 `val learnSource = sc.textFile(...)`。
画面7: 显示 PPT 页面，标题为“3.1 步骤1:关联维度统计分析”，子标题“3.1.1 统计逻辑”。
画面8: 显示 PPT 页面，标题为“1.4 ODS数据存储分析-用户学习”，内容包括数据存储格式、存储方式和内容格式。
画面9: 代码中高亮显示对读取的数据进行解析和转换的逻辑 `learnSource.map(...)`。
画面10: 显示两个 Scala 文件，分别是 `InstantQueryStepToHive.scala` 和 `Courses.scala`，后者定义了 `UserOnline` 和 `LearningCourseOnlineIndex` 案例类。
画面11: 显示 PPT 页面，标题为“1.3.2 ODS层数据结构-用户学习”，包含一个表格，列出了采集字段、字段说明和数据格式。
画面12: 代码中高亮显示对数据进行转换的逻辑 `case class UserOnline(...)`。
画面13: 代码中高亮显示读取 HDFS 数据的路径 `val learnSource = sc.textFile(...)`。
画面14: 代码中高亮显示创建 Hive 表并写入数据的语句 `spark.createDataFrame(...).createReplaceTempView(...)`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1:
```scala
object InstantQueryStepToHive {
  // 初始化 SparkSession
  val spark: SparkSession = EtlEnvironment.getSparkSession(this.getClass.getSimpleName, etlTableName = null)

  def main(args: Array[String]): Unit = {
    // 获取 SparkContext
    val sc = spark.sparkContext

    // 1. 根据入口HDFS中原始数据路径
    // 2. 关联相关维度表
    // 3. 算计学习时长
    // 4. 存在数据集全表
    // 假设Hive参数
    spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")

    // 中间表
    val tableLame = "data_course.learning_course_online_dam"
    userLearnDS
    .repartition(1)
    .write.mode("overwrite")
    // 插入表
    .insertInto("s${tableLame}")
  }
```

画面2:
```scala
    .write.mode("overwrite")
    // 插入表
    .insertInto("s${tableLame}")
```

画面6:
```scala
    val date_info = "2019-12-11"
    val learnSource = sc.textFile(s"/user/hive/external/data_course/learning_course_online_source/${date_info}")
```

画面9:
```scala
    val learnSource = learnSource.map(_split(regx = "\t")).map(err => {
      UserOnline(err(0), err(1), err(2), err(3), err(4), err(5), err(6).toLong)
    })
```

画面12:
```scala
case class UserOnline(user_id: String,
                      course_id: String,
                      course_video_id: String,
                      user_session_id: String,
                      user_agent: String,
                      learn_time: Long)
```

画面14:
```scala
    spark.createDataFrame(learnSourceRDD).createReplaceTempView(viewName = "learn_source_tmp")
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面7:
标题：3 统计分析
子标题：3.1 步骤1:关联维度统计分析
子子标题：3.1.1 统计逻辑
内容：
1. 根据入口HDFS中获取原始数据
2. 关联相关维度表
3. 统计学习时长
4. 保存到数据仓库中

画面8:
标题：1.4 ODS数据存储分析-用户学习
内容：
数据存储格式：hdfs 文本文件
数据存储方式：每天的数据以 年/月/日 为目录名，每天的数据存储在一个目录中，如：`/user/hive/external/data_course/learning_course_online_source/${now}(format:yyyy-MM-dd)`
数据内容格式：
- 数据分隔符：\t
- 数据换行符：\n
数据样例：
```
ch8dd0387fa59412d990448cc7f04b0c
92e64dffce36/4d00aa31b02486d281305
Chrome 1570500691
```

画面11:
标题：1.3.2 ODS层数据结构-用户学习
表格：
| 采集字段 | 字段说明 | 数据格式 |
| :--- | :--- | :--- |
| user_id | 用户id，根据是否有值，可判断是否为访客 | uuid |
| course_id | 课程id，根据课程id可以做更多的分析，如热门课程等 | uuid |
| course_video_id | 视频id，可对视频维度关联排名 | uuid |
| user_ip | 用户ip，可分析用户所在区域 | ipv4 |
| user_session_id | 用户会话id，每打开一个页面就会产生一个会话id，关联浏览器 | uuid |
| user_agent | 浏览器标识，可判断用户访问方式及是否是机器人 | 浏览器ua |

5) 无。
