# 08系统集成测试-NiFi采集-清洗-统计分析-离线分析-热门学科排名

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\08系统集成测试-NiFi采集-清洗-统计分析-离线分析-热门学科排名_【海量资源尽在 666java.com】.mp4
- 时长 6分52秒（音频 412s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,离线分析中还有热门学科排名,没有按照咱们的测试步骤进行一个测试。
[00:08] 接下来呢,就切到NiFi进行热门学科排名的测试。
[00:14] 咱们来切到NiFi。
[00:16] 这里呢,已经进入到咱们热门学科排名的处理器组。
[00:21] 首先呢,是数据的采集。
[00:23] 这里呢,数据的采集和
[00:26] 课程购买量的采集一样的都是采集MySQL中的数据这里呢先把采集MySQL数据的这个处理器组给启动了这里呢它会监控MySQL的数据来过滤咱们用户选客的这个原始数据并且把它采集到数据仓库中这里呢原始数据的生产咱们采用NetFi生产数据的方式这里呢也是直接启动集合
[00:55] 这里咱们测试的话生产2000多条数据就行了这里可以看到对列中呢还是数据蛮多的咱们只用看到这个地方大概有2000条以上的数据咱们就可以把整个处理器组给停下来了这里呢数据还在生产的过程中2000好已经超过2000条了停下来一共是2497条这个时候呢咱们就可以
[01:27] 来查看咱们NetFi的监控MySQL的采集是否将数据采集到这里呢可以看到它已经处理了一个一组数据第二组数据呢正在处理中刷新因为Hive的话存储它需要做相应的计算这个存储没有MySQL快可以看到这个呢存储也一定成功成功之后呢采集的处理系统就可以停止了
[01:58] 采集的处理器组停止完成之后呢咱们就是数据的清洗分析以及咱们落地到业务库的一个任务调度按顺序就是把处理器组给启动了这个时候呢等待咱们这个处理器执行完成即可这里呢可以看到对列中是有数据的这个对列在这里咱们呢也可以登录Spark来查看一下
[02:32] 刚才呢是有我之前测试的这个缓存这个时候咱们重新刷新这个新的数据已经进来了这里任务的处理还是比较多了咱们呢稍微暂停一下等待这个任务调度执行完成好咱们继续这里呢可以看到现在对列中只有一个数据了OK就在我刚才说话这个时间这个呢对列也已经处理完成
[03:07] 处理完成之后呢,咱们可以看到,现在呢,是在等待去下一个处理器组这个任务调度中,它呢,默认是等待30秒,咱们呢,等待即可。
[03:22] 好,这个时候呢,已经看到它已经处理完成,处理完成之后呢,咱们来进到上一层,返回到上一层,返回到上一层呢,可以看到这个地方呢,每一个处理器组都有数据进入,都有数据进入之后呢,
[03:42] 也可以看到它每个处理器座都有数据的一个流动可以看到这也是已经处理完成了因为咱们存汉武往MySQL读数据这个速度还是非常快的OK每一个都处理完成咱们来可以切到MySQL验证一下下面的几张表就是咱们离线分析所用到离线分析中热门学科排名所用到的表来可以查看一下
[04:15] 咱们现在是12月的数据可以看到12月的数据往下找最下面这个就是了51周接下来是12月的数据也是有数据的51周有数据了12月是有数据的51周是有数据的也就是说这里咱们使用NiFi进行一个调度测试
[04:55] 数据的处理方式呢是使用传递日期的方式进行一个数据处理这个地方呢可以看到咱们数据处理呢是传递日期的一个处理这个地方呢还要多说一点咱们虽然说咱们这个地方数据清洗使用了数据这个传递这个日期它是简易了一个格式前面呢后边呢咱们在数据统计分析的时候这个日期呢传递的是当天的日期
[05:24] 这个传递当天的日期的一个原因是什么呢咱们在代码中这里的日期工具类在获取周的区间还有月的区间的时候它呢已经做了相应的处理它呢自动呢在这个地方是有相应的注释它是将自动的把这个日期呢减了1减1之后呢就得到了咱们需要的这个区间所以说咱们这个地方虽然说传的是日期但是呢传的是当天的之前咱们
[05:53] 清洗的时候传的日期呢离线分析还有咱们认为学科排名中除了咱们这个统计分析以外就是数据清洗还有离线分析前面的可能购买量可能防御量都是传的是前一天的日期因为那个是什么那个是属于数据清洗的咱们生产的一个数据但是这个的话它是属于统计因为咱们这个地方
[06:21] 任门学科排名用了中间表的数据用的是任课程购买量中间表的数据它呢这个地方就传的是当天的这个日期这个地方因为已经配置好稍微了解一下即可通过测试呢咱们已经将离线分析中任门学科排名的这个调度呢处理完成咱们来回到文档到此呢咱们离线分析已经配置完成视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Nifi 进行数据采集、清洗和统计分析，并通过 Spark 处理数据，最终将结果写入 MySQL 和 Hive。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 Nifi 界面，包含三个处理节点：
  - 1. 数据生产：用户选课 To MySQL
  - 2. 数据清洗分析：热门学科排名
  - 3. 数据落地：热门学科排名 To Hive
