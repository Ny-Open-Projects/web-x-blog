# 16-课程分析-课程购买量-统计分析

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\16-课程分析-课程购买量-统计分析_【海量资源尽在 666java.com】.mp4
- 时长 13分25秒（音频 806s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前边呢,咱们已经对课程购买量进行了一个轻度聚合,就是在DW层。
[00:07] 聚合的方式呢,是以天为单位,求出了课程的一个销售额以及呢,它的销售量。
[00:15] 接下来呢,咱们对课程购买量的一个统计分析的时候呢,直接在DW层的基础上,再以天为单位,对课程购买量进行求合操作聚合。
[00:29] 这里呢咱们来HOE看一下数据结构这是咱们之前保存的以天为单位是具体的天的每个课程它的一个课程购买量它这课程购买量得到之后呢咱们接下来求和的时候这里是11月12号以11月12号为例把所有11月12号的数据把这个地方给把这个
[00:57] 具体的购买量给SAM就是求核集合就得到了咱们每天的这个课程购买量咱们来再切回文档最终呢保存到数据仓库中之后它的这个保存结构呢和咱们前边的课程访问量是很类似的前边呢是Data Info接下来呢是具体的值Data Info呢就是咱们的具体的日期格式是呢YYYMMDD然后呢接下来是
[01:29] 具体的购买量后边呢有咱们年月日的一个分区就是年月日的分区这里呢咱们也有一个实体相对应以上呢就是咱们课程购买量的一个统计分析的一个介绍接下来呢咱们就进行代码的一个编写因为这里呢代码使用统计的时候呢咱们还是使用Spark的这个Circle使用Spark Circle进行编写咱们呢这里Circle
[01:59] 还是使用HUE进行编写开发工具这边已经将基础的环境配置好这是咱们课程购买量的数据统计以天文一段而进行集合咱们把咱们的Circle测试好之后直接拿过来就可以直接使用咱们来写Circle这里咱们是读取的数据是课程购买量的DWM层的数据咱们先把它给查出来
[02:32] Sled星from咱们的DWM层的数据这里呢最好是把咱们的数据库也给加上这里是DataCast这个拿到之后呢咱们要对它进行一个聚合聚合的时候是根据什么聚合的呀是根据天来聚合的这里边咱们和天有关系的是谁呀咱们前面刚才说了和时间有关系的在上面应该也有和时间有关系的
[03:04] 现在的话聚合之后是不是只有年月日啊只有这个分区所以说呢咱们这个地方呢就根据分区栏嗯这个地方应该也可以展开它这个数据结构对在这里咱们只有这个年月日可以根据它这个年月日的分区栏这里呢咱们以天为单位进行聚合的时候呢就是使用的使用害物的函数是counter c-o-n-c-a-t
[03:34] 将呢年月日给连接起来这里呢连接符是杠横杠然后呢咱们是年月日这些有了之后呢咱们接下来呢就可以进行一个聚合了这个地方咱们最终因为要统计啥呀要统计这个data1号这里呢年月日呢把它给起一个别名就是data1号
[04:04] 后边呢咱们也要需要使用这个因为咱们聚合的时候要根据谁来聚合啊要根据他来聚合根据他来聚合的时候咱们是不是要有一个格尔夫拜啊这里呢咱们就进行格尔夫拜聚合了这里是格尔夫拜可以呢根据他进行哎不对这个地方格尔夫拜呢是直接根据年月日格尔夫拜就行了因为咱们前面是用了这个抗的函数这个呢直接是可以使用的
[04:34] 有了它之后呢接下来Data1号有了接下来呢就是咱们的那个具体的一个数量这个地方的数量呢直接进行SUM求和就行了这里SUM的是谁呀咱们这个里边的课程购买量就是SAL这个value这个课程购买量有了之后咱们还需要把啥给输出来啊就是年月日的一个分区咱们呢这里还需要年月日的分区有了这些数据之后咱们这个Circle就写完了
[05:04] 这里呢执行一下这个地方呢咱们还少了一个条件就是咱们的VR条件咱们在真实的就是生产环境开发的时候这个地方呢是需要过滤日期的也就是哪天你的访问量是多少我是具体到天的这里呢咱们没有过滤条件没有过滤条件呢它得到的是啥呀它得到的是所有日期的这里呢咱们把过滤条件给加上VR这里呢咱们的过滤条件就是具体到天
[05:36] 具体的天的时候咱们就要使用上面这个了把这个给粘过来然后呢让它等于一个具体的日期这里呢咱们就让它等于这个吧9月26号这是随机挑的一个日期然后呢接着进行一个聚合接着进行一个查询得到咱们聚合的一个结果这个时候得到的结果就是具体的每一天就是9月6号这一天的一个具体的一个数据这个地方呢
[06:13] 有一个CE,这个CE呢,咱们把它给起一个别名,叫asconc,这个地方因为没有别名,这个地方显示的CE,这是具体的日期,然后具体的值,然后年月日的分区,这个有了之后呢,咱们再来到咱们的开发工具,在开发工具里边进行一个测试,这里呢,直接使用Spark,circle进行一个编写,因为咱们是多行,还是呢,使用多行的方式,有日期过滤,
[06:43] 这个查询完之后呢,咱们其实这个地方可以把它给转换成一个咱们的实体,后边咱们方便咱们的一个保存,咱们呢是有一个对应的实体呢,所以我用rse,然后呢by,biz,这是咱们的实体,这个地方呢它已经导包导进来了,咱们呢这个地方报错还需要将隐私转换给导入进来,Spark的隐私转换。
[07:14] 就是把所有的都给导过来导过来之后呢这个时候就需要一个变量来接收这个呢咱们看一下数据类型是什么是一个dataset这就是那个by然后ds这个给它一个变量这个地方呢有一个等号完了之后呢这个地方咱们就可以进行一个受操作了来在开发工具中呢也对它进行一个相应的测试这里呢把注射给加一下
[07:46] 只能进行以天为单位进行求和进行计算好这里呢他报了一个错咱们来看是报什么错case inter他说呢这个地方呢是一个inter类型的但是呢他不能找到他这个inter值的因为咱们这个地方是直接转换的as inter的as inter的话在这个在这个里边进行输出的时候是没有问题的
[08:29] 但是呢咱们这个地方呢要把它给映射成什么了映射成一个对象了这个对象呢是有具体的一个数据类型的有数据类型呢咱们这里就需要将它给转换成一个inter类型的这里呢把它给粘一下把它给粘一下因为咱们最终别名还是counter就先把这个at给去掉这里呢咱们使用casecase它进行一个转换
[08:59] 把这个结果呢这里有一个s然后呢它是int类型的最终呢这个地方这个地方s可以加可以不加这个地方先不加吧这个地方的s就不加了就是这个case的呢函数的意思呢就是将那个结果转换成int类型的这样的话就和咱们实体中的这个int对应上了然后咱们再来执行这里呢咱们是输出结果输出结果
[09:37] 这里等它执行一下好这个结果呢和咱们在HUE上执行的结果是一模一样的这里呢程序就跑完了但是呢咱们再回过来说咱们测试的时候呢你一次只统计一天的这个课程的购买量咱们对于咱们业务外表生态来说数据太少咱们呢这里统计还是要统计多天的就是这里呢下两条就先不要
[10:07] 把这个有筛选条件的注释料咱们呢把这个筛选条件给去掉再次来执行一下这个时候呢得到的结果就是咱们目前来说以测试方便咱们测试呢得到咱们所有的这个DWM层的一个所有数据的一个计算有了这个数据之后呢它因为是多天的咱们业务报表系统呢就方便它一个展示接下来就是保存了
[10:36] 保存的话咱们保存的方式和前边是一样的这里呢直接就是进行一个保存这个地方也有一个也有一个这个对应的一个分区咱们呢这个地方直接进行一个保存操作这个呢是DS这个DS是可以执行保存操作的这个呢咱们把这个粘过来之后呢一定要把后缀给改了咱们呢现在是业务表业务表的后缀呢是BIZ这个地方呢也是BIZ
[11:07] 因为保存格式咱们是一样的所以说这段代码就是除了变量名不一样以外表名不一样以外其他的都是一样的一样的情况下呢咱们就直接粘过来了这个时候呢把这个结果输出给先注一下注释一下然后呢咱们执行这个时候呢应该是直接保存到咱们BIZ表里边然后对BIZ表再进行一个查看咱们让程序走一下这里呢把注释给加起来
[11:37] 这个是方便测试不过滤日期方便测试不过滤日期这里它已经在计算了咱们稍微等待一下等待它计算完成这里咱们可以在BIZ这个地方来等待它目前可以看到是没有数据的目前是没有数据的因为咱们程序还没有执行完这里等它执行完成程序还在运行中
[12:15] 这里呢可以看到它已经在网表里边插入了好这个已经保存完成了就是瞬间就一下子就完成了这里呢还是只显示了多少天的数据啊多少条的数据呢只显示了20条的数据咱们呢来数据仓库上来刷新一下这里呢走嗯还没有数据可能是HUE还没有读过来咱们再来刷好这里呢数据已经有了这个地方呢数据有了之后就说明咱们这里已经完全OK了
[12:44] 以天为单位然后统计课程的一个购买量这里呢就统计完成咱们再回到文档这里呢咱们通过咱们的一个APP型代码的一个编写以及呢咱们最终的一个测试咱们的测试结果呢也已经保存到了咱们的数据仓库中咱们的ID诸那JL相对应的结果的一个输出这呢就是咱们这就是咱们
[13:13] 课程购码量统计分析的全部内容存步骤的分析到代码的编写到最终的一个测试好 视频就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过Spark程序处理课程购买事实表数据，生成按日期维度聚合的业务指标，并将结果写入目标表。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程统计分析章节，重点是APP层数据结构，包含Hive外部表定义和对应实体类的注释。
画面2：继续展示APP层数据结构，显示了Scala中CourseBuyBiz类的定义，包含字段映射。
画面3：在Hue界面编写并执行Hive SQL，查询课程购买事实表数据，按年月日分组聚合销售额。
画面4：在Hue界面修改Hive SQL，增加WHERE条件，限定查询日期为'2019-09-26'。
画面5：在IDEA中展示Spark程序代码，包含SparkSession初始化、SQL查询语句和结果写入逻辑。
画面6：在IDEA中运行Spark程序，控制台输出SparkSession创建和数据库连接信息。
画面7：在IDEA中运行Spark程序，控制台报错：Cannot up cast 'count' from double to int，提示类型转换失败。
画面8：在IDEA中修改Spark SQL，将count字段的类型从double改为int。
画面9：在IDEA中运行修改后的Spark程序，控制台显示成功执行并输出结果。
画面10：在IDEA中修改Spark程序，设置动态分区模式为“nonstrict”，并添加写入模式为“overwrite”。
画面11：在IDEA中运行修改后的Spark程序，控制台显示成功执行并输出结果。
画面12：在IDEA中修改Spark程序，设置动态分区模式为“nonstrict”，并添加写入模式为“overwrite”。
画面13：在Hue界面查看course_buy_biz表，显示该表无数据。
画面14：展示课程统计分析章节的测试部分，包含运行方法和部分运行结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_course.course_buy_biz
(date_info String,
count INT)
PARTITIONED BY (years String,months String,days String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/Hive/external/data_course/course_buy_biz';

对应实体：
/**
 * 每天购买量
 * @param date_info 日期，格式：yyyy-MM-dd
 * @param count 购买量
 * @param years 分年
 * @param months 分月
 * @param days 分日
 */
case class CourseBuyBiz(date_info: String,
count: Int,
years: String,
months: String,
days: String)

画面3：
SELECT
concat_ws('','years, months, days') as date_info,
sum(salesvolume) as count,
years, months, days
FROM data_course.course_buy_dwm
GROUP BY years, months, days

画面4：
SELECT
concat_ws('','years, months, days') as date_info,
sum(salesvolume) as count,
years, months, days
FROM data_course.course_buy_dwm
WHERE concat_ws('','years, months, days') = '2019-09-26'
GROUP BY years, months, days

画面5：
object CourseBuyProcessByBiz {
  // Spark session
  val Spark: SparkSession = FileEnvironment.getSparkSession(this.getClass.getSimpleName)

  def main(args: Array[String]): Unit = {
    import Spark.implicits._

    val buyDS = Spark.sql(
      """
        |SELECT
        |concat_ws('','years, months, days') as date_info,
        |sum(salesvolume) as count,
        |years, months, days
        |FROM data_course.course_buy_dwm
        |WHERE concat_ws('','years, months, days') = '2019-09-26'
        |GROUP BY years, months, days
        |""".stripMargin).as(CourseBuyBiz)
    buyDS.show()
    Spark.close()
  }
}

画面6：
val Spark: SparkSession = FileEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  import Spark.implicits._

  val buyDS = Spark.sql(
    """
      |SELECT
      |concat_ws('','years, months, days') as date_info,
      |sum(salesvolume) as count,
      |years, months, days
      |FROM data_course.course_buy_dwm
      |WHERE concat_ws('','years, months, days') = '2019-09-26'
      |GROUP BY years, months, days
      |""".stripMargin).as(CourseBuyBiz)
  buyDS.show()
  Spark.close()
}

