# 26_爬虫数据解析保存_综合测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\26_爬虫数据解析保存_综合测试【海量资源尽在 666java.com】.mp4
- 时长 5分10秒（音频 311s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来去测试一下测试下项目好吧刚才咱们已经写完了咱们现在就去测试这个测试的话其实你还是打开之前的测试就可以了还是打开这个然后是正向测试正向测试咱们现在就只测正向就可以好吧然后你打开这个东西咱们可以在这打断点这是断点打着的现在就可以启动一下看看有没有暴速有暴速咱们就改一下好吧就来调试一下先去debug启动走
[00:29] 看看有没有报错啊稍等但是这个启动之前呢我要再去说一下你首先呢去把这当前的这个叫什么叫什么来着mycat启动然后呢是readist要启动啊这最起码你要把这两个启动啊啊还真报错是吧我看看啊说当前这个属性有问题这个不就是咱们之前的叫什么来着是评论那个条件是吧我看看这一块咱们找到当前这个东西啊嗯这
[01:09] 说他这有问题为什么会有问题呢啊对这注入的时候啊这有一个dollar符然后你的字符串里边是不是也有dollar符是吧那这样的话咱们就稍微改一改啊稍微改一改那么怎么改呢咱们就不以这种方式去注入了啊那种方式呢你可以可以参考当前的参考当前的笔记啊用这种直接去勾取跑包意思文件的方式啊直接去拿过来也行啊直接去考过来考过来之后呢咱们可以看一下啊
[01:44] 读的就是叫一个叫做caller的properties然后是里边去拿了一个属性叫sysdn command ur跟这个是一样的是吧然后最终的是这个是他比如说下面引用的时候呢你稍微改一改好吧这时候呢咱们再去走一遍测试再看看行不行啊走咱们在解析这块啊去打个脸啊如果他没报错的话应该是能够先到这啊先到哪啊先到这一块然后是到解析的html这一块啊
[02:22] 应该是到哪啊往上往上啊应该是到这啊咱们在这找点点好吧咱一咱们一会看一下这个效果就可以好吧来往下走他应该先到这啊先到这那这里边呢应该是再去给我加一个当前的什么当前的一个这种解析的模块是吧好你可以把鼠标放到这啊好往下看1234567一个是吧你看这啊这有个call html pass
[02:52] paperland是吧这个不就是持续化那个吗好那咱们这样直接就放行了啊放行之后呢咱们就看一下能不能到这啊到这之后呢说明前面的工作都没事啊包括你的下载是吧还有你的这种什么解析啊但是解析啊解析解析的话咱们说的是那个在当前的页面上去解析啊比如说你有一些解析的规则
[03:18] 是吧现在最终呢咱们到存库的时候呢还是要还是要走这走这咱们再去解析主要是解析这个内容然后呢是把这个存储他现在已经到这了到这之后啊这个东西再多了咱们也可以走咱们也可以直接放行这样吧放行放行之后咱们看一下这个到底能不能存到数据库就可以了那这块内容啊我已经把它干嘛了呢我已经把它给清空了就是CL News已经清空了我直接放行你看啊放行
[03:48] 这块呢是是在走的你看到了吧这块是在走的啊然后呢咱们直接看一下数据库刷新一下看有没有存你看是不是一会就存了那么多没问题吧我呀这个数据是刚刚存的是绝对没问题的啊嗯行那这个这个的话咱们就算是存了啊从结果上看啊咱们的代码写的还是没有问题的OK那这个这个咱们最好是给他关了啊关了啊防止呢是这个出错了是吧来看一看啊
[04:17] 出错的话咱们就看一看当前的现成现成这块是有问题因为因为爬虫的话有的时候有可能会出问题其实出问题的话也属于正常并不是说你所有的文章都能跑下来因为有个别的东西它这个东西可能是跟你你看比如说咱们这个叫什么评论这一块它这个要去组装的话肯定是不行的为啥说不行呢因为它这个东西是一个中文的
[04:48] 是一个中文的那中文的话但与法文的话有可能会出问题的所以说这个属于正常现象大家呢一定要去证实这个问题你说这个怎么还出错呢其实咱们大文都成功了啊只有个别情况是不成功的你爬任何文章基本上都会我爬个人网站吧基本上都会出现这种类似情况好吧行那这个测试啊咱们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

