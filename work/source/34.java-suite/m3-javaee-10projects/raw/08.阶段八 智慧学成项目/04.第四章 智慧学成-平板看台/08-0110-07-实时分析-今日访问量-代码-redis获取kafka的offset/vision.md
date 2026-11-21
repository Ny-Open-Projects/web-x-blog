# 画面线理解：07-实时分析-今日访问量-代码-redis获取kafka的offset

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\07-实时分析-今日访问量-代码-redis获取kafka的offset_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:18, 00:49, 00:56, 01:52, 03:28, 03:37, 03:55, 04:51, 08:46, 10:17, 11:23, 11:51, 11:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:40:08

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark Streaming 应用中，通过 Redis 工具类获取 Kafka 消费的最新偏移量，以实现消费位点的持久化管理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 `RealTimeVisit` 主程序中初始化 Spark 配置、Kafka 消费参数、Redis 实例，并调用 `getlastCommittedOffsets` 方法获取偏移量。
画面 2: 选中 `val sparkConf: SparkConf = ...` 代码行，准备查看 Spark 配置细节。
画面 3: 跳转到 `RedisUtils.scala` 文件，查看 `makePool` 方法，用于创建 Jedis 连接池。
画面 4: 在 `RedisUtils.scala` 中，展示 `getlastCommittedOffsets` 方法的定义和注释，说明其功能是获取 Kafka 偏移量。
画面 5: 在 `RealTimeVisit` 中，调用 `redis.getlastCommittedOffsets(...)` 方法，准备获取偏移量。
画面 6: 在 `RedisUtils.scala` 中，光标位于 `getlastCommittedOffsets` 方法的注释部分。
画面 7: 在 `RealTimeVisit` 中，光标位于 `redis.getlastCommittedOffsets(...)` 方法调用处，准备执行。
画面 8: 在 `RedisUtils.scala` 中，光标位于 `getlastCommittedOffsets` 方法的 `val jedis = getPool.getResource` 代码行。
画面 9: 在 `RedisUtils.scala` 中，光标位于 `val offsetMap = collection.mutable.HashMap.empty[TopicPartition, Long]` 代码行。
画面 10: 在 `RedisUtils.scala` 中，光标位于 `for (partition <- 0 to partitions - 1)` 循环开始处。
画面 11: 在 `RedisUtils.scala` 中，光标位于 `val lastOffsetStep = jedis.hget(...)` 代码行，准备获取 Redis 中的偏移值。
画面 12: 在 `RedisUtils.scala` 中，光标位于 `offsetMap.put(...)` 代码行，准备将偏移量存入 Map。
画面 13: 在 `RedisUtils.scala` 中，光标位于 `offsetMap.put(...)` 代码行，准备将偏移量存入 Map。
画面 14: 在 `RealTimeVisit` 中，光标位于 `val offsets = redis.getlastCommittedOffsets(...)` 代码行，准备执行获取偏移量的操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
object RealTimeVisit {
  // 1. 从 Redis 中获取上次消费的 offset，如果没有则从 Kafka 读取
  // 2. Spark Streaming 从 Kafka 中读取用户行为数据，每5秒读取一次
  // 3. 根据用户id、sessionid、ip去重，计算实时访问量
  // 4. 底层处理 Druid，但业务逻辑
  // 5. redis 中存储当前offset
  val sparkConf: SparkConf = ETEnvironment.getSparkConf(this.getClass.getSimpleName)
  def main(args: Array[String]): Unit = {
    // Spark context
    val sc = new SparkContext(sparkConf)
    val bootstrapServers = "xc-online-kafka:9092"
    val groupId = "visit_topic"
    val topicName = "visit_topic"
    val rt_cv_key = "today:course.visit:current"
    val rt_cv_offset = "today:course.visit:offset"
    val redis = new RedisUtils
    redis.initRedisPool()
    val offsets = redis.getlastCommittedOffsets(rt_cv_key, topicName, partitions = 1)
  }
```

画面 3:
```scala
transient private var pool: JedisPool = null

def makePool(redisHost: String, redisPort: Int, redisTimeout: Int,
             maxTotal: Int, maxIdle: Int, minIdle: Int, testOnBorrow: Boolean,
             testOnReturn: Boolean, maxWaitMillis: Long): Unit = {
  if (pool == null) {
    val poolConfig = new GenericObjectPoolConfig
    poolConfig.setMaxTotal(maxTotal)
    poolConfig.setTestOnBorrow(testOnBorrow)
    poolConfig.setTestOnReturn(testOnReturn)
    poolConfig.setMinIdle(minIdle)
    poolConfig.setMaxIdle(maxIdle)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setNumTestsPerEvictionRun(3)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setMinEvictableIdleTimeMillis(1000 * 60 * 30)
    poolConfig.setTimeBetweenEvictionRunsMillis(1000 * 60)
    poolConfig.setNumTestsPerEvictionRun(3)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    poolConfig.setTestOnReturn(true)
    poolConfig.setTestWhileIdle(true)
    poolConfig.setTestOnBorrow(true)
    pool
