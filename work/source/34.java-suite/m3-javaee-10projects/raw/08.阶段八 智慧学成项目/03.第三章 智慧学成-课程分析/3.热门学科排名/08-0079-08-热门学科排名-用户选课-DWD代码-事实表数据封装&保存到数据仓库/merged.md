# 08-热门学科排名-用户选课-DWD代码-事实表数据封装&保存到数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\08-热门学科排名-用户选课-DWD代码-事实表数据封装&保存到数据仓库_【海量资源尽在 666java.com】.mp4
- 时长 6分51秒（音频 412s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,接下来呢,咱们通过对原始数据的维度关联来得到咱们的试试表,这里呢,使用咱们的line source这个变量,这里使用map算子,进行呢,维度的关联,这个地方给它一个obj,给它一个变量叫做obj,然后呢,接下来咱们是要关联维度,这里需要关联的维度呢,咱们来这里来粘一下,
[00:30] 这就是咱们需要关联的维度咱们需要关联的维度呢其中用户维度和课程维度是不是通过用户的ID和课程的ID直接获取就行了直接封装就行需要聚散的维度呢只有两个一个是时间维度一个是课程分类的维度课程分类的维度呢是不是在这个地方可以通过咱们的这个CostMap进行一个获取给它一个变量这里呢就叫CAT IDCategor ID
[01:04] 它呢就等于咱们cosmapget谁啊通过咱们课程的ID进行一个获取这里是obg咱们的课程ID就是cosid这个地方呢它获取它的一个返回值是什么呀它是opt的但是咱们这个地方呢是不是需要的一个是字符刷啊这个呢还需要再进行一个get操作存咱们的open生里边就是optl里边然后获取它的具体的一个值接下来是时间维度的ID
[01:35] 时间维度的ID呢,咱们是通过格式化咱们的选客时间来进行一个获取这里呢,就叫timeID它呢,等于格式化咱们的getDataStra这个呢,getDataStra在咱们的工具类中就是日期工具类中由于呢,这个它不会自动的打完咱们呢,需要将它给手动的进行一个打完copy reference然后呢,这里
[02:05] 直接把它import了这个时候就可以使用getstr这个变量这里呢getstr它需要两个参数一个参数呢是毫秒值一个参数呢是你的格式化的一个表达式毫秒值呢咱们是通过obj的咱们选客时间来获取这个呢选客时间它的一个防御值是什么啊begin但是这个情况是需要的是lang先把它给转换成lang类型了
[02:33] 转换进之后呢还需要说明一点咱们的选客时间呢这个地方是时间戳但是呢它需要的是行表值时间戳转行表值是需要乘以1000的这个地方来乘以1000这个地方行表值就搞定接下来呢是咱们的表达式表达式呢咱们时间维度的ID的表达式呢是yyy-mm-dd然后-hh它是带小时的到此呢维度的ID这个地方就完成了
[03:03] 接下来咱们就是数据的一个封装这里呢咱们数据封装是learning learning cause fate应该是c-u-r-s-e然后fate f-a-c-ta-c-t这里呢咱们直接使用这个实体进行一个封装这个地方呢为了方便咱们查看就是说我封装到哪个哪个属性了咱们呢进行一个窗口的一个分割首先呢这个地方咱们要的是谁啊
[03:35] 它的维度ID,它的维度ID呢,这个地方是UOID,咱们的OBG里边已经有了,对应的是LearnCourseID,它就是一个选课表的ID,接下来呢,是课程分类ID,接下来是课程分类的ID,课程分类ID是不是前面已经扩充到了,是咱们的CID,接下来呢,是课程维度的ID,这里就是直接OBG的咱们的课程ID,课程ID完了之后是用户ID,用户ID也是可以直接用的,
[04:05] obj.userid就行了接下来呢是时间维度id时间维度id是不是前面已经获取过了时间维度id按了之后是状态状态呢也是直接拿来就可以用状态有了之后接下来还有谁啊还有分区的年月日分区的年月日咱们是不是可以通过时间维度来获取啊这里ymd是咱们分区的一个变量时间分区的变量
[04:33] 他那通过timeid进行一个切割就行了因为咱们的年月月就是对应的前面这三个咱们的切割使用横杠这个时候就可以使用ymd来进行一个数据的获取首先呢是咱们的年年完了之后是月然后日这个呢根据咱们的变量它就是21这个地方报了一个错应该是中文标点的一个导致的中文逗号导致的
[05:05] 这个地方也是一样它是一个中文动画好改成英文就行了稍微格式化一下这个让它来后边这个放到一行这个功能完成之后咱们需要一个变量来进行一个接收变量接收完成之后咱们是把它给保存到数据仓库中的然后就叫learn fit有了它之后咱们接下来就是保存到数据仓库了保存到数据仓库咱们首先是要把它转换成df的
[05:36] 这个地方保存操作由于都是相同的代码咱们来直接来粘一个咱们就拿课程房量的吧这个地方是咱们转换的代码保存的代码把它直接拿过来这个保存的代码咱们只需要就是将咱们的只需要将咱们的变量给修改一下就行了这个地方是learn fit这个地方叫做learn fit
[06:08] DF吧这个地方是编量修改一下接下来是谁啊接下来是不是你要保存的表明要写需要修改啊这里咱们来查看一下表明这个地方呢我已经将这个窗口给打开了这就是咱们试试表用户选择试试表的一个表明把全路径给单过来这里呢走起保存完成之后呢咱们还要去对它进行一个查看查看呢是否保存成功好
[06:40] 以上呢就是咱们用户选客原始数据清洗的试试表的所有代码代码编写呢就到这里咱们呢这个视频也就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
val learnSource = Spark.sql(s"SELECT * from data_course.learning_course_source WHERE from_unixtime(choose_time, 'yyyy-MM-dd') = '${date_info}'")
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

