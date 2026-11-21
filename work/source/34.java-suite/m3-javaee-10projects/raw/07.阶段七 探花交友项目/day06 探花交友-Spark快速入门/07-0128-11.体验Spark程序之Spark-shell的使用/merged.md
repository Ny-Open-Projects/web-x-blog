# 11.体验Spark程序之Spark-shell的使用

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\11.体验Spark程序之Spark-shell的使用_【海量资源尽在 666java.com】.mp4
- 时长 10分13秒（音频 613s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 那么接下来呢 我们来了解一下Spark sale的一个使用那么Spark sale呢 它其实是Spark所自带的这样的一个交互式的一个sale程序那我们可以在这个sale程序中呢 去输入一些命令那么就会在Spark中去做一些运行我们就可以看到一些这个结果了当然了 我们所输入的这个命令呢 是需要通过这个scanner这个语言去做一个编写那么前面呢 其实我们提到过我们本套课程呢
[00:30] 不会涉及到这个Skyler的语法的一个学习那么一会儿呢我们呢也是给大家做一些这个讲解大家能够看懂啊就可以了OK好那么我们首先来看一下我们的一个需求就是我们去读取本地的一个文件然后呢实现文件内的一个呃单词数量的一个这样的一个技术啊那我们来看一下啊怎么样去做一个实现呢那么首先呢我们是在我们的ITcast
[00:57] 这个目录下面呢去创建一个文件啊创建一个文件哎OK好那么来登录一下哎刚刚他退出了那么登录之后呢我们就在itcast哎我们用这个机器吧就是我们第一台这个节点然后呢我们去在这个下面去创建一个文件啊那么文件内容呢非常简单我们就把这个输入进来就好了就是这个什么hello world啊hello spree啊mvc啊Spark啊这样的一个
[01:26] 几个这个单词啊几句话呃然后呢我们去进入到itcast下面Spark下面有一个什么呢并目录啊在这个下面呢有一些这个脚本那么其实可以看到这个位置是不是有一个Spark sale对吧那我们就来去执行一下他呃点呃Spark干什么sale走那我们就可以启动这个sale程序了那么我们就可以在这个中呢去输入一些命令就可以看到一些这个结果了
[01:56] 它其实它是运行了一个什么相当于运行了一个本地的一个这样的一个这个SPARK那么我们可以看到在这个位置呢它帮我们去创建了一个SPARK的conductor然后呢并且呢给它设置为一个什么呢SC作为它的一个这个别名那我们可以通过SC就可以调用这个SPARK的conductor去做一些啊这样的一些这个实现了
[02:23] OK好那么接下来呢我们来看一下那我们把这个命令呢就拷贝过来来看一下那么这个命令呢其实我们所写的是通过Skala语言所写的这么一个命令啊那么简单的我们来解释一下是什么意思啊那么通过这个sc就是我们前面所提到的这个Spark的contact然后呢点这个text fill就是去读取一个文本的文件那么这个文件的路径在哪里呢
[02:52] 通过这个file冒号双斜杠来指定这是一个文件然后是在根目录下面的idcast下面的一个word这样的一个文件了OK那么读取到之后呢那么我们就需要通过一个flatmap那么就需要把这个数据呢做一个这个拍扁然后呢做一个这个操作那么怎么操作呢就是通过这个下滑线就代表着每一行我们那个数据了啊然后呢去通过一个split
[03:21] 然后呢空格去做一个分割然后呢我们再去做一个map这个操作map这个操作呢其实就是会对相同的这个单词呢去我们会对这个单词呢去做一个计数啊就每一个单词呢都出现一次去做一个计数然后呢再调用这个什么reduce by key那么就会对相同的这个单词呢去做一个这个合并然后呢我们去把它这个数量呢做一个相加
[03:50] 最后得到一个单词的一个总数那么在后面我们会写一个word count这样的一个程序也会实现这样的一个效果我们是通过这个Java来做一个编写那么大家对这个Scanla这样的一个语法然后去能够去通过我的一个讲解能够去把它能够认识读懂就可以了那么最后一个connector这个就是去真正的去做一个触发
[04:18] 这个SPARC去做一个执行并且去收集数据得到结果这样的一个过程然后我们来执行一下走那么他就去做一个最后的一个输出了可以看到那么最后的输出其实是一个输出的是一个我们的一个集合然后可以看到这个激素的结果就是Hello出现了4次MVC的一次Word的一次SPARC一次Spring一次那么这个就最终的一个结果跟我们刚刚的所
[04:47] 填写这个内容的这个结果呢是一致的对吧一致的那么刚刚这个代码的解释呢在下面这个位置是不是有详细的一个这样的一个说明呢那么刚刚呢其实我也给大家做了一些这个解释了那么如果还是不是很理解的同学呢可以看一下这一块的一个解释啊好那么接下来呢我们来看一下这个集群的一个运行那么刚刚呢我们在启动的时候其实我们并没有去指定这个master的地址
[05:15] 那么我们也发现了他也是可以正常执行的那么他其实是采用了什么SPAG的这个local啊这样的一个模式那么他并没有和集群的去关联起来啊那么我们要想去把我们这个呃就是我们刚刚啊说
[05:32] 希望去行这个应用去在我们的Spark中去做个运行的话那我们就需要去指定我们这个master了那我们来看一下那么我们在这个位置呢去通过我们这个Spark sale指定这个master指定它那么我们首先要确定一下我们的master是在哪里呢那么我们来看刷新一下那么还是我们刚刚的是不是这个上面就是这个
[05:58] 就是我们这个node2这个节点那么我们就可以去指定它了我们再来执行一下那就退出一下OK好那我们再来去做一个指定那么这个时候它就会去连接到我们这个集群了那我们稍微等待一下那么其实可以看到呢在这个位置啊在这个位置它其实已经告诉我们了must我们现在是不是已经连接到是node2这个的7077啊这样的一个这个节点了
[06:26] OK好那么接下来呢我们还是呢去做这样的一个命令的拷贝那么要注意的是呢这个命令跟之前的命令有所不同就是在前面这一段前面这一段的都是一样的只是在最后呢有所不同就是在这个位置了那么这个位置呢它并不是直接去做一个输出而是什么呢把我们这个结果去写入到我们的一个目标的一个文件中
[06:53] 那么是在根目录下面的IDcast下面有个WC这样的一个目录那么这个目录其实指向的就是我们本机的目录注意是本机的这个目录并不是我们的Zookeeper目录这一定要搞清楚好然后我们回测一下那么等待它的一个执行那么执行结束之后那么就OK了那么刚刚其实我们可以看到它有一个执行的一个进度的这样的一个效果
[07:20] 那么现在就已经执行结束了我们一起来看一下那我们回到哪里呢回到根目录下面itcast那么可以看到在这个位置是不是有那个wc这样的一个什么呢注意它是一个目录它是一个目录那么我们进入到这个wc那么我们进入到这个wc这个目录来看一下这个下面是不是有一个下滑线success
[07:46] 就意味着这个应用它已经就结束了跑完了然后我们再进入 part000然后它是一个文件我们来看一下 part000然后这个可以看到就是我们的一个结果了hello出现了4次mvc出现了两次word出现了一次那么这个是第一个结果那么第二个结果是1那么这个里面spa一次
[08:14] 这个死不愿的是一次当然了如果我们把这个结果
[08:18] 去做一个这两个文件的这个结果去做一个汇总的话是不是跟我们之前所直接在控制台所打印出来的结果呢是一样的对不对那么只是说在这个位置呢它是通过两个文件去做一个存储原因是我们Spark它本身是一个这个分布式的这样的一个计算那么是不是每一个计算完之后呢都会生成一个这个结果文件最终呢我们需要把它做一个汇总
[08:45] 是的就OK了那我们可以来打开这个success来看一下这个文件那么这个文件中它是其实没有内容的它仅仅用作一个标识就标识着我们这个计算它已经完成了那么我们可以来看一下刷新一下在我们之前的这个完成的应用它的数量是不是三但是现在变成什么变成四了
[09:09] 可以看到它的一个Name就是我们的Application的Name就是什么呢Spark sale这样的一个操作那我们通过它是不是就完成了这做这样的一个这个计算呀对吧OK那么可以来点击进去来看一下这个是它的一些这个Worker这些这个数量啊这么多呢去做一个计算哎呦OK好那么最终的这个结果呢还是比较符合我们预期的是不是啊那么可以在最后的这个位置去做一些这个查看了
[09:38] OK这个大家理解了吗OK好那么现在我们是不是已经就基本掌握了一些Spark sale这样的一个操作对吧它很方便只要输入一些命令就可以执行
[09:51] 就可以看效果那么如果我们对Skala语言比较熟悉的话那么去写一些命令去看效果还是非常方便的所以说在我们开发测试的时候使用Spark sale是非常方便的这样的一个操作OK好那么关于Spark sale的使用的一个讲解我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面 8：在 Spark Shell 中执行完单词计数命令后，输出结果 `res0: Array[(String, Int)] = Array((hello,4), (mvc,1), (world,1), (Spark,1), (spring,1))`。
画面 9：在终端中执行命令 `./Spark-shell --master Spark://node2:7077`，启动远程 Spark Shell。
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
19/08/09 18:26:25 INFO ShutdownHookManager: Deleting directory /tmp/Spark-8a7d217-9448-4b23-a1ef-174c
355f4acc
```

画面 2：
```
[root@itcast bin]# /Spark-shell
19/08/09 18:38:59 WARN NativeCodeLoader: Unable to load native-Hadoop library for your platform... using
builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/Spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://itcast:4040
Spark context available as 'sc' (master = local[*], app id = local-1565347144325).
Spark session available as 'Spark'.
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
[root@itcast bin]# /Spark-shell
19/08/09 18:38:59 WARN NativeCodeLoader: Unable to load native-Hadoop library for your platform... using
builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/Spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://itcast:4040
Spark context available as 'sc' (master = local[*], app id = local-1565347144325).
Spark session available as 'Spark'.
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
res0: Array[(String, Int)] = Array((hello,4), (mvc,1), (world,1), (Spark,1), (spring,1))
```

画面 9：
```
[root@itcast bin]# ./Spark-shell --master Spark://node2:7077
19/08/09 18:43:

