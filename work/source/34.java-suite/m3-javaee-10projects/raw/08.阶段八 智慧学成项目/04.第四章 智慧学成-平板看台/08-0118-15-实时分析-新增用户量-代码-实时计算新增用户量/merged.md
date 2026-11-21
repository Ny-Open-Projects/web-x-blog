# 15-实时分析-新增用户量-代码-实时计算新增用户量

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\15-实时分析-新增用户量-代码-实时计算新增用户量_【海量资源尽在 666java.com】.mp4
- 时长 5分54秒（音频 354s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前边已经分析了新增用户量的统计分析逻辑,接下来咱们就是根据这个逻辑进行代码的编写,这里分析逻辑的时候咱们也分析了,这所有的操作步骤只有第三步,是和咱们之前的今日访问量是不一样的,其他步骤都是一样的,这里咱们来切到开发工具,这里咱们也准备好了咱们新增用户量的基础工程,
[00:30] 这个工程内呢,咱们已经把相同的给代码,就是重复的代码呢,给抽取了出来。
[00:36] 前半部分呢,就是接着Kafka的协议,以及咱们Redis中的变量。
[00:42] 这个变量呢,是现在使用着新的,咱们呢,是已经配置好的变量。
[00:47] 下面呢,就是手动管理Kafka的offset,以及呢,配置Kafka,配置Sparks追命来获取Kafka中的数据。
[00:57] 这些呢,都是固定的代码。
[00:59] 这里唯一不一样的话咱们就是把这个检查点修改了咱们现在是today new user咱们呢这里只用做的是就是根据用户ID进行一个新增用户量的一个获取接下来呢就是把统计结果保存到redis中redis中进行offset的管理呢也是和咱们今日这个访问量是一样的这里呢代码都直接复用了这里呢咱们
[01:28] 这边要修改的变量咱们已经修改好就是现在这些Galaxy ProID Topic Name以及Redis中的KV6都修改成了咱们新增用货量的相关数据接下来咱们对代码进行编写的时候直接就是来编写根据ID来计算的新增用货量就行了这里获取数据还是使用的Kafka Message因为咱们上面已经指定了相关的Topic
[01:56] 这里呢获取的数据呢就是新增用户的数据咱们来使用这个messager来进行根据用户ID计算用户量这个操作这里呢它由于它的一个特殊性就是这个用户ID呢是唯一的而且呢是不会重复的咱们呢直接使用Map算子把它的value给取出来取出来完成之后呢咱们计算它的值就非常简单了
[02:25] 咱们呢直接进行一个word counter就行因为呢它这个值是唯一的这个地方变量叫做x由于它这个值呢是唯一的也就是说它永远不会重复永远不会重复的话咱们就不需要对它进行一个去重不需要对它进行去重了咱们这个地方也就是技术的时候这个新的这个用户ID它肯定永远是1的它永远是1的这种情况下呢咱们
[02:55] 后边操作就没有那么麻烦了这个呢是new user这个new user呢咱们就是最终的一个结果在使用redis往这个redis保存的时候呢咱们是通过共享变量直接这个地方呢进行counter的一个技术就行了咱们呢接着往下行接着呢就是使用共享变量来保存相关的一个数据的操作这里呢其实使用共享变量来保存数据和咱们之前呢
[03:25] 也是重复的代码都是一样的这里呢咱们对照原来的代码这是使用共享变量来保存redis中的数据咱们呢把它给单过来修改一下这个地方呢使用共享变量原来是叫做uv这个地方呢就不能叫做uv了就叫new user这个地方呢是vz的data咱们呢现在是新增用户量这个地方变量也进行一个修改是叫做
[03:56] new usernew user data然后下方键其他的都是一样的就不要再做任何修改了接下来呢就是将这个统计结果呢保存到咱们的redis中这个代码呢也是一样的就是唯一不一样的就是咱们这里的变量把它给拿过来这里之前没有把它给粘过来的一个原因是啥呢就是咱们变量没有定义这个地方呢它是会报错的把这个变量给拿过来就OK了
[04:27] 拿过来之后呢这个地方因为咱们这个redis这个k还有咱们那个k-info呢已经通过咱们新定义的变量呢进行了一个指定这里呢结果直接进行相关的保存即可好以上呢就是咱们新增用户量的所有代码这里呢代码相对来说已经非常非常简单了因为咱们前边做了这个新今日房量
[04:57] 这个代码今日访问量呢相对来说是比较麻烦的因为它有一个去重操作这里新增用户量基于今日访问量呢是有大量的重复代码咱们呢重复代码像这些这一大堆都是重复代码咱们呢就没有对它进行一个编写就是直接拿来复用还有下边这一大堆都是一个重复的代码咱们唯一编写呢就是有效代码其实就这一点
[05:25] 就是根据用户ID实时的一个计算的一个新增量然后呢就是变量的一个修改就OK了好咱们来切回文档咱们呢已经基于咱们今日访问量的这个代码进行一个修改得到了咱们新增用户量的代码咱们呢在开发工具中已经准备好这里呢代码编写就到这里好视频呢也就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spark Streaming 从 Kafka 读取实时用户访问数据，并使用 Redis 存储用户访问统计结果的 Scala 代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示代码文件结构，定位到 `RealTimeNewUser.scala`，代码中定义了 SparkConf、Kafka 服务地址、Topic、Redis 连接等配置，并初始化了 SparkContext 和 StreamingContext。
画面 2：代码中设置 Spark Streaming 的检查点目录为 `/user/Hive/external/data_course/today_new_user/checkpoint`。
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
    // Kafka
    val bootstrapServers = "xc-online-Kafka:9092"
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
    ssc.checkpoint(directory = "/user/Hive/external/data_course/today_new_user/checkpoint")
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
ssc.checkpoint(directory = "/user/Hive/external/data_course/today_new_user/checkpoint")
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
ssc.checkpoint(directory = "/user/Hive/external/data_course/today_new_user/checkpoint")
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

