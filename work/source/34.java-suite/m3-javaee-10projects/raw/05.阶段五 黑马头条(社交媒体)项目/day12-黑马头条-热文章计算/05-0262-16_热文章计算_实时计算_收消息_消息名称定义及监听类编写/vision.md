# 画面线理解：16_热文章计算_实时计算_收消息_消息名称定义及监听类编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\16_热文章计算_实时计算_收消息_消息名称定义及监听类编写【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:14, 01:19, 02:14, 02:34, 03:33, 04:16, 04:54, 05:36, 06:12, 06:46, 07:34, 08:14, 08:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:42:15

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Kafka 实现文章浏览量实时统计功能，包括定义消息实体类、配置 Kafka 主题、编写监听器和处理方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `UpdateArticleMessage` 消息实体类定义，以及 `KafkaSender` 中发送消息的方法。
画面2：展示 `kafka.properties` 配置文件，定义了多个 Kafka 主题，如 `kafka.topic.article-submit`、`kafka.topic.article-audit-success`、`kafka.topic.article-incr-handle`。
画面3：展示 `KafkaTopicConfig` 配置类，定义了多个 Kafka 主题的字符串常量。
画面4：展示 `ArticleVisitStreamMessage` 消息实体类定义，以及 `ArticleVisitStreamDto` 数据传输对象。
画面5：在项目中右键点击，准备新建一个 Java 类。
画面6：展示 `ArticleVisitStreamMessage` 类的完整定义。
画面7：展示 `ArticleVisitStreamDto` 数据传输对象的定义。
画面8：展示 `HotArticleStreamHandler` 监听器类的开始编写。
画面9：展示 `HotArticleStreamHandler` 类中导入的 `@Component` 注解和 `@Autowired` 注解。
画面10：展示 `HotArticleStreamHandler` 类中定义了 `KafkaTopicConfig` 和 `KafkaStream` 的方法。
画面11：在项目中右键点击，准备新建一个 Java 类。
画面12：展示 `ArticleIncrHandleListener` 监听器类的定义，包含 `@Component`、`@Autowired` 注解和 `onMessage` 方法。
画面13：展示 `ArticleIncrHandleListener` 类中 `onMessage` 方法的实现，用于处理 Kafka 消息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public class UpdateArticleMessage extends KafkaMessage<UpdateArticle> {
    public UpdateArticleMessage() {
    }
    public UpdateArticleMessage(UpdateArticle data) {
        super(data);
    }
    @Override
    public String getType() {
        return "update-article";
    }
}
```
```java
/**
 * 发送修改文章请求消息
 */
public void sendArticleUpdateBus(KafkaMessage message) {
    this.messageBus.send(this.kafkaTopicConfig.getArticleUpdateBus(),
            UUID.randomUUID().toString(), message);
}
```

画面2：
```properties
admin.username=admin
admin.password=admin
hostname.eureka.server=localhost
eureka.client.serviceUrl.defaultZone=http://localhost:8701/eureka/

# 文章提交的消费者名称
kafka.topic.submit-article-auth=heima.topic.submit.article.auth.sige.test
kafka.topic.article-audit-success=kafka.topic.article.audit.success.sige.test
kafka.topic.article-incr-handle=kafka.topic.article.incr.handle.sige.test
# app产生的更新文章数据消息
kafka.topic.article-update-bus=heima.topic.app.article.update.bus.test
```

画面3：
```java
package com.heima.common.kafka;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.PropertySources;
import org.springframework.core.env.PropertySourcesPlaceholderConfigurer;

@Configuration
@PropertySources({
        @PropertySource("classpath:kafka.properties")
})
public class KafkaTopicConfig {
    private String submitArticleAuth;
    private String articleAuditSuccess;
    private String articleIncrHandle;
    private String articleUpdateBus;
}
```

画面4：
```java
public class ArticleVisitStreamMessage extends KafkaMessage<ArticleVisitStreamDto> {
    @Override
    public String getType() {
        return "article-visit-stream";
    }
}
```
```java
@Data
public class ArticleVisitStreamDto {
    private Integer articleId;
    private Long view;
    private Long collect;
    private Long comment;
    private Long like;
}
```

画面6：
```java
public class ArticleVisitStreamMessage extends KafkaMessage<ArticleVisitStreamDto> {
    @Override
    public String getType() {
        return "article-visit-stream";
    }
}
```

画面7：
```java
@Data
public class ArticleVisitStreamDto {
    private Integer articleId;
    private Long view;
    private Long collect;
    private Long comment;
    private Long like;
}
```

画面8：
```java
package com.heima.article.stream;

import com.heima.common.kafka.KafkaMessage;
import org.springframework.stereotype.Component;

@Component
public class HotArticleStreamHandler implements KafkaStreamListener<String, String> {
}
```

画面9：
```java
import org.springframework.stereotype.Component;

@Component
public class HotArticleStreamHandler implements KafkaStreamListener<String, String> {
    protected Object clone() { }
    public Package getPackage() { }
    public ProcessBuilder processBuilder() { }
    public Logger getLog() { }
    public boolean equals(Object obj) { }
    public int hashCode() { }
    public String toString() { }
    return null;
}
```

画面10：
```java
public class HotArticleStreamHandler implements KafkaStreamListener<String, String> {
    @Autowired
    private KafkaTopicConfig kafkaTopicConfig;
    @Override
    public String listenerTop() {
        return kafkaTopicConfig.getArticleIncrHandle();
    }
    @Override
    public KStream<String, String> getService(KStream<String, String> stream) {
        return null;
    }
}
```

画面12：
```java
/**
 * 监听类
 */
@Component
public class ArticleIncrHandleListener implements
        com.heima.kafka.KafkaListener<String, String> {
    @Autowired
    KafkaTopicConfig kafkaTopicConfig;
    @Autowired
    ObjectMapper mapper;
    @Autowired
    AppArticleService appArticleService;
    @Override
    public String topic() {
        return kafkaTopicConfig.getArticleIncrHandle();
    }
    @Override
    public void onMessage(ConsumerRecord<String, String> consumerRecord, String consumerGroup) {
    }
}
```

画面13：
```java
import lombok.extern.log4j.Log4j2;
import org.apache.kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
import org.springframework.util.StringUtils;
import org.springframework.util.Assert;

@Component
@Log4j2
public class ArticleIncrHandleListener implements
        com.heima.kafka.KafkaListener<String, String> {
    @Autowired
    private KafkaTopicConfig kafkaTopicConfig;
    @Override
    public String topic() {
        return kafkaTopicConfig.getArticleIncrHandle();
    }
    @Override
    public void onMessage(ConsumerRecord<String, String> consumerRecord, String consumerGroup) {
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“3.1.3 添加发送消息的方法”。
画面4：PPT标题为“3.2.3 定义消息处理的实体类”和“3.2.4 定义监听类，接收流消息”。
画面6：PPT标题为“3.2.3 定义消息处理的实体类”。
画面7：PPT标题为“3.2.3 定义消息处理的实体类”和“3.2.4 定义监听类，接收流消息”。
画面12：PPT标题为“3.2.5 更新文章浏览量”。
画面13：PPT标题为“3.2.5 更新文章浏览量”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
