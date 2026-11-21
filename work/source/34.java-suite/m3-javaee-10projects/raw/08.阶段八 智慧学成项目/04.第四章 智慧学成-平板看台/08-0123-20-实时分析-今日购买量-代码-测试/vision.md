# 画面线理解：20-实时分析-今日购买量-代码-测试

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\20-实时分析-今日购买量-代码-测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:28, 00:44, 00:50, 01:02, 01:17, 01:23, 01:28, 01:37, 01:42, 01:46, 02:00, 02:21, 02:32, 02:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:50:37

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Python 脚本生成模拟订单数据，写入 MySQL，再由 Spark Streaming 读取并处理后写入 Redis，最终通过 RedisView 工具查看结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程文档目录，定位到“4.3.1 生产数据脚本”章节，介绍后续操作步骤。
画面 2: 鼠标光标移动，准备进入代码编辑环境。
画面 3: 在 IDEA 中打开项目结构，展示 `RealTimeBuy` 模块下的 `RealTimeNewUser.scala` 文件。
画面 4: 在 IDEA 中打开 `RealTimeBuy.scala` 文件，显示 Spark Streaming 代码，用于读取 Kafka 数据并写入 Redis。
画面 5: 在 IDEA 中打开 `RealTimeBuy.scala` 文件，显示 Spark Streaming 代码，用于读取 Kafka 数据并写入 Redis。
画面 6: 在 IDEA 中打开 `RealTimeBuy.scala` 文件，显示 Spark Streaming 代码，用于读取 Kafka 数据并写入 Redis。
画面 7: 在 RedisView 工具中，查看 `x-online` 数据库下的 `todaycourse_visitoffset` 键，其 `visit_date_201_` 字段值为 100。
画面 8: 在 RedisView 工具中，查看 `x-online` 数据库下的 `todaycourse_visitoffset` 键，其 `visit_date_201_` 字段值变为 25。
画面 9: 在 IDEA 的终端中，显示 Spark Streaming 作业已成功启动并开始处理数据。
画面 10: 在 RedisView 工具中，查看 `x-online` 数据库下的 `todaycourse_visitoffset` 键，其 `visit_date_201_` 字段值变为 3。
画面 11: 在 Navicat 中，执行 SQL 语句向 `xc_order` 表插入一条新订单数据。
画面 12: 在 RedisView 工具中，查看 `x-online` 数据库下的 `todaycourse_visitoffset` 键，其 `visit_date_201_` 字段值变为 3。
画面 13: 在 IDEA 的终端中，显示 Spark Streaming 作业正在处理数据，日志显示 checkpoint 和数据流状态。
画面 14: 返回课程文档目录，再次展示“4.3.1 生产数据脚本”章节。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```scala
val accumulator = sc.longAccumulator(name = "courseBuy")
val keyInfo = "course_buy_date" + getTimestamp(new Date()).getYear + "_" + "yyyy-MM-dd"
val value = redis.getResultsRedis(rt_cv_key, keyInfo)
if (null != valueStr) {
  accumulator.add(valueStr.toLong)
}
```

画面 4:
```scala
val accumulator = sc.longAccumulator(name = "courseBuy")
val keyInfo = "course_buy_date" + getTimestamp(new Date()).getYear + "_" + "yyyy-MM-dd"
val valueStr = redis.getResultsRedis(rt_cv_key, keyInfo)
if (null != valueStr) {
  accumulator.add(valueStr.toLong)
}
```

画面 5:
```scala
object RealTimeBuy {
  def main(args: Array[String]): Unit = {
    // 初始化 SparkContext
    val sc = new SparkContext(sparkConf)
    // 初始化 Kafka 消费者
    val bootstrapServers = "xc-online-kafka:9092"
    val groupId = "course_buy"
    val topicName = "course_buy"
    val rt_cv_key = "todaycourse_buy:current"
    val rt_cv_offset = "Today:course_buy:offset"
    // 初始化 Redis 客户端
    val redis = new RedisUtils
    redis.initRedisClient()
    val offsets = redis.getLatestCommittedOffsets(rt_cv_offset, topicName, partitions = 1)
  }
}
```

画面 6:
```scala
object RealTimeBuy {
  def main(args: Array[String]): Unit = {
    // 初始化 SparkContext
    val sc = new SparkContext(sparkConf)
    // 初始化 Kafka 消费者
    val bootstrapServers = "xc-online-kafka:9092"
    val groupId = "course_buy"
    val topicName = "course_buy"
    val rt_cv_key = "todaycourse_buy:current"
    val rt_cv_offset = "Today:course_buy:offset"
    // 初始化 Redis 客户端
    val redis = new RedisUtils
    redis.initRedisClient()
    val offsets = redis.getLatestCommittedOffsets(rt_cv_offset, topicName, partitions = 1)
  }
}
```

画面 7:
```sql
INSERT INTO `xc_order` (`order_number`, `initial_price`, `price`, `start_time`, `end_time`, `status`, `user_id`, `details`, `old_status`) VALUES ('0004208902c0dc15b97c74680937e', '100.00', '100.00', '2019-10-03 00:00:00', '2019-10-03 00:00:00', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
