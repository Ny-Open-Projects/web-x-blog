# 7.18 项目实战 - 数据流程和开发流程

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.18 项目实战 - 数据流程和开发流程_【海量资源尽在 666java.com】.mp4
- 时长 3分11秒（音频 192s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来看一看Apache最的在我们冷链设备监控平台中的实战那么首先呢我们来看一看数据的流程我们看一下这一张流程图设备比如说我们的温度采集器或者湿度采集器它提交
[00:19] 报文数据给我们的NetEase服务器而它提交的报文呢是一种这个非常简单的这种格式它以竖杠来分割各个数据的字段那么NetEase接收到这些数据之后呢会把它转化成一个JSON格式这种JSON格式会推送到我们Kafka堆裂里边去而此时Flink呢在监听Kafka堆裂它发现这个数据之后它会结合我们在Redis里边存储
[00:48] 的温湿度的预值数据进行实时的计算计算的结果就是我们下边这个比较长的这个阶层格式的数据这个数据会一方面会存储到我们的马赛克数据库里边另一方面会推送到Kafka队列里边而此时我们的阿帕奇坠的就是监听我们的Kafka队列得到这个数据把数据存储到坠者中那么
[01:14] 在这个过程中如何保障或者如何让我们的Droid来监听卡布卡队列这就需要有一个开发流程而这个流程的话我们需要两部分一部分是我们需要修改我们的配置修改我们的配置的时候添加我们的叫Droid卡布卡Indexing Service那么这个配置文件呢在我们Droid安装目录的Config目录下那么
[01:42] 无论有可能是我们当前是一个single server那是就是就是在single server这个目录下如果是当前是cluster server就是在cluster server目录下那么接着就是我们的这个是集群的大小是small还是说是Xlarge的下面这个目录下面的有一个common目录这common目录下有一个common.run time.property文件这是我们的droid的配置文件
[02:12] 我们打开这个配置文件在这里的有一个dread extension叫loadlist在这个属性里边我们添加dread-kavka-indexing-Service添加完这个之后呢我们就可以就是重启我们的服务此时我们的这个就能够提供了这种
[02:47] 所引服务了那第二步的话是我们需要提交一个supervisor的任务这是我们整个开发的一个流程经过这种开发流程之后呢我们的队的就能够监听卡普卡队列实时的把数据存储到队的里边去至于后边如何来提交我们的supervisor任务我们在后边给大家介绍

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过修改Druid配置文件来添加Kafka索引服务，实现从设备数据到Druid的实时数据处理流程。

