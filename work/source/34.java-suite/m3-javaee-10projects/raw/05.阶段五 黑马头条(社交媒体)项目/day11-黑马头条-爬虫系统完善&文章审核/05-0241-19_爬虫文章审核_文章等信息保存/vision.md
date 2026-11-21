# 画面线理解：19_爬虫文章审核_文章等信息保存

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\19_爬虫文章审核_文章等信息保存【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:21, 02:31, 03:32, 04:39, 06:07, 07:22, 08:29, 09:31, 10:30, 12:17, 13:52, 15:11, 16:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:27:58

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中编写和调试一个用于保存文章信息的 Service 层方法，涉及作者、文章、标签和图片等实体的持久化操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 编辑器中显示 `ReviewCrawlerArticleService.java` 文件，正在定义 `saveArticleByCrawler` 方法的开头部分，光标位于 `private` 关键字后，准备输入方法体。
画面 2: 方法体中，使用 `@Autowired` 注入 `ApAuthorMapper`，并开始编写获取作者信息的逻辑，包含 `if (authorId == null || apAuthor.getId() == null)` 判断。
画面 3: 光标位于 `private void saveArticleLabel(ApArticle aparticle) {` 方法定义处，准备编写标签保存逻辑。
画面 4: 方法体中，使用 `@Autowired` 注入 `ApArticleMapper`，并开始编写设置文章属性的代码，包括 `apArticle.setAuthorId(new AuthorId(...))`。
画面 5: 继续编写 `saveArticleByCrawler` 方法，设置文章的 `channelId`, `channelName`, `id`, `cNews` 等属性。
画面 6: 编写 `if (null != images && images.size() > 0)` 条件判断，用于处理图片列表。
画面 7: 在 `if` 条件内，使用 `StringBuilder` 拼接图片 URL，并调用 `apArticle.setImages(sb.toString())`。
画面 8: 光标位于 `private void saveArticleContent(String content, ApArticle aparticle) {` 方法定义处，准备编写内容保存逻辑。
画面 9: 方法体中，使用 `@Autowired` 注入 `ApArticleConfigMapper`，并开始编写配置保存逻辑。
画面 10: 光标位于 `private void saveArticleLabel(ApArticle aparticle) {` 方法定义处，准备编写标签保存逻辑。
画面 11: 方法体中，使用 `@Autowired` 注入 `ApArticleLabelMapper`，并开始编写标签保存逻辑。
画面 12: 在 `for` 循环中，创建 `ApArticleLabel` 对象并调用 `apArticleLabelMapper.selectList()`。
画面 13: 在 `for` 循环中，调用 `apArticleLabel.setCount(apArticleLabel.getCount())`。
画面 14: 方法体中，调用 `apArticleMapper.insert(apArticle)` 并返回 `apArticle`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private ApArticle saveArticleByCrawler(List<String> images, Integer channelId, String ch
```

画面 2:
```java
@Autowired
private ApAuthorMapper apAuthorMapper;

private ApAuthor saveAuthor(Clickers cNews) {
    if (authorId == null || apAuthor.getId() == null) {
        apAuthor = new ApAuthor();
        apAuthor.setCreatedTime(new Date());
        apAuthor.setAuthorName(cNews);
    }
}
```

画面 3:
```java
private void saveArticleLabel(ApArticle aparticle) {
```

画面 4:
```java
@Autowired
private ApArticleMapper apArticleMapper;

private ApArticle saveArticleByCrawler(List<String> images, Integer channelId, String ch
```

画面 5:
```java
private ApArticle saveArticleByCrawler(List<String> images, Integer channelId, String ch
    ApArticle apArticle = new ApArticle();
    apArticle.setChannelId(channelId);
    apArticle.setChannelName(channelName);
    apArticle.setAuthorId(new Long(authorId));
    apArticle.setAuthorName(cNews.getNews());
    apArticle.setOrigin(cNews.getOrigin());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
