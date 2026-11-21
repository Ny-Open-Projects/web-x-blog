# 23_爬虫文章审核_爬虫系统与admin系统整合测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\23_爬虫文章审核_爬虫系统与admin系统整合测试【海量资源尽在 666java.com】.mp4
- 时长 6分41秒（音频 401s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就继续啊刚才呢咱们是用单元测试的方式把咱们那个自动审核那个逻辑啊已经测完了啊出现的问题呢咱们也已经解决了啊然后下面呢咱们就去整合一下那整合啥呢整合的是当前caller他去采集文章的同时呢要去发送消息是吧这时候呢我要去审核审核文章那怎么审核呢就是admin端去接收消息去审核
[00:30] 这时候呢他应该发的是某一条文章的ID对吧那行那咱们下面呢先去来去完成当前什么当前去接收消息怎么去接收啊其实发送消息的代码咱们写完了吗之前是不是在去采集的时候已经把这个写写完了呀好那咱们下面就来去接收一下啊那接收的话呢其实呢你不用再去重新创建类了啊直接还是用当前的这个auto review是article listener这个呢是之前
[00:59] 自媒体端的这种监听是吧可以打开大家看一看啊咱们呢还是用当前的这个方法那哪一块需要改一改呢或者加什么东西嘛其实呢这是有一个类型的咱们自媒体呢是当前微微地儿啊当然这个爬虫的话咱们是caller所以说呢这时候你这个类型判断的不一样他就会去审核不同的文章信息所以说你在这儿他去加一个erse啊if然后呢就是上面这个
[01:30] 说type等于color改一改啊点color就是color的话呢这时候呢你拿到的还是文章的ID没错而这个审核的就是谁呀是爬虫文章的信息这个review也不是它了啊所以说你把它给删了这时候呢你在上面去入一个刚才爬虫的自动审核serviceprivateall reviewcaller article Service就它入进来
[02:03] 然后你就用它的一个方法R就是第一个还是当前的文章的IDAPR article id这个咱们需要去抛一个异常咱们这样咱们捕获一下好try cache一下好吧这样的话咱们就算是整合了这个代码咱们就写完了然后下面咱们就来去测试一下测试的话怎么去测
[02:34] 就正常的话呢你需要在这去接收消息对吧你需要在这啊先去启动当前的项目比如说我右键debug启动当前的项目然后呢我在这一端在caller这一端呢去爬虫或者说去启动启动完之后呢它会自动去爬去文章然后呢是一边采集一边审核这样就可以了但这是正式上线的时候是这么这么走啊没有问题啊那是这么个流程那现在啊咱们就做简单点
[03:03] 咱们就干嘛呢就在这去发一段消息让他去接收看看到底能不能走到这就可以好吧这时候呢我在这去打个断点好那我现在呢想让这一端的去发消息怎么发呢好咱们可以去找下咱们之前的代码啊找一找走咱们之前去发消息是在哪知道吗在这pass里边有一个叫做pass那processor里边有个pass啊有一个mpl里边有个colorhtml pass配合来好
[03:34] 打开它之后呢你看其实其实我已经之前打开过啊就是发送消息你需要去审核文章咱们可以把它考出来好点呢考到一个测试环境里边啊嗯就到这吧好吧把这个把这个方法咱们就给它替换掉啊这样好吧嗯把它稍微改改啊啊这个log咱们也不要了啊这卡不卡center没有咱们就在这去注入一个autowire卡卡center好吧
[04:14] 好 注进来之后呢 这缺了个ID这个ID呢 很好找咱们就直接在数据库中去找一条就可以了啊好 找到咱们的数据库稍等CR News咱们就找第一条吧 好吧这个好像是之前测过是吧咱们换一条吧好 换这个吧 35182看看这个数据是不是1状态是不是1状态的确是1 没问题吧
[04:49] 好那这时候呢咱们就可以去拿到当前这个IP一直啊直接就放到这就可以了这时候呢你就可以去直接发送消息看看能不能直接到这好这个断电我已经打了啊我我现在呢就要去发送消息了走稍等正在正在加载环境啊这个启动的时候也没有出错吧看这个启动的时候没有问题啊好稍等啊正在加载环境看看有没有看看会不会出问题
[05:39] 好嘞来看一下啊当前到这了是吧这样咱们就先给它过掉啊你看啊现在你看接收到的消息断点在哪啊断点是不是在admin端的auto review article listener啊好往下走啊看看这个ID能不能拿到走走走这个ID的话咱们可以看一眼也行35182没问题吧OK啊的确是消息35182啊然后下面呢这个例行的话咱们看是谁啊
[06:11] 我先走你看这类型类型是不是callerOK啊那这时候呢他就会去执行这执行这的话他就会去审核咱们的文章信息没问题吧就会把35182传到传到当前这个方法里边就会去审核了咱们直接放行看看这个当前的这个日就可以了你看是不是要去保持数据是吧审核流程结束好吧行那这个测试啊咱们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Kafka 的文章自动审核系统，包括消息监听器、测试用例、代理IP更新机制以及数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 显示 IntelliJ IDEA 中的项目结构，选中了 `heima-leadnews-admin` 模块。
- 编辑器中显示 `ReviewArticleTest.java` 文件，其中包含一个测试方法 `testReviewCrawler`，调用 `reviewCrawlerArticleService.autoReviewArticleByCrawler(35181)`。

画面2：
- 显示 `AutoReviewArticleListener.java` 文件。
- 代码中定义了 `@Autowired` 的 `ObjectMapper Mapper` 和 `ReviewMediaArticleService`。
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
private ObjectMapper Mapper;
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
        SubmitArticleAuthMessage message = Mapper.readValue(value, SubmitArticleAuthMessage.class);
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
private ObjectMapper Mapper;
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
        SubmitArticleAuthMessage message = Mapper.readValue(value, SubmitArticleAuthMessage.class);
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
    SubmitArticleAuthMessage message = Mapper.readValue(value, SubmitArticleAuthMessage.class);
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
    SubmitArticleAuthMessage message = Mapper.readValue(value, SubmitArticleAuthMessage.class);
    if

