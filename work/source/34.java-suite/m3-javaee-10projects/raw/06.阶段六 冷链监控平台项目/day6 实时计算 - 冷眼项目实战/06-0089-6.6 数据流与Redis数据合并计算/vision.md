# 画面线理解：6.6 数据流与Redis数据合并计算

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.6 数据流与Redis数据合并计算_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:23, 01:59, 03:35, 05:15, 06:41, 07:57, 08:49, 10:04, 10:51, 11:53, 12:34, 13:45, 14:25, 15:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:32:54

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Flink 流处理程序中，通过自定义的 MapFunction（MessageAggregate）将来自 Kafka 的 MessageEntity 对象与从 Redis 中获取的 MeterEntity 对象进行数据聚合，并将结果写回 Kafka。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示了 MessageEntity.java 文件，其中定义了用于表示监控数据的实体类，包含字段如 maximum、temAlert、temLimit、state 等，并有中文注释说明其含义。
画面 2: 显示了 MessageAggregate.java 文件，该类实现了 MapFunction<MessageEntity, MessageEntity> 接口，用于对输入数据进行处理。
画面 3: 在 MessageAggregate.java 中，代码开始初始化 Jedis 实例，用于连接 Redis。
画面 4: 代码中调用 Jedis 的 get 方法获取 Redis 中存储的 MeterEntity 对象。
画面 5: 代码中使用 Jedis 的 get 方法获取 Redis 中存储的 MeterEntity 对象，并通过反序列化将其转换为 MeterEntity 实例。
画面 6: 代码中将 MessageEntity 对象的属性设置为从 MeterEntity 中获取的值。
画面 7: 代码中将 MessageEntity 对象的属性设置为从 MeterEntity 中获取的值，并处理了温度相关的字段。
画面 8: 代码中将 MessageEntity 对象的属性设置为从 MeterEntity 中获取的值，并处理了温度相关的字段。
画面 9: 代码中将 MessageEntity 对象的属性设置为从 MeterEntity 中获取的值，并处理了温度相关的字段。
画面 10: 代码中根据温度值设置 MessageEntity 对象的 temAlert 字段。
画面 11: 代码中根据温度值设置 MessageEntity 对象的 temAlert 字段。
画面 12: 代码中将 MessageEntity 对象的属性设置为从 MeterEntity 中获取的值，并处理了温度相关的字段。
画面 13: 代码中将 MessageEntity 对象的属性设置为从 MeterEntity 中获取的值，并处理了温度相关的字段。
画面 14: 代码中创建了 KafkaConsumer 和 KafkaProducer，用于从 Kafka 读取数据并写入 Kafka。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private int maximum;
//温度下限
private int minimum;
//温度状况：1.高温，0.正常，-1.低温
private int temAlert;
//温度状况：1.高温，0.正常，-1.低温
private int temLimit;
//状态：1-在用，0-停用，-1-异常
private int state
```

画面 2:
```java
package com.ithema.cold.flink;
import com.ithema.cold.common.entity.MessageEntity;
import org.apache.flink.api.common.functions.MapFunction;
public class MessageAggregate implements MapFunction<MessageEntity, MessageEntity> {
```

画面 3:
```java
import com.ithema.cold.common.entity.MessageEntity;
import com.ithema.cold.common.utils.JedisUtil;
import org.apache.flink.api.common.functions.MapFunction;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
```

画面 4:
```java
final JedisUtil jedisUtil = JedisUtil.getInstance();
```

画面 5:
```java
byte[] meterBy = jedis.get(SafeEncoder.encode(messageEntity.getMetercode()));
MeterEntity meter = (MeterEntity) SerializeUtil.unserialize(meterBy);
messageEntity.setMetercode(meter.getMetercode());
```

画面 6:
```java
messageEntity.setMetername(meter.getMetername());
messageEntity.setHostcode(meter.getHostcode());
messageEntity.setHostid(meter.getHostid());
messageEntity.setHousecode(meter.getHousecode());
messageEntity.setHouseid(meter.getHouseid());
messageEntity.setCompanyname(meter.getCompanyname());
```

画面 7:
```java
messageEntity.setMetername(meter.getMetername());
messageEntity.setHostcode(meter.getHostcode());
messageEntity.setHostid(meter.getHostid());
messageEntity.setHousecode(meter.getHousecode());
messageEntity.setHouseid(meter.getHouseid());
messageEntity.setCompanyname(meter.getCompanyname());
```

画面 8:
```java
messageEntity.setMetername(meter.getMetername());
messageEntity.setHostcode(meter.getHostcode());
messageEntity.setHostid(meter.getHostid());
messageEntity.setHousecode(meter.getHousecode());
messageEntity.setHouseid(meter.getHouseid());
messageEntity.setCompanyname(meter.getCompanyname());
```

画面 9:
```java
messageEntity.setMetername(meter.getMetername());
messageEntity.setHostcode(meter.getHostcode());
messageEntity.setHostid(meter.getHostid());
messageEntity.setHousecode(meter.getHousecode());
messageEntity.setHouseid(meter.getHouseid());
messageEntity.setCompanyname(meter.getCompanyname());
```

画面 10:
```java
if (messageEntity.getTemAlert() == 1) {
    messageEntity.setTemAlert(1);
} else if (messageEntity.getTemAlert() == 0) {
    messageEntity.setTemAlert(0);
} else {
    messageEntity.setTemAlert(0);
}
```

画面 11:
```java
if (messageEntity.getTemAlert() == 1) {
    messageEntity.setTemAlert(1);
} else if (messageEntity.getTemAlert() == 0) {
    messageEntity.setTemAlert(0);
} else {
    messageEntity.setTemAlert(0);
}
```

画面 12:
```java
messageEntity.setMetername(meter.getMetername());
messageEntity.setHostcode(meter.getHostcode());
messageEntity.setHostid(meter.getHostid());
messageEntity.setHousecode(meter.getHousecode());
messageEntity.setHouseid(meter.getHouseid());
messageEntity.setCompanyname(meter.getCompanyname());
```

画面 13:
```java
messageEntity.setMetername(meter.getMetername());
messageEntity.setHostcode(meter.getHostcode());
messageEntity.setHostid(meter.getHostid());
messageEntity.setHousecode(meter.getHousecode());
messageEntity.setHouseid(meter.getHouseid());
messageEntity.setCompanyname(meter.getCompanyname());
```

画面 14:
```java
//Kafka队列的consumer，接收kafka发来的数据
FlinkKafkaConsumer<String> consumer = new FlinkKafkaConsumer<>(druid_topic, new SimpleStringSchema(), properties);
consumer.setStartFromEarliest();
//设置数据源
DataStream<MessageEntity> stream = env.addSource(consumer)
    .map(new MessageAggregate());
//将数据写入kafka队列
FlinkKafkaProducer<String> producer = new FlinkKafkaProducer<>(druid_topic, new SimpleStringSchema(), properties);
outStream.addSink(new SinkWithRetry(producer));
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
