# 4.7 示例操作演示

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day4 Flink基础与流数据处理
- 源文件：06.阶段六 冷链监控平台项目\day4 Flink基础与流数据处理\4.7 示例操作演示_【海量资源尽在 666java.com】.mp4
- 时长 6分34秒（音频 394s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好前面我们给大家演示了我们如何安装和配置我们的Flink的一个程序那么整个Flink的安装呢在包括我们在local的安装和standalone的这么一个安装那么安装完了之后下一步的话我们需要把我们的Flink程序在我们Flink服务器上来运行和执行那么本身Flink
[00:23] 它的安装程序里边已经有了一些example就是示例我们可以看到我们的Flink-1.9.1这里边有一个example的目录而进入到这目录里边它包括我们的P处理或者包括我们的流处理甚至table处理都是有一些这样的应用的我们可以先看一个streaming也就是说是一个流处理的一个目录结构里边那么这里边的话有很多的针对于流适处理的一个例子
[00:51] 比如我们可以看有一个叫socket window word count也就是说这个工程呢其实是要监听某一个端口而这个端口是我们能够用Flink程序实时的监听这个端口能够得到我们在这个端口里边输入的一些单词的数量我们现在就来演示一下这个那提交程序的过程呢有两种方式啊一种方式是我们使用我们的在我们
[01:20] Linux搜索系统里边或者说在我们命令行里边直接使用我们的Flink的一个一个安装一个可执行程序就是这个就是这个Flink的一个程序那么我们在执行的时候我们就能够执行这个程序的时候我们就能提交我们的价包那还有另外一种方式是我们在管理页面里边我们添加我们的价包这两种方式都是可以的那首先我们要演示这个程序的时候我们先要
[01:50] 创建一个socket的一个端口而创建socket的端口的方式很简单就是nc-l然后919010那么此时我们就把我们的端口给它打开了我们可以看一下我们如果是telnet我们这个端口的时候其实是能够telnet成功的对吧此时我们重新打开一下那下一步的话我们把我们的这个工程给它添加进来我们在我们的管理页面上
[02:19] 点击啊也就是说选择一下我们的一个价包这个价包就是socket window word count我们选择选择他选择他的时候他会给我们进行上传上去上传上去之后我们点一下这条记录那么他需要传入一个参数这个参数呢就是泡杠杠泡他刚刚泡他的一个9010那此时我们可以点击一下submitok我们可以看到
[02:50] 我们的当前的在执行的一个running的job有一条记录这条记录就叫socket window word count那么我们点进去可以其实可以看到这个工程或者说这个任务它其实分成四个步骤这四个步骤来讲的话一个步骤的话是说我们要数据源是我们的一个socket那么我们要对它进行一个flat map
[03:18] Flat Map之后我们要根据我们的时间窗口比如说是五秒钟之内我们要计算那么计算完了之后我们要对它进行一个打印当然了现在的这个情况可能看起来有一点点困难因为大家还没有学习这个所谓的这个我们的Flat Map到底是什么意思我们的Windows的五秒钟是什么意思我们的Sync的在这个Sync的这种打印是一个什么意思还不知道那现在不知道没关系我们就是来感受一下此时我们已经把它提交上来了
[03:48] 那提交完了之后呢我们后台的服务器啊这个端口里边我们可以输入啊比如说abcabc或者说是def等等各种各样的一些单词吧def啊这样的一些单词我们回车那我们在我们的这个程序里边呢我们可以点开我们的task manager因为task manager是具体要执行我们任务的一个具体执行我们任务的一个节点在这个节点里边我们看一下ok
[04:18] 那我在这个这个节点呢就是说这个task manager这一个节点因为我们当前有三个嘛我们打开一个的话我们可以看到此时我们的输出的时候是有一个DF是两次然后DFS是一次ABC是两次对吧这和我们刚才看到的是输入的是一样的我们ABC是两次DF是两次DFS是一次这样的话
[04:45] 我们的这个程序其实就是运行正常的运行成功的那么我们再简单的回顾一下我们这个事例我们首先要提交我们的这个jar 包而这个jar 包呢就是我们开发的程序当然了我们现在还不太会开发那我们提交完程序之后呢我们在我们的服务器端这个服务器端是用的是一个NC服务器NC服务器实际上是Linux操作系统里边的有一个命令有一个NC命令这个命令的话
[05:14] 它会打开一个端口它本身是一个socket的一个服务器它的功能非常非常简单我就是输入我在这里边输入一些单词那么我在我的Flink的应用里边我就能够看到我们的这个任务或者看到我们这个Flink计算的一个结果它计算的是过去五秒钟之内的所有的数据的一个值那我还可以再输入一个比如说ttt然后tttgggg
[05:44] 然后回车那么我们在我们的这个task manager里边我们再看一眼它其实是已经是能够实时的给我们显示出来了但是刚才我们看到的是它需要从我们的后台的日志里边读取到我们的页面里边所以说我们在这个地方看到的是稍微有一点点延迟
[06:06] 但是针对于我们整个过程来讲的话它应该是一个实时的我们从后台服务里边它运行的过程其实实时的就能够监测到我们的数据到底有多少OK我们对于我们整个Flink的一个安装部署以及演示就给大家介绍到这儿我们通过我们今天的这个演示呢就能够理解我们Flink程序到底是做什么的它的运行过程是一个什么样的一个

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Flink Web Dashboard 提交并监控一个 Socket Window WordCount 流处理作业。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示 Flink 1.9.1 的安装目录结构，其中包含 bin、conf、examples、lib 等子目录，以及 LICENSE 和 README.txt 文件。
画面 2: Flink Web Dashboard 的概览页面，显示可用任务槽位为 6，正在运行的作业为 0。
画面 3: 在 Linux 终端中，列出 Flink 示例目录下的多个 .jar 文件，如 IncrementalLearning.jar、SessionWindowing.jar 等。
画面 4: 在终端中执行 telnet 命令尝试连接本地端口 9010，最终成功连接。
画面 5: 在 Windows 文件资源管理器中，选择并准备上传一个名为 "SocketWindowWordCount.jar" 的文件。
画面 6: Flink Web Dashboard 的“Running Jobs”页面，显示为空。
画面 7: Flink Web Dashboard 的作业详情页面，显示作业名为 "Socket Window WordCount"，状态为 "RUNNING"，并展示作业的拓扑结构：Socket Stream -> Flat Map -> Window。
画面 8: Flink Web Dashboard 的作业详情页面，显示作业拓扑结构中 Flat Map 操作的并行度为 4。
画面 9: 在终端中执行 nc 命令，准备向端口 9010 发送数据。
画面 10: Flink Web Dashboard 的 Task Managers 页面，显示一个 Task Manager 的内存使用情况，包括 Heap 和 Non-Heap 内存。
画面 11: 在终端中通过 nc 命令向端口 9010 发送数据 "abc abc def"。
画面 12: 在终端中通过 nc 命令向端口 9010 发送数据 "abc abc def dfs def"。
画面 13: Flink Web Dashboard 的“Task Managers”页面。
画面 14: Flink 课程 PPT 页面，标题为“1.6 作业提交”，内容包括如何通过命令行或 Web 页面提交示例应用，并展示了上传的 jar 文件信息和配置。

