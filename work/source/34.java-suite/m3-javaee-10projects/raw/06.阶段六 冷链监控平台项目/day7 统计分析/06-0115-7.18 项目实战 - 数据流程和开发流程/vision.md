# 画面线理解：7.18 项目实战 - 数据流程和开发流程

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.18 项目实战 - 数据流程和开发流程_【海量资源尽在 666java.com】.mp4
- 抽帧：10 帧 @ 00:11, 01:16, 01:21, 01:23, 01:24, 02:15, 02:18, 02:21, 02:35, 02:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:49:26

1) 这一组画面整体在讲如何通过修改Druid配置文件来添加Kafka索引服务，实现从设备数据到Druid的实时数据处理流程。

2) 按时间顺序列出每张画面的要点：
画面1：展示Druid数据流架构图，包含设备→Netty→Kafka→Flink→MySQL→Kafka→Druid，以及两个数据示例（JSON格式）。
画面2：在架构图下方新增“开发流程”部分，第一点为“修改配置，添加druid-kafka-indexing-service”，并给出配置文件路径。
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
druid_extensions.loadList=["druid-hdfs-storage", "druid-kafka-indexing-service", "druid-datasinkes", "mysql-metadata-storage"]
```
画面3：
```properties
druid_extensions.loadList=["druid-hdfs-storage", "druid-kafka-indexing-service", "druid-datasinkes", "mysql-metadata-storage"]
```
画面4：
```properties
druid_extensions.loadList=["druid-hdfs-storage", "druid-kafka-indexing-service", "druid-datasinkes", "mysql-metadata-storage"]
```
画面5：
```properties
druid_extensions.loadList=["druid-hdfs-storage", "druid-kafka-indexing-service", "druid-datasinkes", "mysql-metadata-storage"]
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
druid_extensions.loadList=["druid-hdfs-storage", "druid-kafka-indexing-service", "druid-datasinkes", "mysql-metadata-storage"]
```
画面8：
```properties
# Extensions Specified in the Load list will be loaded by Druid
# We are using local fs for deep storage - not recommended for production - use S3, HDFS, or NFS instead
# We are using local derby for the metadata store - not recommended for production - use MySQL or Postgres instead
# If you specify 'druid.extensions.loadList=[]', Druid won't load any extension from file system.
# If you don't specify 'druid.extensions.loadList', Druid will load all the extensions under root extension directory.
# More info: http://druid.io/docs/latest/operations/including-extensions.html
druid_extensions.loadList=["druid-hdfs-storage", "druid-kafka-indexing-service", "druid-datasinkes", "mysql-metadata-storage"]
```
画面9：
```properties
# Extensions Specified in the Load list will be loaded by Druid
# We are using local fs for deep storage - not recommended for production - use S3, HDFS, or NFS instead
# We are using local derby for the metadata store - not recommended for production - use MySQL or Postgres instead
# If you specify 'druid.extensions.loadList=[]', Druid won't load any extension from file system.
# If you don't specify 'druid.extensions.loadList', Druid will load all the extensions under root extension directory.
# More info: http://druid.io/docs/latest/operations/including-extensions.html
druid_extensions.loadList=["druid-hdfs-storage", "druid-kafka-indexing-service", "druid-datasinkes", "mysql-metadata-storage"]
```
画面10：
```bash
[root@node2-vm06 _common]# vim /opt/druid/conf/druid/single-server/small/_common/common.runtime.properties
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：标题“2.1 数据存储”、“2.1.1 数据流程”；架构图：设备 → Netty → Kafka → Flink → MySQL → Kafka → Druid；Flink指向MySQL的箭头标注“温冷层调度数据”；Kafka指向Druid的箭头标注“温冷层调度数据”。
画面2：标题“2.1.1 数据流程”；架构图：设备 → Netty → Kafka → Flink → MySQL → Kafka → Druid；Flink指向MySQL的箭头标注“温冷层调度数据”；Kafka指向Druid的箭头标注“温冷层调度数据”。
画面3：标题“2.1.1 数据流程”；架构图：设备 → Netty → Kafka → Flink → MySQL → Kafka → Druid；Flink指向MySQL的箭头标注“温冷层调度数据”；Kafka指向Druid的箭头标注“温冷层调度数据”。
画面4：标题“开发流程”；内容：1. 修改配置，添加druid-kafka-indexing-service；2. 提交supervisor任务；表格：2.1.2 数据结构，列名：名称、类型、长度、是否默认值、备注。
画面5：标题“开发流程”；内容：1. 修改配置，添加druid-kafka-indexing-service；2. 提交supervisor任务；表格：2.1.2 数据结构，列名：名称、类型、长度、是否默认值、备注。
画面6：无PPT标题或架构图。
画面7：无PPT标题或架构图。
画面8：无PPT标题或架构图。
画面9：无PPT标题或架构图。
画面10：无PPT标题或架构图。

5) 不要评价画面美观，不要输出与课程无关的内容。
