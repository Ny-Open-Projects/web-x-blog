# 画面线理解：10.体验Spark程序（计算圆周率）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\10.体验Spark程序（计算圆周率）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:18, 01:44, 01:56, 02:06, 02:27, 03:45, 03:52, 03:58, 04:11, 04:23, 04:41, 05:31, 06:07, 06:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:23:43

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark Standalone 模式下运行一个计算 Pi 的示例程序，并对比普通模式与高可用模式提交任务的区别。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Spark 快速入门文档，内容为“4.1.1. 普通模式提交任务”，并显示终端中执行 `./run-example SparkPi 10` 的命令及输出结果。
画面2：显示终端中 `ls` 命令列出的 Spark 相关脚本文件，包括 `run-example.cmd`、`spark-shell.cmd`、`spark-submit.cmd` 等。
画面3：与画面1相同，展示文档内容和终端输出。
画面4：与画面2相同，显示终端中 `ls` 命令列出的脚本文件。
画面5：与画面1相同，展示文档内容和终端输出。
画面6：终端输出显示 Spark 应用程序执行完毕，包括 `SparkUI: Stopped Spark web UI at http://itcast:4040` 和 `SparkContext: Successfully stopped SparkContext`。
画面7：终端中执行 `./run-example --master spark://node1:7077,node2:7077,node3:7077 SparkPi 10` 命令，显示 Spark 版本为 2.4.3。
画面8：终端输出显示 Spark 应用程序执行过程，包括任务启动和完成日志，最终显示 `SparkContext: Successfully stopped SparkContext`。
画面9：与画面8相同，终端输出显示 Spark 应用程序执行过程。
画面10：与画面8相同，终端输出显示 Spark 应用程序执行过程。
画面11：显示 Spark Master Web UI 页面，标题为“Spark Master at spark://itcast:7077”，显示有3个 Alive Workers 和3个已完成的应用程序。
画面12：显示 Spark Master Web UI 中“Application: Spark Pi”页面，列出 Executor Summary 和 Removed Executors 的详细信息。
画面13：展示文档“4.1.2. 高可用模式提交任务”，并显示终端中执行 `./run-example --master spark://node1:7077,node2:7077,node3:7077 SparkPi 10` 命令。
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
docker-image-tool.sh
find-spark-home.cmd
load-spark-env.sh
pyspark
pyspark2.cmd
spark
spark-class.cmd
spark-class2.cmd
spark-shell.cmd
spark-shell2.cmd
sparkR
sparkR2.cmd
sparkR.cmd
spark-sql.cmd
spark-sql2.cmd
spark-submit.cmd
spark-submit2.cmd
run-example.cmd
```
画面7：
```bash
./run-example --master spark://node1:7077,node2:7077,node3:7077 SparkPi 10
```
画面13：
```bash
./run-example --master spark://node1:7077,node2:7077,node3:7077 SparkPi 10
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
