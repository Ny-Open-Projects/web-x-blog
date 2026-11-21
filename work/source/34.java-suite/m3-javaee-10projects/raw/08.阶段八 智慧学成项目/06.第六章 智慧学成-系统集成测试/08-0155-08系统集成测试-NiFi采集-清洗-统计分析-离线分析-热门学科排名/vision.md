# 画面线理解：08系统集成测试-NiFi采集-清洗-统计分析-离线分析-热门学科排名

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\08系统集成测试-NiFi采集-清洗-统计分析-离线分析-热门学科排名_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:29, 02:26, 02:57, 03:35, 03:59, 04:21, 04:33, 04:44, 05:01, 05:17, 05:46, 05:55, 06:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:13:54

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
