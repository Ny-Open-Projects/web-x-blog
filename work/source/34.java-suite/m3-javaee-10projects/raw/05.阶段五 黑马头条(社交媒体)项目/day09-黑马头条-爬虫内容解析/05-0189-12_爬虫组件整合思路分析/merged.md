# 12_爬虫组件整合思路分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\12_爬虫组件整合思路分析【海量资源尽在 666java.com】.mp4
- 时长 5分16秒（音频 316s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续往下讲那关于文档处理这一块呢咱们这个还没有讲完还有最后一个内容就是说这块呢需要去抽出抽出来一个方法这方法方法呢就是来去编写咱们的核心逻辑就是process那这个单转呢是在当前的哪个当前的这个Obstract Color Page Processor就是这个抽象那种抽象里找到咱们的这个process然后是它
[00:26] 之前咱们在说的时候其实这块内容是空的我是拷贝过来的咱们可以把它给删了之后可以重新去说一说这个是该怎么去写其实它就是去调用了各个类的什么各个类的什么当前的handle方法handle方法那咱们写一下首先你要在这去设置一个color page processor manager就是刚刚咱们设置这个管理器
[00:53] 那管理器啊然后这里边呢其实大部分的代码呢其实都是围绕当前一个叫colorpitchprocessor然后是按进去点什么呢有个handle然后你把pitch装进去其实这个代码就算是写完了写完呢咱们下面呢就可以去做一些这种注释是吧也就是说可以去记录一些日志啊我写呢首先呢咱们也可以去首先设置一个拿到一个时间
[01:22] 这个时间呢,我们经常拿啊,R,ArenderedType,是吧然后最终呢,是拿到一个时间然后下面呢,咱们可以拿到它的类型这类型的话呢,其实还是之前那种方法,ColorHairPort.getHandleType然后呢,你就可以去,这只点,getRequest就可以了,好吧最终就拿到了当前一个HandleType这时候呢,咱们就可以去记录当前的东西,R,Info
[01:54] 开始解析页面数据页面然后这是什么这是URL是吧下面还有啥呢还有是handle type这个呢其实咱们已经拿到了一个呢就是当前的page.getURL是吧然后第二个呢就是handle type
[02:24] 下面呢如果说它完成之后呢咱们可以再去加一个日志.loginfo这里边咱们也可以设置说解析数据页面完成然后是ur啥handle type都要去设啥ur然后是handle type最终的还有一个号识号识冒号怎么用英文的啊
[02:58] 设完之后呢这儿你就可以去写了还是配置.geturl是吧然后第二个呢是handletype第三个呢第三个就是当前的systemsister current time billions减去谁啊减去当前的这个就可以了那这样的话咱们这个数据啊或者说当前的方法咱们就算是补充完整了这时候你要注意啊你要去注入当前的一个管理器
[03:27] 刚刚编写那个管理器那这个说完之后啊这说完之后呢咱们算是收尾也算是结束了其实呢咱们写了那么长时间一直没有测试啊可能有的学员可能心里就犯题误那这些东西写的到底对不对啊所以说呢咱们下面呢就来去做一个整合做整合之前呢这个整合呢其实也只是能测试一部分因为咱们目前所写完的呢有哪些呢当前的一个downloader还有什么orange是吧还有一个processor
[03:57] 其实就是下载和解析但是并没有去进行比如说咱们后期还有还会设置拍虫啊比如说咱们要去吃酒化的数据库啊是吧像这些像这些次呢咱们的后期都会去做但是呢咱们现在啊先去进行一个测试然后测试完之后呢如果说这都没问题啊测试完之后如果说这些都没问题呢咱们再进行下一步的操作好吧行那这个啊这个整合呢其实下面都已经写了啊
[04:24] 它呢主要呢就是当基于当前这个类那这个类呢其实就是啊这里呢其实就是相当于我们定义了webmagic的一些组件组件的话你看里边有解析是吧有piple是吧还有什么scandal还有什么dialog是吧像这些呢其实都是webmagic的一些组件啊咱们呢是都把它封装到这个里边之后呢咱们再去一步一步去执行这个执行的话是有顺序的
[04:54] 是有顺序的先去下载然后再去解析然后最终的是去重然后再然后呢咱们就可以去持久化可以去持久化好吧行那这个流程咱们大概也算是回顾了一下下面咱们就来去写或者编写当前一个代码然后去整合这些组件然后去测试好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在爬虫框架中实现页面处理器（PageProcessor）的逻辑，包括获取页面处理类型、记录处理耗时、调用处理器管理器处理页面以及记录处理完成日志。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，选中了 `AbstractCrawlerPageProcessor.java` 文件。
画面2：在 `process` 方法中，记录开始处理页面的日志，调用 `crawlerPageProcessorManager.handle(page)`。
画面3：在 `process` 方法中，选中了 `crawlerPageProcessorManager.handle(page)` 这行代码。
画面4：在 `process` 方法中，选中了 `crawlerPageProcessorManager.handle(page)` 这行代码。
画面5：在 `process` 方法中，选中了 `System.currentTimeMillis()` 这行代码。
画面6：在 `process` 方法中，选中了 `crawlerHelper.getHandleType(page.getRequest())` 这行代码。
画面7：在 `process` 方法中，选中了 `Log.info(...)` 这行代码。
画面8：在 `process` 方法中，选中了 `Log.info(...)` 这行代码。
画面9：在 `process` 方法中，选中了 `Log.info(marker, ...)` 这行代码，其中 `marker` 是 `PageProcessor` 类型。
画面10：在 `process` 方法中，选中了 `Log.info(marker, ...)` 这行代码，其中 `marker` 是 `PageProcessor` 类型。
画面11：在 `process` 方法中，选中了 `Log.info(...)` 这行代码。
画面12：在 `process` 方法中，选中了 `Log.info(...)` 这行代码。
画面13：切换到 `CrawlerComponent` 类的代码，显示了 `pipelineList` 和 `scheduler` 等成员变量。
画面14：切换到 `CrawlerComponent` 类的代码，显示了 `pipelineList` 和 `scheduler` 等成员变量。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
public void process(Page page) {
    long currentTimeMillis = System.currentTimeMillis();
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    Log.info("开始解析数据页面, url: {}, handleType: {}", page.getUrl(), handleType);
    crawlerPageProcessorManager.handle(page);
}
```

画面9：
```java
Log.info(marker, "解析数据页面完成. url: {}, handleType: {}, 耗时: {}", page.getUrl(), handleType, System.currentTimeMillis() - currentTimeMillis);
```

画面13：
```java
public class CrawlerComponent implements Serializable {
    // 页面处理类
    private PageProcessor pageProcessor;
    // pipelineList 处理
    private List<Pipeline> pipelineList = new ArrayList<Pipeline>();
    // 调度组件
    private Scheduler scheduler;
    // 下载组件
    private Downloader downloader;

    public void addPipeline(Pipeline pipeline) {
        pipelineList.add(pipeline);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

