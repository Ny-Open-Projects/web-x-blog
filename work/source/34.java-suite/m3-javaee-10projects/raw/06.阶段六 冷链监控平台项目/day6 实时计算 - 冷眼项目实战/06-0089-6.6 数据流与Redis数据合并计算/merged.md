# 6.6 数据流与Redis数据合并计算

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.6 数据流与Redis数据合并计算_【海量资源尽在 666java.com】.mp4
- 时长 15分15秒（音频 915s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来开发我们这个message aggregate这个类这个类的主要作用呢是把我们卡普卡里面拿到的数据和redis里面获取的预值相关的一些数据进行合并和计算那么在这个过程中我们可以看到我们用我们
[00:17] 开始拿到Kafka里面数据的时候我们得到的是一个message entity而这个message entity呢它包含了三部分的数据一部分数据是我们的这个设备的基本信息而这个设备基本信息呢是从我们这个redis里面拿到的数据那第二部分数据是我们的这个温度湿度数据温度湿度数据是从Kafka里面拿到的数据那第三部分数据其实是我们的这个温度湿度的一个预警
[00:46] 预警数据是属于我们的这个计算的一个结果所以说我们需要在我们的这个message aggregate这个类里边把这三部分的数据统一的合并成一个message entity所以我们在这里我们开发我们的这个叫aggregate messagemessage aggregatemessage aggregate我们要实现这个
[01:18] 开发这个类这个类的话它其实是需要实现了一个map的一个叫map function而这个map function呢它是把我们一个message entity转换成另外一个message entity那最终得到我们一个想要的一个message entity的这样的实体的实体对象那我现在把我们的我们的这个map方法给它重写一下OK
[01:52] 那此时我们拿到了是message entity的这样的一个类那此时相应的我们需要把我们的这个叫什么呢把我们的redis里边拿到的数据比如说我们要所以说在这个过程中我们要定义我们的我们的g-edit-util那等于g-edit-util的一个get instance我要获取我们的instance这实际上是我们的这个redis它的一个工具类
[02:22] 那在我们这个MAP方法里边我们要做的事情就是把Redis里边的数据拿到和我们Kafka里边的数据Kafka里边此时拿到的数据已经是一个message entity了也就是这个message entity这个对象那么我们拿到这个数据之后呢我们下一步就把我们的Redis的数据给它覆盖上去没有原来的从
[02:48] Kafka里边拿到数据里边的messagemessageintact这个数据对象给它补全它那我们在这里我们定义我们的geditgedit等于geditutil.getedit也就是说我拿到了一个reddit一个客户单那么此时我们要执行我们的执行我们的方法然后我们
[03:25] 如果出现异常的时候啊我给他一个print出来对吧那异常的时候我要把我的edit的这个呃工具类我们把我们的broken然后deedit那如果是我们执行完了之后呢我们要把我们的final类里边deedit给执行我们的return我们的redditok这是我们的这个这个程序体已经呃
[03:59] 大致的这个结构是这样的那在这里边我们就开发我们从从这个哪从我们的从我们的这个redis里面拿到的数据我们redis里面拿到数据我们定义一个变量啊这实际上是beta类型的等于gedit然后呢我们获取获取获取一个k对不对而这个k呢我们需要先进行一个呃一个一个一个解码
[04:27] 因为本身我们把这个redis里边把数据存储到redis里边的时候实际上是进行了一个编码编码之后呢我们现在获取的时候我们要进行解码这种解码的话cf encoder然后我们把它encoder这种encoder的话我们可以使用messageentity我们获取我们的这种metacode因为我们把它存储到我们的
[04:55] 存储到我们的redis里面的时候我们的主件是我们设备的一个code对吧那现在我们从这里边我们就拿到了一个我们的这个数据流是我们的battery型的这种设备的一个数据那我们就把metaintity这是一个设备嘛对吧设备我们设置我们的meta等于把它进行一个
[05:32] realize utile应该是应该是它的这个类对我们要把它进行啊反序列化OK这个时候我们它类型类型是不对的也就是说我们拿到了是我们的我们的字符流字符流之后要把它反序列化成我们的一个matter entity这种类型的而这种matter entity这种类型呢我们需要给它一个加上一个叫matter entity
[06:06] 这个时候就OK了对吧我们此时拿到了这样的数据那下一步的时候我们要把我们当前的这个message entity那此时message entity里边是Kafka里边的数据对吧那么我们要把这个message entity给它复制复制什么呢我们设置我们的这个meta id等于meta.get id然后我们再设置message entity然后设置set
[06:42] meta name等于meta.getmeta name然后我们的因为我们messagemessage entity里边这个其实已经有有有code了我们就不需要设置它的code了但是我们还可以设置我们还需要设置这个其他的比如说我们的setset我们的什么呢host主机host code等于meta.gethost code
[07:14] 然后我们还在设置我们的host id的meta应该是metaredis里面的get host idmessage entity然后设置host name然后meta.get host name那下一步的话我们设置完host之后我们再设置我们的house也就是说我们的仓库此时方法也是一样的对吧
[07:50] 那下一步的话我们设置
[08:26] 这个时候我们把我们的主机上的就是在Redis里面存储的我们的一些主机仓库公司
[08:56] 然后这样的一些信息放到我们的我们的卡普卡队列的对应的消息的这种实体上了下一步的话我们还可以设置一些预值的信息对不对其实是我们的messageintent我们要设置最大的home.meta.getmark失误数据然后
[09:26] 但是这个来讲的话类型不匹配它是一个integra的value of我要把它转换成这个对吧下一个的同样道理来讲的话我都是需要message entity然后setmean也就是说integra.valueof value of matter.get最小的适度数据
[10:01] 那一样道理message inti设置最大的一个温度然后matter.getmark的最小的温度域值那从redis里边获得我们的温度域值的最小值ok这个时候是把这个值放进来了那下一步的时候我们就需要设置我们的这个
[10:44] 温度和湿度的是否进行预警如果我们的messageintended我们如果获得一个我们的温度那么这个温度呢如果它小于我们的当前的因为我们message已经了已经当前的最小的最小的温度的时候那其实我们要给我们的messageintended设置我们的term alert是-1
[11:18] 也就是说它是属于这个叫什么呢低温意见那否则情况下S else if if什么呢if如果我们的这个message entity如果我们获得我们的温度那么大于我们的当前这个温度的预值就是最大的温度那么我们需要把我们的这个com alert设置成1
[11:57] 也就是说它实际上是属于高温预警是吧那否则的情况下那其实就是我们给它设置成一个正常温度对吧温度预警是没有正常温度的这个时候其实就是我们对于我们的温度的预警数据进行了一个添加了那还有一个的话就是我们对于我们的湿度的一个预警预警数据
[12:25] 那湿度预警数据其实也是一样的,类似的嘛我们获取我们的这种我们把它拷贝一下get我们的朋友们对吧那么我们这个时候是get这个最小的那么我们这个地方就需要给它设置成我们的set湿度预警属于低湿度低湿度预警对吧
[13:02] 但是这个如果我们的get我们的湿度如果大于我们最大的湿度域值那我们其实就是一个湿度set湿度域景这个里面其实就是一个湿度域景否则情况下我们的湿度就变成湿度否则情况下我们的湿度就是属于一个正常的湿度那它反回过来是个什么呢我们给它反回过来就是
[13:47] 我们的这个message in titlereturn我们的message in titleok这个时候我们就把我们的数据给返回过来了返回过来之后当然最后一个返回空返回空我们不返回空了我们给它还是返回这个吧也就是说如果出现异常之后我们还是把这个数据流返回成我们这个数据流了原来数据远了这个时候我们就把我们
[14:24] 对于在我们这块的时候这个不用不着了在我们进行数据流就是卡普卡数据流和Redis数据流进行合并那么这个方法这个类我们给它写完了那么我们看一下它的一个简单的看一下它的这个过程那以一个过程来讲我要拿到Redis的数据那拿到Redis数据的时候本身我自己实际上是有了一个这种卡普卡的数据流
[14:55] 那么卡帕卡数据流之后和Redis数据流进行合并合并完了之后呢我要进行进行这个计算而这个计算呢是我要计算除了是高温的还是低温的还是高湿的还是低湿的最后呢把这个数据流合并完了数据流返回返回过来那么我们此时就得到了是一个合并之后的一个数据流

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Flink 流处理程序中，通过自定义的 MapFunction（MessageAggregate）将来自 Kafka 的 MessageEntity 对象与从 Redis 中获取的 MeterEntity 对象进行数据聚合，并将结果写回 Kafka。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示了 MessageEntity.java 文件，其中定义了用于表示监控数据的实体类，包含字段如 maximum、temAlert、temLimit、state 等，并有中文注释说明其含义。
画面 2: 显示了 MessageAggregate.java 文件，该类实现了 MapFunction<MessageEntity, MessageEntity> 接口，用于对输入数据进行处理。
画面 3: 在 MessageAggregate.java 中，代码开始初始化 Jedis 实例，用于连接 Redis。
画面 4: 代码中调用 Jedis 的 get 方法获取 Redis 中存储的 MeterEntity 对象。
画面 5: 代码中使用 Jedis 的 get 方法获取 Redis 中存储的 MeterEntity 对象，并通过反序列化将其转换为 MeterEntity 实例。
画面 6: 代码中将 MessageEntity 对象的属性设置为从 MeterEntity 中获取的值。
画面 7: 代码中将 MessageEntity 对象的属性设置为从 MeterEntity 中获取的值，并处理了温度相关的字段。
画面 8: 代码中将 MessageEntity 对象的属性设置为从 MeterEntity 中获取的值，并处理了温度相关的字段。
画面 9: 代码中将 MessageEntity 对象的属性设置为从 MeterEntity 中获取的值，并处理了温度相关的字段。
画面 10: 代码中根据温度值设置 MessageEntity 对象的 temAlert 字段。
画面 11: 代码中根据温度值设置 MessageEntity 对象的 temAlert 字段。
画面 12: 代码中将 MessageEntity 对象的属性设置为从 MeterEntity 中获取的值，并处理了温度相关的字段。
画面 13: 代码中将 MessageEntity 对象的属性设置为从 MeterEntity 中获取的值，并处理了温度相关的字段。
画面 14: 代码中创建了 KafkaConsumer 和 KafkaProducer，用于从 Kafka 读取数据并写入 Kafka。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private int maximum;
//温度下限
private int minimum;
//温度状况：1.高温，0.正常，-1.低温
private int temAlert;
//温度状况：1.高温，0.正常，-1.低温
private int temLimit;
//状态：1-在用，0-停用，-1-异常
private int state
```

画面 2:
```java
package com.ithema.cold.Flink;
import com.ithema.cold.common.entity.MessageEntity;
import org.apache.Flink.api.common.functions.MapFunction;
public class MessageAggregate implements MapFunction<MessageEntity, MessageEntity> {
```

画面 3:
```java
import com.ithema.cold.common.entity.MessageEntity;
import com.ithema.cold.common.utils.JedisUtil;
import org.apache.Flink.api.common.functions.MapFunction;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
```

画面 4:
```java
final JedisUtil jedisUtil = JedisUtil.getInstance();
```

画面 5:
```java
byte[] meterBy = jedis.get(SafeEncoder.encode(messageEntity.getMetercode()));
MeterEntity meter = (MeterEntity) SerializeUtil.unserialize(meterBy);
messageEntity.setMetercode(meter.getMetercode());
```

画面 6:
```java
messageEntity.setMetername(meter.getMetername());
messageEntity.setHostcode(meter.getHostcode());
messageEntity.setHostid(meter.getHostid());
messageEntity.setHousecode(meter.getHousecode());
messageEntity.setHouseid(meter.getHouseid());
messageEntity.setCompanyname(meter.getCompanyname());
```

画面 7:
```java
messageEntity.setMetername(meter.getMetername());
messageEntity.setHostcode(meter.getHostcode());
messageEntity.setHostid(meter.getHostid());
messageEntity.setHousecode(meter.getHousecode());
messageEntity.setHouseid(meter.getHouseid());
messageEntity.setCompanyname(meter.getCompanyname());
```

画面 8:
```java
messageEntity.setMetername(meter.getMetername());
messageEntity.setHostcode(meter.getHostcode());
messageEntity.setHostid(meter.getHostid());
messageEntity.setHousecode(meter.getHousecode());
messageEntity.setHouseid(meter.getHouseid());
messageEntity.setCompanyname(meter.getCompanyname());
```

画面 9:
```java
messageEntity.setMetername(meter.getMetername());
messageEntity.setHostcode(meter.getHostcode());
messageEntity.setHostid(meter.getHostid());
messageEntity.setHousecode(meter.getHousecode());
messageEntity.setHouseid(meter.getHouseid());
messageEntity.setCompanyname(meter.getCompanyname());
```

画面 10:
```java
if (messageEntity.getTemAlert() == 1) {
    messageEntity.setTemAlert(1);
} else if (messageEntity.getTemAlert() == 0) {
    messageEntity.setTemAlert(0);
} else {
    messageEntity.setTemAlert(0);
}
```

画面 11:
```java
if (messageEntity.getTemAlert() == 1) {
    messageEntity.setTemAlert(1);
} else if (messageEntity.getTemAlert() == 0) {
    messageEntity.setTemAlert(0);
} else {
    messageEntity.setTemAlert(0);
}
```

画面 12:
```java
messageEntity.setMetername(meter.getMetername());
messageEntity.setHostcode(meter.getHostcode());
messageEntity.setHostid(meter.getHostid());
messageEntity.setHousecode(meter.getHousecode());
messageEntity.setHouseid(meter.getHouseid());
messageEntity.setCompanyname(meter.getCompanyname());
```

画面 13:
```java
messageEntity.setMetername(meter.getMetername());
messageEntity.setHostcode(meter.getHostcode());
messageEntity.setHostid(meter.getHostid());
messageEntity.setHousecode(meter.getHousecode());
messageEntity.setHouseid(meter.getHouseid());
messageEntity.setCompanyname(meter.getCompanyname());
```

画面 14:
```java
//Kafka队列的consumer，接收Kafka发来的数据
FlinkKafkaConsumer<String> consumer = new FlinkKafkaConsumer<>(druid_topic, new SimpleStringSchema(), properties);
consumer.setStartFromEarliest();
//设置数据源
DataStream<MessageEntity> stream = env.addSource(consumer)
    .map(new MessageAggregate());
//将数据写入Kafka队列
FlinkKafkaProducer<String> producer = new FlinkKafkaProducer<>(druid_topic, new SimpleStringSchema(), properties);
outStream.addSink(new SinkWithRetry(producer));
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

