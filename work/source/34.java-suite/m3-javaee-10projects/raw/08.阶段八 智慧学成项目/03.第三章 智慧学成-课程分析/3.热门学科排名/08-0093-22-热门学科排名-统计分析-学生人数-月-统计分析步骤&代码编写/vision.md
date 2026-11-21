# 画面线理解：22-热门学科排名-统计分析-学生人数-月-统计分析步骤&代码编写

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\22-热门学科排名-统计分析-学生人数-月-统计分析步骤&代码编写_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:34, 01:06, 01:30, 01:50, 02:14, 02:19, 03:04, 03:24, 03:28, 03:41, 04:12, 04:34, 04:54, 05:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:26:23

1) 这一组画面整体在讲如何使用 Spark 编写代码，将按月维度的用户数据从临时表写入到 Hive 的外部表中。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程文档，说明统计分析步骤和APP层数据结构，包含创建外部表的SQL语句。
画面2：展示IDE中Spark代码，定义了获取当月时间区间、设置视图名、创建临时视图的逻辑。
画面3：展示IDE中Spark代码，定义了SparkSession和main函数，设置当月时间区间。
画面4：展示IDE中Spark代码，设置当月时间区间为“2019-11-11”。
画面5：展示IDE中Spark代码，设置当月时间区间为“2019-11-11”，并定义了months变量。
画面6：展示IDE中Spark代码，定义了monthOfYear变量，用于获取年份和月份。
画面7：展示Hue界面，显示了subject_user_week_biz表的数据，包含课程类别、用户数、用户占比、年份和月份等字段。
画面8：展示IDE中Spark代码，定义了当月时间区间为“2019-11-11”。
画面9：展示IDE中Spark代码，定义了monthOfYear变量，用于获取年份和月份。
画面10：展示IDE中Spark代码，定义了当月时间区间为“2019-11-11”。
画面11：展示IDE中Spark代码，定义了当月时间区间为“2019-11-11”。
画面12：展示IDE中Spark代码，定义了SparkSQL查询语句，从learn_biz_month_tmp表中选择数据，并与课程维度表进行左连接。
画面13：展示IDE中Spark代码，设置Hive执行动态分区模式，设置写入模式为“overwrite”，并执行写入操作。
画面14：展示课程文档，说明测试数据和统计分析步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_user_month_biz
(course_category_dim_id String,
course_category_name String,
user_num Int,
user_percent FLOAT)
PARTITIONED BY (years String, month_of_year String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
LOCATION '/user/hive/external/data_subject/subject_user_month_biz';

画面6：
val monthOfYear = getMonthNum(current(0).split(regex = "*"))
val learnDS = spark.sql(
  """
  select
  a.course_category_dim_id,
  b.name course_category_name,
  cast(a.user_num as int) user_num,
  cast(a.user_percent as float) user_percent,
  $(monthOfYear(0)) years,
  $(monthOfYear(1)) month_of_year
  from learn_biz_month_tmp a
  left join data_dimen.course_category_dim b
  on a.course_category_dim_id = b.course_category_dim_id
  """ .stripMargin
)

画面12：
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
learnDS.repartition(numPartitions = 1)
.write.mode(saveMode = "overwrite")
.insertInto(tableName = "data_subject.subject_user_month_biz")

画面13：
spark.sql(sqlText = "select * from data_subject.subject_user_month_biz").show()
spark.close()

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
标题：3.5.2.2.1 统计分析步骤
内容：3.3、3.4章节已经采集清洗了DWD层数据（参考：3.3数据采集、3.4数据清洗），这里直接复用使用，统计还是非常简单的根据时间范围执行了，比较麻烦的是根据时间同比增加，步骤如下：
1. 获取当月的时间区间，例如：1号至18号
2. 获取上月的相同时间区间，例如：上月1号至上月18号
3. 获取本月的数据
4. 获取上月的数据
5. 计算指标
6. 根据维度id获取相关数据
7. 保存结果

画面14：
标题：3.5.2.1.3 测试
内容：开发工具中直接运行代码如下：
| course_category_dim_id | course_category_name | user_num | user_percent | years | week_of_year |
|------------------------|----------------------|----------|--------------|-------|--------------|
| 1-12                   | 产品经理             | 1813     | 0.823715414   | 2019   | 27           |
| 1-2                    | 游戏开发             | 1525     | 0.817344986   | 2019   | 27           |
| 1-2                    | 移动开发             | 1601     | -0.074608535  | 2019   | 27           |
| 1-7                    | UI设计               | 2747     | 0.980656486   | 2019   | 27           |
| 1-7                    | 程序开发             | 1173     | -0.920668113  | 2019   | 27           |
| 1-3                    | 系统运维             | 1381     | 0.810998965   | 2019   | 27           |
| 1-10                   | 研发管理             | 2088     | 0.962392621   | 2019   | 27           |
| 1-9                    | 云计算/大数据        | 2245     | -0.090459263  | 2019   | 27           |
| 1-6                    | 智能硬件/物联网      | 2393     | 0.864196393   | 2019   | 27           |
| 1-13                   | 企业/办公/电商       | 2852     | 0.816588716   | 2019   | 27           |
| 1-14                   | 人工智能             | 2799     | -0.064268943  | 2019   | 27           |

5) 不要评价画面美观，不要输出与课程无关的内容。