- 节点间通过“From out”和“To Input”连接。

画面 2：
- 显示 Nifi 界面，展示数据处理流程：
  - RouteOnAttributeUpdateInsert
  - MySQLBinLogCdcProcessor
  - PutHive
- 数据从 MySQL Binlog 采集，经过处理后写入 Hive。

画面 3：
- 显示 Spark Master 界面，显示正在运行的应用程序：
  - Running Applications (5)
  - Completed Applications (2)
- 显示 Worker 节点状态和资源使用情况。

画面 4：
- 显示 Nifi 界面，展示数据处理流程：
  - 多个处理节点，包括：
    - subject_sales_volume_by_week_biz
    - subject_sales_volume_by_month_biz
    - subject_sales_by_week_biz
    - subject_sales_by_month_biz
  - 节点间通过“From out”和“To Input”连接。

画面 5：
- 显示 Nifi 界面，展示数据处理流程：
  - 热门学科排名 Hive-To-Mysql
  - 热门学科人数统计 Hive-To-Mysql
  - 节点间通过“From out”和“To Input”连接。

画面 6：
- 显示 Nifi 界面，展示数据处理流程：
  - 热门学科排名 Hive-To-Mysql
  - 热门学科人数统计 Hive-To-Mysql
  - 节点间通过“From out”和“To Input”连接。

画面 7：
- 显示 Navicat Premium 界面，展示 MySQL 数据库表：
  - 表名：subject_amount_week_biz
  - 数据列：course_category_dim_id, course_category_name, sale_num, sale_percent, date_info
  - 当前选中行数据。

画面 8：
- 显示 Navicat Premium 界面，展示 MySQL 数据库表：
  - 表名：subject_sale_week_biz
  - 数据列：course_category_dim_id, course_category_name, sale_num, sale_percent, date_info
  - 当前选中行数据。

画面 9：
- 显示 Navicat Premium 界面，展示 MySQL 数据库表：
  - 表名：subject_amount_week_biz
  - 表名：subject_sale_week_biz
  - 表名：subject_sale_month_biz
  - 表名：subject_user_month_biz
  - 表名：subject_user_week_biz
  - 表名：subject_visit_week_biz
  - 表名：subject_visit_month_biz
  - 表名：agency_amount_month_biz
  - 表名：agency_amount_week_biz
  - 表名：agency_sale_month_biz
  - 表名：agency_sale_week_biz
  - 表名：agency_user_month_biz
  - 表名：agency_user_week_biz
  - 表名：course_hot_month_biz
  - 表名：course_hot_week_biz
  - 表名：course_buy_biz
  - 表名：course_visit_biz
  - 表名：platform_offline_biz

画面 10：
- 显示 Nifi 界面，展示数据处理流程：
  - subject-sales-volume-by-week-biz
  - subject-sales-volume-by-month-biz
  - 节点间通过“From out”和“To Input”连接。

画面 11：
- 显示 Nifi 界面，展示数据处理流程：
  - 多个处理节点，包括：
    - subject_sales_volume_by_week_biz
    - subject_sales_volume_by_month_biz
    - subject_sales_by_week_biz
    - subject_sales_by_month_biz
  - 节点间通过“From out”和“To Input”连接。

