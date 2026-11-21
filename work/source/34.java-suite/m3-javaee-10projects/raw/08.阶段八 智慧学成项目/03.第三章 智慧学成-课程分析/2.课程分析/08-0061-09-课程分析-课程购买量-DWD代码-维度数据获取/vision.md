# 画面线理解：09-课程分析-课程购买量-DWD代码-维度数据获取

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\09-课程分析-课程购买量-DWD代码-维度数据获取_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:18, 00:28, 00:51, 01:19, 02:14, 02:27, 03:25, 04:04, 04:12, 04:15, 04:18, 04:20, 04:30, 04:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:03:34

1) 这一组画面整体在讲如何使用 Spark Scala 编写数据清洗代码，将原始数据中的用户、区域、公司维度信息映射为事实表所需的维度 ID。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Scala 代码文件 CourseBuyHiveToFact.scala 的开头部分，定义了 SparkSession，并注释了“获取Spark session”和“关闭资源”。
画面2: 在画面1基础上，选中了 main 方法的代码块，准备进行编辑。
画面3: 切换到 PPT 页面，显示“2.4.1.2 数据清洗分析”章节，其中包含“清洗字段说明”表格，列出了 order_number、item_id、order_time、user_id 等字段的清洗说明和映射后的维度 ID。
画面4: 切换回代码编辑器，光标在 main 方法的开始处。
画面5: 在 main 方法中，定义了 userMap 变量，并编写了 SQL 查询语句：spark.sql("select * from data_dimen_user_dim").as[UserDim].collect().map(x => userMap += (x.user_dim_id -> x.id))。
画面6: 在 main 方法中，导入了 spark.implicits._，并展示了 Spark SQL 的常用方法，如 createDataFrame、createDataset 等。
画面7: 切换回 PPT 页面，显示“2.4.1.2 数据清洗分析”章节的“清洗字段说明”表格。
画面8: 在 main 方法中，继续编写代码，将 userMap 的 SQL 查询结果映射为 Map[String, String]。
画面9: 切换到另一个 Scala 文件 VisitSourceToFact.scala，展示代码中定义了 areaMap 和 courseMap 变量，并编写了对应的 SQL 查询语句。
画面10: 在 VisitSourceToFact.scala 文件中，光标位于 courseMap 的 SQL 查询语句上。
画面11: 切换回 CourseBuyHiveToFact.scala 文件，光标位于 userMap 的 SQL 查询语句上。
画面12: 在 CourseBuyHiveToFact.scala 文件中，继续编写 areaMap 和 courseMap 的 SQL 查询语句。
画面13: 在 CourseBuyHiveToFact.scala 文件中，光标位于 courseMap 的 SQL 查询语句上。
画面14: 切换回 PPT 页面，显示“2.4.1.2 数据清洗分析”章节的“清洗字段说明”表格。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```scala
package cn.istart.xc.analysis.buy

import cn.istart.xc.common.ETLEnvironment
import org.apache.spark.sql.SparkSession

/**
 * @author
 */
object CourseBuyHiveToFact {
  // 获取Spark session
  val spark: SparkSession = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)

  def main(args: Array[String]): Unit = {
    // 关闭资源
    spark.close()
  }
}
```

画面5:
```scala
var userMap = Map[String, String]()
spark.sql("select * from data_dimen_user_dim").as[UserDim].collect().map(x => {
  userMap += (x.user_dim_id -> x.id)
})
```

画面6:
```scala
import spark.implicits._
```

画面9:
```scala
var areaMap = Map[String, String]()
spark.sql("SELECT * FROM data_dimen_area_dim").as[AreaDim].collect().map(x => {
  areaMap += (x.city_name -> x.area_dim_id.toString)
})

var courseMap = Map[String, String]()
spark.sql("SELECT * FROM data_dimen_course_dim").as[CourseDim].collect().map(x => {
  if (x.course_dim_id != null && x.company_id != null) {
    courseMap += (x.course_dim_id.toString -> x.company_id.toString)
  }
})
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面3:
标题：2.4.1.2 数据清洗分析
表格数据：
| 清洗字段 | 清洗说明 | 清洗后字段名 |
| :--- | :--- | :--- |
| order_number | 订单id，即事实表主键id | course_buy_fact_id |
| item_id | 这里的商品id就是课程id | course_buy_fact_id |
| order_time | 订单时间，根据订单时间计算出维度id | time_dim_id |
| user_id | 用户注册时有登录id，通过用户id可以找到对应公司，并关联公司维度id | area_dim_id |
| item_id | 这里的商品id就是课程id，通过课程id可以找到对应公司，并关联公司维度id | company_dim_id |

画面7:
标题：2.4.1.2 数据清洗分析
表格数据：
| 清洗字段 | 清洗说明 | 清洗后字段名 |
| :--- | :--- | :--- |
| order_number | 订单id，即事实表主键id | course_buy_fact_id |
| item_id | 这里的商品id就是课程id | course_buy_fact_id |
| order_time | 订单时间，根据订单时间计算出维度id | time_dim_id |
| user_id | 用户注册时有登录id，通过用户id可以找到对应公司，并关联公司维度id | area_dim_id |
| item_id | 这里的商品id就是课程id，通过课程id可以找到对应公司，并关联公司维度id | company_dim_id |

画面14:
标题：2.4.1.2 数据清洗分析
表格数据：
| 清洗字段 | 清洗说明 | 清洗后字段名 |
| :--- | :--- | :--- |
| order_number | 订单id，即事实表主键id | course_buy_fact_id |
| item_id | 这里的商品id就是课程id | course_buy_fact_id |
| order_time | 订单时间，根据订单时间计算出维度id | time_dim_id |
| user_id | 用户注册时有登录id，通过用户id可以找到对应公司，并关联公司维度id | area_dim_id |
| item_id | 这里的商品id就是课程id，通过课程id可以找到对应公司，并关联公司维度id | company_dim_id |

5) 无
