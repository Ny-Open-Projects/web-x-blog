# 画面线理解：12-环境搭建-wordcount任务提交到集群执行

- 阶段：08.阶段八 智慧学成项目
- 章节：01.第一章 智慧学成-项目介绍环境搭建
- 源文件：08.阶段八 智慧学成项目\01.第一章 智慧学成-项目介绍环境搭建\12-环境搭建-wordcount任务提交到集群执行_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:35, 01:09, 01:36, 02:14, 02:36, 03:32, 04:12, 05:19, 05:39, 06:12, 06:45, 07:06, 07:23, 07:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:34:56

1) 这一组画面整体在讲如何使用IDEA打包Scala项目并使用spark-submit将任务提交到Spark集群。

2) 按时间顺序列出每张画面的要点：
画面1：
- IDE中显示项目结构，选中`target`目录下的`xc-service-offline.jar`。
- 代码中`WordCount.scala`文件内容：
  ```scala
  val counts = sc.textFile("https://xc-online-bakup:9000/word.txt")
  .flatMap(line => line.split(" "))
  .map(word => (word, 1))
  .reduceByKey(_ + _)
  .sortBy(_._2, ascending = false)
  counts.collect().foreach(println(_))
  ```
- Maven面板显示`package`步骤。

画面2：
- IDE中显示`application.properties`文件内容：
  ```properties
  usingCluster=true
  ```
- 控制台显示Maven编译过程中的警告信息，包括多个Scala版本冲突。

画面3：
- 控制台显示Maven编译过程中的警告信息，包括多个Scala版本冲突。
- Maven面板显示`package`步骤。

画面4：
- 控制台显示Maven编译过程中的警告信息，包括多个Scala版本冲突。
- Maven面板显示`package`步骤。

画面5：
- PPT页面标题为“2.4.2 提交Spark任务到集群”，子标题“2.4.2.1 使用IDEA打包任务”。
- 图解说明：在Maven视图中，点击`Lifecycle` -> `package`，将`xc-service-offline.jar-with-dependencies.jar`改名为`wordcount.jar`。
- 图中红色箭头标注“打包后，不能直接运行”，“打包后，不能直接运行”。

画面6：
- WinSCP界面显示`/opt`目录下的文件，包括`xc-service-offline.jar`。
- IDE中显示项目结构。

画面7：
- 控制台显示命令行操作，包括进入`/opt/jars`目录，执行`docker cp wordcount.jar xc-online-spark:/opt`。
- PPT页面标题为“2.4.2 提交Spark任务到集群”，子标题“2.4.2.1 使用IDEA打包任务”。

画面8：
- 控制台显示使用`spark-submit`提交任务的命令和输出日志。
- 日志显示Spark服务启动成功，包括`SparkContext`、`BlockManagerMaster`、`MemoryStore`等信息。

画面9：
- IDE中显示项目结构，选中`target`目录下的`xc-service-offline.jar`。
- 控制台显示Maven编译过程中的警告信息，包括多个Scala版本冲突。
- Maven面板显示`package`步骤。

画面10：
- 浏览器空白页面，地址栏为空。

画面11：
- 浏览器显示Spark任务的stdout日志页面，显示任务执行过程中的日志信息。
- 日志内容包括`Executor`、`Stage`、`BlockManagerMaster`等信息。

画面12：
- PPT页面标题为“2.4.2 提交Spark任务到集群”，子标题“2.4.2.1 使用IDEA打包任务”。
- 图解说明：在Maven视图中，点击`Lifecycle` -> `package`，将`xc-service-offline.jar-with-dependencies.jar`改名为`wordcount.jar`。
- 图中红色箭头标注“打包后，不能直接运行”，“打包后，不能直接运行”。

画面13：
- PPT页面标题为“2.4.2 提交Spark任务到集群”，子标题“2.4.2.3 使用spark-submit进行提交到集群”。
- 代码示例：
  ```bash
  spark-submit --class cn.itcast.xc.first.WordCount --master spark://xc-online-spark:7077 wordcount.jar
  ```
- 图解说明：将`wordcount.jar`上传到Spark容器的`/opt/jars`目录。

画面14：
- PPT页面标题为“2.4.2 提交Spark任务到集群”，子标题“2.4.2.2 上传任务到spark容器”。
- 代码示例：
  ```bash
  docker cp wordcount.jar xc-online-spark:/opt
  ```
- 图解说明：将`wordcount.jar`上传到Spark容器的`/opt`目录。