2) 按时间顺序列出每张画面的要点：
画面1：展示Druid数据流架构图，包含设备→Netty→Kafka→Flink→MySQL→Kafka→Druid，以及两个数据示例（JSON格式）。
画面2：在架构图下方新增“开发流程”部分，第一点为“修改配置，添加druid-Kafka-indexing-Service”，并给出配置文件路径。
画面3：继续展示开发流程，配置文件路径和druid_extensions.loadList配置项。
画面4：展示开发流程的第二点“提交supervisor任务”，并列出“2.1.2 数据结构”表格的列名：名称、类型、长度、是否默认值、备注。
画面5：继续展示开发流程的第二点“提交supervisor任务”，并列出“2.1.2 数据结构”表格的列名：名称、类型、长度、是否默认值、备注。
画面6：切换到终端界面，显示当前目录为/opt/druid/conf/druid/single-server/small/_common/，准备编辑配置文件。
画面7：在终端中使用vim打开配置文件，显示文件头部的Apache License 2.0声明和druid_extensions.loadList配置项。
画面8：在终端中使用vim打开配置文件，显示文件头部的Apache License 2.0声明和druid_extensions.loadList配置项。
画面9：在终端中使用vim打开配置文件，显示文件头部的Apache License 2.0声明和druid_extensions.loadList配置项。
画面10：在终端中使用vim打开配置文件，显示文件头部的Apache License 2.0声明和druid_extensions.loadList配置项。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1：
```json
{
  "timestamp": "20181117172120",
  "value": "10",
  "timestamp": "20181117172120",
  "value": "10"
}
```
画面2：
```properties
配置文件:/opt/druid/conf/druid/single-server/small/common/common.runtime.properties
druid_extensions.loadList=["druid-hdfs-storage", "druid-Kafka-indexing-Service", "druid-datasinkes", "mysql-metadata-storage"]
```
画面3：
```properties
druid_extensions.loadList=["druid-hdfs-storage", "druid-Kafka-indexing-Service", "druid-datasinkes", "mysql-metadata-storage"]
```
画面4：
```properties
druid_extensions.loadList=["druid-hdfs-storage", "druid-Kafka-indexing-Service", "druid-datasinkes", "mysql-metadata-storage"]
```
画面5：
```properties
druid_extensions.loadList=["druid-hdfs-storage", "druid-Kafka-indexing-Service", "druid-datasinkes", "mysql-metadata-storage"]
```
画面6：
```bash
[root@node2-vm06 _common]#
```
画面7：
```properties
# Extensions Specified in the Load list will be loaded by Druid
# We are using local fs for deep storage - not recommended for production - use S3, HDFS, or NFS instead
# We are using local derby for the metadata store - not recommended for production - use MySQL or Postgres instead
# If you specify 'druid.extensions.loadList=[]', Druid won't load any extension from file system.
# If you don't specify 'druid.extensions.loadList', Druid will load all the extensions under root extension directory.
# More info: http://druid.io/docs/latest/operations/including-extensions.html
druid_extensions.loadList=["druid-hdfs-storage", "druid-Kafka-indexing-Service", "druid-datasinkes", "mysql-metadata-storage"]
```
画面8：
```properties
# Extensions Specified in the Load list will be loaded by Druid
# We are using local fs for deep storage - not recommended for production - use S3, HDFS, or NFS instead
# We are using local derby for the metadata store - not recommended for production - use MySQL or Postgres instead
# If you specify 'druid.extensions.loadList=[]', Druid won't load any extension from file system.
# If you don't specify 'druid.extensions.loadList', Druid will load all the extensions under root extension directory.
# More info: http://druid.io/docs/latest/operations/including-extensions.html
druid_extensions.loadList=["druid-hdfs-storage", "druid-Kafka-indexing-Service", "druid-datasinkes", "mysql-metadata-storage"]
```
画面9：
```properties
# Extensions Specified in the Load list will be loaded by Druid
# We are using local fs for deep storage - not recommended for production - use S3, HDFS, or NFS instead
# We are using local derby for the metadata store - not recommended for production - use MySQL or Postgres instead
# If you specify 'druid.extensions.loadList=[]', Druid won't load any extension from file system.
# If you don't specify 'druid.extensions.loadList', Druid will load all the extensions under root extension directory.
# More info: http://druid.io/docs/latest/operations/including-extensions.html
druid_extensions.loadList=["druid-hdfs-storage", "druid-Kafka-indexing-Service", "druid-datasinkes", "mysql-metadata-storage"]
```
画面10：
```bash
[root@node2-vm06 _common]# vim /opt/druid/conf/druid/single-server/small/_common/common.runtime.properties
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：标题“2.1 数据存储”、“2.1.1 数据流程”；架构图：设备 → Netty → Kafka → Flink → MySQL → Kafka → Druid；Flink指向MySQL的箭头标注“温冷层调度数据”；Kafka指向Druid的箭头标注“温冷层调度数据”。
画面2：标题“2.1.1 数据流程”；架构图：设备 → Netty → Kafka → Flink → MySQL → Kafka → Druid；Flink指向MySQL的箭头标注“温冷层调度数据”；Kafka指向Druid的箭头标注“温冷层调度数据”。
画面3：标题“2.1.1 数据流程”；架构图：设备 → Netty → Kafka → Flink → MySQL → Kafka → Druid；Flink指向MySQL的箭头标注“温冷层调度数据”；Kafka指向Druid的箭头标注“温冷层调度数据”。
画面4：标题“开发流程”；内容：1. 修改配置，添加druid-Kafka-indexing-Service；2. 提交supervisor任务；表格：2.1.2 数据结构，列名：名称、类型、长度、是否默认值、备注。
画面5：标题“开发流程”；内容：1. 修改配置，添加druid-Kafka-indexing-Service；2. 提交supervisor任务；表格：2.1.2 数据结构，列名：名称、类型、长度、是否默认值、备注。
画面6：无PPT标题或架构图。
画面7：无PPT标题或架构图。
画面8：无PPT标题或架构图。
画面9：无PPT标题或架构图。
画面10：无PPT标题或架构图。

5) 不要评价画面美观，不要输出与课程无关的内容。

