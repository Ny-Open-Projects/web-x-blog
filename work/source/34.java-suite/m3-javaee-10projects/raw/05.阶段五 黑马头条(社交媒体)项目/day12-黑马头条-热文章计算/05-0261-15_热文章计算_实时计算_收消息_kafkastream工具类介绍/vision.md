# 画面线理解：15_热文章计算_实时计算_收消息_kafkastream工具类介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\15_热文章计算_实时计算_收消息_kafkastream工具类介绍【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:18, 01:27, 01:38, 01:48, 01:56, 02:10, 02:23, 02:40, 03:03, 04:03, 04:15, 04:33, 04:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:41:32

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Spring Boot 项目中使用 Kafka Streams 实现热文章的实时处理，包括配置类、监听器接口和处理器类的定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，标题为“2 热文章处理-热数据计算”，当前章节为“3.2 文章微服务接收消息处理”，子章节“3.2.1 导入kafkaStream配置类”，内容说明通过 KafkaStreamListenerFactory 扫描并创建 KafkaStreamProcessor 对象，并调用 doAction 方法进行计算。
画面 2: 展示一个架构图，图中包含“热文章实时处理”、“行为采集”、“用户行为”、“文章热度”、“文章推荐”等模块，以及“Kafka”、“Redis”、“MySQL”等中间件，图中有一个“热文章实时处理”模块指向“Kafka”，“Kafka”指向“Redis”和“MySQL”，“Redis”和“MySQL”分别指向“文章推荐”和“用户行为”模块。
画面 3: 展示 IDEA 项目结构，当前选中包为“com.heima.common”，目录结构包含 admin、article、common、kafka、media、mysql、redis、threadpool、web、zookeeper 等。
画面 4: 展示 IDEA 项目结构，当前选中包为“com.heima.common”，目录结构与画面 3 相同。
画面 5: 展示 IDEA 中的 KafkaStreamConfig.java 文件，光标位于类定义处，右键弹出菜单，选中“Create class KafkaTopicConfig”。
画面 6: 展示 KafkaStreamConfig.java 文件的开头部分，导入了 org.apache.kafka.clients.consumer.ConsumerConfig、org.apache.kafka.common.serialization.Serdes、org.apache.kafka.streams.StreamsConfig、org.apache.kafka.streams.Topology、org.springframework.beans.factory.annotation.Autowired、org.springframework.context.annotation.Configuration、org.springframework.context.annotation.PropertySource、org.springframework.kafka.annotation.EnableKafkaStreams、org.springframework.kafka.config.KafkaStreamsConfiguration、java.util.HashMap、java.util.Map 等包。
画面 7: 展示 KafkaStreamConfig.java 文件中定义的 defaultKafkaStreamConfig 方法，代码中设置了 StreamConfig 的多个属性，包括 BOOTSTRAP_SERVERS_CONFIG、APPLICATION_ID_CONFIG、CLIENT_ID_CONFIG、RETRIES_CONFIG、REPLICATION_FACTOR_CONFIG、RETRY_BACKOFF_MS_CONFIG、SEND_BUFFER_CONFIG、AUTO_OFFSET_RESET_CONFIG。
画面 8: 展示 KafkaStreamConfig.java 文件中定义的 KafkaTopicConfig 类，光标位于类定义处，下方有注释“重定义默认的 KafkaStreams 配置属性，包括：1、服务器地址 2、应用 ID 3、消息的默认大小等配置”。
画面 9: 展示 KafkaStreamListener.java 文件，光标位于接口定义处，接口名为 KafkaStreamListener<T>，包含方法 ListenerTopic()、sendTopic()、getService(T stream)。
画面 10: 展示 KafkaStreamListener.java 文件，光标位于接口定义处，接口名为 KafkaStreamListener<T>，包含方法 ListenerTopic()、sendTopic()、getService(T stream)。
画面 11: 展示 KafkaStreamProcessor.java 文件，光标位于方法定义处，方法名为 doAction()，代码中使用了 KStream 和 KTable 对象进行流处理。
画面 12: 展示 KafkaStreamProcessor.java 文件，光标位于类定义处，类名为 KafkaStreamProcessor，包含属性 streamBuilder、listener，以及构造函数和 parseType() 方法。
画面 13: 展示 KafkaStreamListener.java 文件，光标位于接口定义处，接口名为 KafkaStreamListener<T>，包含方法 ListenerTopic()、sendTopic()、getService(T stream)。
画面 14: 展示课程 PPT 页面，标题为“2 热文章处理-热数据计算”，当前章节为“3.2 文章微服务接收消息处理”，子章节“3.2.2 定义消息名称”和“3.2.3 定义消息处理的实体类”，内容说明定义消息处理实体类为 com.heima.common.kafka.messages.app.ArticleVisitStreamMessage。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
```java
@Data
@Configuration
@EnableKafkaStreams
@PropertySource("classpath:kafka.properties")
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
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.Topology;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.kafka.annotation.EnableKafkaStreams;
import org.springframework.kafka.config.KafkaStreamsConfiguration;
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
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, this.getProps("kafka"));
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
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, this.getProps("kafka"));
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
