# 14-ETL-维度数据采集-区域维度原文件数据与实体映射

- 阶段：08.阶段八 智慧学成项目
- 章节：02.第二章 智慧学成-数据仓库与ETL
- 源文件：08.阶段八 智慧学成项目\02.第二章 智慧学成-数据仓库与ETL\14-ETL-维度数据采集-区域维度原文件数据与实体映射_【海量资源尽在 666java.com】.mp4
- 时长 9分3秒（音频 543s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前边已经将经纬度的实体以及区域的实体编写好也把这个文件上传到HDFS并用Spark进行一个读取接下来呢就是实体的一个映射咱们先来区域这个实体的一个映射咱们来到HUE看一下区域实体的这个原数据的一个数据结构根据它这个数据结构呢咱们来编写这个映射的一个代码
[00:30] 这里呢咱们使用map这个算子首先呢咱们可以看得到的是它是按行来存储的所以说呢咱们操作的时候也是按行来操作的这里呢变量名字做lay这里每一行的操作咱们需要将每一行的数据呢映射成省省的编码是市的编码县县的编码它其实是首先是逗号分隔然后分隔为三组然后呢再用空格这些分隔获取到每一个值
[01:00] 咱们首先是使用什么风格这个地方加个大括号咱们在里边可以写更多的代码因为不加大括号的话它只是一行这里加个大括号咱们可以写多行这里咱们首先是逗号风格这个地方可以看得到它是一个英文逗号这是需要注意的写代码的时候不要把它给写成中文逗号了接下来得到的值就叫就叫这个编辑Strength
[01:32] 是一个字符上这个值呢咱们再次分隔可以得到什么呀得到省加省的编码市和市的编码对它呢咱们这里可以确定到的是它是有三个三个三组值咱们这个地方直接就可以通过索引来取这个地方它的第一个值然后进行一个去空格的一个操作这个地方只是一个保险防止
[02:01] 有空格然后造成数据呢有脏数据接下来呢还是一个切分咱们就使用空格中间这个空格进行切分这个去空格是去除两边的空格就是咱们后边再使用空格切分的时候它就不会对结果造成一个干扰这里呢给它一个变量这是省其实是线和大它这个道理是一样的只不过索引不一样这里呢是线是
[02:33] 索引为2的线有了这个之后其实咱们就可以直接一个复制操作了这个还是非常简单的这个复制操作呢咱们就是由于这个用空格切了之后它只有两个值索引为0的就是第一个值就是咱们的省第二个就是咱们的编码是也是一样的第一个是咱们的是第二个是是的编码线也是相同道理咱们就直接根据咱们这个省进行一个编写
[03:01] 按照咱们的顺序首先省接下来省的编码接着是是缩影为0然后是的编码缩影为1接下来是限限的话缩影为0它的编码缩影也是1这个有了之后咱们用一个变量对它进行一个接收它得到的就是咱们映射后的一个值Auracode这个地方已经
[03:30] ERRORCODE用过了咱们这个地方就叫ERROR有了它之后呢咱们接下来为了方便咱们的一个处理因为你虽然说这个地方是一个DF这个地方得到的一个DF你两个DF进行操作的时候还是很不方便的咱们这里呢将它转换成什么呀转换成Hive的临时表转换成Hive的临时表呢后面咱们直接将两个临时表进行一个聚合操作就行了
[04:00] 这里还需要获取Hive的相关数据这里是使用Spark获取SepHive的context这是Hive的context就是circleContext这里给它一个变量就叫Hive注释借用一下这是获取circleContext咱们因为是操作的Hive所以说这个变量明显就起为Hive这里使用Hive创建一个什么DataForm
[04:35] 把这个DataForm咱们要创建的值就是咱们的区域这个行政区域这个编码然后把它给转换成一个什么Creator一个临时表临时视图这里用CreatorAllReplace假如说如果已存在的话就把它给覆盖掉如果没有存在的情况下咱们是什么没有覆盖的话就是新的如果有覆盖的那就将它给覆盖这里编辑名还叫这个
[05:06] 这个时候呢后面的时候咱们在使用的时候就可以直接使用hi5这个直接使用hi5写circle的方式进行一个数据的一个编写就是直接hi5然后circle这里呢选错了这里呢来读取这个刚才咱们创建这个创建这个临时表这是区域的接下来咱们来操作精美度的这个注视一定要加上这是区域转换为实体
[05:39] 去转换为实体这个是呢转换为临时表临时表接下来这个也是相同的操作就是咱们的静纬度也是相同的操作来点开静纬度静纬度这个的话经过观察它的数据结构就比较简单它只有逗号它只有逗号的情况下咱们就少了一层切割就直接逗号切割完之后进行一个复制就行了这里呢
[06:15] 咱们直接来还是一个map按行进行一个处理这里呢用逗号切分split咱们是逗号这个地方逗号要注意啊它也是英文的不是中文的得到一个值这个时候这个值就可以直接进行一个后边的一个复制操作咱们这个区域咱们这个维度叫什么呀原来名是这个这个时候呢就可以直接复制
[06:51] 它是省、市、县,然后两个值,咱们直接其实按照索引就行了索引的话就是0、1,这到了市,这个是县的接下来还有两个值是经纬度的,这个写错了,这个索引应该是2接下来索引是3,这是经度的,接下来呢索引是4,这是纬度的这个地方多了一个逗号吗
[07:27] 这个地方不是多了一个多号是数据类型的问题咱们读取到的数据是什么类型是String类型的但是人家要求什么类型看到没required要求是Float这个地方进行一个转换把它给转换成toFloat这个地方也需要转一下转完之后这个就有了给它用一个变量来接收这个地方它这个变量就叫做tmp因为
[08:03] 这个编量名就起的随意一点就实在是不想想这个名字叫什么了这个是区域转换式体这个是经纬度经纬度转换式体接下来呢也需要把它给转换成临时表这个转换成临时表呢就是咱们这个temp然后得到的临时表也是temp有了它之后呢接下来是咱们的一个什么样操作呀就是一个终极的一个聚合操作
[08:41] 好咱们聚合操作呢留到下一个视频再讲这个视频呢主要是讲解了将区域的原数据转换为实体以及经纬度的原数据转换为实体转换成实体之后呢把它再转换成害物的临时表方便咱们后边的一个聚合使用好视频就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spark 读取区域代码和区域信息文本文件，解析数据并创建 Hive 表。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Scala 代码文件 AreaDimInsert.scala，定义了区域映射类和区域代码类，初始化 SparkSession，并读取 area_code.txt 和 region.txt 文件。
画面 2: 在 Hue 浏览器中查看 area_code.txt 文件内容，显示北京、天津等城市的区域代码。
画面 3: 在 Hue 浏览器中查看 area_code.txt 文件内容，显示河北、山西等省份的区域代码。
画面 4: 在 Scala 代码中，对 area_code.txt 的每一行进行 split 操作，提取省份、城市、区域代码。
画面 5: 在 Scala 代码中，对 area_code.txt 的每一行进行 split 操作，提取省份、城市、区域代码，并对字符串进行 trim 和 split 操作。
画面 6: 在 Scala 代码中，对 area_code.txt 的每一行进行 split 操作，提取省份、城市、区域代码，并对字符串进行 trim 和 split 操作。
画面 7: 在 Scala 代码中，对 area_code.txt 的每一行进行 split 操作，提取省份、城市、区域代码，并对字符串进行 trim 和 split 操作。
画面 8: 在 Scala 代码中，对 area_code.txt 的每一行进行 split 操作，提取省份、城市、区域代码，并对字符串进行 trim 和 split 操作。
画面 9: 在 Scala 代码中，使用 Hive.createDataFrame 创建表 area_code。
画面 10: 在 Scala 代码中，使用 Hive.createDataFrame 创建表 area_code。
画面 11: 在 Hue 浏览器中查看 region.txt 文件内容，显示北京、天津等城市的经纬度信息。
画面 12: 在 Scala 代码中，对 region.txt 的每一行进行 split 操作，提取城市、经纬度信息。
画面 13: 在 Scala 代码中，对 region.txt 的每一行进行 split 操作，提取城市、经纬度信息，并创建临时视图 region_temp。
画面 14: 在 Scala 代码中，对 region.txt 的每一行进行 split 操作，提取城市、经纬度信息，并创建临时视图 region_temp。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
object AreaDimInsert {
  // 省份维度实体
  case class regionMap(sh: String, xian: String, lng: Float, lat: Float)
  // 区域维度实体
  case class areaCodeMap(sheng: String, shengCode: String, shi: String, shiCode: String, xian: String, xianCode: String)
  // 其它Spark session
  val Spark = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
  def main(args: Array[String]): Unit = {
    // 初始化Spark context
    val sc = Spark.sparkContext
    val area_code = sc.textFile(path = "/area_code.txt")
    val region = sc.textFile(path = "/region.txt")
  }
}
```

画面 4:
```scala
val area_code = sc.textFile(path = "/area_code.txt")
val region = sc.textFile(path = "/region.txt")
val area = area_code.map(line => {
  val strings = line.split(regexp = "=")
  val sheng = strings(0).trim().split(regexp = ",")
  val shi = strings(1).trim().split(regexp = ",")
  val xian = strings(2).trim().split(regexp = ",")
  areaCodeMap(sheng(0), sheng(1), shi(0), shi(1), xian(0), xian(1))
})
```

画面 9:
```scala
Hive.createDataFrame(area).createReplaceTempView(viewName = "area_code")
```

画面 12:
```scala
val region_temp = region.map(line => {
  val strings = line.split(regexp = "=")
  regionMap(strings(0), strings(1), strings(2).toFloat, strings(4).toFloat)
})
```

画面 14:
```scala
Hive.createDataFrame(region_temp).createOrReplaceTempView(viewName = "region_temp")
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

