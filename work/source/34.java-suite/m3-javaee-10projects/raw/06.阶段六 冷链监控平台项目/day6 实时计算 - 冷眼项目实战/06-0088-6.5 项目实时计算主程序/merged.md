# 6.5 项目实时计算主程序

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.5 项目实时计算主程序_【海量资源尽在 666java.com】.mp4
- 时长 21分0秒（音频 1261s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来开发我们这个Flink实时计算的主程序而这个程序呢是主要作用就是我们把我们redis里别的数据和我们的卡布卡里边的数据进行实时计算进行比对查询出来所有的这种属于
[00:19] 温度异常或者说湿度异常的数据然后把它的计算出来的结果发送到我们的这种卡法卡队列里面去这是我们这个程序里边所要的主要的功能那么我们现在先创建一个Java的一个类而这个类的话是com我们写一下包名com.rt黑马.code.Flink.stream.streamingjobOK
[00:53] 我们创建这么一个教本这么一个教本来讲的话我们使用的是这个一个Main函数这个Main函数里边是我们开发我们的这Flink程序那么我们开发Flink的应用的话大致分成这么几个几个步骤吧第一个来讲的话是设置环境信息那第二步来讲的话设置设置数据语言第三部分是进行实时
[01:29] 实时的一个计算或者说是数据源数据流的一个计算然后设置输出输出源执行程序Clink程序的应用它基本上它的这种组含数都是这种过程或者是这样的一个步骤那么首先来讲我们要设置一个数据源数据源final的一个streamstreamexecutionenvironment
[02:12] 我们有一个一个在线以外的 env env等于是这一名一个在线以外的crate然后我让他crate呃我不用crate我可以crate local的对吧但是我可以用啊get in一个在线以外的那么这是我们就设置好了数据员设置好数据员之后呢但是我需要给他设置一下我的这个呃
[02:36] 环境信息我的环境信息的话我需要设置它的一些参数比如说我Enable Checkpoint就是容错那么5000那下一步的话我可以设置一些检查点这个其实是我们的叫设置容错容错点那么下面呢我们来设置检查点因为第二
[03:17] get checkpoint的config然后在这里面的话我设置checkpoint的model那这个model就是设置检查点的一个模式这种模式是checkpointmodel里面checkpointcheckpointconfig的default一个model那我还可以再设置设置我们的重启策略也就是说
[03:55] 我如果我们的这个程序发生了异常之后我们如何来进行重取inv.getconfig然后呢.setrestart然后这个restart这个策略的话实际上是restartinrestartstratejtjtj点
[04:34] 然后这个时候flex的delay restart然后这个我们加上加上参数OK这个意思是说我们重启restart的这个次数是四次然后呢我们在两次重启之间我们用了啊1000毫秒或者说是这个但是它实际上是一个这个间隔嘛重启的重启之间的间隔啊这个这个是我们把我们的这个环境信息给填写上了
[05:11] 那下一步的话我们来因为我们是我们的这个Flink程序它要监听我们的Kafka里边的数据那首先的话我们就需要定义一个Kafka的一个对列对吧我定义Kafka对列这个对列的名字Kafka对列对列名称是这样类型的一个Kafka等于all device下划线all topicok
[05:51] 我点击好了我的我的这个队列那下一步的话我就需要设置我们Kafka的一些啊对列的一些属性而这个属性呢实际上用到了我们的一个设置Kafka对列属性对列属性那这个属性的话我们用到了propertiesproperties然后有一个这种这个啊propertiesproperties等于new
[06:25] 那么我们要设置properties以什么属性呢setpropertiesok那第一个来讲的话是我们的Kafka队列的地址对吧bossdrop.server然后呢它是我们的服务器Kafka队列的服务器172.17.0.143然后是9092
[06:57] 这是我们对这个对这个对列的服务器的IP和地址和端口对吧那么再可以设置我们的property然后我们的这个grouper.id然后呢是我们的code link那下一个的话我们要设置我们的properties.setproperty设置一个autoo.offset.
[07:31] 那么这个的话我们用了一个叫EarList我们用最早的对吧我们可以用最早的然后我们也可以用Lattice这其实就是它的一个属性那设置完了之后我们要设置我们的这个Kafka对列Kafka对列的Consumer也就是说我们的这种Consumer也用来接收
[08:05] 接收Neti发送的数据OK我们要设置这个consumer那么它的consumer是Flink consumerflink kafuka consumer我们用了这个而这个consumer的话它的数据类型呢是一个string类型的也就是说我们拿到的数据是一个string类型的这个consumer等于什么等于newflink kafuka
[08:41] consumerstring然后这个时候我们需要给这个consumer设置一些参数而这个参数的话我们一个是属于我们的KafkaKafka topic这是我们的Kafka的一个对列对列的名字那另外一个的话我们要设置它的类型它是一个simple的一个string的一个scam也就是说是它的数据类型是一个string类型的然后我们再加上我们的这个perpetual参数OK
[09:13] 这个时候我们就把我们的consumer的一个队列给它添加上了而添加完这个队列之后呢下一步的话我们就可以设置我们的这个consumer所用到的一些属性对吧刚才是定义了一个consumerconsumer然后我们可以设置我们的start fromstart from什么呢from list我就是从最早的时候我开始给它获取数据那
[09:43] 下面的话我们就要设置我们的这个数据源了而这个数据源的话是我们的这种这个Flink用到的数据源就是Flink stream我们这个数据源是它类型是messageentitymessageentity的话我们拿到了一个数据流而这个数据流实际上是我们
[10:16] 根据环境就是streaming environmentexecution environment然后它呢我要添加一个source而这个source我们可以使用consumer然后我们可以设置我们set它的这个并行度是一个并行度然后呢我们把它因为我们这个数据流我们consumer就是卡普卡里边consumer的数据实际上是一个stream类型的我现在需要把stream类型的给它转换一下转换成我们的message entity
[10:52] 那么实际上在这里面的时候我要对它进行一个mapOK这种map的话实际上我们要对一个string类型的转换成什么呢转换成我们的一个json我们用json把我们的Kafka里面的数据给进行一个pass一下pass objectpass object这个是一个string类型的然后呢我们再把我们的转换成的messageinit
[11:30] ok那其实此时我们可以看一眼它实际上是把我们consumer来调用使用我们的这个consumer然后呢设置一个我们的这个Flink执行的一个变形度然后得到的一个是我们的string类型的一个数据数据数据流这种数据流的话我要把它转换成我们的这种message entity类型的数据流那么我们就
[12:03] 用了一个map的这样的一个方法而这个方法之后呢我们就拿到了一个这种message entity就是message的这种类型的这种数据流那获取了这种数据流之后呢那下一步的话我们是需要什么呢我们需要从redis中获取预持的一些数据
[12:28] 然后我们现在刚才已经拿到了是我们的这个设备里边提交过来的温度和湿度那我要对温度湿度进行比对那比对之后比对的话我需要再拿另外一个数据源这个数据源是从Redis里边获取的而这种Redis获取的那我可以把它设置成一个我们的DataStream我们设置成DataStream了DataStream的时候我们还是有一个MessageEntity而这种MessageEntity
[13:00] 是我们的这种redis的一个redis的一个stream等于stream.map而这个map的话我们用了一个messageagreegit这样的一个方法也就是说在这个时候我们从redis里边获取预支数据并且并且与与什么呢与刚才的这个数据源与Kafka的数据流
[13:42] 进行合并对吧那其实是这个我们的这个message aggregate这个这个类实际上是做了这样的一个工作那我们回头再写这样的啊写这样的一个类这个类的话这个类主要是做做合并的一个工作的啊release拿取数据然后进行合并工作的那我们可以把它先放一下之后我们再从设备中啊
[14:08] 得到这个数据之后我们要把这个数据存储到我们的存储到我们的这个mycircle里面去因为我们拿到了数据之后一个数据类型是说我要把这个数据一种是说我要把数据存到我们的这个mycircle里面另外一个的话是我们要把数据扔给我们的这个卡普卡扔到卡普卡队列里面去所以说我第一步我要存储到mycircle里面去那么我把什么存储到mycircle我把outstream.add
[14:45] 而add sync来讲的话那这中间其实是我们可以添加一些方法这个方法的话我们可以添加syncToMyCircle是这样的一个方法那此时我们要把我们这个方法下一步的话我们要把这个我们的数据发送到Kafka对列因为刚才我们看到了一个方法是我们需要一个方法来发送到这种MyCircle里面去我们
[15:24] 下一步的话我们需要一个方法发送到Kafka里边那我先把这个主程序体来给呃填写上那么后边的话我们再把两个这两个方法一个是和我们的redis进行合并那么另外一个的话是和我们的马赛口存储到马赛口里面去再把这两个实际体来呃填写上那我们因为呃我们这个Kafka里边来讲的话我们就使用了这个Flink的一个呃Kafka的Kafka的一个
[15:56] producer这种producer的话实际上是一个什么呢是一个string类型的也就是说我要把string类型的放到我们的这个producer我要把我们的这个string类型的发送到我们的Kafka队列里面去linkKafka的这种队列而这个队列呢其实是我们要用到的是另外一个队列名字这个队列名字其实是
[16:30] 我们在上面再加一个dream.topic也就是说这个是我们的这个dread要用到的一个topic这个topic的名字就叫all the wise message那此时它是一个dread使用的队列而上面这个呢其实是我们的这个Flink使用的队列对吧ok我们现在再回到这个地方来我们的Flink
[17:15] 咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳咳
[17:45] 经过要把它转化成一个String类型的对不对因为你刚才的话我们是要把String发送到卡普卡队列里面去所以说我们的outStream这是进行最终的一个结果我们要把结果转换成一个转换成我们的String类型然后再发送到卡普卡里面去那么此时的我们要对outStream进行MapMap的时候要new一个Map function而这个function其实是我们的一个
[18:15] 就是这样的一个这样的一个就是一个死争类型的它是一个死争类型的死争类型的一个死争类型的OK这种死争类型的那此时我们需要进行一个转换这种转换的一个map的时候我们可以使用什么呢我们可以把它转换成了一个return也就是说我由一个message entityreturn出我们一个一个字符率
[18:51] 而这种制服赛是我们用 json 的一个to json string然后是此时是一个 message in tally这个时候我们就把我们的一个叫 message in tally 这种类型的对象数据流转换成 string 类型的数据流然后此时我们再把它 add sync对吧add sync 是干嘛呢实际上是要把它放到我们的这个producer 里边去
[19:21] 这个时候我们把我们的数据发送到Kafka队列里面去了那此时我们再把我们的my producer的一个close一下ok那下一步的时候因为这此时我们的两个数据源已经一个数据留了一个计算这个计算的话其实上面已经做到了那下面来点的话是输出源这个输出源的话其实是输出到我们的输出到我们的my cq里面去和输出到我们的Kafka队列里面去
[19:50] 只不过是我们现在有两个方法现在两个类还没写那我们先把主程序体写完它那下一步的话我们其实就可以执行我们的execute执行这个程序其实就OK了而执行这个程序来讲的话实际上我们这个可以设置成什么冷链设备实时监控任务但是它现在是报了个错报了个错的是实际上我们没有把我们的这个
[20:24] 错误给它抛出来我们要把它从错误抛出来其实也OK了那此时我们就把我们整个书成语体给开发完了那下一步的话我们再开发我们的这两个没写完的这种类一个是我们卡不卡因为从Redis里面获取数据然后和我们卡不卡拿到的数据进行合并合并成一个具有这种message entity类型的这个数据流
[20:52] 另外一块的话是把合并后的结果发送到我们存储到我们的Mathsql里面去这是我们的一个整个的程序主体

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
编写一个基于 Flink 的 Kafka 数据流处理程序，实现从 Kafka 消费数据、进行转换计算、再写入另一个 Kafka 主题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IDEA 中右键点击项目目录，选择“Build Module 'cold-Flink'”进行模块构建。
画面 2: 编辑器中显示 StreamingJob 类的开头，包含注释“//设置环境信息”、“//设置检查点”、“//设置流计算”、“//设置输出”。
画面 3: 在代码中调用 env.getCheckpointConfig()，弹出方法提示框，显示可设置的检查点相关方法。
画面 4: 设置检查点模式为 DEFAULT_MODE，并设置重启策略为 fixedDelayRestart，参数为 restartAttempts=4 和 delayBetweenAttempts=1000。
画面 5: 在代码中调用 Properties 类的 setProperty 方法，弹出方法提示框，显示可设置的属性。
画面 6: 设置 Kafka 的连接属性，包括 bootstrap_servers、group_id 和 auto.offset.reset。
画面 7: 创建 FlinkKafkaConsumer 实例，用于从 Kafka 消费数据。
画面 8: 在代码中调用 DataStream.addSource 方法，弹出方法提示框，显示可设置的源。
画面 9: 设置并行度，调用 map 方法进行数据转换，将字符串解析为 MessageEntity 对象。
画面 10: 设置并行度，调用 map 方法进行数据转换，将字符串解析为 MessageEntity 对象。
画面 11: 调用 addSink 方法，准备将处理后的数据写入 Kafka。
画面 12: 创建 FlinkKafkaProducer 实例，用于将数据写入 Kafka。
画面 13: 定义 map 函数，用于将 MessageEntity 对象转换为字符串。
画面 14: 代码完整显示，包含设置环境、检查点、Kafka 消费者、数据转换、Kafka 生产者等部分。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
无

