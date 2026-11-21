# 画面线理解：12即时查询-统计分析-步骤1：代码-关联相关维度&统计学习时长

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\12即时查询-统计分析-步骤1：代码-关联相关维度&统计学习时长_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:05, 04:47, 05:42, 06:59, 08:17, 09:13, 10:04, 10:37, 11:19, 12:34, 13:06, 13:30, 13:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:00:45

1) 这一组画面整体在讲如何在 Spark 中编写代码，通过读取原始数据、注册 UDF、进行 SQL 查询和聚合，最终生成用户学习中间表（DWM层）。

2) 按时间顺序列出每张画面的要点：
画面1：
- 代码：val sc = spark.sparkContext
- 代码：val date_info = args(0)
- 代码：val learnSource = sc.textFile(path = s"/user/hive/external/data_course/learning_course_online_source/${date_info}")
- 代码：val learnSourceRDD = learnSource.map(_.split("\t").map(arr => {
  UserLearnOnline(arr(0), arr(1), arr(2), arr(3), arr(4), arr(5).toLong)
}))
- 代码：spark.createDataFrame(learnSourceRDD, createdReplaceTempView(viewName = "learn_source_tmp")

画面2：
- 代码：spark.sql(
  select
  user_id,
  course_id,
  course_video_id,
  min(learn_time) learn_time,
  count(1) learn_count_tmp
  from learn_source_tmp
  group by user_id, course_id, course_video_id, user_session_id
  left join data_dimen.course_dim cv on cv.course_dim_id = 1.course_video_id
  left join data_dimen.user_dim u on u.user_dim_id = 1.user_id
  ***.stripMargin)
- 代码：spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")

画面3：
- 代码：spark.sql(
  select
  getUuid() learning_course_online_id,
  course_id,
  course_video_id,
  user_id,
  learn_time,
  min(learn_time) learn_time,
  count(1) learn_count_tmp
  from learn_source_tmp
  group by user_id, course_id, course_video_id, user_session_id
  left join data_dimen.course_dim cv on cv.course_dim_id = 1.course_video_id
  left join data_dimen.user_dim u on u.user_dim_id = 1.user_id
  ***.stripMargin)

画面4：
- PPT标题：3.1.2 中间表结构
- 表格内容：
  | 用户学习中间表字段 | 源数据字段 | 字段说明 |
  | --- | --- | --- |
  | learning_course_online_id | - | 用户学习id, uuid生成 |
  | course_id | 通过course_id关联 | 课程维度id |
  | course_name | 通过course_id关联 | 课程名称 |
  | video_name | 通过course_video_id关联 | 视频名称 |
  | user_id | user_id | 用户维度id |
  | user_name | 通过user_id关联 | 用户名 |
  | learn_time | learn_time | 学习时间 |
  | learn_count | 通过learn_time计算 | 学习时长 |
  | date_info | 通过learn_time格式化 | yyyy-MM-dd格式日期 |

画面5：
- 界面：Hue File Browser，显示路径 /user/hive/external/data_course/learning_course_online_source/2019-12-11
- 表格：显示文件列表，包含两个文件：259f88c4a4194ab98c0b78f0d98b7e0 和 d55b9f3611d4abe97533d701252f6e4a

画面6：
- PPT标题：3.1.2 中间表结构
- 表格内容：
  | 用户学习中间表字段 | 源数据字段 | 字段说明 |
  | --- | --- | --- |
  | learning_course_online_id | - | 用户学习id, uuid生成 |
  | course_id | 通过course_id关联 | 课程维度id |
  | course_name | 通过course_id关联 | 课程名称 |
  | video_name | 通过course_video_id关联 | 视频名称 |
  | user_id | user_id | 用户维度id |
  | user_name | 通过user_id关联 | 用户名 |
  | learn_time | learn_time | 学习时间 |
  | learn_count | 通过learn_time计算 | 学习时长 |
  | date_info | 通过learn_time格式化 | yyyy-MM-dd格式日期 |

画面7：
- PPT标题：3.1.2 中间表结构
- 表格内容：
  | 用户学习中间表字段 | 源数据字段 | 字段说明 |
  | --- | --- | --- |
  | learning_course_online_id | - | 用户学习id, uuid生成 |
  | course_id | 通过course_id关联 | 课程维度id |
  | course_name | 通过course_id关联 | 课程名称 |
  | video_name | 通过course_video_id关联 | 视频名称 |
  | user_id | user_id | 用户维度id |
  | user_name | 通过user_id关联 | 用户名 |
  | learn_time | learn_time | 学习时间 |
  | learn_count | 通过learn_time计算 | 学习时长 |
  | date_info | 通过learn_time格式化 | yyyy-MM-dd格式日期 |

画面8：
- 代码：spark.sql(
  select
  getUuid() learning_course_online_id,
  course_id,
  course_video_id,
  user_id,
  learn_time,
  min(learn_time) learn_time,
  count(1) learn_count_tmp
  from learn_source_tmp
  group by user_id, course_id, course_video_id, user_session_id
  left join data_dimen.course_dim cv on cv.course_dim_id = 1.course_video_id
  left join data_dimen.user_dim u on u.user_dim_id = 1.user_id
  ***.stripMargin)

画面9：
- 界面：Navicat Premium，显示数据库结构，选中表 xc_user

画面10：
- 界面：Hue File Browser，显示路径 /user/hive/external/data_course/learning_course_online_source/2019-12-11
- 表格：显示文件列表，包含两个文件：259f88c4a4194ab98c0b78f0d98b7e0 和 d55b9f3611d4abe97533d701252f6e4a

画面11：
- PPT标题：3.1.2 中间表结构
- 表格内容：
  | 用户学习中间表字段 | 源数据字段 | 字段说明 |
  | --- | --- | --- |
  | learning_course_online_id | - | 用户学习id, uuid生成 |
  | course_id | 通过course_id关联 | 课程维度id |
  | course_name | 通过course_id关联 | 课程名称 |
  | video_name | 通过course_video_id关联 | 视频名称 |
  | user_id | user_id | 用户维度id |
  | user_name | 通过user_id关联 | 用户名 |
  | learn_time | learn_time | 学习时间 |
  | learn_count | 通过learn_time计算 | 学习时长 |
  | date_info | 通过learn_time格式化 | yyyy-MM-dd格式日期 |

画面12：
- 代码：val tableLane = "data_course.learning_course_online_dwm"
- 代码：userLearnDF
- 代码：.repartition(numPartitions = 1)

画面13：
- 代码：object InstantQueryStepToDw {
  val spark: SparkSession = ITIEnvironment.getSparkSession(this.getClass.getSimpleName, null)
  def main(args: Array[String]): Unit = {
    // 1. 建立Spark中数据源
    val sc = spark.sparkContext
    val date_info = args(0)
    val learnSource = sc.textFile(path = s"/user/hive/external/data_course/learning_course_online_source/${date_info}")
    val learnSourceRDD = learnSource.map(_.split("\t").map(arr => {
      UserLearnOnline(arr(0), arr(1), arr(2), arr(3), arr(4), arr(5).toLong)
    }))
    // 创建临时表
    spark.createDataFrame(learnSourceRDD, createdReplaceTempView(viewName = "learn_source_tmp")

画面14：
- 代码：spark.sql(
  select
  cv.video_name video_name,
  1.user_id,
  1.learn_time,
  minConvertDayHourMin(learn_count_tmp) learn_count,
  from_unixtime(1.learn_time, 'yyyy-MM-dd') date_info
  from (
    select
    user_id,
    course_id,
    course_video_id,
    learn_time,
    count(1) learn_count_tmp
    from learn_source_tmp
    group by user_id, course_id, course_video_id, user_session_id
    left join data_dimen.course_dim cv on cv.course_dim_id = 1.course_video_id
    left join data_dimen.user_dim u on u.user_dim_id = 1.user_id
    ***.stripMargin)
- 代码：spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
- 代码：val tableLane = "data_course.learning_course_online_dwm"
- 代码：userLearnDF
- 代码：.repartition(numPartitions = 1)
