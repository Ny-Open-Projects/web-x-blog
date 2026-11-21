# 画面线理解：24_爬虫数据解析保存_文章自动审核消息发送

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\24_爬虫数据解析保存_文章自动审核消息发送【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:17, 00:41, 01:18, 01:32, 01:39, 01:45, 02:00, 02:05, 02:16, 02:34, 02:45, 03:02, 03:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:16:13

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中通过 IDE 编辑器编写和调试处理文章评论数据、发送审核消息及与 Kafka 消息队列交互的代码逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 `CrawlerNewsParsePipeline.java` 文件中 `addCommentData` 方法，用于处理评论数据并调用 `crawlerNewsCommentService.saveNewsComment` 保存评论。
画面 2: 展示 `buildCommentUrl` 方法，通过反射将 `parseItem` 中的键值对拼接成评论 URL。
画面 3: 展示 `sendSubmitArticleAutoMessage` 方法的声明，用于发送审核文章消息。
画面 4: 在 `sendSubmitArticleAutoMessage` 方法中，开始输入 `String` 类型的变量名，IDE 提供了 `String` 类的自动补全建议。
画面 5: 在 `sendSubmitArticleAutoMessage` 方法中，输入 `submitArticleAuto`，IDE 提供了 `SubmitArticleAuto` 类的自动补全建议。
画面 6: 在 `sendSubmitArticleAutoMessage` 方法中，输入 `submitArticleAuto`，IDE 提供了 `SubmitArticleAuto` 类的自动补全建议。
画面 7: 在 `sendSubmitArticleAutoMessage` 方法中，输入 `submitArticleAuto`，IDE 提供了 `SubmitArticleAuto` 类的自动补全建议。
画面 8: 在 `sendSubmitArticleAutoMessage` 方法中，创建 `SubmitArticleAuto` 实例并设置文章 ID 和类型。
画面 9: 在 `sendSubmitArticleAutoMessage` 方法中，输入 `private` 关键字，IDE 提供了 `private` 作用域的自动补全建议。
画面 10: 在 `sendSubmitArticleAutoMessage` 方法中，声明 `@Autowired private KafkaSender kafkaSender;` 用于注入 Kafka 发送器。
画面 11: 在 `sendSubmitArticleAutoMessage` 方法中，调用 `kafkaSender.sendSubmitArticleAutoMessage();` 发送消息。
画面 12: 在 `sendSubmitArticleAutoMessage` 方法中，IDE 提供了 `kafkaSender.sendSubmitArticleAutoMessage();` 方法的自动补全建议。
画面 13: 在 `sendSubmitArticleAutoMessage` 方法中，IDE 提供了 `log` 类的自动补全建议。
画面 14: 展示 `handleHtmlData` 方法，根据 `handleType` 判断是正向还是反向处理，并调用 `updateAdditional(parseItem);`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 添加评论数据
 * @param parseItem
 * @param cNews
 */
private void addCommentData(CrawlerParseItem parseItem, CNews cNews) {
    long currentTimMillis = System.currentTimeMillis();
    log.info("开始获取文章评论数据");
    List<CNewsComment> commentList = getCommentData(parseItem);
    if (null != commentList && commentList.isEmpty()) {
        for (CNewsComment cNewsComment : commentList) {
            cNewsComment.setNewsId(cNews.getId());
            crawlerNewsCommentService.saveNewsComment(cNewsComment);
        }
    }
    log.info("获取文章评论数据完成, 耗时: 0", System.currentTimeMillis()-currentTimMillis);
}
```

画面 2:
```java
/**
 * 构建评论链接
 * @param parseItem
 * @return
 */
private String buildCommentUrl(CrawlerParseItem parseItem) {
    Map<String, Object> map = ReflectUtils.beanToMap(parseItem);
    for (Map.Entry<String, Object> entry : map.entrySet()) {
        String key = entry.getKey();
        String buildKey = "${" + key + "}";
        Object value = entry.getValue();
        if (null == value) {
            csdnCommentUrl = csdnCommentUrl.replace(buildKey, "");
        }
    }
    return csdnCommentUrl;
}
```

画面 3:
```java
/**
 * 发送信息，审核文章
 * @param id
 */
private void sendSubmitArticleAutoMessage(Integer id) {
    log.info("开始发送自动审核文章消息。id: 0", id);
}
```

画面 4:
```java
String (java.lang)
System (java.lang)
StringBuilder (java.lang)
StringBuffer (java.lang)
Short (java.lang)
```

画面 5:
```java
SubmitArticleAuto (com.heima.model.mess.admin)
SubmitArticleAutoMessage (com.heima.comm.kafka.messages)
```

画面 6:
```java
SubmitArticleAuto (com.heima.model.mess.admin)
SubmitArticleAutoMessage (com.heima.comm.kafka.messages)
```

画面 7:
```java
SubmitArticleAuto (com.heima.model.mess.admin)
SubmitArticleAutoMessage (com.heima.comm.kafka.messages)
```

画面 8:
```java
private void sendSubmitArticleAutoMessage(Integer id) {
    log.info("开始发送自动审核文章消息。id: 0", id);
    SubmitArticleAuto submitArticleAuto = new SubmitArticleAuto();
    submitArticleAuto.setArticleId(id);
    submitArticleAuto.setType(SubmitArticleAuto.ArticleType.CRAWLER);
}
```

画面 9:
```java
private
```

画面 10:
```java
@Autowired
private KafkaSender kafkaSender;
```

画面 11:
```java
kafkaSender.sendSubmitArticleAutoMessage();
```

画面 12:
```java
kafkaSender.sendSubmitArticleAutoMessage();
```

画面 13:
```java
log
```

画面 14:
```java
@Override
public void handleHtmlData(CrawlerParseItem parseItem) {
    long currentTimMillis = System.currentTimeMillis();
    log.info("文章数据加入线程池进行执行，url: 0, handleType: 0", parseItem.getUrl(), parseItem.getHandleType());
    HtmlThreadPool.submit(() -> {
        if (CrawlerEnum.HandleType.FORWARD.name().equals(parseItem.getHandleType())) {
            // 正向处理
        } else if (CrawlerEnum.HandleType.REVERSE.name().equals(parseItem.getHandleType())) {
            updateAdditional(parseItem);
        }
    });
    log.info("处理文章数据结束，url: 0, handleType: 0", parseItem.getUrl(), parseItem.getHandleType(), System.currentTimeMillis()-currentTimMillis);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
