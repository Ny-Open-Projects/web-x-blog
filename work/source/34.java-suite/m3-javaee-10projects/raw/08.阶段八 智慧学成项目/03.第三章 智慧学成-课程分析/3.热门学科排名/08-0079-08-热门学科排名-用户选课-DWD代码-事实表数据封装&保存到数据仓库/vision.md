# 画面线理解：08-热门学科排名-用户选课-DWD代码-事实表数据封装&保存到数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\08-热门学科排名-用户选课-DWD代码-事实表数据封装&保存到数据仓库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:20, 00:41, 01:25, 01:47, 01:57, 02:21, 03:27, 03:31, 04:24, 05:38, 05:44, 05:54, 06:39, 06:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:15:17

1) 这一组画面整体在讲如何在 Spark 中通过 SQL 和 DataFrame API 对用户学习数据进行处理，包括数据读取、时间转换、结构化映射和写入 Hive 表。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 UserLearnSourceToFact.scala 中，定义了 Spark SQL 查询语句，从 data_course.learning_course_source 表中选择数据，条件为 from_unixtime(choose_time, 'yyyy-MM-dd') = '2019-11-11'。
画面 2: 在 UserLearnSourceToFact.scala 中，对 learnSource.map(obj) 进行了注释，说明其作用是“用户维度”。
画面 3: 在 UserLearnSourceToFact.scala 中，使用 map 方法对数据进行转换，调用 get(obj.course_id) 获取课程ID。
画面 4: 在 UserLearnSourceToFact.scala 中，定义了变量 timeId，用于存储时间戳转换后的值。
画面 5: 在 DateUtils.scala 文件中，右键点击 def getDays 方法，弹出上下文菜单。
画面 6: 在 UserLearnSourceToFact.scala 中，定义了变量 timeId，用于存储时间戳转换后的值。
画面 7: 在 Course.scala 文件中，右键点击 LearningCourseFact 类，选择“Split and Move Down”操作。
画面 8: 在 UserLearnSourceToFact.scala 中，定义了变量 catId 和 timeId，用于存储课程ID和时间戳转换后的值。
画面 9: 在 Course.scala 文件中，高亮显示了 LearningCourseFact 类的字段，包括 course_category_dim_id、user_id、time_dim_id、status、years、months、days。
画面 10: 在 UserLearnSourceToFact.scala 中，定义了变量 ymd，用于存储时间戳转换后的年、月、日。
画面 11: 在 VisitSourceToFact.scala 文件中，定义了变量 visitDF，用于创建 DataFrame。
画面 12: 在 VisitSourceToFact.scala 文件中，定义了变量 visitDF，用于创建 DataFrame。
画面 13: 在 UserLearnSourceToFact.scala 文件中，定义了变量 learnFact，用于创建 DataFrame。
画面 14: 在 UserLearnSourceToFact.scala 文件中，定义了变量 learnFact，用于创建 DataFrame。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 1:
```scala
val date_info = "2019-11-11"
val learnSource = spark.sql(s"SELECT * from data_course.learning_course_source WHERE from_unixtime(choose_time, 'yyyy-MM-dd') = '${date_info}'")
```

画面 3:
```scala
val courseMap = Map[String, String]()
courseMap += ("course_id" -> "course_id")
courseMap += ("course_name" -> "course_name")
courseMap += ("course_category_id" -> "course_category_id")
courseMap += ("course_status" -> "course_status")
courseMap += ("course_start_time" -> "course_start_time")
courseMap += ("course_end_time" -> "course_end_time")
courseMap += ("course_price" -> "course_price")
courseMap += ("course_desc" -> "course_desc")
courseMap += ("course_cover" -> "course_cover")
courseMap += ("course_video_url" -> "course_video_url")
courseMap += ("course_video_duration" -> "course_video_duration")
courseMap += ("course_video_play_count" -> "course_video_play_count")
courseMap += ("course_video_comment_count" -> "course_video_comment_count")
courseMap += ("course_video_like_count" -> "course_video_like_count")
courseMap += ("course_video_dislike_count" -> "course_video_dislike_count")
courseMap += ("course_video_share_count" -> "course_video_share_count")
courseMap += ("course_video_download_count" -> "course_video_download_count")
courseMap += ("course_video_view_count" -> "course_video_view_count")
courseMap += ("course_video_view_duration" -> "course_video_view_duration")
courseMap += ("course_video_view_ratio" -> "course_video_view_ratio")
courseMap += ("course_video_view_rate" -> "course_video_view_rate")
courseMap += ("course_video_view_rate_ratio" -> "course_video_view_rate_ratio")
courseMap += ("course_video_view_rate_ratio_ratio" -> "course_video_view_rate_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio" -> "course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio")
courseMap += ("course_video_view_rate_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio_ratio
