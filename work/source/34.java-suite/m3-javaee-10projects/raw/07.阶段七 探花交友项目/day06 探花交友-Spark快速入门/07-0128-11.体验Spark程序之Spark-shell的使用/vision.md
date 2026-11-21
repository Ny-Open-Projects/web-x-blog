# 画面线理解：11.体验Spark程序之Spark-shell的使用

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\11.体验Spark程序之Spark-shell的使用_【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:58, 02:03, 02:29, 02:57, 03:25, 03:51, 04:19, 04:47, 06:14, 06:42, 07:12, 07:55, 09:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:24:34

1) 这一组画面整体在讲什么（一句话）：
演示如何在本地启动 Spark Shell 并执行一个单词计数的 Spark 作业，随后通过 Spark Master 启动远程集群作业并查看作业执行结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：显示 Spark 作业执行完成后的日志，包括任务完成、Stage 结束、Spark Web UI 关闭、各组件停止等信息。
画面 2：显示 Spark Shell 启动成功，提示信息包括 Spark 版本、Scala 版本、Web UI 地址和 Spark 上下文。
画面 3：在 Spark Shell 中输入命令 `sc.textFile("file:///itcast/word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(+).collect`，准备执行单词计数。
画面 4：在 Spark Shell 中输入命令 `sc.textFile("file:///itcast/word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(+).collect`，准备执行单词计数。
画面 5：在 Spark Shell 中输入命令 `sc.textFile("file:///itcast/word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(+).collect`，准备执行单词计数。
画面 6：在 Spark Shell 中输入命令 `sc.textFile("file:///itcast/word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(+).collect`，准备执行单词计数。
画面 7：在 Spark Shell 中输入命令 `sc.textFile("file:///itcast/word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(+).collect`，准备执行单词计数。
画面 8：在 Spark Shell 中执行完单词计数命令后，输出结果 `res0: Array[(String, Int)] = Array((hello,4), (mvc,1), (world,1), (spark,1), (spring,1))`。
画面 9：在终端中执行命令 `./spark-shell --master spark://node2:7077`，启动远程 Spark Shell。
画面 10：在远程 Spark Shell 中执行命令 `sc.textFile("file:///itcast/word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(+).saveAsTextFile("file:///itcast/wc")`，将结果保存到文件。
画面 11：在远程 Spark Shell 中执行命令 `sc.textFile("file:///itcast/word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(+).saveAsTextFile("file:///itcast/wc")`，将结果保存到文件。
画面 12：在终端中执行命令 `cd itcast`，然后 `cd wc`，查看生成的输出文件。
画面 13：在 Spark Master 的 Web UI 页面上，显示了作业 `app-20190809184331-0005` 的执行详情，包括多个 Worker 节点的执行状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```
19/08/09 18:26:25 INFO TaskSetManager: Starting task 9.0 in stage 0.0 (TID 9, 192.168.31.82, executor
2 partition 9, PROCESS_LOCAL, 7430 bytes)
19/08/09 18:26:25 INFO TaskSetManager: Finished task 8.0 in stage 0.0 (TID 8) in 37 ms on 192.168.31.82
(executor 2) (8/10)
19/08/09 18:26:25 INFO TaskSetManager: Finished task 9.0 in stage 0.0 (TID 7) in 41 ms on 192.168.31.82
(executor 2) (10/10)
19/08/09 18:26:25 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool
19/08/09 18:26:25 INFO DAGScheduler: ResultStage 0 (reduce at SparkPi.scala:39) took 2.369 s
19/08/09 18:26:25 INFO CoarseGrainedSchedulerBackend: Shutting down all executors
19/08/09 18:26:25 INFO SparkUI: Stopped Spark web UI at http://itcast:4040
19/08/09 18:26:25 INFO StandaloneSchedulerBackend: Shutting down all executors
19/08/09 18:26:25 INFO MapOutputTrackerMasterEndpoint: MapOutputTrackerMasterEndpoint stopped!
19/08/09 18:26:25 INFO MemoryStore: MemoryStore cleared
19/08/09 18:26:25 INFO BlockManagerMaster: BlockManagerMaster stopped
19/08/09 18:26:25 INFO OutputCommitCoordinatorEndpoint: OutputCommitCoordinatorEndpoint stopped!
19/08/09 18:26:25 INFO SparkContext: Successfully stopped SparkContext
19/08/09 18:26:25 INFO ShutdownHookManager: Shutting down hook called
19/08/09 18:26:25 INFO ShutdownHookManager: Deleting directory /tmp/spark-8a7d217-9448-4b23-a1ef-174c
355f4acc
```

画面 2：
```
[root@itcast bin]# /spark-shell
19/08/09 18:38:59 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using
builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://itcast:4040
Spark context available as 'sc' (master = local[*], app id = local-1565347144325).
Spark session available as 'spark'.
Welcome to
Spark
version 2.4.3
Using Scala version 2.11.12 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_141)
Type in expressions to have them evaluated.
Type :help for more information.
scala>
```

画面 3：
```
[root@itcast bin]# /spark-shell
19/08/09 18:38:59 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using
builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://itcast:4040
Spark context available as 'sc' (master = local[*], app id = local-1565347144325).
Spark session available as 'spark'.
Welcome to
Spark
version 2.4.3
Using Scala version 2.11.12 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_141)
Type in expressions to have them evaluated.
Type :help for more information.
scala>
```

画面 4：
```
scala> sc.textFile("file:///itcast/word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(+).collect
```

画面 5：
```
scala> sc.textFile("file:///itcast/word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(+).collect
```

画面 6：
```
scala> sc.textFile("file:///itcast/word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(+).collect
```

画面 7：
```
scala> sc.textFile("file:///itcast/word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(+).collect
```

画面 8：
```
res0: Array[(String, Int)] = Array((hello,4), (mvc,1), (world,1), (spark,1), (spring,1))
```

画面 9：
```
[root@itcast bin]# ./spark-shell --master spark://node2:7077
19/08/09 18:43:
