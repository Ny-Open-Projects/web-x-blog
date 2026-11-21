# 6.14 学习总结

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.14 学习总结_【海量资源尽在 666java.com】.mp4
- 时长 2分0秒（音频 121s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面我们来总结一下我们的实时计算模块实时计算模块来讲的话在我们冷链设备监控平台里边分成两部分一部分叫实时数据的一个处理叫CodeFlink另外一个的话叫实时数据的一个查询那么实时数据的处理的话这个CodeFlink这个Java的这个工程我们在它是一个普通的一个架构工程只不过是引用了Flink的一些jar 包那么这个jar 包这个工程呢我们把它打包打包成
[00:29] 加文件之后呢我们又可以把它部署到Flink的一个运行环境里边那么在我们当前的这个模块里边我们实现的逻辑啊一方面是它的数据是从Kafka里边拿到的结构化的报文数据那么另外一块的话是我们从Redis里边拿到的温湿度的一个预值数据那么两者结合我们进行一个计算那得到了一个数据的一个结果呢我们一方面是发送到我们Kafka的一个队列里边那另外一方面我们存储到MySQL里边
[00:59] 这就是我们在我们的实时处理逻辑处理模块里边的它相应的一个逻辑那么第二部分来讲是我们的一个Flink的一个实时数据的一个查询那么实时数据的查询它就是查询我们在第一部分存储到mySQL里边的这些实时数据其实就是一个java gdbc的一个查询数据库相应来讲的话代码和整体的业务逻辑也比较简单一些
[01:27] 从今天这个学习里边我们需要掌握的就是第一我们如何来开发Flink的一个工程Flink的一个java工程那么第二我如何来实现我的一个实时计算的一个逻辑我代码的结构我们是什么样的一个结构对吧那第三部分来讲是说我如何来提交我们的程序把我们的Flink的一个java工程如何提交到Flink的运行环境里边来进行一个执行
[01:56] 这是我们今天的一个学习的一个总结

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解基于 Flink 的实时数据处理系统，涵盖需求分析、数据模型设计、核心代码实现及系统架构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：介绍课程主题“实时计算模块”，学习目标包括掌握 Flink 数据流开发、Nginx 代理的使用、实时数据处理方式。
画面2：展示“1.1 需求分析”内容，说明系统需将设备数据转换为 JSON 提交到 Kafka，并通过 Flink 实时对比温度湿度进行异常预警。下方展示业务流程图：提交数据 → 数据转换 → 数据解析 → 数据存储。
画面3：展示“1.2.1 实现逻辑”流程图，包含设备 → Netty → Kafka → Flink → MySQL → Druid 的数据流向。图中包含两个代码块：左侧是 Netty 接收设备数据的 JSON 格式示例；右侧是 Flink 中处理数据的 JSON 格式示例。
画面4：展示“1.2.2 数据模型”内容，列出数据处理的五个步骤：监听 Kafka 队列、从 Redis 获取基础数据、合并判断阈值、推送至 Kafka、存储至 MySQL。
画面5：展示“1.2.2 数据模型”表格，列出字段名、类型、长度、是否主键、默认值、备注。
画面6：展示“1.2.2 数据模型”表格，继续展示字段，包括 temAlert、humAlert、state、lon、lat、curtime、createTime 及其注释。
画面7：展示“1.2.3 核心代码”部分，展示 Flink 环境配置代码，包括设置检查点、重启策略、Kafka 消费者配置。
画面8：展示“1.2.3 核心代码”部分，展示从 Redis 获取数据的 Java 代码片段，包含 try-catch-finally 结构，以及存储到 MySQL 的 Sink 类定义。
画面9：展示“1.2.3 核心代码”部分，展示向 MySQL 插入数据的 PreparedStatement 设置代码。
画面10：展示“1.2.3 核心代码”部分，展示在 Apache Druid 中提交作业的界面截图。
画面11：展示“1.2.2 数据模型”表格，再次展示字段，包括 meterCode、meterName、hostId、hostCode、hostName、houseId、houseCode、houseName、companyId、companyName、tem、maxTem、minTem、hum、maxHum、minHum、temAlert、humAlert、state、lon、lat、curtime、createTime。
画面12：展示“2.3 代码实现”标题，以及左侧导航栏中“1.2.3 核心代码”被选中。
画面13：展示“1.2.3 核心代码”部分，展示 Flink 环境配置代码，包括设置检查点、重启策略、Kafka 消费者配置。
画面14：展示“1.2.3 核心代码”部分，展示完整的 Flink 程序核心代码，包括设置数据源、从 Redis 获取数据、存储到 MySQL、推送至 Kafka、执行任务。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```json
{
  "meterCode": "00000000000000000000000000000000",
  "meterId": "00000000000000000000000000000000",
  "hostId": "00000000000000000000000000000000",
  "hostCode": "00000000000000000000000000000000",
  "houseId": "00000000000000000000000000000000",
  "companyId": "00000000000000000000000000000000",
  "companyName": "00000000000000000000000000000000",
  "tem": 0,
  "maxTem": 0,
  "minTem": 0,
  "hum": 0,
  "maxHum": 0,
  "minHum": 0
}
```
画面3：
```json
{
  "meterCode": "00000000000000000000000000000000",
  "meterId": "00000000000000000000000000000000",
  "hostId": "00000000000000000000000000000000",
  "hostCode": "00000000000000000000000000000000",
  "houseId": "00000000000000000000000000000000",
  "companyId": "00000000000000000000000000000000",
  "companyName": "00000000000000000000000000000000",
  "tem": 0,
  "maxTem": 0,
  "minTem": 0,
  "hum": 0,
  "maxHum": 0,
  "minHum": 0
}
```
画面7：
```java
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
//设置容错
env.enableCheckpointing(5000);
//设置检查点模式
env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
//设置重启策略
env.getConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
Properties properties = new Properties();
properties.setProperty("bootstrap.servers", "172.17.0.143:9092");
properties.setProperty("group.id", "coldlink");
properties.setProperty("auto.offset.reset", "earliest");
//Kafka队列consumer，接收netty发送过来的数据
FlinkKafkaConsumer<String> consumer = new FlinkKafkaConsumer<String>("device_mag_topic",
        new SimpleStringSchema(), properties);
consumer.setStartFromLatest();
//设置实时数据源：Kafka队列
DataStream<MessageEntity> stream = env.addSource(consumer)
        .setParallelism(1)
        .map(string -> JSON.parseObject(string, MessageEntity.class));
```
画面8：
```java
public class SinkToMySQL extends RichSinkFunction<MessageEntity> {
    private Connection connection = null;
    private PreparedStatement preparedStatement = null;
    private String userName = null;
    private String password = null;
    private String database = null;
    private String url = null;
    private String driver = null;
}
```
画面9：
```java
preparedStatement.setString(2, value.getUtername());
preparedStatement.setString(4, value.getHousId());
preparedStatement.setString(6, value.getHouseId());
preparedStatement.setString(7, value.getHouseCode());
preparedStatement.setString(8, value.getHouseName());
preparedStatement.setString(9, value.getCompanyId());
preparedStatement.setString(10, value.getCompanyName());
preparedStatement.setInt(12, value.getTem());
preparedStatement.setInt(14, value.getHumin());
preparedStatement.setInt(15, value.getHum());
preparedStatement.setInt(16, value.getHum());
preparedStatement.setString(17, value.getCurtime());
// preparedStatement.toString();
preparedStatement.executeUpdate();
catch (Exception e) {
```
画面13：
```java
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
//设置容错
env.enableCheckpointing(5000);
//设置检查点模式
env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
//设置重启策略
env.getConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
Properties properties = new Properties();
properties.setProperty("bootstrap.servers", "172.17.0.143:9092");
properties.setProperty("group.id", "coldlink");
properties.setProperty("auto.offset.reset", "earliest");
//Kafka队列consumer，接收netty发送过来的数据
FlinkKafkaConsumer<String> consumer = new FlinkKafkaConsumer<String>("device_mag_topic",
        new SimpleStringSchema(), properties);
consumer.set

