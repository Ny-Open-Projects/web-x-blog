# 智慧学成-第2章-ETL

- 来源：04.阶段四 大数据转型 必备课程-Hadoop3\JavaEE中级进修课资料（新版）\08.基于大数据的智慧学成项目课程\day02\讲义-pdf版本\智慧学成-第2章-ETL【海量资源尽在 666java.com】.pdf
- 页数：31
- 抽取：pypdf 文本层



<!-- page 1 -->
智慧学成  第 2 章  ETL  
学习⽬标  
1. 理解 ETL 。
2. 理解数据采集执⾏流程。
3. 能够搭建并运⾏数据采集系统。
4. 理解 NiFi 的⼯作流程。
5. 能够使⽤ NiFi 采集维度数据。
6. 能够分析课程访问量指标。
7. 能够编写课程访问量 Spark 清洗程序。
1 ETL 介绍  
ETL （ Extract-Transform-Load ）是将数据从来源端经过抽取（ extract ）、转换（ transform ）、加载
（ load ）⾄⽬的端的过程。从数据源抽取出所需要的原始数据，经过数据清洗，最终将清洗后的数据加
载到数据仓库中去。也称为数据仓库技术。
1. 数据源通过采集的⽅式获取，  保存到数据仓库
2. 通过数据清洗，处理完成落地到数据仓库
3. 供业务使⽤
1.1 数据抽取  
数据抽取是从数据源抽取需要的原始数据，抽取的⽅式多种多样，要根据数据源的特点来确定，通常有
如下⼏种数据抽取的⽅式：
1 、从关系数据抽取数据
通常 OLTP 系统采⽤关系数据库存储业务操作数据，从关系数据库抽取操作型数据是最多⼀种数据抽取
⽅式。

<!-- page 2 -->
数据从关系数据库抽取后通常会先以⽂件的⽅式存储到分布式⽂件系统中（例如 HDFS ），⽅便 ETL 程序
读取原始数据。也有的是将抽取后的数据直接存储到数据仓库中，采⽤第⼆种⽅法需要提前在数据仓库
创建与原始数据相同结构的数据仓库模型。
2 、从⽇志⽂件抽取
OLTP 系统通过⽇志系统将⽤⼾的操作⽇志、系统⽇志等存储在 OLTP 服务器上，由专⻔的采集程序从服
务器上采集⽇志⽂件信息。
3 、从数据流接⼝抽取
OLTP 系统提供对外输出数据的接⼝（⽐如 telnet ），采集系统与该接⼝对接，从数据流接⼝抽取需要的
数据。
 
1.2 数据转换  
数据转换也叫数据清洗转换，是将采集过来的原始数据（通常原始数据存在⼀定的脏数据）清洗（过
虑）掉不符合要求的脏数据，根据数据仓库的要求对数据格式进⾏转换，经过数据清洗转换后是符合数
据仓库要求的数据。
要清洗的脏数据的形式有：
1 、错误的数据
存在数据内容错误的信息，⽐如学⽣选课信息中课程标识错误或选课⽇志⾮法等。
2 、不完整的数据
是指信息不完整，⽐如学⽣选课信息中缺少学⽣或缺少课程的信息，这类信息是不符合学⽣选课数据模
型的要求。
3 、重复数据
第三类数据是要根据具体的业务进⾏单独去重操作，⽐如：同⼀个课程学习会话中只允许有⼀条学习记
录，这⾥就要根据会话 ID 对数据进⾏去重操作。
 
数据转换的形式有：
1 、数据格式转换
对数据的格式进⾏转换，通常转换后数据内容是不变的，⽐如：数据仓库要求的⽇期存储格式是
yyyymmdd ，⽽采集过来的数据格式是 yyyy-mm-dd ，这⾥需要将 yyyy-mm-dd 的格式转换为
yyyymmdd 。
2 、数据内容转换
对数据内容进⾏转换，通常数据内容转换后是不会改变原始数据内容的意义的，⽐如：数据仓库要求存
储⽤⼾所在区域，这⾥就需要根据采集过来的⽤⼾ IP 地址从 IP 库中查找出⽤⼾的 IP 地址所对应的区域信
息，这⾥根据 IP 地址转换为区域就是数据内容的转换。
 
1.3 数据加载  
数据加载就是清洗转换后的数据存储到数据仓库中，数据加载的⽅式包括：全量加载、增量加载。
全量加载：

