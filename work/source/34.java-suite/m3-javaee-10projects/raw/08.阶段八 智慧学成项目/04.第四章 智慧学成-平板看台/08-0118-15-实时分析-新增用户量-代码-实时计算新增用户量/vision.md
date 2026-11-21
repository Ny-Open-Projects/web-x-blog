# 画面线理解：15-实时分析-新增用户量-代码-实时计算新增用户量

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\15-实时分析-新增用户量-代码-实时计算新增用户量_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:24, 00:41, 00:59, 01:24, 01:39, 01:56, 02:12, 03:03, 03:25, 04:04, 04:45, 05:11, 05:20, 05:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:46:33

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spark Streaming 从 Kafka 读取实时用户访问数据，并使用 Redis 存储用户访问统计结果的 Scala 代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示代码文件结构，定位到 `RealTimeNewUser.scala`，代码中定义了 SparkConf、Kafka 服务地址、Topic、Redis 连接等配置，并初始化了 SparkContext 和 StreamingContext。
画面 2：代码中设置 Spark Streaming 的检查点目录为 `/user/hive/external/data_course/today_new_user/checkpoint`。
画面 3：展示 Kafka 消费者配置，包括 bootstrapServers、group.id、key 和 value 的反序列化类。
画面 4：展示如何从 Kafka 消费数据并处理，使用 `foreachRDD` 对数据进行处理，包括获取 Redis 中的 offset、计算访问次数并存储回 Redis。
画面 5：代码中设置 Spark Streaming 的检查点目录。
画面 6：代码中设置 Kafka 消费者配置，包括 bootstrapServers、group.id、key 和 value 的反序列化类。
画面 7：展示 Spark Streaming 的数据处理逻辑，包括使用 `foreachRDD` 对数据进行处理，包括获取 Redis 中的 offset、计算访问次数并存储回 Redis。
画面 8：展示 Spark Streaming 的数据处理逻辑，包括使用 `foreachRDD` 对数据进行处理，包括获取 Redis 中的 offset、计算访问次数并存储回 Redis。
画面 9：展示 Spark Streaming 的数据处理逻辑，包括使用 `foreachRDD` 对数据进行处理，包括获取 Redis 中的 offset、计算访问次数并存储回 Redis。
画面 10：展示 Spark Streaming 的数据处理逻辑，包括使用 `foreachRDD` 对数据进行处理，包括获取 Redis 中的 offset、计算访问次数并存储回 Redis。
画面 11：展示 Spark Streaming 的数据处理逻辑，包括使用 `foreachRDD` 对数据进行处理，包括获取 Redis 中的 offset、计算访问次数并存储回 Redis。
画面 12：展示 Spark Streaming 的数据处理逻辑，包括使用 `foreachRDD` 对数据进行处理，包括获取 Redis 中的 offset、计算访问次数并存储回 Redis。
画面 13：展示 Spark Streaming 的数据处理逻辑，包括使用 `foreachRDD` 对数据进行处理，包括获取 Redis 中的 offset、计算访问次数并存储回 Redis。
画面 14：展示 Spark Streaming 的数据处理逻辑，包括使用 `foreachRDD` 对数据进行处理，包括获取 Redis 中的 offset、计算访问次数并存储回 Redis。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```scala
object RealTimeNewUser {
  val sparkConf = new SparkConf()
  def main(args: Array[String]): Unit = {
    val sc = new SparkContext(sparkConf)
    // kafka
    val bootstrapServers = "xc-online-kafka:9092"
    val groupid = "new_user"
    val topicName = "new_user"
    val rt_cv_key = "today:new_user:current"
    val rt_cv_offset = "today:new_user:offset"
    // 1. 不动 KafkaOffset (redis 中存储当前的 offset，如果没 48 小时)
    val redis = new RedisUtils
    redis.initRedisPool()
    val offsets = redis.getLastCommittedOffsets(rt_cv_offset, topicName, partitions = 1)
    // 2. Spark Streaming 读取 Kafka 中用户行为数据，每秒钟读取一次
    val ssc = new StreamingContext(sc, Seconds(5))
    ssc.checkpoint(directory = "/user/hive/external/data_course/today_new_user/checkpoint")
    val kafkaParam = Map[String, Object](
      ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG -> bootstrapServers,
      ConsumerConfig.GROUP_ID_CONFIG -> groupid,
      ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer],
      ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer]
    )
    val message = KafkaUtils.createDirectStream[String, String](
      ssc,
      LocationStrategies.PreferConsistent,
      ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
    )
  }
}
```

画面 2：
```scala
ssc.checkpoint(directory = "/user/hive/external/data_course/today_new_user/checkpoint")
```

画面 3：
```scala
val kafkaParam = Map[String, Object](
  ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG -> bootstrapServers,
  ConsumerConfig.GROUP_ID_CONFIG -> groupid,
  ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer],
  ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer]
)
```

画面 4：
```scala
message.foreachRDD(rdd => {
  if (rdd.isEmpty()) {
    val offsetRanges = rdd.asInstanceOf[HasOffsetRanges].offsetRanges
    offsetRanges.foreach(offsetRange => {
      val topic_partition_key = offsetRange.topic + "_" + offsetRange.partition
      redis.storeOffsetRedis(rt_cv_offset, topic_partition_key, offsetRange.untilOffset)
    })
  }
})
```

画面 5：
```scala
ssc.checkpoint(directory = "/user/hive/external/data_course/today_new_user/checkpoint")
```

画面 6：
```scala
val kafkaParam = Map[String, Object](
  ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG -> bootstrapServers,
  ConsumerConfig.GROUP_ID_CONFIG -> groupid,
  ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer],
  ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer]
)
```

画面 7：
```scala
val message = KafkaUtils.createDirectStream[String, String](
  ssc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

画面 8：
```scala
val message = KafkaUtils.createDirectStream[String, String](
  ssc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

画面 9：
```scala
val message = KafkaUtils.createDirectStream[String, String](
  ssc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

画面 10：
```scala
val message = KafkaUtils.createDirectStream[String, String](
  ssc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

画面 11：
```scala
val message = KafkaUtils.createDirectStream[String, String](
  ssc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

画面 12：
```scala
val message = KafkaUtils.createDirectStream[String, String](
  ssc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

画面 13：
```scala
val message = KafkaUtils.createDirectStream[String, String](
  ssc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

画面 14：
```scala
val message = KafkaUtils.createDirectStream[String, String](
  ssc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
