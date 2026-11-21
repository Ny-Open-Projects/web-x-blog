# 15_热文章计算_实时计算_收消息_kafkastream工具类介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\15_热文章计算_实时计算_收消息_kafkastream工具类介绍【海量资源尽在 666java.com】.mp4
- 时长 4分54秒（音频 294s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续啊下面咱们有一个叫做文章微服务的接收消息处理那这块呢咱们采用的是当前的Kafka斯专门流的方式去接收消息咱们呢可以再打开之前那个图那咱们目前其实做完的呢其实就是下面这一块啊比如说这块咱们已经做完了咱们打击了用户的行为比如说点赞和阅读然后呢那这时候啊
[00:27] 我们的文章段呢要去接收消息那这个接收的方式呢就是用流的方式去接收那流的方式有什么好处吗那就是可以实时的去接收只要是他发送消息啊我就要去接收消息并且呢那这个呢咱们还可以做一个这种聚合运算做一个时间窗口比如说我每十秒钟十秒钟干嘛呢接收一次那接收完一次之后呢我再统一去处理当前的十秒钟
[00:56] 聚合的数据然后再去处理然后下一个10秒咱们再去处理这样的话咱们就保证了当前的一个流逝的这种实时的信息的接收好吧那行那这是一个介绍那这时候你要想去用当前的卡普卡Stream这时候你首先得要干嘛呢得需要去把相关的配置类考到咱们的项目中这个配置类其实已经提供了就在当前的今天的资料文件夹中有一个卡普卡
[01:26] 然后你直接把它拨备一下拷到哪呢拷到当前的common打开在这去创建一个包叫卡普卡好然后这创建完之后啊直接去拷贝过来就可以啊那有没有报错我们打开当前的卡普卡config这个咱们需要找下包然后呢然后这块是有问题啊咱们就去删除一下就可以了啊那这样的话就不会报错了啊那这个呢其实就是一个这种
[01:59] 你看这就是把当前的什么configuration对象重新设置一下参数并且放到了Sprint容器中你看这加了一个admin看到了吧这里边就是去设置了一些属性比如说咱们的连接还有一些这种调优的一些信息好吧这个大家可以知道一下就可以行这个就是咱们的一个配置类也就是说咱们以后想在项目中去引用当前的KabookaStream怎么办
[02:27] 你需要去加入或者扫描当前的KafkaStream这个包就可以了那具体该怎么去用呢那具体用的方式呢其实呢咱们这里边有有三个类啊咱们需要去说一说啊那这个类呢第一个类呢就是呃自定义的一个接口就是一个KafkaStreamListener这个是一个范形T啊这个范形T呢是有两种方式一个是KStream一个是KTable啊当然这个呢咱们用的是一般都是流啊一般都是流流势啊咱们本项目中用的都是流啊
[02:58] 那这里边是有三个参数咱们可以简单说一说那这三个参数呢第一个呢就是你监听的类型你发送的类型还有你处理业务逻辑的一个一个东西或者是算是一个方法其实这三个都是方法是吧也就是说什么意思呢我可以去接收消息我也可以干嘛呢我也可以去发送消息我也可以发送消息啊也就是说同时去接收也可以同时去发送消息啊这就是理由
[03:28] 好那这个呢这是一个自定义的接口那你说那你说该怎么去用呢是这样啊咱们所有的这种消息处理的类呢都要去实现当前的接口那个实现的接口之后呢这时候里边还有一个类他呢就会去扫描当前卡布卡StreamListener这个接口啊他实现这个接口的所有的类
[03:53] 然后呢把它给注册并且去干嘛呢并且呢去把它呢是有一个叫做执行当前的processor to action其实呢就是东西中的咱们会用到一个extreme然后呢是去处理咱们的流逝计算好了啊那这个呢其实就是配置啊你直接考过来现在我再去总结一下你现在啊你现在所有的这种监听的类
[04:21] 不管是发送还是接收他们都要干嘛呢都要去实现当前这个接口里边是有三个方法这三个方法呢就是一个是我可以接收消息我可以发送消息我还可以处理对象的逻辑这个逻辑呢其实都是在Stream中去保存着的比如说你的消息那你去接收的时候其实通过Stream都可以去拿到你想要的消息
[04:47] 好吧那行那这个呢就是咱们的一个工具列啊咱们就试到这啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Spring Boot 项目中使用 Kafka Streams 实现热文章的实时处理，包括配置类、监听器接口和处理器类的定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，标题为“2 热文章处理-热数据计算”，当前章节为“3.2 文章微服务接收消息处理”，子章节“3.2.1 导入kafkaStream配置类”，内容说明通过 KafkaStreamListenerFactory 扫描并创建 KafkaStreamProcessor 对象，并调用 doAction 方法进行计算。
画面 2: 展示一个架构图，图中包含“热文章实时处理”、“行为采集”、“用户行为”、“文章热度”、“文章推荐”等模块，以及“Kafka”、“Redis”、“MySQL”等中间件，图中有一个“热文章实时处理”模块指向“Kafka”，“Kafka”指向“Redis”和“MySQL”，“Redis”和“MySQL”分别指向“文章推荐”和“用户行为”模块。
画面 3: 展示 IDEA 项目结构，当前选中包为“com.heima.common”，目录结构包含 admin、article、common、Kafka、media、mysql、redis、threadpool、web、ZooKeeper 等。
画面 4: 展示 IDEA 项目结构，当前选中包为“com.heima.common”，目录结构与画面 3 相同。
画面 5: 展示 IDEA 中的 KafkaStreamConfig.java 文件，光标位于类定义处，右键弹出菜单，选中“Create class KafkaTopicConfig”。
画面 6: 展示 KafkaStreamConfig.java 文件的开头部分，导入了 org.apache.Kafka.clients.consumer.ConsumerConfig、org.apache.Kafka.common.serialization.Serdes、org.apache.Kafka.streams.StreamsConfig、org.apache.Kafka.streams.Topology、org.springframework.beans.factory.annotation.Autowired、org.springframework.context.annotation.Configuration、org.springframework.context.annotation.PropertySource、org.springframework.Kafka.annotation.EnableKafkaStreams、org.springframework.Kafka.config.KafkaStreamsConfiguration、java.util.HashMap、java.util.Map 等包。
画面 7: 展示 KafkaStreamConfig.java 文件中定义的 defaultKafkaStreamConfig 方法，代码中设置了 StreamConfig 的多个属性，包括 BOOTSTRAP_SERVERS_CONFIG、APPLICATION_ID_CONFIG、CLIENT_ID_CONFIG、RETRIES_CONFIG、REPLICATION_FACTOR_CONFIG、RETRY_BACKOFF_MS_CONFIG、SEND_BUFFER_CONFIG、AUTO_OFFSET_RESET_CONFIG。
画面 8: 展示 KafkaStreamConfig.java 文件中定义的 KafkaTopicConfig 类，光标位于类定义处，下方有注释“重定义默认的 KafkaStreams 配置属性，包括：1、服务器地址 2、应用 ID 3、消息的默认大小等配置”。
画面 9: 展示 KafkaStreamListener.java 文件，光标位于接口定义处，接口名为 KafkaStreamListener<T>，包含方法 ListenerTopic()、sendTopic()、getService(T stream)。
画面 10: 展示 KafkaStreamListener.java 文件，光标位于接口定义处，接口名为 KafkaStreamListener<T>，包含方法 ListenerTopic()、sendTopic()、getService(T stream)。
画面 11: 展示 KafkaStreamProcessor.java 文件，光标位于方法定义处，方法名为 doAction()，代码中使用了 KStream 和 KTable 对象进行流处理。
画面 12: 展示 KafkaStreamProcessor.java 文件，光标位于类定义处，类名为 KafkaStreamProcessor，包含属性 streamBuilder、listener，以及构造函数和 parseType() 方法。
画面 13: 展示 KafkaStreamListener.java 文件，光标位于接口定义处，接口名为 KafkaStreamListener<T>，包含方法 ListenerTopic()、sendTopic()、getService(T stream)。
画面 14: 展示课程 PPT 页面，标题为“2 热文章处理-热数据计算”，当前章节为“3.2 文章微服务接收消息处理”，子章节“3.2.2 定义消息名称”和“3.2.3 定义消息处理的实体类”，内容说明定义消息处理实体类为 com.heima.common.Kafka.messages.app.ArticleVisitStreamMessage。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
```java
@Data
@Configuration
@EnableKafkaStreams
@PropertySource("classpath:Kafka.properties")
public class KafkaStreamConfig {
    private static final int MAX_MESSAGE_SIZE = 16 * 1024 * 1024;
    @Autowired
    KafkaTopicConfig kafkaTopicConfig;
    private String hosts;
    private String group;
}
```

