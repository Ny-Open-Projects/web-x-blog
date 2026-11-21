# 画面线理解：13-Zeppelin简介、Zeppelin调式Spark程序

- 阶段：08.阶段八 智慧学成项目
- 章节：01.第一章 智慧学成-项目介绍环境搭建
- 源文件：08.阶段八 智慧学成项目\01.第一章 智慧学成-项目介绍环境搭建\13-Zeppelin简介、Zeppelin调式Spark程序_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:09, 01:59, 02:22, 03:43, 04:31, 04:37, 05:25, 05:56, 06:29, 08:01, 11:02, 11:33, 11:52, 12:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:35:28

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Docker 启动 Zeppelin 并使用 Spark SQL 和 Spark Core 进行数据操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：介绍 Zeppelin 是一个基于网页的交互式数据分析开源框架，支持数据查询、可视化等功能，并展示其界面元素（表格、柱状图、折线图等）。
画面2：继续介绍 Zeppelin，强调其支持多种语言（Scala、Python、SparkSQL、Hive、HBase、Elasticsearch、JDBC等），并展示配置 spark 属性的界面。
画面3：展示 Zeppelin Notebook 页面，准备创建新 Notebook。
画面4：在 Zeppelin 中创建新 Notebook，选择默认解释器为 spark。
画面5：在 Zeppelin 文档中说明创建 spark notebook 的操作步骤。
画面6：展示 Zeppelin Notebook 界面，准备执行 spark sql 查询数据库。
画面7：在终端中执行 docker-compose up 命令启动服务。
画面8：在终端中执行 bash 命令进入容器环境。
画面9：展示 Zeppelin Notebook 界面，准备执行 spark sql 查询数据库。
画面10：在 Zeppelin Notebook 中输入 Spark 代码读取文件。
画面11：在 Zeppelin Notebook 中执行 Spark 代码，显示结果。
画面12：在 Zeppelin 文档中说明使用 SparkSQL 查看数据库。
画面13：展示 Zeppelin Notebook 页面，准备创建新 Notebook。
画面14：展示 Zeppelin Notebook 界面，准备执行 spark sql 查询数据库。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
a. Apache Zeppelin 是一个基于网页的交互式数据分析开源框架。Zeppelin提供了数据
分析，数据可视化功能支持的界面如下所示：
```
画面2：
```
启动zeppelin 如果已启动，此步可跳过，继续下一步
在docker-compose.yml文件中执行bash命令，这里的路径是：/opt/cdh5.14.0
docker-compose up -d xc-online-zeppelin
```
画面7：
```
xc-online-s$ docker-compose up -d xc-online-zeppelin
```
画面8：
```
xc-online-s$ xc-online-hive bash
```
画面10：
```
val input = sc.textFile("/hdfs://xc-online-hadoop:9000/word.txt")
```
画面11：
```
val counts = input.flatMap(line => line.split(" ")).map(word => (word, 1)).reduceByKey(_ + _).sortBy(_._2, false)
counts.collect().foreach(println(_))
```
画面14：
```
show databases
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题“3.1 什么是Zeppelin”，内容包括 Zeppelin 的功能介绍和界面元素。
画面2：PPT标题“3.2 Zeppelin配置spark”，内容包括启动命令和配置界面。
画面5：PPT标题“3.3 Zeppelin运行spark程序”，内容包括创建 notebook 的操作步骤。
画面6：PPT标题“3.3.2 使用SparkSQL查看有多少数据库”，内容包括 spark sql 查询数据库的界面。
画面12：PPT标题“3.3.2 使用SparkSQL查看有多少数据库”，内容包括 spark sql 查询数据库的界面。
画面13：PPT标题“3.3.1 创建spark notebook”，内容包括创建 notebook 的操作步骤。
画面14：PPT标题“3.3.2 使用SparkSQL查看有多少数据库”，内容包括 spark sql 查询数据库的界面。

5) 不要评价画面美观，不要输出与课程无关的内容。
