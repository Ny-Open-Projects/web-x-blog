# 画面线理解：02-ETL-数据清洗-课程访问量清洗-获取维度数据&原始数据

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\02-ETL-数据清洗-课程访问量清洗-获取维度数据&原始数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:29, 00:52, 02:56, 04:06, 05:23, 06:34, 06:58, 07:35, 09:37, 10:18, 10:47, 11:14, 11:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:49:47

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Scala 中编写数据清洗代码，通过 Spark SQL 读取维度表数据并进行转换，最终将结果写入文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：显示课程大纲，当前章节为“4.4.3 清洗代码”，并展示代码文件开头部分，包含包声明和导入语句。
画面2：继续展示“4.4.3 清洗代码”章节，代码中定义了 Spark Session。
画面3：在 IDEA 中，通过“Search Everywhere”功能搜索并创建名为“VisitSourceToFact”的 Scala 类。
画面4：展示“4.4.2 数据清洗分析”章节内容，包含事实表字段与维度表字段的映射关系表。
画面5：在 Hue 界面中，浏览“data_dimen”数据库下的表结构。
画面6：在 IDEA 中，为“VisitSourceToFact”类添加注解，提示需要的参数。
画面7：在 IDEA 中，编写 Spark SQL 语句，从“data_dimen.area_dim”表中选择所有字段并转换为“areaDimen”类型。
画面8：在 IDEA 中，继续编写代码，将上一步的 Spark SQL 语句中的字段映射为“areaDimen”类型。
画面9：在 IDEA 中，为 Spark SQL 语句添加映射函数，将“city_name”字段映射为“area_dim_id”。
画面10：在 Hue 界面中，执行 SQL 查询，查看“course_dim.course_dim_id”和“course_dim.name”字段的数据。
画面11：在 IDEA 中，编写代码，从“data_dimen.course_dim”表中选择“course_dim_id”和“company_id”字段。
画面12：在 IDEA 中，继续编写代码，将“course_dim_id”字段映射为“courseDim”类型。
画面13：在 IDEA 中，编写代码，创建 Spark Context 并调用 textFile 方法。
画面14：在 IDEA 中，为 textFile 方法指定文件路径，并设置日期格式。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
package cn.itcast.xc.analysis
import cn.itcast.xc.common.ETLEnvironment
import cn.itcast.xc.entity.{AreaDimen, CourseDimen, CourseVisitFact}
import cn.itcast.xc.utils.DataUtils.getAreaStr
import cn.itcast.xc.utils.Iputils.getArea
import cn.itcast.xc.utils.Strutils.getUid

画面2：
package cn.itcast.xc.analysis
import cn.itcast.xc.common.ETLEnvironment
import cn.itcast.xc.entity.{AreaDimen, CourseDimen, CourseVisitFact}
import cn.itcast.xc.utils.DataUtils.getAreaStr
import cn.itcast.xc.utils.Iputils.getArea
import cn.itcast.xc.utils.Strutils.getUid

画面3：
无代码，为 IDE 操作界面。

画面4：
课程访问事实表字段 | 对应维度表字段 | 字段说明
course_visit_fact_id | - | 课程访问事实表主键，uid自动生成
course_dim_id | course_id | 课程id，课程维度表中获取
time_dim_id | time_id | 时间维度id，也可根据访问时间自动生成
area_dim_id | client_ip | 区域id，根据用户ip，在公司维度表中获取公司id
company_dim_id | course_id | 公司id，根据课程id，在公司维度表中获取公司id
client_ip | client_ip | 用户ip
client_sessionid | session_id | 用户会话id
client_type | user_agent | 浏览器类型
visit_time | visit_time | 访问时间
years | visit_time | 访问时间-年（也可根据时间维度）
months | visit_time | 访问时间-月（也可根据时间维度）
days | visit_time | 访问时间-天（也可根据时间维度）

画面5：
无代码，为 Hue 界面。

画面6：
object VisitSourceToFact {
  // 初始化Spark session
  val spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
  def main(args: Array[String]): Unit = {
  }
}

画面7：
val spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].collect()
}

画面8：
val spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].collect()
}

画面9：
val spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  var areaMap = Map[String, String]()
  spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
}

画面10：
无代码，为 Hue 界面。

画面11：
val spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  import spark.implicits._
  var areaMap = Map[String, String]()
  spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
  var compMap = Map[String, String]()
  spark.sql("SELECT * FROM data_dimen.course_dim").as[CourseDimen].map(x => {
    compMap += (x.course_dim_id -> x.company_id.toString)
  })
}

画面12：
val spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  import spark.implicits._
  var areaMap = Map[String, String]()
  spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
  var compMap = Map[String, String]()
  spark.sql("SELECT * FROM data_dimen.course_dim").as[CourseDimen].map(x => {
    compMap += (x.course_dim_id -> x.company_id.toString)
  })
}

画面13：
val spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  import spark.implicits._
  var areaMap = Map[String, String]()
  spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
  var compMap = Map[String, String]()
  spark.sql("SELECT * FROM data_dimen.course_dim").as[CourseDimen].map(x => {
    compMap += (x.course_dim_id -> x.company_id.toString)
  })
  val sc = spark.sparkContext
  sc.textFile(path)
}

画面14：
val spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  import spark.implicits._
  var areaMap = Map[String, String]()
  spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
  var compMap = Map[String, String]()
  spark.sql("SELECT * FROM data_dimen.course_dim").as[CourseDimen].map(x => {
    compMap += (x.course_dim_id -> x.company_id.toString)
  })
  val sc = spark.sparkContext
  sc.textFile("/user/hive/external/data_course/course_visit/2015-11-04")
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：表格数据，包含“课程访问事实表字段”、“对应维度表字段”和“字段说明”三列。
画面10：Hue 界面中，显示“course_dim.course_dim_id”和“course_dim.name”字段的数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
