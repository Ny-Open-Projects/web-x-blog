# 画面线理解：11-实时分析-今日访问量-代码-测试

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\11-实时分析-今日访问量-代码-测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:32, 02:15, 03:00, 03:36, 04:31, 05:49, 06:45, 07:47, 10:40, 11:29, 12:07, 12:47, 13:38, 14:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:43:27

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spark Streaming 的实时访问量统计程序，通过 Kafka 消费数据、Redis 做状态存储，并最终将统计结果写入 Redis。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Scala 代码中 Spark Streaming 的初始化配置，包括 Kafka 服务地址、主题名、Redis 的 key 和 offset 等。
画面 2: 展示了 Spark Streaming 中对数据进行处理的代码，包括对消息进行 split、filter 和 map 操作。
画面 3: 展示了 Spark Streaming 的日志，显示了 DirectKafkaStream 初始化成功，以及 ConsumerConfig 的配置参数。
画面 4: 展示了 Redis 中的 key "todaycourse.visitoffset" 的值为 1，用于记录消费位点。
画面 5: 展示了 Spark Streaming 的日志，显示了 JobScheduler 启动了 Streaming Job，并开始处理数据。
画面 6: 展示了 Spark Streaming 的日志，显示了 Checkpoint 数据已提交到指定路径。
画面 7: 展示了代码中对 valstr 进行判断和处理的逻辑。
画面 8: 展示了 Redis 中的 key "visit_date_2017" 的值为 4，用于记录访问日期。
画面 9: 展示了代码中对状态进行更新的逻辑，以及对 "hl" 字符串的过滤。
画面 10: 展示了 Redis 中的 key "hl" 的值为 17，用于记录特定条件下的统计结果。
画面 11: 展示了 Spark Streaming 的日志，显示了 Block broadcast 和 TaskScheduler 的任务调度信息。
画面 12: 展示了 Spark Streaming 的日志，显示了 TaskScheduler 的任务执行完成。
画面 13: 展示了 Spark Streaming 的日志，显示了 Checkpoint 数据已保存到指定路径。
画面 14: 展示了 Spark Streaming 的日志，显示了 Checkpoint 数据已清除，并且程序正常结束。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
def main(args: Array[String]): Unit = {
  // Spark context
  val sc = new SparkContext(sparkConf)
  // kafka
  val bootstrapServers = "xc-online-kafka:9092"
  val groupid = "visit_topic"
  val topicname = "visit_topic"
  // redis
  val rt_cv_key = "today.course.visit:current"
  val rt_cv_offset = "today.course.visit:offset"
  // 1. 读取最后的offset (redis中保存的offset，避免重复消费)
  val redis = redis.getlastCommittedOffsets(rt_cv_offset, topicname, partitions = 4)
  // 2. Spark Streaming
  val ssc = new StreamingContext(sc, Seconds(5))
  ssc.checkpoint("/user/hive/external/data_course/today_visit_online/checkpoint")
}
```

画面 2:
```scala
val uTemp = message.map(_.value()).map(_.split(regex = "\\t"))
.filter(arr => arr.length == 7)
.map(arr => {
  (arr(0) + "+" + arr(2) + "+" + arr(3), 1)
})
```

画面 3:
```scala
metadata.max.age.m = 300000
partition.assignment.strategy = [org.apache.kafka.clients.consumer.RangeAssignor]
reconnect.backoff.ms = 100
ssl.keberos.ticket.renew.window.factor = 0.8
bootstrap.servers = [xc-online-kafka:9092]
ssl.keberos.type = 2KS
enable.auto.commit = true
```

画面 4:
```text
Key: current 216:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1
