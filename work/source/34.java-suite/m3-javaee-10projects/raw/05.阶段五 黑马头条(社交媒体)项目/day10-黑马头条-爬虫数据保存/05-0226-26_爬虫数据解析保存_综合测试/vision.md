# 画面线理解：26_爬虫数据解析保存_综合测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\26_爬虫数据解析保存_综合测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:35, 00:50, 01:07, 01:31, 02:06, 02:19, 02:35, 02:58, 03:31, 03:51, 04:08, 04:20, 05:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:17:44

1) 这一组画面整体在讲一个爬虫系统中，如何通过 Java 代码处理解析后的评论数据，并将其发送到 Kafka，同时展示测试过程中因 URL 中非法字符导致的异常。

2) 按时间顺序列出每张画面的要点：

画面1：
要点：展示 `CrawlerHtmlParsePipeline.java` 中的 `buildCommentUrl` 方法，用于构建评论 URL。代码中使用 `ReflectUtils.beanToMap` 将对象转换为 Map，然后遍历 Map 构建 URL。代码中注释“生成评论访问链接”和“@param parseItem”。

画面2：
要点：展示 `ProcessingFlowManagerTest.java` 中的测试类 `ProcessingFlowManager`，测试方法 `test()` 调用 `processingFlowManager.handle()`。控制台显示 Spring Boot 启动日志。

画面3：
要点：测试失败，控制台显示异常堆栈，错误信息为 `PropertySourcesPlaceholderConfigurer` 无法解析属性，导致测试失败。控制台显示“Tests failed”。

画面4：
要点：继续展示 `CrawlerHtmlParsePipeline.java` 中的 `buildCommentUrl` 方法，代码逻辑与画面1一致，但此处光标在 `for` 循环内部。

画面5：
要点：展示一个 PPT 页面，标题为“第3章 爬虫模块”，子标题包括“3.1 爬虫模块类”、“3.2 线程池”、“3.3 爬虫线程”、“3.4 Html解析类”、“3.5 爬虫下载类”、“3.6 爬虫工具类”、“3.7 爬虫流程”、“3.8 CrawlerHtmlParsePipeline类”、“3.9 爬虫配置类”。当前选中“3.8 CrawlerHtmlParsePipeline类”。

画面6：
要点：展示 `CrawlerHtmlParsePipeline.java` 文件，光标在 `buildCommentUrl` 方法的末尾。控制台显示“Compilation completed successfully”。

画面7：
要点：展示 `ProcessingFlowManager.java` 中的 `sendSubmitArticleAutoMessage` 方法，用于发送自动审核文章消息。代码中使用 `SubmitArticleAuto` 类，并设置 `id`。控制台显示日志“开始发送自动审核文章消息”。

画面8：
要点：展示 `ProcessingFlowManager.java` 中的 `startTask` 方法，用于启动爬虫任务。代码中使用 `crawlerConfig.getSpider().start()` 启动爬虫。控制台显示 Netty 和 Spring Boot 的启动日志。

画面9：
要点：展示 `ProcessingFlowManager.java` 中的 `startTask` 方法，光标在 `crawlerConfig.getSpider().start()` 行。调试器显示 `handleType` 的值为 `null`。

画面10：
要点：展示 `ProcessingFlowManager.java` 中的 `handleHtmlData` 方法，用于处理 HTML 数据。代码中使用 `CrawlerThreadPool.submit` 提交任务。控制台显示“开始处理消息”和“Starting ChromeDriver”。

画面11：
要点：展示 `ProcessingFlowManager.java` 中的 `handleHtmlData` 方法，光标在 `Log.info` 行。代码中嵌入了一个 `insertSort` 方法的伪代码，用于演示排序算法。

画面12：
要点：展示 MySQL 数据库管理工具，显示 `news_comments` 表的数据。表中包含 `channel_id`、`labels`、`label_ids`、`original_id`、`created_time`、`submitted_time`、`status`、`publish_time`、`reason`、`article_id` 等字段。当前选中第 31 行数据。

画面13：
要点：展示 `ProcessingFlowManager.java` 中的 `handleHtmlData` 方法，光标在 `Log.info` 行。控制台显示异常堆栈，错误信息为 `URIISyntaxException: Illegal character in path at index 37: https://blog.csdn.net/...`。

画面14：
要点：展示 `ProcessingFlowManager.java` 中的 `handleHtmlData` 方法，光标在 `Log.info` 行。控制台显示异常堆栈，错误信息为 `URIISyntaxException: Illegal character in path at index 57: https://blog.csdn.net/...`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：

