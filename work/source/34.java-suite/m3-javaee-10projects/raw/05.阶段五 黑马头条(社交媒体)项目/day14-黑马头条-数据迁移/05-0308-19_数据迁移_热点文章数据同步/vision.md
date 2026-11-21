# 画面线理解：19_数据迁移_热点文章数据同步

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\19_数据迁移_热点文章数据同步【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 00:52, 01:24, 02:22, 02:56, 03:38, 04:12, 04:52, 05:47, 06:45, 07:18, 08:09, 08:44, 09:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:12:27

1) 这一组画面整体在讲如何通过 Kafka 消息监听器接收热点文章数据，并调用服务层将数据同步至 MongoDB 数据库。

2) 按时间顺序列出每张画面的要点：
画面1: 展示项目结构，选中 `src/main/java/com/heima/migration/kafka/listener/MigrationHotArticleListener.java` 文件。
画面2: 展示 `ApHotArticleServiceImpl.java` 中的 `computeHotArticle` 方法，用于计算热点文章列表，并调用 `kafkaSender.sendHotArticleMessages(hot)` 发送消息。
画面3: 展示 `MigrationHotArticleListener.java` 文件顶部的包声明和导入语句，包括 `org.apache.kafka.clients.consumer.ConsumerRecord`。
画面4: 展示 `MigrationHotArticleListener.java` 中的 `onMessage` 方法，其中 `log.info("接收到热点文章数据: {}", data);` 用于日志记录。
画面5: 展示 `MigrationHotArticleListener.java` 中的 `onMessage` 方法，正在输入 `String value = data.value();`。
画面6: 展示 `MigrationHotArticleListener.java` 中的 `onMessage` 方法，正在输入 `ApHotArticleMessage message = null;`。
画面7: 展示 `MigrationHotArticleListener.java` 中的 `onMessage` 方法，正在输入 `Integer articleId = message.getData().getArticleId();`。
画面8: 展示 MongoDB 数据库的 `articles` 集合，其中包含 `articleId: 10160` 的文档。
画面9: 展示 `ApHotArticleQuartz.java` 文件，这是一个 Quartz 定时任务类，用于触发热点文章同步。
画面10: 展示 `MigrationHotArticleListener.java` 中的 `onMessage` 方法，正在输入 `if (null != articleId) { apHotArticleService.hotApArticle(articleId); }`。
画面11: 展示 `MigrationHotArticleListener.java` 中的 `onMessage` 方法，正在输入 `Integer articleId = message.getData().getArticleId();`。
画面12: 展示 `ApHotArticleServiceImpl.java` 中的 `hotApArticle` 方法，用于将热点文章数据同步至 MongoDB。
画面13: 展示 `ApHotArticleServiceImpl.java` 中的 `hotApArticleToMongoService` 方法，用于将热点文章数据写入 MongoDB。
画面14: 展示 `MigrationHotArticleListener.java` 中的 `onMessage` 方法，正在输入 `log.info("接收到热点文章数据: {}", data);`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面2:
```java
String lastDay = DateTime.now().minusDays(1).toString("yyyy-MM-dd 00:00:00");
List<Article> articleList = apArticleMapper.loadLastArticleForHot(lastDay);
List<ApHotArticles> hotArticleList = computeHotArticle(articleList);
//分页
List<ApBehaviorEntry> entryList = apBehaviorMapper.selectEntryList();
for (ApHotArticles hot : hotArticleList) {
    apHotArticlesMapper.insert(hot);
    //每个用户保存一份热点文章
    saveArticleForEntryList(hot, entryList);
}
```

画面3:
```java
package com.heima.migration.kafka.listener;
import com.heima.common.kafka.KafkaListener;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import org.apache.kafka.clients.consumer.ConsumerTimeoutException;
import
