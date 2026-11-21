# 02-ETL-数据清洗-课程访问量清洗-获取维度数据&原始数据

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\02-ETL-数据清洗-课程访问量清洗-获取维度数据&原始数据_【海量资源尽在 666java.com】.mp4
- 时长 12分45秒（音频 765s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前边已经分析了课程访问量试试表的数据结构也分析了咱们这里清洗的一个步骤接下来呢就是咱们清洗代码的编写咱们来切到开发工具这里呢先新建一个包这个包上呢就是放咱们所有的清洗代码这里咱们要清洗的是谁啊课程访问量课程访问量呢咱们是存原数据清洗的
[00:37] 事实表这里的名字就叫VZSourceToFit咱们来创建一下VZSourceToFit这里呢类型是Object咱们把注释给加一下课程访问量的清洗程序步骤呢第一是关联维度第二去除机器人也是过滤机器人
[01:27] 第三呢,去重按照这个步骤,咱们开始编写代码通过本节的学习呢,咱们最终需要掌握的是使用代码将课程访问量的原始数据清洗到咱们的一个试试表中首先呢,咱们来关联维度关联维度呢,咱们来看一下咱们的文档这里咱们需要关联的维度有课程维度还有时间维度,以及区域维度
[02:01] 和公司维度一共是4个其中的课程维度它本身的课程ID就是维度ID这个直接拿来使用就行时间维度也是一样的可以通过咱们的访问量计算过来如果前台传过来了就是Time ID这个地方前台直接传的时候传过来了咱们是可以直接用的也是不需要计算的这里咱们需要计算的就是
[02:27] 咱们需要关联完完全全的话存维度表拿的也就是区域ID和咱们的区域维度ID和公司维度的ID咱们来看一下区域ID是怎么来获取然后公司维度的ID怎么来获取咱们来数据仓库这里使用HUE来看一下咱们的和区域相关的维度有哪些表和公司ID维度相关的有哪些表
[02:54] 这里呢根据咱们的已知条件这里是有IP区域维度呢是通过IP来获取这里呢咱们有一个IP工具类它可以根据咱们这个名称就是咱们的city name城市名称来反向的查找咱们的这个区域ID这个时候呢咱们只需要要拿量相纸就行了就是把这个表里边的city name和
[03:25] 区域ID给拿出来拿出来之后呢后边进行一个关联直接获取就行了或者关联查询言行另外一个呢就是咱们公司的维度公司的维度呢咱们首先来看公司维度这个这本身这张表咱们在分析里边说了它是通过什么来获取的它是通过课程ID来获取的咱们看公司维度这张表有课程信息吗没有没有的话咱们再来这个公司维度来看公司维度咱们来看一下有课程
[03:56] 有这个课程维度接下来咱们来看课程维度来看有没有公司ID字像象象这是咱们的公司ID以及咱们的公司名称也就是说我拿公司维度的时候通过的是课程维度这张表接下来呢咱们就来开始编写代码这里获取维度咱们先来写一个样例这里是区域维度但是咱们这个地方呢需要把
[04:29] 数据库给加上data然后是区域维度这里执行一下这里查到了所有的一个区域维度这个circle呢咱们需要使用等会呢就是查过来所有之后咱们已经分析过了通过程式的名称来反向查找这个查找区域的ID开始写代码之前呢这里咱们还没有还没有Spark session也没有Spark context也没有Spark circle
[04:58] 咱们已经有了ETL的环境变量使用ETL的环境变量进行一个编写给它一个变量名就叫做Spark咱们使用ETL这个环境变量的攻击类来获取Spark的session它需要一个app内幕咱们一般都是运行时的任务名就用当前的类名raise.getClass.getSimpleName这就是获取当前的一个
[05:29] 配置获取当前的名类名配置为程序Spark任务程序运行时的名称这是获取Spark session获取完了之后呢咱们这里就可以使用Spark session来使用Spark session来执行circle来查询维度首先呢这里是刚才是咱们写的circle回来看一下是哪一个写的是区域维度的这里呢就先获取
[06:04] 区域维度这里使用Spark.circle来获取获取完成之后呢咱们在这个实体里边已经实体这个包里边已经将所有的表结构映射为实体这里呢咱们来做一个映射操作s这里是区域就是咱们的区域维度好已经出来了已经出来了之后呢这里进行一个
[06:39] map的一个转换操作前面呢咱们已经分析了这个是通过IP来直接查找的IP直接查找的话最终咱们需要的值在这里需要的值是city name还有咱们的区域ID这两项就行这里呢咱们就使用map进行一个进行一个使用map进行一个存取就是把这个数据呢把这个数据转换成一个map这里呢由于这个map会有一个复制的操作
[07:09] 所以说这个变量是VR的不能是VL的这里呢就叫map给它一个map这里它的值呢有两个死去应的为方便咱们后边的一个操作都把它写成死去应了这里呢直接进行一个map的操作给它一个x吧这个名字可以随便起这个时候呢就是map的一个复制操作这个地方使用的还是加等
[07:41] 本身呢它是一个对象这个地方报了一个错它说的是没有隐世转换没有隐世转换的话咱们需要把Spark的隐世转换给导进来让这个报的错给消失掉这就是把Spark隐世转换这个地方报了就没了接下来呢就是进行一个复制操作咱们要的是哪两项值啊一个是set name然后另外一个呢是arrow id
[08:14] 拿到这个ID了之后,咱们就可以进行一个后面的操作这个地方呢,其实有一个注意信场,它是一个int类型的但是呢,咱们上面写的是string,这个地方就有一个toString的一个转换这就是咱们区域维度区域维度获取完了之后,接下来咱们来获取课程,那个公司维度获取公司维度呢,是通过公司维度的ID呢,是通过课程来课程维度来进行获取的这是区域维度
[08:50] 这是区域维度加个ID吧获取区域维度ID这个地方不能叫ID这就是获取区域维度的信息这个呢是获取客厂维度拿到公司维度ID好这个变量名改一下咱们既然是公司这个地方就叫com吧com变量名记得统一统一完成之后呢咱们来看一下它是在哪一张
[09:24] 表里边是在cos错了这是公司的查一下确认一下是不是这样表OK这有公司ID公司名称可以看到到那就说明这个是对的咱们呢就把这个给端过来这个时候呢就不能用区域维度了咱们最终它是什么维度呀它是客乘维度把这个变量给修改掉C大姐好客乘维度过来过来之后呢由于变量明显不对咱们呢
[10:11] 修改一下这个地方是客厂的维度ID这个地方呢是公司的ID这两个看一下数据结构是什么样的公司ID和客厂ID都是String的都是String的情况下这个地方就不需要ToString的转换到这呢咱们维度已经拿过来了拿过来之后呢接下来是进行过滤机器人的一个操作过滤机器人的一个操作咱们是不是要对它进行一个
[10:44] 原数据的一个拿取就是获取接下来咱们进行原数据的就是客层房量原始数据的获取这里需要使用Spark的context使用Spark获取context给它一个变量这叫scsc拿到之后这里它需要读取读取的话就使用了text file咱们来hue上看一下咱们的路径是在哪里的这里是咱们
[11:20] cause with source是原始数据的一个保存客厅访问量原始数据的一个保存路径这里呢又以天为单位进行一个分开存储分别存储咱们最终清洗的路径以天为单位清洗这个地方只有一天的数据就以它为例这个呢就拿到了这个数据但是这个地方有一个硬编码硬编码是什么呀就是这个日期咱们后期在执行的时候使用NiFi进行调度的时候这个日期
[11:49] 按道理来说应该是传过来的传过来的情况下你这里写死很显然是不合适的咱们先把它给拿出来等后面的话这个地方会需要修改成使用args这个参数进行一个读取动态的获取咱们这个日期参数这个读取完了之后给它一个变量就是咱们的一个input就是咱们的输入值这个地方加入一个变量获取加入一个注释
[12:22] 获取原始数据获取的是课程仿量的原始数据到这呢咱们基础数据已经获取的完成获取完成之后呢咱们本个视频本视频就到这里后续操作呢咱们在下一个视频进行讲解

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  val Spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
  def main(args: Array[String]): Unit = {
  }
}

