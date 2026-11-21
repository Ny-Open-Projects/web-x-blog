# 10-课程分析-课程访问量分析-步骤2：课程访问量统计求和

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\10-课程分析-课程访问量分析-步骤2：课程访问量统计求和_【海量资源尽在 666java.com】.mp4
- 时长 6分27秒（音频 387s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 这里呢,咱们已经读取了课程防御量事实表的数据,接下来呢,咱们就是根据日期以天为单位进行一个求核计算,得到每天的,得到咱们那个DataInfo这天的一个防御量,就是咱们传过来的日期是哪一天,就得到哪一天的一个防御量,这个时候呢,咱们要求核的时候,求核的时候呢,需要将上面的结果给接收一下。
[00:30] 然后咱们这里给它一个变量叫做VZDF因为这个circle的返回的数据类型是DataForm这个地方以DataDF进行结尾做一个标识这里呢咱们求和就可以进行一个GrabBy然后指定字段进行一个求和咱们刚才说了咱们的日期是什么呀是这个以这个为单位进行求和了
[01:00] 但是咱们slide星就是在咱们事实表里边所有的字段里边有这样的格式吗是没有的咱们在这个hue上这个地方已经看过了这是没有的而且咱们之前分析过没有这样的字段但是咱们在过滤日期的时候是不是通过连接咱们分区年月日得到了一个这样的字段呢就是和咱们这个data info一样的数据格式的一个字段
[01:31] 咱们来切到文档上来看一下咱们就是APP层最终的保存格式是什么是不是DataInfo然后它接下来是具体的一个访问量然后是分区咱们这个地方进行一个数据获取的时候这个地方对应一个实体的时候实体也是这样的实体上已经告诉咱们咱们的格式是不是要是这样的然后它这个地方也是根据分区进行一个保存
[02:00] 那么这样的一个情况下,咱们是不是这个日期就可以直接使用了?
[02:06] 这个咱们拼接号的格式,在输出的时候我就不用输出slot星,然后直接使用,我就把它给as为,起一个别名就叫data音号,因为这个data音号和咱们最终数据仓库里面的这个是对应上的,然后呢它是需要一个什么呀,需要一个技术,
[02:27] 技术的话咱们这个地方有了DataInfo就可以使用DataInfo进行一个GraphyGraphy完了之后呢咱们需要技术就使用Count进行一个操作到这呢其实咱们这个技术还不算完咱们来看咱们的这个数据结构这个地方是不是还有分区呢分区的年月日是不是还没有呢咱们前面这个地方只要了谁呀只要了咱们的DataInfoDataInfo这个地方是一个拼接
[02:56] 但是呢这个地方咱们Galaxy Proby的时候你Galaxy Proby几个字段你最终是不是就得到几个字段呢你Galaxy Proby一个字段加上一个Count也就是说一个字段加一个具体的值咱们这个地方其实可以输出来看一下它呢需要一个变量来接受一下这是咱们的一个求和的一个结果就是咱们统计后的一个结果就叫Count这个时候呢咱们其实可以把这个Count给输出一下
[03:25] 因为你这个地方格式书面一个字段它肯定是根据这一个字段然后得到一个统计结果咱们这个日期呢11月11号咱们来HUE看一下这个日期有没有看这个日期有没有呢其实直接看咱们的分区就行了咱们是根据年月日进行分区的如果这个分区存在就说明这个数据肯定是有的这里呢有11号最新的日期是18号后面的就不看了只要确认它11号有就行了咱们再切到开发工具
[03:55] 这里呢咱们就可以直接运行看一下结果它的结果的话按照咱们的推测它应该是一个data info然后得到一个具体的值这个地方比如说是123吧这就得到一个具体的值它的输出结果是这样的咱们推断正确的情况下它是这样的但是呢咱们还需要什么还需要分区年月日这个地方其实咱们还需要把啥给加上把分区年月日给加上
[04:32] 咱们等待这个结果看咱们的推断是否正确走起好这个地方已经得到结果具体的日期有然后具体的访问值也有但是没有啥没有分区所以说咱们这个地方还要把分区给加上分区给加上的话咱们直接在这里边取它对应的字段就行了在这个地方加一个逗号逗号完了之后呢咱们是年月日年月日这个地方格尔布拜的时候你
[05:03] 虽然说Galaxy One这一个字段就行了但是咱们需要什么咱们需要年月日的分区也需要把这三个字段给拿过来这里我就直接粘过来它需要一个双引号它也需要它也需要这个时候咱们Galaxy One之后就是带分区的就是咱们数据仓库中最终带分区的这种咱们来执行一下看效果
[05:38] 这里呢程序已经在编译运行了咱们稍微等待一下看咱们这个日期加分区年月日加上咱们统计的值这个推算是否正确这个地方呢它就变成了2019然后呢11-11这是最后咱们的一个统计的值方便区分的话中间加一个数个大概是这五个字段
[06:12] 好,结果已经出来,和咱们预想的一模一样,这个时候呢,咱们的这个统计结果就是咱们需要的了。
[06:21] 好,咱们求和的步骤呢,就讲解到这里。

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark SQL 从 Hive 表中按日期维度聚合课程访问量，并将结果展示出来。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Scala 代码，定义 SparkSession，设置日期变量，构建 SQL 查询语句，准备从 Hive 表 data_course.course_visit_fact 中按日期维度聚合访问量。
画面2：展示 PPT 内容，标题为“1.1.2 APP层数据结构”，包含 Hive 表创建语句（CREATE EXTERNAL TABLE）和对应的 Scala 案例类定义（case class CourseVisitBiz）。
画面3：展示 PPT 内容，标题为“1.1.3 编写代码”，展示 Scala 案例类定义（case class CourseVisitBiz）。
画面4：在 Scala 代码中，右键选中变量 visitDF，弹出菜单选择“Generate...”并点击“Generate Scala Code”。
画面5：展示 Hue 界面，显示 Hive 表 data_course.course_visit_fact 的数据，按日期分区展示。
画面6：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面7：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面8：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面9：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面10：展示 PPT 内容，标题为“1.1.3 编写代码”，展示 Scala 案例类定义（case class CourseVisitBiz）。
画面11：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面12：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面13：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。
画面14：在 Scala 代码中，将 SQL 查询语句修改为聚合语句，变量 visitCount 被赋值。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```scala
object CourseVisitProcessByDay {
  def main(args: Array[String]): Unit = {
    val Spark: SparkSession = SparkSession.builder()
      .appName("CourseVisitProcessByDay")
      .config("Spark.sql.warehouse.dir", "hdfs://node1:8020/user/Hive/warehouse")
      .config("Spark.sql.catalogImplementation", "Hive")
      .enableHiveSupport()
      .getOrCreate()

    val date_info = "2020-11-11"
    val visitDF = Spark.sql(s"select concat_ws('-',years,months,days) as date_info from data_course.course_visit_fact where concat_ws('-',years,months,days) = '$date_info'")
    // 2. 查询
    // 3. 展示
    // 4. 关闭资源
    Spark.close()
  }
}
```

