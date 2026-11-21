# 16-热门学科排名-统计分析-销售量-月-统计分析步骤及代码编写

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\16-热门学科排名-统计分析-销售量-月-统计分析步骤及代码编写_【海量资源尽在 666java.com】.mp4
- 时长 8分37秒（音频 517s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前边呢,咱们已经按周统计分析了热门学科排名中的销售量,接下来呢,咱们按月统计这里的销售量,这里统计销售量呢,使用的基础数据还是课程购买量章节已经清洗好的DWM层的数据,采用的计算方式呢,就是增幅的计算方式呢,还是同比的计算方式,这里清洗的步骤和咱们
[00:31] 按周清洗步骤基本是一样的唯一的区别呢就是在日期处理上这里呢按月处理的时候是以月为单位来获取区间获取之后呢计算相应的一个涨幅APP层的结构呢也是有一点不一样就是咱们最后的一个分区前面保存的就是学科ID学科名销售量以及涨幅都是一样的包括咱们的分区年最后呢
[01:01] 按周为单位统计的时候这里是年中的周但是呢咱们按月的时候这里边就是年中的月这里由于咱们这个统计分析步骤是一样的只有在这个日期处理上有一个细微的差别咱们代码的重合度也是比较高的这里呢咱们直接在周的基础上进行一个修改得到咱们月的代码就是按月统计的代码咱们来切到开发工具上
[01:33] 通过本节的学习呢,咱们需要掌握,咱们需要掌握按月来统计分析课程,认为课程排名里边的销售量,这里呢,咱们直接把它给复制了,复制完成之后呢,这个地方需要改名,它那是月,这个名字复制一下,这个时候呢,把这个名字也改一下,咱们呢,学科是按月这个地方改一下。
[02:07] 按月来统计咱们这个销售量按月统计销售量咱们这里的区间需要改变的是谁啊这个地方的话就不是就不是安州了咱们就把这个咱们把对应的注释给复制过来这里呢咱们是没有占过来这里呢咱们就是按月来处理按月来处理呢这里工具类也已经写好了对应按月来获取日期的一个数据
[02:42] 咱们呢直接修改就行这个呢也修改一下按月按月来处理数据其他的其他的像基本上都是一样的咱们不用怎么修改这里呢首先还是存自上向下自上向下进行一个代码的一个修改这个地方原来是按钩现在呢需要按月咱们呢这个地方是有一个按月来获取数据的一个方法这个呢咱们把这个方法给导进来
[03:14] 导进来这个地方其实你直接替换就行了这个导进来之后只用改个方法名这个时候呢你全九月咱们就是按照九月和八月的这个数据但是咱九月是不是数据非常少吗咱们还按照双十一这个时间来处理月的这个数量有了这个变量呢咱们也对应的修改一下因为如果你这个地方还是周它回头的话你在后边再回来看代码的时候
[03:45] 你可能就忘了这个地方是一个怎么样的一个回事这个地方修改完成之后呢咱们这个地方就获取的不是年终的周了就获取的是年终的月这里是月咱们把变量也改一下month这个呢获取的是月的数据咱们看有这个方法没直接导这个方法是存在的但是呢还是保险期间咱们来确认一下它的参数
[04:19] 给它一个DataNameFile然后返回的是年然后横杠加上月那这个地方咱们就可以直接来使用了这个地方修改一下这个地方也一定要修改这个地方是啥它就不是周在年中的周了这个地方年中的月咱们来看一下这个地方的变量名MouseOfAyr咱们把它给修改一下这个修改完接下来还要修改的是啥
[04:50] 是不是要修改咱们的一个保存的表明以及咱们这个实体了来改一下改完之后呢咱们来导个包这个地方也是一样的这个地方改成month改完之后呢到此咱们按月来统计咱们这个销售量就结束了这个地方呢咱们就可以直接进行一个测试了
[05:24] 但是呢这个地方咱们再确认一下这个表明是否正确防止这个表明回头写错了也是麻烦咱们这个地方是销售量month好这个地方是正确的这个只要这个表明写正确咱们后边咱们往里边保存数据的时候就是OK的改完之后呢咱们再来确认一下自上向下再检查一下代码因为咱们这个代码呢是修改的修改的情况下呢防止发生那个变量的错误
[05:57] 导致咱们的数据是错误的咱们再来排查一遍代码首先是日期的获取这里咱们是有现成的工具类这里获取两个月相对的时间这工具类已经封装好咱们是不用担心接下来是根据咱们这个日期把当前的月和上月给取过来这个在这个地方它也是以逗号进行切割的咱们直接进行一个切割然后分别获取到当月和上月就行了
[06:28] 接下来呢是根据查询这个呢根据咱们传递的日期进行一个查询然后呢计算它的涨幅这个地方是咱们抽取的工具类它是一个公共的代码只要你前边这个日期传的是对的这个结果计算出来就是对的这个呢也没有问题这个地方是一个临时表咱们呢在计算的时候这个地方有一个临时表改一下名字吧因为咱们前边是有一个什么了已经有一个
[06:58] 有一个按周统计的是这样的这个地方呢再加一个按月统计的防止啊到时间重名重名的时候如果两个程序同时运行它这个地方是用了replace它会把它给覆盖掉这里呢就是month这个地方改完之后咱们需要将这个里边也改了因为咱们这个地方呢表明要保持统一表明保持统一咱们才能确准咱们的结果是正确的这个代码呢
[07:27] 因为咱们这个地方封装值这个位置是关键其他呢都是一样的咱们封装值唯一不一样的只有只有这个分区月这个字段不一样其他的字段也是一样的所以说只要咱们确认这个表明其他的就是这个分区咱们这个月这个分区确定正确那这块代码也是没有问题的然后呢咱们还把这个最终那个封装的实体给修改了也修改成了咱们自己正常的这个实体
[07:55] 这个修改完成之后呢,咱们就是保存,保存的时候咱们也已经在咱们的HUE上确认过,这个地方呢,命名规则是OK的,只用把中间那个WIC换成MOS,然后就OK,换成OK之后呢,这个地方再查一下,然后呢,这个地方只要确认完成,咱们就是代码就是没有问题的。
[08:19] 好,以上呢,就是咱们按月统计的一个步骤,以及咱们代码,这个代码呢,由于重合度非常高,
[08:27] 咱们直接采用修改周的方式把这个代码给修改了一下好 视频就到这里测试交给下一个视频

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark 编写月度销售数据统计分析程序，包括数据表结构定义、SQL 查询语句和 Scala 代码实现。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程文档中“3.5.1.2 APP层数据结构”的 SQL 代码，定义了 `data_subject.subject_sale_month.biz` 表。
画面2：展示 `SubjectSalesVolumeByWeekBiz.scala` 文件，包含获取当前周数据的 Scala 代码。
画面3：展示课程文档中“3.5.1.2 月”章节的分析步骤和数据结构。
画面4：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含获取月度数据的 SQL 查询语句和写入操作。
画面5：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含获取月度数据的 Scala 代码。
画面6：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含获取月度数据的 SQL 查询语句。
画面7：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含写入数据和查看结果的 Spark 操作代码。
画面8：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含获取月度数据的 Scala 代码。
画面9：展示 `DateUtils.scala` 文件，包含 `getMonthRelativeInterval` 方法的实现，用于计算月份间隔。
画面10：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含获取月度数据的 Scala 代码。
画面11：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含写入数据和查看结果的 Spark 操作代码。
画面12：展示 `Subject.scala` 文件，定义了 `SubjectSaleMonthBiz` 和 `SubjectSaleMonthWith` 两个 case class。
画面13：展示课程文档中“3.5.1.2.3 统计分析代码”的 Scala 代码，包含导入包和类定义。
画面14：展示 `SubjectSalesVolumeByMonthBiz.scala` 文件，包含获取月度数据的 Scala 代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_sale_month.biz
(course_category_dim_id String,
course_category_name String,
sale_num INT,
sale_percent FLOAT)
PARTITIONED BY (Years String, month_of_year String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
Location "/user/Hive/external/data_subject/subject_sale_month_biz"

画面4：
val sld5 = Spark.sql(
  """
    |select
    |a.course_category_dim_id,
    |b.name course_category_name,
    |cast(a.sale_num as int) sale_num,
    |cast(a.sale_percent as float) sale_percent,
    |$monthOfYear(0) years,
    |$monthOfYear(1) month_of_year
    |from salesvolume_biz tmp a
    |left join data_dimen.course_category_dim b
    |on a.course_category_dim_id = b.course_category_dim_id
    |""".stripMargin).as[SubjectSaleMonthBiz]

画面7：
Spark.conf.set("Hive.exec.dynamic.partition.mode", "nonstrict")
sld5.repartition(numPartitions = 1)
sld5.write.mode(saveMode = "overwrite")
sld5.insertInto(tableName = "data_subject.subject_sale_month_biz")
Spark.sql("select * from data_subject.subject_sale_month_biz").show()
Spark.close()

画面12：
case class SubjectSaleMonthBiz(course_category_dim_id: String,
  course_category_name: String,
  sale_num: Int,
  sale_percent: Float,
  years: String,
  month_of_year: String)

画面13：
package cn.itcast.xc.analysis.subject.salesvolume
import cn.itcast.xc.common.EtlEnvironment
import cn.itcast.xc.entity.SubjectSaleMonthBiz
import cn.itcast.xc.utils.DateUtils.{getMonthNum, getMonthRelativeInterval}
import cn.itcast.xc.utils.SubjectUtils.subjectBuyCountSql
import org.apache.Spark.sql.SparkSession

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题“3.5.1.2 APP层数据结构”，内容包含 SQL 代码。
画面3：PPT标题“3.5.1.2 月”，内容包含分析步骤和数据结构。
画面13：PPT标题“3.5.1.2.3 统计分析代码”，内容包含 Scala 代码。

5) 不要评价画面美观，不要输出与课程无关的内容。