<!-- page 3 -->
全量加载相当于覆盖加载的⽅式，每个加载都会覆盖原始数据将数据全部加载的数据仓库，此类加载⽅
式通常⽤于维度数据。
增量加载：
增量加载按照⼀定的计划（通常是时间计划）逐步的将数据⼀批⼀批的将数据加载到数据仓库，此类加
载⽅式通常⽤于 OLTP 的业务操作数据。
2 课程访问量需求分析  
2.1 需求分析  
2.1.1 原型  
操作流程如下 :
1. ⾸先打开主⻚ , 地址 : http://211.103.136.242:8036
2. 在登陆⻚输⼊任意⽤⼾名、密码、验证码即可登陆
3. 点击课程访问量 , 操作指引如下图 :
 
3, 点击完成后⻚⾯展⽰效果如下 :

<!-- page 4 -->
2.1.2 指标与维度分析  
指标：
课程访问量是单位时间内⽤⼾访问课程详细⻚⾯的数量，以天为单位显⽰课程访问量。
维度：
时间维度包括 : 周、⽉、年 3 个级别，  在每个级别中⼜以天为单位进⾏数据展⽰。
按周：显⽰指定周范围内每天的课程访问量。
按⽉：显⽰指定⽉范围内每天的课程访问量。
按年：显⽰指定年范围内每天的课程访问量。
 
2.2 数据分析  
2.2.1 数据结构分析  
数据是以天为单位存储的课程访问量 , 下表是课程访问量 Web 前端⻚⾯展⽰字段 :
（原型中统计图的数据字段 , 数据来源业务表）

<!-- page 5 -->
字段名 字段说明 数据格式 数据⽰例
day 天 yyyy-MM-dd 2019-09-10
visitNum 访问量 int 类型 666
周查询前端请求 响应数据格式 数据说明
以第 37 周为例 , 请求参数为 :
startDate=2019-09-
09&endDate=2019-09-15
[{day: "2019-09-09", visitNum:
55054}, {day: "2019-09-10",
visitNum: 8869},…]
以天为单位 , 返
回当前周每天
的数据
⽉查询前端请求 响应数据格式 数据说明
以 9 ⽉为例 , 请求参数为 :
startDate=2019-09-
01&endDate=2019-09-30
[{day: "2019-09-01", visitNum:
55054}, {day: "2019-09-30",
visitNum: 8869},…]
以天为单位 , 返
回当前⽉每天
的数据
年查询前端请求 数据格式 数据说明
以 2019 年为例 , 请求参数为 :
startDate=2019-01-
01&endDate=2019-12-31
[{day: "2019-01-01", visitNum:
55054}, {day: "2019-01-02",
visitNum: 8869},…]
以天为单位 , 返
回当前⽉每天
的数据
2.2.2 数据查询分析  
以周为单位展⽰时 , 是展⽰当前选择周内每天的课程访问量 , 数据格式如下 :
以⽉为单位展⽰时 , 是展⽰当前选择⽉的课程访问量 , 数据格式如下 :
以年为单位展⽰时 , 是展⽰当前选择年的课程访问量 , 数据格式如下 :
 
2.3 数据模型  
2.3.1 ODS 层数据结构  
根据  需求分析 , 课程访问量的维度是时间维度，  有 : 周、⽉、年这三个级别 , 并以天为单位展⽰ , 由于进
⾏推断需要那些字段进⾏数据分析 , 下表是整理出来的所有采集数据的字段。

<!-- page 6 -->
采集字段 字段说明 数据格式 数据样例
course_id
课程 id, 根据课程 id 可以
做更多的分析 , 如课程热
⻔程度等等
uuid e60f96225a9046d5b7d752d168d98d14
time_dim_id 时间维度 , 根据⽤⼾访问时间计算出来
yyyy-
MM-
dd-
HH
2017-11-15-09
session_id
会话 id, 每打开⼀个⻚⾯
就会产⽣⼀个会话 id, 关
闭浏览器消失 , ⽤于去重
uuid 0b26410f5b1e49ac813137e9d14eb254
client_ip ⽤⼾ ip, ⽤于去重 ipv4 129.39.209.149
user_id ⽤⼾ id, 根据是否有值 ,可判断是否为登陆⽤⼾ uuid 311e3af993644504a059fb6be75c7743
user_agent
浏览器标识 , 可判断⽤⼾
访问⽅式及是否是机器
⼈
浏览
器 ua
Mozilla/5.0 (X11; Linux x86_64)
AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/76.0.3809.87
Safari/537.36
visit_time
⽤⼾访问时间 , 可根据访
问时间计算时间维度 , 确
认⽤⼾访问的具体时间
时间
戳 1510708629
 
