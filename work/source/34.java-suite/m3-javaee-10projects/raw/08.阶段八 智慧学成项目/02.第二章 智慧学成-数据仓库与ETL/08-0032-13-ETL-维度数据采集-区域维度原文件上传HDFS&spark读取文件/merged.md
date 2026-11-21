# 13-ETL-维度数据采集-区域维度原文件上传HDFS&spark读取文件

- 阶段：08.阶段八 智慧学成项目
- 章节：02.第二章 智慧学成-数据仓库与ETL
- 源文件：08.阶段八 智慧学成项目\02.第二章 智慧学成-数据仓库与ETL\13-ETL-维度数据采集-区域维度原文件上传HDFS&spark读取文件_【海量资源尽在 666java.com】.mp4
- 时长 9分4秒（音频 545s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前面上咱们已经使用NiFi将时间维度以及课程维度的信息采到了咱们的数据仓库中,还有一个维度呢就是区域维度,咱们还没有采集到咱们的数据仓库中,区域维度呢是由区域经维度和区域编码两个数据合并而成,这里有两个文件,就是咱们的基础数据,这里呢使用Spark清洗的方式,
[00:29] 把它给保存到咱们的数据仓库中这两个文件呢在咱们的资料中第二张数据仓库与ATL的Data目录下这两个文件这是咱们这两个文件为了方便清洗呢咱们把它给上传到HDFS的根目录这里上传使用HUE进行一个上传操作点击上传按钮选择咱们的文件首先是区域的接下来是
[01:02] 经纬度的上传完成之后呢咱们来看一下文件内容这是区域的区域的话它是区域的行政编码区域的就是北京没有特别的一个代表性咱们往下看因为北京的话省市它好多都是一样的因为它是地级市因为它是直辖市省市县咱们这个区域呢行政区域编码呢是按照这样一个逻辑来的
[01:34] 像北京和天津重庆这些直辖市呢它是比较特殊的就是按照可能是北京然后北京天津天津这样的北京四辖区啊东腾区啊这样的这是咱们的行政编码咱们来看经纬度这个经纬度的话就是按照北京北京然后北京市它的经纬度是多少其实呢咱们还得想按它的典型呢咱们还得往下看河北这是省
[02:06] 施加状态是然后接下来是线或者是区它是按照这样一个这样一个逻辑在这里排列最后两位呢是经纬度咱们呢需要边写代码将这两个文件呢给合并成咱们最终的区域维度咱们来写代码这里呢新建一个包就叫做维度接下来呢是咱们区域维度的一个数据区域是area小写的
[02:42] 然后这是要往数据里边插入叫做insert然后呢这个地方是object.get咱们使用object.get来编写咱们的代码这个呢就是区域维度的一个清洗区域区域维度数据处理接下来呢这个地方咱们方法的入口是咱们的mint方法
[03:14] 这里有一个现成的工具类来获取Spark的,咱们把Spark给获取了这里获取的是Spark的Session,咱们编列名字叫做Spark这里使用ETL,getSparkSession它需要一个AppName,咱们的AppName就是咱们当前类这里使用z字关键字来获取,然后获取SympaName
[03:43] 就是当前的类名加个注释这个是获取Spark session咱们读取hdfs上的文件呢使用的是啥呢使用的是Spark context这里还要用Spark session将Spark context来获取给它一个变量名这里叫做sc然后加个注释这是获取Spark context
[04:23] 获取完Spark Context之后呢,咱们就可以进行文件的一个读取了。
[04:30] 这里点Text File,因为咱们是文本文件。
[04:34] 咱们在项目中已经配置了HDFS还有这个Card Set文件。
[04:40] 这里呢,它的协议路径就不需要读了。
[04:44] 就是这里边的协议路径就不需要读了,不需要写了。
[04:48] 咱们直接通过上面的根目录进行一个文件读取就行。
[04:53] 首先是 error code 的这样的话减少了咱们的就是这个文件路径的一个长度这个呢就是咱们的 error code用一个变量来接收接下来呢是咱们的区域这个是经纬度把这个文件名给复制过来这两个文件拿到之后呢咱们就可以进行一个计算的一个操作了
[05:30] 由于咱们最终呢是需要将两个文件合并的这里咱们根据这个文件呢根据文件的结构根据文件的结构现在是谁啊现在是经纬度的根据经纬度的这个结构呢咱们创造一个映射对象最终呢不是最终啊最后边呢就使用那个映射对象进行数据的一个操作咱们首先来把这个对象给创建出来case class
[06:00] 创建出来之后呢咱们后边就使用这个就使用这个对象来进行相应的数据的一个处理所以大写二维扣的这里是一个映射关系起名叫做map以map为后缀根据咱们这个是这个是经纬度的经纬度的话是这个咱们按照当前那个文件来这个区域的等会儿再来这个呢先给他写这轻微
[06:30] 去呢等会再写现在先搞经纬度的加个注释经纬度这个是映射实体吧经纬度实体根据这个的话咱们可以得到它是省是限然后是经纬度咱们就这个地方就直接使用拼音来省给它一个数据类型然后是是给它一个数据类型死圈样的然后是限
[07:08] 数据类型也是实行的手势线有了之后呢咱们还有一个什么呀精度和纬度精度呢用lng来表示这个地方的话它的数据类型是flot的因为这个地方有小数点纬度呢用lat来表示也是flot这个有了之后呢咱们剪下来是就是咱们的行动区域区域的实体区域实体这个地方上面就是写错了
[07:45] 咱们来切到咱们的区域实体区域的这个文件它呢它的结构呢省然后省的编码是市的编码然后线线的编码或者这个线呢也可能是区上面呢这个是可以做一个复用的把它给粘过来省完了之后呢这里是这里是省的扣的cod然后数据类型呢是死性的接下来呢是市的这里呢
[08:23] String也是String类型接下来是线的编码数据类型也是String这样的话咱们实体就创建好了创建好实体之后咱们接下来是对它进行一个映射咱们映射到就是文件到实体的映射接下来咱们下一个视频再讲就是到目前为止咱们是把文件上传到了咱们的HDAPI S上
[08:54] 然后映射的代码给写了然后读取的代码写完了这节呢就先到这里剩下的咱们下节继续

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark 读取文本文件（area_code.txt 和 region.txt）并进行数据处理，涉及 Hadoop 文件系统、Hue 文件浏览器和 Scala 代码编写。