画面7：
val buyDS = Spark.sql(
  """
    |SELECT
    |concat_ws('','years, months, days') as date_info,
    |sum(salesvolume) as count,
    |years, months, days
    |FROM data_course.course_buy_dwm
    |WHERE concat_ws('','years, months, days') = '2019-09-26'
    |GROUP BY years, months, days
    |""".stripMargin).as(CourseBuyBiz)
buyDS.show()
Spark.close()

画面8：
val buyDS = Spark.sql(
  """
    |SELECT
    |concat_ws('','years, months, days') as date_info,
    |cast(sum(salesvolume) as int) count,
    |years, months, days
    |FROM data_course.course_buy_dwm
    |WHERE concat_ws('','years, months, days') = '2019-09-26'
    |GROUP BY years, months, days
    |""".stripMargin).as(CourseBuyBiz)
buyDS.show()
Spark.close()

画面9：
val buyDS = Spark.sql(
  """
    |SELECT
    |concat_ws('','years, months, days') as date_info,
    |cast(sum(salesvolume) as int) count,
    |years, months, days
    |FROM data_course.course_buy_dwm
    |WHERE concat_ws('','years, months, days') = '2019-09-26'
    |GROUP BY years, months, days
    |""".stripMargin).as(CourseBuyBiz)
buyDS.show()
Spark.close()

