# 画面线理解：22_爬虫文章审核_整体测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\22_爬虫文章审核_整体测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:00, 01:58, 02:33, 02:58, 03:44, 04:20, 04:59, 05:26, 06:25, 06:55, 07:35, 08:13, 08:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:29:49

1) 这一组画面整体在讲什么（一句话）：
演示一个文章自动审核服务的测试与实现过程，包括从测试用例触发、内容相似度比对、图片审核到最终数据持久化入库的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示测试类 ReviewArticleTest 中的 testReviewCrawler 方法调用，以及服务类 ReviewCrawlerArticleServiceImpl 中的 autoReviewArticleByCrawler 方法。日志显示数据库连接池初始化和连接创建。
画面2：在 ReviewArticleTest.java 中，光标位于 testReviewCrawler 方法的定义处，准备执行测试。
画面3：执行 testReviewCrawler 方法，日志显示测试成功完成。
画面4：在调试模式下，查看 CNews 对象的属性，包括 id=35181，title="CSDN 公司公告"，content 为文章内容，status 为 0。
画面5：在 ReviewCrawlerArticleServiceImpl.java 中，查看 autoReviewArticleByCrawler 方法，其中包含内容相似度计算逻辑。
画面6：查看 handlerTextAndImages 方法，用于处理 JSON 数组中的文本和图片数据。
画面7：查看内容相似度计算逻辑，若相似度小于 0 则返回，否则继续执行文本审核。
画面8：查看图片审核逻辑，使用阿里云图片审核服务，若审核失败则更新状态并返回。
画面9：查看 saveArticleContent 方法，将文章内容保存到数据库。
画面10：查看 saveIndexEntity 方法，将文章索引信息保存到数据库。
画面11：在 Navicat for MySQL 中，查看 ap_article 表的数据，显示文章内容和元数据。
画面12：在 Navicat for MySQL 中，执行 DELETE 语句，删除 id 为 25103 的记录。
画面13：在 Navicat for MySQL 中，执行 SELECT 语句，查询 ap_article 表中的文章数据。
画面14：在 Navicat for MySQL 中，查看 ap_article 表中包含文章标题、内容、标签等字段的数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public void testReviewCrawler() throws Exception {
    reviewCrawlerArticleService.autoReviewArticleByCrawler(cNewsId: 35181);
}
```
画面2：
```java
public void testReviewCrawler() throws Exception {
```
画面3：
```java
public void testReviewCrawler() throws Exception {
    reviewCrawlerArticleService.autoReviewArticleByCrawler(cNewsId: 35181);
}
```
画面4：
```java
cNews = new CNews();
cNews.setId(35181);
cNews.setTitle("CSDN 公司公告");
cNews.setStatus((byte) 0);
cNews.setChannelId(2101);
cNews.setAuthorId(4100);
cNews.setOriginalTime(new Date());
cNews.setPublishTime(new Date());
cNews.setUpdateTime(new Date());
cNews.setLabels(new ArrayList<>());
cNews.setImages(new ArrayList<>());
cNews.setContent("H41AAAAAAAAAA..."); // 内容省略
```
画面5：
```java
long currentTimeMillis = System.currentTimeMillis();
if (null == cNews) {
    log.info("文章内容为空");
    return;
}
double degree = Compute.SimilarDegree(content, title);
if (degree < 0) {
    updateNews(cNews, messages: "文章和标题不匹配");
    return;
}
log.info("开始文本内容的审核");
```
画面6：
```java
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    for (Object obj : jsonArray) {
        JSONObject jsonObject = (JSONObject) obj;
        String type = (String) jsonObject.get("type");
        if ("image".equals(type)) {
            String value = (String) jsonObject.get("value");
            images.add(value);
        }
        if ("text".equals(type)) {
            String value = (String) jsonObject.get("value");
            sb.append(value);
        }
    }
}
```
画面7：
```java
double degree = Compute.SimilarDegree(content, title);
if (degree < 0) {
    updateNews(cNews, messages: "文章和标题不匹配");
    return;
}
log.info("开始文本内容的审核");
```
画面8：
```java
String imageResponse = aliYunImageScanRequest.imageScanRequest(images);
if (null == imageResponse || !imageResponse.equals("pass")) {
    updateNews(cNews, messages: "图片内容审核失败");
    return;
}
```
画面9：
```java
try {
    saveArticleContent(content, apArticle);
    createIndex(apArticle);
} catch (Exception e) {
    e.printStackTrace();
}
```
画面10：
```java
private IndexEntity savedIndexEntity(ApArticle apArticle, CNews cNews) {
    IndexEntity indexEntity = new IndexEntity();
    indexEntity.setId(new Long(apArticle.getId()));
    indexEntity.setContent(cNews.getContent());
    indexEntity.setStatus(new Long(value: 1));
    indexEntity.setTitle(cNews.getTitle());
    indexEntity.setPublishTime(new Date());
    if (apArticle.getChannelId() != null) {
        indexEntity.setChannelId(new Long(apArticle.getChannelId()));
    }
    return indexEntity;
}
```
画面11：
```sql
SELECT * FROM ap_article LIMIT 0, 1000;
```
画面12：
```sql
DELETE FROM ap_article WHERE id = 25103;
```
画面13：
```sql
SELECT * FROM ap_article LIMIT 0, 1000;
```
画面14：
```sql
SELECT * FROM ap_article LIMIT 0, 1000;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
