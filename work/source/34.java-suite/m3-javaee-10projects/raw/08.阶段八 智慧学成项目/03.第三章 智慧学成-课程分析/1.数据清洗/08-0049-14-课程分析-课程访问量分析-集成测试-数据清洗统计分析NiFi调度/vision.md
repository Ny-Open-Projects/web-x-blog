# 画面线理解：14-课程分析-课程访问量分析-集成测试-数据清洗统计分析NiFi调度

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\14-课程分析-课程访问量分析-集成测试-数据清洗统计分析NiFi调度_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:29, 01:44, 02:26, 03:06, 03:49, 04:16, 04:56, 05:18, 06:53, 08:53, 09:30, 10:24, 11:33, 12:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:56:47

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Nifi 数据采集、调度代码执行、Spark 处理和 Hive 数据存储，完成课程访问事实表的数据处理全流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Nifi 界面中三个处理组的监控面板，分别是“数据采集：课程访问量-ToHDFS”、“数据清洗统计：课程访问量”和“落地业务库：课程访问量-Hive-ToMysql”，并说明 Nifi 主要承担数据采集和清洗任务。
画面2：展示 Nifi 调度代码的部署步骤，需将 jar 包上传至容器的 /opt/run/jars 目录，并将脚本上传至 /opt/run/script 目录。
画面3：展示 Scala 代码文件 CourseVisitProcessDay.scala 的内容，包含 SparkSession 初始化和 main 函数。
画面4：在 Nifi 界面中点击“Upload Template”，弹出“Select Template”对话框。
画面5：在 Nifi 界面中保存处理组配置，弹出“Process group configuration successfully saved”提示框。
画面6：展示 Scala 代码中处理数据路径和过滤条件的逻辑，包括对数据的切分和时间戳转换。
画面7：在 Windows 资源管理器中显示 /opt/tmps 目录，其中包含课程访问事实表的处理脚本。
画面8：在 Xshell 中连接到 Nifi 容器的终端界面。
画面9：在 Xshell 终端中执行命令，将 jar 包复制到 Nifi 容器的 /opt 目录，并执行脚本启动 Nifi 流程。
画面10：在 Hue 界面中查看 Hive 表 course_visit_fact 的属性和统计信息。
画面11：在 Hue 的文件浏览器中查看 /user/hive/external/data_course 目录下的文件，包括 course_visit_fact 表。
画面12：在 Spark Master 界面中查看正在运行的应用程序，显示名为 VisitSourceToFact 的 Spark 作业正在运行。
画面13：在 Hue 的 Hive 编辑器中编写并执行 SQL 查询语句 SELECT * FROM course_visit_bi。
画面14：展示 Nifi 界面中三个处理组的监控面板，与画面1相同，下方文字提示“后续步骤进行联动配置”，并显示章节标题“1.3.1 数据采集”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```scala
import org.apache.spark.sql.SparkSession

object VisitSourceToFact {
  def main(args: Array[String]): Unit = {
    import spark.implicits._
    val spark = EtlEnvironment.getSparkSession(this.getClass.getSimpleName)
    val sc = spark.sparkContext
    val data_info = "2019-11-18"
    // 代码省略
  }
}
```

画面6：
```scala
val visitSource = sc.textFile(path = s"/user/hive/external/data/course/visit_source/${data_info}.txt")
val visitList = visitSource
  .map(_.split("V"))
  .filter(_.contains("Robot"))
  .filter(arr => {
    val dataInfo = getDateTime(arr(0).toString, "yyyy-MM-dd")
    dataInfo == data_info
  })
```

画面9：
```bash
cp course_visit_process.sh /opt/tmps/
course_visit_process.sh course_visit_process.sh xc-service-offline.jar-with-dependencies.jar
xc-online:/opt/tmps$ docker cp course_visit_process.sh xc-online-nifi:/opt
xc-online:/opt/tmps$ docker cp course_visit_process.sh xc-online-nifi:/opt
xc-online:/opt/tmps$ ls
course_visit_process.sh
xc-online:/opt/tmps$ ./course_visit_process.sh hive mysql-connector-java-8.0.16.jar spark xc-service-offline.jar-with-dependencies.jar
```

画面13：
```sql
SELECT * FROM course_visit_bi;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、14：PPT 标题为“1.3.1 数据采集”，左侧目录结构显示“1.3 集成测试”下的“1.3.3 Nifi调度代码”。
画面2：PPT 标题为“1.3.3 Nifi调度代码”，内容说明 Nifi 调度代码的部署方式。
画面10：Hue 界面显示表 course_visit_fact 的属性和统计信息，包括表名、创建时间、存储格式等。
画面12：Spark Master 界面显示正在运行的应用程序，包括 Application ID、Name、Cores、Memory per Executor、State、Duration 等字段。
画面13：Hue 界面显示 SQL 查询语句和执行结果，包括查询语句、执行时间、返回结果等。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
