# 画面线理解：18_数据迁移_文章审核后同步数据

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\18_数据迁移_文章审核后同步数据【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 02:05, 03:13, 03:54, 04:47, 05:35, 06:27, 08:28, 09:47, 10:32, 11:31, 12:30, 13:09, 14:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:11:36

1) 这一组画面整体在讲：文章审核成功后，通过 Kafka 发送消息，触发异步数据同步到数据库的流程。

2) 按时间顺序列出每张画面的要点：
画面1：展示数据库表 ap_article 的数据，包含 likes、collection、comment、views、province_id、city_id、county_id、created_time、publish_time、sync_status、origin 等字段，当前查询语句为 SELECT * FROM ap_article LIMIT 0, 1000。
画面2：展示 KafkaSender.java 文件内容，包含 sendSubmitArticleAuthMessage、sendArticleAuditSuccessMessage、sendArticleUpdateBus 方法，用于发送不同类型的 Kafka 消息。
画面3：展示 ReviewMediaArticleServiceImpl.java 文件内容，包含审核成功后发送用户消息的逻辑，调用 kafkaSender.sendArticleAuditSuccessMessage。
画面4：展示 ReviewMediaArticleServiceImpl.java 文件内容，包含审核成功后更新文章状态和发送用户消息的逻辑。
画面5：展示 ReviewMediaArticleServiceImpl.java 文件内容，包含审核成功后更新文章状态和发送用户消息的逻辑，其中注释“文章审核成功”。
画面6：展示 MigrationAuditSuccessArticleListener.java 文件内容，包含 onMessage 方法，用于处理 Kafka 消息。
画面7：展示 MigrationAuditSuccessArticleListener.java 文件内容，包含 onMessage 方法，用于处理 Kafka 消息。
画面8：展示 MigrationAuditSuccessArticleListener.java 文件内容，包含 sendSubmitArticleAuthMessage、sendArticleAuditSuccessMessage、sendArticleUpdateBus 方法。
画面9：展示 MigrationAuditSuccessArticleListener.java 文件内容，包含 onMessage 方法，用于处理 Kafka 消息。
画面10：展示 MigrationAuditSuccessArticleListener.java 文件内容，包含 onMessage 方法，用于处理 Kafka 消息。
画面11：展示 ArticleQuantityService.java 文件内容，包含 getArticleQuantityList 方法，用于获取文章数量列表。
画面12：展示 ReviewArticleTest.java 文件内容，包含测试审核成功后发送消息的逻辑。
画面13：展示 ArticleQuantityService.java 文件内容，包含 dbToBase 方法，用于将数据同步到数据库。
画面14：展示 ArticleQuantityService.java 文件内容，包含 dbToBase 方法，用于将数据同步到数据库，日志显示“异步数据库到base同步完成”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```java
public void sendSubmitArticleAuthMessage(SubmitArticleAuthMessage message) {
    this.sendMessage(kafkaTopicConfig.getSubmitArticleAuth(), UUID.randomUUID().toString(), message);
}

public void sendArticleAuditSuccessMessage(ArticleAuditSuccessMessage message) {
    ArticleAuditSuccessMessage temp = new ArticleAuditSuccessMessage();
    temp.setData(message);
    this.sendMessage(kafkaTopicConfig.getArticleAuditSuccess(), UUID.randomUUID().toString(), temp);
}

public void sendArticleUpdateBus(KafkaMessage message) {
    this.sendMessage(kafkaTopicConfig.getArticleUpdateBus(), UUID.randomUUID().toString(), message);
}
```

画面3：
```java
kafkaSender.sendArticleAuditSuccessMessage(articleAuditSuccess);
ApUserMessage apUserMessage = new ApUserMessage();
apUserMessage.setUserId(awdewo.getUserId());
apUserMessage.setCreatedTime(new Date());
apUserMessage.setIsRead(false);
apUserMessage.setContent("文章审核成功");
apUserMessage.setTypeId(108);
apUserMessageMapper.insertSelective(apUserMessage);
```

画面4：
```java
if (result != null && !result.isSuccessed()) {
    log.error("插入文章索引失败。message: {}", result.getErrorMessage());
}
//修改windows的状态为 9
wifone.setArticleId(apArticle.getId());
updateWindows(windows, short4, message); //审核成功
kafkaSender.sendArticleAuditSuccessMessage(articleAuditSuccess);
```

画面6：
```java
import com.heima.common.kafka.KafkaListener;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.OffsetAndMetadata;
import org.apache.kafka.clients.consumer.OffsetCommitCallback;
import org.apache.kafka.clients.consumer.OffsetResetStrategy;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.TopicPartition;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache
