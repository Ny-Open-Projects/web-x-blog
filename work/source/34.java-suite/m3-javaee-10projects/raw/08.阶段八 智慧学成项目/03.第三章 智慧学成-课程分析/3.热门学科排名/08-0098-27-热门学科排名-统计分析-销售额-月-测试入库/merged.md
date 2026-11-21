# 27-热门学科排名-统计分析-销售额-月-测试入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\27-热门学科排名-统计分析-销售额-月-测试入库_【海量资源尽在 666java.com】.mp4
- 时长 3分24秒（音频 204s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前面上咱们已经基于认为学科排名中销售额的周的统计修改得到了销售额月的统计接下来呢就是对这个月的统计进行代码的一个测试咱们这里呢直接运行代码这里呢代码运行中咱们来HOE刷新等待这个代码然后返回咱们那个对应的一个结果这里呢代码还没有运行完这里还没有数据咱们
[00:31] 来观察控制台的日志来等待这里运行完成这里呢咱们统计的日期是10月份的日期它呢相对于它那个同比呢增幅是对的对应的是9月份的日期9月份的数据呢咱们在数据仓库里边相对来说比较少10月份的数据呢相对来说相对多一点这里呢咱们看到结果它的增幅已经达到这已经百分之
[01:04] 500%600%了还有800%的这里呢咱们改到11月改到11月呢因为10月的数据和11月的数据相对来说是对等了这里呢咱们再运行一遍看11月相对于10月它的增幅是多少这里呢咱们来刷新一下数据应该已经进来了这里的确数据已经进来这里呢已经达到600%的增长和500%的增长还有900%的增长
[01:37] 咱们呢等会儿看云计算和大数据在10月和11月的对比中相对于10月11月的增幅是多少这里呢还在计算中咱们等待它运行完成这里呢可以看到它正在根据咱们这个日期呢进行数据的读取好这里呢已经运行完成运行完成这里输出的数据相对来说比较少最多呢只有20条它也是默认是20条咱们呢来一期游戏进行一个查看
[02:15] 小心咱们来看大数据大数据的这个呢这条数据咱们来看是10月还是11月的这个呢还是10月的它的增幅呢是900%接下来咱们来看11月云计算大数据的数据是第24条24条往后走24条它这个地方已经是负增长了它11月相对于10月它呢负增长20%左右
[02:50] 因为10月和11月的数据是对等的但是呢9月和10月它俩的数据相对差别还是比较大的因为9月的数据比较少这里呢结果差距也是比较明显的好咱们回到文档经过对代码的一个测试咱们呢这里已经可以得到正确的结果到此呢热门学科排名中销售额的周统计和月统计就统计完成咱们呢课程
[03:20] 本节课程就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spark 应用程序如何读取原始数据、按月聚合计算并写入 Hive 表的过程，同时展示在 Hue 中查看结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Spark 代码，定义了日期范围（2019-10-25），并准备了月份数据。代码中包含 SQL 查询语句，用于从原始数据中选择课程类别ID、名称、销售金额、金额占比和年份。
画面 2: 在 Hue 的 Table Browser 中，显示了表 subject_amount_month_biz，但提示“该表不包含任何数据”。
画面 3: Spark 代码执行日志，显示了初始化对象存储、获取所有数据库等操作。
画面 4: Spark 代码执行日志，显示了任务调度、数据广播和任务提交等过程。
画面 5: Spark 代码执行日志，显示了正在读取文件，文件路径为 HDFS 上的原始数据。
画面 6: Spark 代码执行日志，显示了正在读取文件，文件路径为 HDFS 上的原始数据。
画面 7: 在 Hue 的 Table Browser 中，显示了表 subject_amount_month_biz 的样本数据，其中包含销售金额和金额占比等字段。
画面 8: Spark 代码执行日志，显示了获取数据库和表的操作。
画面 9: Spark 代码执行日志，显示了读取文件，文件路径为 HDFS 上的原始数据。
画面 10: Spark 代码执行日志，显示了读取文件，文件路径为 HDFS 上的原始数据。
画面 11: 在 Hue 的 Table Browser 中，显示了表 subject_amount_month_biz 的“Sample”标签页，列出了表的字段和分区信息。
画面 12: 在 Hue 的 Table Browser 中，显示了表 subject_amount_month_biz 的样本数据，其中包含销售金额和金额占比等字段。
画面 13: 在 Hue 的 Table Browser 中，显示了表 subject_amount_month_biz 的样本数据，其中包含销售金额和金额占比等字段。
画面 14: 展示了文档中的 SQL 语句，用于创建外部表 subject_amount_month_biz，包含字段 course_category_dim_id、course_category_name、sale_amount、amount_percent，分区字段为 years 和 month_of_year，存储格式为 PARQUET。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
def main(args: Array[String]): Unit = {
  import Spark.implicits._
  // 1. 读取当前月份的日期范围，例：1号至18号
  val date_info = "2019-10-25"
  val months = getMonthRelativeInterval(date_info).split(regex = "\\")
  val current = months(0).split(regex = "\\")
  val last = months(1).split(regex = "\\")
  // 2. 获取本月所有数据
  // 3. 读取上月数据
  // 4. 读取本月数据
  // 5. 计算指标
  subjectBuyAmountSql(Spark, current, last, createReplaceTempView, viewName = "sales_biz_month_tmp")
  // 6. 根据维度id获取相关数据
  val monthOfYear = Spark.sql("select
  a.course_category_dim_id,
  a.course_category_name,
  b.name as course_name,
  cast(a.sale_amount as float) as amount,
  cast(a.amount_percent as float) as amount_percent,
  a.year,
  a.month
  from sales_biz_month_tmp a
  join dim_course b on a.course_id = b.id
  where a.year = 2019 and a.month = 10
  group by a.course_category_dim_id, a.course_category_name, b.name, a.year, a.month
  order by a.course_category_dim_id, a.course_category_name, b.name, a.year, a.month
  ").collect()
  // 7. 保存结果
  val tmp = Spark.sql("select
  a.course_category_dim_id,
  a.course_category_name,
  b.name as course_name,
  cast(a.sale_amount as float) as amount,
  cast(a.amount_percent as float) as amount_percent,
  a.year,
  a.month
  from sales_biz_month_tmp a
  join dim_course b on a.course_id = b.id
  where a.year = 2019 and a.month = 10
  group by a.course_category_dim_id, a.course_category_name, b.name, a.year, a.month
  order by a.course_category_dim_id, a.course_category_name, b.name, a.year, a.month
  ").collect()
```
画面 14:
```sql
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_amount_month_biz
(course_category_dim_id String,
course_category_name String,
sale_amount Int,
amount_percent FLOAT)
PARTITIONED BY (years String, month_of_year String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
LOCATION '/user/Hive/external/data_subject/subject_amount_month_biz'
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14:
PPT 标题：3.5.3.2.1 统计分析步骤
表格数据：
| 字段名 | 类型 |
| --- | --- |
| course_category_dim_id | String |
| course_category_name | String |
| sale_amount | Int |
| amount_percent | FLOAT |
| years | String |
| month_of_year | String |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