3) 画面中出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 1:
```
bin
conf
examples
lib
licenses
LICENSE
README.txt
```

画面 3:
```
[root@node2-vm06 streaming]# pwd
/opt/Flink-1.9.1/examples/streaming
[root@node2-vm06 streaming]# ll
total 4092
-rw-r--r-- 1 502 games 12597 Sep 30 14:55 IncrementalLearning.jar
-rw-r--r-- 1 502 games 13692 Sep 30 14:55 Iteration.jar
-rw-r--r-- 1 502 games 8310 Sep 30 14:55 SessionWindowing.jar
-rw-r--r-- 1 502 games 9411 Sep 30 14:55 SocketWindowWordCount.jar
-rw-r--r-- 1 502 games 1137032 Sep 30 14:55 StateMachineExample.jar
-rw-r--r-- 1 502 games 11963 Sep 30 14:55 TopSpeedWindowing.jar
-rw-r--r-- 1 502 games 3546331 Sep 30 14:55 Twitter.jar
-rw-r--r-- 1 502 games 15212 Sep 30 14:55 WindowJoin.jar
-rw-r--r-- 1 502 games 9612 Sep 30 14:55 WordCount.jar
```

画面 4:
```
[root@node2-vm06 ~]# free -m
              total        used        free      shared     buff/cache   available
Mem:           32612       12197       18588          5       12225       19286
Swap:          18127       4466       11661
[root@node2-vm06 ~]# telnet localhost 9010
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
telnet: connect to address