2) 按时间顺序列出每张画面的要点：
画面1：在 Windows 文件资源管理器中，定位到 data 目录，显示 area_code.txt 和 region.txt 两个文件。
画面2：在 Hue 文件浏览器中，弹出“Upload to /”对话框，准备上传文件。
画面3：在 Hue 文件浏览器中，打开并显示 area_code.txt 文件内容，包含城市、省、区、邮编等信息。
画面4：在 Hue 文件浏览器中，打开并显示 region.txt 文件内容，包含城市、经纬度坐标。
画面5：在 IntelliJ IDEA 中，打开 xc-analysis 项目，显示项目结构。
画面6：在 IntelliJ IDEA 中，打开 AreaDimInsert.scala 文件，显示 Spark 会话初始化代码。
画面7：在 IntelliJ IDEA 中，打开 core-site.xml 文件，显示 Hadoop 配置。
画面8：在 Hue 文件浏览器中，页面加载中，显示加载图标。
画面9：在 IntelliJ IDEA 中，同时打开 Hue 文件浏览器和 AreaDimInsert.scala 文件，显示 region.txt 文件内容。
画面10：在 IntelliJ IDEA 中，编辑 AreaDimInsert.scala 文件，定义 regionMap 案例类。
画面11：在 IntelliJ IDEA 中，编辑 AreaDimInsert.scala 文件，定义 areaCodeMap 案例类。
画面12：在 IntelliJ IDEA 中，编辑 AreaDimInsert.scala 文件，定义 area_code 案例类。
画面13：在 IntelliJ IDEA 中，编辑 AreaDimInsert.scala 文件，定义 area_code 案例类，包含 shi、xian 等字段。
画面14：在 IntelliJ IDEA 中，编辑 AreaDimInsert.scala 文件，定义 region 案例类，包含 path = "/region.txt"。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6代码：
```scala
object AreaDimInsert {
  val Spark: SparkSession = SparkSession.builder()
    .appName("AreaDimInsert")
    .config("Spark.sql.warehouse.dir", "hdfs://node1:8020/user/Hive/warehouse")
    .config("Spark.serializer", "org.apache.Spark.serializer.KryoSerializer")
    .config("Spark.sql.catalogImplementation", "inmemory")
    .config("Spark.sql.adaptive.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.skewJoin.enabled", "true")
    .config("Spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes", "100M")
    .config("Spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes", "100M")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("Spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("Spark.sql.adaptive.coalescePartitions.targetParallelism", "100")
    .config("