画面 6:
```java
import lombok.Data;
import org.apache.Kafka.clients.consumer.ConsumerConfig;
import org.apache.Kafka.common.serialization.Serdes;
import org.apache.Kafka.streams.StreamsConfig;
import org.apache.Kafka.streams.Topology;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.Kafka.annotation.EnableKafkaStreams;
import org.springframework.Kafka.config.KafkaStreamsConfiguration;
import java.util.HashMap;
import java.util.Map;
```

画面 7:
```java
@Configuration
public class KafkaStreamConfig {
    @Bean
    public KafkaStreamsConfiguration defaultKafkaStreamConfig() {
        Properties props = new HashMap<>();
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, this.getProps("Kafka"));
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, this.getProps("stream_id"));
        props.put(StreamsConfig.CLIENT_ID_CONFIG, this.getProps("stream_cid"));
        props.put(StreamsConfig.RETRIES_CONFIG, 10);
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.REPLICATION_FACTOR_CONFIG, 3);
        props.put(StreamsConfig.RETRY_BACKOFF_MS_CONFIG, 5_000);
        props.put(StreamsConfig.SEND_BUFFER_CONFIG, 3 * MAX_MESSAGE_SIZE);
        props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, Topology.AutoOffsetReset.EARLIEST.name().toLowerCase());
        return new KafkaStreamsConfiguration(props);
    }
}
```