2.3.2 数据存储  
数据存储格式 :
hdfs ⽂本⽂件
数据存储⽅式 :
每天的数据以 : 年 - ⽉ - ⽇⽬录命名 , 每天的数据存放在⼀个⽬录中，
如： /user/hive/external/data_course/course_visit_source/${yyyy-MM-dd},
数据内容格式 :

<!-- page 7 -->
数据分隔 : \t
数据换⾏ : \n
数据样例 :
3 采集系统  
3.1 采集系统介绍  
对于数据的抽取通常会搭建专业的数据采集系统来完成各种源数据的抽取。
采集系统的执⾏流程如下：
 
3.2 采集系统搭建  
搭建步骤如下：
1. 配置 Kafka-Connecter （ kafka-to-hdfs ）
e60f96225a9046d5b7d752d168d98d14    2019-07-01-09   
f8150a9f3a424053b2d9366927052a7f    169.63.52.55    
79f210da266b44bd871cd409227b6a84    Mozilla/5.0 (X11; Linux x86_64) 
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36    
1561943829
e60f96225a9046d5b7d752d168d98d14    2018-03-28-09   
58d9d8e25d0849a784b5b7d54da1f368    186.242.215.247 
f9ebcfa2947c4973918730b87eb8bd52    Mozilla/5.0 (X11; Linux x86_64) 
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36    
1522199829
e60f96225a9046d5b7d752d168d98d14    2018-09-15-09   
24c9f89c2d334663a8c7a09f218f46ae    188.34.239.169  
c05eda3041a64f52aa91683704aa5632    Mozilla/5.0 (X11; Linux x86_64) 
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36    
1536974229
e60f96225a9046d5b7d752d168d98d14    2017-11-13-09   
45ac0144431d4806a3c3a8163b5d7147    51.211.133.164  
9b2565eee9e447499a6fb2dc427fd0aa    Mozilla/5.0 (X11; Linux x86_64) 
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36    
1510535829
......

<!-- page 8 -->
2. 部署采集系统
3. 部署学成在线 web 前端
资源路径 :
 
3.3 测试 - 采集课程访问量  
采集系统搭建完成后，  访问课程主⻚即可采集课程访问量的数据，  地址为：http://xc-online:19856/le
aring-index
通过前端⻚⾯的访问，⽤⼾的⾏为数据通过采集服务器保存到 hdfs 上，  hdfs 保存结果如下图所⽰：
 
3 NiFi 采集  
3.1 NiFi 介绍及使⽤  
niﬁ 是课上使⽤重点 , 参考 : 讲义  - 第 2 章  Niﬁ 使⽤⽂档 .md
资源路径 :
 
3.2 维度数据采集  
3.2.1 维度介绍  
.
└── 授课资料
    └──  第 2 章 - 数据仓库与 ETL
        └──  采集系统
            └──  采集系统部署使⽤说明 .md
            └──  Kafka-Connecter 使⽤⽂档 .md
.
└──  授课资料
    └──  第 2 章 - 数据仓库与 ETL
        └──  Nifi 使⽤⽂档 .md

<!-- page 9 -->
维度名 对应 MySQL 表名 ( 库名 . 表名  )
公司 xc_user.xc_company
课程视频 xc_course.teachplan
⽤⼾选课 xc_learning.xc_learning_course
课程信息 xc_course.course_base
⽤⼾ xc_user.xc_user
课程学习频率 xc_course.course_study_freq
课程分类 xc_course.category
数据清洗离不开相关的维度数据 , 维度数据来⾃学成在线项⽬的业务数据 , 这⾥使⽤ NiFi 把业务数据采集
到 hive 中 , 这种业务数据称为维度数据。需要采集的维度数据如下 :
1. 时间维度  ( 业务没有 , 脚本⽣成  )
2. 公司维度
3. 课程视频维度
4. ⽤⼾选课维度
5. 课程信息维度
6. ⽤⼾维度
7. 课程学习频率维度
8. 课程分类维度
9. 区域维度  ( 业务数据没有 , 需要清洗出来  )
与业务数据对应关系如下 :
3.2.2 维度数据采集步骤  
1. 导⼊业务（学成在线） MySQL 数据
2. 导⼊ NiFi 源码
3. 配置维度采集的 NiFi 参数
4. 执⾏采集
 