画面10：
// 配置动态分区模式
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")
buyDS
  .write
  .mode("overwrite")
  .insertInto("data_course.course_buy_fact")
  .show()

画面11：
val buyDS = Spark.sql(
  """
    |SELECT
    |concat_ws('','years, months, days') as date_info,
    |cast(sum(salesvolume) as int) count,
    |years, months, days
    |FROM data_course.course_buy_dwm
    |WHERE concat_ws('','years, months, days') = '2019-09-26'
    |GROUP BY years, months, days
    |""".stripMargin).as(CourseBuyBiz)
buyDS.show()
Spark.close()

画面12：
val buyDS = Spark.sql(
  """
    |SELECT
    |concat_ws('','years, months, days') as date_info,
    |cast(sum(salesvolume) as int) count,
    |years, months, days
    |FROM data_course.course_buy_dwm
    |WHERE concat_ws('','years, months, days') = '2019-09-26'
    |GROUP BY years, months, days
    |""".stripMargin).as(CourseBuyBiz)
buyDS.show()
Spark.close()

画面14：
def main(args: Array[String]): Unit = {
  // Run 'CourseBuyProcessByBiz' Ctrl+Shift+F10
  // Debug 'CourseBuyProcessByBiz'
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“2.5 统计分析”，子标题“2.5.1 统计步骤”和“2.5.2 APP层数据结构”。
画面14：PPT标题为“2.5.4 测试”，包含运行方法和部分运行结果表格。
表格数据：
| date_info | count | years | months | days |
| --- | --- | --- | --- | --- |
| 2017-09-30 | 123 | 2017 | 09 | 30 |
| 2017-10-01 | 129 | 2017 | 10 | 01 |
| 2017-10-02 | 137 | 2017 | 10 | 02 |
| 2017-10-03 | 144 | 2017 | 10 | 03 |
| 2017-10-04 | 139 | 2017 | 10 | 04 |
| 2017-10-05 | 149 | 2

