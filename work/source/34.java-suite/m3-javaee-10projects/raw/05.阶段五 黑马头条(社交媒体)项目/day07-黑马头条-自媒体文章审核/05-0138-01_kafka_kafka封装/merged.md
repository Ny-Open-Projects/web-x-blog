# 01_kafka_kafka封装

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\01_kafka_kafka封装【海量资源尽在 666java.com】.mp4
- 时长 8分51秒（音频 531s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好的下面咱们就来去说一下卡普卡的封装好首先咱们来看一下第一个是功能需求那说现在的是消息对于现代软件项目来说占有很重要的地位是吧现在产品有很多比如说ActiveMQRubyMQ卡普卡是吧还有RockyMQ还有最近比较火热的一个叫Porsa是吧像这些都是一些消息中间件那为什么要用卡普卡呢
[00:29] 这份其实有一个优点在这去说一下说它是支持大数据量的高层图实时流量计算等功能实践咱们都可以用卡不卡来做好吧行那这个东西咱们就不再去介绍了下面咱们就直接去说一下在咱们项目中怎么去集成当前卡不卡中间件首先咱们要去明确一些定义这边定义其实就是大家比较好理解的
[00:56] 消息和多消息啊说要是单消息咱们这边是呃前面是黑马套逼个啊黑马点套逼个是开头然后是后面是一个single结尾啊single结尾这是个命名规范啊都说是混合类也就是多多消息啊多消息那这时候呢咱们还是以黑马套逼个开头下面呢是buzz结尾buzz结尾啊当然中间的这部分啊这部分的内容呢就是你的具体的业务
[01:23] 记着业务名称这个可以自定义是吧当然跟你的业务相匹配就可以了好吧行那这个是命名的一个约束啊大家要遵循当前这个命名才行好吧行那这个说完之后啊下面还有一些类那这类呢其实有很多啊这些呢都是自己奉装的啊一些类这个类呢你可以直接去到当前的资料中当前的资料中啊这个资料呢是在哪呢是在当前的这个
[01:50] 第07里边有个资料资料里边有一个卡不卡封装的工具类这里边你可以直接拷贝一下用完之后咱们还是老套路直接去放哪放到咱们的common工程下面他就是在这去创建一个包比如要卡我卡好吧点ok然后你可以把这些类拷过来拷过来这个类咱们就拷过来了拷过来之后你要想去连上的话首先你还得去在这去创建一个配置文件
[02:21] 咱们在这去创建配置文件啊这配置文件叫啥呢咱们可以笔记保持一致啊这叫Kafka点跑跑历史好吧行咱们可以把这个内容给拷过来在这去创建一个Kafka跑跑历史然后呢刚才内容拷过来很显然上面的这个呢是你的怎么去连接上你的Kafka然后呢下面这东西呢就是什么呢哎就是咱们的一个组这个组暂时用不着大家知道一下就可以然后还有一个啊
[02:53] 最后咱们这个其实都是以single结尾什么意思就是单通道的一个消息当然也有可能是多通道多通道怎么着多通道的话就是bus结尾是吧这是以single结尾是吧现在这个其实就是一个测试的消息的名称这个是怎么来的大家都知道咱们之前写过是吧都是在哪写都是在当前的test环境provide环境deevee环境是吧这时候从这里边去读的
[03:21] 从这里边去读的也就是说你要去定义消息名称怎么办呢首先你在这定义然后让他去读读完之后在你的具体的配置类中去读取当前这个配种件就可以了这是咱们通常是都是这么做的行那这个配种文件咱们算是准备好了好吧准备好之后咱们在这去看一下当前这个类这个类其实有很多是吧那这样咱们主要的是看几个主要看几个首先大家要知道
[03:50] 知道第一个呢是可否改的message那这个类的其实就是去封装了什么呢封装了当前的消息内容他这个消息内容的话不仅仅是包含了内容还包含了啥呢还包含了当前的时间就是你创建消息的时间还有什么呢还有你的类型啊你消息的类型这些都要考虑到所以说咱们在自己去封装消息的时候应该去继承当前的可否改message这是一个类啊
[04:20] 行,咱们再往下看一个啊还有一个比较重要的类就是当前的卡普卡点Send那这个Send是啥呢其实Send里边啊里边去注入了一个卡普卡Template这个Template大家应该很熟是吧一般这个类呢都是一些工具模板类是吧比如说咱们之前学过的Radius Template是吧还有什么Solar Template等等像这些呢都是Spring帮你封装之后的一类
[04:47] 然后这个类里边就可以去调用一些方法进行这个卡布卡就是来用来干嘛发送消息发送消息你看这里边卡布卡就可以直接点send然后你就可以传三个参数就可以发消息了第一个就是topic就是你的消息的名称t就是一个字幕串这个字幕串可以定义无所谓你写上啥都行然后下面这个第三个参数就是你的什么
[05:14] 就是你的message就是你的具体的消息的内容哎对就是具体消息的内容好吧行那这是一些东西这是一些你看这他这个类型啥呢是Kafkamessage是谁呀就是当前这个Kafkamessage就是他好吧行那这个啊这几个类大家知道啊当然这个那你说这个template是怎么来的呢其实啊咱们在这其实已经封装了咱们可以看一下当前下面这个这些描述啊然后往下找找啊就这个类啊
[05:44] 这个里面其实有一个produsrconfig咱们打开Kafka.produsrconfig这里边其实就是怎么去连上当前这个house这个house就怎样house就是当前的当前这个地址是吧你看这个地址就是你怎么去连上你的Kafka然后最终的这里边其实看这个方法大家熟悉吧这个方法就是去让Spring去管理了一个
[06:11] Kafkatemplate然后这时候呢咱们在Kafkasender里边就能去用当前这个template了然后呢你就可以去发消息了好吧行那这是一个内容啊当然那除了这个内容之外呢咱们还有一个接收啊这是发送吗那接收怎么接收呢接收的话其实里边还有一个叫Kafkalisten这东西呢其实就是接收消息的咱们所有接收消息的监听类都要去实现当前这个接口实现这个接口然后是声明你的消息
[06:41] 然后最终的那怎么连呢其实都是有一个Kafka康费康熊猫康费克这里边有个号其实连的是同一个当前的什么Kafka软件是吧当然这里边设置了很多的参数啊大家看一下就可以好吧最终你要能知道最终是咱们的生产者和消费者都要去连接当前的Kafka才能去接收到消息
[07:04] 行那这是一个啊还有一个类啊大家必须要知道的类就是当前这个producer config啊不对啊这个这个叫topic config那这个类是干嘛的呢这个类是这样啊这个类你看最终啊你看他是不是读了一个Kafka叫popolis啊是吧他读完之后呢他设置个前置然后呢就是这个这东西是admin test很显然这东西是谁啊
[07:32] 这东西是不是读取了当前的Kafka点Proportis然后最终呢最终就能去读取到这个值读取到这个值它就能去拿到你具体的消息的名称具体的消息的名称所以说咱们要以后在发消息的时候啊首先呢你要在这定义你的消息是吧定义完之后呢你需要在当前这个KafkaTopic Config中去加入怎么去读
[08:02] 读到你的消息然后最终呢你才能使用最终你才能使用啊那这个具体怎么使用咱们一会儿去做一个例子因为他呢做完例子之后啊咱们会非常清晰的就能够知道啊咱们到底该怎么去设置其实呢这个呢最终让谁要用呢让当前发送消息的时候这个这个topic其实就是在那读的呀就是通过当前这个类当前这个类去读取的一段信息
[08:29] 好吧行那这个呢其实就是一些类啊这个呢大家呢能理解就可以把类考过来之后之后呢咱们呢又会做一个缩压测试能够去编写当前的什么当前的生产者和消费者拿到消息之后啊这样的事就算是完成了好吧行那这个卡普卡的介绍和封装啊咱们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解基于 Spring Kafka 的消息自动重试机制，包括 Topic 命名规范、核心组件架构、配置文件、消息实体类、生产者与消费者配置类的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“1.1 功能需求”和“1.2.1 约束定义”部分，其中明确 Topic 命名规范：常量为 heima.topic.{自定义名称}.sigle，治理为 heima.topic.{自定义名称}.bus。
画面2：展示“1.3 实现设计”部分的架构图，图中包含 KafkaMessage、KafkaTopicConfig、KafkaSender、KafkaListenerFactory、KafkaConsumerConfig、KafkaProducerConfig、RetryErrorHandler 等组件及其相互关系。
画面3：展示项目结构，当前选中的是 heima-leadnews-common 模块下的 Kafka 包。
画面4：展示“1.4 开发实现”部分，强调 Kafka 功能有独立的配置文件，放置在 src/main/resources/Kafka.properties。
画面5：展示 Kafka.properties 配置文件内容，其中包含：
Kafka.config
Kafka.hosts=localhost:9092
Kafka.group=heima.{profiles.name}.{spring.application.name}
# 串消息通道，需要以single结尾
Kafka.topic.admin-test={Kafka.topic.admin-test}
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
Kafka.config
Kafka.hosts=localhost:9092
Kafka.group=heima.{profiles.name}.{spring.application.name}
# 串消息通道，需要以single结尾
Kafka.topic.admin-test={Kafka.topic.admin-test}

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
@PropertySource("classpath:Kafka.properties")
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
package com.heima.common.Kafka;
import ...
@Configuration
@ConfigurationProperties(prefix = "Kafka.topic")
@PropertySource("classpath:Kafka.properties")
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

