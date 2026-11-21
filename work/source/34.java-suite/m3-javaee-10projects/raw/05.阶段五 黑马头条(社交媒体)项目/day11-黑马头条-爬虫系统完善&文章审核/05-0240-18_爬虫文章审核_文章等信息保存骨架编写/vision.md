# 画面线理解：18_爬虫文章审核_文章等信息保存骨架编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\18_爬虫文章审核_文章等信息保存骨架编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:36, 00:53, 01:13, 01:25, 01:52, 02:37, 03:18, 03:58, 04:11, 04:35, 05:34, 06:09, 06:44, 07:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:27:04

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中实现文章审核流程，包括文本和图片内容的审核、作者与频道信息的关联、以及文章内容的保存。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 001: 展示 ReviewCrawlerArticleService 类中处理文章审核的逻辑，包括文本和图片审核的条件判断。
画面 002: 展示 if (null != cNews) 条件判断，用于检查文章对象是否为空。
画面 003: 展示自动审核流程的入口方法 autoReviewArticleByCrawler，包含日志记录和内容获取。
画面 004: 展示图片审核失败时的处理逻辑，包括判断图片响应是否为 "pass"。
画面 005: 展示根据频道 ID 查询频道信息的代码，使用 adChannelMapper。
画面 006: 展示保存文章内容的 SQL 语句，包括插入文章表和更新文章状态。
画面 007: 展示保存作者信息的方法 saveAuthor，用于创建或更新作者。
画面 008: 展示保存文章信息的方法 saveArticleByCrawler，包含参数和注释。
画面 009: 展示保存文章标签的方法 saveArticleLabel，用于关联文章与标签。
画面 010: 展示保存文章配置的方法 saveArticleConfig，用于设置文章的配置信息。
画面 011: 展示保存文章内容的方法 saveArticleContent，用于存储文章的文本内容。
画面 012: 展示保存文章标签的方法 saveArticleLabel，用于关联文章与标签。
画面 013: 展示保存文章配置的方法 saveArticleConfig，用于设置文章的配置信息。
画面 014: 展示保存文章内容的方法 saveArticleContent，用于存储文章的文本内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 003:
```java
@Override
public void autoReviewArticleByCrawler(CNews cNews) throws Exception {
    long currentTimeMillis = System.currentTimeMillis();
    log.info("开始自动审核流程");
    if (null != cNews) {
        String content = cNews.getUnCompressContent();
```

画面 004:
```java
if (null != imageResponse || !imageResponse.equals("pass")) {
    updateNews(cNews, message: "图片内容审核失败");
}
```

画面 006:
```sql
INSERT INTO article (channel_id, title, content, author_id, status, create_time, update_time)
VALUES (?, ?, ?, ?, ?, ?, ?);

UPDATE article SET status = ? WHERE id = ?;
```

画面 007:
```java
private ApAuthor saveAuthor(CNews cNews) {
    // 创建作者
    ApAuthor apauthor = new ApAuthor();
    apauthor.setChannelId(cNews.getChannelId());
    apauthor.setAuthorName(cNews.getAuthorName());
    apauthor.setAuthorId(cNews.getAuthorId());
    apauthor.setAuthorType(cNews.getAuthorType());
    apauthor.setAuthorStatus(cNews.getAuthorStatus());
    apauthor.setAuthorCreateTime(cNews.getAuthorCreateTime());
    apauthor.setAuthorUpdateTime(cNews.getAuthorUpdateTime());
    apauthor.setAuthorRemark(cNews.getAuthorRemark());
    apauthor.setAuthorEmail(cNews.getAuthorEmail());
    apauthor.setAuthorPhone(cNews.getAuthorPhone());
    apauthor.setAuthorWechat(cNews.getAuthorWechat());
    apauthor.setAuthorWeibo(cNews.getAuthorWeibo());
    apauthor.setAuthorQq(cNews.getAuthorQq());
    apauthor.setAuthorWechatOpenId(cNews.getAuthorWechatOpenId());
    apauthor.setAuthorWechatUnionId(cNews.getAuthorWechatUnionId());
    apauthor.setAuthorWechatNickname(cNews.getAuthorWechatNickname());
    apauthor.setAuthorWechatHeadimgurl(cNews.getAuthorWechatHeadimgurl());
    apauthor.setAuthorWechatGender(cNews.getAuthorWechatGender());
    apauthor.setAuthorWechatProvince(cNews.getAuthorWechatProvince());
    apauthor.setAuthorWechatCity(cNews.getAuthorWechatCity());
    apauthor.setAuthorWechatCountry(cNews.getAuthorWechatCountry());
    apauthor.setAuthorWechatLanguage(cNews.getAuthorWechatLanguage());
    apauthor.setAuthorWechatDeviceId(cNews.getAuthorWechatDeviceId());
    apauthor.setAuthorWechatDeviceType(cNews.getAuthorWechatDeviceType());
    apauthor.setAuthorWechatDeviceModel(cNews.getAuthorWechatDeviceModel());
    apauthor.setAuthorWechatDeviceBrand(cNews.getAuthorWechatDeviceBrand());
    apauthor.setAuthorWechatDeviceVersion(cNews.getAuthorWechatDeviceVersion());
    apauthor.setAuthorWechatDeviceSystem(cNews.getAuthorWechatDeviceSystem());
    apauthor.setAuthorWechatDeviceSystemVersion(cNews.getAuthorWechatDeviceSystemVersion());
    apauthor.setAuthorWechatDeviceSystemName(cNews.getAuthorWechatDeviceSystemName());
    apauthor.setAuthorWechatDeviceSystemVersionName(cNews.getAuthorWechatDeviceSystemVersionName());
    apauthor.setAuthorWechatDeviceSystemVersionCode(cNews.getAuthorWechatDeviceSystemVersionCode());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechat
