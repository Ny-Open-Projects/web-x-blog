# 10.体验Spark程序（计算圆周率）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\10.体验Spark程序（计算圆周率）_【海量资源尽在 666java.com】.mp4
- 时长 6分11秒（音频 371s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来体验一下Spark的程序啊那么前面呢我们只是呢把Spark的集群呢跑起来了那么下面我们就来体验一下如何在Spark集群中去运行我们的一些应用那么首先我们来看我们的第一个这个程序那么第一个程序的提示是我们不需要去编写任何的代码
[00:23] 那么在Spark它内置了一些这种example就是一些事例帮我们去做一些这种体验了那么我们首先来看一下在普通模式下面的一个任务的提交那么也就是说通过我们单机这样的一个计算并不会真正的去提交到我们的集群那么在我们演示完成之后我们再给大家去讲一下如何去提交到这个集群OK
[00:49] 好 那么在这儿我们将去运行一个例子就是去利用一个叫做门特卡罗的一个算法来计算圆周率π那么我们知道这个圆周率它是等于3.1415等等等等一直往后 这样的一个圆周率那么它将通过这种计算机模拟大量的随机数最终去计算出相对比较准确的一个π的一个值
[01:17] 那么怎么样去使用呢其实是在我们的B目录下面呢有这样的一个脚本那么就是去run一个example然后呢我们去调用这个传入参数啊叫做Spark pi然后呢传入这个1010呢代表是说计算10次去做这样的一个计算得到一个相对准确的一个值然后呢我们来看一下这个操作那我们进入到B目录B目录下面呢会有一些这个脚本
[01:47] 其中有一个叫做 wrong example 再造然后我们把这个就拷贝过来那么其实我们不用去关心这个门特卡罗这个算法究竟是怎么样实现但是我们先可以来体验一下用 Spark 怎么样能够把这个 pi 这个值去计算出来然后走我们来等待它的一个执行
[02:09] 好那么现在呢我们其实就可以看到它已经呢就执行结束了啊那我们来看一下最终的一个结果呢其实是在这里啊它说派的这个值呢是3.140099啊那么是一个是不是相对比较准确的一个值啊是不是3.14啊比较准确的一个值那么这种模式呢是一个呃这个呃就是单节点或者说是一种普通啊模式的这样的一个提交那么接下来呢我们来看一下高可用模式的一个提交
[02:37] 那么在高可用下面的因为我们设计的会有多个这个master那么这个master有可能是会发生变化的比如说我们这个node1等于当机了会选择node2等等那么我们怎么样去解决这个问题呢其实也是比较简单的那我们只需要呢去给我们的这个run example来指定一个master这个列表就可以了那么你可以指定一个也可以指定多个那么我建议呢大家指定多个因为呢
[03:05] 这个SPAG会做一个这个轮旋比如说你第一个这个节点它检测到已经连接不到了它会自动会连接到第二个然后会再继续连接到第三个那么这一块我们写的会有点问题这个应该是3这样的一个节点那么要注意的是我们看一下它的结构是去通过这个run example然后杠杠master然后去通过一个SPAG冒号双斜杠然后在这个位置来指定三个服务节点
[03:35] node17077node27077node3和7077同样的去计算我们这个派的值好那么我们可以来做一个执行去做一个提交那么这个时候他就会把这个应用的去通过我们集群的去做一个计算了然后走好那么等待他的一个执行那么最终这个结果就计算出来了那么其实可以看到在前面这个过程大致可以去浏览一下那么他是不是就会通过什么
[04:05] 通过我们的这个具体的这种服务啊具体这种服务呢去等待他计算的一个完成那完成之后他会对这个结果去做一些这个汇总啊最终去得到我们的一个结果呢就是这样的一个结果啊就是3.143395啊等等等等
[04:22] 那么这个是不是我们通过这个SPAG集群就完成了一个计算可以看到这个结果跟我们前面结果呢是差不多的虽然说后面这个值呢是不一样但是3.14这个位置它是一样的好那么接下来呢我们可以来看一下在我们的集群中的这个情况那么其实可以看到呢在这个位置啊我们已经运行了有三次了但也能说我们不是
[04:49] 只运行了一次吗怎么会有三次呢因为在前面呢我也做了一次测试啊那么可以看到呢这个就是我们所完成的啊这样的一个啊这样的一个应用啊那么当然了我们可以点击进去来看一下那么它每个所运行的这个结果啊所运行的结果这个可以看到它这个呢是所执行器的一些这种汇总的一些这个信息啊
[05:15] 然后呢有它的Worker呢参与Worker参与这个Worker的计算呢会有这么多啊会这么多它的一些这个Core就是我们这个CPU的核数还有我们的内存数啊等等还有它的一些状态啊都有了一些这样的一些这个计算然后呢上面呢有这个当前这个Application应用的一个这个状态啊下面呢是这个Remote啊就是已经移除的一些执行器了以及它的状态呢是Queue的啊
[05:44] OK好那么可以看到相对比较详细的一些信息了那么现在呢其实我们是不是就有了一个大致的一个这个认知那就是那么我们可以通过这个Spark集群呢就可以来运行一些应用比如说我们给大家所运行的这个我们计算这个圆周率啊这样的应用了对吧OK好那么关于我们的第一个这个体验呢那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark Standalone 模式下运行一个计算 Pi 的示例程序，并对比普通模式与高可用模式提交任务的区别。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Spark 快速入门文档，内容为“4.1.1. 普通模式提交任务”，并显示终端中执行 `./run-example SparkPi 10` 的命令及输出结果。
画面2：显示终端中 `ls` 命令列出的 Spark 相关脚本文件，包括 `run-example.cmd`、`Spark-shell.cmd`、`Spark-submit.cmd` 等。
画面3：与画面1相同，展示文档内容和终端输出。
画面4：与画面2相同，显示终端中 `ls` 命令列出的脚本文件。
画面5：与画面1相同，展示文档内容和终端输出。
画面6：终端输出显示 Spark 应用程序执行完毕，包括 `SparkUI: Stopped Spark web UI at http://itcast:4040` 和 `SparkContext: Successfully stopped SparkContext`。
画面7：终端中执行 `./run-example --master Spark://node1:7077,node2:7077,node3:7077 SparkPi 10` 命令，显示 Spark 版本为 2.4.3。
画面8：终端输出显示 Spark 应用程序执行过程，包括任务启动和完成日志，最终显示 `SparkContext: Successfully stopped SparkContext`。
画面9：与画面8相同，终端输出显示 Spark 应用程序执行过程。
画面10：与画面8相同，终端输出显示 Spark 应用程序执行过程。
画面11：显示 Spark Master Web UI 页面，标题为“Spark Master at Spark://itcast:7077”，显示有3个 Alive Workers 和3个已完成的应用程序。
画面12：显示 Spark Master Web UI 中“Application: Spark Pi”页面，列出 Executor Summary 和 Removed Executors 的详细信息。
画面13：展示文档“4.1.2. 高可用模式提交任务”，并显示终端中执行 `./run-example --master Spark://node1:7077,node2:7077,node3:7077 SparkPi 10` 命令。
画面14：与画面13相同，展示文档内容和终端命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```bash
#进入bin目录
./run-example SparkPi 10
```
画面2：
```bash
[root@itcast bin]# ls
beeline
beeline
beeline
Docker-image-tool.sh
find-Spark-home.cmd
load-Spark-env.sh
pyspark
pyspark2.cmd
Spark
Spark-class.cmd
Spark-class2.cmd
Spark-shell.cmd
Spark-shell2.cmd
sparkR
sparkR2.cmd
sparkR.cmd
Spark-sql.cmd
Spark-sql2.cmd
Spark-submit.cmd
Spark-submit2.cmd
run-example.cmd
```
画面7：
```bash
./run-example --master Spark://node1:7077,node2:7077,node3:7077 SparkPi 10
```
画面13：
```bash
./run-example --master Spark://node1:7077,node2:7077,node3:7077 SparkPi 10
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面11：表格数据：
- Workers 表格：
  - Worker Id: worker-20190809173847-192.168.31.82-35418
  - Address: 192.168.31.82:35418
  - State: ALIVE
  - Cores: 2 (0 Used)
  - Memory: 2.7 GB (0 B Used)
  - Worker Id: worker-20190809173901-192.168.31.83.35029
  - Address: 192.168.31.83.35029
  - State: ALIVE
  - Cores: 2 (0 Used)
  - Memory: 2.7 GB (0 B Used)
  - Worker Id: worker-20190809173902-192.168.31.84.41043
  - Address: 192.168.31.84.41043
  - State: ALIVE
  - Cores: 2 (0 Used)
  - Memory: 2.7 GB (0 B Used)
- Running Applications 表格：
  - Application ID: (空)
  - Name: (空)
  - Cores: (空)
  - Memory per Executor: (空)
  - Submitted Time: (空)
  - User: (空)
  - State: (空)
  - Duration: (空)
- Completed Applications 表格：
  - Application ID: app-20190809182622-004
  - Name: Spark Pi
  - Cores: 6
  - Memory per Executor: 1024.0 MB
  - Submitted Time: 2019/08/09 18:26:22
  - User: root
  - State: FINISHED
  - Duration: 3 s
  - Application ID: app-20190809181655-000
  - Name: Spark Pi
  - Cores: 6
  - Memory per Executor: 1024.0 MB
  - Submitted Time: 2019/08/09 18:16:55
  - User: root
  - State: FINISHED
  - Duration: 0 s

画面12：表格数据：
- Executor Summary 表格：
  - ExecutorID: 3
  - Worker: worker-20190809173901-192.168.31.83.35029
  - Cores: 2
  - Memory: 1024
  - State: EXITED
  - Logs: stout slr
  - ExecutorID: 4
  - Worker: worker-20190809173902-192.168.31.84.41043
  - Cores: 2
  - Memory: 1024
  - State: EXITED
  - Logs: stout slr
  - ExecutorID: 0
  - Worker: worker-20190809173901-192.168.31.83.35029
  - Cores: 2
  - Memory: 1024
  - State: EXITED
  - Logs: stout slr
- Removed Executors 表格：
  - ExecutorID: 2
  - Worker: worker-20190809173847-192.168.31.82-35418
  - Cores: 2
  - Memory: 1024
  - State: KILLED
  - Logs: stout slr
  - ExecutorID: 6
  - Worker: worker-20190809173902-192.168.31.84.41043
  - Cores: 2
  - Memory: 1024
  - State: KILLED
  - Logs: stout slr
  - ExecutorID: 5
  - Worker: worker-20190809173901-192.168.31.83.35029
  - Cores: 2
  - Memory: 1024
  - State: KILLED
  - Logs: stout slr

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

