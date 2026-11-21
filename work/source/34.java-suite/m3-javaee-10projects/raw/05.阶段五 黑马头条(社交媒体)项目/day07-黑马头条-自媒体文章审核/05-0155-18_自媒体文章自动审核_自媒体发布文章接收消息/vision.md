# 画面线理解：18_自媒体文章自动审核_自媒体发布文章接收消息

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\18_自媒体文章自动审核_自媒体发布文章接收消息【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:59, 01:18, 01:52, 02:24, 03:19, 03:46, 04:04, 04:39, 05:16, 05:37, 06:20, 07:09, 08:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:28:54

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 Kafka 消费者监听器处理文章自动审核消息，并通过对象映射器解析消息体并调用服务处理。

2) 按时间顺序列出每张画面的要点：
画面1: 展示项目结构，选中 `heima-leadnews-admin` 模块，准备进入代码编辑。
画面2: 打开 `AutoReviewArticleListener.java` 文件，显示类定义和导入语句。
画面3: 在 `AutoReviewArticleListener` 类中添加 `@Component` 注解，并定义 `topic()` 和 `onMessage()` 方法的骨架。
画面4: 在 `@Component` 注解下方，使用 `@Autowired` 注解注入 `KafkaTopicConfig`。
画面5: 定义 `topic()` 方法，返回 `kafkaTopicConfig.getSubmitArticleAuth()`。
画面6: 在 `onMessage()` 方法中，使用 `kafkaTemplate` 发送消息，但画面焦点在 `KafkaSender.java` 文件。
画面7: 在 `onMessage()` 方法中，使用 `ObjectMapper` 解析消息体。
画面8: 使用 `ObjectMapper` 将字符串解析为 `SubmitArticleAuthMessage` 对象。
画面9: 在 `onMessage()` 方法中，对解析出的对象进行非空判断。
画面10: 在 `onMessage()` 方法中，根据消息类型进行判断，使用 `SubmitArticleAuto.ArticleType` 枚举。
画面11: 在 `onMessage()` 方法中，根据消息类型判断是否为 `MEDIA` 类型。
画面12: 在 `onMessage()` 方法中，调用 `reviewMediaArticleService` 服务处理媒体文章。
画面13: 在 `onMessage()` 方法中，添加 `catch` 块处理异常。
画面14: 完成 `onMessage()` 方法，显示最终代码结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```java
package com.heima.admin.kafka;
import com.heima.common.kafka.KafkaListener;
public class AutoReviewArticleListener implements KafkaListener<String, String> {
```

画面3:
```java
import com.heima.common.kafka.KafkaListener;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Override
public String topic() {
    return null
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {

}
```

画面4:
```java
import com.heima.common.kafka.KafkaListener;
import com.heima.common.kafka.KafkaTopicConfig;
import org.apache.kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {

}
```

画面5:
```java
import com.heima.common.kafka.KafkaListener;
import com.heima.common.kafka.KafkaTopicConfig;
import org.apache.kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
}
```

画面6:
```java
public class KafkaSender {
    private KafkaTemplate<String, String> kafkaTemplate;
    private KafkaTopicConfig kafkaTopicConfig;
    public void sendMessage(String topic, String key, String message) {
        try {
            this.kafkaTemplate.send(topic, key, message);
        } catch (Exception e) {
            logger.error("send message to {} error: {}", topic, e);
        }
    }
    public void sendSubmitArticleAuthMessage(SubmitArticleAuthMessage message) {
        this.kafkaTemplate.send(kafkaTopicConfig.getSubmitArticleAuth(), UUID.randomUUID().toString(), message);
    }
}
```

画面7:
```java
import com.heima.common.kafka.KafkaListener;
import com.heima.common.kafka.KafkaTopicConfig;
import org.apache.kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper mapper;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
}
```

画面8:
```java
import com.heima.common.kafka.KafkaListener;
import com.heima.common.kafka.KafkaTopicConfig;
import org.apache.kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper mapper;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    SubmitArticleAuthMessage message = mapper.readValue(value, SubmitArticleAuthMessage.class);
}
```

画面9:
```java
import com.heima.common.kafka.KafkaListener;
import com.heima.common.kafka.KafkaTopicConfig;
import org.apache.kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper mapper;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    SubmitArticleAuthMessage message = mapper.readValue(value, SubmitArticleAuthMessage.class);
    if (message == null) {
        message.getData().getArticleId();
    }
}
```

画面10:
```java
import com.heima.common.kafka.KafkaListener;
import com.heima.common.kafka.KafkaTopicConfig;
import org.apache.kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper mapper;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    SubmitArticleAuthMessage message = mapper.readValue(value, SubmitArticleAuthMessage.class);
    if (message == null) {
        message.getData().getArticleId();
    }
    if (message.getData().getArticleType() == 0) {
        message.getData().getArticleId();
    }
}
```

画面11:
```java
import com.heima.common.kafka.KafkaListener;
import com.heima.common.kafka.KafkaTopicConfig;
import org.apache.kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper mapper;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    SubmitArticleAuthMessage message = mapper.readValue(value, SubmitArticleAuthMessage.class);
    if (message == null) {
        message.getData().getArticleId();
    }
    if (message.getData().getArticleType() == 0) {
        message.getData().getArticleId();
    }
}
```

画面12:
```java
import com.heima.common.kafka.KafkaListener;
import com.heima.common.kafka.KafkaTopicConfig;
import org.apache.kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper mapper;
private ReviewMediaArticleService reviewMediaArticleService;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    SubmitArticleAuthMessage message = mapper.readValue(value, SubmitArticleAuthMessage.class);
    if (message == null) {
        message.getData().getArticleId();
    }
    if (message.getData().getArticleType() == 0) {
        message.getData().getArticleId();
    }
}
```

画面13:
```java
import com.heima.common.kafka.KafkaListener;
import com.heima.common.kafka.KafkaTopicConfig;
import org.apache.kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig
