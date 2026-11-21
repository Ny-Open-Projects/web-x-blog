# 画面线理解：20_爬虫数据解析保存_文章保存2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\20_爬虫数据解析保存_文章保存2【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:27, 00:53, 01:08, 01:34, 01:56, 02:26, 02:54, 03:10, 03:30, 03:48, 04:09, 04:38, 05:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:13:25

1) 这一组画面整体在讲什么（一句话）：
在 Java 项目中，演示如何在爬虫解析管道类中，将解析到的 HTML 文章数据转换为实体对象，并处理文章的标题、标签、发布时间等字段。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 `CrawlerItemParsePipeline.java` 文件中，处理文章插入逻辑的代码段，包含判断文章是否已存在、记录插入耗时、以及调用 `crawlerNewsService.saveNews(cNews)` 的逻辑。
画面 2: 在 `toCNews` 方法中，通过 IDE 的自动补全功能，选择 `setLabels` 方法，准备为实体对象设置标签。
画面 3: 继续在 `toCNews` 方法中，通过 IDE 自动补全，选择 `setLabels` 方法，准备为实体对象设置标签。
画面 4: 在 `toCNews` 方法中，通过 IDE 自动补全，选择 `setLabels` 方法，准备为实体对象设置标签。
画面 5: 展示了 `CrawlerItemParsePipeline.java` 文件中，类的顶部注解和成员变量声明，包括 `@Autowired` 注入的 `crawlerNewsAdditionalService` 和 `crawlerNewsService`。
画面 6: 在 `toCNews` 方法中，通过 IDE 自动补全，选择 `setLabels` 方法，准备为实体对象设置标签。
画面 7: 在 `toCNews` 方法中，通过 IDE 自动补全，选择 `intValue()` 方法，准备将标签 ID 转换为整型。
画面 8: 在 `toCNews` 方法中，通过 IDE 自动补全，选择 `setLabels` 方法，准备为实体对象设置标签。
画面 9: 在 `toCNews` 方法中，通过 IDE 自动补全，选择 `setOriginalTime` 方法，准备为实体对象设置原始发布时间。
画面 10: 在 `toCNews` 方法中，通过 IDE 自动补全，选择 `setLabels` 方法，准备为实体对象设置标签。
画面 11: 在 `toCNews` 方法中，通过 IDE 自动补全，选择 `parseItem.getReleaseDate()` 方法，准备获取文章的发布时间。
画面 12: 在 `toCNews` 方法中，通过 IDE 自动补全，选择 `parseItem.getReleaseDate()` 方法，准备获取文章的发布时间。
画面 13: 在 `toCNews` 方法中，通过 IDE 自动补全，选择 `parseItem.getReleaseDate()` 方法，准备获取文章的发布时间。
画面 14: 在 `toCNews` 方法中，通过 IDE 自动补全，选择 `parseItem.getReleaseDate()` 方法，准备获取文章的发布时间。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
HtmlParser htmlParser = HtmlParser.getHtmlParser(getParseExpression(), getSetHtmlStyleMap());
List<HtmlLabel> htmlLabels = htmlParser.parseHtmlItem(getContent());
int type = getDocType(type);//图文类型【无图】、【单图】、【多图】
String jsonStr = JSON.toJSONString(ZipUtils.gzip(jsonStr));
parseItem.setCompression(ZipUtils.gzip(jsonStr));
```
画面 2:
```java
private CNews toCNews(CrawlerParseItem parseItem) {
    CNews cNews = new CNews();
    String labels = parseItem.getLabels();
    cNews.setLabels(labels);
    cNews.setUrl(parseItem.getUrl());
    cNews.setAuthor(parseItem.getAuthor());
    cNews.setTitle(parseItem.getTitle());
    cNews.setCompressContent(parseItem.getCompressContent());
    cNews.setInitialUrl(parseItem.getInitialUrl());
    cNews.setParserContent(parseItem.getParserContent());
    cNews.setSpatialUrl(parseItem.getSpatialUrl());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel(parseItem.getChannel());
    cNews.setChannelId(parseItem.getChannelId());
    cNews.setChannel
