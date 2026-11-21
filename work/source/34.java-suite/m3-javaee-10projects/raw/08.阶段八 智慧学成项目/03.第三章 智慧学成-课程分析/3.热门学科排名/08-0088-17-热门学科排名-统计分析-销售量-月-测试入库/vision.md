# 画面线理解：17-热门学科排名-统计分析-销售量-月-测试入库

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\17-热门学科排名-统计分析-销售量-月-测试入库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:23, 00:40, 00:51, 01:21, 01:49, 02:02, 02:12, 02:17, 02:44, 02:56, 03:12, 03:33, 03:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:22:01

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark 中通过 Scala 代码动态分区创建 Hive 表，并在 Hue 中验证数据结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Scala 代码中定义了数据范围（2019年11月），并创建了一个名为 sales_volume_biz_month_tmp 的临时视图。
画面2：展示 Scala 代码中定义了 Spark SQL 查询语句，从数据表 data_subject.subject_sale_month_biz 中读取数据。
画面3：展示 Spark 作业启动日志，显示创建了临时目录并初始化了 Hive 客户端。
画面4：展示 Spark 作业执行日志，显示 Spark Web UI 已停止，作业成功完成。
画面5：在 Hue 中展示数据表 data_subject.subject_sale_month_biz 的样本数据，包含课程类别、销售额、百分比、年份和月份。
画面6：展示 Scala 代码中定义了动态分区模式，并执行了创建视图的操作。
画面7：在 Hue 中展示数据表 data_subject.subject_sale_month_biz 的样本数据，包含课程类别、销售额、百分比、年份和月份。
画面8：展示 Spark 作业执行日志，显示任务正在运行并完成。
画面9：展示 Spark 作业执行日志，显示 Spark Web UI 已停止，作业成功完成。
画面10：展示 Scala 代码中定义了动态分区模式，并执行了创建视图的操作。
画面11：在 Hue 中展示数据表 data_subject.subject_sale_month_biz 的样本数据，包含课程类别、销售额、百分比、年份和月份。
画面12：在 Hue 中展示数据表 data_subject.subject_sale_month_biz 的样本数据，包含课程类别、销售额、百分比、年份和月份。
画面13：在 Hue 中展示数据表 data_subject.subject_sale_month_biz 的样本数据，包含课程类别、销售额、百分比、年份和月份。
画面14：展示 PDF 文档中关于学生人数的统计分析内容，包含课程类别、销售额、百分比、年份和月份。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```scala
object SubjectSalesVolumeByMonthBiz {
  // Spark session
  val spark: SparkSession = SparkSession.builder().appName("SubjectSalesVolumeByMonthBiz").getOrCreate()

  def main(args: Array[String]): Unit = {
    import spark.implicits._
    // 2. 获取当前日期
    val date_info = "2019 11 11"
    val months = getMonthRelativeInterval(date_info).split(regexp = " ")
    val current = months(0).split(regexp = " ")
    val last = months(1).split(regexp = " ")
    // 3. 获取本月数据
    subjectBuyCountSql(spark, current, last).createOrReplaceTempView(viewName = "sales_volume_biz_month_tmp")
    // 4. 获取本月销售额
    val monthOfYear = getMonthOfYear(current(0).split(regexp = " "))
    val slds = spark.sql(
      s"""
         |select * from sales_volume_biz_month_tmp
         |""".stripMargin
    )
    slds.show()
  }
```

画面2：
```scala
  // 1. 查询
  spark.sql(s"select * from data_subject.subject_sale_month_biz").show()
```

画面6：
```scala
  // 7. 动态分区
  spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
  slds.repartition(numPartitions = 1)
```

画面10：
```scala
  // 7. 动态分区
  spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
  slds.repartition(numPartitions = 1)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
PPT标题：3.5.1.2.3 工具类
表格数据：
| course_category_dim_id | course_category_name | sale_num | sale_percent | years | month_of_year |
|------------------------|----------------------|----------|--------------|-------|---------------|
| 1-12                    | 产品经理            | 283      | 0.07213114947080612 | 2019   | 11            |
| 1-8                     | 游戏开发            | 84       | 0.2000000292823224   | 2019   | 11            |
| 1-11                    | 移动开发            | 195      | 0.0268157896697212   | 2019   | 11            |
| 1-13                    | 前端开发            | 388      | 0.037403790231682    | 2019   | 11            |
| 1-17                    | UI设计              | 301      | 0.08787878600743149  | 2019   | 11            |
| 1-18                    | 系统运维            | 171      | 0.0604299665627221   | 2019   | 11            |
| 1-19                    | 研发管理            | 134      | 0.1779141128065202   | 2019   | 11            |
| 1-20                    | 数据库              | 310      | 0.047297298082364    | 2019   | 11            |
| 1-21                    | 云计算/大数据       | 87       | 0.1470588235294118   | 2019   | 11            |
| 1-22                    | 智能硬件/物联网     | 277      | 0.1206439289590994   | 2019   | 11            |
| 1-23                    | 企业办公/市场      | 152      | 0.048275618812193    | 2019   | 11            |
| 1-24                    | 人工智能            | 107      | 0.00943396240472736  | 2019   | 11            |
| 1-25                    | 信息安全            | 270      | 0.01098901126337407  | 2019   | 11            |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
