# 画面线理解：01_kafka_kafka封装

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\01_kafka_kafka封装【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:50, 01:43, 02:10, 02:25, 03:02, 03:52, 04:27, 05:39, 05:52, 06:14, 06:43, 07:00, 07:44, 08:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:14:41

1) 这一组画面整体在讲什么（一句话）：
讲解基于 Spring Kafka 的消息自动重试机制，包括 Topic 命名规范、核心组件架构、配置文件、消息实体类、生产者与消费者配置类的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“1.1 功能需求”和“1.2.1 约束定义”部分，其中明确 Topic 命名规范：常量为 heima.topic.{自定义名称}.sigle，治理为 heima.topic.{自定义名称}.bus。
画面2：展示“1.3 实现设计”部分的架构图，图中包含 KafkaMessage、KafkaTopicConfig、KafkaSender、KafkaListenerFactory、KafkaConsumerConfig、KafkaProducerConfig、RetryErrorHandler 等组件及其相互关系。
画面3：展示项目结构，当前选中的是 heima-leadnews-common 模块下的 kafka 包。
画面4：展示“1.4 开发实现”部分，强调 Kafka 功能有独立的配置文件，放置在 src/main/resources/kafka.properties。
画面5：展示 kafka.properties 配置文件内容，其中包含：
kafka.config
kafka.hosts=localhost:9092
kafka.group=heima.{profiles.name}.{spring.application.name}
# 串消息通道，需要以single结尾
kafka.topic.admin-test={kafka.topic.admin-test}
画面6：展示 KafkaMessage.java 文件内容，定义了消息实体类，包含 retry、time、type、data 等字段。
画面7：展示 KafkaSender.java 文件内容，其中包含 sendMessage 方法，使用 kafkaTemplate 发送消息。
画面8：展示 KafkaMessage.java 文件内容，与画面6内容一致。
画面9：展示 KafkaProducerConfig.java 文件内容，其中包含配置属性和默认的 KafkaProducerFactory。
画面10：展示 KafkaSender.java 文件内容，与画面7内容一致。
画面11：展示 KafkaConsumerConfig.java 文件内容，其中包含默认的 KafkaListenerContainerFactory。
画面12：展示 KafkaConsumerConfig.java 文件内容，与画面11内容一致。
画面13：展示 KafkaConsumerConfig.java 文件内容，与画面11内容一致。
画面14：展示 KafkaTopicConfig.java 文件内容，其中包含 String adminTest 字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
kafka.config
kafka.hosts=localhost:9092
kafka.group=heima.{profiles.name}.{spring.application.name}
# 串消息通道，需要以single结尾
kafka.topic.admin-test={kafka.topic.admin-test}

画面6：
public abstract class KafkaMessage<T> {
    @Getter
    int retry;
    // 生成时间
    @Getter
    long time = System.currentTimeMillis();
    // 消息类型
    String type;
    // 消息实体数据
    @Setter
    T data;
    public KafkaMessage() { this.data = data; }
    public void addRetry() { this.retry++; }
    protected abstract String getType();
}

画面9：
@Configuration
@EnableKafka
@PropertySource("classpath:kafka.properties")
public class KafkaProducerConfig {
    private static final int MAX_MESSAGE_SIZE = 16 * 1024 + 1024;
    private String hosts;
    @Autowired(required = false)
    private ProducerListener<String, String> producerListener;
    @Bean
    public DefaultKafkaProducerFactory<String, String> producerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, this.getKafkaHosts());
        props.put(ProducerConfig.RETRIES_CONFIG, 10);
        props.put(ProducerConfig.BUFFER_MEMORY_CONFIG, 5 * 1024);
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        props.put(ProducerConfig.MAX_REQUEST_SIZE_CONFIG, MAX_MESSAGE_SIZE);
        props.put(ProducerConfig.COMPRESSION_TYPE_CONFIG, "lz4");
        return new DefaultKafkaProducerFactory<>(props);
    }

画面11：
@Bean("defaultKafkaListenerContainerFactory")
public ConcurrentKafkaListenerContainerFactory<String, String> kafkaListenerContainerFactory(RetryTemplate retryTemplate, String kafkaGroup) {
    ConcurrentKafkaListenerContainerFactory<String, String> factory = new ConcurrentKafkaListenerContainerFactory<>();
    factory.setRetryTemplate(this.buildRetryTemplate());
    factory.setConcurrency(KafkaConsumerConfig.CONCURRENCY);
    factory.setConsumerFactory(new DefaultKafkaConsumerFactory<>(buildConsumerConfig()));
    factory.setConcurrency(KafkaConsumerConfig.CONCURRENCY);
    return factory;
}

画面14：
package com.heima.common.kafka;
import ...
@Configuration
@ConfigurationProperties(prefix = "kafka.topic")
@PropertySource("classpath:kafka.properties")
public class KafkaTopicConfig {
    String adminTest;
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：架构图中包含以下组件：
- KafkaMessage → KafkaSender
- KafkaMessage → KafkaListenerFactory
- KafkaSender → KafkaProducerConfig
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaProducerConfig → KafkaTopicConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaTopicConfig → KafkaListenerFactory
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
- KafkaSender → KafkaListenerFactory
- KafkaListenerFactory → KafkaConsumerConfig
- KafkaConsumerConfig → KafkaTopicConfig
- KafkaTopicConfig → KafkaSender
