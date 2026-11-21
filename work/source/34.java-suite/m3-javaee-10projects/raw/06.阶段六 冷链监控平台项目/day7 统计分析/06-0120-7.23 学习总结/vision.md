# 画面线理解：7.23 学习总结

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.23 学习总结_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:27, 02:06, 02:18, 02:29, 02:38, 03:16, 03:26, 03:48, 04:08, 04:37, 05:00, 05:14, 05:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:52:24

1) 这一组画面整体在讲什么（一句话）：
演示如何搭建 Apache Druid 实时数据处理平台，包括环境准备、组件安装、配置文件结构、数据导入、查询操作及代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
要点：展示在 Typora 中打开的课程大纲，当前章节为“1.1 特性”，并显示了终端命令行界面，其中包含设置 Kafka 环境变量、进入 Kafka 目录、列出 topic 的命令，以及启动 Kafka 生产者和消费者的命令。

画面2：
要点：展示课程大纲，当前选中“1.1.3 不适用场景”，并列出 Druid 的适用和不适用场景，包括对实时数据、高并发、高可用性的支持，以及对流式更新和跨表 join 的不支持。

画面3：
要点：展示课程大纲，当前选中“1.2 环境”，并显示了 Druid 的架构图，包含 Streaming Data、Metadata Storage、Zookeeper、Broker Nodes、Historical Nodes 和 Deep Storage 等组件及其连接关系。下方列出演示环境使用的软件：2核、8G内存、CentOS 7、jdk 1.8、Apache Druid 0.15.8。

画面4：
要点：展示课程大纲，当前选中“1.2.4 安装kafka”，并显示了安装 Zookeeper 的命令，包括下载、解压、配置和启动 Zookeeper 的命令。

画面5：
要点：展示课程大纲，当前选中“1.4 配置”，并显示了 Druid 0.15.8 版本的配置文件目录结构，包括 config 目录下的 cluster、common、data、historical、middlemanager、master、coordinator-overlord、query、broker、single-server、large、medium、nitro-quickstart 等子目录。

画面6：
要点：展示课程大纲，当前选中“3.6.1 高速数据导入”，并显示了 Druid 的 Web 界面，其中包含数据源配置、查询类型、时间范围等选项，以及一个警告提示。

画面7：
要点：展示课程大纲，当前选中“1.7.1.1 客户端”，并显示了 Druid 的查询界面，包含一个简单的查询结果，以及一个 SQL 查询示例，用于统计维基百科编辑次数。

画面8：
要点：展示课程大纲，当前选中“1.7.1.3 JDBC”，并显示了使用 Apache Calcite 的 JDBC 示例代码，包括连接字符串、属性设置、SQL 查询和结果集处理。

画面9：
要点：展示课程大纲，当前选中“1.7.3 聚合粒度(granularity)”，并显示了 JSON 格式的查询配置，包括 queryType、dataSource、granularity、dimensions、aggregations 和 intervals 等字段。

画面10：
要点：展示课程大纲，当前选中“2 Druid实战”，并显示了 Druid 实战部分的目录结构，包括数据源、数据查询、supervisor、数据指标、报警记录、温度曲线等子章节。

画面11：
要点：展示课程大纲，当前选中“2.1 数据源”，并显示了 Kafka 消费者配置的 JSON 格式，包括 offsetFetchPeriod、IntermediateHandoffPeriod、logParseExceptions、maxSavedParseExceptions、skipSequenceNumberAvailabilityCheck、topic、replicas、taskcount、consumerProperties、pollTimeout、startDelay、period、useFarthestOffset、completionTimeout、earlyMessageRejectionPeriod、lateMessageRejectionPeriod、stream、useEarliestSequenceNumber 等字段。

画面12：
要点：展示课程大纲，当前选中“2.2.2 温湿度曲线”，并显示了 Druid 的数据查询界面，包含报警记录和温度曲线的图表。