画面1：
```java
private String csdn_comment_url;
/*
 * 生成评论访问链接
 * @param parseItem
 * @return
 */
private String buildCommentUrl(CrawlerParseItem parseItem) {
    String buildCommentUrl = csdn_comment_url;
    Map<String, Object> map = ReflectUtils.beanToMap(parseItem);
    for (Map.Entry<String, Object> entry : map.entrySet()) {
        String key = entry.getKey();
        Object value = entry.getValue();
        if (null != value) {
            String sizeValue = value.toString();
            buildCommentUrl = buildCommentUrl.replace("${key}", sizeValue);
        }
    }
    return buildCommentUrl;
}
```

画面2：
```java
@SpringBootTest
@ContextConfiguration(classes = SpringBootRunner.class)
public class ProcessingFlowManagerTest {

    @Autowired
    private ProcessingFlowManager processingFlowManager;

    @Test
    public void test() {
        processingFlowManager.handle();
    }
}
```

画面3：
```java
Tests failed: 12ms PropertySourcesPlaceholderConfigurer. lambda$processProperties$4
```

画面4：
```java
private String csdn_comment_url;
/*
 * 生成评论访问链接
 * @param parseItem
 * @return
 */
private String buildCommentUrl(CrawlerParseItem parseItem) {
    String buildCommentUrl = csdn_comment_url;
    Map<String, Object> map = ReflectUtils.beanToMap(parseItem);
    for (Map.Entry<String, Object> entry : map.entrySet()) {
        String key = entry.getKey();
        Object value = entry.getValue();
        if (null != value) {
            String sizeValue = value.toString();
            buildCommentUrl = buildCommentUrl.replace("${key}", sizeValue);
        }
    }
    return buildCommentUrl;
}
```

画面5：
```markdown
3.8 CrawlerHtmlParsePipeline类
```

画面6：
```java
private String csdn_comment_url;
/*
 * 生成评论访问链接
 * @param parseItem
 * @return
 */
private String buildCommentUrl(CrawlerParseItem parseItem) {
    String buildCommentUrl = csdn_comment_url;
    Map<String, Object> map = ReflectUtils.beanToMap(parseItem);
    for (Map.Entry<String, Object> entry : map.entrySet()) {
        String key = entry.getKey();
        Object value = entry.getValue();
        if (null != value) {
            String sizeValue = value.toString();
            buildCommentUrl = buildCommentUrl.replace("${key}", sizeValue);
        }
    }
    return buildCommentUrl;
}
```

画面7：
```java
private void sendSubmitArticleAutoMessage(Integer id) {
    log.info("开始发送自动审核文章消息。id: {}.", id);
    SubmitArticleAuto submitArticleAuto = new SubmitArticleAuto();
    submitArticleAuto.setId(id);
}
```

画面8：
```java
public void startTask(List<ParseItem> parseItemList, CrawlerHtmlHandleType handleType) {
    processFlowData.setHandleType(handleType);
    processFlowData.setParseItemList(parseItemList);
    for (ProcessFlow processFlow : processFlowList) {
        processFlow.handle(processFlowData);
    }
    crawlerConfig.getSpider().start();
}
```

画面9：
```java
public void startTask(List<ParseItem> parseItemList, CrawlerHtmlHandleType handleType) {
    processFlowData.setHandleType(handleType);
    processFlowData.setParseItemList(parseItemList);
    for (ProcessFlow processFlow : processFlowList) {
        processFlow.handle(processFlowData);
    }
    crawlerConfig.getSpider().start();
}
```

画面10：
```java
public void handleHtmlData(CrawlerParseItem parseItem) {
    long currentTimeMillis = System.currentTimeMillis();
    Log.info("数据被加入线程池进行执行, url: {}, handleType: {}, parseItem.getHandleType(), parseItem.getHandleType());
    CrawlerThreadPool.submit(() -> {
        // 上层逻辑
        if (CrawlerHtmlHandleType.FORWARD.name().equals(parseItem.getHandleType())) {
            Log.info("开始处理消息, url: {}, handleType: {}, parseItem.getHandleType(), parseItem.getHandleType());
            addParseMessage(parseItem);
        }
    });
}
```

画面11：
```java
public void handleHtmlData(CrawlerParseItem parseItem) {
    long currentTimeMillis = System.currentTimeMillis();
    Log.info("数据被加入线程池进行执行, url: {}, handleType: {}, parseItem.getHandleType(), parseItem.getHandleType());
    CrawlerThreadPool.submit(() -> {
        // 上层逻辑
        if (CrawlerHtmlHandleType.FORWARD.name().equals(parseItem.getHandleType())) {
            Log.info("开始处理消息, url: {}, handleType: {}, parseItem.getHandleType(), parseItem.getHandleType());
            addParseMessage(parseItem);
        }
    });
}
```

画面12：
```sql
SELECT * FROM `news_comments` ORDER BY `created_time` DESC LIMIT 0, 1000
```

画面13：
```java
Caused by: java.net.URISyntaxException: Illegal character in path at index 37: https://blog.csdn.net/
