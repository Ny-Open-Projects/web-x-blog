# 16-实时分析-新增用户量-代码-测试

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\16-实时分析-新增用户量-代码-测试_【海量资源尽在 666java.com】.mp4
- 时长 4分6秒（音频 246s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前边呢,咱们已经编写了新综用货量的统计分析代码,接下来呢,就是对代码进行测试,咱们的测试步骤如下,首先呢,是在NetFi中启动咱们新综用货量的实时采集,这里呢,是已经采集好,已经启动好的,接下来呢,是运行代码,这里呢,开发工具的代码还没有运行,咱们呢,等会儿需要把它给运行起来,第三步呢,就是手动的mySQL中插入数据,这个呢,
[00:31] 因为咱们是实时采集只有MySQL有新增数据的时候你才可以进行把这个数据给采集到咱们呢就是采用手动的方式来新增数据新增完数据之后呢通过实时的一个计算咱们呢就可以在Redis中进行查看一个结果好咱们呢第一步就是Netflix上的一个处理器呢现在是启动好的咱们呢不用管它让它继续运行这个接下来呢是在开发工具中运行代码
[01:00] 咱们来切到开发工具这里呢直接运行即可他正在打包这里呢打包需要一个过程咱们呢之前测试的时候已经测试了一个插入的一个代码咱们呢在咱们的文档中也准备了一条插入语句咱们来使用这个这里呢可以看到他已经在读取这个checkpoint了就是咱们的检查点就说明了他已经启动OK
[01:34] 咱们来新增用户走起这里呢已经是新增成功了一个咱们来看卡普卡读到没咱们来看采集读到没采集呢已经读到了而且放到卡普卡中这个时候呢咱们来烧心redis咱们原来呢只有两个k咱们呢现在应该变成四个k就是有了新增用户new user这是他的一个当前的一个值这个呢是当前他的offset这个为什么现在是21呢
[02:03] 是因为咱们之前有一个历史数据就是咱们在测试采集的时候他呢把一个数据呢一部分数据呢已经放到Kafka中了放到Kafka中呢之后呢他就读取了这个数据呢就把它实时的给计算了出来这里因为是Kafka有历史数据然后呢他就把它给第一次计算的时候就拿到了咱们接下来呢接着进行一个新增咱们在编写代码的时候这个地方就是代码说这个写的非常简单
[02:32] 主要原因是新增用户量的一个特点就是说ID永远是唯一的咱们来开始试一下不唯一的ID咱们来查看能不能保存到数据库这个地方它告诉你报了一个错是主件这个地方说重复咱们把主件给稍微修改一下删除一颗删除一个字段接下来它又报了一个
[02:59] user nameuser name是联合主件的意思说这个99a这个联合主件重复好再删一位这个时候才能查到成功这个查到成功之后呢等他计算完成咱们的数据呢应该变成22条好已经变成22条了这个呢是由于数据库的逻辑他帮咱们做了一个很好的判断数据库的有一个主件约束就是联合主件加上咱们的一个唯一的一个用户ID的这个主件两个约束呢就
[03:30] 保证了咱们这个地方的ID肯定是唯一的这个时候咱们的代码就省事了非常省了很多事就是非常省事的就可以对一个新增用户进行一个实时计算咱们来切回温暖到此咱们通过在开发工具中运行咱们代码而且利用手动添加数据的方式来验证咱们结果就是Redis中最终实时计算的结果
[03:58] 经过验证呢这个结果是OK的没有问题的好咱们这个测试呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  // Kafka
  val bootstrapServers = "xc-online-Kafka:9092"
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
  ssc.checkpoint("/user/Hive/external/data_course/today_new_user/checkpoint")
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

