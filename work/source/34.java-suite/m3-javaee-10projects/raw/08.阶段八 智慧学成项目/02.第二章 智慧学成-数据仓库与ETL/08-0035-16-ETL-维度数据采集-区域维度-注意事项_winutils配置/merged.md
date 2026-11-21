# 16-ETL-维度数据采集-区域维度-注意事项：winutils配置

- 阶段：08.阶段八 智慧学成项目
- 章节：02.第二章 智慧学成-数据仓库与ETL
- 源文件：08.阶段八 智慧学成项目\02.第二章 智慧学成-数据仓库与ETL\16-ETL-维度数据采集-区域维度-注意事项：winutils配置_【海量资源尽在 666java.com】.mp4
- 时长 8分5秒（音频 485s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前面咱们在使用代码处理维度数据的时候如果没有配置的WinUtils代码是不能正常执行的这里在这个错只会在Windows环境下出现如果你是用的Linux操作系统或者是苹果的Mac操作系统不会出现这个问题Windows的情况Windows环境下这个WinUtils是需要进行一个配置的如果没有配置
[00:30] 回报一个错咱们来演示一下这个错我这里呢原来是有WinUtils的配置的这里是配置了一个Hadoop的home然后指定WinUtils的目录这里我把它给删除点击确定再确定环境呢删除完之后开发工具需要重启才能生效这里呢就把开发工具关掉再次打开再次打开执行咱们的
[00:59] 就是区域维度的处理代码清洗代码这个时候就会发错咱们呢来看一下这个错是一个什么样的错好这里程序已经加载完成咱们就可以执行了直接运行这里程序执行可能需要一点时间耐心等待一下这个还在打包这里呢已经在开始执行了它已经在读取这个是
[01:39] 驱动的这个是初始化objected star这个地方到了Hive这个地方再组Hive metadata了这呢都是应该是都是在初始化Hive的一个操作这里呢显示已经初始化完成初始化完成之后呢他就是在做一些计算了好错已经报了出来这里呢第41行第41行报了一个控制人首先呢咱们这个代码之前是可以跑的
[02:11] 咱们可以再次验证一下因为4G航报的控制针咱们的变量只有两个一个是Hive一个是这个Era就是咱们的区域清洗后的区域维度数据这里已经到了断点首先咱们Hive是有值的还有另外一个变量这个区域维度的这个数据也不是区域维度就是映射后的这个区域这个实体也是有值的这两个都有值的情况下还报了控制针
[02:42] 经过测试呢发现是由于这个咱们切到文档是由于windows环境下没有配置咱们的winutils而且呢这个winutils必须它的变量是环境变量是hadophomehadophome呢指向了winutils的这个节目录然后它这个目录内呢会有另外两个文件就是有一个bin目录bin目录下呢
[03:09] 是咱们真正的WinUtils这个文件他最终找的是这个咱们资料中也提供了WinUtils在咱们资料中第二张的数据仓库语ETL这就是咱们提供的WinUtils的文件它解压出来之后是WinUtils下面有一个bin目录最终是WinUtils exe这个文件这里我已经把它给解压到了地盘我的开发工具目录
[03:39] 咱们配置环境变量的时候只要找到副层目录就行了找到这个WinUtils目录这呢就是我刚才删除的那个环境变量这里是Hadoop Home接下来呢就是这个路径这个路径指定完成之后呢就OK了这个时候呢再把开发工具给重启就是直接把它给关掉然后呢再启动跑代码就没事了
[04:10] 就没有问题了因为咱们的环境所依赖所缺少的WinUtils已经配置好这里说的这种配置呢是你本机没有安装Hadoop的情况下如果你本机已经安装了Hadoop就是咱们的情况二而且呢也配置了Hadoop Home这个时候呢只需要将这个WinUtils这个文件这个文件放到你Hadoop B目录内
[04:39] 这里呢Hadoop是你本机的一个版本这个版本以你自己安装的为准咱们来看一下在这里Hadoop然后在bin里边有一个win-utils在这个目录里边咱们配置Hadoop home的时候如果你是安装的Hadoop这个地方安装路径是它以它为例这个时候你的bin不是你的bin你的pass就需要配置为这个
[05:08] 但是我这里没有安装Hadoop,那个只是一个B目录,我这里直接用WinUtils这个目录当作Hadoop Home,这个时候咱们再来测试咱们的程序。
[05:24] 走起。
[05:25] 这里演示的错是由于WinUtils没有配置到咱们那个Hadoop Home里面导致的。
[05:34] 如果你已经确认WinUtils已经配置,而且WinUtils可以使用的。
[05:42] 如果还报了相关的错这个时候就要及时反馈咱们一起来看具体是哪的错哪里引起了该如何解决这个还在初始化中咱们等它初始化完成来验证咱们就是配了这个WinUtils的环境变量HadoopHadoopHome配置完这个之后咱们的环境OK咱们的代码运行也没有错误咱们来验证一下这个
[06:18] 这里还在计算中等他计算完成这里日志已经刷的很快了这里呢咱们来看一下因为咱们刚才呢是在咱们代码里边啊不是刚才咱们代码里边呢是有日志打打印的是有一个是有一个输出结果打印的但是这个地方的话日志太多了咱们并没有看到那个输出结果走走走走走哎并没有看到这个输出结果
[06:58] 但是呢这个代码也是没有报错的就说明咱们这个已经是OK的了我来搜一下搜一下咱们的日志在这里time for matter这里呢已经OK但是刷到咱们的日志了在这里由于日志太多咱们这个结果就被给刷没了通过这个搜索的方式终于把它给找到了OK
[07:38] 咱们验证完代码是OK到之后说明咱环境OK你代码才能运行这时候呢由于WinUtils没有配置导致咱们这个Windows开发环境代码不能运行这个问题呢就解决了还是刚才说的如果WinUtils配置了然后代码还报错一定要及时反馈好 视频就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Windows 环境下配置并运行一个基于 Spark 和 Hive 的数据处理程序，重点演示了 winutils.exe 的配置、Spark 作业的执行过程以及 Hive 表的创建与数据插入。

