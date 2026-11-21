# 画面线理解：17_自媒体文章自动审核_自媒体发布文章发送消息

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\17_自媒体文章自动审核_自媒体发布文章发送消息【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:30, 02:07, 02:59, 04:34, 05:58, 06:58, 08:14, 09:26, 10:32, 11:38, 12:50, 14:36, 15:28, 16:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:28:02

1) 这一组画面整体在讲什么（一句话）：
实现自媒体文章发布成功后，通过 Kafka 发送认证消息的完整流程，包括配置、消息实体、发送器和业务逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了文档中“2.2.4 自媒体发布文章成功后发送消息”章节。
- 代码片段：`kafka.topic.submit-article-auth=submit-article-auth`（在 `maven_test.properties` 中）。
- 代码片段：`String submitArticleAuth;`（在 `KafkaTopicConfig` 类中）。
- 代码片段：`public class SubmitArticleAuto { ... }`（定义消息类型）。

画面 2：
- 展示了 `KafkaTopicConfig` 类的代码，其中包含 `@Configuration` 注解和 `@PropertySource` 注解。
- 代码片段：`@Configuration`。
- 代码片段：`@PropertySource("classpath:kafka.properties")`。
- 代码片段：`String adminTest;`。

画面 3：
- 展示了 `SubmitArticleAuto` 类的代码，定义了 `ArticleType` 枚举。
- 代码片段：`public enum ArticleType{ WEMEDIA, CRAWLER; }`。

画面 4：
- 展示了 `SubmitArticleAuthMessage` 类的代码，它继承自 `KafkaMessage`。
- 代码片段：`public class SubmitArticleAuthMessage extends KafkaMessage { ... }`。

画面 5：
- 展示了 `KafkaMessage` 抽象类的代码，定义了消息的通用属性。
- 代码片段：`public abstract class KafkaMessage { ... }`。
- 代码片段：`int retry;`。
- 代码片段：`String type;`。
- 代码片段：`protected abstract String getType();`。

画面 6：
- 展示了 `KafkaSender` 类的代码，其中包含 `KafkaTemplate` 和 `ObjectMapper`。
- 代码片段：`public class KafkaSender { ... }`。
- 代码片段：`@Autowired KafkaTemplate<String, String> kafkaTemplate;`。
- 代码片段：`@Autowired ObjectMapper mapper;`。
- 代码片段：`public void sendMessage(String topic, String key, KafkaMessage<?> message) { ... }`。

画面 7：
- 展示了 `KafkaSender` 类的 `sendMessage` 方法的实现。
- 代码片段：`public void sendMessage(String topic, String key, KafkaMessage<?> message) { ... }`。
- 代码片段：`this.kafkaTemplate.send(topic, key, mapper.writeValueAsString(message));`。

画面 8：
- 展示了 `SubmitArticleAuthMessage` 类的 `getType` 方法。
- 代码片段：`public String getType() { return "submit-article-auth"; }`。

画面 9：
- 展示了 `AdminMessageSender` 类的代码，它使用 `KafkaSender`。
- 代码片段：`public class AdminMessageSender { ... }`。
- 代码片段：`private KafkaSender kafkaSender;`。

画面 10：
- 展示了 `AdminMessageSender` 类的 `sendMessage` 方法的实现。
- 代码片段：`public void sendMessage(SubmitArticleAuthMessage message) { ... }`。
- 代码片段：`kafkaSender.sendMessage(topic, key, message);`。

画面 11：
- 展示了 `NewsServiceImpl` 类的 `saveNews` 方法。
- 代码片段：`private void saveNews(News news, int countImageNum, Short type) { ... }`。
- 代码片段：`if (countImageNum == ValidaConstants.WM_NEWS_SINGLE_IMAGE) { ... }`。
- 代码片段：`else if (countImageNum == ValidaConstants.WM_NEWS_MANY_IMAGES) { ... }`。
- 代码片段：`else { ... }`。

