# 10即时查询-统计分析-步骤1：代码-获取原始数据

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\10即时查询-统计分析-步骤1：代码-获取原始数据_【海量资源尽在 666java.com】.mp4
- 时长 6分51秒（音频 411s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 咱们继续前边已经分析了步骤一的统计逻辑咱们接下来就根据逻辑进行代码的编写来切到开发工具开发工具中咱们已经创建好了工程并且已经将固定的代码给准备好这里固定的代码包括咱们获取SWAG session获取SWAG的context以及最终是将数据保存到数据仓库中的固定代码
[00:28] 这个地方由于最终这个变量还没有确认咱们呢把保存的代码这一块先给注释掉了等咱们在第三步统计完学习时长这个变量咱们声明好这里呢直接把注释给放开就可以直接保存到数据仓库中好咱们接着呢就编写根据日期来获取数据的代码这里呢咱们直接使用Spark context
[00:59] 这个方法进行数据的获取这里咱们数据的获取要使用的路径就是咱们数据采集的时候用户学习的数据路径咱们来到HUE上来查看一下这个路径咱们来切到file这个地方切到file就是查看HDFS上的文件路径这里learn cost online source就是咱们的原始路径
[01:35] 就是咱们的原始数据的一个路径咱们来切到把具体日期给选择掉之后就获得了咱们在HDFS上的完整路径但是这个地方是有一个硬编码咱们在真正的生产环境这个日期是应该是传递过来的而不是在这里写死传递过来的话咱们这个日期先定一个变量名叫做DataInfo
[02:04] 它的日期格式应该是使用参数进行传递但是咱们这个地方测试阶段先把它给写死就是咱们的这个日期2019-112-11这个时候这里采用变量传递的方式把这个Data引号给传递过来就解决了咱们硬编码的问题这里数据获取完成之后咱们需要使用一个变量来接收这里
[02:33] 就叫做learnSource这就是咱们的单次写作了source这个就是咱们的原始数据原始数据获取完成之后咱们还是不能直接使用的因为获取到的它只是一个文本数据咱们需要把它给转成一个RDD接下来咱们对它进行一个转换使用learnSource咱们
[03:09] 进行转换的时候需要明确一件事情咱们上边这个原始数据是怎么保存的在咱们的ods层这里呢是各个字段咱们保存的是文件的方式使用-t进行分隔使用-n进行换行咱们呢这里使用-t来获取各个字段这里呢咱们使用map算子进行数据的一个切分直接呢split一个杠就行
[03:41] 这个时候呢就得到了各个字段得到了各个字段之后呢还不算完因为呢咱们最终是要对每个字段进行一个操作的比如说关联维度啊比如说计算时长啊咱们接着把它转换成一个对象前边呢它是一个AR因为咱们使用了Split切割之后呢它是一个AR这里呢咱们有一个实体是userlearn这个实体这个实体呢就对应了
[04:11] 咱们原始数据的各个字段咱们就根据这个实体把咱们切分好的数据进行一个封装这里呢就是AR把这个AR呢来复制一下咱们从0开始进行一个复制这里是0然后呢逗号这个字段呢它的顺序是和咱们这个文档中它这个顺序是一模一样的咱们的保存数据是一模一样的
[04:41] 所以说就可以按照0123456这样进行一个排列接下来是1接下来是2第二个是索引2是Cross-Video ID索引3是U3 IP接着是索引4索引4是Session ID接下来是索引5索引5是浏览器的标识接下来是索引6
[05:11] 好,到所有6呢,咱们就把这个复制操作给处理完了这个时候呢,它获取到的数据呢是String的但是咱们这个地方呢,要求是浪类型的使用toLang方法把它给转换转换完成之后呢,这个时候咱们就得到了这个map得到的是R,得到的是RDD咱们呢,这个地方就得到了learnSource的RDD用一个变量进行一个接收
[05:40] 有了这个RDD之后呢咱们后边关联维度以及计算它的一个时长的时候学习时长的时候呢就相对来说方便了咱们呢这里计算时长和关联维度呢使用Spark和Circle这个地方还要将它创建一个零时表使用Circle来计算这个地方呢创建零时表使用Spark进行创建这里呢是CreateDataForm把RDD传进去然后呢Create
[06:14] replaceValve,这个就是说如果已存在了我就把你给覆盖掉这个呢是learnSourceTime这个呢将一个下滑线把这个全部变成小写快捷键呢是Ctrl Shift U好,创建完成之后呢咱们接下来使用SparkSoccer就可以直接用这个变量进行数据的一个操作咱们呢获取数据代码就写到这里
[06:45] 后边的步骤呢咱们交给下一个视频好视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark 读取 HDFS 上的用户学习行为原始数据，并将其转换为结构化的 DataFrame，最终写入 Hive 表中。

2) 按时间顺序列出每张画面的要点：
画面1: 显示 Scala 代码，定义 SparkSession，读取 HDFS 数据并写入 Hive 表，设置 Hive 参数。
画面2: 代码中高亮显示写入 Hive 表的 SQL 语句 `insertInto("s${tableLame}")`。
画面3: 代码中高亮显示 SparkSession 的创建语句 `val sc = Spark.sparkContext`。
画面4: 代码中高亮显示 SparkSession 的创建语句 `val sc = Spark.sparkContext`。
画面5: 显示 Hue 文件浏览器界面，展示 HDFS 上的目录结构，其中包含多个事实表文件夹。
画面6: 代码中高亮显示读取 HDFS 数据的路径 `val learnSource = sc.textFile(...)`。
画面7: 显示 PPT 页面，标题为“3.1 步骤1:关联维度统计分析”，子标题“3.1.1 统计逻辑”。
画面8: 显示 PPT 页面，标题为“1.4 ODS数据存储分析-用户学习”，内容包括数据存储格式、存储方式和内容格式。
画面9: 代码中高亮显示对读取的数据进行解析和转换的逻辑 `learnSource.map(...)`。
画面10: 显示两个 Scala 文件，分别是 `InstantQueryStepToHive.scala` 和 `Courses.scala`，后者定义了 `UserOnline` 和 `LearningCourseOnlineIndex` 案例类。
画面11: 显示 PPT 页面，标题为“1.3.2 ODS层数据结构-用户学习”，包含一个表格，列出了采集字段、字段说明和数据格式。
画面12: 代码中高亮显示对数据进行转换的逻辑 `case class UserOnline(...)`。
画面13: 代码中高亮显示读取 HDFS 数据的路径 `val learnSource = sc.textFile(...)`。
画面14: 代码中高亮显示创建 Hive 表并写入数据的语句 `Spark.createDataFrame(...).createReplaceTempView(...)`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1:
```scala
object InstantQueryStepToHive {
  // 初始化 SparkSession
  val Spark: SparkSession = EtlEnvironment.getSparkSession(this.getClass.getSimpleName, etlTableName = null)

  def main(args: Array[String]): Unit = {
    // 获取 SparkContext
    val sc = Spark.sparkContext

    // 1. 根据入口HDFS中原始数据路径
    // 2. 关联相关维度表
    // 3. 算计学习时长
    // 4. 存在数据集全表
    // 假设Hive参数
    Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")

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
    val learnSource = sc.textFile(s"/user/Hive/external/data_course/learning_course_online_source/${date_info}")
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
    Spark.createDataFrame(learnSourceRDD).createReplaceTempView(viewName = "learn_source_tmp")
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
数据存储方式：每天的数据以 年/月/日 为目录名，每天的数据存储在一个目录中，如：`/user/Hive/external/data_course/learning_course_online_source/${now}(format:yyyy-MM-dd)`
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

