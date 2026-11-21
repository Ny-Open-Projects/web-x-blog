# 20-实时分析-今日购买量-代码-测试

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\20-实时分析-今日购买量-代码-测试_【海量资源尽在 666java.com】.mp4
- 时长 2分47秒（音频 167s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续前边已经基于新增用户量的一个代码修改得到了咱们今日购买量的代码接下来就是对咱们今日购买量统计分析的代码进行测试通过本节咱们来测试这个代码来验证代码的一个准确性来看测试步骤首先是启动咱们这个客户购买量MySQL2 Kafka的实时产机这里在Kafaka上面
[00:29] 在这个内发上面已经启动好了第二手动在买测课中插入订单数据这里呢咱们使用这个内部看的这个工具往订单中插入数据第三呢就是在代码在开发工具中运行代码运行代码呢他监控到这个结果呢就会进行一个实时的统计分析统计分析的结果呢是保存到redis中这里呢咱们使用redis的工具进行一个结果的一个查看好咱们呢
[01:02] 先来插入一条数据咱们前面已经插入了一条数据了这里呢也是测试数据咱们呢只用把这个ID给修改一下就行了然后呢接下来进行一个测试这个地方显示呢已经插入成功插入成功之后呢咱们来运行咱们这个代码这是咱们今日购买量这个代码运行成功之后呢这个地方还会出现两组K就是咱们今日购买量的
[01:33] offset以及呢他当前的一个值这里呢还没有出现咱们来看日志好这里呢日志已经刷新了咱们来刷新这里的键这里呢已经出现了costbuy以及呢costbuy的offset他这个地方呢显示有两个什么呀两个订单的记录咱们是不是刚刚刚是不是手动插入了有两条数据啊这里咱们再插入一条数据我再多删几个
[02:05] 把这个ID给粘过来然后再次运行好已经显示X2成功了显示X2成功咱们来刷新这里好已经变成三个了offset呢这个地方也可以也可以看到它呢也有相当一个改变咱们来切回温暖通过咱们呢对代码的一个测试按照这个流程呢对代码的一个测试已经验证了咱们这个代码呢是没有问题的
[02:32] 它那个可以实时分析并且呢把结果呢实时的保存到redis中好咱们这里今日购买量的统计分析代码测试就到这里视频呢也听下来了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
    val bootstrapServers = "xc-online-Kafka:9092"
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
    val bootstrapServers = "xc-online-Kafka:9092"
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

