# 画面线理解：09-实时分析-今日访问量-代码-去重计算实时访问量&保存redis

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\09-实时分析-今日访问量-代码-去重计算实时访问量&保存redis_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:59, 01:13, 01:31, 02:07, 04:17, 05:42, 07:31, 11:33, 14:12, 15:28, 16:00, 17:15, 18:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:41:30

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Scala 中使用 Spark Streaming 处理实时数据流，并将处理结果写入 Redis。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 `RealTimeVisit.scala` 文件中 Spark Streaming 的初始化配置，包括设置反序列化器和消费者策略。
画面 2: 展示了 ETL 学习资料中的数据表结构，包含 `course_id`, `time_dim_id`, `session_id`, `client_ip`, `user_id`, `user_agent`, `visit_time` 等字段及其说明和示例。
画面 3: 与画面 2 内容相同，为数据表结构的重复展示。
画面 4: 展示了对消息进行 `map` 和 `split` 操作的代码，用于将字符串消息按换行符分割。
画面 5: 展示了 `map` 操作后的代码，准备进行状态管理。
画面 6: 展示了 `mapWithState` 方法的定义，用于处理带有状态的流数据。
画面 7: 展示了 `mapWithState` 方法的实现，包含状态的初始化和更新逻辑。
画面 8: 展示了 `mapWithState` 方法中状态更新的代码，计算单词和计数的总和。
画面 9: 展示了 `mapWithState` 方法中状态更新的代码，定义了 `accumulator` 用于累加计数。
画面 10: 展示了 `mapWithState` 方法中状态更新的代码，获取 Redis 中的 keyInfo。
画面 11: 展示了 `mapWithState` 方法中状态更新的代码，定义了 `accumulator` 的类型和初始化。
画面 12: 展示了 `mapWithState` 方法中状态更新的代码，使用 `foreachRDD` 遍历数据并写入 Redis。
画面 13: 展示了 `mapWithState` 方法中状态更新的代码，写入 Redis 的具体实现。
画面 14: 展示了 `mapWithState` 方法中状态更新的代码，完成写入 Redis 的操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer],
ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer]
val message = KafkaUtils.createDirectStream[String, String](
  // Spark Streaming
  ssc,
  // 指定一致性配置
  LocationStrategies.PreferConsistent,
  // kafka参数
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParams, offsets)
)
```

画面 4:
```scala
message.map(_).map(_.split(regexp = "\t")).map(arr => {
```

画面 5:
```scala
message.map(_).map(_.split(regexp = "\t")).map(arr => {
```

画面 6:
```scala
val mapWithStateMethod = (word: String, count: Option[Int], state: State[Int]) => {
```

画面 7:
```scala
val mapWithStateMethod = (word: String, count: Option[Int], state: State[Int]) => {
  val sum = count.getOrElse(0) + state.getOption().getOrElse(0)
  state.update(sum)
  (word, sum)
}
```

画面 8:
```scala
val sum = count.getOrElse(0) + state.getOption().getOrElse(0)
state.update(sum)
(word, sum)
```

画面 9:
```scala
val uvTemp = uvTemp.mapWithState(StateSpec.function(mapWithStateMethod))
val accumulator = sc.longAccumulator(name = "uv")
```

画面 10:
```scala
val keyInfo = "visit_date" + getDateTime(new Date()).getTime(), pattern = "yyyy-MM-dd"
val valStr = redis.getResultRedis(rt_cv_key, keyInfo)
if (null != valStr) {
  accumulator.add(valStr.toLong)
}
```

画面 11:
```scala
val uvTemp = uvTemp.mapWithState(StateSpec.function(mapWithStateMethod))
val accumulator = sc.longAccumulator(name = "uv")
```

画面 12:
```scala
uv.foreachRDD(iter => {
  if (iter.count() > 0) {
    accumulator.add(iter.count())
  }
  redis.storeResultRedis(rt_cv_key, keyInfo, accumulator.value.toString)
})
```

画面 13:
```scala
uv.foreachRDD(iter => {
  if (iter.count() > 0) {
    accumulator.add(iter.count())
  }
  redis.storeResultRedis(rt_cv_key, keyInfo, accumulator.value.toString)
})
```

画面 14:
```scala
uv.foreachRDD(iter => {
  if (iter.count() > 0) {
    accumulator.add(iter.count())
  }
  redis.storeResultRedis(rt_cv_key, keyInfo, accumulator.value.toString)
})
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2 和 3: 展示了 ETL 学习资料中的数据表结构，包含字段、说明和示例。
画面 2 表格数据：
| 采集字段 | 字段说明 | 数据格式 | 数据样例 |
| --- | --- | --- | --- |
| course_id | 课程id，根据课程id可以做更多的分析，如课程热门程度等 | uuid | e60f96225a9046d5b7d572d168d98d14 |
| time_dim_id | 时间维度，根据用户访问时间计算出来 | YYYY-MM-dd HH | 2017-11-15-09 |
| session_id | 会话id，每打开一个页面就会产生一个会话id，关闭浏览器消失，用于去重 | uuid | 0b26410f5b1e49c8131789d14eb254 |
| client_ip | 用户ip，用于去重 | ipv4 | 129.39.209.149 |
| user_id | 用户id，根据是否有值，可判断是否为登陆用户 | uuid | 311e3a9f39644504a059fb6e7c57743 |
| user_agent | 浏览器标识，可判断用户访问方式及是否是机器人 | 浏览器ua | Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36 |
| visit_time | 用户访问时间，可根据访问时间计算时间维度，确认用户访问的具休时间 | 时间戳 | 1510708629 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
