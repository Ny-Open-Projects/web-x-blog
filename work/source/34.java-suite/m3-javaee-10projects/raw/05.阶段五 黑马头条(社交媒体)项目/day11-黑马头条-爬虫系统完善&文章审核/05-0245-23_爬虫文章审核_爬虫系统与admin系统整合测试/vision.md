# 画面线理解：23_爬虫文章审核_爬虫系统与admin系统整合测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\23_爬虫文章审核_爬虫系统与admin系统整合测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:27, 01:05, 01:37, 02:03, 02:30, 02:56, 03:21, 03:55, 04:15, 04:46, 05:24, 05:44, 06:15, 06:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:30:40

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Kafka 的文章自动审核系统，包括消息监听器、测试用例、代理IP更新机制以及数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 显示 IntelliJ IDEA 中的项目结构，选中了 `heima-leadnews-admin` 模块。
- 编辑器中显示 `ReviewArticleTest.java` 文件，其中包含一个测试方法 `testReviewCrawler`，调用 `reviewCrawlerArticleService.autoReviewArticleByCrawler(35181)`。

画面2：
- 显示 `AutoReviewArticleListener.java` 文件。
- 代码中定义了 `@Autowired` 的 `ObjectMapper mapper` 和 `ReviewMediaArticleService`。
- `onMessage` 方法中，从 Kafka 消息中读取并解析 `SubmitArticleAuthMessage`，根据消息类型（`PENDED` 或 `CRAWLER`）调用不同的审核服务。

画面3：
- 在 `onMessage` 方法中，对 `articleId` 进行判断，如果为 `null`，则调用 `reviewMediaArticleService.autoReviewArticleByMedia(articleId)`。
- 代码中有一个 `else if` 分支，处理 `CRAWLER` 类型的消息。

画面4：
- 显示 `AutoReviewArticleListener.java` 文件。
- 代码中定义了 `@Autowired` 的 `KafkaTopicConfig`、`ObjectMapper`、`ReviewMediaArticleService` 和 `ReviewCrawlerArticleService`。
- `onMessage` 方法中，从 Kafka 消息中读取并解析 `SubmitArticleAuthMessage`，根据消息类型（`PENDED` 或 `CRAWLER`）调用不同的审核服务。

画面5：
- 显示项目结构，选中了 `heima-leadnews-crawler` 模块。
- 编辑器中显示 `AutoReviewArticleListener.java` 文件，代码与画面2、3相同。

画面6：
- 显示项目结构，选中了 `heima-leadnews-crawler` 模块。
- 编辑器中显示 `AutoReviewArticleListener.java` 文件，代码与画面2、3相同。

画面7：
- 显示项目结构，选中了 `heima-leadnews-crawler` 模块。
- 编辑器中显示 `AutoReviewArticleListener.java` 文件，代码与画面2、3相同。
- 控制台显示了 Kafka 消费者分配分区的日志。

画面8：
- 显示项目结构，选中了 `heima-leadnews-crawler` 模块。
- 编辑器中显示 `JobTest.java` 文件，其中包含一个测试方法 `test`，使用 `while (true)` 循环。

画面9：
- 显示 `JobTest.java` 文件。
- 代码中定义了 `@Autowired` 的 `KafkaSender`。
- `test` 方法中，创建了一个 `SubmitArticleAuto` 对象，设置其 `articleId` 和 `articleType`，并创建 `SubmitArticleAuthMessage`，然后调用 `kafkaSender.sendSubmitArticleAuthMessage(authMessage)`。

画面10：
- 显示 Navicat for MySQL 的界面。
- 数据库表 `crawler_oriz_job` 中显示了多行数据，包含 `content`、`type`、`channel_id`、`label_ids`、`original_time`、`created_time`、`submitted_time` 等字段。

画面11：
- 显示 `JobTest.java` 文件。
- 控制台显示了测试运行日志，包括 Spring Boot 测试上下文配置、连接到目标 JVM、测试类加载等信息。

画面12：
- 显示 `ProxyUpdateQuartz.java` 文件。
- 代码中定义了 `@Autowired` 的 `ProxyManager` 和 `CrawlerProxyProvider`。
- `executeInternal` 方法中，记录日志，调用 `proxyManager.updateProxy()` 和 `crawlerProxyProvider.updateProxy()`。

画面13：
- 显示 `JobTest.java` 文件。
- 代码中显示了 `try` 块，从 Kafka 消息中读取并解析 `SubmitArticleAuthMessage`，获取 `type` 字段。

