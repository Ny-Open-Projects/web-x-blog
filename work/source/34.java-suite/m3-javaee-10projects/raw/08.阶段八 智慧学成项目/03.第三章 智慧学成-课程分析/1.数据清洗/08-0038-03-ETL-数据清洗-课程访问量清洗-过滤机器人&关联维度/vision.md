# 画面线理解：03-ETL-数据清洗-课程访问量清洗-过滤机器人&关联维度

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\03-ETL-数据清洗-课程访问量清洗-过滤机器人&关联维度_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:44, 02:39, 04:13, 05:11, 05:50, 06:58, 08:14, 09:21, 10:37, 12:42, 14:44, 15:06, 15:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:50:41

1) 这一组画面整体在讲如何使用 Spark 编写代码，对课程访问数据进行清洗、转换和聚合，生成事实表。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Spark 代码，定义了两个 Map 变量 areaMap 和 compMap，分别用于映射城市和公司维度，以及读取 Hive 表数据的 SQL 语句。代码中定义了 val date_info = "2019-11-04" 和 val input = sc.textFile(path = s"/user/hive/external/data_course/visit_source/${date_info}")。
画面2：展示 PPT 页面，标题为“4.4.2 数据清洗分析”，表格列出了课程访问事实表字段与对应维度表字段的映射关系。
画面3：展示 Spark 代码，继续编写数据清洗逻辑，使用 .map(_.split(regex = "t")) 分割数据行，并使用 .filter(arr => arr.contains("Robot")) 过滤掉机器人访问记录。
画面4：展示 Spark 代码，继续编写数据清洗逻辑，使用 .map(_.split(regex = "t")) 分割数据行，并使用 .filter(arr => arr.contains("Robot")) 过滤掉机器人访问记录。
画面5：展示 Scala 代码，定义了 case class CourseVisitFact，包含 course_visit_fact_id、course_dim_id、time_dim_id、area_dim_id、company_dim_id、client_ip、client_sessionid、user_agent、client_type、visit_time、years、months、days 等字段。
画面6：展示项目结构，选中了 target 目录下的 pom.xml 文件。
画面7：展示 Hue 数据浏览器界面，显示了 /user/hive/external/data_course/course_visit_source/2019-11-04/... 的数据文件内容，包含访问记录的详细信息。
画面8：展示 Spark 代码，定义了 object VisitSourceToFact，包含 Spark 会话和主函数，以及两个 Map 变量 areaMap 和 compMap。
画面9：展示 Spark 代码，继续编写数据清洗逻辑，使用 .map(_.split(regex = "t")) 分割数据行，并使用 .filter(arr => arr.contains("Robot")) 过滤掉机器人访问记录。
画面10：展示 Spark 代码，继续编写数据清洗逻辑，使用 .map(_.split(regex = "t")) 分割数据行，并使用 .filter(arr => arr.contains("Robot")) 过滤掉机器人访问记录。
画面11：展示 PPT 页面，标题为“2.3.1 ODS层数据结构”，表格列出了事实表字段、维度表字段、数据格式和数据样例。
画面12：展示 Spark 代码，继续编写数据清洗逻辑，使用 .map(_.split(regex = "t")) 分割数据行，并使用 .filter(arr => arr.contains("Robot")) 过滤掉机器人访问记录。
画面13：展示 Spark 代码，继续编写数据清洗逻辑，使用 .map(_.split(regex = "t")) 分割数据行，并使用 .filter(arr => arr.contains("Robot")) 过滤掉机器人访问记录。
画面14：展示 Spark 代码，继续编写数据清洗逻辑，使用 .map(_.split(regex = "t")) 分割数据行，并使用 .filter(arr => arr.contains("Robot")) 过滤掉机器人访问记录。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1：
val spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  import spark.implicits._
  var areaMap = Map[String, String]()
  spark.sql(sqlText = "SELECT * FROM data_dimen.area_dim").as[AreaDim].map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
  var compMap = Map[String, String]()
  spark.sql(sqlText = "SELECT * FROM data_dimen.course_dim").as[CourseDim].map(x => {
    compMap += (x.course_dim_id -> x.company_id)
  })
  val sc = spark.sparkContext
  val date_info = "2019-11-04"
  val input = sc.textFile(path = s"/user/hive/external/data_course/visit_source/${date_info}")
}

