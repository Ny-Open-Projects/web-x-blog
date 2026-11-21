# 08-实时分析-今日访问量-代码-SparkStreaming获取kafka中的数据

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\08-实时分析-今日访问量-代码-SparkStreaming获取kafka中的数据_【海量资源尽在 666java.com】.mp4
- 时长 10分14秒（音频 614s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前边已经使用Redis的方法,咱们封装的方法,获取了Redis中保存的offset,接下来就是使用Spark Streaming来获取,通过offset来获取Kafka中的数据,这里Spark Streaming这个变量还没有创建出来,咱们来把它创建出来,Spark Streaming咱们是使用Streaming Compact进行一个创建,
[00:27] 它需要 Spark context Spark context 咱们前面已经创建好接下来是需要一个时间 时间函数咱们这里是5秒获取一次它这里面就是 secunda这个地方就是秒的意思这个括号是要英文的然后给它一个变量来接受一下多了一个a 上一下这里就叫 ssc 它报了一个错咱们来看一下
[00:58] 他要Spark contacts这个地方有多个时间Spark contacts然后卡不卡的相关信息这个目前看不出来咱们来看他这个地方的话鼠标点到这你可以看到这个呢contacts这个地方呢多了一个括号这是咱们前边进行编写的时候应该是首务然后多了一个括号这个括号删完之后呢他就不再报酬了咱们在这个地方查看的时候
[01:27] 因为这个地方没有原码有原码的话应该也可以看到到它是需要两个参数好咱们接着往下写这个是获取完了SparkConnect这个不是SparkConnect这是使用SparkConnect获取SparkStreaming这里就是获取SparkStreaming获取完成之后咱们要使用SparkStreaming来读取Kafka中的数据这里咱们还要配置Kafka的参数
[01:59] 接下来呢就是配置Kafka中的参数Kafka小写参数这里呢给他一个变量就叫Kafkac a m a m然后呢他是一个map类型的咱们呢来给他一个数据类型就是stream类型加obj的类型这里要指定obj的类型的主要原因呢咱们后边要指定Kafka的
[02:36] 序列化方式它的序列化方式呢是死春用类型的但是呢他是要指定他的这个具体类型的一个类所以说这个地方咱们有呃5i6要使用这个我不接受的类型的咱们呢这个地方需要配置4个参数嗯就是咱们上面的首先呢是咱们的bot三入然后接下呢是gulp id接下来呢是kv的序列化方式
[03:09] 咱们需要配置这四项咱们首先来第一项咱们呢这个地方配置Kafka的地址呢由于它是使用咱们是消费者这里呢就使用cast termcast term config这里呢要英文的点它呢是bot server config给它这个变量咱们是上面复制的可以直接给它接下来呢是Galaxy Pro ID
[03:38] Galaxy ID也是使用这个变量进行一个配置接下来Galaxy ID config把Galaxy ID给它Galaxy ID完了之后接下来是KV的序列化方式这里还是使用Custom Config k的序列化方式是这个咱们这个地方是要指定类路径这里就是class offset指定具体的类
[04:08] 这里呢咱们是使用的String使用Kafka的String系列化方式就是这个导播的时候一定要导对这是Kafka系列化方式String的系列化方式接下来呢是ValueValue也是相同的咱们呢这个地方只用把这个值改一下就行了Value这个配置完成之后呢咱们接下来就是使用Kafka的工具类来获取Kafka中的一个数据这里呢咱们需要将
[04:39] Spark streaming指定给他接下来咱们就是获取Kafka中的数据这里使用的是Kafka的工具类Kafkayoutube的carrierdecreate stream这里在配置之前咱们需要指定一下咱们的数据类型这里是stream和stream的因为咱们这个地方k和value都是stream的并且指定化了指定了它序列化方式接下来
[05:13] 是对它进行配置这里首先是Spark streaming它一共是三个参数第二接着是保持一致性参数因为咱们这个地方咱们最终程序是要放到Spark集群上进行分布式的一个运行这里有一个集群保持一致性的一个配置一致性配置接下来是咱们卡普卡的参数
[05:52] 参数cd参数好咱们一个一个来配置这里呢Spark streaming就是ssc下一个变量保持一致性呢这里咱们咱们可以点它进行查看它这是有多实现的这个地方你可以看到Spark streaming呢放完之后呢它是有一个location stage接下来呢是Kafka的配置咱们呢接下来是使用它把它给粘一下
[06:22] 这个呢呃他应该是要大写的l呢是大写呃存头写吧location l大写location啊就第一个这个呢咱们指定的是他指定完成之后呢接下来就是Kafka三数Kafka三数呢咱们使用的是谁呀是消费者这个地方呢还是cast term把这个也粘一下他呢cast term
[06:54] 是stage是这个1.0我们应该适用的1.0我找个包对适应的1.0然后接下来是ASS这个地方没有点出来就说明这个不是010不是010呢不是咱们这个前面少了一个逗号少了一个逗号它没有过来这个时候这个010它就自动就出来了
[07:27] 使用的是assign指定咱们的参数它指定参数的时候咱们也需要指定数据类型数据类型也是shrimp和shrimp的它这里边需要的参数就比较多了不是也比较多了就是咱们上面配置的这些参数了就是咱们已经准备好的参数是offsetoffsetk接下来是Kafka的参数
[08:00] 接下来呢是offset把这个给复制一下offset的k呢咱们这里使用offsetcase.to list它呢这个地方使用list来接收接下来呢是Kafka的参数逗号不要丢了咱们上面这个逗号丢了就导致下面写的时候点不出来就是它没有相当提示接下来呢是Kafka的参数接下来呢是offsetoffset
[08:31] 这个也是少了多号所以点不出来这里咱们配置完成之后到此咱们获取数据就OK了获取完完成之后这个地方是需要一个变量来接受一下的这里就叫做messagemessage叫message的原因因为咱们是从Kafka中获取数据Kafka是一个消息服务这里获取的数据就是消息数据
[09:03] 这个地方它稍微有点长咱们呢给它来个这个注射就不要吧因为只有三个参数注射就不要把它给折成一行这样的话就比较美观一点这个括号还不能在一起因为它们是两个数据类型的一个封装好到此呢咱们使用Spark Streaming来获取Kafka的数据通过参数的封装以及
[09:35] 通过使用Kafka这个工具类来获取这个Kafka中的数据咱们呢到此这个配置就完成了接下来呢就可以使用message的这个变量来读取数据对数据进行去虫操作并计算相对的反反量计算去虫以及计算实时的反反量交给后面的视频进行讲解咱们呢本视频就到此结束通过本视频的学习呢需要掌握
[10:05] 把Kafka的相关参数给配置并且呢能够使用供应类获取Kafka中的数据好视频呢到此结束

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark Streaming 从 Kafka 消费数据，并通过 Redis 保存消费位点，实现基于 Redis 的 Kafka 消费位点管理。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了创建 SparkContext 的代码，配置了 Kafka 的 bootstrapServers、group.id、topic.name 和 Redis 的 offset 键值。
画面 2: 展示了 Spark Streaming 的 StreamingContext 类的源码，包含其内部的私有成员变量和构造函数。
画面 3: 同画面 2，展示 StreamingContext 类的源码。
画面 4: 展示了 ConsumerConfig 类的常量定义，用于配置 Kafka 消费者。
画面 5: 展示了 ConsumerConfig 类的常量定义，用于配置 Kafka 消费者。
画面 6: 展示了创建 KafkaDirectStream 的代码，配置了 Kafka 的参数。
画面 7: 展示了选择 KafkaDirectStream 方法的弹窗，显示了方法签名。
画面 8: 展示了为 KafkaDirectStream 设置 locationStrategy 的代码。
画面 9: 展示了 Consumer 类的自动补全列表，包含各种 Consumer 类型。
画面 10: 展示了 ConsumerStrategies 类的自动补全列表，包含各种消费策略。
画面 11: 展示了 Scala 中的集合操作方法，如 scan、split、span 等。
画面 12: 展示了创建 KafkaDirectStream 并设置 locationStrategy 和 assign 的代码。
画面 13: 展示了设置 KafkaDirectStream 的 locationStrategy 和 assign 的完整代码。
画面 14: 展示了设置 KafkaDirectStream 的 locationStrategy 和 assign 的完整代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
val sc = new SparkContext(sparkConf)
val bootstrapServers = "xc-online-kaika:9002"
val groupId = "visit_topic"
val topicName = "visit_topic"
val rt_cv_key = "today:course:visit:current"
val rt_cv_offset = "today:course:visit:offset"
```

画面 4:
```scala
val redis = new RedisUtils
redis.initRedisPool()
val offsets = redis.getLastCommittedOffsets(rt_cv_offset, topicName, partitions = 1)
```

画面 6:
```scala
val kafkaParam = Map[String, Object](
  ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG -> bootstrapServers,
  ConsumerConfig.GROUP_ID_CONFIG -> groupId,
  ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer],
  ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer]
)
```

画面 8:
```scala
LocationStrategies.PreferConsistent
```

画面 12:
```scala
val message = KafkaUtils.createDirectStream[String, String](
  sc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Assign[String, String](offsets.keys.toList, kafkaParam, offsets)
)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