3.2.3 导⼊ MySQL  
学成在线 MySQL 数据库在资料中位置，  需要导⼊到 xc-online-mysql 数据库中：
导⼊步骤如下：
.
└──  授课资料
    └──  第 2 章 - 数据仓库与 ETL
        └──  sql
            └──  xc.zip // 需要解压

<!-- page 10 -->
PS: 这个数据库⽂件包括最终的业务库，  先导⼊后⾯使⽤
 
3.2.4 NiFi 调度源码  
源码路径 :
NiFi 调度处理器已配置好 , 导⼊源码 , 需要配置 Mysql, hdfs, hive
3.2.4.1 导⼊ NiFi 调度源码  
步骤如下：
1. 右键⼯作区空⽩位置 , 在弹出菜单点击  Upload template, 如图所⽰ : 
 1568168040902
.
└──  授课资料
    └──  第 2 章 - 数据仓库与 ETL
        └──  nifi
            └──  时间维度采集 .xml
            └──  课程维度采集 .xml

<!-- page 11 -->
2. 弹出窗⼝选择 Browse 按钮 , 选择你 niﬁ xml 代码路径 , 然后点击 Upload, 操作如下图 :
操作步骤如下图所⽰：
3.2.4.2 NiFi 维度采集配置  
导⼊完成的 NiFi 调度如下图所⽰，所有的⻩⾊感叹号都是需要配置的项：
以课程维度配置为例，  进⾏配置，  其他维度的配置相同，操作如下：
步骤：
1. 配置 MySQL 密码，启⽤连接
2. 启⽤ Hive 连接

<!-- page 12 -->
PS: 时间维度只需要配置 Hive 连接即可
操作看下图：
 
配置好的 NiFi 调度如下图所⽰，  没有任何感叹号，  说明已配置好
3.2.4.2.1 MySQL 配置说明  
由于 MySQL 的配置，  在 NiFi 源码中已配置，  这个了解下即可，  知道都配置了那些项，  如下图所⽰：

<!-- page 13 -->
3.2.4.2.1 Hive 配置说明  
由于 Hive 的配置，  在 NiFi 源码中已配置，  这个了解下即可，  知道都配置了那些项，  如下图所⽰：
3.2.5 时间维度数据⽣成脚本  
数据⽣成脚本源码如下 :
import arrow
import json
import datetime
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback

<!-- page 14 -->
3.2.6 执⾏采集  
以时间维度为例⼦，  进⼊处理器组，  在⼯作区空⽩处右键，  点击 start 即可，执⾏完成可以把处理器关
闭了，  然后到 hue 中查看数据，  操作如下：
from org.apache.nifi.processors.script import ExecuteScript
def isLeapYear(years):
    if ((years % 4 == 0 and years % 100 != 0) or (years % 400 == 0)):
        days_sum = 366
        return days_sum
    else:
        days_sum = 365
        return days_sum