2) 按时间顺序列出每张画面的要点：
画面1：显示 Windows 系统信息，确认 CPU 为 Intel Core i7-5775R，内存 16.0 GB，系统为 Windows 10 家庭版。
画面2：IntelliJ IDEA 启动界面，显示版本 2019.2.3，下方有“配置 HADOOP_HOME 环境变量如下图所示”的文字提示。
画面3：IntelliJ IDEA 编辑器中显示 Scala 代码，创建 SparkSession 并初始化 HiveContext，终端输出 Spark 服务启动成功。
画面4：代码中调用 HiveContext，终端输出 Hive 外部元数据初始化成功。
画面5：调试器界面，显示代码执行到 `Hive.createDatabase` 方法，变量区域显示 `area code` 的值。
画面6：文件资源管理器显示项目目录结构，包含 `code`、`data`、`images`、`nifi`、`nhl`、`winutils.zip` 等文件夹。
画面7：PPT 页面，标题为“情况2：有Hadoop环境”，说明需将 winutils.zip 解压到 HADOOP_HOME 目录下，环境变量配置为 HADOOP_HOME=D:\devtools\Hadoop-2.6.0\bin，目录结构图显示 bin 目录下有 winutils.exe。
画面8：PPT 页面，内容与画面7相同，但鼠标光标在“winutils.exe”文件上。
画面9：代码中执行 `Hive.metastore.warehouse.dir` 设置，终端输出 Hive 元数据初始化成功。
画面10：终端输出 Spark 作业执行过程，显示任务启动和完成。
画面11：终端输出 Spark 作业执行过程，显示任务启动和完成。
画面12：代码中添加注释“// 输出表”，并显示 `areaTable` 变量。
画面13：代码中执行 `result.createReplaceTempView` 创建临时视图，终端输出表创建成功。
画面14：PPT 页面，标题为“3.2.7.1 注意事项”，说明“Windows 配置winutils”，并显示“情况1：无Hadoop环境”的配置方法，环境变量配置为 HADOOP_HOME=D:\devtools\bin。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3代码：
val Spark = EIEnvironment.getSparkSession(this.getTask.getSplitData)
val sc = Spark.sparkContext
val Hive = Spark.sqlContext

画面4代码：
val area = area.split(" ")
val sheng = strings(0).trim().split(" ")
val shi = strings(1).trim().split(" ")
val xian = strings(2).trim().split(" ")
areaCodeMap(sheng(0), sheng(1), shi(0), shi(1), xian(0), xian(1))

画面5代码：
Hive.createDatabase(area, createReplaceTempView("area_code"))

画面9代码：
val Spark = EIEnvironment.getSparkSession(this.getTask.getSplitData)
val sc = Spark.sparkContext
val Hive = Spark.sqlContext

画面13代码：
result.createReplaceTempView("region")
select
a.id area_dim
b.shengCode province
b.shiCode city
b.xianCode county
a.lng longitude
a.lat latitude
from area_dim a
join region b on a.id = b.id

画面7目录结构：
winutils
bin
winutils.exe

画面14环境变量配置：
HADOOP_HOME=D:\devtools\bin

4) PPT 标题、架构图/流程图的结构、表格数据：
画面7标题：“情况2：有Hadoop环境”
画面7表格数据：
环境变量：
变量：HADOOP_HOME
值：D:\devtools\Hadoop-2.6.0\bin

画面14标题：“3.2.7.1 注意事项”
画面14表格数据：
情况1：无Hadoop环境
环境变量：
变量：HADOOP_HOME
值：D:\devtools\bin

5) 无其他内容。

