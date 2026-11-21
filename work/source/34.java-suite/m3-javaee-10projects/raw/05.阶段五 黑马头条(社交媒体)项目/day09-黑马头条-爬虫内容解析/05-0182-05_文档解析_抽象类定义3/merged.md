# 05_文档解析_抽象类定义3

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\05_文档解析_抽象类定义3【海量资源尽在 666java.com】.mp4
- 时长 7分23秒（音频 444s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好继续啊刚才呢咱们是写了一个这种解析URL的方法这个URL方法解析完之后呢咱们其实还要去发请求因为这个最终的都是为了发请求的吧所以说呢咱们在这儿还要在复类中去抽取第二个方法就是去发请求的方法public void然后呢然后是叫做什么呢spider request好吧
[00:31] 这个咱们比喻上是一致的list它是一个这个其实就是url的list然后第二个是request对象这个request对象它就是webmatics还有是当前的类型.document type咱们在这可以去定义当前的一个这种说是什么添加数据到哪儿它从
[01:01] 列表你添加之前呢其实咱们可以去调用复类的一个东西咱们要去我往里边传的是一个看啥我往里边传的呢给你去看一看啊不对啊这个啊我往里边传的呢其实是一个什么list里边有个pass-item这里边呢其实这个方法组装这个方法其实咱们之前是学过的啊或者是用过的意思啊他呢就是咱们要去扭出来
[01:36] 最终呢其实你需要做的事呢就是从当前这个URL的list集合中去寄出了URL然后是保存成这个list集合就可以了好吧那咱们呢现在呢就往里边去保存可以把它呢直接装进去一会儿呢咱们就往这里边去装出去就可以了咱们可以在这去做循环首先呢咱们这是一个当前的URList并且呢
[02:05] 是 urlist.list.empty 咱们可以在前面加个费当这个空的时候呢咱们就可以做循环了urlist.for那这个咱们就可以去往里边去加入了那加入之前呢这个东西呢咱们需要去设置可以直接用它的一个子类去做子类其实它这里边主要设置一个urlist.empty
[02:38] 好啊哦又有一个caller pass item然后呢是caller pass itemcaller.seturlurl是谁啊其实就是s就是s啊这个我们可以给它改一改改成url好这个就是url下面呢其实这里边还有一个咱们需要去用啊这个呢咱们需要去用到前的handler type
[03:11] 这个hander type该怎么设呢?
[03:15] 你看啊color pass item.set handler type这个type怎么弄呢?
[03:25] 其实呢咱们可以输入在这儿啊去输入一个当前的不用输入啊用一个工具类去造就可以了咱们用哪个工具类呢?
[03:36] 咱们之前用过叫color caw area help.get.
[03:43] 我们是有一个叫getHandler没有吗那这时候呢咱们需要去注入了需要注入啊上面去注入一个private caller helper就是caller helper然后呢碰它点前的getHandler type然后最终呢咱们就可以呢去拿到了前面这个但这里面需要去request对象啊咱们把这个request对象放进去就可以了啊
[04:19] 然后下面还有一个就是咱们还要去设置一个类型.set.document.type这个就是document.type好了那这个咱们就算是设置完了我给你最终是拿到的内幕那这个就算是设置完了然而你需要把当前这个东西装入到当前这个集合中.add.ad.对象装进去那这个咱们就算是演习完了
[04:52] 看啊这还少了东西啊这加一个二图院这样的话咱们就算是设置完了啊那这个方法咱们设置完之后咱们当前的这个类啊这个类呢其实呢写的差不多了只是抽取了一些公共的方法那这时候咱们还有一些真正处理的工作需要在这去定义那让当前的子类呢去实现不同的东西所以说咱们在这还要再去
[05:21] 定义一些抽象的方法让子类去实现我们在这儿去定义的第一个就是要去处理前的页面我们是设一个abstract然后咱们是void handle这是写错了是吧void handlehandle page好吧咱们传的就是这个page就是一个pagepage的话其实也是谁都对象
[05:54] 这是webmagic的对象这是一个处理页面处理页面好这是一个然后再往下咱们还要再去设置第二个public public-struct这时候咱们可以去设置一个boot我们看一下说你是否需要啥需要当前的handle type好这个咱们也可以去传一个handle type
[06:29] 这个是写下是否需要处理类型再往下还有一个就是跟那个类似然后是普尔类型然后这是呢This need document ducumeng type这个传的其实也是一个type好嘞那这个咱们写下注释吧这是什么
[07:07] 是否需要文档类型那目前的话呢咱们就算是所有的关于当前的这个子类啊副类啊咱们已经设置完了咱们一会儿呢下面就分别的去写它的子类

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 Java 项目中，通过 IDE 编辑器逐步实现一个抽象爬虫处理器类（AbstractCrawlerPageProcessor）的 `addSpiderRequest` 方法，用于将解析出的 URL 转换为爬虫请求对象并添加到请求队列中。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 `AbstractCrawlerPageProcessor.java` 文件中 `helpParseRuleList` 方法的实现，用于解析页面内容并提取 URL 列表。
画面 2: 选中 `addSpiderRequest` 方法的参数列表，准备编写方法实现。
画面 3: 在 `addSpiderRequest` 方法中，定义了方法参数：`urlList`, `request`, `documentType`。
画面 4: 在方法内创建 `List<ParselItem>` 对象 `parseItemList`。
画面 5: 添加对 `urlList` 是否为空的判断，如果为空则直接返回。
画面 6: 在 `urlList` 不为空时，开始遍历 URL 列表。
画面 7: 为每个 URL 创建 `CrawlerParseItem` 对象，并调用 `setUrl` 方法设置 URL。
画面 8: 调用 `crawlerHelper.getHandleType(request)` 获取处理类型并设置给 `crawlerParseItem`。
画面 9: 调用 `crawlerHelper.getDocumentType(request)` 获取文档类型并设置给 `crawlerParseItem`。
画面 10: 设置 `crawlerParseItem` 的文档类型为 `documentType`。
画面 11: 将 `crawlerParseItem` 添加到 `parseItemList` 列表中。
画面 12: 调用 `addSpiderRequest(parseItemList)` 方法将列表中的请求添加到队列。
画面 13: 展示 `handlePage` 抽象方法的定义。
画面 14: 展示 `isNeedHandleType` 和 `isNeedDocumentType` 两个抽象方法的定义。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public List<String> getHelpList(List<ParselRule> helpParseRuleList) {
    List<String> helpList = new ArrayList<>();
    for (ParselRule parseRule : helpParseRuleList) {
        List<String> urlLinks = ParseRuleUtils.getUrls(parseRule.getParseContentList());
        helpList.addAll(urlLinks);
    }
    return helpList;
}
```

画面 2:
```java
public void addSpiderRequest(List<String> urlList, Request request, CrawlerEnum DocumentType documentType) {
```

画面 3:
```java
public void addSpiderRequest(List<String> urlList, Request request, CrawlerEnum DocumentType documentType) {
    // 添加爬虫请求到列表
    @Param urlList
    @Param request
    @Param documentType
```

画面 4:
```java
List<ParselItem> parseItemList = new ArrayList<>();
```

画面 5:
```java
if (!urlList.isEmpty()) {
    urlList
}
```

画面 6:
```java
CrawlerParseItem crawlerParseItem = new CrawlerParseItem();
crawlerParseItem.setUrl(url);
```

画面 7:
```java
crawlerParseItem.setHandleType(crawlerHelper.getHandleType(request));
```

画面 8:
```java
crawlerParseItem.setDocumentType(crawlerHelper.getDocumentType(request));
```

画面 9:
```java
crawlerParseItem.setDocumentType(documentType);
```

画面 10:
```java
parseItemList.add(crawlerParseItem);
```

画面 11:
```java
private CrawlerHelper crawlerHelper;
```

画面 12:
```java
public abstract void handlePage(Page page);
```

画面 13:
```java
public abstract boolean isNeedHandleType(String handleType);
```

画面 14:
```java
public abstract boolean isNeedDocumentType(String documentType);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

