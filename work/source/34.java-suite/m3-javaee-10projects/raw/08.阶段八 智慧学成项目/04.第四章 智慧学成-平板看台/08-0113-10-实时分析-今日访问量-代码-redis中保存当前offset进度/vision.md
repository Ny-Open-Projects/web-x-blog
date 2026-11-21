# 画面线理解：10-实时分析-今日访问量-代码-redis中保存当前offset进度

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\10-实时分析-今日访问量-代码-redis中保存当前offset进度_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:45, 02:11, 03:12, 04:20, 06:11, 07:15, 08:51, 09:39, 09:58, 10:14, 10:33, 11:56, 12:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:42:21

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Scala 中使用 Spark Streaming 从 Kafka 消费数据，并将处理后的结果和消费位点（offset）持久化到 Redis。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 RedisUtils.scala 文件中用于将聚合结果存储到 Redis 的代码，包含对 Redis 的 key 和 value 的操作。
画面 2: 代码光标移动，显示了对 Redis 的 key 和 value 的操作，注释提到“redis中存储的offset位置”。
画面 3: 代码光标移动，显示了对 Redis 的 key 和 value 的操作，注释提到“redis中存储的offset位置”。
画面 4: 展示了 getLatestCommittedOffsets 方法，用于获取 Kafka 消费位点，代码中包含对 Jedis 的操作。
画面 5: 展示了 foreachRDD 的代码块，用于处理从 Kafka 消费到的 RDD 数据，包含对 Redis 的操作。
画面 6: 展示了 storeOffsetRedis 方法的定义，用于将消费位点存储到 Redis。
画面 7: 展示了 storeOffsetRedis 方法的实现，使用 Jedis 的 pipeline 进行批量操作。
画面 8: 展示了 foreachRDD 的代码块，用于处理从 Kafka 消费到的 RDD 数据，包含对 Redis 的操作。
画面 9: 展示了 Spark Streaming 的配置代码，包括 Kafka 的配置和 Spark 的配置。
画面 10: 展示了 Spark Streaming 的配置代码，包括 Kafka 的配置和 Spark 的配置。
画面 11: 展示了 foreachRDD 的代码块，用于处理从 Kafka 消费到的 RDD 数据，包含对 Redis 的操作。
画面 12: 展示了 Spark Streaming 的初始化代码，包括创建 StreamingContext 和配置 Kafka 的参数。
画面 13: 展示了 Spark Streaming 的初始化代码，包括创建 StreamingContext 和配置 Kafka 的参数。
画面 14: 展示了 Spark Streaming 的启动和关闭代码，包括 start 和 awaitTermination 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
val keyInfo = "visit_date" + getDateTime(new Date()).getTime, pattern = "yyyy-MM-dd"
val valStr = redis.getMultiRedis(rt_cv_key, keyInfo)
if (null != valStr) {
  accumulator.add(valStr.toLong)
}
accumulator.add(valStr.toLong)
redis.storeResultRedis(rt_cv_key, keyInfo, accumulator.value.toString)
```

画面 2:
```scala
// redis中存储的offset位置
```

画面 3:
```scala
val keyInfo = "visit_date" + getDateTime(new Date()).getTime, pattern = "yyyy-MM-dd"
val valStr = redis.getMultiRedis(rt_cv_key, keyInfo)
if (null != valStr) {
  accumulator.add(valStr.toLong)
}
accumulator.add(valStr.toLong)
redis.storeResultRedis(rt_cv_key, keyInfo, accumulator.value.toString)
```

画面 4:
```scala
def getLatestCommittedOffsets(rt_offset_key: String, topicName: String, partitions: Int): Map[TopicPartition, Long] = {
  val jedis = getPool.getResource
  val offsetMap = collection.mutable.Map[TopicPartition, Long]()
  for (partition <- 0 to partitions - 1) {
    val topicPartitionKey = topicName + "_" + partition
    val lastOffsetTmp = jedis.get(rt_offset_key + "_" + topic_partition_key)
    val lastOffset = if (lastOffsetTmp == null) 0L else lastOffsetTmp.toLong
    offsetMap += (new TopicPartition(topicName, partition) -> lastOffset)
  }
  offsetMap.toMap
}
```

画面 5:
```scala
message.foreachRDD(rdd => {
  if (rdd.isEmpty()) {
    // 获取offset
    val offsetRanges = rdd.asInstanceOf[HasOffsetRanges].offsetRanges
    offsetRanges.foreach(offsetRange => {
      val topic_partition_key = offsetRange.topic + "_" + offsetRange.partition
      redis.storeOffsetRedis(rt_cv_offset, topic_partition_key, offsetRange.untilOffset)
    })
  }
})
```

画面 6:
```scala
def storeOffsetRedis(key: String, keyInfo: String, value: Long): Unit = {
  // todo 完成功能
}
```

画面 7:
```scala
def storeOffsetRedis(key: String, keyInfo: String, value: Long): Unit = {
  val jedis = getPool.getResource
  val pip = jedis.pipelined()
  pip.multi()
}
```

画面 8:
```scala
message.foreachRDD(rdd => {
  if (rdd.isEmpty()) {
    // 获取offset
    val offsetRanges = rdd.asInstanceOf[HasOffsetRanges].offsetRanges
    offsetRanges.foreach(offsetRange => {
      val topic_partition_key = offsetRange.topic + "_" + offsetRange.partition
      redis.storeOffsetRedis(rt_cv_offset, topic_partition_key, offsetRange.untilOffset)
    })
  }
})
```

画面 9:
```scala
val message = KafkaUtils.createDirectStream[String, String](
  spark,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

画面 10:
```scala
val message = KafkaUtils.createDirectStream[String, String](
  spark,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

画面 11:
```scala
message.foreachRDD(rdd => {
  if (rdd.isEmpty()) {
    // 获取offset
    val offsetRanges = rdd.asInstanceOf[HasOffsetRanges].offsetRanges
    offsetRanges.foreach(offsetRange => {
      val topic_partition_key = offsetRange.topic + "_" + offsetRange.partition
      redis.storeOffsetRedis(rt_cv_offset, topic_partition_key, offsetRange.untilOffset)
    })
  }
})
```

画面 12:
```scala
val rt_cv_key = "today's course.visit:current"
val rt_cv_offset = "today's course.visit:offset"
val redis = new RedisUtils
redis.initRedis()
val offsets = redis.getLatestCommittedOffsets(rt_cv_offset, topicName, partitions = 1)
val ssc = new StreamingContext(sc, Seconds(5))
```

画面 13:
```scala
val ssc = new StreamingContext(sc, Seconds(5))
val checkpointDirectory = "/user/hion/external/data_course/today_visit/checkpoint"
val kafkaParam = Map[String, Object](
  "bootstrap.servers" -> bootstrapServers,
  "group.id" -> groupId,
  "key.deserializer" -> classOf[StringDeserializer],
  "value.deserializer" -> classOf[StringDeserializer]
)
val message = KafkaUtils.createDirectStream[String, String](
  spark,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

画面 14:
```scala
ssc.start()
ssc.awaitTermination()
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