画面13：
要点：展示课程大纲，当前选中“2.3 代码实现”，并显示了 Druid 的温度曲线图表，以及一个请求映射的按钮。

画面14：
要点：展示课程大纲，当前选中“2.3 代码实现”，并显示了 Java 代码，包括获取数据库连接的方法和关闭数据库连接、语句和结果集的方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```bash
export KAFKA_OPTS="-Dfile.encoding=UTF-8"
[root@node2-v86 opt]# cd /opt
[root@node2-v86 opt]# /opt/software/kafka_2.12-2.3.8/bin/kafka-console-producer.sh --broker-list 172.17.0.143:9092 --topic wikipedia
# 执行kafka队列消费者
[root@node2-v86 opt]# /opt/software/kafka_2.12-2.3.8/bin/kafka-console-consumer.sh --bootstrap-server 172.17.0.143:9092 --topic wikipedia --from-beginning
```

画面5：
```yaml
config
  druid
    - cluster
    - common
    - data
    - historical
    - middlemanager
    - master
    - coordinator-overlord
    - query
    - broker
    - single-server
    - large
    - medium
    - nitro-quickstart
```

画面7：
```sql
dsql> SELECT page, COUNT(*) AS Edits FROM wikipedia WHERE "_time" BETWEEN TIMESTAMP '2015-09-12 00:00:00' AND TIMESTAMP '2015-09-13 00:00:00' GROUP BY page ORDER BY Edits DESC LIMIT 10;
```

画面8：
```java
String url = "jdbc:avatica:remote:url=http://172.17.0.143:8882/druid/v2/sql/avatica/";
Properties properties = new Properties();
String sql = "SELECT * from wikipedia order by _time desc limit 10";
try {
    Connection connection = DriverManager.getConnection(url, properties);
    ResultSet resultSet = connection.createStatement().executeQuery(sql);
    while (resultSet.next()) {
        System.out.println(resultSet.getString("page"));
    }
    connection.close();
} catch (SQLException e) {
    e.printStackTrace();
}
```

画面9：
```json
{
  "queryType": "groupBy",
  "dataSource": "Wikipedia",
  "granularity": "hour",
  "dimensions": [
    "language"
  ],
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ],
  "intervals": [
    "2019-01-01T00:00:00/2019-01-01T00:00:00Z"
  ]
}
```

画面11：
```json
{
  "offsetFetchPeriod": "PT30S",
  "IntermediateHandoffPeriod": "P1474836470",
  "logParseExceptions": false,
  "maxSavedParseExceptions": 8,
  "skipSequenceNumberAvailabilityCheck": false,
  "loConfig": {
    "topic": "all_device_message",
    "replicas": 1,
    "taskcount": 3,
    "taskDuration": "PT000S",
    "consumerProperties": {
      "bootstrap.servers": "172.17.0.143:9092"
    }
  },
  "pollTimeout": 100,
  "startDelay": "PT5S",
  "period": "PT30S",
  "useFarthestOffset": false,
  "completionTimeout": "PT1200S",
  "earlyMessageRejectionPeriod": null,
  "lateMessageRejectionPeriod": null,
  "stream": "all_device_message",
  "useEarliestSequenceNumber": false
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：
架构图结构：
- Streaming Data → Metadata Storage
- Streaming Data → Broker Nodes
- Metadata Storage → Broker Nodes
- Broker Nodes → Historical Nodes
- Broker Nodes → Deep Storage
- Historical Nodes → Deep Storage
- Metadata Storage → Zookeeper
- Broker Nodes → Zookeeper
- Historical Nodes → Zookeeper

画面5：
表格数据：
- config 目录下的子目录：cluster、common、data、historical、middlemanager、master、coordinator-overlord、query、broker、single-server、large、medium、nitro-quickstart

画面12：
表格数据：
- 报警记录表格包含：设备名称、报警时间、报警数量、报警日期、温度、湿度、报警等级、报警次数、报警状态等字段。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
