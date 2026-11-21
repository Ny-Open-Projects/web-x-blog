# 持续追加的日志文件怎么采：exec source 加 tail -F 的思路，以及断点续传的缺口

目录采集解决的是「目录里不断冒出新文件」的场景，还有一类更常见的：业务系统用 log4j 这类日志组件生成日志文件，同一个文件被进程持续追加，内容随时间不断增长，需求是把文件里新增的数据实时采进 HDFS。这种文件没有「采完改名」的那一刻，spooldir 方案对它无从下手，source 必须换一种盯法。

## 先给结论

- 单文件持续追加的采集用 exec source：`type = exec`，`command` 写 `tail -F /export/servers/taillogs/access_log`。
- exec 的机制是「agent 启动时执行一次命令，把命令的标准输出逐行读成 event」，tail -F 守着文件吐新增行，source 就间接盯住了文件变化。
- sink 沿用 hdfs sink 的既有套路，channel 可用 file channel 也可用内存 channel，课程示例选内存并把 capacity 提到 50 万。
- exec 不记录读取位置，agent 重启后 tail -F 从文件末尾重新开始，停机期间追加的数据不会补采，断点续传是这套方案的天然缺口。
- 与 spooldir 的分工按文件形态定：整文件一次性进目录用 spooldir，单文件持续追加用 exec，两者对「文件能否被修改」的约束正好相反。

## 三大要素：换一头，稳一头

按 Flume 采集的三步走：写配置文件、启动 agent 实例、运行测试。写配置前先定三大要素：

```text
采集源，即 Source：监控文件内容更新，exec tail -F file
下沉目标，即 Sink：HDFS 文件系统，hdfs sink
Source 与 Sink 之间的通道，即 Channel：可用 file channel，也可用内存 channel
```

sink 与目录案例完全复用，仍是 hdfs sink；channel 二选一，课程示例用内存。真正要重新设计的是 source：数据从哪里来，怎么知道一个文件发生了变化。

## 为什么不能用 spooldir

spooldir 有两个隐含前提，在日志场景里全被打破。它盯的是目录里的新文件，靠出现与改名来管理采集状态，而日志自始至终是同一个文件，只是内容在长；它假定文件放入后不再修改，而日志文件每一秒都在追加。把一个正在被业务进程写入的文件放进监控目录，等于直接踩上一章总结过的报错现场。

换一个思路：操作系统里本来就有一个守着文件变化的命令。`tail -F 文件名` 会输出文件新增的内容，进程不退出，一直跟着文件走。如果 source 盯住这条命令的输出，就间接盯住了文件的变化。

**exec source 就是这座桥。**Flume 官网的 source 列表里，exec 类型的定义是执行一个 Unix 命令并读取其标准输出。把 command 配成 `tail -F /export/servers/taillogs/access_log`，命令每吐一行，Flume 就多一个 event，文件的新增内容顺着命令输出流进采集链路。

```mermaid
flowchart LR
    L["access_log<br>业务进程持续追加"] -->|"tail -F 输出新增行"| E["exec source<br>读命令标准输出"]
    E -->|"一行一个 event"| C["memory channel<br>capacity 500000"]
    C --> K["hdfs sink"]
    K --> H["HDFS<br>按时间转义分桶目录"]
```

这张图在讲文件采集的数据通路：日志文件的追加内容经 tail -F 变成命令输出，exec source 把输出读成 event。关键路径一句话：与 spooldir 案例相比，变化只在 source，数据的入口从「目录里出现新文件」变成了「一条盯文件的命令的输出」。

## tail -F 与 tail -f 差一个字母，差一种健壮性

`tail -f` 跟踪的是文件描述符，日志按天切割改名后，旧描述符还挂在老文件上，新写入的内容再也读不到。`tail -F` 会重试打开同名文件，跟着改名后重建的新文件继续走。生产日志几乎都会切割轮转，采集命令必须写大写 F。

## 配置骨架：source 与 channel 两段

配置文件名与讲义保持一致，叫 `tail-file.conf`：

```bash
cd /export/servers/apache-flume-1.8.0-bin/conf
vim tail-file.conf
```

命名段照旧是 `agent1.sources = source1`、`agent1.sinks = sink1`、`agent1.channels = channel1`，本案例的 agent 名换成 `agent1`。source 段：

```properties
# 描述和配置 tail -F source1
agent1.sources.source1.type = exec
agent1.sources.source1.command = tail -F /export/servers/taillogs/access_log
agent1.sources.source1.channels = channel1
```

type 写 exec，command 写要执行的命令，这里也可以把 source 认 channel 的那行留到最后连线段统一写，两种写法等价。

channel 段：

```properties
# memory channel
agent1.channels.channel1.type = memory
agent1.channels.channel1.keep-alive = 120
agent1.channels.channel1.capacity = 500000
agent1.channels.channel1.transactionCapacity = 600
```

