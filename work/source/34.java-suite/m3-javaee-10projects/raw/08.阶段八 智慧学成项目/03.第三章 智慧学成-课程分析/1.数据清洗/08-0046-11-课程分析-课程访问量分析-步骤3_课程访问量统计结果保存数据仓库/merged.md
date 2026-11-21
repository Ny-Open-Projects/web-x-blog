# 11-课程分析-课程访问量分析-步骤3：课程访问量统计结果保存数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\11-课程分析-课程访问量分析-步骤3：课程访问量统计结果保存数据仓库_【海量资源尽在 666java.com】.mp4
- 时长 8分32秒（音频 512s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前边上咱们已经进行了求客操作,并将结果变量保存到咱们的VDataCount里边,数据结构是咱们的DataInfo加年月日的分期,最后是咱们的一个当天的一个统计结果。
[00:19] 接下来咱们就进行保存到数据仓库中代码的一个编写。
[00:25] 首先咱们需要去指定一个列,这个地方为什么要指定列呢?
[00:31] 咱们来说明一下我先把这个方法给写出来由于咱们这个数据结构数据APP层的数据结构是data info然后是count最后才是分区的年月日但是呢咱们这个地方是不是年月日是跟着这个data info呢它造成了一个数据的混乱就是保存到时候你直接进行保存会出现数据混乱
[00:58] 这里呢,咱们需要将这个列和咱们这个地方对应起来,让这个count在data info的后面,最后呢是年月日的一个分区,这里直接指定对应列就行了,首先是data info,接下来呢是count,再接下来呢是年月日的分区,年月日的分区这个地方就可以直接粘过来了,咱们指定完列之后呢就可以进行一个写入,这里呢直接write,
[01:33] 然后写入的模式呢咱们还是overwrite是覆盖的模式接下来呢就是指定一个表明指定表明的时候呢咱们可以来这偷个脸把这个表明给粘过来进行一个修改即可因为呢咱们那个每一个指标它的命名规则都是一样的这是事实表就后面就是以fit结尾然后业务表呢就以biz结尾咱们那个客栋房量的业务表就是这个
[02:07] 保存完之后呢咱们在代码里边进行一个查看当然咱们这个地方也可以使用HUE进行web界面的一个查看哪种方式都行咱们呢直接在代码里边将结果给打印了这里呢使用收方法把结果打印到控制台好到此为止呢咱们保存操作就完成了但是这个地方呢有一个注意事项就是咱们在编写课程访问量清洗代码的时候
[02:39] 同样有一个保存到数据参控的一个操作它呢要求你配置动态分区也就是每一个程序都需要配置这里呢咱们直接来这里把配置动态分区的代码给粘过来然后呢就可以测试咱们的一个完整的一个统计分析的程序这里开始运行程序执行的呢我将咱们这个代码的注释给加一下这里呢就是
[03:11] 指定列防止数据混乱这个呢就是咱们的写入模式写入模式确定了之后呢咱们就是指定数据仓库的表明中的表明它的格式呢是库名然后是底表明接下来呢就是一个结果的查看结果查看这个地方也有一个结果查看但是这个结果查看呢是
[03:59] 咱们这个变量的一个结果查看这个结果查看呢再加一下吧是数据仓库中的的结果查看这里就是咱们对应到的一个结果data info然后咱们的对应的一个值就是具体这一天有多少咱们的访问量以上呢就是咱们课程访问量的所有程序就是所有代码咱们也测试通过了就是以天为单位计算就通过了
[04:31] 但是呢这个地方还有一个注意事项就是咱们在测试的测试阶段这个每次执行只有一天的数据但是咱们报表系统展示的时候需要大量的数据进行一个展示这个地方呢就可以做一个简单的一个修改就是把咱们这个日期过滤条件给去掉也就是说我下面根据日期进行根据咱们那个DataInfo进行分组
[05:00] 分组完成之后统计它的一个具体的一个求核操作统计它具体的一个当天仿量的个数对下面这个结果是不影响的我上面有DataInfo它只统计一天的我过滤的时候DataInfo是一天它只统计一天的但是上面我不过滤的时候有多少天我这里就统计多少天咱们来再执行程序来进行一个测试这个时候咱们数据里边就是咱们的事实表里边
[05:30] 有多少天的数据这里呢去掉日期过滤之后它得到呢就是有多少天的一个数据这个地方也加了一个小注释吧这个是求可结果查看查看咱们注释这边已经加完接下来呢就是等待这个程序运行完成咱们耐心等待一下程序跑完这里还在计算中
[06:08] 咱们呢可以切到HUE上这里已经计算完成控制台默认呢是只显示20条数据咱们可以去HUE来看一下咱们具体有多少条数据这个的话应该是刚才上面的一个计算结果就是这个求和求和结果查看就是求和的一个结果查看刚才是只显示20条这里呢
[06:39] 等它保存完,咱们可以学HUE,看它一共有多少条,咱们可以来先写circle这里呢,这个circle还是可以复用的,直接粘过来粘过来之后呢,加一个统计的条件就行这里是进行一个count操作,咱们直接count第一列这里呢,就耐心的等待什么呀,等待它这里代码跑完由于咱们
[07:11] 分区里这个不是分区啊咱们这个课程方案量这个试试表里边日期根据这个显示的话还是挺多的9月份的也有10月份的也有这个统计呢需要一定的时间咱们还不知道他多久能统计完刚说他还要多久能统计完这里已经出了结果这里呢还是只显示了20条咱们来这里查看一下走程序还没有执行完成这里
[07:50] 教卜还正在运行好这里结果已经出来是60条也就是说咱们这次这个统计呢结果有60条而且呢已经保存到数据仓库中到此呢咱们来切到文档到此呢咱们这个课程访问量统计分析的代码就已经写完而且呢这里咱们也已经测试OK好课程访问量统计代码的一个编写及测试
[08:27] 到这里就结束了本视频到这里也结束了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark 读取 Hive 表数据、进行分组聚合，并将结果写入 Hive 表，同时展示了在 Hive 中查看数据的过程。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Hive 表结构定义（CREATE EXTERNAL TABLE）和对应的 Scala 案例类（case class CourseVisitBiz）。
画面2：展示 Spark 代码，定义了日期变量、读取 Hive 表、分组聚合，并准备写入数据。
画面3：在 Spark 代码中设置动态分区模式（Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")）。
画面4：执行 Spark 任务，终端显示任务启动和执行日志。
画面5：Spark 任务执行中，终端显示任务状态和日志。
画面6：Spark 任务执行完成，终端显示任务成功完成。
画面7：Spark 任务执行完成，终端显示任务成功完成。
画面8：Spark 任务执行完成，终端显示任务成功完成。
画面9：Spark 任务执行完成，终端显示任务成功完成。
画面10：Spark 任务执行完成，终端显示任务成功完成。
画面11：切换到 Hive 的 Hue 编辑器界面，准备执行 SQL 查询。
画面12：在 Spark 代码中执行了 Hive 表的分区替换操作。
画面13：在 Hue 编辑器中执行了 SQL 查询（select count() from data_course.course_visit_biz）。
画面14：展示课程大纲，内容为“1.1 课程访问量统计分析”下的“1.1.1 统计步骤”和“1.1.2 APP层数据结构”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面1：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_course.course_visit_biz
(date_info String,
count INT)
PARTITIONED BY (years String,months String,days String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/Hive/external/data_course/course_visit_biz';

对应实体：
/**
 * 每天访问量
 * @param date_info 日期，格式：yyyy-MM-dd
 * @param count 访问次数
 * @param years 分区年
 * @param months 分区月
 * @param days 分区日
 */
case class CourseVisitBiz(date_info: String,
count: Int,
years: String,
months: String,
days: String)

画面2：
val Spark: SparkSession = ETLEnvironment.getSparkSession(this.getClass.getClassLoader)
def main(args: Array[String]): Unit = {
  val date_info = "2019-11-11"
  val visitCount = visitDF.groupBy(col = "date_info", cols = "years", "months", "days").count()
  visitCount.show()
}

画面3：
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")

画面4：
// 3. 存储到数据表（业务表中）
visitCount.selectExpr(exprs = "date_info", "count", "years", "months", "days")
.write.mode(saveMode = "overwrite")
.insertInto(tableName = "data_course.course_visit_biz")

画面5：
// 3. 存储到数据表（业务表中）
visitCount.selectExpr(exprs = "date_info", "count", "years", "months", "days")
.write.mode(saveMode = "overwrite")
.insertInto(tableName = "data_course.course_visit_biz")

画面6：
// 4. 天然查询
Spark.sql("select * from data_course.course_visit_biz").show()

画面7：
// 4. 天然查询
Spark.sql("select * from data_course.course_visit_biz").show()

画面8：
// 4. 天然查询
Spark.sql("select * from data_course.course_visit_biz").show()

画面9：
// 4. 天然查询
Spark.sql("select * from data_course.course_visit_biz").show()

画面10：
// 4. 天然查询
Spark.sql("select * from data_course.course_visit_biz").show()

画面11：
（无代码）

画面12：
// 1. 替换分区
Spark.sql("replace partition with '2019-11-11' partition by (years, months, days) from data_course.course_visit_biz")

画面13：
select count() from data_course.course_visit_biz

画面14：
（无代码）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：
标题：1.1.2 APP层数据结构
内容：数据结构定义（CREATE EXTERNAL TABLE）和对应的 Scala 案例类（case class CourseVisitBiz）。

画面14：
标题：1.1 课程访问量统计分析
子标题：1.1.1 统计步骤
内容：1. 读取课程访问量事实表数据；2. 以天为单位求和；3. 将结果保存到课程访问量外表。
子标题：1.1.2 APP层数据结构
内容：数据结构定义（CREATE EXTERNAL TABLE）和对应的 Scala 案例类（case class CourseVisitBiz）。

5) 不要评价画面美观，不要输出与课程无关的内容。