画面 8:
```java
@Configuration
public class KafkaStreamConfig {
    @Bean
    public KafkaStreamsConfiguration defaultKafkaStreamConfig() {
        Properties props = new HashMap<>();
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, this.getProps("Kafka"));
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, this.getProps("stream_id"));
        props.put(StreamsConfig.CLIENT_ID_CONFIG, this.getProps("stream_cid"));
        props.put(StreamsConfig.RETRIES_CONFIG, 10);
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.REPLICATION_FACTOR_CONFIG, 3);
        props.put(StreamsConfig.RETRY_BACKOFF_MS_CONFIG, 5_000);
        props.put(StreamsConfig.SEND_BUFFER_CONFIG, 3 * MAX_MESSAGE_SIZE);
        props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, Topology.AutoOffsetReset.EARLIEST.name().toLowerCase());
        return new KafkaStreamsConfiguration(props);
    }
}
```

画面 9:
```java
public interface KafkaStreamListener<T> {
    // 监听的类型
    String listenerTopic();
    // 处理消息发送的类
    String sendTopic();
    // 对象处理逻辑
    T getService(T stream);
}
```

画面 10:
```java
public interface KafkaStreamListener<T> {
    // 监听的类型
    String listenerTopic();
    // 处理消息发送的类
    String sendTopic();
    // 对象处理逻辑
    T getService(T stream);
}
```

画面 11:
```java
public Object doAction() {
    if ("kstream".equals(this.type)) {
        KStream<?, ?> stream = streamBuilder.stream(listener.listenerTopic(), Consumed.with(Topology.AutoOffsetReset.LATEST));
        streamF(KStream.listener, getService(stream));
        stream.to(listener.sendTopic());
        return stream;
    } else {
        KTable<?, ?> table = streamBuilder.table(listener.listenerTopic(), Consumed.with(Topology.AutoOffsetReset.LATEST));
        table = (KTable) listener, getService(table);
        table.to(listener.sendTopic());
        return table;
    }
}
```

画面 12:
```java
public class KafkaStreamProcessor {
    // 流构建器
    StreamBuilder streamBuilder;
    // 监听器
    KafkaStreamListener listener;
    private String type;

    public KafkaStreamProcessor(StreamBuilder streamBuilder, KafkaStreamListener kafkaStreamListener) {
        this.streamBuilder = streamBuilder;
        this.listener = kafkaStreamListener;
        this.parseType();
    }

    public void parseType() {
        Assert.notNull(this.type, message: "Kafka Stream 监听器只支持kstream、ktable，当前类型是" + this.type);
    }
}
```

画面 13:
```java
public interface KafkaStreamListener<T> {
    // 监听的类型
    String listenerTopic();
    // 处理消息发送的类
    String sendTopic();
    // 对象处理逻辑

