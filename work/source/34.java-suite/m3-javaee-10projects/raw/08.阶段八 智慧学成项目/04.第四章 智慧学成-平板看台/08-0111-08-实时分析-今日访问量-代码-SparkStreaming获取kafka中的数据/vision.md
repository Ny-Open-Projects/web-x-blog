# 画面线理解：08-实时分析-今日访问量-代码-SparkStreaming获取kafka中的数据

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\08-实时分析-今日访问量-代码-SparkStreaming获取kafka中的数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 01:00, 01:26, 03:27, 03:54, 04:56, 06:07, 06:28, 06:53, 07:33, 08:27, 09:28, 09:59, 10:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:40:38

1) 这一组画面整体在讲如何使用 Spark Streaming 从 Kafka 消费数据，并通过 Redis 保存消费位点，实现基于 Redis 的 Kafka 消费位点管理。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了创建 SparkContext 的代码，配置了 Kafka 的 bootstrapServers、group.id、topic.name 和 Redis 的 offset 键值。
画面 2: 展示了 Spark Streaming 的 StreamingContext 类的源码，包含其内部的私有成员变量和构造函数。
画面 3: 同画面 2，展示 StreamingContext 类的源码。
画面 4: 展示了 ConsumerConfig 类的常量定义，用于配置 Kafka 消费者。
画面 5: 展示了 ConsumerConfig 类的常量定义，用于配置 Kafka 消费者。
画面 6: 展示了创建 KafkaDirectStream 的代码，配置了 Kafka 的参数。
画面 7: 展示了选择 KafkaDirectStream 方法的弹窗，显示了方法签名。
画面 8: 展示了为 KafkaDirectStream 设置 locationStrategy 的代码。
画面 9: 展示了 Consumer 类的自动补全列表，包含各种 Consumer 类型。
画面 10: 展示了 ConsumerStrategies 类的自动补全列表，包含各种消费策略。
画面 11: 展示了 Scala 中的集合操作方法，如 scan、split、span 等。
画面 12: 展示了创建 KafkaDirectStream 并设置 locationStrategy 和 assign 的代码。
画面 13: 展示了设置 KafkaDirectStream 的 locationStrategy 和 assign 的完整代码。
画面 14: 展示了设置 KafkaDirectStream 的 locationStrategy 和 assign 的完整代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
val sc = new SparkContext(sparkConf)
val bootstrapServers = "xc-online-kaika:9002"
val groupId = "visit_topic"
val topicName = "visit_topic"
val rt_cv_key = "today:course:visit:current"
val rt_cv_offset = "today:course:visit:offset"
```

画面 4:
```scala
val redis = new RedisUtils
redis.initRedisPool()
val offsets = redis.getLastCommittedOffsets(rt_cv_offset, topicName, partitions = 1)
```

画面 6:
```scala
val kafkaParam = Map[String, Object](
  ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG -> bootstrapServers,
  ConsumerConfig.GROUP_ID_CONFIG -> groupId,
  ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer],
  ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer]
)
```

画面 8:
```scala
LocationStrategies.PreferConsistent
```

画面 12:
```scala
val message = KafkaUtils.createDirectStream[String, String](
  sc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