画面2：
```sql
CREATE EXTERNAL TABLE IF NOT EXISTS data_course.course_visit_biz (
  date_info String,
  count INT
)
PARTITIONED BY (years String, months String, days String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
LOCATION '/user/Hive/external/data_course/course_visit_biz';
```

画面3：
```scala
case class CourseVisitBiz(date_info: String,
  count: Int,
  years: String,
  months: String,
  days: String)
```

画面6：
```scala
val visitCount = visitDF.groupBy(col = "date_info").count()
visitCount.show()
```

画面10：
```scala
package cn.itcast.xc.analysis.visit
```

画面11：
```scala
val visitCount = visitDF.groupBy(col = "date_info", cols = "years", "months", "days").count()
visitCount.show()
```

画面12：
```scala
val visitCount = visitDF.groupBy(col = "date_info", cols = "years", "months", "days").count()
visitCount.show()
```

画面13：
```scala
val visitCount = visitDF.groupBy(col = "date_info", cols = "years", "months", "days").count()
visitCount.show()
```

画面14：
```scala
val visitCount = visitDF.groupBy(col = "date_info", cols = "years", "months", "days").count()
visitCount.show()
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面2：
标题：1.1.2 APP层数据结构
内容：
- Hive 表创建语句（CREATE EXTERNAL TABLE）
- 对应实体类（case class CourseVisitBiz）定义

画面3：
标题：1.1.3 编写代码
内容：
- Scala 案例类定义（case class CourseVisitBiz）

画面10：
标题：1.1.3 编写代码
内容：
- Scala 包声明（package cn.itcast.xc.analysis.visit）

5) 无

