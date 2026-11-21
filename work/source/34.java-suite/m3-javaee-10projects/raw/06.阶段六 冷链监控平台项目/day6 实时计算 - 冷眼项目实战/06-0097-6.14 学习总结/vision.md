# 画面线理解：6.14 学习总结

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.14 学习总结_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:38, 00:40, 01:04, 01:18, 01:21, 01:22, 01:24, 01:26, 01:27, 01:28, 01:31, 01:42, 01:54, 01:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:38:26

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
//设置实时数据源：kafka队列
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
