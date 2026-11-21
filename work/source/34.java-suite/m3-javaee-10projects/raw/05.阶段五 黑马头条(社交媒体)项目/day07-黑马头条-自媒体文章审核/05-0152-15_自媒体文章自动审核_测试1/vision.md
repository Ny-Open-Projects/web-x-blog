# 画面线理解：15_自媒体文章自动审核_测试1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\15_自媒体文章自动审核_测试1【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:25, 02:44, 03:50, 05:06, 06:06, 07:45, 08:22, 09:16, 10:01, 10:37, 11:46, 12:30, 13:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:26:27

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现文章内容的自动审核功能，包括文本相似度计算、图片审核、作者关联、文章内容与配置信息的持久化等核心逻辑，并通过单元测试验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 项目结构：展示 `heima-leadnews-admin` 项目，选中 `ReviewMediaArticleServiceImpl.java`。
- 代码：展示审核服务类中处理文本内容的逻辑，包括调用阿里云文本审核接口，根据返回结果更新数据库状态。
  ```java
  try {
      String response = aliYunTextScanRequest.textScanRequest(sb.toString(), 3);
      if ("review".equals(response)) { // 审核通过
          updateValues(wmNews, (short)3, message: "需要人工审核");
          return;
      }
      if ("block".equals(response)) { // 审核失败
          updateValues(wmNews, (short)2, message: "文本内容审核失败");
          return;
      }
      if ("review".equals(response)) { // 审核通过
          updateValues(wmNews, (short)3, message: "需要人工审核");
      }
  ```

画面 2：
- 代码：展示测试类 `ReviewArticleTest` 中的 `@RunWith` 注解和 `@Test` 注解，以及 `testReview()` 方法的定义。
  ```java
  @RunWith(SpringRunner.class)
  @SpringBootTest
  @Test
  public void testReview() {
  ```

画面 3：
- 代码：展示 `ReviewMediaArticleServiceImpl` 类中 `handlerTextAndImages` 方法的实现，用于解析 JSON 数组中的图片和文本内容。
  ```java
  private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
      for (Object ob : jsonArray) {
          JSONObject jsonOb = (JSONObject) ob;
          String type = (String) jsonOb.get("type");
          if ("image".equals(type)) {
              String value = (String) jsonOb.get("value");
              images.add(value);
          }
          if ("text".equals(type)) {
              sb.append(jsonOb.get("value"));
          }
      }
  }
  ```

画面 4：
- 代码：展示测试类中调用 `reviewMediaArticleService.autoReviewArticle(Media newsId: 6110)` 方法。
- 控制台：显示测试执行日志，包括 Spring Boot 启动、数据源初始化等信息。

画面 5：
- 代码：展示 `ReviewMediaArticleServiceImpl` 类中计算文本相似度的逻辑。
  ```java
  String content = wmNews.getContent(); // content: "[\"type\": \"text\", \"value\": \"3333333333\"]"
  String title = wmNews.getTitle(); // title: "22222"
  double degree = Compute.SimilarDegree(content, title); // degree: 0.01205803252411766
  if (degree == 0) {
      updateValues(wmNews, (short)2, message: "文章标题与内容不匹配");
      return;
  }
  ```

画面 6：
- 数据库：展示 Navicat for MySQL 中 `wm_news` 表的数据，其中 `id=6110` 的记录 `status` 为 1（待审核）。
- SQL：显示执行的 SQL 语句 `UPDATE wm_news SET status = '1' WHERE (id = 6110) AND (enable = '1')`。

画面 7：
- 代码：展示 `ReviewMediaArticleServiceImpl` 类中获取用户和作者信息的逻辑。
  ```java
  if (wmNews.getUserId() != null) {
      WmUser wmUser = wmUserMapper.selectById(wmNews.getUserId());
      if (wmUser != null && wmUser.getHead() != null) {
          apAuthor = apAuthorMapper.selectByAuthorName(wmUser.getHead());
          if (apAuthor == null) {
              apAuthor = new ApAuthor();
              apAuthor.setUserId(wmNews.getUserId());
              apAuthor.setCreatedTime(new Date());
          }
      }
  }
  ```

画面 8：
- 代码：展示 `ReviewMediaArticleServiceImpl` 类中设置文章图片 URL 并插入文章内容的逻辑。
  ```java
  sb.append(fileServerUrl);
  sb.append(split[i]);
  apArticle.setImages(sb.toString());
  apArticleMapper.insert(apArticle);
  ApArticleContent apArticleContent = new ApArticleContent();
  apArticleContent.setArticleId(apArticle.getId());
  apArticleContent.setContent(ComputeUtils.gzipUtils.getGzipContent());
  apArticleContentMapper.insert(apArticleContent);
  ```

画面 9：
- 代码：展示 `ReviewMediaArticleServiceImpl` 类中设置文章配置信息并插入的逻辑。
  ```java
  ApArticleConfig apArticleConfig = new ApArticleConfig();
  apArticleConfig.setArticleId(apArticle.getId());
  apArticleConfig.setComment(true);
  apArticleConfig.setLike(false);
  apArticleConfig.setFollow(false);
  apArticleConfigMapper.insert(apArticleConfig);
  ```

画面 10：
- 代码：展示测试类 `ReviewArticleTest` 中的 `testReview()` 方法，调用 `reviewMediaArticleService.autoReviewArticle(Media newsId: 6110)`。
- 控制台：显示测试执行成功。

画面 11：
- 代码：展示 `ReviewMediaArticleServiceImpl` 类中设置文章索引信息并插入的逻辑。
  ```java
  EsIndexEntity esIndexEntity = new EsIndexEntity();
  esIndexEntity.setArticleId(apArticle.getId());
  esIndexEntity.setChannelId(new Long(channelId));
  esIndexEntity.setContent(wmNews.getContent());
  esIndexEntity.setPublishTime(new Date());
  esIndexEntity.setStatus(new Long(1));
  esIndexEntity.setTitle(wmNews.getTitle());
  if (wmNews.getUserId() != null) {
      esIndexEntity.setUserId(wmNews.getUserId());
  }
  ```

画面 12：
- 代码：展示 `ReviewMediaArticleServiceImpl` 类中设置文章索引信息并插入的逻辑。
  ```java
  EsIndexEntity esIndexEntity = new EsIndexEntity();
  esIndexEntity.setArticleId(apArticle.getId());
  esIndexEntity.setChannelId(new Long(channelId));
  esIndexEntity.setContent(wmNews.getContent());
  esIndexEntity.setPublishTime(new Date());
  esIndexEntity.setStatus(new Long(1));
  esIndexEntity.setTitle(wmNews.getTitle());
  if (wmNews.getUserId() != null) {
      esIndexEntity.setUserId(wmNews.getUserId());
  }
  ```

画面 13：
- 数据库：展示 Navicat for MySQL 中 `wm_news` 表的数据，其中 `id=6110` 的记录 `status` 为 1（待审核）。
- SQL：显示执行的 SQL 语句 `UPDATE wm_news SET status = '1' WHERE (id = 6110) AND (enable = '1')`。

画面 14：
- 数据库：展示 Navicat for MySQL 中 `wm_article` 表的数据，其中 `id=6110` 的记录 `status` 为 9（审核成功）。
- SQL：显示执行的 SQL 语句 `SELECT * FROM wm_article LIMIT 0, 1000`。
