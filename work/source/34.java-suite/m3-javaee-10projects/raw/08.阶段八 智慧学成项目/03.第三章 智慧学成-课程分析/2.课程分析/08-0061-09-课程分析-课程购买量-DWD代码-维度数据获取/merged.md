# 09-课程分析-课程购买量-DWD代码-维度数据获取

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\09-课程分析-课程购买量-DWD代码-维度数据获取_【海量资源尽在 666java.com】.mp4
- 时长 4分51秒（音频 291s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 到此呢,咱们准备工作就完成了,接下来呢,就是清洗代码的编写。
[00:06] 在代码的开始呢,咱们首先是要关联维度数据呢。
[00:11] 本视频的内容呢,就是相关维度数据的获取。
[00:15] 咱们来切到开发工具。
[00:17] 这里呢,已经建好了一个基础工程,就是咱们课程购买量,DW层,就是试约表清洗的一个基础工程。
[00:27] 由于这些内容都是固定的,咱们就已经写好,已经准备好,只用在问方法里面直接写代码就行了,这里咱们首先是进行维度数据的获取,首先咱们获取用户维度,获取用户维度咱们来切到文档上来分析一下,用户维度咱们是通过用户的ID来获取谁,来获取用户的IP,然后再通过IP关联到,
[01:02] 用户的这个区域ID所以说咱们在获取用户数据的时候只需要将查询出来的数据最终转换成用户ID然后用户IP这种形式就行了咱们呢还是以MAP来保存咱们来创建一个MAP这就叫UserMAPMAP它的数据结构呢是两个String接下来呢进行Circle的编写
[01:34] Circle编写呢,咱们直接使用Spark Circle集合,因为咱们直接读的是Hive中的数据这里呢查询所有,Sled星,From,咱们的表呢是维度表是DataDim,Dim,Dim1,然后呢咱们,这是库呀,咱们是库咱们库呢是维度库,接下来表呢是用户表,是UsterDim这个查了之后呢,咱们是需要
[02:07] 进行一个转换的转换成咱们的一个用户的一个实体方便咱们后续的一个操作这个地方呢就是u3dm转换中之后呢这个地方报了一个错是因为啊咱们那个隐世转换没有导入进来需要把Spark的隐世转换给导入进来Spark的隐世转换然后呢就导入所有导入之后呢这个地方就不报错了咱们呢接着把它转换成一个集合
[02:35] 进行一个map的一个操作这个地方变量名就起的可以随意一点因为呢只在这一个地方用接下来呢咱们就是一个复制的一个操作user map呢咱们就是对它复制这里呢加个括号咱们需要的值刚才已经分分析过了是什么呢user的id这里呢就是dim id加上谁啊不是加上谁啊
[03:01] 另外一个值呢就是咱们的user IP因为呢是通过user的ID找到user的IP然后呢找到之后呢就可以后边就可以直接进行一个数据的查询操作这个地方刚才写错了写成逗号了应该是尖角号横杠加尖角号这个时候呢用户维度的数据已经获取到了咱们来看还需要什么维度这里呢通过关联的还有公司维度是需要的关联是通过课程的ID
[03:32] 还有一个呢是区域ID咱们有了这个课程维度也有了这个地方公司维度公司维度呢区域维度对咱们还要需要一个公司维度和一个区域维度的一个数据因为呢需要用区域维度的需要用区域维度通IP呢找到程式然后关联到具体ID的值咱们呢接下来把公司维度和区域维度的信息呢给给
[04:02] 呃维度给获取过来这里公司维度和区域维度呢咱们之前在写课程访问量的时候呢就已经写过了这里呢这个数据是可以复用的直接把它给粘过来即可粘过来粘过来咱们是拿来直接使用因为代码前面呢已经准备过了就是在课程访问量的时候已经使用过已经写过了这里咱们还需要使用直接拿过来复用即可
[04:32] 以上呢就是咱们所需要的所有的维度数据咱们来切到代码这里公司维度的区域维度的还有咱们用户维度的用户维度的在这里好咱们到此维度获取的代码呢就完成了视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark Scala 编写数据清洗代码，将原始数据中的用户、区域、公司维度信息映射为事实表所需的维度 ID。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Scala 代码文件 CourseBuyHiveToFact.scala 的开头部分，定义了 SparkSession，并注释了“获取Spark session”和“关闭资源”。
画面2: 在画面1基础上，选中了 main 方法的代码块，准备进行编辑。
画面3: 切换到 PPT 页面，显示“2.4.1.2 数据清洗分析”章节，其中包含“清洗字段说明”表格，列出了 order_number、item_id、order_time、user_id 等字段的清洗说明和映射后的维度 ID。
画面4: 切换回代码编辑器，光标在 main 方法的开始处。
画面5: 在 main 方法中，定义了 userMap 变量，并编写了 SQL 查询语句：Spark.sql("select * from data_dimen_user_dim").as[UserDim].collect().map(x => userMap += (x.user_dim_id -> x.id))。
画面6: 在 main 方法中，导入了 Spark.implicits._，并展示了 Spark SQL 的常用方法，如 createDataFrame、createDataset 等。
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
import org.apache.Spark.sql.SparkSession

/**
 * @author
 */
object CourseBuyHiveToFact {
  // 获取Spark session
  val Spark: SparkSession = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)

  def main(args: Array[String]): Unit = {
    // 关闭资源
    Spark.close()
  }
}
```

画面5:
```scala
var userMap = Map[String, String]()
Spark.sql("select * from data_dimen_user_dim").as[UserDim].collect().map(x => {
  userMap += (x.user_dim_id -> x.id)
})
```

画面6:
```scala
import Spark.implicits._
```

画面9:
```scala
var areaMap = Map[String, String]()
Spark.sql("SELECT * FROM data_dimen_area_dim").as[AreaDim].collect().map(x => {
  areaMap += (x.city_name -> x.area_dim_id.toString)
})

var courseMap = Map[String, String]()
Spark.sql("SELECT * FROM data_dimen_course_dim").as[CourseDim].collect().map(x => {
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

