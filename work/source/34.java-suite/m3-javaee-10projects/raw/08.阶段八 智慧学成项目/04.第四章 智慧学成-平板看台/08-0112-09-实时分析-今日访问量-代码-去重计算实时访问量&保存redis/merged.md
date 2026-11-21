# 09-实时分析-今日访问量-代码-去重计算实时访问量&保存redis

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\09-实时分析-今日访问量-代码-去重计算实时访问量&保存redis_【海量资源尽在 666java.com】.mp4
- 时长 18分37秒（音频 1118s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前边呢已经使用Kafka的工具类,加上咱们的Spark Streaming来获取到了Kafka中的数据,接下来呢,咱们对数据进行去虫并计算它的一个访问量,这里呢使用Messager这个变量进行一个去虫操作,这里呢Messager它是Kafka中的流数据,这里呢咱们使用Map算子,
[00:26] 来取出它里边的值这里呢就是取出它的一个value取出value之后呢咱们对值进行一个切分继续呢使用myp算子这里呢咱们切分是使用-t切分你问这个地方为什么要使用-t切分呢如果这个地方记忆不起来呢咱们来打开咱们第二张etl的文档在咱们
[00:54] 第二张ETR文档课程法案量就是ODS层原型数据这个地方呢有咱们原型的数据结构以及呢它的一个存储方式这里咱们的数据存储是使用-t进行分割然后用-n进行换行也就是说这些字段的分割方式呢就是使用-t咱们呢也是这里使用-t切割来得到每个字段的值好咱们继续回到开发工具
[01:22] 这里切分完成之后接下来就是一个计算了它得到了一个数字咱们还是使用MAP算子进行一个计算这里是AR接下来对AR进行一个统计这里咱们是使用课程的IDSession ID和用户的IP进行去除咱们来看一下它分别是对应哪几个字段课程的IDSession ID用户的IP分别是
[01:51] 锁引0数组因为这个地方已经是切坑后的数组了这里锁引0 1 2 3也就是锁引0和锁引2以及锁引3咱们呢需要这三个字段进行一个去重这里呢咱们对它进行一个去重操作在它去重之前呢咱们呢首先要给它把这三个字段呢合并成一个字段这里呢就是AR2
[02:21] 这个少了一个括号AR0咱们使用下滑线进行一个链接加上咱们的AR2和AR3这里所以少了一个加号所以2加上下滑线这里所以3加号加号错了它是通过竖组把这
[02:53] 课程ID,SessionID以及IP把它给连接起来连接起来它就是一个整体对这个总体对它进行一个复制操作也就是说每过来一个数据把这个整体计数为1计数为1之后咱们后边就可以对它进行一个去重的操作了咱们这里先只是给它计数计数完成之后咱们这个地方用一个变量来接收咱们这个地方是UserVisit
[03:23] 这里呢变量名就叫做uv然后呢因为咱们还没有去程它是一个临时变量user vdata的一个临时变量咱们接下来呢是接下来呢使用这个临时变量呢进行一个去程操作这个地方呢加个注释这是计数根据根据咱们的这三项进行先计数这里呢是计数
[03:55] 技术完成之后呢咱们接下来呢进行一个去虫这个地方去虫呢咱们是需要使用一个函数的这个地方呢是mapmap with stage这个地方呢这个函数咱们还没有定义咱们呢需要taststate需要呢这个地方需要定义一个函数咱们呢就是使用
[04:28] state这个方法呢来定义一个函数但是呢这个函数呢咱们需要定义在外边也就是这个地方呢直接调用在外边定义一个函数然后这个地方直接调用接下来呢咱们来定义这个去重的函数这它呢给它一个变量咱们那个函数呢就叫messer的它的返回值先给它一个等号不是返回值它这个地方的参数呢
[05:00] 它是一共是三个参数咱们先把这个格式给写完三个参数呢它需要对参数内的一个根据这个参数呢需要对这相应的参数做处理咱们呢先把这个格式给写出来接下来呢来写参数这里呢第一个参数就是word这个word呢就是上面咱们拼接好的这个值word然后呢它是一个死清类型的
[05:30] 接下来是CountCount是一个Int类型但是这个Int是用Open进行包裹的因为咱们这个值是包裹后的值咱们才能获取也就是通过Count.get值能得到咱们具体的一个value接下来是一个Stage就是这个Stage它是方便咱们进行
[06:01] 计数的时候就是去程的时候方便咱们对它进行一个同值的一个操作这个呢是由于分布式计算要用到的咱们呢这个地方主要是用在分布式计算上面嗯它呢同样的是包裹起来的它的数据类型呢这里也是印创这是咱们定的函数这是函数的参数有了这些参数之后呢咱们需要对它进行一个相对应的一个计数操作首先呢
[06:32] 这个地方来一个number这个number就是一个计数的一个值咱们使用count来get这个值这个地方是一个get all else它的意思就是说你这个值存在了我就获取具体的值你这个值不存在我就给你一个默认值0这是咱们当前的一个count接下来是咱们分布式计算它这个计算的时候保存的一个count这叫做stae
[07:01] 在这个里面呢也是get先是get open把值给取出来接下来呢也是get all else也就是说如果你有的话我就是把值给拿过来没有呢你的默认值就是0这个呢就是它最终计算的一个值呢就是咱们word的一个值也就是说我这次获得的一批数据这个word有几个通过这个计算呢前面是咱们count的一个就是说你传过来参数的一个值这个地方
[07:31] 默认的话按道理来说咱们这个地方是1因为咱们这个地方默认值是1这个stage呢state呢它是咱们分布式计算存的值如果有也就是说你这个word之前有值了我就会存到这个里边如果没有呢你这个地方在获取的时候它就是0咱们呢接下来还有一个还有一个更新的一个操作也就是说我之前
[07:59] 如果没有的话这个地方是0但是如果我有的情况下我是不是就是最终计算这个SUM就是这个计数这个值是不是就更新了这个更新完成之后呢我还需要把这个数呢给更新进来它呢就是一个update把咱们那个更新后的计数给放回去这个放回去之后呢咱们就可以对这个值进行一个返回了就是把新的值返回返回回去返回回去呢
[08:28] 交给下一个处理下一次处理的时候进行一个操作处理这个呢是更新分布式里边的分布式计算里边的一个值这里呢是加个度式更新值这个呢是返回数据就是返回更新后的数据返回计数后的数据返回计数后的数据返回计数后的数据这个呢更新值
[09:00] 它呢是更新分布式计算里边存取了值分布式这个是框架帮咱们做的咱们就不用关心只用知道这个地方是这样用就行了接下来呢就可以直接来调用这个方法了调用一下之后呢它也会得到新的值这个值呢就是咱们的u v了u v得到咱们的user方user v zeta这个user v zeta呀就是当前这个
[09:36] word这个word呢就是咱们这个地方课程id三线id加ip咱们拼接后的这个值这个值呢它访问了多少次后边呢是具体的值咱们呢最终的时候对这个uv进行一个以求return计算就行了这个时候呢咱们这个值有了之后咱们就是接下来的计算接下来的计算呢因为咱们
[10:03] 这个Spark的String名读取卡普卡的数据呢它是每5秒钟进行一个读取的这个时候呢咱们还需要用到一个共享变量也就是说如果这个UV值更新了咱们这个共享变量也来更新这个共享变量主要的一个操作就是防止咱们原来计算的值丢失这个地方的UV啊还是很多用户的一个访问量咱们呢还没有把它给聚合成具体的一个值比如说我这次取的数据
[10:33] 它访问了5次有效访问是5次咱们还没有咱们还没有真正的一个聚合这呢还是一个技术操作技术接下来呢是共享变量共享变量这个共享变量呢就是保存咱们的Spark中进行共享这个呢是使用Spark Context然后进行一个值的一个获取
[11:13] 给它起个名字就是uv这个uv呢就是咱们具体的一个值吧这个呢它叫做acc这个number吧把这个后边的就叫这个值吧就叫它就行这个值有了之后呢咱们是不是这个具体的这个聚合还没有出来呢这个技术呢是技术的是访问次数就是每个人的
[11:44] 应该不叫每个人是每个用户的访问次数最终呢咱们还需要将这个访问次数进行一个计数接下来呢就是一个计数的操作咱们在redis中保存的时候呢是以天为单位加上咱们visit data这个前缀进行一个保存咱们呢来把这个字段给创建出来这个呢字段就叫做key info它呢就是咱们的visit data下滑线data
[12:17] 然后接着是下黄线加上咱们有一个getinfget这个时间就是当天的一个日期咱们new一个data然后呢来get它一个具体的时间这个获取的好秒值格式呢就是yyy小写的y-mm-dd这是咱们这个字段的这个值这个字段值有了之后呢咱们接下来就是一个
[12:48] 往 redis 保存的一个操作但是往 redis 保存的时候呢保存之前呢咱们还要判断咱们这个 redis 之前是否有值因为咱们这个 redis 呢呃是当天那个数据是实时刷新的也就是每统计一次他都要刷新在保存之前呢我还要判断这个值是否存在咱们呢使用 redis 的这个方法这里呢是 get result redis咱们的 k 呢 redis 中呢
[13:17] 这个仿佛量的k呢是这个是rtcvk然后接下来咱们加上咱们的字段咱们字段呢就是k-info这个呢就是咱们redis保存的值如果有的情况下这个呢如果有的情况下咱们呢就把它给复制给咱们的贡献变量如果没有咱们贡献变量这个地方还是没有值的就是说交给它计算的时候再保存这个地方呢来一个判断
[13:47] 这个地方如果它不等于NOW的情况下如果它不等于NOW的情况下咱们呢先给共享变量添加一个值这个共享变量呢add一下就行了是vl.st.tool这个呢共享变量就有了咱们原来保存的值接下来呢就是对咱们之前用户每次的访问进行一个聚合聚合得到谁啊
[14:19] 得到咱们这次统计的一个访问次数得到这次统计的访问次数之后呢咱们再对它进行一个再对它进行一个相加的一个操作就行了好接下来呢咱们来获取ready不是获取啊咱们来计算这个UA中的这个数据UA对它进行一个聚合这里呢是for each RDD它呢是使用etiorator
[14:50] 咱们呢这个地方是直接叫做ITR就行ITR就行了给它一个方法题在这个里边呢咱们要判断它这个这次计算呢要判断它这个是否有值也就是说这个ETR的count大于0的情况下它是C O U N T大于0的情况下说明咱们这次计算是有效的也就是计算到了这个用户有访问次数咱们
[15:21] 有访问次数的情况下接下来呢就是对它进行一个啥呀对它进行一个和原来值相加这个地方呢把它给add一下就行了add它谁呀就是咱们的这个utriter的count这个更新完成之后就说明了谁呀咱们这个共享变量值更新的共享变量的值更新完成之后这里还不算完咱们是不是还要把redis中的值进行一个更新呢
[15:51] 接下来是redis中的一个值的一个更新这里呢是stop result咱们来看这个方法是有的k的话还是k和字段还是这个接下来呢它的value就是咱们贡献变量的这个值这里呢就是它具体的value咱们直接用value来获取就行了它呢获取到不是浪类型的咱们呢还需要
[16:21] 它获取到的是浪类型的但是呢这个地方呢需要的是啥需要的是一个String类型的主要以上咱们呢把它给转换成一个String就行了to to to to toString转换成String之后呢咱们这个地方就是使用共享变量的方式把这个Redis中的值更新更新完成之后咱们第三步根据这个课程IDSessionID进行去重然后并实时计算就算完成了
[16:50] 这里呢来加个字段这里是组装字段加个注释这个地方呢是组装字段redis hash结构的字段这叫hash字段吧接下来呢是查看原来是否有值原来是否有值这个呢是进行一个复制操作
[17:35] 技术进行复制操作技术这个不应该是技术这个是聚合聚合然后复制这里呢是复制是共享变量复制共享变量接下来呢是redis共享变量复制redis复制复制完成之后呢咱们这个步骤就算完成了好本视频的内容呢
[18:18] 就是根据课程ID,Session ID以及IP进行去重去重完成之后计算这里的实时的访问量计算实时访问量使用共享变量的方式对共享变量进行更新以及对Redis进行更新好,视频就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  // Kafka参数
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

