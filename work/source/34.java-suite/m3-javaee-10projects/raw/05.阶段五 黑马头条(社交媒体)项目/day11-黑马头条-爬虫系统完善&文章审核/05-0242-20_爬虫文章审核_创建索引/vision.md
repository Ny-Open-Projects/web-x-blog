# 画面线理解：20_爬虫文章审核_创建索引

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\20_爬虫文章审核_创建索引【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 01:18, 01:48, 02:50, 03:45, 04:23, 05:16, 06:13, 06:49, 07:31, 08:07, 08:24, 08:50, 09:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:28:35

1) 这一组画面整体在讲如何在 Java 项目中使用 Jest（Elasticsearch 客户端）为文章实体创建并更新索引。

2) 按时间顺序列出每张画面的要点：
画面 1:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  //保存标签
  saveArticleLabel(aparticle);
  //保存文章
  saveArticle(aparticle);
  //保存文章内容
  saveArticleContent(content_aparticle);
  //更改状态为 9
  ```

画面 2:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  private
  ```
  代码补全弹窗显示了 `private` 关键字的可用选项，包括 `Private`、`PrivateKey`、`PrivateClassLoader` 等。

画面 3:
- 代码位置：搜索结果页面（非代码文件）
- 代码内容：
  ```
  import
  Choose Implementation of Action (8) found:
  Refresh (io.searchbox.indices.refresh)
  Reindex (io.searchbox.indices.reindex)
  Revert (io.searchbox.indices.revert)
  RestoreSnapshot (io.searchbox.indices.snapshot)
  ScavengeStatus (io.searchbox.indices.scavenge)
  Search (io.searchbox.indices.search)
  SearchScroll (io.searchbox.indices.searchscroll)
  SearchShards (io.searchbox.indices.searchshards)
  SingleResultAbstractDocumentTargetedAction (io.searchbox.action)
  State (io.searchbox.indices.state)
  TaskInformation (io.searchbox.indices.task)
  TemplateAction (io.searchbox.indices.template)
  ```

画面 4:
- 代码位置：Elasticsearch 实体类文件
- 代码内容：
  ```java
  package com.heima.common.common.pojo;

  public class EsIndexEntity {
      private Long id;
      private String content;
      private Long channelId;
      // private Date pub_time;
      private Date publishTime;
      private Long status;
      private String title;
      private Long userId;
      private String tag;
  }
  ```

画面 5:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  private void createEsIndex(ApArticle aparticle, CNews cNews) {
      EsIndexEntity esIndexEntity = saveEsIndexEntity(aparticle, cNews);
      Index.Builder builder = new Index.Builder(esIndexEntity);
      builder.id(aparticle.getId().toString());
      // ...
  }
  ```
  代码补全弹窗显示了 `Index.Builder` 的方法，如 `id`、`type`、`index`、`refresh` 等。

画面 6:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  Index index = builder.index(ESIndexConstants.ARTICLE_INDEX).type(ESIndexConstants.DOC).build();
  jestClient.execute(index);
  ```
  代码补全弹窗显示了 `ESIndexConstants` 类中的常量，如 `ARTICLE_INDEX`、`AUTHOR_INDEX`、`USER_INDEX`、`DEFAULT_DOC`。

画面 7:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  Index index = builder.index(ESIndexConstants.ARTICLE_INDEX).type(ESIndexConstants.DOC).build();
  JestResult result = jestClient.execute(index);
  if (result != null && result.isSucceeded()) {
  ```
  代码补全弹窗显示了 `JestResult` 类的常用方法，如 `isSucceeded()`、`getErrorMessage()`。

画面 8:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  if (result != null && result.isSucceeded()) {
      throw new RuntimeException(result.getErrorMessage()) + "插入更新索引失败!";
  }
  ```
  代码补全弹窗显示了 `RuntimeException` 类的构造方法。

画面 9:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  private EsIndexEntity saveEsIndexEntity(ApArticle aparticle, CNews cNews) {
      EsIndexEntity esIndexEntity = new EsIndexEntity();
      esIndexEntity.setId(new Long(aparticle.getId()));
      // ...
  }
  ```

画面 10:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  esIndexEntity.setContent(cNews.getCompressContent());
  ```

画面 11:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  esIndexEntity.setTitle(cNews.getTitle());
  ```

画面 12:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  esIndexEntity.setStatus(cNews.getStatus());
  ```

画面 13:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  if (aparticle.getChannelId() != null) {
      esIndexEntity.setChannelId(aparticle.getChannelId());
  }
  ```

画面 14:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  @Autowired
  private JestClient jestClient;

  private void createEsIndex(ApArticle aparticle, CNews cNews) throws TOException {
      EsIndexEntity esIndexEntity = saveEsIndexEntity(aparticle, cNews);
      Index.Builder builder = new Index.Builder(esIndexEntity);
      builder.id(aparticle.getId().toString());
      builder.refresh(true);
      Index index = builder.index(ESIndexConstants.ARTICLE_INDEX).type(ESIndexConstants.DEFAULT_DOC).build();
      JestResult result = jestClient.execute(index);
      if (result != null && result.isSucceeded()) {
          throw new RuntimeException(result.getErrorMessage()) + "插入更新索引失败!";
      }
  }
  ```
