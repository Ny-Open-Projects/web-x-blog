# 10-实时分析-今日访问量-代码-redis中保存当前offset进度

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\10-实时分析-今日访问量-代码-redis中保存当前offset进度_【海量资源尽在 666java.com】.mp4
- 时长 12分41秒（音频 762s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好咱们继续前边呢就是将统计结果保存到redis供业务使用呢咱们在写咱们的根据客户ID进行去重就是根据客户ID三线ID进行去重的时候这个地方呢一共就是一并已经写了这个时候呢咱们把这个注释给移到上面来聚合然后复制这里呢就是redis复制就是帮把这个结果保存到redis中
[00:29] 供咱们业务使用这里呢写完之后咱们接下来就是将咱们的新的offset保存到release中这里呢release中咱们还有一个方法是没有实现的就是存储新的offset这里呢咱们来编写存储新的offset代码这里呢是存储新的offset要需要使用到message这个message呢是咱们Kafka的
[00:58] 用的这个流数据这里呢使用它的一个follow each它的一个rdd对它这个rdd进行一个便利操作也就是说你这里边有多少的一个数据我呢就把它给全部拿过来这个rdd呢就代表你有多少多少个数据这里呢rdd这个rdd呢是可以直接获取到它的分区操作的或者获取到它这个相关分区的一个数据的
[01:27] 这里呢咱们使用 as instance off 这个方法这个方法呢它里边有一个heizheiz offheiz off set range这个呢它可以获取到offset的一个range它这个变量就是获取的是当前这个offset的这个变量是多少获取到当前的offset之后呢咱们还要判断一件事就是说你这个 RDD 是否是空的
[01:59] 如果你这个RDD是空的我接下来这个就没有必要进行一个新的便利了因为你这个RDD是没有数据的咱们来进行一个盘子这里呢这个RDD它不能是空的isimpleted它不为空的情况下呢咱们就可以对这个runge进行一个操作了这里呢咱们对它进行一个for each对它for each的时候呢就可以得到它每一个一个offset
[02:31] 这里呢就是offset urgence把这个s给去掉对它进行相应的操作这个时候呢你就可以得到相对应的分区咱们呢在数据保存的时候呢是分区名加上咱们的咱们的topic name加上咱们的分区名根据咱们的分区名呢进行相应的保存这里呢咱们首先将咱们的topic pardon k给topic pardon k给
[03:05] 保存过来就是给组装出来这里呢topic pattern k这个变量还采用这个把这个之前咱们保存那个变量给加过来它呢就是等于你当前这个分区的topic name这就是topic name加上一个下滑线将呃用作拼接接下来呢就是它的partner这个partner呢就是它的一个分区
[03:31] 这个k有了之后呢咱们就对它进行一个redis的一个保存操作咱们这里使用的是stopoffsetk呢还是咱们原来的k上头就是上面redis中卡不卡的offsetk把这个变量呢给拿过来接下来呢是它的字段字段呢就是topicpartnk接下来是具体的值这里呢具体的值就是它的utiloffset
[04:04] 这个变量用错了我说怎么点不出来呢怎么应该是他unitl offset这个呢就是他当前的offset这里咱们来加个注释其实这个呢可以放到这个if里边提高它这个效率看它DD是否有值加完注释呢咱们来实现这个方法把这个给取消掉
[04:41] 是否有值这里呢获取分区获取分区这里呢根据分区进行便利便利分区便利分区完成之后呢这里是获取分区的相关信息组装获取分区相关值这里呢获取分区相关值完了之后呢组装自端名组装哈希
[05:32] 组装完哈希的字段值之后呢咱们就是进行保存进行保存这里呢咱们保存redis的offset这个地方咱们是根据这里的分区进行一个保存的就是咱们的咱们的这个我找一下这个变量last offsetoffset在这里
[06:06] 是根据topic的name加上咱们的分区的值进行一个保存的这里呢咱们把这个功能给实现一下把这个先给删掉咱们呢首先是这边的这个k这个k呢这个地方保存的时候嗯需要说一点就是说它可能redis呢可能会有一个什么呀保存成功的一种情况或者是有一种保存室外的这种情况就是为了防止这种意外的一个发生咱们这个地方呢
[06:41] 使用 GDIS 的这个事务来进行相关的一个保存开始呢还是和上面一样首先呢来获取这个 GDIS获取完成 GDIS 之后呢咱们使用 GDIS 来开启这个事务这里呢开启事务是使用 PIPLAN 的它呢是可以得到一个事务的一个操作它呢就叫 PPL1.2 就行得到它了之后呢咱们使用它来开启事务
[07:14] 这里呢他MATI MU LITIN这个呢就是开启事物开启事物之后呢咱们用ppl进行值的保存咱们呢是hc这里就用hset进行保存k呢就是这里的k咱们的字段呢就是k info具体的值呢就是这个value这个value呢是一个lang类型的lang类型呢不能直接保存咱们需要把它转成一个string类型的
[07:45] 对这个地方获取到它的一个浪类型的可以看到这个是一个浪类型的把它转换成死性之后呢就可以保存这个地方呢保存成功咱们进行一个提交事务就是exec然后呢把咱们这个pplppl呢把它给关掉先把它给同步同步完成之后呢它会自动关掉咱们呢再把gdx的给连接给关掉这个呢把注射给加一下
[08:16] 这个呢是使用这个是开启事物保存这个是这两个操作呢是提交事物提交事物完成之后呢这个是关流关流完成之后呢咱们这个保存操作就算完成了这个地方呢咱们第五步就算完成了第五步完成之后呢咱们的Spark Streaming这个地方呢还要对它进行一个启动
[09:01] Spark streaming这个地方starstar完成之后呢这个地方还不算完咱们呢还要把它给等待它这个结束等待结束呢是使用这个方法注视加一下这里呢是启动这个呢等待结束其实呢就是一个阻塞操作因为咱们上面是每5秒读起一下数据除非你手动把这个程序给停了
[09:36] 不然的话它就是一直在执行咱们来自上向下检查一下代码获取协议相关的信息获取Spark Context配置基础信息然后获取OffsetSpark的数据像Spark Kafka的相关的参数这是Spark StreamingKafka的相关参数然后使用相关参数获取Kafka中的数据然后进行一个去重去重完成之后是技术的操作
[10:06] 并且使用共享变量来保存咱们的相关数据最终把咱们统计后的数据放到redis中接着咱们在redis中又保存咱们当前offset的进度OK接着启动咱们的Spark streaming这个地方还少了一步就是加一个检查点这个地方ssc因为咱们Kafka是一直在读数据
[10:36] 加这个检查点呢就是保存原来的数据保存原来的这个数据呢方便咱们这个啥呀方便咱们后边那个去虫啊等等的一个操作而且你这个程序停了之后呢你这个检查点只要还在你下次启动的时候它会读取检查点的数据这个呢咱们是保存到咱们的HDFS上咱们来切到HUE这个呢已经在HDFS上呢创建了一个目录这个目录呢就是咱们保存
[11:07] 今日访问量的这个目录相同的咱们后面就是用户新增用户量以及还有咱们的课程购买量都会有一个检查点的目录这里呢就是咱们访问量检查点的位置增加检查点S检查点保存历史保存数据这个检查点不是保存数据是共享数据
[11:45] 共享数据就是共享咱们通过一次一次的清洗在这个地方就是你每次读的数据都通过检查点进行一个共享这里呢进行通过这个函数进行计算的时候就可以拿到历史的数据拿到历史数据呢拿到之后咱们这个地方就可以对它进行一个相关的counter的一个操作counter的操作是在这个地方进行一个相关的一个操作相关的counter操作
[12:17] 好咱们呢课程访问量就是实时分析的代码就写到这里咱们呢这节的主要内容就是保存redis中保存offset的进度好通过本节的学习呢需要掌握redis中保存offset的一个进度的一个代码的一个编写视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  Spark,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

画面 10:
```scala
val message = KafkaUtils.createDirectStream[String, String](
  Spark,
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
  Spark,
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

