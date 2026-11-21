# 24-热门学科排名-统计分析-销售额-周-统计分析步骤&代码编写

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\24-热门学科排名-统计分析-销售额-周-统计分析步骤&代码编写_【海量资源尽在 666java.com】.mp4
- 时长 5分34秒（音频 334s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来对热门学科排名中的销售额进行统计分析,首先是州的统计分析,咱们这里的销售额和前边的销售量是非常相似的,前边是统销售量,是统计的是具体的一个课程卖出的一个个数,这里销售额是具体的课程卖出的前数,由于它们非常相似,包括咱们这里的统计步骤以及使用的基础数据。
[00:30] 都是一样的咱们呢就基于销售额的基于销售量来编写咱们销售额周的统计分析咱们呢来切到开发工具这是咱们这是咱们开发这是咱们已经写好的销售量的一个统计分析咱们呢就基于这个周的销售量的统计分析来修改出来咱们销售额的统计分析首先呢还是周的统计分析这里把变量给修改一下
[01:02] 这个地方呢就是咱们要修改的销售额的统计分析代码咱们呢自上向下开始修改这块内容是获取日期区间的周的区间不用动这个地方是获取数据然后计算涨幅这个地方需要修改这个呢是咱们销售量的咱们呢销售额也有对应的一个统计方法就是咱们抽取的供给类这里呢直接把它给拿过来对它进行修改就行了
[01:33] 这里咱们需要统计的是销售额的数据咱们来到HOE上看一下咱们DWM层的数据结构这个是销售量这个是销售额咱们在统计分析的时候就是使用销售额的数据这里就需要将销售额把它给统计出来这里就把销售量改成销售额即可这个变量也是需要进行修改的它就不是那面了它就是具体的数了
[02:04] 咱们来文档上看这个地方呢使用的变量是什么销售额是使用的这个变量咱们来把它就粘过来销售额的这个地方呢也是销售额的这个变量有了之后一定不要忘记咱们就算增幅这个地方也需要修改这个地方修改完成之后咱们这个基本上就完成了咱们来看这个变量是叫什么名字变量千万不要错了这个变量也是修改一下变量修改完成之后呢咱们这一块的
[02:37] 代码修改就完成了这块的代码修改完成之后咱们还回到咱们的周的统计里边这个地方呢咱们需要对方法进行一个修改就修改成咱们销售额度的这个统计这个地方完了之后接下来周的或许一年中的周不用改接下来呢就是咱们维度相关的数据以及关联这个呢咱们切到咱们的咱们的实体中这个地方呢就是热门学科
[03:07] 销售额周的数据咱们呢最终是要封装成这样一个数据咱们呢这个地方先把它给改了改完之后呢这个地方咱们对照咱们的窗口来改咱们这个circle的数据把它给打个包这个circle呢前面是一样的第一个是ID第二个是学科名第三个就变了第三个是什么呀第三个就是咱们的销售额了这两个呢都是flot咱们呢这地方就是flot类型了
[03:37] 这个地方呢把它改成Flock变量也修改一下这是咱们销售额的增幅的变量也修改一下这个修改完成之后咱们接下来这个地方临时表是不是也要修改一下呀这个还是销售量的一个临时表咱们呢把它给修改成销售额的临时表这个修改完成之后这段代码就修改完成了修改完成之后接下来就是保存表的一个修改咱们这里是保存到哪张表呢咱们来看文档
[04:08] 是这张表咱们呢把咱们有保存的表也给替换一下到此咱们修改已经完成修改完成之后呢咱们再回过头来再确认一遍其实来保证咱们这个修改是没有问题的首先咱们没有修改的部分是日期部分接下来呢这个地方是根据获取的数据计算奖服咱们做了修改这个地方呢这些都是固定的这是咱们的
[04:38] 这是咱们的销售额度销售额这个是根据销售额计算的涨幅接下来呢这是使用三目算子使用三目函数然后计算它这个销售额下边也是一样的这些咱们修改完成之后这确认完成之后呢接着往后走这里呢咱们要改变的只是它是一个销售额然后呢销售额的增幅这里呢它们两个都是flot类型的这里已经修改
[05:06] 然后呢咱们需要转换成实体这个也转换了过来转换完成之后呢接下来就是保存保存呢咱们只用将表明给修改一下就行修改完成之后咱们查看结果也是修改一下表明到此呢到此呢咱们热门学科排名中销售额按周统计咱们代码已经完成了视频呢也就到这里测试呢交给下一个视频

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark 编写周粒度销售金额统计程序，涉及数据读取、时间处理、SQL 查询和结果写入。