class PyStreamCallback(StreamCallback):
    def __init__(self):
        pass
    def process(self, inputStream, outputStream):
        years = int('2018')
        data = []
        start_date = '%s-1-1' % years
        a = 0
        days_sum = isLeapYear(int(years))
        while a < days_sum:
            for num in range(0, 24):
                time_dim_id = arrow.get(start_date).shift(days=a).format("YYYY-
MM-DD-") + str(num)
                obj = {}
                obj['time_dim_id'] = time_dim_id
                temp = time_dim_id.split('-')
                obj['year'] = temp[0]
                obj['month'] = temp[1]
                obj['day'] = temp[2]
                obj['hour'] = temp[3]
                tmp_week = datetime.date(int(temp[0]), int(temp[1]), 
int(temp[2])).isocalendar()
                obj['week'] = tmp_week[1]
                obj['week_name'] = tmp_week[1]
                data.append(obj)
            a += 1
        outputStream.write(bytearray(json.dumps(data),encoding='utf-8'))
flowFile = session.create()
if flowFile != None:
    flowFile = session.write(flowFile, PyStreamCallback())
    session.transfer(flowFile, ExecuteScript.REL_SUCCESS)
else:
    pass

<!-- page 15 -->
PS: 所有维度采集都是这样的流程
3.2.6.1 注意事项  
采集的数据乱码问题 :
如果保存在数据仓库中的维度数据出现了乱码，  解决步骤如下：
 
3.2.7 区域维度代码  
区域维度是由区域经纬度和区域编码两个数据合并⽽成 , 由于数据不规则 , 没办法使⽤ NiFi 调度 , 这⾥什么
spark 进⾏清洗⼊库 , 区域经纬度和区域编码原数据在资料中 , 路径如下 :
使⽤时需要上传到 hdfs 根⽬录 , 如下图所⽰ :
# 登陆 nifi 容器
docker exec -it xc-online-nifi bash
# 重启 nifi
$NIFI_HOME/bin/nifi.sh restart
# nifi 重启成功后，再次采集即可
.
└──  授课资料
    └──  第 2 章 - 数据仓库与 ETL
        └──  data
            ├──  region.txt
            └──  area_code.txt

<!-- page 16 -->
清洗代码如下 :
AreaDimInsert.scala
package cn.itcast.xc.dimen
import cn.itcast.xc.common.EtlEnvironment
/**
 * <p>
 * 区域维度数据处理
 * </p>
 **/
object AreaDimInsert {
  // 经纬度实体
  case class regionMap(sheng: String, shi: String, xian: String, lng: Float, 
lat: Float)
  // 区域实体
  case class areaCodeMap(sheng: String, shengCode: String, shi: String, shiCode: 
String, xian: String, xianCode: String)
  /**
   * 获取 spark session
   */
  val spark = EtlEnvironment.getSparkSession(this.getClass.getSimpleName)
  def main(args: Array[String]): Unit = {
    // 获取 spark context
    val sc = spark.sparkContext
    // 获取 sql context
    val hive = spark.sqlContext
    val area_code = sc.textFile("/area_code.txt")
    val region = sc.textFile("/region.txt")
    // 区域转换实体
    val area = area_code.map(line => {
      val strings = line.split(",")
      val sheng = strings(0).trim().split(" ")
      val shi = strings(1).trim().split(" ")
      val xian = strings(2).trim().split(" ")
      areaCodeMap(sheng(0), sheng(1), shi(0), shi(1), xian(0), xian(1))
    })
    // 转换为临时表
    hive.createDataFrame(area).createOrReplaceTempView("area_code")
    // 经纬度转换实体
    val region_temp = region.map(line => {
      val strings = line.split(",")
      regionMap(strings(0), strings(1), strings(2), strings(3).toFloat, 
strings(4).toFloat)
    })
    // 转换为临时表
    hive.createDataFrame(region_temp).createOrReplaceTempView("region_temp")

<!-- page 17 -->
3.2.7.1 注意事项  
Windows 配置 winutils ：
winutils 在资料中的路径：
情况 1 ：  ⽆ hadoop 环境
    // 给 region_temp 这个表加 id
    val result = hive.sql("select row_number() over(order by sheng) as id, * 
from region_temp")
    // 转为临时表
    result.createOrReplaceTempView("region")
    val areaTale = hive.sql(
      """
        |select
        | a.id area_dim_id,  b.shengCode province , b.shiCode city, b.xianCode 
county,
        | a.lng longitude, a.lat latitude,
        | a.sheng province_name, a.shi  city_name, a.xian county_name
        |from region a
        |left join area_code b
        |on a.xian = b.xian and a.shi = b.shi
        |order by a.id
        |""".stripMargin)
    // 输出结果
    areaTale.show()
    areaTale
      // 分区修改 1 ，  减少⼩⽂件
      .repartition(1)
      // 字段分割⽅式
      .write.option("delimiter", "\\t")
      // 保存路径
      .option("path", "/user/hive/external/data_dimen/area_dim")
      // 写⼊模式
      .mode("overwrite")
      // 数据仓库的库名 . 表名
      .saveAsTable("data_dimen.area_dim")
    // 关闭资源
    sc.stop()
    spark.close()
  }
}
.
└──  授课资料
    └──  第 2 章 - 数据仓库与 ETL
        └──  winutils.zip

<!-- page 18 -->
没有 hadoop 环境也需要配置 HADOOP_HOME 环境变量，  把 winutils.zip 解压到⾮中⽂⽬录，这⾥解压
到  D:\devtools ⽬录，  如下图所⽰：
配置 HADOOP_HOME 环境变量如下图所⽰：
完整⽬录结构如下：
 
情况 2 ：  有 hadoop 环境
确认HADOOP_HOME环境变量已正确配置，  把 winutils.zip 解压任意⽬录，  找到 winutils.exe ，把
winutils.exe 复制到 HADOOP_HOME ⽬录内 bin ⽬录下，  如下图所⽰：
环境变量配置：
⽬录结构：
d:
└──  devtools 
    └──  winutils
        └──  bin
            └──  winutils.exe

<!-- page 19 -->
课程访问量事实表字段 对应源数据字段 字段说明
course_visit_fact_id - 课程访问量事实表 id, uuid ⽣成
course_dim_id course_id 课程 id, 课程 id 也是课程维度 id
time_dim_id time_dim_id 时间维度 id, 也可根据访问时间计算
area_dim_id client_ip 区域 id: 根据⽤⼾ ip, 在区域维度获取
company_dim_id course_id 公司 id: 根据课程 id, 在公司维度表中获取公司 id
client_ip client_ip ⽤⼾ ip
client_sessionid session_id ⽤⼾会话 id
client_type user_agent 浏览器类型
visit_time visit_time 访问时间
years visit_time 访问时间  - 年  ( 也可根据时间维度  )
months visit_time 访问时间  - ⽉ ( 也可根据时间维度  )
days visit_time 访问时间  - 天 ( 也可根据时间维度  )
 
 
 
 
4 数据清洗  
4.4.1 DWD 层数据结构  
采集的原始数据会有⼀些垃圾数据，如：爬⾍访问的数据、⾃动⼯具访问的数据、数据内容不完整的数
据等 , 这些数据是不能直接使⽤的 , 这个时候就需要对数据进⾏清洗 , 过虑掉垃圾数据、并根据要求进⾏
数据格式转换等操作 , 清理后的数据保存到事实表中。
为⽅便进⾏不同的维度的分析，清洗后的数据会关联很多维度字段 , 这时事实表的数据字段会很多 , 把这
种事实表叫做事实宽表。
事实表字段说明 :
 
4.4.2 数据清洗分析  
清洗逻辑分析：
1. 关联维度
2. 过滤机器⼈访问
3. 以天为单位 , 根据 session 和 ip, 课程 id 去重
清洗字段详细说明：

<!-- page 20 -->
清洗字段 清洗说明 清洗后字段名
client_ip ⽤⼾ ip, 关联数据仓库区域维度表 id area_dim_id
course_id 课程 id, 与数据仓库课程维度表 id 相同 , course_dim_id
course_id 课程 id, 通过关联数据仓库课程维度 , 关联到公司维度 id company_dim_id
- 课程访问量事实表 id, uuid ⽣成 course_visit_fact_id
visit_time 事实表是根据 : 年、⽉、⽇分区 , 这⾥根据访问时间清洗出分区年 years
visit_time 事实表是根据 : 年、⽉、⽇分区 , 这⾥根据访问时间清洗出分区⽉ months
visit_time 事实表是根据 : 年、⽉、⽇分区 , 这⾥根据访问时间清洗出分区⽇ days
 
4.4.3 清洗代码  
根据清洗分析编写代码如下 :
package cn.itcast.xc.analysis
import cn.itcast.xc.common.EtlEnvironment
import cn.itcast.xc.entity.{AreaDimen, CourseDimen, CourseVisitFact}
import cn.itcast.xc.utils.DateUtils.getDateStr
import cn.itcast.xc.utils.IpUtils.getArea
import cn.itcast.xc.utils.StrUtils.getUuId
/**
 * <p>
 * 课程访问量，  事实表清洗程序
 * 1 ，关联维度
 * 2 ，过滤机器⼈
 * 3 ，去重
 * </p>
 **/
object VisitSourceToFact {
  /**
   * 初始化 spark session
   */
  val spark = EtlEnvironment.getSparkSession(this.getClass.getSimpleName)
  def main(args: Array[String]): Unit = {
    import spark.implicits._
    // 获取  spark context
    val sc = spark.sparkContext
    val data_info = "2019-11-04"

<!-- page 21 -->
// 获取维度数据
    // 区域维度
    var areaMap = Map[String, String]()
    spark.sql("SELECT * FROM data_dimen.area_dim").as[AreaDimen].collect().map(x 
=> {
      areaMap += (x.city_name -> x.area_dim_id.toString)
    })
    // 公司维度
    var courseMap = Map[String, String]()
    spark.sql("SELECT * FROM 
data_dimen.course_dim").as[CourseDimen].collect().map(x => {
      if (x.course_dim_id != null && x.company_id != null) {
        courseMap += (x.course_dim_id.toString -> x.company_id.toString)
      }
    })
    // 访问量原始数据
    val visitSource = 
sc.textFile(s"/user/hive/external/data_course/course_visit_source/${data_info}")
    // 进⾏清洗
    val visitClean = visitSource
      // 分割得到每个字段
      .map(_.split("\t"))
      // 过滤机器⼈
      .filter(arr => {
        !arr(5).contains("Rebot")
      })
      // 批量⽣产数据进⾏清洗时，以 date_info 为准清，需要过滤⽇期
      // 测试时，  这个⼀般不过滤，  清洗所有⽅便报表系统使⽤
      .filter(arr => {
        data_info == getDateStr(arr(6).toLong * 1000, "yyyy-MM-dd")
      })
      // 关联维度，  转换为事实表的实体对象
      .map(tmp => {
        // 时间维度
        val time_dim_id = getDateStr(tmp(6).toLong * 1000, "yyyy-MM-dd-HH")
        // 区域
        var areaId = "-1"
        try {
          areaId = areaMap.get(getArea(tmp(3))).get
        } catch {
          case e =>
        }
        // 公司
        var comId = "-1"
        try {
          comId = courseMap.get(tmp(0)).get
        } catch {
          case e =>
        }
        // 年⽉⽇分区
        val ymd = time_dim_id.split("-")
        // 转换为对象
        CourseVisitFact(getUuId(), tmp(0), time_dim_id, areaId, comId, tmp(3), 
tmp(2), tmp(5), tmp(6).toLong * 1000, ymd(0), ymd(1), ymd(2))
      })
      // 根据 session 和 ip, 课程 id, 选择去重
      .groupBy(x =>

<!-- page 22 -->
4.4.4 测试  
清洗代码编写完成后 , 就可以进⾏运⾏测试了 , 操作如下图 , 可以运⾏直接运⾏ , 还是 debug 运⾏
运⾏结果如下图 :
        x.client_ip + x.client_sessionid + x.course_dim_id
      )
      // 重复的值取时间⼩的
      .map {
        x => x._2.minBy {
          _.visit_time
        }
      }
    // 转换为 df
    val visitDF = spark.createDataFrame(visitClean)
    // 配置允许动态分区
    spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
    // 保存到数据仓库
    visitDF.repartition(1)
      .write.mode("overwrite")
      .insertInto("data_course.course_visit_fact")
    // 查看结果
    spark.sql("select * from data_course.course_visit_fact").show()
    // 关闭资源
    sc.stop()
    spark.close()
  }
}

<!-- page 23 -->
5 NiFi ⽣产数据  
JS 埋点与 niﬁ ⽣产数据的数据格式是⼀样的
 
5.1 NiFi 调⽤流程  
niﬁ 调度是使⽤ niﬁ 调⽤ python 脚本 , 产⽣模拟数据 , 此⽅法可以⽅便快速⽣成⼤量测试数据 , 调度流程如
下 , 以处理器为例 :
QueryDatabaseTable 
  ConvertAvroToJSON 
  SplitJson 
  EvaluateJsonPath 
ReplaceText 
  ExecuteScript 
  PutHDFS
NIFI 调⽤流程图 , 如下图所⽰ :
5.2 流程代码  
niﬁ 流程 xml 代码路径 :
 
└── 授课资料
    └── 第 2 章 - 数据仓库与 ETL
        └── nifi/ 课程访问量 .xml

<!-- page 24 -->
5.3 NiFi xml 代码  导⼊  
导⼊已有 NiFi 代码操作参考：  3.2.4.1 导⼊ NiFi 调度源码
使⽤上传的 NiFi 代码 , 操作如下 :
 
导⼊ niﬁ xml 代码 , 需要⾃已配置⾃⼰的 mysql 连接及 hdfs 配置⽂件路径 , 配置详情如下 :
 
5.4 课程访问量⽣产数据 NiFi 配置  
5.4.1 配置  
导⼊配置后 , 会有相应的提⽰ , 要求进⾏配置 , 不配置的话 NiFi ⽆法正常调度 , 如下图所⽰ :
配置 DBCPConnectionPool MySQL 密码

<!-- page 25 -->
操作如图所⽰ :
 
配置 DBCPConnectionPool MySQL 驱动位置
MySQL 驱动根据你的实时情况配置 , 这⾥⼀定要配置绝对路径 , 操作如下图 :
 
启⽤  DBCPConnectionPool
配置好  DBCPConnectionPool MySQL 密码和  DBCPConnectionPool MySQL 驱动位置后 , 需要把
DBCPConnectionPool 启⽤才能连接 MySQL, 操作如下 :

<!-- page 26 -->
配置 HDFS 配置⽂件
由于使⽤了 PutHDFS 处理器 , 这⾥需要配置  hdfs-site.xml 和  core-site.xml 这两个配置⽂件的绝对路径 ,
操作步骤如下 :
 
配置 HDFS ⽂件存储路径 **

<!-- page 27 -->
5.4.2 python 脚本  
PS: ⾮常重要  --- NiFi 调度时脚本中不能出现  “ 任何中⽂  ” ( 注释也不⾏  ) , 否则脚本不能正常执⾏  ! ! ! ,
本课程所有 Python 脚本都遵循这个规范
python 脚本主要⽤于⽣成模拟数据 , 代码如下 :
import random
import uuid
import time, datetime
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.apache.nifi.processors.script import ExecuteScript
BROWSER = ['Firefox', 'Chrome', '360', 'Fz', 'Sougou', 'Rebot', 'IE', 'Spark', 
'QQ', 'UC', 'Dnucl', 'Liebao', 'AY']
def datestamp():
    now_info = datetime.datetime.now()
    delta = datetime.timedelta(random.randint(1, 720))
    time_info = now_info - delta
    for_time = time_info.strftime('%Y-%m-%d %H:%M:%S')
    times = int(time.mktime(time.strptime(for_time, '%Y-%m-%d %H:%M:%S')))
    return times
class PyStreamCallback(StreamCallback):

<!-- page 28 -->
5.4.2.1 脚本说明  
脚本⽣成数据时间及⽣成数据量说明 , 详情看下图  :
PS: Python 脚本配置控制数据⽣成量及⽇期都是这样的配置
 
5.4.2.2 注意事项  
    def __init__(self):
        pass
    def process(self, inputStream, outputStream):
        text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        for i in xrange(1, random.randint(1000, 3000)):
            ip_str = str('.'.join(str(random.randint(1, 255)) for i in 
xrange(4)))
            dt = datestamp()
            time_dim_id = time.strftime("%Y-%m-%d-%H", time.localtime(dt))
            user_agent = str(BROWSER[random.randint(0, BROWSER.__len__() - 1)])
            outputStream.write(bytearray(str(text) + '\t' + time_dim_id + '\t' + 
str(uuid.uuid4()) + '\t' + ip_str + '\t' + str(uuid.uuid4()) + '\t' + user_agent 
+ '\t' + str(dt) + '\n', encoding='utf-8'))
flowFile = session.get()
if flowFile != None:
    flowFile = session.write(flowFile, PyStreamCallback())
    session.transfer(flowFile, ExecuteScript.REL_SUCCESS)
else:
    pass
# 课程 id, 维度 id( 根据时间计算得到 ), session_id, ⽤⼾ ip, ⽤⼾ id, user_agent, 访问时间

<!-- page 29 -->
访问时间问题
python ⽣产数据使⽤的时间戳，  Js 埋点使⽤的是毫秒值  ，使⽤⽣产数据测试时程序⾥时间操作需要乘
以 1000, 变成毫秒值  ，  如下图所⽰：
图⼀ :
图⼆ :
图三 :
 
 
5.5 测试  
 
所有的都配置完成之后 , 接下就是运⾏程序进⾏测试了 , 启动之前还要确认依赖的服务已启动 , 这⾥依赖
了 MySQL, Hadoop, 请确认已启动 , 最终在 hdfs 上直接产⽣数据 , 测试成功 , 运⾏步骤如下 :
启动所有处理器 :
右建⼯作区空⽩处  
  弹出菜单点 start
启动单个处理器 :
选择对应处理器  
  弹出菜单点 start
 
启动所有处理器操作如图所⽰ :

<!-- page 30 -->
只要 PutHDFS 处理有数据写⼊ , 就说明整个流程没有问题 , 可以去 hdfs ⽂件查看结果了 , 下图为数据写⼊
成功截图 :
 
 
5.6 再次测试清洗代码  
参考 : ⽂档  4.4.4 测试 章节

<!-- page 31 -->

