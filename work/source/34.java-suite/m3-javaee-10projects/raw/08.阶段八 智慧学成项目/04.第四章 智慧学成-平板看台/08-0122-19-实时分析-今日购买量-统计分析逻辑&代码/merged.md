# 19-实时分析-今日购买量-统计分析逻辑&代码

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\19-实时分析-今日购买量-统计分析逻辑&代码_【海量资源尽在 666java.com】.mp4
- 时长 7分35秒（音频 456s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续前边已经使用NiFi采集了咱们今日购买量所需要的订单数据接下来就是统计分析代码的编写在代码编写之前咱们需要理解一下统计分析的逻辑这里由于今日购买量和咱们前面的新增用户量它这个采集是一样的都是采集的MySQL数据它这个地方根据
[00:28] 计算的时候就是计算这个购买量的时候前边呢是根据用户ID这里呢是基于订单ID他们呢都有一个相同的特点都是这个ID是唯一的也就是说这个地方实时计算的时候是一样的剩下的步骤呢也是一模一样的也就是说咱们只要写了咱们的新增用户量的代码之后咱们今日购买量的代码是非常非常的简单了
[00:56] 通过本节的学习呢咱们需要理解咱们统计分析的逻辑然后呢还能够编写出来统计分析的代码咱们呢再把逻辑给过一遍第一手动管理Kafka的offset这里呢手动管理Kafka的offset呢是使用redis咱们呢在今日访问量那个阶段呢已经编写了这个代码进行手动的一个维护第二
[01:25] Spark Streaming然后获取Kafka的中的一个用户行为数据这个数据呢就是这里的用户行为数据呢就是指用户的一个订单数据咱们呢使用Spark Streaming来获取由于是手动管理Offset的这里呢是通过Redis中的Offset来获取Kafka的数据第三根据订单ID实时计算今日的购买量这里呢由于订单ID的唯一性
[01:54] 实时计算他的购买量直接执行word count即可接下来就是将统计结果保存到redis中这里保存到redis中主要是供咱们业务使用由于是实时统计这里保存到redis中也可以进行一个实时的查看第五redis中保存当时的一个offset进度咱们Spark streaming读取完Kafka中的数据之后通过
[02:23] 统计咱们的统计分析最终呢将结果保存到redis只要这个过程中没有出现问题就说明这个每5秒读取这个数据呢即是处理成功的处理成功的情况下呢咱们需要更新redis中的offset这里呢就是保存当前的这个offset以上呢就是咱们统计分析的逻辑和咱们前面金融购买量和那个新通用货量的逻辑是一模一样的接下来呢就是代码的变形
[02:53] 咱们来切到开发工具前面已经说了咱们代码和咱们新增用户这个代码是一模一样的只用修改几个变量就行了你只要编写了新增用户量的代码咱们这里的今日购买量的代码那就非常简单了咱们来把这个给复制一下这个咱们是新增这个是今日购买量就叫BY把它给复制一下
[03:25] 这个时候保持这个名字是唯一的咱们首先来改一个注释这里是今日更改良由于它的步骤是一样的而且它这个地方实时统计的时候它这个逻辑也是一样的只用执行一个word counter即可咱们先进行变量的修改这里咱们Galaxy Pro X1就是Kafka中的Galaxy Pro X1还有topic name就需要改变了
[04:01] 咱们这里是课程购买量就叫CostBuy复制一下接下来是Redis中的K这里也是把它改成CostBuy好改完成之后咱们还有一个地方要改就是咱们的检查点这个地方也是TodayCostBuy修改一下这个修改完成之后咱们其实需要使用的变量就剩两个了
[04:37] 就是咱们共享变量还有redis的一个字段这两个修改完成就是咱们变量相关的修改就完成了这个呢咱们也叫cosby这个呢把b改成大写这个就不是new user了咱们就是cosby data了cosby data好到此呢咱们这个变量呢也就基本上修改完了修改完了之后呢但是为了有一点叫什么呀见名之意
[05:09] 咱们呢还得再修改一个地方这个地方呢还叫什么呢还叫new user呢咱们呢为了见名之意就把它改成castby改成castby之后下边呢也需要一个修改这个也改完之后咱们这个代码就算完成了咱们这个代码就算完成了完成之后呢咱们把注释看一下这是根据用户ID实时计算新增用户量把注释也修改一下这个呢是根据订单ID
[05:43] 定单根据定案定的案例实时的计算今日购买量看一下还有别的地方要进行修改吗这是共享变量的这是读取卡普卡中的数据这是相关的配置OK到此呢咱们今日购买量的代码呢基于咱们新增用户量的代码只修改了相关的变量修改完成之后呢咱们这里代码就完成了
[06:16] 本节视频的主要内容就是对咱们统计分析的逻辑进行一个概述理解统计分析的逻辑即可接下来对统计分析的代码进行了一个修改这里是基于咱们心中用户量这个代码进行修改的因为它的重合度实在是太高了基本上是99%的一个重合咱们只改了几个变量名就是把咱们Kafka的协议
[06:45] 需要使用的Galaxy P9 Topic Name给改了Redis中呢保存的K也修改了这里呢读取数据的时候它就去这个今日购买量这个Topic去读取数据保存呢也是保存到今日购买量这个Redis中这里呢检查点也做了一个相应的修改就是说咱们这个地方是今天的购买量这个检查点这个目楼下面的检查点还有咱们
[07:14] redis中的哈希字段这里呢是通过日期动态生成的前置字段也修了修改一下这个地方呢为了见名之义咱们呢也把这个变量就是今日购买量这个计算这个变量也修改了修改完成之后呢咱们这个代码就算回了好视频呢也就到这里就停下来了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
sc.checkpoint(directory = "/user/Hive/external/data_course/today_new_user/checkpoint")
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
val bootstrapServers = "xc-online-Kafka:9092"
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

