# 04_爬虫系统完善_逆向抓取测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\04_爬虫系统完善_逆向抓取测试【海量资源尽在 666java.com】.mp4
- 时长 3分15秒（音频 196s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去测试一下当前这个逆向的处理啊其实跟咱们正向的其实差不多啊只是调的方法不一样啊咱们现在呢就还是打开当下那个processing flow manager test在这下边你再去拷贝一个方法这个咱们叫reverse好吧这个方法叫reverse好测试之前的你首先呢你得保证你当前这个CL news additional当前这个附加信息表啊必须有数据并且并且呢
[00:35] nice update要小于小于当前时间小于你的当前时间好做完之后下面咱们就可以去测一下当然这个redis要起还有买cat也要启动好吧这我就不再多说了下面咱们就来去执行测试咱们在这打断点我在这已经打断点了这就是逆向处理的这种方法好来走一遍执行看看他能不能到这
[01:09] 然后呢他到这之后他会去执行这个start task然后呢他就会去执行上面这个方法是吧然后最终的就会去执行这里边组件的一个一个去调用就可以了好吧稍等一下咱们看一看咱们也可以打开谁呀打开当前那个pass pass里边的有一个这种pass color smr pass ppland然后这里边啊到这了是吧这里边咱们
[01:41] 逆向的时候咱们会去走一个东西走这你看我这打断点了他就会去走当前更新走这个更新他们应该会走到这才对好吧要是正向的话他就会去走这东西是去添加那种这是更新那种好吧来咱们看一下当前咱们可以往下走一步往下走你可以看一下这里边是有一条数据是吧就是刚才我加的这条数据好加完之后咱们下面就可以去处理了
[02:11] 然后他就会去调用start task好直接放行能到这是吧这里边呢还是咱们这七个组件加进来了没有问题然后最终呢他就会去走到这走到这啊他应该走这咱们直接放行啊看看能不能到这走稍等咱们刷一下啊10月23咱们也可以看日志啊你看这些是不是正常的下点你看这不是逆向都是逆向对吧好到这了啊
[02:47] 到了之后呢咱们可以直接让他放行啊直接放行放行啊放行之后啊这块的内容就算是走完了啊走完了走完之后呢你可以看一下当前的数据有没有更新你看这个是不是更新到了28看到吧这个13啊他呢每次都会把这时间给改了他就会去告诉你会修改你当前这段数据的什么下一次更新的时间好吧请他这个啊这个逆向爬举呢咱们就来说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个新闻爬虫系统中，处理反向增量数据的 Java 服务类及其测试类的代码逻辑和运行过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 `ProcessingFlowManagerTest.java` 测试类中的 `test1()` 方法，用于测试 `processingFlowManager.handle1()` 方法。
画面 2：展示 `ProcessingFlowManagerTest.java` 中的 `@Test` 方法 `test1()`，调用 `processingFlowManager.handle1()` 并休眠。
画面 3：展示 Redis 服务器的监控界面，显示客户端连接数和内存使用情况。
画面 4：展示 `ProcessingFlowManager.java` 中的 `handleReverseData()` 方法，处理反向增量数据。
画面 5：展示 `ProcessingFlowManager.java` 中的 `handleReverseData()` 方法，包含 `crawlerNewsAdditionalService` 的调用。
画面 6：展示 `ProcessingFlowManager.java` 中的 `handleReverseData()` 方法，包含 `parseItemList` 的处理逻辑。
画面 7：展示 `ProcessingFlowManager.java` 中的 `startTask()` 方法，用于启动数据处理任务。
画面 8：展示 `CrawlerHtmlParsePipeline.java` 中的 `updateAdditional()` 方法，用于更新附加数据。
画面 9：展示 `CrawlerHtmlParsePipeline.java` 中的 `handleHtmlData()` 方法，根据 `handleType` 判断处理逻辑。
画面 10：展示 `ProcessingFlowManager.java` 中的 `reverseHandle()` 方法，调用 `handleReverseData()`。
画面 11：展示 `ProcessingFlowManager.java` 中的 `reverseHandle()` 方法，显示 `parseItemList` 的大小。
画面 12：展示 `CrawlerHtmlParsePipeline.java` 中的 `handleHtmlData()` 方法，处理不同 `handleType` 的数据。
画面 13：展示 `SeleniumClient` 初始化日志，显示 ChromeDriver 启动成功。
画面 14：展示 MySQL 数据库 `c_news_additional` 表的数据，显示 `likes`、`comment`、`forward` 等字段的值。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
@Test
public void test1() {
    processingFlowManager.handle1();
    try {
        Thread.sleep(Integer.MAX_VALUE);
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
}
```

画面 4：
```java
private void handleReverseData(List<ParseItem> parseItemList) {
    if (null != parseItemList && !parseItemList.isEmpty()) {
        for (ParseItem parseItem : parseItemList) {
            parseItem.setDocumentType(CrawlerEnum.DocumentType.PAGE.name());
            parseItem.setHandelType(CrawlerEnum.HandelType.REVERSE.name());
        }
    }
}
```

画面 5：
```java
private void reverseHandle() {
    List<ParseItem> parseItemList = crawlerNewsAdditionalService.queryIncrementParseItem(new Date());
    handleReverseData(parseItemList);
    log.info("开始进行数据逆向更新，增量数据数量为：0，parseItemList.size()：{}", parseItemList.size());
    if (null != parseItemList && !parseItemList.isEmpty()) {
        startTask(parseItemList, CrawlerEnum.HandelType.REVERSE);
    } else {
        log.info("增量数据为空不能进行数据更新");
    }
}
```

画面 6：
```java
private void handleReverseData(List<ParseItem> parseItemList) {
    if (null != parseItemList && !parseItemList.isEmpty()) {
        for (ParseItem parseItem : parseItemList) {
            parseItem.setDocumentType(CrawlerEnum.DocumentType.PAGE.name());
            parseItem.setHandelType(CrawlerEnum.HandelType.REVERSE.name());
        }
    }
}
```

画面 7：
```java
public void startTask(List<ParseItem> parseItemList, CrawlerEnum.HandelType handelType) {
    ProcessFlowData processFlowData = new ProcessFlowData();
    processFlowData.setHandelType(handelType);
    processFlowData.setParseItemList(parseItemList);
    processFlowData.start();
}
```

画面 8：
```java
public void updateAdditional(CrawlerParseItem parseItem) {
    long currentTimeMillis = System.currentTimeMillis();
    if (null != parseItem) {
        cNewsAdditional.setReadCount(parseItem.getReadCount());
        cNewsAdditional.setComment(parseItem.getCommentCount());
        cNewsAdditional.setLike(parseItem.getLikeCount());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional.setUpdateTime(new Date());
        cNewsAdditional