画面7：
val Spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  Spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].collect()
}

画面8：
val Spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  Spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].collect()
}

画面9：
val Spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  var areaMap = Map[String, String]()
  Spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
}

画面10：
无代码，为 Hue 界面。

画面11：
val Spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  import Spark.implicits._
  var areaMap = Map[String, String]()
  Spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
  var compMap = Map[String, String]()
  Spark.sql("SELECT * FROM data_dimen.course_dim").as[CourseDimen].map(x => {
    compMap += (x.course_dim_id -> x.company_id.toString)
  })
}

画面12：
val Spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  import Spark.implicits._
  var areaMap = Map[String, String]()
  Spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
  var compMap = Map[String, String]()
  Spark.sql("SELECT * FROM data_dimen.course_dim").as[CourseDimen].map(x => {
    compMap += (x.course_dim_id -> x.company_id.toString)
  })
}

画面13：
val Spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  import Spark.implicits._
  var areaMap = Map[String, String]()
  Spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
  var compMap = Map[String, String]()
  Spark.sql("SELECT * FROM data_dimen.course_dim").as[CourseDimen].map(x => {
    compMap += (x.course_dim_id -> x.company_id.toString)
  })
  val sc = Spark.sparkContext
  sc.textFile(path)
}

画面14：
val Spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
def main(args: Array[String]): Unit = {
  import Spark.implicits._
  var areaMap = Map[String, String]()
  Spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].map(x => {
    areaMap += (x.city_name -> x.area_dim_id.toString)
  })
  var compMap = Map[String, String]()
  Spark.sql("SELECT * FROM data_dimen.course_dim").as[CourseDimen].map(x => {
    compMap += (x.course_dim_id -> x.company_id.toString)
  })
  val sc = Spark.sparkContext
  sc.textFile("/user/Hive/external/data_course/course_visit/2015-11-04")
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：表格数据，包含“课程访问事实表字段”、“对应维度表字段”和“字段说明”三列。
画面10：Hue 界面中，显示“course_dim.course_dim_id”和“course_dim.name”字段的数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