画面2：
课程访问事实表字段 | 对应维度表字段 | 字段说明
--|--|--|
course_visit_fact_id | - | 课程访问事实表主键，id自动生成
course_dim_id | course_id | 课程id，课程维度表主键
time_dim_id | time_dim_id | 时间维度id，也可根据访问时间维度计算
area_dim_id | client_ip | 区域id，根据用户ip，在区域维度表获取
company_dim_id | course_id | 公司id，根据课程id，在公司维度表获取
client_ip | client_ip | 用户ip
client_sessionid | session_id | 用户会话id
client_type | user_agent | 浏览器类型
visit_time | visit_time | 访问时间
years | visit_time | 访问时间 - 年（也可根据时间维度）
months | visit_time | 访问时间 - 月（也可根据时间维度）
days | visit_time | 访问时间 - 天（也可根据时间维度）

画面3：
val sc = spark.sparkContext
val date_info = "2019-11-04"
val input = sc.textFile(path = s"/user/hive/external/data_course/visit_source/${date_info}")
Input
// 数据分割字符串中字段
.map(_.split(regex = "t"))
// 过滤机器人
.filter(arr => {
  arr(5).contains("Robot")
})
}

画面4：
val sc = spark.sparkContext
val date_info = "2019-11-04"
val input = sc.textFile(path = s"/user/hive/external/data_course/visit_source/${date_info}")
Input
// 数据分割字符串中字段
.map(_.split(regex = "t"))
// 过滤机器人
.filter(arr => {
  arr(5).contains("Robot")
})
}

画面5：
case class CourseVisitFact(
  course_visit_fact_id: String,
  course_dim_id: String,
  time_dim_id: String,
  area_dim_id: String,
  company_dim_id: String,
  client_ip: String,
  client_sessionid: String,
  // user-agent
  client_type: String,
  visit_time: Long,
  years: String,
  months: String,
  days: String
)

画面6：
无代码或配置内容。

画面7：
无代码或配置内容。

画面8：
object VisitSourceToFact {
  val spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
  def main(args: Array[String]): Unit = {
    import spark.implicits._
    var areaMap = Map[String, String]()
    spark.sql(sqlText = "SELECT * FROM data_dimen.area_dim").as[AreaDim].map(x => {
      areaMap += (x.city_name -> x.area_dim_id.toString)
    })
    var compMap = Map[String, String]()
    spark.sql(sqlText = "SELECT * FROM data_dimen.course_dim").as[CourseDim].map(x => {
      compMap += (x.course_dim_id -> x.company_id)
    })
  }
}

画面9：
val sc = spark.sparkContext
val date_info = "2019-11-04"
val input = sc.textFile(path = s"/user/hive/external/data_course/visit_source/${date_info}")
Input
// 数据分割字符串中字段
.map(_.split(regex = "t"))
// 过滤机器人
.filter(arr => {
  arr(5).contains("Robot")
})
}

画面10：
val sc = spark.sparkContext
val date_info = "2019-11-04"
val input = sc.textFile(path = s"/user/hive/external/data_course/visit_source/${date_info}")
Input
// 数据分割字符串中字段
.map(_.split(regex = "t"))
// 过滤机器人
.filter(arr => {
  arr(5).contains("Robot")
})
}

画面11：
无代码或配置内容。

画面12：
val sc = spark.sparkContext
val date_info = "2019-11-04"
val input = sc.textFile(path = s"/user/hive/external/data_course/visit_source/${date_info}")
Input
// 数据分割字符串中字段
.map(_.split(regex = "t"))
// 过滤机器人
.filter(arr => {
  arr(5).contains("Robot")
})
}

画面13：
val sc = spark.sparkContext
val date_info = "2019-11-04"
val input = sc.textFile(path = s"/user/hive/external/data_course/visit_source/${date_info}")
Input
// 数据分割字符串中字段
.map(_.split(regex = "t"))
// 过滤机器人
.filter(arr => {
  arr(5).contains("Robot")
})
}

画面14：
val sc = spark.sparkContext
val date_info = "2019-11-04"
val input = sc.textFile(path = s"/user/hive/external/data_course/visit_source/${date_info}")
Input
// 数据分割字符串中字段
.map(_.split(regex = "t"))
// 过滤机器人
.filter(arr => {
  arr(5).contains("Robot")
})
}

4)