画面 12：
- 展示了 `NewsServiceImpl` 类的 `saveNews` 方法中，根据文章状态发送认证消息的逻辑。
- 代码片段：`if (ValidaConstants.WM_NEWS_SUBMIT_STATUS == type) { ... }`。
- 代码片段：`SubmitArticleAuthMessage message = new SubmitArticleAuthMessage();`。
- 代码片段：`SubmitArticleAuto submitArticleAuto = new SubmitArticleAuto();`。
- 代码片段：`submitArticleAuto.setArticleType(SubmitArticleAuto.ArticleType.WEMEDIA);`。
- 代码片段：`message.setData(submitArticleAuto);`。

画面 13：
- 展示了 `NewsServiceImpl` 类的 `saveNews` 方法中，设置文章状态和创建时间。
- 代码片段：`news.setCreatedTime(new Date());`。
- 代码片段：`news.setEnable(true);`。
- 代码片段：`news.setStatus(type);`。

画面 14：
- 展示了 `NewsServiceImpl` 类的 `saveNews` 方法中，创建 `SubmitArticleAuthMessage` 并设置数据。
- 代码片段：`SubmitArticleAuthMessage message = new SubmitArticleAuthMessage();`。
- 代码片段：`SubmitArticleAuto submitArticleAuto = new SubmitArticleAuto();`。
- 代码片段：`submitArticleAuto.setArticleType(SubmitArticleAuto.ArticleType.WEMEDIA);`。
- 代码片段：`message.setData(submitArticleAuto);`。
- 代码片段：`adminMessageSender.sendMessage(message);`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
- `kafka.topic.submit-article-auth=submit-article-auth`
- `String submitArticleAuth;`

画面 2：
- `@Configuration`
- `@PropertySource("classpath:kafka.properties")`
- `String adminTest;`

画面 3：
- `public enum ArticleType{ WEMEDIA, CRAWLER; }`

画面 4：
- `public class SubmitArticleAuthMessage extends KafkaMessage { ... }`

画面 5：
- `public abstract class KafkaMessage { ... }`
- `int retry;`
- `String type;`
- `protected abstract String getType();`

画面 6：
- `public class KafkaSender { ... }`
- `@Autowired KafkaTemplate<String, String> kafkaTemplate;`
- `@Autowired ObjectMapper mapper;`
- `public void sendMessage(String topic, String key, KafkaMessage<?> message) { ... }`

画面 7：
- `public void sendMessage(String topic, String key, KafkaMessage<?> message) { ... }`
- `this.kafkaTemplate.send(topic, key, mapper.writeValueAsString(message));`

画面 8：
- `public String getType() { return "submit-article-auth"; }`

画面 9：
- `public class AdminMessageSender { ... }`
- `private KafkaSender kafkaSender;`

画面 10：
- `public void sendMessage(SubmitArticleAuthMessage message) { ... }`
- `kafkaSender.sendMessage(topic, key, message);`

画面 11：
- `private void saveNews(News news, int countImageNum, Short type) { ... }`
- `if (countImageNum == ValidaConstants.WM_NEWS_SINGLE_IMAGE) { ... }`
- `else if (countImageNum == ValidaConstants.WM_NEWS_MANY_IMAGES) { ... }`
- `else { ... }`

画面 12：
- `if (ValidaConstants.WM_NEWS_SUBMIT_STATUS == type) { ... }`
- `SubmitArticleAuthMessage message = new SubmitArticleAuthMessage();`
- `SubmitArticleAuto submitArticleAuto = new SubmitArticleAuto();`
- `submitArticleAuto.setArticleType(SubmitArticleAuto.ArticleType.WEMEDIA);`
- `message.setData(submitArticleAuto);`

画面 13：
- `news.setCreatedTime(new Date());`
- `news.setEnable(true);`
- `news.setStatus(type);`

画面 14：
- `SubmitArticleAuthMessage message = new SubmitArticleAuthMessage();`
- `SubmitArticleAuto submitArticleAuto = new SubmitArticleAuto();`
- `submitArticleAuto.setArticleType(SubmitArticleAuto.ArticleType.WEMEDIA);`
- `message.setData(submitArticleAuto);`
- `adminMessageSender.sendMessage(message);`

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
