# 24_爬虫数据解析保存_文章自动审核消息发送

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\24_爬虫数据解析保存_文章自动审核消息发送【海量资源尽在 666java.com】.mp4
- 时长 3分30秒（音频 210s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好继续刚才咱们是把评论给写了一下那这块还报了个错刚才没有看到咱们再重新去设置一下这块内容他说你最终没有return是吧咱们应该把这个是放到下边为了不影响他咱们可以这样可以在这去死在这重新定一个变量就得什么amount url就等于目前的什么呢目前的这个东西
[00:31] 好吧重新负药值然后最终的这个呢都换成他那这样就可以了啊就报错了下面呢咱们就来去完成哪个呢完成当前的发送消息这一块就是让他去自动去审核啊在这呢就写呗其实这个东西咱们之前写过啊主要的是往当前的Kafka中去发一些消息啊说什么呢开始发送
[01:00] 审核文章消息我们的ID是啥可以去设置一下冒号这个呢就是ID是吧下面呢咱们就可以去创建一个对象叫submit article auto里边呢咱们就可以去封装咱们的这种ID又一个submit它然后呢咱们就可以去设置一个这种article ID这个ID呢就是ID
[01:37] 第二个呢咱们要去设立一个类型类型的话呢其实呢你要去设置啊这个里边它呢是一个什么是一个当前的点ArticleType之前咱们是Y为Media是吧现在是Color是一个爬虫是吧最终呢咱们要去调用Kafka咱们要去把这个Kafka呢输入进来privateprivate叫Kafka卡
[02:09] 然后就是他进来之后在这你可以直接发消息有一个submit就是他里边装的不是这个东西他应该还是有一个对象这个对象叫什么submit article叫auth message把他的给拿到之后
[02:43] 然后呢你往里边去设置一个值点set当前一个东西那就把当前上面这个东西啊装进去就可以了然后你把它呢放到这这样的话消息就发出去了啊我们在这去打印一下发送自动审核消息完成我们可以再去设置一个IDID是谁呢当前的ID
[03:16] 那这样的话咱们这个整个流程算是做完了那这个呢只是哪一块流程做完了是不是正向抓取做完了下面咱们就来处理这个反向抓取

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
SubmitArticleAutoMessage (com.heima.comm.Kafka.messages)
```

画面 6:
```java
SubmitArticleAuto (com.heima.model.mess.admin)
SubmitArticleAutoMessage (com.heima.comm.Kafka.messages)
```

画面 7:
```java
SubmitArticleAuto (com.heima.model.mess.admin)
SubmitArticleAutoMessage (com.heima.comm.Kafka.messages)
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

