# 7.4 Druid管理程序介绍

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.4 Druid管理程序介绍_【海量资源尽在 666java.com】.mp4
- 时长 4分35秒（音频 275s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来看一看我们Apache Droid它的一个web的一个管理端那么它的端口是四个八我们打开之后我们看到首页里边有一些当前的Apache Droid它的一个版本号我们在这Citizen能看到当前这个0.15.0这个版本的Apache Droid它是在一个running的一个状态那么DataSource呢
[00:25] 是指的我们当前数据库里边就是这个J的数据库里边有哪一个表目前的话是一个DataSource也就是说一个表那Segment是指我们的数据的分区分成几个区分成多少个分区那Supervisor它这个稍微有点意思Supervisor我们可以把它理解成一个叫做公投那么这个公投呢它管理的是各种各样的一个任务
[00:52] 也就是说我这个supervisor它会把task给启动起来那么task的这个页面里边或者是task这个区域里边我们能看到当前有一个是在启动或者是运行中的一个task那么有44个实际上是一个成功的一个task有98个是失败的一个task
[01:13] 那么我们data server的话其实也可以看到现在有一个是middle manager然后有0个是historical的一个这种节点那第二部分来讲的话是我们的这个load data那load data的话就是加载数据嘛那加载数据可以批量的加载数据也可以通过其他的这个数据数据流的方式来加载那么批量数据
[01:38] 加载的话我们可以批量的加载我们的http的一个呃接口也可以批量的加载我们的aws的数据还可以加载我们的啊谷歌的谷歌的云服务的甚至于我们本地的一个文件的一些加载那呃这种这个叫什么呢这个流工作流数据流的一个呃加载啊是实际上是在我们呃下边这一块能够
[02:07] 加载数据流那DataSourceDataSource这个菜单里边我们可以看到DataSource菜单里边有一个all deviceall下滑线device message这样的一个表这个表里边来讲的话它的加载的一些叫做规则把什么时间的加载什么时间的一个删除当然这个删除的话只是说我不在我们当前的这个Mail Manager这个节点上的我们可以把它放到别的节点上的
[02:35] 历史节点上的那Segment的话就是我们的这个分区了这分区的话我们从这里边可以看到我们这个分区的每个分区的版本是什么样它分区的大小有多少条数据等等这样的一些信息任务的话就是我们在这里边可以添加我们的Supervisor我们可以添加一个工头这个工头会启动相应的一些执行任务这是我们的这个Task
[03:01] Data Server的话在这里面其实就可以看到我们历史接点是什么然后我们的历史接点和我们的Main Manager这样的一个接点状态当然它的端口我们其实也可以看到对吧这个是8083这个端口Query的话实际上是我们从这里面能够查询我们的数据库和我们使用My Circle来查询是一样的Select From我们的就比如说
[03:32] Device MessageLimit是此时我们就能把数据给查询查询出来了和我们在Masako客户端里面查询是一样的那么简单的来讲的话我们这个管理端它能够提供的服务一个是能够查看我们当前节点服务的节点的各个节点的一些状态信息第二来讲的话我们能够加载本地的数据第三来讲的话我们在通过Task的时候能够加载我们的
[04:04] 就是就叫实时的一些数据流啊我们通过创建一个supervisor能够监听我们的这种啊呃Kafka对列啊监听Kafka对列把Kafka对列的数据呃存储到我们的Jade里面去同时我们还可以使用我们的这种叫query就是使用我们的circuit去来加载来查询我们的Jade里面的数据啊这是我们的呃Jade他的这种web的一个客户端web的一个服务服务器
[04:32] 管理的一個頁面

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Apache Druid 的统一控制台界面，包括数据源管理、数据段查看、任务监控、中间管理器状态和 SQL 查询功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Druid 控制台的“Load data”页面，提示用户指定原始数据位置，提供 HTTP(s)、AWS S3、Google Cloud Storage、Local disk 等选项。
画面 2: 切换到“DataSources”页面，显示一个名为 “all_device_message” 的数据源，状态为“Fully available”，保留策略为 “loadby(period)(P100), dropby(period)(P300)”，压缩策略为“None”，大小 36.37 MB，行数 444,097。
画面 3: 切换到“Segments”页面，显示空的段列表。
画面 4: 在“Segments”页面中，显示了多个数据段，数据源均为 “all_device_message”，时间范围从 2019-12-05T00:00:00.000Z 到 2019-12-04T16:00:00.000Z，版本从 1 到 11，行数从 161 到 336。
画面 5: 切换到“Tasks”页面，显示空的任务列表。
画面 6: 切换到“Data servers”页面，显示“Supervisors”部分，主机为 “172.17.0.143:8091”，使用率为 1/3，上次完成任务时间为 2019-12-05T04:11:39.629Z。
画面 7: 在“Data servers”页面中，显示了另一个主机 “172.17.0.143:8093”，数据源为 “default_liter”，大小 36.37 MB，容量 300.00 GB，使用率 0.0%，队列为空。
画面 8: 在“Data servers”页面中，显示了主机 “172.17.0.143:8093” 的详细信息，数据源为 “default_liter”，大小 36.37 MB，容量 300.00 GB，使用率 0.0%，队列为空。
画面 9: 切换到“Query”页面，SQL 编辑器为空。
画面 10: 在“Query”页面中，输入 SQL 语句：`select * from all_device_message`。
画面 11: 在“Query”页面中，SQL 语句为：`select * from all_device_message limit 30`。
画面 12: 执行 SQL 查询后，显示查询结果，包含字段如 `line`, `companyname`, `curtime`, `hotcode`, `hostid`, `hostname`, `housecode`, `houseid`, `hum`, `humslat`, `lat`, `lon` 等，数据行数为 10。
画面 13: 切换回“Load data”页面，提示用户指定原始数据位置。
画面 14: 切换回“Query”页面，SQL 编辑器为空。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 10: `select * from all_device_message`
画面 11: `select * from all_device_message limit 30`
画面 12: 查询结果中的字段包括：
```
line
companyname
curtime
hotcode
hostid
hostname
housecode
houseid
hum
humslat
lat
lon
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

