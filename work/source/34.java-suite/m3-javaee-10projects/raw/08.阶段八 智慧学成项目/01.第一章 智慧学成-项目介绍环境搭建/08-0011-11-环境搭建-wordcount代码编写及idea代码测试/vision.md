# 画面线理解：11-环境搭建-wordcount代码编写及idea代码测试

- 阶段：08.阶段八 智慧学成项目
- 章节：01.第一章 智慧学成-项目介绍环境搭建
- 源文件：08.阶段八 智慧学成项目\01.第一章 智慧学成-项目介绍环境搭建\11-环境搭建-wordcount代码编写及idea代码测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:03, 02:37, 03:03, 03:39, 05:19, 07:43, 08:44, 10:38, 11:50, 12:19, 12:41, 13:19, 14:26, 14:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:34:23

1) 这一组画面整体在讲如何在IDEA中编写并提交一个统计单词个数的Spark任务，包括准备数据、编写Scala代码、提交任务等步骤。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程PPT内容，标题为“2.4 测试项目”，子标题“2.4.1 IDEA 中 Spark任务提交过程”，并列出步骤：1. 准备word.txt文件用于统计；2. 上传到hadoop；3. 编写scala统计代码；4. Idea中测试代码；5. 提交spark集群测试。下方展示word.txt内容，包含多行单词。
画面2: 展示终端窗口，执行命令 `docker exec -it xc-online-hadoop bash` 进入Hadoop容器，随后执行 `hadoop fs -put word.txt` 命令上传文件。
画面3: 展示课程PPT内容，与画面1内容相同，但页面位置略有不同，显示“上传hadoop步骤”下的命令 `docker exec -it xc-online-hadoop bash` 和 `vi word.txt`。
画面4: 展示IDEA界面，鼠标右键点击项目中的“first”文件，弹出菜单，选择“Run”选项。
画面5: 展示IDEA界面，编辑器中打开Scala文件WordCount.scala，代码中包含 `import cn.iteast.xc.common.fileEnvironment` 和 `object WordCount {`，光标位于 `val spark: SparkSession = ...` 行。
画面6: 展示课程PPT内容，与画面1内容相同，页面位置不同，显示“上传hadoop步骤”下的命令 `docker exec -it xc-online-hadoop bash` 和 `vi word.txt`。
画面7: 展示IDEA界面，编辑器中打开WordCount.scala文件，代码中包含 `import org.apache.spark.sql.SparkSession`，并定义了 `val spark: SparkSession = ...` 和 `val sc = spark.sparkContext`。
画面8: 展示IDEA界面，编辑器中WordCount.scala文件，代码中包含 `.flatMap(line => line.split(regexp = " "))` 和 `.reduceByKey(_ + _)`。
画面9: 展示课程PPT内容，与画面1内容相同，页面位置不同，显示“上传hadoop步骤”下的命令 `docker exec -it xc-online-hadoop bash` 和 `vi word.txt`。
画面10: 展示IDEA界面，运行窗口显示“Background Tasks”正在“Scanning files to index...”，同时“Messages”窗口显示编译成功信息和警告。
画面11: 展示课程PPT内容，与画面1内容相同，页面位置不同，显示“上传hadoop步骤”下的命令 `docker exec -it xc-online-hadoop bash` 和 `vi word.txt`。
画面12: 展示IDEA界面，运行窗口显示“WordCount”任务执行成功，输出结果为 `[(scala,2), (java,2), (tom,1), (spark,1)]`。
画面13: 展示IDEA界面，运行窗口显示Spark任务执行日志，包括“Successfully started Spark”、“BlockManager”、“MemoryStore”、“FileInputFormat”等信息。
画面14: 展示课程PPT内容，与画面1内容相同，页面位置不同，显示“上传hadoop步骤”下的命令 `docker exec -it xc-online-hadoop bash` 和 `vi word.txt`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```
步骤为：
1. 准备word.txt文件用于统计
2. 上传到hadoop
3. 编写scala统计代码
4. Idea中测试代码
5. 提交spark集群测试
2.4.1 IDEA 中 Spark任务提交过程
2.4.1.1 word.txt 上传hadoop
word.txt内容：
hi java
hello
world
java
scala
java
scala
hi
tom
java
spark
hadoop
scala
```
画面2:
```
docker exec -it xc-online-hadoop bash
hadoop fs -put word.txt
```
画面3:
```
# 登陆容器
docker exec -it xc-online-hadoop bash
# 创建并编辑word.txt文件，文件内容在上边
vi word.txt
```
画面4:
```
// 无代码内容
```
画面5:
```
package cn.iteast.xc.first
object WordCount {
  val spark: SparkSession = ...
}
```
画面6:
```
步骤为：
1. 准备word.txt文件用于统计
2. 上传到hadoop
3. 编写scala统计代码
4. Idea中测试代码
5. 提交spark集群测试
2.4.1 IDEA 中 Spark任务提交过程
2.4.1.1 word.txt 上传hadoop
word.txt内容：
hi java
hello
world
java
scala
java
scala
hi
tom
java
spark
hadoop
scala
```
画面7:
```
import org.apache.spark.sql.SparkSession
object WordCount {
  val spark: SparkSession = ...
  val sc = spark.sparkContext
  val input = sc.textFile("hdfs://xc-online-hadoop:9000/word.txt")
}
```
画面8:
```
// 进行分词
input.flatMap(line => line.split(regexp = " "))
// 统计单词出现次数
.map(word => (word, 1))
.reduceByKey(_ + _)
```
画面9:
```
步骤为：
1. 准备word.txt文件用于统计
2. 上传到hadoop
3. 编写scala统计代码
4. Idea中测试代码
5. 提交spark集群测试
2.4.1 IDEA 中 Spark任务提交过程
2.4.1.1 word.txt 上传hadoop
word.txt内容：
hi java
hello
world
java
scala
java
scala
hi
tom
java
spark
hadoop
scala
```
画面10:
```
Information: Kotlin: kotlinc-jvm 1.3.41 (JRE 1.8.0_221-b11)
Information: Modules 'xc-service-offline', 'xc-common-entity', 'xc-common-utils' were fully rebuilt due to project configuration/dependencies changes
Information: 2019/11/13 17:26:20 INFO Build completed successfully in 18 s 200 ms
Warning: (113, 12) This catches a Throwable. If this is really intended, use 'case e: Throwable' to clear this warning.
Warning: (27, 12) This catches a Throwable. If this is really intended, use 'case e: Throwable' to clear this warning.
```
画面11:
```
步骤为：
1. 准备word.txt文件用于统计
2. 上传到hadoop
3. 编写scala统计代码
4. Idea中测试代码
5. 提交spark集群测试
2.4.1 IDEA 中 Spark任务提交过程
2.4.1.1 word.txt 上传hadoop
word.txt内容：
hi java
hello
world
java
scala
java
scala
hi
tom
java
spark
hadoop
scala
```
画面12:
```
WordCount
WordCount taskscheduler: Removed task 1.0, whose tasks have all completed, from pool
WordCount taskscheduler: ResultStage 1 (collect at WordCount.scala:35) Finished in 0.088 s
19/11/13 17:26:20 SparkUI: Stopped Spark UI at http://192.168.48.1:4040
```
画面13:
```
19/11/13 17:28:00 INFO Utils: Successfully started Spark network service on port 3222.
19/11/13 17:28:00 INFO BlockManagerMaster: Registering BlockManager
19/11/13 17:28:00 INFO BlockManagerMasterEndpoint: Registering block manager
19/11/13 17:28:00 INFO MemoryStore: Block broadcast_0 stored as bytes in memory (estimated size 211.4 KB, free 1987.3 MB)
19/11/13 17:28:00 INFO SparkContext: Created broadcast_0 from textFile at WordCount.scala:25
19/11/13 17:28:00 INFO FileInputFormat: Total input paths to process : 1
```
画面14:
```
<artifactId>junit</artifactId>
<version>4.12</version>
<scope>test</scope>
</dependency>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、3、6、9、11、14: PPT标题为“2.4 测试项目”，子标题