2) 按时间顺序列出每张画面的要点：
画面1: 展示项目结构，选中 `SubjectSalesByWeekBiz.scala` 文件，准备编写周销售统计代码。
画面2: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义主函数，初始化 SparkSession，解析日期参数。
画面3: 展示 `SubjectUtils.scala` 文件内容，包含 `subjectBuyAmountSql` 函数，定义 SQL 查询语句。
画面4: 切换到 Hive 图形界面，展示 `sales` 数据库下的表结构，包括 `salesvolume`、`salesvolume_biz_tmp` 等。
画面5: 回到代码编辑器，展示 `SubjectUtils.scala` 文件中 `subjectBuyAmountSql` 函数的 SQL 语句。
画面6: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `subjectBuyAmountSql` 函数，创建临时视图 `salesvolume_biz_tmp`。
画面7: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `weekOfYear` 变量，加载 SQL 文件。
画面8: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `SubjectAmountWeekBiz` 案例类，用于封装周销售数据。
画面9: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `SubjectAmountMonthBiz` 案例类，用于封装月销售数据。
画面10: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `SubjectAmountWeekBiz` 案例类，用于封装周销售数据。
画面11: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `SubjectSalesByWeekBiz` 类，包含 `subjectBuyAmountSql` 函数。
画面12: 展示 `SubjectUtils.scala` 文件内容，包含 `subjectBuyAmountSql` 函数，定义 SQL 查询语句。
画面13: 展示 `SubjectSalesByWeekBiz.scala` 文件内容，定义 `subjectBuyAmountSql` 函数，创建临时视图 `salesvolume_biz_tmp`。
画面14: 展示 PPT 页面，标题为“3.5.3 销售额”，子标题“3.5.3.1 周”，内容为“3.5.3.1.1 统计分析步骤”，并列出 7 个步骤，其中步骤 7 为“保存结果”，并展示 SQL 创建外部表语句。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面2:
```scala
package cn.itcast.xc.analysis.subject.sales

import cn.itcast.xc.common.fileEnvironment
import cn.itcast.xc.entity.SubjectSaleBiz
import cn.itcast.xc.utils.DateUtils.getWeekNum, getWeekRelativelyInterval
import org.apache.Spark.sql.SparkSession

object SubjectSalesByWeekBiz {
  val Spark: SparkSession = EtlEnvironment.getSparkSession(this.getClass.getSimpleName)

  def main(args: Array[String]): Unit = {
    import Spark.implicits._
    val date_info = args(0)
    val weeks = getWeekRelativelyInterval(date_info).split(regex = "-")
    val current = weeks(0).split(regex = "-")
    val last = weeks(1).split(regex = "-")
  }
}
```

画面3:
```scala
def subjectBuyAmountSql(Spark: SparkSession, current: Array[String], last: Array[String]): sql.DataFrame = {
  Spark.sql(
    """
      SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num,
      ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
      FROM (SELECT course_category_dim_id, sum(salesvolume) sale_num
      FROM data_course.course_buy_dim
      WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
      GROUP BY course_category_dim_id) as a
      LEFT JOIN (
      SELECT course_category_dim_id, sum(salesvolume) sale_num
      FROM data_course.course_buy_dim
      WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
      GROUP BY course_category_dim_id) as b
      ON a.course_category_dim_id = b.course_category_dim_id
    """.stripMargin
  )
}
```

画面4:
```sql
SELECT a.course_category_dim_id, course_buy_dim_id, a.sale_num sale_num,
ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
FROM (SELECT course_category_dim_id, sum(salesvolume) sale_num
FROM data_course.course_buy_dim
WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
GROUP BY course_category_dim_id) as a
LEFT JOIN (
SELECT course_category_dim_id, sum(salesvolume) sale_num
FROM data_course.course_buy_dim
WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
GROUP BY course_category_dim_id) as b
ON a.course_category_dim_id = b.course_category_dim_id
```

画面6:
```scala
subjectBuyAmountSql(Spark, current, last).createReplaceTempView(viewName = "salesvolume_biz_tmp")
```

画面7:
```scala
val weekOfYear = getWeekNum(current(0)).split(regex = "-")
val sids = Spark.sql(
  """
    select
      a.course_category_dim_id,
      b.name course_category_name,
      cast(a.sale_num as float) sale_amount,
      cast(a.sale_percent as float) amount_percent,
      ${weekOfYear(0)} week_of_year
    from salesvolume_biz_tmp a
    left join data_dimen.course_category_dim b
    on a.course_category_dim_id = b.course_category_dim_id
  """.stripMargin
)
```

画面8:
```scala
case class SubjectAmountWeekBiz(course_category_dim_id: String,
  course_category_name: String,
  sale_amount: Float,
  amount_percent: Float,
  years: String,
  week_of_year: String)
```

画面9:
```scala
case class SubjectAmountMonthBiz(course_category_dim_id: String,
  course_category_name: String,
  sale_amount: Float,
  amount_percent: Float,
  years: String,
  month_of_year: String)
```

画面10:
```scala
case class SubjectAmountWeekBiz(course_category_dim_id: String,
  course_category_name: String,
  sale_amount: Float,
  amount_percent: Float,
  years: String,
  week_of_year: String)
```

画面11:
```scala
val date_info = args(0)
val weeks = getWeekRelativelyInterval(date_info).split(regex = "-")
val current = weeks(0).split(regex = "-")
val last = weeks(1).split(regex = "-")
```

画面12:
```scala
SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num,
ifnull((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
FROM (SELECT course_category_dim_id, sum(salesvolume) sale_num
FROM data_course.course_buy_dim
WHERE concat_ws('-',years,months,days) BETWEEN '${current(0)}' and '${current(1)}'
GROUP BY course_category_dim_id) as a
LEFT JOIN (
SELECT course_category_dim_id, sum(salesvolume) sale_num
FROM data_course.course_buy_dim
WHERE concat_ws('-',years,months,days) BETWEEN '${last(0)}' and '${last(1)}'
GROUP BY course_category_dim_id) as b
ON a.course_category_dim_id = b.course_category_dim_id
```

画面13:
```scala
subjectBuyAmountSql(Spark, current, last).createReplaceTempView(viewName = "salesvolume_biz_tmp")
```

画面14:
```sql
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_amount_week_biz
(course_category_dim_id String,
course_category_name string,
sale_amount Float,
amount_percent Float)
PARTITIONED BY (years string, week_of_year string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面14:
标题: 3.5.3 销售额
子标题: 3.5.3.1 周
子子标题: 3.5.3.1.1 统计分析步骤
内容:
1. 获取当前周的时间区间，例如：上周1至上周5
2. 获取上周的时间区间，例如：上周1至上周5
3. 获取本周的数据
4. 获取上周的数据
5. 计算增幅
6. 根据维度id获取相关数据
7. 保存结果
表格数据:
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_amount_week_biz
(course_category_dim_id String,
course_category_name string,
sale_amount Float,
amount_percent Float)
PARTITIONED BY (years string, week_of_year string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'

5) 无

