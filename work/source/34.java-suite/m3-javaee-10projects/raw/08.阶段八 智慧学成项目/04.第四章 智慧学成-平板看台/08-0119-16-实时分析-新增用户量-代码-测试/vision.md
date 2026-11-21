# 画面线理解：16-实时分析-新增用户量-代码-测试

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\16-实时分析-新增用户量-代码-测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:54, 01:03, 01:14, 01:28, 01:35, 01:47, 02:18, 02:30, 02:38, 03:15, 03:31, 03:38, 04:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:47:19

1) 这一组画面整体在讲如何通过 NIFI 实时采集 MySQL 数据并写入 Kafka，再由 Spark Streaming 消费 Kafka 数据并写入 Redis，最终通过 RedisView 监控实时数据。

2) 按时间顺序列出每张画面的要点：
画面1：展示在线学习平台的首页，包含课程推荐（如 ThinkPHP 5.0、Angular 2 等），但未显示具体课程内容。
画面2：展示 NIFI 流程图，包含 CaptureChangeMySQL、Insert、Kafka、Redis 等组件，用于演示数据从 MySQL 到 Kafka 再到 Redis 的流转。
画面3：展示 Scala 代码，用于创建 Spark Streaming 上下文并配置 Kafka 消费者。
画面4：展示 Navicat Premium 中的 SQL 语句，用于向 MySQL 的 xc_user 表插入数据。
画面5：展示 IDEA 中的终端日志，显示 Spark Streaming 程序启动并进行 checkpoint 操作。
画面6：展示 Navicat Premium 中的 SQL 语句，用于向 MySQL 的 xc_user 表插入数据。
画面7：展示 Navicat Premium 中的 SQL 语句，用于向 MySQL 的 xc_user 表插入数据。
画面8：展示 RedisView Community 界面，显示实时数据（如 todaynew_usercurrent 为 21）。
画面9：展示 IDEA 中的终端日志，显示 Spark Streaming 程序进行 checkpoint 操作。
画面10：展示 IDEA 中的 Scala 代码，用于处理 Kafka 消费者数据并写入 Redis。
画面11：展示 RedisView Community 界面，显示实时数据（如 todaynew_usercurrent 为 21）。
画面12：展示 IDEA 中的 Scala 代码，用于处理 Kafka 消费者数据并写入 Redis。
画面13：展示 IDEA 中的终端日志，显示 Spark Streaming 程序进行 checkpoint 操作。
画面14：展示 PPT 页面，标题为“3.3.3 测试”，内容包括“手动在mysql中插入数据”和“redis查看数据SQL如下”，并附有 SQL 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```scala
def main(args: Array[String]): Unit = {
  // Spark context
  val sc = new SparkContext(sparkConf)
  // kafka
  val bootstrapServers = "xc-online-kafka:9092"
  val groupid = "new_user"
  val topicname = "new_user"
  val rt_cv_key = "today:new_user:current"
  val rt_cv_offset = "today:new_user:offset"
  // redis
  val redis = new RedisUtils
  redis.initRedisPool(1)
  // 1. 手动在mysql中插入数据（在redis中没有初始值）
  val offsets = redis.getLatestCommittedOffsets(rt_cv_offset, topicname, parBions = 1)
  // 2. Spark Streaming 消费Kafka中用户行为数据，每秒消费一次
  val ssc = new StreamingContext(sc, Seconds(1))
  ssc.checkpoint("/user/hive/external/data_course/today_new_user/checkpoint")
  val kafkaParam = Map[String, Object](
    "bootstrap.servers" -> bootstrapServers,
    "group.id" -> groupid,
    "key.deserializer" -> classOf[StringDeserializer],
    "value.deserializer" -> classOf[StringDeserializer],
    "auto.offset.reset" -> "earliest",
    "enable.auto.commit" -> (false: java.lang.Boolean)
  )
```

画面4：
```sql
INSERT INTO `xc_user`(`id`, `username`, `password`, `salt`, `name`, `userpic`, `utype`, `birthday`, `sex`, `email`, `phone`, `qq`, `ip`, `status`, `create_time`, `update_time`, `last_password_reset_date`) VALUES ('0005dccc3e2341d0b0b0e909e8c0', 'Fcg830521ff4f4fbcb0e998b99a', 'Tyvm', NULL, NULL, '101001', NULL, NULL, NULL, '158.222.112.75', '3', '2019-08-11 18:44:04', NULL, NULL);
```

画面14：
```sql
INSERT INTO `xc_user`(`id`, `username`, `password`, `salt`, `name`, `userpic`, `utype`, `birthday`, `sex`, `email`, `phone`, `qq`, `ip`, `status`, `create_time`, `update_time`, `last_password_reset_date`) VALUES ('0005dccc3e2341d0b0b0e909e8c0', 'Fcg830521ff4f4fbcb0e998b99a', 'Tyvm', NULL, NULL, '101001', NULL, NULL, NULL, '158.222.112.75', '3', '2019-08-11 18:44:04', NULL, NULL);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：PPT 标题为“3.3.3 测试”，内容包括“手动在mysql中插入数据”和“redis查看数据SQL如下”，并附有 SQL 语句。

5) 不要评价画面美观，不要输出与课程无关的内容。
