# 画面线理解：19-实时分析-今日购买量-统计分析逻辑&代码

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\19-实时分析-今日购买量-统计分析逻辑&代码_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 02:54, 03:06, 03:16, 03:47, 03:54, 04:42, 05:07, 05:21, 05:29, 06:00, 06:11, 06:42, 07:02, 07:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:49:40

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Scala 中使用 Spark Streaming 从 Kafka 消费数据，并通过 Redis 实现实时用户和课程购买数据的统计与状态维护。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 RealTimeNewUser.scala 文件的代码，其中定义了 Redis 连接、获取偏移量、创建 Spark Streaming 上下文、设置检查点目录和 Kafka 消费参数。同时，控制台显示了程序运行日志，包括清理检查点和删除旧日志文件。
画面 2: 代码中光标位于 kafkaParam 的定义处，显示了 Kafka 消费者配置，包括 bootstrapServers、group.id、key 和 value 的反序列化器设置。
画面 3: 弹出“Copy RealTimeNewUser.scala to...”对话框，用于复制文件。下方代码显示了 ConsumerConfig 的配置项，包括 BOOTSTRAP_SERVERS_CONFIG、GROUP_ID_CONFIG、KEY_DESERIALIZER_CLASS_CONFIG 和 VALUE_DESERIALIZER_CLASS_CONFIG。
画面 4: 展示了 RealTimeBuy.scala 文件，代码结构与 RealTimeNewUser.scala 类似，但 topicName 设置为 "course_buy"，用于处理课程购买数据。
画面 5: 展示了 RealTimeBuy.scala 文件的 main 方法，定义了 SparkConf、SparkContext、Kafka 消费者参数（bootstrapServers、group.id、topicName）和 Redis 连接。
画面 6: 代码中定义了 accumulator 和 keyInfo，用于统计用户购买数据。keyInfo 使用 getDateTime 获取当前日期并格式化为 "yyyy-MM-dd"。
画面 7: 代码中定义了 rt_cv_offset 和 rt_cv_key，用于记录课程购买的偏移量和键值。
画面 8: 代码中展示了 foreachRDD 的逻辑，用于处理每批数据。如果数据量大于 0，则将统计结果存入 Redis。
画面 9: 代码中光标位于 kafkaParam 的定义处，显示了 Kafka 消费者配置，包括 bootstrapServers、group.id、key 和 value 的反序列化器设置。
画面 10: 代码中光标位于 kafkaParam 的定义处，显示了 Kafka 消费者配置，包括 bootstrapServers、group.id、key 和 value 的反序列化器设置。
画面 11: 代码中定义了 topicName 为 "course_buy"，用于处理课程购买数据。
画面 12: 代码中定义了 topicName 为 "course_buy"，用于处理课程购买数据。
画面 13: 代码中定义了 rt_cv_offset 和 rt_cv_key，用于记录课程购买的偏移量和键值。
画面 14: 代码中展示了 foreachRDD 的逻辑，用于处理每批数据。如果数据量大于 0，则将统计结果存入 Redis。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
val redis = new RedisUtils
redis.initRedisPool()
val offsets = redis.getLatestCommittedOffsets(rt_cv_offset, topicName, partitions = 1)
// 2. Spark Streaming
val sc = new StreamingContext(sc, Seconds(5))
sc.checkpoint(directory = "/user/hive/external/data_course/today_new_user/checkpoint")
val kafkaParam = Map[String, Object](
  "bootstrapServers" -> bootstrapServers,
  "groups" -> groupId,
  ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer],
  ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer]
)
```
画面 2:
```scala
val kafkaParam = Map[String, Object](
  "bootstrapServers" -> bootstrapServers,
  "groups" -> groupId,
  ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer],
  ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer]
)
```
画面 3:
```scala
ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG -> bootstrapServers,
ConsumerConfig.GROUP_ID_CONFIG -> groupId,
ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer],
ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer]
```
画面 4:
```scala
val kafkaParam = Map[String, Object](
  "bootstrapServers" -> bootstrapServers,
  "groups" -> groupId,
  ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer],
  ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer]
)
```
画面 5:
```scala
val bootstrapServers = "xc-online-kafka:9092"
val groupId = "new_user"
val topicName = "today_new_user:current"
val rt_cv_key = "today_new_user:offset"
val rt_cv_offset = "today_new_user:offset"
```
画面 6:
```scala
val accumulator = sc.longAccumulator(name = "newUser")
val keyInfo = "new_user_data_" + getDateTime(new Date()).getTime + "_" + getDateTime(new Date()).getDay
val valStr = redis.getResults(rt_cv_key, keyInfo)
if (null != valStr) {
  accumulator.add(valStr.toLong)
}
```
画面 7:
```scala
val rt_cv_offset = "today:course_buy:offset"
val rt_cv_key = "today:course_buy:current"
val rt_cv_offset = "today:course_buy:offset"
```
画面 8:
```scala
courseBuy.foreachRDD(iter => {
  if (iter.count() > 0) {
    accumulator.add(iter.count())
    redis.storeResultRedis(rt_cv_key, keyInfo, accumulator.value.toString)
  }
})
```
画面 9:
```scala
val kafkaParam = Map[String, Object](
  "bootstrapServers" -> bootstrapServers,
  "groups" -> groupId,
  ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer],
  ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer]
)
```
画面 10:
```scala
val kafkaParam = Map[String, Object](
  "bootstrapServers" -> bootstrapServers,
  "groups" -> groupId,
  ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer],
  ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer]
)
```
画面 11:
```scala
val topicName = "course_buy"
```
画面 12:
```scala
val topicName = "course_buy"
```
画面 13:
```scala
val rt_cv_offset = "today:course_buy:offset"
val rt_cv_key = "today:course_buy:current"
```
画面 14:
```scala
courseBuy.foreachRDD(iter => {
  if (iter.count() > 0) {
    accumulator.add(iter.count())
    redis.storeResultRedis(rt_cv_key, keyInfo, accumulator.value.toString)
  }
})
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