画面14：
- 显示 `AutoReviewArticleListener.java` 文件。
- 代码中显示了 `if (articleId != null)` 条件，调用 `reviewMediaArticleService.autoReviewArticleByMedia(articleId)`。
- 控制台显示了测试通过的日志，包括 `DEBUG` 级别的日志信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Autowired
private ReviewCrawlerArticleService reviewCrawlerArticleService;

@Test
public void testReviewCrawler() throws Exception {
    reviewCrawlerArticleService.autoReviewArticleByCrawler(35181);
}
```

画面2：
```java
@Autowired
private ObjectMapper mapper;
@Autowired
private ReviewMediaArticleService reviewMediaArticleService;

@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}

@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    try {
        SubmitArticleAuthMessage message = mapper.readValue(value, SubmitArticleAuthMessage.class);
        if (message == null) {
            SubmitArticleAuto.ArticleType type = message.getData().getTypes();
            if (type == SubmitArticleAuto.ArticleType.PENDED) {
                Integer articleId = message.getData().getArticleId();
                if (articleId != null) {
                    //审核文章信息
                    reviewMediaArticleService.autoReviewArticleByMedia(articleId);
                } else if (type == SubmitArticleAuto.ArticleType.CRAWLER) {
                    Integer articleId = message.getData().getArticleId();
                    if (articleId != null) {
                        //审核爬虫文章信息
                        reviewCrawlerArticleService.autoReviewArticleByCrawler(articleId);
                    }
                }
            }
        }
    } catch (IOException e) {
        e.printStackTrace();
        log.error("处理自动审核文章错误：{}, {}", e.getMessage(), e);
        throw new RuntimeException("WS消息处理错误");
    }
}
```

画面3：
```java
if (articleId != null) {
    //审核文章信息
    reviewMediaArticleService.autoReviewArticleByMedia(articleId);
} else if (type == SubmitArticleAuto.ArticleType.CRAWLER) {
    Integer articleId = message.getData().getArticleId();
    if (articleId != null) {
        //审核爬虫文章信息
        reviewCrawlerArticleService.autoReviewArticleByCrawler(articleId);
    }
}
```

画面4：
```java
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
@Autowired
private ObjectMapper mapper;
@Autowired
private ReviewMediaArticleService reviewMediaArticleService;
@Autowired
private ReviewCrawlerArticleService reviewCrawlerArticleService;

@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}

@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    try {
        SubmitArticleAuthMessage message = mapper.readValue(value, SubmitArticleAuthMessage.class);
        if (message == null) {
            SubmitArticleAuto.ArticleType type = message.getData().getTypes();
            if (type == SubmitArticleAuto.ArticleType.PENDED) {
                Integer articleId = message.getData().getArticleId();
                if (articleId != null) {
                    //审核文章信息
                    reviewMediaArticleService.autoReviewArticleByMedia(articleId);
                } else if (type == SubmitArticleAuto.ArticleType.CRAWLER) {
                    Integer articleId = message.getData().getArticleId();
                    if (articleId != null) {
                        //审核爬虫文章信息
                        reviewCrawlerArticleService.autoReviewArticleByCrawler(articleId);
                    }
                }
            }
        }
    } catch (IOException e) {
        e.printStackTrace();
        log.error("处理自动审核文章错误：{}, {}", e.getMessage(), e);
        throw new RuntimeException("WS消息处理错误");
    }
}
```

画面5：
```java
try {
    SubmitArticleAuthMessage message = mapper.readValue(value, SubmitArticleAuthMessage.class);
    if (message == null) {
        SubmitArticleAuto.ArticleType type = message.getData().getTypes();
        if (type == SubmitArticleAuto.ArticleType.PENDED) {
            Integer articleId = message.getData().getArticleId();
            if (articleId != null) {
                //审核文章信息
                reviewMediaArticleService.autoReviewArticleByMedia(articleId);
            } else if (type == SubmitArticleAuto.ArticleType.CRAWLER) {
                Integer articleId = message.getData().getArticleId();
                if (articleId != null) {
                    //审核爬虫文章信息
                    reviewCrawlerArticleService.autoReviewArticleByCrawler(articleId);
                }
            }
        }
    }
} catch (IOException e) {
    e.printStackTrace();
    log.error("处理自动审核文章错误：{}, {}", e.getMessage(), e);
    throw new RuntimeException("WS消息处理错误");
}
```

画面6：
```java
try {
    SubmitArticleAuthMessage message = mapper.readValue(value, SubmitArticleAuthMessage.class);
    if