画面 12：
- 显示 IntelliJ IDEA 界面，展示 Scala 代码：
  - 文件路径：src/main/scala/com/xxx/analysis/sales/SubjectSalesByMonthBiz.scala
  - 代码内容：
    ```scala
    val dateInfo = "2019-07-12"
    println(getMonthInterval(dateInfo))
    println(getMonthInterval(dateInfo))
    ```
    ```scala
    def getMonthInterval(dateInfo: String): String = {
      val sdf = new SimpleDateFormat(pattern = "yyyy-MM-dd")
      val date = sdf.parse(dateInfo)
      val calendar = Calendar.getInstance()
      calendar.setTime(date)
      val day = calendar.get(Calendar.DAY_OF_MONTH)
      calendar.set(Calendar.DAY_OF_MONTH, 1)
      val newMonth = calendar.get(Calendar.MONTH) + 1
      val newYear = calendar.get(Calendar.YEAR)
      val newMonthStr = newMonth + "月"
      val newYearStr = newYear + "年"
      return newMonthStr + "月" + newYearStr
    }
    ```
    ```scala
    calendar.setMilliseconds(date.getTime() - 86400000)
    val dateInfoNew = sdf.format(calendar.getTime())
    val newMonth = dateInfoNew.split(" ")[0].toInt
    val newYear = dateInfoNew.split(" ")[1].toInt
    (newMonth, newYear)
    ```

画面 13：
- 显示 Nifi 界面，展示处理器属性设置：
  - Processor Details
  - 属性设置：
    - Command Argument: ${row().toNumber().minus(86400000).format("yyyy-MM-dd")}
    - Command Path: /opt/run/script/user_lewers_source_to_fact.sh
    - Ignore STDIN: true
    - Working Directory: /opt/run/script
    - Argument Delimiter: No value set
    - Max Attribute Length: 256

画面 14：
- 显示 Typora 文档，标题为“6.2 Nifi采集-清洗-统计分析”：
  - 步骤说明：
    1. 数据采集：使用 Nifi 生产数据的方式进行采集，根据指标逐个进行，生成一定量的数据后停止即可。
    2. 数据清洗统计分析：执行 Spark 时占用资源较多，根据指标逐个进行。
    3. 落地业务库和资源库：自动触发。
  - PS1：清理即时点的数据，osth索引数据及hbase存储的完整数据。
  - PS2：Nifi调度执行新业务报表系统的数据库清空，以便验证数据处理结果，清空脚本如下：
    ```sql
    # es中的数据需要删除，web端：http://xc-online:9100/
    disable 'learningonlineDetail'
    drop 'learningonlineDetail'
    ```
    ```sql
    truncate table agency_amount_month_biz;
    truncate table agency_amount_week_biz;
    truncate table agency_sale_month_biz;
    truncate table agency_sale_week_biz;
    truncate table agency_user_month_biz;
    truncate table agency_user_week_biz;
    truncate table course_hot_month_biz;
    truncate table course_hot_week_biz;
    truncate table course_buy_biz;
    truncate table course_visit_biz;
    truncate table subject_amount_month_biz;
    truncate table subject_amount_week_biz;
    truncate table subject_sale_month_biz;
    truncate table subject_sale_week_biz;
    truncate table subject_user_month_biz;
    truncate table subject_user_week_biz;
    truncate table subject_visit_month_biz;
    truncate table subject_visit_week_biz;
    ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 12：
```scala
val dateInfo = "2019-07-12"
println(getMonthInterval(dateInfo))
println(getMonthInterval(dateInfo))
```
```scala
def getMonthInterval(dateInfo: String): String = {
  val sdf = new SimpleDateFormat(pattern = "yyyy-MM-dd")
  val date = sdf.parse(dateInfo)
  val calendar = Calendar.getInstance()
  calendar.setTime(date)
  val day = calendar.get(Calendar.DAY_OF_MONTH)
  calendar.set(Calendar.DAY_OF_MONTH, 1)
  val newMonth = calendar.get(Calendar.MONTH) + 1
  val newYear = calendar.get(Calendar.YEAR)
  val newMonthStr = newMonth + "月"
  val newYearStr = newYear + "年"
  return newMonthStr + "月" + newYearStr
}
```
```scala
calendar.setMilliseconds(date.getTime() - 86400000)
val dateInfoNew = sdf.format(calendar.getTime())
val newMonth = dateInfoNew.split(" ")[0].toInt
val newYear = dateInfoNew.split(" ")[1].toInt
(newMonth, newYear)
```

画面 14：
```sql
# es中的数据需要删除，web端：