画面 2:
package com.thema.cold.Flink;
public class StreamingJob {
    public static void main(String[] args) {
        //设置环境信息
        //设置检查点
        //设置流计算
        //设置输出
    }
}

画面 3:
import org.apache.Flink.streaming.api.environment.StreamExecutionEnvironment;
public class StreamingJob {
    public static void main(String[] args) {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置流计算
        //设置输出
    }
}

画面 4:
import org.apache.Flink.streaming.api.environment.CheckpointConfig;
import org.apache.Flink.streaming.api.environment.StreamExecutionEnvironment;
public class StreamingJob {
    public static void main(String[] args) {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置流计算
        //设置输出
    }
}

画面 5:
import java.util.Properties;
public class StreamingJob {
    public static void main(String[] args) {
        //设置环境信息
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置流计算
        //设置输出
    }
}

画面 6:
import java.util.Properties;
public class StreamingJob {
    public static void main(String[] args) {
        //设置环境信息
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置Kafka列属性
        Properties properties = new Properties();
        properties.setProperty("bootstrap.servers", "172.17.0.143:9092");
        properties.setProperty("group.id", "coldlink");
        properties.setProperty("auto.offset.reset", "earliest");
        //设置Kafka列的消费者，接收Kafka发来的数据
        FlinkKafkaConsumer<String> consumer = new FlinkKafkaConsumer<String>(kafla_topic, new SimpleStringSchema(), properties);
        consumer.setStartFromEarliest();
    }
}

