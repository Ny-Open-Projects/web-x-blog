# 7.23 学习总结

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.23 学习总结_【海量资源尽在 666java.com】.mp4
- 时长 5分21秒（音频 321s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来总结一下我们今天的课程那首先呢我们介绍了我们的这个Apache DroidApache Droid到底是一个什么大家记住Apache Droid首先它是一个数据库这个数据库能存储数据这是数据和我们的这个时间相关联的事件的数据同时呢它在存储数据的时候呢它能对数据进行一些聚合进行一些统计分析
[00:24] 这是我们的Apache Droid那么它的一个适用的场景呢包括我们的一些数据量比较大的一些不容易改变的数据同时要进行聚合实时统计分析的数据而且统计分析实时的数据的查询结果呢又比较要求时效性又比较快或者说是秒级或者亚秒级的这样的一个我就能把统计结果拿到或者是统计结果查询到了这样的一个数据库
[00:51] 那他不适应的一个场景包括一些联表的一些联表的一些关联查询啊或者是一些这个进行批量的更新的进行修改或者说更新操作比较多的这样的他其实不太适合的那他针对他的架构体系来讲的话大家要记住两个方向一个来讲的话是从数据的流入了进来因为我们打着把他
[01:14] 整个的当成一个数据库来讲的话一个是数据要存储进去一个是数据要进行查询出来那么进行存储进去的话一种是包括我们的这种批量的数据也就是说是文本文件或者说API或者其他的一些这种离线数据的一个存储存储进去另外一块就是我们的实时数据实时数据到底怎么存储到我们ApacheJ的里面去的
[01:39] 那存储完了之后呢它是如何来保存到我们的这个叫深入存储里边以及由深入存储如何加载到我们的这种历史节点的那还有另外一个是查询的一个流向查询的流向来讲的话从客户端进行查询的时候它一种情况它会查询我们实时的节点另一种的话它可以查询到我们的这历史节点对吧这是两种方式那么
[02:06] 接着我们给大家介绍了如果安装Apache Dread的时候我需要安装JDK需要安装或在我们的Dread里边添加MySQL的驱动我们要安装Zookable和Kafka那么下面的话我们就安装我们的这个Dread安装Dread的时候其实是我们只要把文件下载下来然后对它进行修改里边的配置然后启动就OK了
[02:31] 紧接着的话我们给大家介绍了数据的导入包括这种离线数据如何导入进来那么实时数据如何导入进来包括我们的如果数据出现了异常的话或者我们直接把它删掉但是大多数删除操作其实用的不是特别多对吧那么还有一个类
[02:48] 一个是查询的时候另外一个就属于我们的这种一个是属于我们的数据导入另外一个就是我们数据的一个查询而这种数据的查询罪的数据查询它和其他的MySQL数据库或者其他数据库查询方式不太一样那么我们先说它的这个查询方式查询方式来讲的话包括我们的客户端查询用我们的DSQL或者是我们的web页面里面对它进行查询那么还有是用API
[03:17] API的话包括我们json格式的API和那种circle格式的API然后还有一个我们开发代码用GDPC来进行开发那么针对于json格式的我们下面会给大家讲的比较多一些那相应来讲的话还有我们针对于J的查询的时候查询的一些查询类型查询属性然后聚合力度它的聚合力度到底是什么聚合力度是什么含义
[03:44] 大家要记住这种聚合力度也好还是查询的过滤区也好还是聚合查询的类型查询搜索条件搜索查询这个都针对的是我针对于J的数据库把它数据查询出来查询我展现的展现出来这样的一个那介绍完J的的这个存储安装存储和这个查询之后呢我们有了一个项目的一个实战在项目实战里边我们知道我们
[04:12] 阿帕奇坠的他在所处的范围因为在前面的Flink进行实时计算之后得到的结果我扔到了卡布卡队列里边而坠的就监听这个卡布卡队列实时的把数据存储到我们的坠的里面去那实时存储到坠的里面去之后呢我们呢这个是一个存储过程对吧我们开发我们的supervisor来存储我们的Flink计算结果的卡布卡的数据
[04:38] 存储完了之后不是目的目的是为了我们最终的一个展示或者说给我们查看对吧查看来讲的话包括两类的一个查看一个是叫做我们的报警记录而这个报警记录的话是从我们的apache追的里面查询出来的数据这种报警记录可以按照我们的编码或者开始时间结束时间来不同的条件来查询那么还有一类的话是属于我们针对于单一的
[05:04] 单个的某一个这种这个设备来查询它过去的一段时间内的温度的曲线和湿度的曲线这是我们今天的一个课程包括我们的代码实现这是今天我们学到的一些内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
要点：展示课程大纲，当前选中“1.2.4 安装Kafka”，并显示了安装 Zookeeper 的命令，包括下载、解压、配置和启动 Zookeeper 的命令。

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
[root@node2-v86 opt]# /opt/software/kafka_2.12-2.3.8/bin/Kafka-console-producer.sh --broker-list 172.17.0.143:9092 --topic wikipedia
# 执行Kafka队列消费者
[root@node2-v86 opt]# /opt/software/kafka_2.12-2.3.8/bin/Kafka-console-consumer.sh --bootstrap-server 172.17.0.143:9092 --topic wikipedia --from-beginning
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