`keep-alive = 120` 是一个等待时限，单位秒：channel 数据存满时，sink 来取数据最多等 120 秒；channel 空了，source 想放数据也最多等 120 秒，超时报错。不设也有默认值。`capacity = 500000` 把总容量提到 50 万个 event，比目录案例的 1000 大得多，日志流量是持续的，缓冲留足；`transactionCapacity = 600` 是发送队列大小，依旧满足队列小于仓库的关系。

sink 段沿用 spooldir 案例的 hdfs 配置套路，`hdfs.path` 换成本案例的目标目录 `hdfs://node01:8020/weblog/flume-collection/%y-%m-%d/%H-%M`，时间转义与滚动参数的逐项解释在这里不再重复，完整清单留到运行测试篇。

## 断点续传的缺口

exec 的命令只在 agent 启动那一刻执行一次，之后 Flume 做的只是消费这条命令进程的标准输出。agent 重启，旧命令进程已经死了，新命令进程重新拉起，tail -F 从当前文件末尾继续输出。两个后果随之而来：

- 停机期间追加进文件的数据不会补采，重启后直接从新位置开始读，中间那段数据丢了。
- tail 默认启动时先输出文件末尾 10 行再进入跟随模式，边界处还可能出现重复数据。

位置信息只存在于内存里，没有落盘。Flume 1.7 之后内置的 taildir source 把每个文件的读取位置写进磁盘上的 position 文件，重启后接着读，才是断点续传的完整答案；课程环境是 Flume 1.8.0，具备使用条件，把它记作 exec 的升级方向即可。这一段属于方案演进，视频里没有展开，实测篇会用实验把 exec 的丢失行为做实。

## 与 spooldir 的适用差异

两个案例摆在一起，选型规则收敛成一张对照：

```text
数据形态：spooldir 盯目录里的新文件，exec 盯单个文件的追加内容
完成标记：spooldir 采完改名 .COMPLETED，exec 无标记，一直守着文件
文件约束：spooldir 要求文件放入后不可改，exec 采集的文件恰恰要求可持续追加
重启表现：spooldir 靠改名天然防重，exec 位置不落盘，重启有丢失与重复风险
```

一句话记法：文件会一直变，选 exec；文件一批一批来，选 spooldir。

## 常见误区

- **采集命令写成小写 `tail -f`。**日志切割改名后 -f 跟丢文件，数据静默断流；必须用 `-F` 让 tail 跟住同名的新文件。
- **以为 exec 能断点续传。**读取位置不落盘，agent 重启即从文件末尾重来，停机窗口的数据补不回来；要续传换 taildir source。
- **把正在追加的日志文件放进 spooldir 监控目录。**违背「放入后不可改」的前提，会触发报错停摆；追加型文件只能走 exec 或 taildir。
- **把 keep-alive 当成网络连接超时。**它是 channel 满或空时组件等待的时限，与网络无关，调大它解决不了 sink 慢的问题。

## 面试可能被问到的问题

1. 面试官追问：「exec source 是怎么工作的？」
   答：agent 启动时执行 command 配置里的命令一次，把命令进程的标准输出逐行读成 event 推进 channel。配 tail -F 命令后，文件新增内容经命令输出进入采集链路，命令进程活着就一直采集。
2. 面试官追问：「tail -F 和 tail -f 有什么区别？」
   答：-f 跟踪文件描述符，文件被切割改名后就跟丢；-F 会重试打开同名文件，跟住改名后重建的新文件。生产日志都会轮转，采集必须用 -F。
3. 面试官追问：「为什么日志文件采集不用 spooldir？」
   答：spooldir 面向目录里的新文件且要求文件放入后不可修改，而业务日志是同一个文件持续追加，两个前提都不成立。追加型文件用 exec 或 taildir 盯文件内容变化。
4. 面试官追问：「exec 重启为什么会丢数据？怎么解决？」
   答：exec 不记录读取位置，重启后重新执行 tail -F，从文件末尾继续，停机期间追加的数据不会补采，边界处还可能重复末尾 10 行。解决方向是换 taildir source，它把每个文件的位置写入磁盘 position 文件，重启接着读。
5. 面试官追问：「memory channel 的 keep-alive 参数是什么意思？」
   答：channel 状态异常时组件等待的时限，channel 满时 sink 取数据、channel 空时 source 放数据，各最多等 keep-alive 秒，超时报错；有默认值，一般不显式设置。

## 配套资料

- 代码：`materials/code/04/day06-Flume/`，本课资料包未附带 tail 案例的配置文件，`tail-file.conf` 按视频画面逐行还原（agent 名 source1、sink1、channel1，路径与容量参数均为画面原值），示例为按本课写法补全。
- 讲义：`materials/docs/04/采集系统部署使用说明.md`，课程采集系统的部署与业务背景，业务系统持续产生用户行为日志、再由采集链路送往后端，正对应「日志文件持续追加、需要实时采集」的需求。
- 代码：`materials/code/04/buried/`，课程用户行为日志采集工程的源码，业务侧通过日志组件产生采集日志的实现可对照查阅。