画面 7:
import java.util.Properties;
public class StreamingJob {
    public static void main(String[] args) {
        //设置环境信息
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置Kafka列属性
        Properties properties = new Properties();
        properties.setProperty("bootstrap.servers", "172.17.0.143:9092");
        properties.setProperty("group.id", "coldlink");
        properties.setProperty("auto.offset.reset", "earliest");
        //设置Kafka列的消费者，接收Kafka发来的数据
        FlinkKafkaConsumer<String> consumer = new FlinkKafkaConsumer<String>(kafla_topic, new SimpleStringSchema(), properties);
        consumer.setStartFromEarliest();
        //设置流计算
        //设置输出
    }
}

画面 8:
import java.util.Properties;
public class StreamingJob {
    public static void main(String[] args) {
        //设置环境信息
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置Kafka列属性
        Properties properties = new Properties();
        properties.setProperty("bootstrap.servers", "172.17.0.143:9092");
        properties.setProperty("group.id", "coldlink");
        properties.setProperty("auto.offset.reset", "earliest");
        //设置Kafka列的消费者，接收Kafka发来的数据
        FlinkKafkaConsumer<String> consumer = new FlinkKafkaConsumer<String>(kafla_topic, new SimpleStringSchema(), properties);
        consumer.setStartFromEarliest();
        //设置流计算
        DataStream<MessageEntity> stream = env.addSource(consumer)
            .setParallelism(1)
            .map(string -> JSON.parseObject(string, MessageEntity.class));
        //设置输出
    }
}

画面 9:
import java.util.Properties;
public class StreamingJob {
    public static void main(String[] args) {
        //设置环境信息
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置Kafka列属性
        Properties properties = new Properties();
        properties.setProperty("bootstrap.servers", "172.17.0.143:9092");
        properties.setProperty("group.id", "coldlink");
        properties.setProperty("auto.offset.reset", "earliest");
        //设置Kafka列的消费者，接收Kafka发来的数据
        FlinkKafkaConsumer<String> consumer = new FlinkKafkaConsumer<String>(kafla_topic, new SimpleStringSchema(), properties);
        consumer.setStartFromEarliest();
        //设置流计算
        DataStream<MessageEntity> stream = env.addSource(consumer)
            .setParallelism(1)
            .map(string -> JSON.parseObject(string, MessageEntity.class));
        //设置输出
        DataStream<MessageEntity> outStream = stream.map(new MessageAggregate());
        //写入Kafka
        outStream.addSink(new SinkToSQL());
    }
}

画面 10:
import java.util.Properties;
public class StreamingJob {

